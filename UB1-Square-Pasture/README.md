# UB1 Square Pasture

Required project: calculate the area of the smallest axis-aligned square that
covers two rectangles. This is the [official USACO December 2016 Bronze problem](https://usaco.org/index.php?page=viewproblem2&cpid=663).

## Input and expected result

`square.in` has two lines. Each holds `x1 y1 x2 y2`, describing lower-left and
upper-right corners with integer coordinates from 0 through 10. Each rectangle
has positive width and height; the two rectangles do not touch or overlap.
`square.out` contains one integer: the minimum square area.

The starter includes the official sample. Its first rectangle is `(6, 6)` to
`(8, 8)`, and its second is `(1, 8)` to `(4, 9)`. Predict the output before
running: the combined width is 7 and height is 3, so a square side of 7 gives
area 49. A square may extend beyond the rectangles; its location need not be
unique. Return area rather than a corner, side length or perimeter.

## Learn and implement

A rectangle contributes two horizontal and two vertical boundaries. Find
extreme boundaries across **both** rectangles, then use the spans to select a
square large enough in both directions. Explain why a shorter side cannot
cover the widest span and why a square of the selected side can cover both.

`starter/main.py` supplies file handling. Complete its three geometry tasks.
The untouched program raises `NotImplementedError` instead of passing with a
finished algorithm. `solution/` retains the migrated reference and its fixtures.

## Run, verify and continue

From the chosen role folder, run `python3 main.py`, then inspect `square.out`.
The starter sample should produce 49 after implementation. Python resolves the
input file relative to the working directory, so run inside the role folder.
In a browser workspace, import the starter with its input file, save the
attempt and inspect the generated output; export both files for local use.

Test horizontal and vertical separation, unequal dimensions, reversed rectangle
order and extreme coordinates. Predict each answer before execution. One sample
is insufficient: an independent check can enumerate candidate square placements
for bounded coordinates rather than repeat the submitted formula.

A shared walkthrough follows the same path: draw both rectangles, mark extreme
boundaries, justify the side, finish the calculation, and compare fixture results.
Save source and two custom predictions before consulting the reference. The
optional extension compares two valid placements of the same minimum square.

Repository verification: `python3 tests/verify-square-pasture.py` checks actual
reference file I/O against a bounded placement oracle and confirms the learner
starter stays unfinished. It does not grade a completed learner submission or
certify other Bronze projects.
