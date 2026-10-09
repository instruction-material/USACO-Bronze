# Cow College reference

`main.py` is the unchanged legacy USACO reference. The learner pack is in
`../starter/`, with a distinct unfinished helper and the full project guide.

Run from this role folder:

```sh
python3 main.py < sample.in
```

This program uses standard input and standard output. `sample.in` is a local
redirectable fixture; no hard-coded input or output filename is required.

The supplied sample prints `12 4`; tied optima require the smallest tuition.

Verify the reference, learner boundary, and completed learner driver from the
repository root with `python3 tests/verify-stdio-packs.py`. That check includes
independent optimality oracles and the full published input limits.

Problem contract: [USACO Cow College](https://usaco.org/index.php?cpid=1251&page=viewproblem2).
