# Source Backlog Ledger

Current status: no unlinked source folders remain at the active top level.

On 2026-05-14, 71 top-level folders that were not linked by the live course catalog were moved to `_archived-unlinked/`. That archive is retained for source-history review, optional-bank recovery, or future promotion, but it is not part of the active public course surface.

Promotion rule: restore a folder from `_archived-unlinked/` only after the live course text names where it belongs, whether it is starter or solution material, and how the student or tutor verifies it. Update `COURSE_SOURCE_MANIFEST.md` and the live catalog link in the same change.

## Learner role backlog

Three of the 55 active project wrappers now have distinct source in both roles:
Square Pasture, Cow College, and Feeding the Cows. The other 52 still have
placeholder learner roles and must not be advertised as runnable starter packs.
The original references are retained. File-input fixtures and algorithm/runtime
acceptance for other projects remain separate audit items.

For Cow College and Feeding the Cows, source readiness is verified by
`python3 tests/verify-stdio-packs.py`. Site import mapping and actual saved IDE
workflows must be verified separately before claiming catalog import readiness.
