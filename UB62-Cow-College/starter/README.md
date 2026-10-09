# Cow College learner project

## Goal and starting point

Choose one tuition for all cows to maximize revenue, then return the smallest
price among tied optima. This project practices frequency tables, a cumulative
count, and an explicit tie rule. Before starting, be able to read integer input,
use a list as a frequency table, and trace a decreasing loop.

The supplied input and output driver follows the preserved legacy reference.
Complete only `choose_tuition` in `main.py`. Its arguments and return contract
are already connected to the driver. The unfinished pack raises
`NotImplementedError` before printing an answer.

## Input and output contract

The first input line is N, between 1 and 100000. The second line contains N
maximum affordable tuition values, each between 1 and 1000000. A cow attends
when its value is at least the chosen tuition. Print two integers on one line:
maximum revenue and the smallest optimal tuition. Python integers support the
largest possible revenue; other languages need at least a 64-bit integer.

Read from standard input and print to standard output. `sample.in` is a local
input fixture, not a file opened by the program. Run from this role folder:

```sh
python3 main.py < sample.in
```

Until the TODOs are complete, that command should stop with the named exception.
For the supplied example, the expected result after completion is `12 4`.

## Contract and reasoning

`tuition_to_cow[p]` counts cows whose maximum affordable tuition is exactly p.
When scanning prices from high to low, add that price's frequency to a running
count before computing revenue. The count then includes precisely the cows
whose values are at least the current price. Revenue is price times this count.

Keep both the best revenue and its tuition. Descending order visits larger tied
prices first; explain why replacing a prior result when the new revenue is
_equal_ keeps the smallest tied price. For values 1 and 2, both prices earn 2,
so the required answer is `2 1`.

The frequency table and scan use O(1000000) storage and O(N + 1000000) work.
Do not scan the entire cow list separately for every possible tuition.

## Guided implementation

1. Initialize the running cow count, best revenue, and best tuition.
2. Scan from `MAX_TUITION` down to 1, including both endpoints.
3. Add the current frequency before calculating the candidate revenue.
4. Update the saved revenue and price with the required tie behavior.
5. Return a pair in the order expected by the supplied driver.

In an instructor session, pause after each step to explain the invariant and
hand-trace the sample table. For independent work, make the trace first, then
implement and compare the printed answer with the hand calculation.

## Check and explain

- Sample values 1, 6, 4, 6: `12 4`.
- Tie values 1, 2: `2 1`.
- One value 1000000: `1000000 1000000`.
- Three equal values 7: `21 7`.
- Reorder an input list. The optimum must stay unchanged.
- For 100000 cows each willing to pay 1000000, explain why the revenue is
  100000000000 and why it must not overflow in another language.

Explain which cows are counted at a price before and after the frequency is
added. Also explain why the program returns the smallest price in every tie.

## Open, save and run

Keep `main.py` and `sample.in` together. Save an independent copy of completed
learner work before comparing with `../solution/main.py`. The reference reads
standard input too. The site may offer an import action only after this exact
source revision and learner/reference roles are verified; opening a preview
alone does not confirm an import or saved attempt.

Problem contract: [USACO Cow College](https://usaco.org/index.php?cpid=1251&page=viewproblem2).
