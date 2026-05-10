# Calculus-Invariant Characters v2.1.3 Patch Plan

Tracking issue: HG-ANNEAL-001 / #6

Status: patch plan, not the final manuscript. This file defines the minimum edits needed to turn the expanded v2 draft into a disciplined v2.1.3 manuscript while preserving exploratory material in future-horizon lanes.

## 1. New abstract stance

The abstract must distinguish:

- established constructions;
- computed identities;
- analytic theorems;
- conjectural lifts;
- future-horizon bridges.

Required abstract replacement language:

```text
For a restricted proof fragment, a canonical normal-form representation, and a fixed statistic sigma, proof-family generating functions T_phi^sigma(x) define analytic objects whose Puiseux singularity channels yield finite phase reductions chi_p. These reductions are strictly multiplicative in no-carry regimes and fail strict multiplicativity by an explicitly computable mod-p carry term zeta_p. In the ordinary cochain setting zeta_p is a coboundary of q_p(alpha)=floor(p alpha) mod p, so it is a finite-resolution section defect rather than a nontrivial cohomological obstruction. Multi-shell Puiseux support refines the dominant-character construction. Regulator, Chern-class, recognition-dynamical, and nonassociative extensions are future work pending additional constructions.
```

## 2. Required section-level edits

### 2.1 Proof-class generating functions

- Define the proof fragment explicitly.
- Use canonical eta-long beta-normal de Bruijn lambda terms as the representation target.
- Treat `sigma` as a parameter, with `sigma_C` fixed only for this paper.
- Add a warning that calculus-invariance holds only after canonicalization.

### 2.2 Examples

- Chain example: mark as proof-family / analytic calibration unless a fixed proposition/type grammar is supplied.
- Catalan example: ground by explicit grammar, e.g. `C_A = (A -> A -> A) -> A -> A`, with `T ::= x | b(T,T)`, or label analytic calibration.
- No example may be used as theorem evidence unless its proof-type grounding is present.

### 2.3 Singularity and shell data

Replace naive local asymptotic definition with Puiseux-channel definition.

Required language:

```text
At a singular point rho, write t = 1 - x/rho and expand T(x) locally as an analytic germ plus singular or nonanalytic Puiseux channels. The exponent used by chi_p is a selected exponent channel beta, not necessarily the leading term of the full function.
```

Catalan must be described as analytic constant term plus square-root singular correction, with exponent `1/2` belonging to the leading nonanalytic channel.

### 2.4 Prime-indexed family and seed basis

Add before finite seed basis:

```text
The full prime-indexed fingerprint is (chi_p(T))_p in product_p mu_p. This is not interpreted as a convergent product in U(1).
```

Then keep `P_13={2,3,5,7,11,13}` as finite computational truncation.

### 2.5 Carry defect

Replace cohomological-obstruction and nonabelian-extension language.

Required theorem/correction:

```text
Let q_p(alpha)=floor(p alpha) mod p. Then zeta_p(alpha,beta)=q_p(alpha+beta)-q_p(alpha)-q_p(beta). Hence zeta_p is a coboundary in ordinary group cohomology with unrestricted cochains. It remains meaningful as the section defect of the chosen finite phase discretization, but it does not by itself define a nontrivial cohomology class or nonabelian extension.
```

Delete or move to future horizon:

- Heisenberg-style group;
- generally nonabelian extension;
- non-split central extension;
- abelian shadow of nonabelian structure.

### 2.6 Multi-shell theorem

Retain with strict scope:

- rational or algebraic generating functions;
- isolated local Puiseux expansions;
- support convolution with analytic-term collection and coefficient cancellation;
- no recognition-dynamical shell law.

### 2.7 Regulator / Chern class

Demote from theorem-core.

Use three subsections:

1. Local analytic `dlog` object for rational functions.
2. Algebraic case on normalization / ramified cover.
3. Future global lift blocked on proof moduli, sentence bundle/local system, connection, curvature, and base map.

No `c_1` claim may be stated as constructed.

### 2.8 Base-relative visibility

Keep flat/local-system visibility only.

- Distinguish `Hom(pi_1(M), U(1))` from singular cohomology with constant coefficients and sheaf cohomology.
- Keep S2/T2/K as examples of flat visibility only.
- Qualify Klein bottle as a useful base with continuous flat direction plus 2-torsion, not absolute smallest 2-torsion detector.

### 2.9 Future horizons

Move to future-horizon note references:

- Wythoff/Schwarz symmetry grammar;
- projection/preimage geometry;
- Temporal Mechanics / S4 recognition diagnostics;
- Moufang/octonionic associator;
- AdS/CFT/holography vocabulary;
- superconductivity / Fermi-Bose analogies.

## 3. Required regression tests

- `tests/test_carry_coboundary.py`: verifies `zeta_p = delta q_p`, symmetry, and selected table values.
- `tests/test_chain_product.py`: verifies ordinary product of `x/(1-x)^2` with itself is `x^2/(1-x)^4`, and separates triangular series as a different operation.
- `tests/test_seed_basis.py`: verifies `k_13(-2)=(0,0,0,0,0,0)` and `k_13(1/2)=(1,1,2,3,5,6)`.
- `tests/test_catalan_puiseux.py`: records that Catalan has analytic constant plus leading nonanalytic exponent `1/2`.

## 4. Stop conditions

Do not add new research lanes to the manuscript until:

- v1/v2 claim diff is complete;
- v2 claim status table is complete;
- carry-coboundary and chain-product regressions exist;
- regulator is demoted to future/global-lift target;
- all future-horizon material is routed out of theorem-core.

## 5. Principle

The purpose of v2.1.3 is not to make the manuscript smaller. It is to make the manuscript honest enough to support future exploration. Exploratory claims survive, but their status must be explicit.
