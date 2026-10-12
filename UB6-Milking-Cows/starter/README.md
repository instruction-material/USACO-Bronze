# Milking Cows: Learner

This separate learner intentionally raises `NotImplementedError` at its first unfinished task. It has no finished answer and leaves an earlier output untouched. Complete only the named functions.

## Contract

Read `milk2.in`: N followed by N start/end pairs. This course pack uses 1..5000 intervals with integer times in 0..1000000 and start < end. An interval covers [start,end): the end instant is not an extra unit. Write the longest continuous period covered by at least one interval and the longest uncovered gap between the earliest start and latest end, separated by a space, to `milk2.out`. Do not count time before the first interval or after the last. Touching intervals form one continuous period.

This standalone guide supplies the course contract and explicit verification bounds. The [original problem resource](https://train.usaco.org/) is additional reading; no account is needed to use this pack.

## Predict and trace

The first two intervals overlap, so together they cover 300..1200, a length of 900. The gap to 1500 has length 300; the last interval lasts 600. The expected answer is `900 300`. `sample.expected` stores the exact answer with a final newline. Read the included input file and record a manual trace before execution.

## Implement and explain

Complete `calc_times(milk_times)`, returning (longest_covered, longest_uncovered). The supplied driver turns intervals into Boolean time units. After each unit, the two current run counters describe runs ending at that unit; at most one is positive. Maintain each maximum and reset the other current counter when the state changes. Explain why a duplicated or nested interval contributes coverage without increasing the elapsed time.

The supplied difference array records two boundaries per interval, then computes a prefix sum. Total time is O(N + T), space O(T), where T is latest_end - earliest_start, at most 1000000. This replaces the previous repeated per-interval filling, which could do 5000 times as much work on overlapping intervals.

## Independent checks

Independently sort and merge intervals, then compare the longest merged interval and longest gap. Check a single interval, identical intervals, nesting, adjacency, unsorted disjoint intervals and a gap of one time unit. At the course limit, 5000 copies of [0,1000000) must return `1000000 0`.

A shared walkthrough pauses at the prediction, one state transition, the invariant and the independent check. Those same checkpoints support individual reading. For optional practice, change the input and predict a separate expected file before running. Retain a corrected trace and an explanation of one boundary case. This project does not complete every topic in its wider course unit.

## Save and run

Use Python 3.9 or newer. Save the attempt and export the complete role folder. Keep `main.py`, `milk2.in`, this README and `sample.expected` together. Run from that folder; terminal standard input or browser Input does not replace the named input file. Learner and reference use separate folders.

The following shell guard copies current source and input to a temporary directory, runs there and compares the exact sample before publishing an answer. An unfinished task, syntax error, missing input or wrong expected answer preserves an earlier `milk2.out`. Each failure must stop the sequence. In a different terminal, perform the same copy/run/compare/publish steps and check their exit statuses.

```sh
task_role="$(pwd)"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if cp main.py milk2.in "$task_run/" \
    && (cd "$task_run" && python3 main.py) \
    && diff -u sample.expected "$task_run/milk2.out" \
    && cp "$task_run/milk2.out" milk2.out.new \
    && mv milk2.out.new milk2.out; then
    printf 'Verified milk2.out\n'
else
    task_status=$?
    rm -f milk2.out.new
    exit "$task_status"
fi
```

After editing input, use an independently predicted expected file for that case. A matching sample alone is insufficient. The repository acceptance command is `python3 tests/verify-required-fileio-packs.py`, run from the repository root. That checks native file I/O, independent cases, unchanged source, unfinished tasks, separately completed learners and the actual guard. Site import, consent and saved-work readiness require a separate pinned browser check.
