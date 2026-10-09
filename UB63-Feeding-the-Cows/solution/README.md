# Feeding the Cows reference

`main.py` is the unchanged legacy USACO reference. The learner pack is in
`../starter/`, with a distinct unfinished helper and the full project guide.

Run from this role folder:

```sh
python3 main.py < sample.in
```

This program uses standard input and standard output. `sample.in` is a local
redirectable fixture; no hard-coded input or output filename is required.

The sample counts are 5, 3, 2, 2, 2, and 2. Accept any minimal layout that
feeds every cow with the matching breed within K; compare validity and count,
not exact placement characters.

Verify the reference, learner boundary, and completed learner driver from the
repository root with `python3 tests/verify-stdio-packs.py`. That check includes
independent optimality oracles and the full published input limits.

Problem contract: [USACO Feeding the Cows](https://usaco.org/index.php?cpid=1252&page=viewproblem2).
