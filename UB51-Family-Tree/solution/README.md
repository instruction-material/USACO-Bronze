# Family Tree: Reference

This reference supplies the completed algorithm for comparison after an attempt. Predict the result and explain its state before running. It assumes input satisfying the contract; it is not an invalid-input validator.

## Contract

Read N and two distinct query names from `family.in`, followed by N mother/child name pairs, with N in 1..100. Names contain 1..10 uppercase letters. Records form a maternal forest: each child has at most one mother and ancestry has no cycles. Write one exact relationship line to `family.out`. Shared mother gives SIBLINGS. Direct ancestry gives NAME is the mother, grand-mother, great-grand-mother, and so on, of OTHER. A sister of a direct ancestor gives NAME is the aunt, great-aunt, and so on, of OTHER. Other shared ancestry gives COUSINS; absent shared ancestry gives NOT RELATED. Put the ancestor or aunt first even if that reverses the input names.

This standalone guide supplies the course contract and explicit verification bounds. The [original problem resource](https://usaco.org/index.php?page=viewproblem2&cpid=833) is additional reading; no account is needed to use this pack.

## Predict and trace

AA reaches MOTHER, GMOTHER, GGMOTHER in three parent steps. BB reaches GGMOTHER in one. The nearest shared ancestor is therefore at distances (3,1), making BB the great-aunt of AA. The required output includes the names and hyphen in great-aunt. `sample.expected` stores the exact answer with a final newline. Read the included input file and record a manual trace before execution.

## Implement and explain

Complete `main(cow1,cow2,parents)` and return the complete relationship string without a newline. Trace both parent chains, including each query cow at distance zero. Find the nearest shared ancestor and both generation distances. Distances (1,1) mean siblings; both above one mean cousins. For other related cases, the shallower query cow is the ancestor or aunt. A mother is one generation away, a grandmother two; an aunt shares a mother with the target's mother. Preserve the exact required capitalization, spaces and hyphens.

The dictionary gives constant-time parent lookup on average. The reference scans one query chain for every ancestor of the other: O(N squared) time and constant additional traversal state. A separate ancestor-distance map can check the classification in O(N) time and space.

## Independent checks

Compare against independently recorded ancestor chains and nearest shared ancestry. Check both query orientations, mother, grandmother, deep ancestry, siblings, aunt, great-aunt, cousins, separate trees and a query name absent from the records. Use a chain of 100 relations to check the longest allowed generation wording.

A shared walkthrough pauses at the prediction, one state transition, the invariant and the independent check. Those same checkpoints support individual reading. For optional practice, change the input and predict a separate expected file before running. Retain a corrected trace and an explanation of one boundary case. This project does not complete every topic in its wider course unit.

## Save and run

Use Python 3.9 or newer. Save the attempt and export the complete role folder. Keep `main.py`, `family.in`, this README and `sample.expected` together. Run from that folder; terminal standard input or browser Input does not replace the named input file. Learner and reference use separate folders.

The following shell guard copies current source and input to a temporary directory, runs there and compares the exact sample before publishing an answer. An unfinished task, syntax error, missing input or wrong expected answer preserves an earlier `family.out`. Each failure must stop the sequence. In a different terminal, perform the same copy/run/compare/publish steps and check their exit statuses.

```sh
task_role="$(pwd)"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if cp main.py family.in "$task_run/" \
    && (cd "$task_run" && python3 main.py) \
    && diff -u sample.expected "$task_run/family.out" \
    && cp "$task_run/family.out" family.out.new \
    && mv family.out.new family.out; then
    printf 'Verified family.out\n'
else
    task_status=$?
    rm -f family.out.new
    exit "$task_status"
fi
```

After editing input, use an independently predicted expected file for that case. A matching sample alone is insufficient. The repository acceptance command is `python3 tests/verify-required-fileio-packs.py`, run from the repository root. That checks native file I/O, independent cases, unchanged source, unfinished tasks, separately completed learners and the actual guard. Site import, consent and saved-work readiness require a separate pinned browser check.
