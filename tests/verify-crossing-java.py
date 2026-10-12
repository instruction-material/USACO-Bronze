"""Check the authored native roles without changing the published learner task."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import random
import re
import shlex
import shutil
import signal
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'UB-22-Why-Did-the-Cow-Cross-the-Road-Java'
REFERENCE = '789561ad2f8b8bb0761f697d95d3e70b46fb73ce8a660d112496b526846dd874'
MARKER = '        throw new UnsupportedOperationException("TASK: crossing transitions"); // ADDED'
COMPLETION = '''        int[] previous = new int[10];
        java.util.Arrays.fill(previous, -1);
        int total = 0;
        for (int[] observation : observations) {
            int index = observation[0] - 1;
            int side = observation[1];
            if (previous[index] != -1 && previous[index] != side) total++;
            previous[index] = side;
        }
        return total;'''
PROCESSES = []


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def command(args, cwd, expected=0, timeout=15):
    proc = subprocess.Popen(args, cwd=cwd, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, start_new_session=True)
    record = dict(parentTaskId=os.environ.get('CODEX_PARENT_TASK_ID', 'bronze-crossing-native'),
                  cwd=str(cwd), command=args, pid=proc.pid, startTime=now(),
                  timeoutSeconds=timeout, expectedExitCode=expected)
    try:
        out, err = proc.communicate(timeout=timeout)
    except BaseException:
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.communicate()
        record['childProcessGroupCleanup'] = True
        raise
    finally:
        record.update(endTime=now(), exitCode=proc.returncode)
        PROCESSES.append(record)
    assert proc.returncode == expected, (args, proc.returncode, err.decode(errors='replace'))
    return out, err


def oracle(rows):
    # Group chronological side sequences by cow, independent of the streaming state.
    sequences = [[side for cow, side in rows if cow == wanted] for wanted in range(1, 11)]
    return sum(sum(a != b for a, b in zip(sequence, sequence[1:])) for sequence in sequences)


def payload(rows):
    return str(len(rows)) + '\n' + ''.join(f'{cow} {side}\n' for cow, side in rows)


def compile_role(directory, javac):
    (directory / 'classes').mkdir(exist_ok=True)
    command([javac, '--release', '17', '-encoding', 'UTF-8', '-Xlint:all',
             '-Werror', '-d', 'classes', 'Main.java'], directory)


def verify(java, javac):
    before = {str(f.relative_to(FOLDER)): f.read_bytes() for f in FOLDER.rglob('*') if f.is_file()}
    reference = before['solution/Main.java'].replace(b'\r\n', b'\n')
    assert hashlib.sha256(reference).hexdigest() == REFERENCE
    source = before['starter/Main.java'].decode()
    assert source.count(MARKER) == 1 and source.encode() != reference
    assert before['starter/crossroad.in'] == before['solution/crossroad.in']
    assert before['starter/sample.expected'] == before['solution/sample.expected'] == b'3\n'
    assert before['solution/crossroad.out'].strip() == b'3'
    expected_files = {'Main.java', 'README.md', 'crossroad.in', 'sample.expected'}
    assert {f.name for f in (FOLDER / 'starter').iterdir()} == expected_files
    assert {f.name for f in (FOLDER / 'solution').iterdir()} == expected_files | {'crossroad.out'}
    for role in ['starter', 'solution']:
        text = before[role + '/README.md'].decode()
        assert all(term in text for term in ['## Contract', '## Predict and trace',
                      '## Independent checks', '## Save, compile and run', '1..100',
                      '1..10', 'sample.expected', 'entry class `Main`'])
        assert '../README' not in text
    sample = [(3, 1), (3, 0), (6, 0), (2, 1), (4, 1), (3, 0), (4, 0), (3, 1)]
    cases = [sample, [(1, 0)], [(10, 1)], [(1, 0), (1, 0)],
             [(1, 0), (1, 1)], [(10, 1), (10, 0)],
             [(1, 0), (10, 1), (1, 1), (10, 0), (1, 1)],
             [(cow, cow % 2) for cow in range(1, 11)],
             [(1, i % 2) for i in range(100)], [(10, 1)] * 100,
             [(i % 10 + 1, i // 10 % 2) for i in range(100)]]
    rng = random.Random(711)
    cases += [[(rng.randint(1, 10), rng.randint(0, 1))
               for _ in range(rng.randint(1, 100))] for _ in range(20)]
    assert oracle(sample) == 3 and oracle(cases[8]) == 99
    invalid = ['0\n', '101\n', '1\n0 1\n', '1\n11 0\n', '1\n1 2\n',
               '2\n1 0\n', '1\n1 not-a-side\n', '1\n1 0\nextra\n']
    roles = []
    with tempfile.TemporaryDirectory(prefix='bronze-crossing-') as temporary:
        root = Path(temporary)
        for role, authored in [('reference', reference.decode()), ('learner', source),
                               ('completed-learner', source.replace(MARKER, COMPLETION))]:
            directory = root / role
            directory.mkdir()
            (directory / 'Main.java').write_text(authored)
            compile_role(directory, javac)
            for rows in cases:
                (directory / 'crossroad.in').write_text(payload(rows))
                (directory / 'crossroad.out').write_text('Earlier answer\n')
                out, err = command([java, '-cp', 'classes', 'Main'], directory,
                                   expected=2 if role == 'learner' else 0)
                assert not out
                answer = (directory / 'crossroad.out').read_text()
                if role == 'learner':
                    assert b'TASK: crossing transitions' in err and answer == 'Earlier answer\n'
                else:
                    assert answer == str(oracle(rows)) + '\n'
            if role != 'reference':
                for text in invalid:
                    (directory / 'crossroad.in').write_text(text)
                    (directory / 'crossroad.out').write_text('Earlier answer\n')
                    out, err = command([java, '-cp', 'classes', 'Main'], directory, expected=1)
                    assert not out and b'IllegalArgumentException' in err
                    assert (directory / 'crossroad.out').read_text() == 'Earlier answer\n'
            roles.append(dict(role=role, independentCases=len(cases),
                              maximumObservations=100, malformedRefusals=0 if role=='reference' else len(invalid),
                              learnerRemainsUnfinished=role=='learner', previousAnswerPreserved=role=='learner'))
        guards = []
        for role in ['starter', 'solution']:
            guide = before[role+'/README.md'].decode()
            found = re.findall(r'```sh\n(.*?)\n```', guide, re.S)
            assert len(found) == 1
            guard = found[0].replace('javac --release', shlex.quote(javac)+' --release')
            guard = guard.replace('java -cp', shlex.quote(java)+' -cp')
            for variant in ['normal', 'broken-compile', 'missing-entry'] + (['wrong-oracle'] if role=='solution' else []):
                directory = root / (role+'-'+variant)
                shutil.copytree(FOLDER/role, directory)
                file = directory / 'Main.java'
                if variant == 'broken-compile': file.write_text('invalid Java\n')
                if variant == 'missing-entry': file.write_text(file.read_text().replace('class Main {', 'class AnotherEntry {', 1))
                if variant == 'wrong-oracle': (directory / 'sample.expected').write_text('Wrong answer\n')
                (directory / 'crossroad.out').write_text('Earlier answer\n')
                success = role=='solution' and variant=='normal'
                command(['/bin/sh', '-c', guard], directory,
                        expected=0 if success else 2 if role=='starter' and variant=='normal' else 1)
                answer = (directory / 'crossroad.out').read_text()
                assert answer == ('3\n' if success else 'Earlier answer\n')
                guards.append(dict(role=role, variant=variant, previousAnswerPreserved=not success))
    after = {str(f.relative_to(FOLDER)): f.read_bytes() for f in FOLDER.rglob('*') if f.is_file()}
    assert before == after
    report = dict(roles=roles, guards=guards, referenceCodePreserved=True,
                  sourceFilesUnchanged=True, completedTaskCheckedSeparately=True,
                  totalNativeProcesses=len(PROCESSES), processes=PROCESSES)
    receipt = os.environ.get('BRONZE_CROSSING_ACCEPTANCE_RECEIPT')
    if receipt: Path(receipt).write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='processes'}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--java', default='java')
    parser.add_argument('--javac', default='javac')
    args = parser.parse_args()
    verify(args.java, args.javac)
