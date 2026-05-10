# HG-ANNEAL-001 Completion Audit

Tracking issue: #6  
Status: materially complete for annealing tranche; CI observation still pending.

## 1. Purpose

HG-ANNEAL-001 was opened to prevent theorem inflation while preserving the exploratory content of the Heller-Godel proof-character program. The issue's core requirement was to compare the safer flat-only draft against the stronger v2 draft, classify every strengthened claim, and lock the corrections before opening new research lanes.

The governing principle is:

```text
Exploration is preserved by classification, not deletion.
```

## 2. Required deliverables and audit result

| Required artifact | Repo path | Status |
|---|---|---|
| v1/v2 claim-diff ledger | `docs/review-ledgers/v1_v2_claim_diff.md` | present |
| v2 claim status table | `docs/review-ledgers/v2_claim_status_table.csv` | present |
| v2.1.3 patch plan | `docs/manuscripts/calculus_invariant_characters_v2_1_3_patch_plan.md` | present |
| v2.1.3 manuscript skeleton | `docs/manuscripts/calculus_invariant_characters_v2_1_3.md` | present |
| carry coboundary regression | `tests/test_carry_coboundary.py` | present |
| chain product regression | `tests/test_chain_product.py` | present |
| seed basis regression | `tests/test_seed_basis.py` | present |
| Catalan Puiseux regression | `tests/test_catalan_puiseux.py` | present |
| theorem-boundary text regression | `tests/test_claim_text_boundaries.py` | present |
| validation workflow | `.github/workflows/validate.yml` | present |
| source classification | `docs/SOURCE_CLASSIFICATION.md` | present |
| source manifest | `data/manifests/SOURCE_MANIFEST.json` | present |
| source manifest hashes | `data/manifests/SOURCE_MANIFEST.sha256` | present |
| BSD context note | `docs/context-notes/BSD_reference_note.md` | present |

## 3. Corrections now locked

The following claims are no longer allowed in theorem-core language:

1. `zeta_p` as a nontrivial ordinary group-cohomology obstruction.
2. `zeta_p` as a nonabelian or Heisenberg extension.
3. `zeta_p` as a non-split central extension under unrestricted cochains.
4. Regulator as a completed Chern-class construction.
5. `chi_p` as a holographic boundary.
6. Ordinary chain product giving `x^2/(1-x)^3`.
7. Naive statistic-invariance.
8. Catalan's local behavior as a naive single square-root term without analytic-germ separation.

## 4. Theorem-core after annealing

The current theorem-core is:

```text
fixed proof fragment
canonical normal form
fixed statistic
proof-family generating function
Puiseux shell/channel extraction
chi_p / chi_13 finite phase fingerprints
zeta_p as finite-resolution section defect / coboundary
multi-shell analytic support for rational/algebraic functions
flat base-relative visibility scoped to local systems
```

## 5. Preserved but not promoted

The following remain preserved outside theorem-core:

```text
Wythoff/Schwarz symmetry grammar
projection chart vs preimage geometry
Temporal Mechanics / S4 ordering diagnostics
observer groupoids / proof moduli
Borsuk-Ulam boundary encoding
heavy-tail/no-mean falsification
Moufang/octonionic associators
AdS/CFT / holography vocabulary
superconductivity / Fermi-Bose analogies
BSD governance precedent
```

## 6. Source and context boundary

Primary load-bearing sources are hash-locked in `data/manifests/SOURCE_MANIFEST.*` and classified in `docs/SOURCE_CLASSIFICATION.md`.

BSD materials are context-only and methodological precedent. They are not executed, reproduced, or cited as evidence for Heller-Godel theorem claims unless a future promotion issue explicitly changes that status.

## 7. Remaining pre-move caveat

The validation workflow exists and is configured to run `pytest -q` on push and pull request events. However, connector inspection did not return a workflow run for the latest commits. Therefore:

```text
CI observation is pending.
```

This is not a content gap. It is an operational verification gap.

Before considering HG-ANNEAL-001 fully closed, one of the following should happen:

1. inspect a GitHub Actions run directly in GitHub;
2. trigger a PR branch and inspect PR workflow status;
3. run `pytest -q` locally in a clone and paste output;
4. add a follow-up issue specifically for CI observation.

## 8. Decision

Content capture for HG-ANNEAL-001 is materially complete. The corpus is now sufficiently annealed to prevent the known old overclaims from re-entering theorem-core text.

Movement to the next research phase is allowed only after acknowledging that CI observation remains pending. If strict process is required, do not close #6 until CI has been observed.
