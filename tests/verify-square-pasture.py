"""Check actual Square Pasture file I/O using an independent placement oracle."""
import hashlib
import itertools
import json
import os
from pathlib import Path
import random
import runpy
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "UB1-Square-Pasture"
REFERENCE_SHA256 = "565bf977e8d413f81f611343abe36aed0c6bf1d1b05a4840ac98b4492401b6b5"


def placement_oracle(rectangles):
    # Enumerate candidate squares; do not reuse the reference extrema formula.
    for side in range(1, 11):
        for left, bottom in itertools.product(range(-10, 11), repeat=2):
            if all(left <= x1 and bottom <= y1 and
                   x2 <= left + side and y2 <= bottom + side
                   for x1, y1, x2, y2 in rectangles):
                return side * side
    raise AssertionError("No square covers this bounded fixture")


def separated(a, b):
    return a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1]


def verify():
    reference = PROJECT / "solution/main.py"
    assert hashlib.sha256(reference.read_bytes().replace(b"\r\n", b"\n")).hexdigest() == REFERENCE_SHA256
    rectangles = [(x1, y1, x2, y2)
                  for x1, y1, x2, y2 in itertools.product(range(4), repeat=4)
                  if x1 < x2 and y1 < y2]
    cases = [(a, b) for a, b in itertools.product(rectangles, repeat=2)
             if separated(a, b)]
    sample = ((6, 6, 8, 8), (1, 8, 4, 9))
    cases.extend([sample, tuple(reversed(sample))])
    rng = random.Random(663)
    while len(cases) < 200:
        x1, x2 = sorted(rng.sample(range(11), 2))
        y1, y2 = sorted(rng.sample(range(11), 2))
        first = (x1, y1, x2, y2)
        x1, x2 = sorted(rng.sample(range(11), 2))
        y1, y2 = sorted(rng.sample(range(11), 2))
        second = (x1, y1, x2, y2)
        if separated(first, second):
            cases.append((first, second))
    previous = Path.cwd()
    try:
        with tempfile.TemporaryDirectory(prefix="square-pasture-check-") as directory:
            os.chdir(directory)
            for case in cases:
                Path("square.in").write_text("".join(" ".join(map(str, r)) + "\n" for r in case))
                Path("square.out").unlink(missing_ok=True)
                runpy.run_path(str(reference), run_name="__main__")
                assert Path("square.out").read_text().strip() == str(placement_oracle(case)), case
            Path("square.in").write_bytes((PROJECT / "starter/square.in").read_bytes())
            Path("square.out").unlink()
            try:
                runpy.run_path(str(PROJECT / "starter/main.py"), run_name="__main__")
            except NotImplementedError as error:
                assert "enclosing-square" in str(error)
            else:
                raise AssertionError("The untouched learner starter must remain unfinished")
            assert not Path("square.out").exists()
    finally:
        os.chdir(previous)
    print(json.dumps({"referenceCases": len(cases), "actualFileIO": True,
                      "independentPlacementOracle": True, "starterUnfinished": True,
                      "referenceBytesPreserved": True}))


if __name__ == "__main__":
    verify()
