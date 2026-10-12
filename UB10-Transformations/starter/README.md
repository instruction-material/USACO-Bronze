# Transformations: Learner

This separate learner intentionally raises `NotImplementedError` at its first unfinished task. It has no finished answer and leaves an earlier output untouched. Complete only the named functions.

## Contract

Read `transform.in`: square size N, then N original rows and N target rows, each containing exactly N characters chosen from @ and -. This course pack uses N in 1..10. Write one integer to `transform.out`, selecting the first matching category: 1 clockwise 90 degrees, 2 clockwise 180, 3 clockwise 270, 4 reflection across the vertical axis, 5 that reflection followed by a nonzero quarter-turn rotation, 6 no change, 7 none of these. Apply priority even when a symmetric pattern fits several categories.

This standalone guide supplies the course contract and explicit verification bounds. The [original problem resource](https://train.usaco.org/) is additional reading; no account is needed to use this pack.

## Predict and trace

The original rows are @--, -@@, @-@. The target rows are @-@, -@-, @@-. The original top-left cell moves to the target top-right cell; the complete target is a clockwise quarter-turn, so category 1 wins. `sample.expected` stores the exact answer with a final newline. Read the included input file and record a manual trace before execution.

## Implement and explain

Complete `rotate90(pattern)` and `reflect(pattern)`, each returning a fresh square list of rows without changing its argument. Track (row,column) and derive the destination using the square size. The supplied category selection composes those operations and applies the required priority. Explain why comparing only the number of @ cells is insufficient and why the reflection reverses columns rather than rows.

Each operation takes O(N squared) time and space. A fixed number of transformations preserves that bound. Avoid aliasing output rows or mutating the original, since later category checks must see the same input.

## Independent checks

Use a separate coordinate-mapping checker. Four quarter-turns and two reflections must restore the original. Include an asymmetric pattern for each category, a reflection-then-rotation case, an unrelated target, a one-cell square and a symmetric square where rotation takes priority over no change. Exercise N=10.

A shared walkthrough pauses at the prediction, one state transition, the invariant and the independent check. Those same checkpoints support individual reading. For optional practice, change the input and predict a separate expected file before running. Retain a corrected trace and an explanation of one boundary case. This project does not complete every topic in its wider course unit.

## Save and run

Use Python 3.9 or newer. Save the attempt and export the complete role folder. Keep `main.py`, `transform.in`, this README and `sample.expected` together. Run from that folder; terminal standard input or browser Input does not replace the named input file. Learner and reference use separate folders.

The following shell guard copies current source and input to a temporary directory, runs there and compares the exact sample before publishing an answer. An unfinished task, syntax error, missing input or wrong expected answer preserves an earlier `transform.out`. Each failure must stop the sequence. In a different terminal, perform the same copy/run/compare/publish steps and check their exit statuses.

```sh
task_role="$(pwd)"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if cp main.py transform.in "$task_run/" \
    && (cd "$task_run" && python3 main.py) \
    && diff -u sample.expected "$task_run/transform.out" \
    && cp "$task_run/transform.out" transform.out.new \
    && mv transform.out.new transform.out; then
    printf 'Verified transform.out\n'
else
    task_status=$?
    rm -f transform.out.new
    exit "$task_status"
fi
```

After editing input, use an independently predicted expected file for that case. A matching sample alone is insufficient. The repository acceptance command is `python3 tests/verify-required-fileio-packs.py`, run from the repository root. That checks native file I/O, independent cases, unchanged source, unfinished tasks, separately completed learners and the actual guard. Site import, consent and saved-work readiness require a separate pinned browser check.
