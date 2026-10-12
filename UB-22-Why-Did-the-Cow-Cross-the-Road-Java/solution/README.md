# Road-Crossing Observations: Reference

The original reference `Main.java`, `crossroad.in` and `crossroad.out` are
preserved byte-for-byte. Keep a learner attempt before comparing this role.
The historical reference assumes inputs satisfy the contract above.

## Contract

Process the observations in their recorded order. `crossroad.in` begins with an
integer N in 1..100. The next N observations each contain a cow ID in 1..10 and
a road side, 0 or 1. A crossing is confirmed only when successive observations
of the same cow have different sides. Observations of other cows can appear
between them. A cow's first observation confirms no crossing. Write the total
as one integer and a newline in `crossroad.out`.

This guide supplies the working contract independently. The
[official problem](https://usaco.org/index.php?page=viewproblem2&cpid=711)
is an additional resource. No inference about unobserved crossings is required.

## Predict and trace

The included `crossroad.in` has eight observations. Cow 3 has side sequence
1,0,0,1 and contributes two changes; cow 4 has 1,0 and contributes one. Cows 6
and 2 are each seen once. Predict `3` followed by a newline; `sample.expected`
contains those exact bytes. Grouping by cow is useful for a separate check,
but the implementation still processes the original observation order.

For each observation, record the cow's previous known side, the new side,
whether it contributes one change, and the updated total. An unknown side
needs a value distinct from both 0 and 1. Maintain a separate state for each
of the ten cows. Explain why another cow's observation cannot change that state.

## Implement and explain

Complete the learner's `Main.countCrossings(int[][] observations)`. Retain the
supplied driver and return an integer count. Before each row, the stored side
for each seen cow is its latest observed side, and the total counts all changes
confirmed by earlier rows. Update both parts of this invariant after the row.
Use O(N) time and O(10) state. A dictionary or a ten-entry indexed array is a
choice about representation; explain the ID-to-index mapping if using an array.

## Independent checks

Collect each cow's side sequence independently, then count unequal neighboring
values in those sequences. Compare that sum with the implementation. Check one
observation, repeated identical sides, 0-to-1 and 1-to-0 changes, IDs 1 and 10,
interleaved cows and the maximum 100 observations. One cow alternating sides
for 100 observations confirms 99 crossings. Ten cows observed once confirm zero.

A shared walkthrough pauses at the prediction, the unknown-side representation,
one interleaved trace, the invariant and the independent check. The same order
supports individual reading. For optional practice, change the observations and
predict the complete result before running; retain one corrected trace and an
explanation. This checkpoint does not complete every topic in its course unit.

## Save, compile and run

Use JDK 17 or newer. Compile the file `Main.java` and run the entry class `Main`.
This native file-I/O program reads `crossroad.in` from the working directory;
browser Input does not replace that file. Save the attempt, export its whole
role folder, and keep its README, input and `sample.expected` together. Learner
and reference need separate generated classes.

Run the following guard from the extracted role folder with a compatible shell.
It clears generated classes, compiles current source, runs in a temporary
directory and compares the sample before replacing an earlier answer. An
unfinished learner, failed compile, missing entry class or wrong expected file
preserves the previous `crossroad.out`. In another terminal, follow the same
compile/run/compare/publish steps and check each exit status before continuing.

```sh
task_classes="$(pwd)/target/classes"
task_run=$(mktemp -d) || exit 1
trap 'rm -rf "$task_run"' EXIT
if rm -rf target/classes \
    && mkdir -p target/classes \
    && javac --release 17 -encoding UTF-8 -Xlint:all -Werror -d target/classes Main.java \
    && cp crossroad.in "$task_run/crossroad.in" \
    && (cd "$task_run" && java -cp "$task_classes" Main) \
    && diff -u sample.expected "$task_run/crossroad.out" \
    && cp "$task_run/crossroad.out" crossroad.out.new \
    && mv crossroad.out.new crossroad.out; then
    printf 'Verified crossroad.out\n'
else
    task_status=$?
    rm -f crossroad.out.new
    exit "$task_status"
fi
```

After changing input, predict a separate expected file and select that comparison
before publishing the changed answer. A matching sample alone does not prove
correctness; retain the independent checks and a changed-case explanation.
