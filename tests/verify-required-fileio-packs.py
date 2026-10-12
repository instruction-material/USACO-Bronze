"""Check seven native file-I/O packs against independent problem models."""
import ast
import datetime
import hashlib
import itertools
import json
import os
from pathlib import Path
import random
import shlex
import shutil
import signal
import subprocess
import sys
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
SPECS = json.loads((ROOT / 'tests/required-fileio-specs.json').read_text())
PROCESSES = []


def digest(path):
    data = path.read_bytes()
    if path.suffix in {'.py', '.md', '.in', '.out', '.expected'}:
        data = data.replace(b'\r\n', b'\n')
    return hashlib.sha256(data).hexdigest()


def execute(args, directory, expected_exit):
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc = subprocess.Popen(args, cwd=directory, stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, start_new_session=True)
    row = dict(parentTaskId=os.environ.get('CODEX_PARENT_TASK_ID', 'bronze-required-fileio'),
               cwd=str(directory), command=args, pid=proc.pid, startTime=start,
               timeoutSeconds=15, expectedExitCode=expected_exit)
    begin = time.monotonic()
    try:
        out, err = proc.communicate(timeout=15)
    except BaseException:
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            proc.communicate()
        row['childProcessGroupCleanup'] = True
        raise
    finally:
        row.update(endTime=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   exitCode=proc.returncode, elapsedSeconds=round(time.monotonic()-begin, 4))
        PROCESSES.append(row)
    assert proc.returncode == expected_exit, (args, directory, proc.returncode, err.decode()[-2000:])
    return out, err


def milk_oracle(intervals):
    merged = []
    for a, b in sorted(intervals):
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b)
        else:
            merged.append([a, b])
    covered = max(b-a for a, b in merged)
    gap = max((right[0]-left[1] for left, right in zip(merged, merged[1:])), default=0)
    return f'{covered} {gap}\n'


def transform_oracle(original, target):
    n = len(original)
    mappings = [lambda r,c:(n-1-c,r), lambda r,c:(n-1-r,n-1-c),
                lambda r,c:(c,n-1-r), lambda r,c:(r,n-1-c),
                lambda r,c:(n-1-c,n-1-r), lambda r,c:(n-1-r,c),
                lambda r,c:(c,r), lambda r,c:(r,c)]
    for category, mapping in zip([1,2,3,4,5,5,5,6], mappings):
        candidate = [''.join(original[mapping(r,c)[0]][mapping(r,c)[1]] for c in range(n)) for r in range(n)]
        if candidate == target:
            return str(category)+'\n'
    return '7\n'


def worm_oracle(points):
    # Canonical pair sets plus graph cycle detection, independent of N-step checks.
    def pairings(indices):
        if not indices:
            yield ()
            return
        for other in indices[1:]:
            rest = tuple(x for x in indices[1:] if x != other)
            for tail in pairings(rest):
                yield ((indices[0], other),)+tail
    right = []
    for x,y in points:
        candidates = [(xx,j) for j,(xx,yy) in enumerate(points) if yy==y and xx>x]
        right.append(min(candidates)[1] if candidates else None)
    total = 0
    for pairs in pairings(tuple(range(len(points)))):
        partner = dict(pairs)
        partner.update({b:a for a,b in pairs})
        cyclic = False
        for start in range(len(points)):
            seen = set()
            node = start
            while node is not None and node not in seen:
                seen.add(node)
                node = right[partner[node]]
            if node is not None:
                cyclic = True
                break
        total += cyclic
    return str(total)+'\n'


def lost_oracle(x,y):
    current, offset, walked = x, 1, 0
    while current != y:
        target = x+offset
        direction = 1 if target > current else -1
        while current != target and current != y:
            current += direction
            walked += 1
        offset *= -2
    return str(walked)+'\n'


def diamond_oracle(sizes,k):
    # Sorted windows, with an additional exhaustive subset model on tiny inputs.
    values = sorted(sizes)
    left, best = 0, 0
    for right in range(len(values)):
        while values[right]-values[left] > k:
            left += 1
        best = max(best,right-left+1)
    if len(sizes) <= 9:
        exhaustive = 0
        for mask in range(1,1 << len(sizes)):
            chosen = [value for i,value in enumerate(sizes) if mask & (1 << i)]
            if max(chosen)-min(chosen) <= k:
                exhaustive = max(exhaustive,len(chosen))
        assert best == exhaustive
    return str(best)+'\n'


def order_oracle(n,hierarchy,fixed):
    # Complete permutations, rather than the candidate-position greedy routine.
    best = n+1
    for order in itertools.permutations(range(1,n+1)):
        positions = {cow:i+1 for i,cow in enumerate(order)}
        if not all(positions[cow]==place for cow,place in fixed):
            continue
        if not all(positions[a] < positions[b] for a,b in zip(hierarchy,hierarchy[1:])):
            continue
        best = min(best,positions[1])
    assert best <= n
    return str(best)+'\n'


def family_oracle(a,b,relations):
    parent = {child:mother for mother,child in relations}
    def chain(cow):
        result = [cow]
        while result[-1] in parent:
            result.append(parent[result[-1]])
        return result
    one,two = chain(a),chain(b)
    shared = set(one) & set(two)
    if not shared:
        return 'NOT RELATED\n'
    ancestor = min(shared,key=lambda cow:one.index(cow)+two.index(cow))
    da,db = one.index(ancestor),two.index(ancestor)
    if da==db==1:
        return 'SIBLINGS\n'
    if da>1 and db>1:
        return 'COUSINS\n'
    if da > db:
        a,b,da,db = b,a,db,da
    if da==0:
        relation = 'mother' if db==1 else 'great-'*(db-2)+'grand-mother'
    else:
        relation = 'great-'*(db-2)+'aunt'
    return f'{a} is the {relation} of {b}\n'


def name(index):
    return chr(65+index//26)+chr(65+index%26)


def cases():
    rng = random.Random(20261011)
    result = {s['task']:[] for s in SPECS}
    intervals = [[(300,1000),(700,1200),(1500,2100)],[(0,1)],[(0,2),(2,5)],
                 [(4,8),(1,2)],[(2,10),(3,7)],[(0,1),(2,3)]]
    intervals += [[(a,a+rng.randrange(1,12)) for a in [rng.randrange(0,25) for _ in range(rng.randrange(1,15))]] for _ in range(15)]
    intervals += [[(0,1000000)]*5000,[(i*200,i*200+1) for i in range(5000)]]
    for values in intervals:
        result['milk2'].append((str(len(values))+'\n'+''.join(f'{a} {b}\n' for a,b in values),milk_oracle(values)))
    patterns = [(['@'],['@']),(['-'],['@']),(['@-','-@'],['@-','-@'])]
    original = ['@--','-@@','@-@']
    n=3
    maps=[lambda r,c:(n-1-c,r),lambda r,c:(n-1-r,n-1-c),lambda r,c:(c,n-1-r),lambda r,c:(r,n-1-c),lambda r,c:(n-1-c,n-1-r),lambda r,c:(n-1-r,c),lambda r,c:(c,r),lambda r,c:(r,c)]
    patterns += [(original,[''.join(original[f(r,c)[0]][f(r,c)[1]] for c in range(n)) for r in range(n)]) for f in maps]
    for size in [2,3,4,5,10]*3:
        a=[''.join(rng.choice('@-') for _ in range(size)) for _ in range(size)]
        b=[''.join(rng.choice('@-') for _ in range(size)) for _ in range(size)]
        patterns.append((a,b))
    for a,b in patterns:
        result['transform'].append((str(len(a))+'\n'+'\n'.join(a+b)+'\n',transform_oracle(a,b)))
    points = [[(0,0),(1,0)],[(0,0),(0,1)],[(0,0),(1,0),(1,1),(0,1)],
              [(0,0),(1000000000,0)],[(1000000000,0),(0,0)]]
    for size in [4,6,8]*3:
        points.append(rng.sample(list(itertools.product(range(5),range(3))),size))
    points += [[(i,i) for i in range(12)],[(i,0) for i in range(12)]]
    for values in points:
        result['wormhole'].append((str(len(values))+'\n'+''.join(f'{x} {y}\n' for x,y in values),worm_oracle(values)))
    coordinates=[(3,6),(0,1),(1,0),(0,1000),(1000,0),(500,504),(500,505),(500,492),(500,491)]
    coordinates += [tuple(rng.sample(range(1001),2)) for _ in range(20)]
    for x,y in coordinates:
        result['lostcow'].append((f'{x} {y}\n',lost_oracle(x,y)))
    diamonds=[([1,6,4,3,1],3),([1],0),([5]*9,0),([1,4,5],3),([1,10000],10000),([1,10000],9998)]
    diamonds += [([rng.randrange(1,20) for _ in range(rng.randrange(1,10))],rng.randrange(0,10)) for _ in range(20)]
    diamonds += [([1,10000]*500,0),([i*10+1 for i in range(1000)],10000)]
    for sizes,k in diamonds:
        result['diamond'].append((f'{len(sizes)} {k}\n'+'\n'.join(map(str,sizes))+'\n',diamond_oracle(sizes,k)))
    orders=[]
    for size in [2,3,4,5,6,7]*3:
        order = rng.sample(list(range(1,size+1)),size)
        slots = sorted(rng.sample(range(size),rng.randrange(1,size)))
        hierarchy=[order[i] for i in slots]
        fixed_slots=sorted(rng.sample(range(size),rng.randrange(1,size)))
        fixed=[(order[i],i+1) for i in fixed_slots]
        orders.append((size,hierarchy,fixed,order_oracle(size,hierarchy,fixed)))
    orders += [(100,list(range(2,101)),[(100,100)],'1\n'),(100,list(range(2,101)),[(1,100)],'100\n'),(100,list(range(2,100))+[1],[(2,1)],'99\n')]
    for size,hierarchy,fixed,expected in orders:
        result['milkorder'].append((f'{size} {len(hierarchy)} {len(fixed)}\n'+' '.join(map(str,hierarchy))+'\n'+''.join(f'{cow} {place}\n' for cow,place in fixed),expected))
    relations=[('MOTHER','AA'),('GGMOTHER','BB'),('MOTHER','SISTER'),('GMOTHER','MOTHER'),('GMOTHER','AUNT'),('AUNT','COUSIN'),('GGMOTHER','GMOTHER')]
    families=[('AA','BB',relations),('BB','AA',relations),('AA','SISTER',relations),('AA','COUSIN',relations),('AA','MOTHER',relations),('GMOTHER','AA',relations),('MISSING','AA',relations),('BB','AUNT',relations)]
    for _ in range(20):
        size=12
        relations=[(name(rng.randrange(i)),name(i)) for i in range(1,size)]
        rng.shuffle(relations)
        a,b=rng.sample(list(range(size)),2)
        families.append((name(a),name(b),relations))
    chain=[(name(i),name(i+1)) for i in range(100)]
    families += [(name(0),name(100),chain),(name(100),name(0),chain),('ZZ',name(100),chain)]
    for a,b,relations in families:
        result['family'].append((f'{len(relations)} {a} {b}\n'+''.join(f'{mother} {child}\n' for mother,child in relations),family_oracle(a,b,relations)))
    return result


def completed_learner(spec, keep_task=None):
    # Fill only task bodies from the verified reference, retaining the learner driver.
    reference=(ROOT/spec['folder']/'solution/main.py').read_text()
    learner=(ROOT/spec['folder']/'starter/main.py').read_text()
    ref_functions={n.name:n for n in ast.parse(reference).body if isinstance(n,ast.FunctionDef)}
    lines=learner.splitlines(keepends=True)
    edits=[]
    for fn in ast.parse(learner).body:
        if isinstance(fn,ast.FunctionDef) and fn.name in spec['functions']:
            if fn.name==keep_task:
                continue
            original=ref_functions[fn.name]
            body=reference.splitlines(keepends=True)[original.body[0].lineno-1:original.end_lineno]
            edits.append((fn.body[0].lineno-1,fn.end_lineno,body))
    assert len(edits)==len(spec['functions'])-(keep_task is not None)
    for start,end,body in sorted(edits,reverse=True):
        lines[start:end]=body
    finished=''.join(lines)
    assert ('raise NotImplementedError' in finished)==(keep_task is not None)
    return finished


def verify():
    all_cases=cases()
    before={str(f.relative_to(ROOT)):f.read_bytes() for s in SPECS for f in (ROOT/s['folder']).rglob('*') if f.is_file()}
    originals=json.loads((ROOT/'tests/required-fileio-originals.json').read_text())
    for path,expected in originals.items():
        folder,relative=path.split('/',1)
        archive=ROOT/'_guide-history/bronze-required-fileio'/folder
        mapped=ROOT/path
        if relative=='README.md': mapped=archive/'project-original.md'
        if relative=='starter/README.md': mapped=archive/'starter-original.md'
        if path=='UB6-Milking-Cows/solution/main.py': mapped=archive/'reference-original.py'
        assert digest(mapped)==expected['sha256'], (path,mapped)
    rows=[]
    guards=[]
    partial_tasks=[]
    with tempfile.TemporaryDirectory(prefix='bronze-required-fileio-') as temporary:
        temporary=Path(temporary)
        for spec in SPECS:
            folder,task=spec['folder'],spec['task']
            assert digest(ROOT/folder/'solution/main.py')==spec['referenceSha256']
            assert (ROOT/folder/'solution/main.py').read_bytes() != (ROOT/folder/'starter/main.py').read_bytes()
            assert (ROOT/folder/'starter'/f'{task}.in').read_bytes()==(ROOT/folder/'solution'/f'{task}.in').read_bytes()
            assert (ROOT/folder/'starter/sample.expected').read_bytes()==(ROOT/folder/'solution/sample.expected').read_bytes()
            assert b'\r' not in (ROOT/folder/'starter/sample.expected').read_bytes()
            assert '*.expected text eol=lf' in (ROOT/'.gitattributes').read_text()
            for role in ['solution','starter','completed']:
                directory=temporary/(folder+'-'+role)
                directory.mkdir()
                code=completed_learner(spec) if role=='completed' else (ROOT/folder/role/'main.py').read_text()
                (directory/'main.py').write_text(code)
                for payload,expected in all_cases[task]:
                    (directory/f'{task}.in').write_text(payload)
                    answer=directory/f'{task}.out'
                    answer.write_text('Earlier answer\n')
                    out,err=execute([sys.executable,'main.py'],directory,1 if role=='starter' else 0)
                    assert not out
                    if role=='starter':
                        assert 'NotImplementedError' in err.decode() and 'TASK:' in err.decode()
                        assert answer.read_text()=='Earlier answer\n'
                    else:
                        assert answer.read_text()==expected,(task,role,payload[:300],answer.read_text(),expected)
                rows.append(dict(folder=folder,role=role,cases=len(all_cases[task]),nativeFileIo=True,
                                 independentOracle=True,unfinished=role=='starter',sourceCodeUnchanged=True))
                print(json.dumps(rows[-1]),flush=True)
            for function in spec['functions']:
                directory=temporary/(folder+'-unfinished-'+function)
                directory.mkdir()
                (directory/'main.py').write_text(completed_learner(spec,keep_task=function))
                (directory/f'{task}.in').write_bytes((ROOT/folder/'starter'/f'{task}.in').read_bytes())
                (directory/f'{task}.out').write_text('Earlier answer\n')
                out,err=execute([sys.executable,'main.py'],directory,1)
                assert not out and f'TASK: {function}' in err.decode()
                assert (directory/f'{task}.out').read_text()=='Earlier answer\n'
                partial_tasks.append(dict(folder=folder,function=function,refused=True,previousAnswerPreserved=True))
            if task == 'milkorder':
                for label, body, payload in [
                    ('false-fixed-one', '    return False\n', '4 2 1\n2 3\n1 4\n'),
                    ('missing-return', '    pass\n', (ROOT/folder/'starter/milkorder.in').read_text()),
                ]:
                    directory=temporary/(folder+'-base-'+label)
                    directory.mkdir()
                    code=completed_learner(spec)
                    fn=next(n for n in ast.parse(code).body if isinstance(n,ast.FunctionDef) and n.name=='check')
                    lines=code.splitlines(keepends=True)
                    lines[fn.body[0].lineno-1:fn.end_lineno]=[body]
                    (directory/'main.py').write_text(''.join(lines))
                    (directory/'milkorder.in').write_text(payload)
                    (directory/'milkorder.out').write_text('Earlier answer\n')
                    out,err=execute([sys.executable,'main.py'],directory,1)
                    assert not out and 'Valid base constraints must be feasible' in err.decode()
                    assert (directory/'milkorder.out').read_text()=='Earlier answer\n'
            for role in ['starter','solution']:
                doc=(ROOT/folder/role/'README.md').read_text()
                assert all(f'## {title}' in doc for title in ['Contract','Predict and trace','Implement and explain','Independent checks','Save and run'])
                guard=doc.split('```sh\n',1)[1].split('\n```',1)[0]
                guard=guard.replace('python3 main.py',shlex.quote(sys.executable)+' main.py')
                for variant in ['normal','syntax','missing-input','wrong-expected']:
                    directory=temporary/(folder+'-guard-'+role+'-'+variant)
                    shutil.copytree(ROOT/folder/role,directory)
                    (directory/f'{task}.out').write_text('Earlier answer\n')
                    if variant=='syntax': (directory/'main.py').write_text('def broken(\n')
                    if variant=='missing-input': (directory/f'{task}.in').unlink()
                    if variant=='wrong-expected': (directory/'sample.expected').write_text('Wrong answer\n')
                    success=role=='solution' and variant=='normal'
                    execute(['/bin/sh','-c',guard],directory,0 if success else 1)
                    actual=(directory/f'{task}.out').read_text()
                    expected=(ROOT/folder/role/'sample.expected').read_text() if success else 'Earlier answer\n'
                    assert actual==expected,(folder,role,variant)
                    assert not (directory/f'{task}.out.new').exists()
                    guards.append(dict(folder=folder,role=role,variant=variant,published=success,previousAnswerPreserved=not success))
    after={str(f.relative_to(ROOT)):f.read_bytes() for s in SPECS for f in (ROOT/s['folder']).rglob('*') if f.is_file()}
    assert before==after
    report=dict(packs=7,namedTasks=10,roles=rows,casesPerCompletedRole=sum(len(v) for v in all_cases.values()),
                baseFeasibilityRefusals=2,guardCases=len(guards),guards=guards,partialTaskCases=len(partial_tasks),partialTasks=partial_tasks,independentProblemModels=True,
                referenceAndOriginalBytesChecked=True,sourceFilesUnchanged=True,
                completedTaskBodiesFromVerifiedReference=True,totalNativeProcesses=len(PROCESSES))
    receipt=os.environ.get('BRONZE_FILEIO_ACCEPTANCE_RECEIPT')
    if receipt: Path(receipt).write_text(json.dumps({**report,'processes':PROCESSES},indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['roles','guards','partialTasks']}),flush=True)


if __name__=='__main__':
    verify()
