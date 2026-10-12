# Source Backlog Ledger

Current status: no unlinked source folders remain at the active top level.

On 2026-05-14, 71 top-level folders that were not linked by the live course catalog were moved to `_archived-unlinked/`. That archive is retained for source-history review, optional-bank recovery, or future promotion, but it is not part of the active public course surface.

Promotion rule: restore a folder from `_archived-unlinked/` only after the live course text names where it belongs, whether it is starter or solution material, and how the student or tutor verifies it. Update `COURSE_SOURCE_MANIFEST.md` and the live catalog link in the same change.

## Learner role backlog

Eleven of the 55 active project wrappers now have distinct source in both roles:
Square Pasture, Cow College, Feeding the Cows, Road-Crossing Observations,
Milking Cows, Transformations, Wormholes, The Lost Cow, Diamond Collector,
Milking Order and Family Tree.
The other 44 still have
placeholder learner roles and must not be advertised as runnable starter packs.
The original references are retained. File-input fixtures and algorithm/runtime
acceptance for other projects remain separate audit items.

For Cow College and Feeding the Cows, source readiness is verified by
`python3 tests/verify-stdio-packs.py`. Site import mapping and actual saved IDE
workflows must be verified separately before claiming catalog import readiness.

The Road-Crossing Observations Java source counterpart is accepted at
`ac876ec86f02b0f1795b6056e68069d7df260670`, including exact review and independent
main Java 17/21 checks.
Its required website row remains an import audit item until the source revision
is pinned and the real browser save/export workflow passes.

The seven required Python file-I/O learner counterparts have explicit tasks,
standalone guides, matched input/oracle files and native acceptance via
`python3 tests/verify-required-fileio-packs.py`. Six reference programs remain
unchanged; Milking Cows has a marked boundary-array performance correction
with the original preserved in `_guide-history/bronze-required-fileio/`.
Exact hosted source checks and pinned site import/save/export checks are
separate gates. This update does not mark all remaining optional roles ready.
