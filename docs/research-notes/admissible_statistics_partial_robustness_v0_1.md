# HG-STAT-001: Partial Robustness for Admissible Constructor-Linear Statistics

## A Standalone Note Companion to *Calculus-Invariant Phase Characters from Proof-Class Generating Functions* v2.1.3

**Status:** v0.1 — theorem for two calibration families; general regular/algebraic/D-finite proof grammar extension conjectural.

---

## Abstract

The parent paper (Heller, *Calculus-Invariant Phase Characters from Proof-Class Generating Functions*, v2.1.3, henceforth CIPC) establishes that the proof-class generating function \(T_\phi^\sigma(x)\) is invariant under choice of proof calculus after canonicalization, but depends on the choice of intrinsic statistic \(\sigma\) (Appendix A.5). CIPC §10 lists statistic-class robustness — preservation of analytic features across some admissible class of statistics — as the natural sequel direction.

This note proposes a precise admissibility class, positive-weight linear combinations of node counts in the de Bruijn syntax tree, and proves that two calibration families preserve analytic type, dominant radius, and dominant local exponent across that class. The proofs are by direct enumeration and closed-form summation. The result is theorem-level for the two tested families and conjectural for general proof grammars.

This note does not patch CIPC v2.1.3. It is a standalone companion artifact. CIPC's claim discipline is unchanged.

---

## 1. Background

CIPC v2.1.3 establishes:

1. **Calculus-invariance after canonicalization (CIPC §2.2).** For any fixed intrinsic statistic \(\sigma\) and after canonicalization to \(\eta\)-long \(\beta\)-normal de Bruijn \(\lambda\)-terms, \(T_\phi^\sigma\) depends only on the alpha-equivalence class of normal proofs of \(\phi\).
2. **Statistic-relativity (CIPC §2.2, A.5).** Different intrinsic statistics on the same alpha-class enumeration produce different generating functions. The construction is statistic-relative; \(\sigma\) is part of the specification.
3. **Open question (CIPC §10).** Whether the analytic type of \(T_\phi^\sigma\) is preserved across some admissible class of statistics is left as the natural sequel.

The current note proposes a precise definition of admissibility and gives a partial answer.

## 2. Admissible constructor-linear statistics

Let \(s\) denote an \(\eta\)-long \(\beta\)-normal de Bruijn \(\lambda\)-term, viewed as a labeled tree with three node types: \(\lambda\)-abstractions, application nodes, and variable occurrences. Write \(|\lambda(s)|\), \(|\mathrm{app}(s)|\), \(|\mathrm{var}(s)|\) for the respective counts.

**Definition 2.1 (admissible constructor-linear statistic).** A statistic \(\sigma : \mathcal N_\phi \to \mathbb Z_{\geq 0}\) is *admissible (constructor-linear)* if it is a positive-weight linear combination of node counts:

\[
\sigma_w(s) = w_\lambda \cdot |\lambda(s)| + w_{\mathrm{app}} \cdot |\mathrm{app}(s)| + w_{\mathrm{var}} \cdot |\mathrm{var}(s)|,
\]

with \(w_\lambda, w_{\mathrm{app}}, w_{\mathrm{var}} \in \mathbb Z_{>0}\).

**Properties motivating the class.** Constructor-linear statistics have the following structural features. They are *not* claimed as a complete iff characterization without further restricting the syntax alphabet and forbidding additional finite-state annotations.

- **(P1) Locality with respect to the three-node alphabet.** \(\sigma_w(s)\) is computable by a bottom-up tree traversal in which each node contributes a constant amount depending only on which of \(\{\lambda,\mathrm{app},\mathrm{var}\}\) it is.
- **(P2) Linearity.** \(\min(w_\lambda,w_{\mathrm{app}},w_{\mathrm{var}})\cdot |s| \leq \sigma_w(s) \leq \max(w_\lambda,w_{\mathrm{app}},w_{\mathrm{var}})\cdot |s|\), where \(|s|\) is total node count.
- **(P3) Sum-compositionality.** \(\sigma_w\) decomposes additively, not by max and not by product, over subterms, so grammar-level recursion translates directly into algebra on the generating function.

The canonical CIPC choice \(\sigma_C\) corresponds to \(w=(1,1,1)\) and is admissible.

**Why the falsifier statistics from CIPC A.5 are non-admissible.**

- \(\sigma_D\), term depth, is not a constructor-linear statistic. Depth is max-aggregated over subterms, not sum-aggregated, so it fails (P3). It also fails (P2) on balanced trees, where \(\sigma_D(s)=O(\log |s|)\).
- \(\sigma_B\), de Bruijn index sum at variable head positions, is locally computable if the variable label includes its de Bruijn integer index, but its contribution is not a constant per node class in the three-node alphabet \(\{\lambda,\mathrm{app},\mathrm{var}\}\). The contribution of a variable depends on its label, which encodes information about the depth of the binder it refers to. Thus \(\sigma_B\) does not satisfy (P1) under the three-node alphabet, and it is not a constructor-linear functional in the sense of Definition 2.1. If the alphabet were enriched to label each variable with its de Bruijn index, \(\sigma_B\) would become locally computable in that richer alphabet, but it would no longer be a constructor-linear statistic in this restricted sense.

The exclusion is exactly the falsifier from CIPC A.5: the statistics that disagreed with \(\sigma_C\) are precisely the ones excluded from the admissibility class.

## 3. Theorem: chain family robustness

**Theorem 3.1.** *For the chain family \(\phi_n=A^{(n+1)}\), with \(n\) as a family parameter, each inhabitant of \(\phi_n\) has the form \(\lambda x_n.\cdots \lambda x_1.x_i\) for some \(i\in\{1,\ldots,n\}\). Thus each inhabitant has*

\[
|\lambda|=n,\qquad |\mathrm{app}|=0,\qquad |\mathrm{var}|=1.
\]

*Under any admissible weight vector \(w=(w_\lambda,w_{\mathrm{app}},w_{\mathrm{var}})\):*

\[
\sigma_w(\text{inhabitant of }\phi_n)=w_\lambda n+w_{\mathrm{var}}.
\]

*The family-level generating function is*

\[
T_{\mathrm{chain}}^{\sigma_w}(x)=\sum_{n\geq1} n x^{w_\lambda n+w_{\mathrm{var}}}=\frac{x^{w_\lambda+w_{\mathrm{var}}}}{(1-x^{w_\lambda})^2}.
\]

*Therefore \(T_{\mathrm{chain}}^{\sigma_w}\) is rational for every admissible \(w\), with dominant radius shell \(|\rho|=1\) at every root of \(x^{w_\lambda}=1\), and double-pole local exponent \(\alpha=-2\) at the positive root \(\rho=1\).* 

**Proof.** The inhabitant set of \(\phi_n\) has cardinality \(n\), one inhabitant per choice of returned variable. The constructor counts are read directly from the term shape. The summation is the standard identity \(\sum_{n\geq1}n y^n=y/(1-y)^2\) with \(y=x^{w_\lambda}\), multiplied by \(x^{w_{\mathrm{var}}}\). Rationality is immediate, and the singular structure follows from inspecting the denominator. \(\square\)

## 4. Theorem: \(((A\to A)\to A)\to A\) family robustness

**Theorem 4.1.** *For the family \(T=((A\to A)\to A)\to A\), there are exactly \(n\) normal inhabitants \(t_{n,i}\), \(1\leq i\leq n\), of the form*

\[
t_{n,i}=\lambda f.\, f(\lambda x_1.\, f(\lambda x_2.\, \cdots f(\lambda x_n.\, x_i)\cdots)).
\]

*Each inhabitant has*

\[
|\lambda|=n+1,\qquad |\mathrm{app}|=n,\qquad |\mathrm{var}|=n+1.
\]

*Under any admissible weight vector \(w\):*

\[
\sigma_w(t_{n,i})=(w_\lambda+w_{\mathrm{app}}+w_{\mathrm{var}})n+(w_\lambda+w_{\mathrm{var}}).
\]

*Setting \(d=w_\lambda+w_{\mathrm{app}}+w_{\mathrm{var}}\) and \(c=w_\lambda+w_{\mathrm{var}}\):*

\[
T_T^{\sigma_w}(x)=\sum_{n\geq1} n x^{dn+c}=\frac{x^{d+c}}{(1-x^d)^2}=\frac{x^{2w_\lambda+w_{\mathrm{app}}+2w_{\mathrm{var}}}}{(1-x^{w_\lambda+w_{\mathrm{app}}+w_{\mathrm{var}}})^2}.
\]

*Therefore \(T_T^{\sigma_w}\) is rational for every admissible \(w\), with dominant radius shell \(|\rho|=1\) and double-pole local exponent \(\alpha=-2\) at \(\rho=1\).* 

**Proof.** Constructor counts are read from the term shape. The summation is again \(\sum n y^n=y/(1-y)^2\) with \(y=x^d\), multiplied by \(x^c\). \(\square\)

**Corollary 4.2.** *For both calibration families simultaneously, analytic type (rational), dominant radius shell \(|\rho|=1\), and dominant local exponent \(\alpha=-2\) are independent of the choice of admissible weight vector.*

## 5. Tested weights

Direct enumeration up to \(n=8\) confirms the closed-form predictions for the following weight vectors.

| \(w=(w_\lambda,w_{\mathrm{app}},w_{\mathrm{var}})\) | Chain \(T_{\mathrm{chain}}^{\sigma_w}\) | \(T\)-family \(T_T^{\sigma_w}\) | Status |
|---|---|---|---|
| \((1,1,1)\) | \(x^2/(1-x)^2\) | \(x^5/(1-x^3)^2\) | admissible |
| \((1,2,1)\) | \(x^2/(1-x)^2\) | \(x^6/(1-x^4)^2\) | admissible |
| \((2,1,1)\) | \(x^3/(1-x^2)^2\) | \(x^7/(1-x^4)^2\) | admissible |
| \((1,1,2)\) | \(x^3/(1-x)^2\) | \(x^7/(1-x^4)^2\) | admissible |
| \((3,1,1)\) | \(x^4/(1-x^3)^2\) | \(x^9/(1-x^5)^2\) | admissible |
| \((1,3,1)\) | \(x^2/(1-x)^2\) | \(x^7/(1-x^5)^2\) | admissible |
| \((5,1,1)\) | \(x^6/(1-x^5)^2\) | \(x^{13}/(1-x^7)^2\) | admissible |
| \((1,1,0)\) | \(x/(1-x)^2\) | \(x^3/(1-x^2)^2\) | boundary, non-admissible |

In every admissible row: rational, \(|\rho|=1\), \(\alpha=-2\).

The weight \((1,1,0)\) violates the strict positivity in Definition 2.1 because it sets \(w_{\mathrm{var}}=0\), and is included as a boundary check. It still produces a rational GF with \(|\rho|=1\) and \(\alpha=-2\) on these test families, suggesting that Definition 2.1 might be relaxable to non-negative weights with at least one positive weight per node-class actually present in the family. This note does not pursue that loosening.

## 6. Why the parent falsifier still stands

CIPC A.5's falsifier showed that \(T_T^{\sigma_C}\) and \(T_T^{\sigma_B}\) have different dominant exponents, \(-2\) and \(-1\) respectively, and different generating functions on the \(((A\to A)\to A)\to A\) family. That falsifier remains valid because \(\sigma_B\) is not admissible per Definition 2.1.

Theorems 3.1 and 4.1 do not contradict the falsifier. They state that within the admissibility class, the analytic features are preserved; they say nothing about non-admissible statistics like \(\sigma_D\) and \(\sigma_B\), which can and do produce different generating functions.

The two results sit in complementary classes:

- **Falsifier (CIPC A.5):** statistic-invariance fails across the admissible vs. non-admissible boundary.
- **Robustness (this note):** within the admissible class, the two calibration families produce identical analytic features.

## 7. General theorem target (conjectural)

The natural conjecture is that the result extends to proof-family generating functions arising from sufficiently structured grammars. We state this in two tiers, separated to prevent the partial result from overgrowing into a false universal claim.

**Conjecture 7.1 (weak conjecture: analytic type preservation).** *Let \(\phi\) be a proposition or family of propositions whose normal-inhabitant grammar is regular, respectively algebraic or D-finite, and let \(\sigma_w\) be admissible per Definition 2.1. Then \(T_\phi^{\sigma_w}(x)\) is rational, respectively algebraic or D-finite. The analytic class is preserved across the admissibility class.*

**Counterexample warning for radius preservation.** A general regular grammar with two distinct token types can produce different radii under different positive weights. For instance, a one-letter alphabet with weight \(1\) yields \(1/(1-x)\), while rebalancing to two tokens with weights \(1\) and \(2\) yields \(1/(1-x-x^2)\). Both are rational, but the singular radius shifts from \(1\) to \(1/\varphi\). Thus the strong conjecture below requires additional hypotheses.

**Conjecture 7.2 (strong conjecture: radius/exponent preservation under rank-uniformity).** *Suppose additionally that the proof-family grammar is rank-uniform, meaning each inhabitant at level \(n\) has the same node-class profile \((|\lambda|,|\mathrm{app}|,|\mathrm{var}|)\) depending only on \(n\), or more generally satisfies a singular-schema-stability condition under positive-weight rescaling. Then, in addition to analytic type, the dominant radius shell \(|\rho|\) and dominant local exponent at \(\rho\) are preserved across the admissibility class.*

The two calibration families in §§3–4 are rank-uniform: every chain inhabitant at level \(n\) has profile \((n,0,1)\), and every \(T\)-family inhabitant at level \(n\) has profile \((n+1,n,n+1)\). Thus Theorems 3.1 and 4.1 are the rank-uniform special case of the strong conjecture.

**Proof strategy for Conjecture 7.1 (sketch).** For regular grammars, the inhabitant set is generated by a finite-state automaton on the syntax tree; weighted constructor counts pull back to a weighted transition matrix on the automaton. Standard transfer-matrix theory then produces a rational GF whose poles are determined by the spectrum of the transition matrix. Different positive weights give different transition matrices, but rationality is preserved because rationality is exactly the class generated by transfer-matrix sums.

For algebraic grammars, kernel-method and quadratic-method arguments produce algebraic GFs from algebraic grammars; weight rescaling produces a substitution of variables in the polynomial defining equation, preserving algebraicity.

For D-finite grammars, the inhabitant generating function satisfies a linear ODE with polynomial coefficients; weight rescaling gives a substitution that preserves D-finiteness under the appropriate closure hypotheses.

Carrying out these arguments rigorously requires:

1. A precise statement of regular, algebraic, and D-finite proof grammars in the de Bruijn / Curry-Howard setting.
2. A precise statement of how positive-weight rescaling acts on the transfer matrix, algebraic equation, or linear ODE.
3. Verification on at least one non-trivial algebraic example, such as the Catalan-grounded type \(C_A\) from CIPC §2.3, to confirm the strategy works beyond rational rank-uniform cases.

## 8. What this note establishes / does not establish

**Established (theorem-level):**

- A precise definition of admissible constructor-linear statistic (Definition 2.1).
- \(\sigma_D\), depth, and \(\sigma_B\), de Bruijn index sum, are non-admissible under Definition 2.1, consistent with their role as the falsifier statistics in CIPC A.5.
- For the chain family (Theorem 3.1) and the \(((A\to A)\to A)\to A\) family (Theorem 4.1): rational analytic type, dominant radius shell \(|\rho|=1\), and dominant local exponent \(\alpha=-2\) are all preserved across the admissibility class. Proofs are direct enumeration and closed-form summation.

**Conjectural:**

- Weak conjecture (Conjecture 7.1): analytic type preservation for general regular/algebraic/D-finite proof grammars across the admissibility class.
- Strong conjecture (Conjecture 7.2): radius and exponent preservation, under additional rank-uniformity or singular-schema-stability hypotheses.

**Not addressed:**

- Behavior on non-admissible statistics such as \(\sigma_D\), \(\sigma_B\), and others. The CIPC A.5 falsifier stands.
- Multi-shell character data \(\chi_p^{(\rho,\beta)}\) from CIPC §§4.7–4.11 across the admissibility class. The two test families have only one non-trivial shell each; the multi-shell version is open.
- Whether analogous robustness results hold for character data \(\chi_p\) extracted from the GF. On the test families, \(\alpha=-2\) for both, hence \(\chi_p\equiv1\) for all \(p\) across the admissibility class. This is a corollary of integer-valued \(\alpha\), not a statement about \(\chi_p\) in general.

## 9. Relationship to CIPC v2.1.3

This note does not require revision to CIPC v2.1.3. The parent paper's claim discipline is unchanged:

- CIPC §2.2 still says calculus-invariance holds after canonicalization for fixed \(\sigma\).
- CIPC §2.2 and A.5 still say statistic-invariance fails, with \(\sigma_D\) and \(\sigma_B\) as falsifiers.
- CIPC §10 still lists statistic-class robustness as an open question.

This note refines CIPC §10 by proposing what admissible should mean (Definition 2.1) and by establishing partial robustness as a theorem on two calibration families. It does not contradict any claim in CIPC.

**Optional cross-reference for a future CIPC v2.2.** If CIPC is revised again, §10 could be updated to read:

> Statistic-class robustness across the admissibility class of positive-weight constructor-linear statistics (Definition 2.1 of HG-STAT-001) is established as a theorem on the two calibration families used in this paper (Theorems 3.1 and 4.1 of HG-STAT-001). The general extension to regular/algebraic/D-finite proof grammars is conjectural (Conjectures 7.1–7.2 of HG-STAT-001) and is the natural sequel.

This cross-reference is optional. CIPC v2.1.3 stands as is.

---

## Appendix A: Test specification

A regression harness for this note lives in `tests/test_admissible_statistics.py`.

The harness encodes the closed-form predictions and verifies them by direct enumeration on inhabitants up to \(n=8\). The relevant test cases are:

- admissible weights for the chain family;
- admissible weights for the \(T\)-family;
- the non-admissible boundary weight \((1,1,0)\), which still matches the formulas on the two calibration families.

## Appendix B: Detailed verification for \(w=(1,1,1)\)

For the \(((A\to A)\to A)\to A\) family with canonical weights:

| \(n\) | \(i\) | \(\sigma_w(t_{n,i})\) |
|---|---|---|
| 1 | 1 | 5 |
| 2 | 1 | 8 |
| 2 | 2 | 8 |
| 3 | 1 | 11 |
| 3 | 2 | 11 |
| 3 | 3 | 11 |
| 4 | 1 | 14 |
| … | … | … |

Coefficient sequence:

\[
(c_5,c_8,c_{11},c_{14},\ldots)=(1,2,3,4,\ldots).
\]

Closed-form prediction:

\[
\frac{x^5}{(1-x^3)^2}=x^5\sum_{k\geq0}(k+1)x^{3k},
\]

which gives the same coefficient sequence. These match across \(n=1,\ldots,8\). Analogous verification for the other admissible weight vectors in §5 also passes.

## Document history

- **v0.1** — initial release. Theorems 3.1 and 4.1 stated and proved by direct closed-form summation. Conjectures 7.1 and 7.2 stated separately (weak/strong tier) with explicit counterexample warning for radius preservation in general regular grammars. Regression harness specified in Appendix A and implemented in `tests/test_admissible_statistics.py`.

---

## Erratum (added after HG-STAT-002 v0.1)

After the initial release of this note, the Catalan-grounded type \(C_A = (A \to A \to A) \to A \to A\) was tested under the same admissibility framework. The result, recorded in HG-STAT-002 v0.1, refutes the strong conjecture stated in §7.2 of this note as originally written.

**Specifically:**

- §7.2 conjectured that *rank-uniformity* of a proof grammar would be sufficient to guarantee preservation of dominant singular radius across the admissibility class.
- HG-STAT-002 Theorems 4.1 and 4.2 show that this is false. The Catalan-grounded type is rank-uniform, but its dominant radius shifts as \(|\rho_w| = 4^{-1/a(w)}\) where \(a(w)\) depends linearly on \(w_{\mathrm{app}}\) and \(w_{\mathrm{var}}\).
- The chain and T-family preservation of \(|\rho| = 1\) that motivated §7.2 is now understood as the special case in which the underlying singular schema has \(\rho_y = 1\), which happens to be invariant under monomial substitution. It is *not* a general consequence of rank-uniformity.

**What §7.2 should now read.** §7.2 as written is superseded. The refined picture is:

- *Type preservation* (the weak conjecture, §7.1) remains conjectured for general regular/algebraic/D-finite proof grammars. HG-STAT-002 provides positive evidence in the algebraic setting.
- *Exponent preservation* under rank-uniformity is conjectured separately (HG-STAT-002 Conjecture 6.2). Holds on chain (\(\alpha = -2\)), T-family (\(\alpha = -2\)), and Catalan (\(\alpha = 1/2\)).
- *Radius preservation* under rank-uniformity is *false* in general; instead, the dominant radius covaries under monomial regrading induced by weight rescaling (HG-STAT-002 Conjecture 6.3).

**What is unaffected.** Theorems 3.1 (chain) and 4.1 (T-family) of this note remain correct as stated. Their preservation of \(|\rho| = 1\) is a consequence of the underlying GF having a singular schema with \(\rho_y = 1\), not a general property of rank-uniformity. The type-preservation aspect of those theorems still holds, and is consistent with the refined Conjecture 6.1.

**Action.** Readers of this note should treat §7.2 as historical and refer to HG-STAT-002 v0.1 §6 for the current conjecture hierarchy. A future v0.2 of this note may inline the correction; for now, this erratum block records the change without revising the body.

**Issue cross-reference.** See issue #7 (or successor) for repository tracking, and HG-STAT-002 v0.1 for the full Catalan analysis and refined conjecture statements.

---

**End of erratum.**
