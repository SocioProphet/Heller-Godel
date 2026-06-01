# HG-STAT-001 Implementation Audit

Status: CI validation branch artifact.

## Implemented on main before this PR branch

- `docs/research-notes/admissible_statistics_partial_robustness_v0_1.md`
- `tests/test_admissible_statistics.py`

## Result captured

HG-STAT-001 is now preserved as a standalone companion note to CIPC v2.1.3. It states theorem-level robustness for two calibration families and keeps the general regular/algebraic/D-finite proof-grammar extension conjectural.

## Regression coverage

`tests/test_admissible_statistics.py` verifies:

1. closed-form chain-family formulas for admissible positive weights;
2. closed-form `((A -> A) -> A) -> A` family formulas for admissible positive weights;
3. the boundary non-admissible vector `(1,1,0)`;
4. corrected table values, including `(1,2,1)` giving `x^6/(1-x^4)^2` for the T-family.

## Validation purpose

This branch exists to trigger a pull-request workflow run for the current repository test suite, since prior connector inspection did not return push-triggered workflow runs.
