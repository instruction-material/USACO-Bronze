# Feeding the Cows learner project

## Goal and starting point

Place the minimum number of breed-specific feeding patches so that every cow
can reach a patch of its own breed. This project practices a left-to-right
greedy scan, separate coverage state, and output validation. Before starting,
be able to index a string, update a list, and trace inclusive distance limits.

Complete only `place_patches(cows, k)` in `main.py`; return a list with one
character for each position. The supplied driver reads the test cases and
prints a patch count followed by the layout. The untouched pack raises
`NotImplementedError` before printing an answer.

## Input and output contract

The first input line is T, between 1 and 10. Each case contains a line with
N and K, then a line of N breed characters (`G` or `H`). N is between 1 and
100000; K is between 0 and N-1. One position can hold either a G patch, an H
patch, or no patch (`.`). A patch feeds unlimited cows of its own breed at
absolute distance at most K.

For every case, print the minimum patch count on one line, then a string of
N patch characters on the next line. The printed count must equal the number
of non-dot characters. Any valid layout with the minimum count is accepted;
a layout need not match the sample character for character.

Read standard input and print standard output. From this role folder, run:

```sh
python3 main.py < sample.in
```

`sample.in` is a redirectable fixture, not a file opened by the program. The
six sample cases require counts 5, 3, 2, 2, 2, and 2. The starter is deliberately
unfinished until the placement helper is completed.

## Contract and reasoning

Maintain a patch list and separate rightmost covered positions for G and H.
Initially neither breed covers any position. Scan cow positions from left to
right. If the current cow is already covered by its own breed, add no patch.
If it is uncovered, a matching patch is necessary: earlier decisions have not
fed that cow.

When `idx + k` is inside the line, put a matching patch there. This is the
furthest right position that can feed the current cow, so it reaches as far
as possible into later cows of the same breed. Its right coverage endpoint is
`idx + 2*k`. Keep the other breed's coverage state separate.

Near the end, when `idx + k` lies beyond the line, placing a matching patch at
`idx` reaches all remaining positions. If that position already contains the
other breed, use `idx - 1`, after reasoning about the boundary and occupancy.
Do not overwrite the existing patch. For K=0, each cow needs its own position;
this trailing collision case cannot occur. With K>0, the adjacent position in
a trailing collision remains reachable, and the other breed's earlier greedy
placements leave it available. Trace the two-cow `GH`, K=1 case to see why two
different patch positions are necessary.

An exchange argument explains the choice: among placements that feed the
first uncovered cow, a furthest-right interior placement cannot cover fewer
later same-breed cows than an earlier placement. Near the end, either valid
trailing placement reaches every remaining same-breed cow. The breed-specific
coverage intervals and collision check let both breeds share the line without
sharing a patch position. The scan takes O(N) work and O(N) output storage.

## Guided implementation

1. Create N dots and initialize separate uncovered G/H boundaries.
2. For each cow, choose the boundary for its breed and test whether `idx` is
   beyond it. Use an inclusive coverage endpoint.
3. Place an interior patch at `idx + k` for an uncovered cow and update only
   that breed's boundary.
4. Implement the trailing case and preserve a patch of the other breed.
5. Return the list. Let the supplied driver count patches and print both lines.

In an instructor session, hand-trace GHHGG for K=0, 1, and 2 before editing.
For independent work, draw the patch positions and matching coverage intervals,
then check them against the same rules before running the program.

## Check and explain

- For K=0, the minimum is N and the layout must match the cows.
- One cow needs one matching patch.
- A single breed with K=N-1 needs one patch.
- Both breeds with K=N-1 need two patches in different positions.
- The sample counts are 5, 3, 2, 2, 2, and 2; validate distance and breed for
  every cow, rather than demanding one exact sample layout.
- Swap G and H. The minimum count must be unchanged and patch breeds swap.
- Test alternating breeds near the right edge to exercise the collision rule.

Explain why an uncovered cow requires another patch, why the interior choice
is optimal, and why advancing G coverage must not advance H coverage.

## Open, save and run

Keep `main.py` and `sample.in` together. Save learner work independently before
comparing it with `../solution/main.py`. The reference uses the same standard
input/output format. A site import requires its own verified revision and
role-specific confirmation; this source pack alone does not establish that
an IDE import is connected.

Problem contract: [USACO Feeding the Cows](https://usaco.org/index.php?cpid=1252&page=viewproblem2).
