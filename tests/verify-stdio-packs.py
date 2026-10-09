"""Verify references and distinct unfinished/completed learner stdio packs."""
from pathlib import Path
import hashlib
import itertools
import json
import os
import random
import signal
import subprocess
import sys
import time
import datetime
root = Path(__file__).resolve().parents[1]
logs = []
REFERENCE_HASHES = {'UB62-Cow-College': '0aa9e236da493fd70932e6a073880aedc35a70563b4d8d84dc9535e19e6c127e', 'UB63-Feeding-the-Cows': '6326122402bff44bdd06932d369331fcc95a0ff7eb7874d5501f2325df12ec03'}
for folder, digest in REFERENCE_HASHES.items():
    source = root / folder / 'solution/main.py'
    assert hashlib.sha256(source.read_bytes().replace(b'\r\n', b'\n')).hexdigest() == digest
    for role in ['starter', 'solution']:
        assert {p.name for p in (root / folder / role).iterdir() if p.is_file()} == {'main.py', 'sample.in', 'README.md'}
    assert (root / folder / 'starter/main.py').read_bytes() != (root / folder / 'solution/main.py').read_bytes()

def execute(folder, payload, path=None, expected_exit=0):
    path = path or root / folder / 'solution/main.py'
    start = time.monotonic()
    proc = subprocess.Popen([sys.executable, str(path)], cwd=root, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, start_new_session=True)
    row = {'parentTaskId': 'bronze-stdio-source-acceptance', 'cwd': str(root), 'command': [sys.executable, str(path)], 'pid': proc.pid, 'start': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'timeoutSeconds': 10, 'expectedExitCode': expected_exit}
    try:
        out, err = proc.communicate(payload, timeout=10)
    except subprocess.TimeoutExpired:
        os.killpg(proc.pid, signal.SIGKILL)
        proc.communicate()
        raise
    row.update(end=datetime.datetime.now(datetime.timezone.utc).isoformat(), exitCode=proc.returncode, elapsedSeconds=round(time.monotonic() - start, 4))
    logs.append(row)
    assert proc.returncode == expected_exit, (folder, err)
    if expected_exit:
        assert not out and 'NotImplementedError' in err
    return out.splitlines()

def college_oracle(values):
    # Compare observed price candidates, independently of the histogram scan.
    return min(((-price * sum((value >= price for value in values)), price) for price in set(values)))
rng = random.Random(1251)
college = [[1, 6, 4, 6], [1, 2], [1], [1000000], [7] * 12, [2, 2, 4, 4], [5, 4, 3, 2, 1], [1, 1, 1, 1000000]]
college += [[rng.randrange(1, 14) for _ in range(rng.randrange(1, 31))] for _ in range(12)]
college += [[1000000] * 100000, [500000] * 50000 + [1000000] * 50000]

def coverage(layout, k):
    # Build breed-specific reachable-position sets for arbitrary patch layouts.
    g = h = 0
    for i, ch in enumerate(layout):
        if ch == '.':
            continue
        left = max(0, i - k)
        right = min(len(layout), i + k + 1)
        mask = ((1 << (right - left)) - 1) << left
        if ch == 'G':
            g |= mask
        else:
            h |= mask
    return (g, h)
cases = []
for n in range(1, 7):
    layouts = sorted(itertools.product('.GH', repeat=n), key=lambda layout: sum((ch != '.' for ch in layout)))
    for k in range(n):
        candidates = [(sum((ch != '.' for ch in layout)), *coverage(layout, k)) for layout in layouts]
        for cows_tuple in itertools.product('GH', repeat=n):
            cows = ''.join(cows_tuple)
            g = sum((1 << i for i, ch in enumerate(cows) if ch == 'G'))
            h = ((1 << n) - 1) ^ g
            optimum = next((count for count, g_cover, h_cover in candidates if g_cover & g == g and h_cover & h == h))
            cases.append((cows, k, optimum))
assert len(cases) == 642
cases += [('GHHGG', k, count) for k, count in enumerate([5, 3, 2, 2, 2])] + [('GH', 1, 2)]
cases += [('G' * 100000, 0, 100000), ('G' * 100000, 99999, 1), ('GH' * 50000, 99999, 2), ('GH' * 50000, 0, 100000)]

def verify_native(paths):
    # Run the real stdin/stdout programs against independent optimality oracles.
    for values in college:
        revenue, tuition = college_oracle(values)
        expected = (-revenue, tuition)
        actual = execute('UB62-Cow-College', str(len(values)) + '\n' + ' '.join(map(str, values)) + '\n', paths.get('UB62-Cow-College'))
        assert len(actual) == 1 and tuple(map(int, actual[0].split())) == expected, (values[:20], actual, expected)
    for offset in range(0, len(cases), 10):
        batch = cases[offset:offset + 10]
        payload = str(len(batch)) + '\n' + ''.join((f'{len(cows)} {k}\n{cows}\n' for cows, k, _ in batch))
        actual = execute('UB63-Feeding-the-Cows', payload, paths.get('UB63-Feeding-the-Cows'))
        assert len(actual) == 2 * len(batch)
        for i, (cows, k, optimum) in enumerate(batch):
            count = int(actual[2 * i])
            layout = actual[2 * i + 1]
            assert len(layout) == len(cows) and set(layout) <= set('.GH')
            assert count == optimum == sum((ch != '.' for ch in layout)), (cows[:30], k, count, optimum)
            g_cover, h_cover = coverage(layout, k)
            assert all(((g_cover if breed == 'G' else h_cover) & 1 << j for j, breed in enumerate(cows))), (cows[:30], k, layout[:30])
COLLEGE_COMPLETION = """current_cows = 0
max_money = 0
best_tuition = 0
for tuition in range(MAX_TUITION, 0, -1):
    current_cows += tuition_to_cow[tuition]
    if tuition * current_cows >= max_money:
        max_money = tuition * current_cows
        best_tuition = tuition
return max_money, best_tuition"""
FEEDING_COMPLETION = """n = len(cows)
patches = ["."] * n
g_cover = -1
h_cover = -1
for idx, ch in enumerate(cows):
    if ch == "G" and g_cover < idx:
        if idx + k >= len(patches):
            if patches[idx] != ".":
                patches[idx - 1] = "G"
            else:
                patches[idx] = "G"
            g_cover = n
        else:
            patches[idx + k] = "G"
            g_cover = idx + 2 * k
    elif ch == "H" and h_cover < idx:
        if idx + k >= len(patches):
            if patches[idx] != ".":
                patches[idx - 1] = "H"
            else:
                patches[idx] = "H"
            h_cover = idx + k
        else:
            patches[idx + k] = "H"
            h_cover = idx + 2 * k
return patches"""

def verify():
    import tempfile
    verify_native({})
    completed = {}
    with tempfile.TemporaryDirectory(prefix='bronze-stdio-learners-') as directory:
        for folder, label, body in [('UB62-Cow-College', 'tuition scan', COLLEGE_COMPLETION), ('UB63-Feeding-the-Cows', 'patch placement', FEEDING_COMPLETION)]:
            starter = root / folder / 'starter/main.py'
            payload = (root / folder / 'starter/sample.in').read_text()
            execute(folder, payload, starter, expected_exit=1)
            source = starter.read_text()
            marker = '    raise NotImplementedError("Complete the ' + label + '")  # ADDED'
            assert source.count(marker) == 1
            prefix, suffix = source.split(marker)
            replacement = '\n'.join(('    ' + line for line in body.splitlines()))
            finished = prefix + replacement + suffix
            assert finished.startswith(prefix) and finished.endswith(suffix)
            path = Path(directory) / (folder + '.py')
            path.write_text(finished)
            completed[folder] = path
        verify_native(completed)
    report = {'cowCollegeCasesPerRole': len(college), 'feedingExhaustiveCasesPerRole': 642, 'feedingTotalCasesPerRole': len(cases), 'fullPublishedSizeCasesPerRole': 6, 'actualNativeStdinStdout': True, 'independentOptimalityOracles': True, 'untouchedStartersRemainUnfinished': True, 'completedLearnerDriversVerified': True, 'referenceCodePreserved': True, 'totalNativeProcesses': len(logs)}
    if os.environ.get('BRONZE_STDIO_ACCEPTANCE_RECEIPT'):
        Path(os.environ['BRONZE_STDIO_ACCEPTANCE_RECEIPT']).write_text(json.dumps({**report, 'processes': logs}, indent=2) + '\n')
    print(json.dumps(report))
if __name__ == '__main__':
    verify()
