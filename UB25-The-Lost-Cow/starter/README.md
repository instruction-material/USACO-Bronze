# The Lost Cow: Learner

This separate learner intentionally raises `NotImplementedError` at its first unfinished task. It has no finished answer and leaves an earlier output untouched. Complete only the named functions.

## Contract

Read distinct integers x and y in 0..1000 from `lostcow.in`. Begin at x and visit endpoints x+1, x-2, x+4, x-8 and so on. These endpoints are offsets from the original x, not from the previous endpoint. Stop immediately when the walk first reaches y, even in the middle of a leg. Write the total distance traveled to `lostcow.out`.

This standalone guide supplies the course contract and explicit verification bounds. The [original problem resource](https://usaco.org/index.php?page=viewproblem2&cpid=735) is additional reading; no account is needed to use this pack.

## Predict and trace

From x=3, walk to 4 (distance 1), then 1 (distance 3), then toward 7. Stop at y=6 after another 5, for a total of 9. The final endpoint is not actually reached. `sample.expected` stores the exact answer with a final newline. Read the included input file and record a manual trace before execution.

## Implement and explain

Complete `main(starting_pos,bessie_pos)` and return an integer distance. Track the original start, the current position, the alternating doubled offset and accumulated distance separately. Before each leg, determine whether the target lies between the current position and the next endpoint, inclusive. If it does, add only the distance to the target and stop. Explain why multiplying an offset by -2 both doubles the reach and changes direction.

A whole-leg calculation takes O(log(abs(x-y)+1)) steps and constant state. Walking one unit at a time is useful as an independent small-case checker.

## Independent checks

Compare with a separate unit-step walk that stops as soon as y is reached. Cover targets on both sides, a target at an endpoint, one just past an endpoint, both boundary coordinates and translated cases with the same x-y separation. x=y is outside this contract.

A shared walkthrough pauses at the prediction, one state transition, the invariant and the independent check. Those same checkpoints support individual reading. For optional practice, change the input and predict a separate expected file before running. Retain a corrected trace and an explanation of one boundary case. This project does not complete every topic in its wider course unit.

## Save and run

Use Python 3.9 or newer. Save the attempt and export the complete role folder. Keep `main.py`, `lostcow.in`, this README and `sample.expected` together. Run from that folder; terminal standard input or browser Input does not replace the named input file. Learner and reference use separate folders.

The following shell guard copies current source and input to a temporary directory, runs there and compares the exact sample before publishing an answer. An unfinished task, syntax error, missing input or wrong expected answer preserves an earlier `lostcow.out`. Each failure must stop the sequence. In a different terminal, perform the same copy/run/compare/publish steps and check their exit statuses.

```sh
task_role="$(pwd)"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if cp main.py lostcow.in "$task_run/" \
    && (cd "$task_run" && python3 main.py) \
    && diff -u sample.expected "$task_run/lostcow.out" \
    && cp "$task_run/lostcow.out" lostcow.out.new \
    && mv lostcow.out.new lostcow.out; then
    printf 'Verified lostcow.out\n'
else
    task_status=$?
    rm -f lostcow.out.new
    exit "$task_status"
fi
```

After editing input, use an independently predicted expected file for that case. A matching sample alone is insufficient. The repository acceptance command is `python3 tests/verify-required-fileio-packs.py`, run from the repository root. That checks native file I/O, independent cases, unchanged source, unfinished tasks, separately completed learners and the actual guard. Site import, consent and saved-work readiness require a separate pinned browser check.
