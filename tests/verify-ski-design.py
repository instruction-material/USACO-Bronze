"""Check the Python and Java references through the contest file-I/O interface."""
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PYTHON = ROOT / "UB15-Ski-Course-Design/solution/main.py"
JAVA = ROOT / "UB-15-Ski-Course-Design-Java/solution/Main.java"
CASES = [
    [50], [7, 7, 7], [100, 99], [20, 3], [2, 20], [0, 100],
    [20, 4, 1, 24, 21], [0, 0, 0, 100], [100, 90, 83], [0, 17] * 500,
]


def minimum_cost(heights):
    # Each legal lower elevation defines a band of 18 integer elevations.
    return min(
        sum((height - min(max(height, low), low + 17)) ** 2 for height in heights)
        for low in range(84)
    )


def main():
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory)
        subprocess.run(["javac", "-d", work, JAVA], check=True, timeout=45)
        for heights in CASES:
            (work / "skidesign.in").write_text(
                f"{len(heights)}\n" + "".join(f"{height}\n" for height in heights)
            )
            expected = f"{minimum_cost(heights)}\n".encode()
            for command in ([sys.executable, PYTHON], ["java", "-cp", work, "Main"]):
                answer = work / "skidesign.out"
                answer.unlink(missing_ok=True)
                subprocess.run(command, cwd=work, check=True, timeout=10)
                actual = answer.read_bytes()
                if actual != expected:
                    raise AssertionError((command[0], heights[:8], expected, actual))
        print(f"Both references matched all {len(CASES)} contest output files.")


if __name__ == "__main__":
    main()
