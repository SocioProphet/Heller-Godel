# HG-EXP-008.9 — Cayley Spectrum Decomposition

Empirical irrep-block decomposition of Cayley graph adjacency spectra, complementary to HG-EXP-008.8.

**Repo target:** Heller-Godel  
**Path:** `docs/experiments/HG-EXP-008.9-cayley-spectrum-decomposition.md`  
**Parents:** HG-MTH-008.6 (dimension-spectrum bridge), HW-PRIME-WEIL-009 (reciprocal)  
**Sibling:** HG-EXP-008.8 (EMR Coxeter sub-complex decomposition)  
**Depends on:** HG-EXP-008.8 tranche 2 — small `S_n` character-table and decomposition helpers in `dimension_spectrum.py`  
**Status:** Empirical experiment. This tranche stages the finite Cayley calibration core and the S4 EMR-image sanity row. It does not yet claim the full higher-dimensional irrep-block numerical atlas.  
**Date:** 2026-05-29

---

## 0. Purpose

The Cayley graph of a finite group is a complementary stratification to the Coxeter-complex view used in HG-EXP-008.8.

| View | Vertices | Edges | Captures |
|------|----------|-------|----------|
| Coxeter complex (008.8) | ordered set partitions | inclusion | subgroup / parabolic structure |
| Cayley graph (008.9) | group elements | generators | multiplication / word structure |

Both are finite combinatorial instruments for reading the same dimension-spectrum coordinate from HG-MTH-008.6. HG-EXP-008.8 probes the Coxeter / weight-selection route. HG-EXP-008.9 is the positive-control instrument: direct group multiplication and finite character arithmetic.

The target theorem is standard: for a finite group G and symmetric generator multiset S, the adjacency spectrum of `Cay(G,S)` decomposes across irreducible representations. This experiment uses that theorem as a calibration check, not as a new theorem.

---

## 1. Claim discipline

Standard facts used here:

- Cayley graph adjacency is right multiplication by the generator multiset.
- If `S = S^{-1}`, the adjacency matrix is symmetric and the spectrum is real.
- For `S_n`, the on-circle irreps are exactly trivial and sign.
- The number of adjacency-spectrum eigenvalues assigned to an irrep block is `(dim rho)^2`, matching the finite Plancherel weighting used in HG-MTH-008.6.

Interpretive placement:

- On-circle eigenvalues for `S_n` are `chi_trivial(S)` and `chi_sign(S)`.
- Off-circle eigenvalue count is `|S_n| - 2` for `n >= 2`.
- Generator choice changes eigenvalues inside blocks, but not the dimension-spectrum partition.

Fenced non-claims:

- No P vs NP implication.
- No RH, GRH, or Artin implication.
- No expander or Ramanujan claim unless a spectral-gap analysis is explicitly computed.
- No infinite groups, Lie groups, or real reductive groups.

---

## 2. Locked sanity row

For `S_4`, use the generators from the EMR image:

```text
g = (1,4,3,2)
h = (1,3,2)
S = {g, g^-1, h, h^-1}
```

Then:

- `|S_4| = 24` vertices.
- `A` is 4-regular and symmetric.
- `chi_trivial(S) = 4`.
- `g` is a 4-cycle and odd; `h` is a 3-cycle and even.
- `chi_sign(S) = -1 -1 + 1 + 1 = 0`.
- On-circle spectrum is `{4, 0}`.
- Total spectrum count is 24.
- Off-circle count is 22.
- Trace is 0 because the identity is not in S, so there are no self-loops.

This sanity row must pass before any off-circle numerical atlas is trusted.

---

## 3. Implementation scope in this tranche

This tranche adds:

- finite permutation utilities for small `S_n`;
- Cayley adjacency construction for right-multiplication graphs;
- generator symmetrization;
- on-circle trivial/sign eigenvalue computation;
- Plancherel block-count verification using `dimension_spectrum.sn_irreps`;
- the locked `S_4` EMR-image sanity row.

This tranche does not yet add:

- higher-dimensional matrix realizations for irreps;
- numerical block eigenvalues for off-circle blocks;
- full `(G,S)` atlas CSV;
- plots or final report;
- expander / spectral-gap claims.

Those belong to a follow-up tranche after matrix-representation fixtures are declared and tested.

---

## 4. Acceptance criteria for this tranche

- S4 sanity row reproduces on-circle eigenvalues `{4, 0}`.
- Cayley graph has `|G|` vertices and degree `|S|` in the symmetrized case.
- Trace is zero when identity is not in S.
- Block counts satisfy `sum(dim rho)^2 = |G|`.
- On-circle count equals the abelianization count for `S_n`, namely 2 for `n >= 2`.
- Boundary guard strings are present in the module docstring.

---

## 5. Full experiment acceptance criteria, later tranche

The full HG-EXP-008.9 experiment is accepted only when:

1. `data/exp_008_9_results.csv` contains rows for all `(G,S)` pairs in the sweep.
2. The S4 sanity row includes locked off-circle numerical eigenvalues from verified matrix blocks.
3. Disjoint-union theorem is verified against the full Cayley spectrum for every pair.
4. `alpha(G)` matches HG-MTH-008.6 / `dimension_spectrum.alpha(G)`.
5. `reports/HG-EXP-008.9-summary.md` contains the spectrum atlas.
6. All tests pass.

---

## 6. Non-claims

This experiment does not claim any new theorem. It does not establish expander or Ramanujan properties. It does not extend to infinite groups, Lie groups, or real reductive groups. It does not bear on P vs NP, RH, GRH, or Artin. The novelty is the systematic dimension-spectrum atlas as a calibration instrument.
