# HG-EXP-008.8 — EMR Coxeter Sub-complex Dimension-Spectrum Decomposition

### Empirical \(S_n\)-isotypic decomposition of \(\Sigma(\lambda)\) as a function of \(\lambda\)'s sign pattern

**Repo target:** Heller-Godel  
**Path:** `docs/experiments/HG-EXP-008.8-emr-coxeter-decomposition.md`  
**Parents:** HG-MTH-008.6 (dimension-spectrum bridge), HW-PRIME-WEIL-009 (reciprocal)  
**Adjacent literature:** Ehrenborg, Morel, Readdy — *Some combinatorial identities appearing in the calculation of the cohomology of Siegel modular varieties*, Algebraic Combinatorics 2 (2019), no. 5, 863–878.  
**Depends on:** HG-MTH-008.6 module (`dimension_spectrum.py`) — provides the on-circle/off-circle classifier and the \(S_n\) dimension-spectrum fixtures.  
**Status:** Exploratory empirical experiment. No theorem claim.  
**Date:** 2026-05-28

---

## 0. Purpose

EMR construct, for \(\lambda \in \mathbb{R}^n\), a sub-complex \(\Sigma(\lambda)\) of the Coxeter complex of \(S_n\). Its faces are ordered set partitions \(B_1|\cdots|B_k\) of \([n]\) satisfying

\[
\sum_{i \in B_1 \cup \cdots \cup B_j} \lambda_i > 0
\quad\text{for all } j<k.
\]

This experiment asks whether the dimension-spectrum coordinate from HG-MTH-008.6 has empirical purchase in this Coxeter-complex / weight-selection setting. The planned full experiment induces stabilizer homology representations up to \(S_n\), decomposes them into irreducibles, and measures on-circle versus off-circle multiplicity profiles.

The output is data, not a theorem. A supported result would be empirical evidence that the dimension-spectrum coordinate separates some sign-profile behavior. A negative result is also meaningful and must be recorded.

---

## 1. Claim discipline

### Standard / established

- **S1 — EMR construction.** \(\Sigma(\lambda)\) is the abstract simplicial complex whose \((k-1)\)-faces are ordered set partitions satisfying the positive-partial-sum condition above.
- **S2 — EMR Lemma 3.7.** For \(\tau \in S_n\), \(\Sigma(\lambda) \cong \Sigma(\tau\lambda)\) by permuting labels.
- **S3 — Stabilizer action.** \(\mathrm{Stab}_{S_n}(\lambda)\) acts on \(\Sigma(\lambda)\) by simplicial automorphisms.
- **S4 — Induced representation.** For \(H \le G\), \(\mathrm{Ind}_H^G W\) has dimension \([G:H]\dim W\), and Frobenius reciprocity controls multiplicities.
- **S5 — On-circle / off-circle.** In the HG-MTH-008.6 vocabulary, an irrep is on-circle iff \(\dim\rho=1\); for \(S_n\), \(n\ge 2\), the on-circle irreps are trivial and sign.

### Interpretive placement

The relevant representation for the full experiment is

\[
V_\lambda := \mathrm{Ind}_{\mathrm{Stab}(\lambda)}^{S_n}
\widetilde H_*(\Sigma(\lambda);\mathbb Q).
\]

The observables are:

\[
m_\circ(\lambda)
=
\langle \chi_{\mathbf 1}, \chi_{V_\lambda}\rangle
+
\langle \chi_{\mathrm{sgn}}, \chi_{V_\lambda}\rangle
\]

and

\[
m_\bullet(\lambda)
=
\sum_{\rho:\dim\rho>1}
\langle \chi_\rho, \chi_{V_\lambda}\rangle.
\]

The Plancherel-weighted off-circle mass is

\[
\mu_\bullet(\lambda)
=
\sum_{\rho:\dim\rho>1}
\langle \chi_\rho, \chi_{V_\lambda}\rangle
\cdot
\frac{(\dim\rho)^2}{|S_n|}.
\]

### Fenced non-theorem material

This experiment does not compute EMR's cohomology identities directly. EMR's identities involve averaged discrete-series characters of real reductive groups; this experiment computes finite-combinatorial \(S_n\)-data only.

This experiment does not compute \(L^2\)-cohomology of Siegel modular varieties or Shimura varieties.

This experiment has no implication for P vs NP, RH, GRH, Artin's conjecture, motives, or the standard conjectures.

This experiment does not promote the HG-MTH-008.6 analogy between \(\delta\) and \(\dim\rho-1\) into an equality.

---

## 2. Hypothesis to test

**P3-H — Sign-profile / dimension-spectrum coupling.** The ratio

\[
R(\lambda)=
\frac{m_\circ(\lambda)}
{m_\circ(\lambda)+m_\bullet(\lambda)}
\]

correlates non-trivially with the sign profile of \(\lambda\), especially with

\[
e(\lambda)=|\{i:\lambda_i>0\}|-|\{i:\lambda_i<0\}|
\]

and the partial-sum positivity rate

\[
p(\lambda)=
|\{j:\sum_{i\le j}\lambda_i>0\}|/n
\]

under a fixed ordering convention.

If P3-H is supported, it becomes empirical support only. If not, the negative result is recorded and PO-23 must look elsewhere.

---

## 3. Tranche plan

### Tranche 1 — geometric core

This PR lands only the construction layer:

- `ordered_set_partitions(n)`
- `sigma_lambda(lam)`
- `f_vector(complex)`
- `reduced_betti(complex)`
- `stabilizer(lam)`

The induced-representation machinery is intentionally excluded from tranche 1.

The gating sanity check is EMR Figure 1:

\[
\lambda=(5,1,-2,-3)
\]

must produce vertex set

\[
\{1\},\{2\},\{1,2\},\{1,3\},\{1,4\},\{1,2,3\},\{1,2,4\}
\]

and f-vector

\[
(7,12,6).
\]

Until this row is correct, no representation-theoretic or regression result is trustworthy.

### Tranche 2 — representation layer

After tranche 1 merges, add:

- `induce_to_Sn`
- `decompose_Sn_rep`
- `m_circle`
- `m_off`
- `mu_off`

Before tranche 2, check whether `dimension_spectrum.py` should expose shared \(S_n\) character-table helpers. If yes, land that dependency in a separate small PR.

### Tranche 3 — experiment run and report

After tranche 2 merges, add:

- `scripts/exp_008_8_emr_decomp.py`
- `data/exp_008_8_results.csv`
- `reports/exp_008_8_fit.json`
- `reports/HG-EXP-008.8-summary.md`
- plots for \(R(\lambda)\) vs \(e(\lambda)\) and multiplicity heatmaps.

---

## 4. Tranche 1 tests

The tranche 1 implementation is accepted only if these construction tests pass:

- `test_fubini_count`: ordered set partition counts match 13, 75, 541 for \(n=3,4,5\).
- `test_emr_figure_1_vertices`: \(\Sigma(5,1,-2,-3)\) has exactly the seven named vertices above.
- `test_emr_figure_1_fvector`: the same row has f-vector `(7, 12, 6)`.
- `test_all_positive_lambda_is_full_complex`: positive \(\lambda\) gives the full Coxeter complex.
- `test_all_negative_lambda_is_empty`: negative \(\lambda\) gives no non-empty faces.
- `test_lemma_37_isomorphism`: f-vector is invariant under permuting coordinates.
- `test_reduced_euler_characteristic`: reduced Euler characteristic agrees with reduced rational homology for the Figure 1 case.

---

## 5. Final acceptance criteria

The full experiment is accepted only when:

1. `data/exp_008_8_results.csv` contains valid rows through \(n=5\), and \(n=6\) if feasible.
2. EMR Figure 1 sanity row passes: f-vector `(7,12,6)` and Betti numbers are reported.
3. `reports/exp_008_8_fit.json` contains coefficients, confidence intervals, and \(R^2\).
4. Plots are committed.
5. Summary report gives a clear supported / not-supported / partial verdict on P3-H.
6. Tests pass.
7. PO-23 is updated according to the empirical verdict.

---

## 6. Non-claims

- Does not claim to reproduce, improve, or contradict EMR (2019) identities.
- Does not compute \(L^2\)-cohomology of Siegel modular varieties or Shimura varieties.
- Does not bear on P vs NP, RH, GRH, Artin's conjecture, motives, or the standard conjectures.
- Does not identify the HG-MTH-008.6 \(\delta\)-analogy with \(\dim\rho-1\).
- Does not compute integral torsion-bearing homology; tranche 1 and the planned experiment use rational coefficients only.
