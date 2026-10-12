# Wormholes: Learner

This separate learner intentionally raises `NotImplementedError` at its first unfinished task. It has no finished answer and leaves an earlier output untouched. Complete only the named functions.

## Contract

Read `wormhole.in`: even N in 2..12, followed by N distinct (x,y) points with coordinates in 0..1000000000. Pair every wormhole with exactly one other wormhole. After teleporting through a pair, the cow walks in the positive x direction to the nearest wormhole strictly to the right on the same horizontal line; if none exists, it escapes. Write to `wormhole.out` the number of distinct pairings for which at least one starting position can enter an infinite cycle. Count each pairing once, regardless of how many starting positions cycle.

This standalone guide supplies the course contract and explicit verification bounds. The [original problem resource](https://usaco.org/index.php?page=viewproblem2&cpid=360) is additional reading; no account is needed to use this pack.

## Predict and trace

For the four corners, there are three pairings. Pairing the two horizontal neighbors on each row cycles. Pairing opposite corners in the matching 1-3 and 2-4 also cycles. Pairing 1-4 and 2-3 does not. Thus the count is 2, not the number of trapped starts. `sample.expected` stores the exact answer with a final newline. Read the included input file and record a manual trace before execution.

## Implement and explain

Complete `generate_next_on_right(x,y)` and `main(partners,next_on_right)`. Use -1 for no right neighbor and an unpaired partner. The supplied `cycle_exists` checks every start for N teleport-and-walk steps. Enumerate pairings by selecting the first unpaired index, pairing it with each available later index, recursing, then restoring both entries to -1. Explain why this generates each complete pairing once and why state restoration is necessary. The legacy neighbor helper uses the supplied global partners list only for its length; all lists have N entries.

Neighbor construction is O(N squared). There are (N-1)!! complete pairings, at most 10395; the supplied cycle check is O(N squared) per pairing. The partner state uses O(N) space, plus recursion depth N/2.

## Independent checks

Independently build the deterministic directed transition graph for each complete pairing and detect a cycle with visited-node sets. Test two points on one row (one cyclic pairing), two on different rows (zero), the square, unsorted input, several rows, coordinate limits and N=12. Verify each point has exactly one symmetric partner before judging a pairing.

A shared walkthrough pauses at the prediction, one state transition, the invariant and the independent check. Those same checkpoints support individual reading. For optional practice, change the input and predict a separate expected file before running. Retain a corrected trace and an explanation of one boundary case. This project does not complete every topic in its wider course unit.

## Save and run

Use Python 3.9 or newer. Save the attempt and export the complete role folder. Keep `main.py`, `wormhole.in`, this README and `sample.expected` together. Run from that folder; terminal standard input or browser Input does not replace the named input file. Learner and reference use separate folders.

The following shell guard copies current source and input to a temporary directory, runs there and compares the exact sample before publishing an answer. An unfinished task, syntax error, missing input or wrong expected answer preserves an earlier `wormhole.out`. Each failure must stop the sequence. In a different terminal, perform the same copy/run/compare/publish steps and check their exit statuses.

```sh
task_role="$(pwd)"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if cp main.py wormhole.in "$task_run/" \
    && (cd "$task_run" && python3 main.py) \
    && diff -u sample.expected "$task_run/wormhole.out" \
    && cp "$task_run/wormhole.out" wormhole.out.new \
    && mv wormhole.out.new wormhole.out; then
    printf 'Verified wormhole.out\n'
else
    task_status=$?
    rm -f wormhole.out.new
    exit "$task_status"
fi
```

After editing input, use an independently predicted expected file for that case. A matching sample alone is insufficient. The repository acceptance command is `python3 tests/verify-required-fileio-packs.py`, run from the repository root. That checks native file I/O, independent cases, unchanged source, unfinished tasks, separately completed learners and the actual guard. Site import, consent and saved-work readiness require a separate pinned browser check.
