# Milking Order: Learner

This separate learner intentionally raises `NotImplementedError` at its first unfinished task. It has no finished answer and leaves an earlier output untouched. Complete only the named functions.

## Contract

Read N, M, K from `milkorder.in`, then M distinct cow IDs in hierarchy order, then K cow/position pairs. N is in 2..100; M and K are each in 1..N-1. Cow IDs and one-based positions are in 1..N. Every cow appears exactly once in the final order, hierarchy cows keep their listed relative order, and fixed positions must be honored. A valid order is guaranteed. Write the earliest feasible one-based position of cow 1 to `milkorder.out`.

This standalone guide supplies the course contract and explicit verification bounds. The [original problem resource](https://usaco.org/index.php?page=viewproblem2&cpid=832) is additional reading; no account is needed to use this pack.

## Predict and trace

Cow 10 must occupy position 2 and cow 8 position 4. Hierarchy 2,10,3,1 requires cow 2 before position 2 and cow 3 after it but before cow 1. Cow 1 cannot use position 3 because cow 3 still needs an earlier free position; position 4 is fixed. Position 5 works, so the answer is 5. `sample.expected` stores the exact answer with a final newline. Read the included input file and record a manual trace before execution.

## Implement and explain

Complete `check(N,social,req_cows)`, returning a Boolean feasibility result. Reserve all fixed positions first. Traverse hierarchy cows in order; use their fixed slot when present and reject a slot before the current lower bound. Otherwise put the cow in the earliest free slot at or after that bound. The learner driver checks the base constraints first, including when cow 1 is already fixed, so an unfinished task always refuses to publish an answer. The supplied `main` then tries candidate positions for cow 1 in ascending order and handles an already fixed cow 1. Explain why placing an unfixed hierarchy cow earlier cannot reduce the space available to later hierarchy cows.

Each feasibility check scans at most N positions plus M hierarchy entries and K fixed entries. Trying up to N candidate positions takes O(N squared) time and O(N) state. State for each trial must be fresh.

## Independent checks

For tiny N, enumerate every complete permutation, retain those satisfying both constraints and take the smallest position of cow 1. Test cow 1 fixed, in the hierarchy, absent from it, blocked early positions, hierarchy entries with fixed anchors and N=100. A false feasibility result must not leave trial state behind.

A shared walkthrough pauses at the prediction, one state transition, the invariant and the independent check. Those same checkpoints support individual reading. For optional practice, change the input and predict a separate expected file before running. Retain a corrected trace and an explanation of one boundary case. This project does not complete every topic in its wider course unit.

## Save and run

Use Python 3.9 or newer. Save the attempt and export the complete role folder. Keep `main.py`, `milkorder.in`, this README and `sample.expected` together. Run from that folder; terminal standard input or browser Input does not replace the named input file. Learner and reference use separate folders.

The following shell guard copies current source and input to a temporary directory, runs there and compares the exact sample before publishing an answer. An unfinished task, syntax error, missing input or wrong expected answer preserves an earlier `milkorder.out`. Each failure must stop the sequence. In a different terminal, perform the same copy/run/compare/publish steps and check their exit statuses.

```sh
task_role="$(pwd)"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if cp main.py milkorder.in "$task_run/" \
    && (cd "$task_run" && python3 main.py) \
    && diff -u sample.expected "$task_run/milkorder.out" \
    && cp "$task_run/milkorder.out" milkorder.out.new \
    && mv milkorder.out.new milkorder.out; then
    printf 'Verified milkorder.out\n'
else
    task_status=$?
    rm -f milkorder.out.new
    exit "$task_status"
fi
```

After editing input, use an independently predicted expected file for that case. A matching sample alone is insufficient. The repository acceptance command is `python3 tests/verify-required-fileio-packs.py`, run from the repository root. That checks native file I/O, independent cases, unchanged source, unfinished tasks, separately completed learners and the actual guard. Site import, consent and saved-work readiness require a separate pinned browser check.
