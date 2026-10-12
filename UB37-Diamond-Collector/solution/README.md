# Diamond Collector: Reference

This reference supplies the completed algorithm for comparison after an attempt. Predict the result and explain its state before running. It assumes input satisfying the contract; it is not an invalid-input validator.

## Contract

Read N and K from `diamond.in`, followed by N diamond sizes. Use 1..1000 diamonds, K in 0..10000 and sizes in 1..10000. Select the largest number that fit in one display case while the largest and smallest selected sizes differ by at most K. A difference exactly equal to K is allowed; equal-size diamonds are separate objects. Write that maximum count to `diamond.out`.

This standalone guide supplies the course contract and explicit verification bounds. The [original problem resource](https://usaco.org/index.php?page=viewproblem2&cpid=639) is additional reading; no account is needed to use this pack.

## Predict and trace

The two size-1 diamonds and sizes 3 and 4 fit in [1,4], giving four objects. Size 6 cannot join that case. The count includes both copies of size 1. `sample.expected` stores the exact answer with a final newline. Read the included input file and record a manual trace before execution.

## Implement and explain

Complete `calc_num_diamonds(min_size,sizes,k)` and `calc_max_diamonds(sizes,k)`. The first counts values in the inclusive interval [min_size,min_size+k]; the second tries observed minimum sizes and returns the best count. Explain why an optimal nonempty case has an observed smallest size and why using abs(size-min_size) would permit an invalid two-sided window.

The candidate-minimum method is O(N squared) time and O(1) additional state. With N at most 1000 it is suitable for this Bronze checkpoint. Sorting and a sliding window provide a separate checker and an optional extension.

## Independent checks

Compare with a sorted contiguous-window checker, and enumerate all subsets on tiny cases. Test K=0, repeated sizes, an exact-K boundary, a just-too-large difference, arbitrary input order, one diamond and 1000 diamonds including sizes 1 and 10000.

A shared walkthrough pauses at the prediction, one state transition, the invariant and the independent check. Those same checkpoints support individual reading. For optional practice, change the input and predict a separate expected file before running. Retain a corrected trace and an explanation of one boundary case. This project does not complete every topic in its wider course unit.

## Save and run

Use Python 3.9 or newer. Save the attempt and export the complete role folder. Keep `main.py`, `diamond.in`, this README and `sample.expected` together. Run from that folder; terminal standard input or browser Input does not replace the named input file. Learner and reference use separate folders.

The following shell guard copies current source and input to a temporary directory, runs there and compares the exact sample before publishing an answer. An unfinished task, syntax error, missing input or wrong expected answer preserves an earlier `diamond.out`. Each failure must stop the sequence. In a different terminal, perform the same copy/run/compare/publish steps and check their exit statuses.

```sh
task_role="$(pwd)"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if cp main.py diamond.in "$task_run/" \
    && (cd "$task_run" && python3 main.py) \
    && diff -u sample.expected "$task_run/diamond.out" \
    && cp "$task_run/diamond.out" diamond.out.new \
    && mv diamond.out.new diamond.out; then
    printf 'Verified diamond.out\n'
else
    task_status=$?
    rm -f diamond.out.new
    exit "$task_status"
fi
```

After editing input, use an independently predicted expected file for that case. A matching sample alone is insufficient. The repository acceptance command is `python3 tests/verify-required-fileio-packs.py`, run from the repository root. That checks native file I/O, independent cases, unchanged source, unfinished tasks, separately completed learners and the actual guard. Site import, consent and saved-work readiness require a separate pinned browser check.
