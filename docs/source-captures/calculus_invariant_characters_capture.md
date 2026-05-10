# Calculus-Invariant Characters - Markdown Capture

Sources:

- `calculus invariant characters v2(2).pdf`  
  Classification: primary / load-bearing  
  SHA-256: `21738175a878d4903066f12e16a28de2e041e3759ea843ef9ccf165baad8c19c`
- `calculus invariant characters(2).pdf`  
  Classification: primary / regression / comparison  
  SHA-256: `17e7821319a95796f58e5622f7ed0f75ea80071f5cbd46ef6521234be2af01d9`

## Purpose

This capture preserves the technical core of the proof-character manuscript and the correction path leading to v2.1.3. It is not itself the corrected manuscript. It records source content, review findings, and the exact boundaries that must be enforced in the manuscript.

## Original technical aim

The working paper proposes to replace presentation-relative rule-count characters with analytic invariants extracted from proof-class generating functions.

The original chain was:

```text
formal theory T + sentence/type phi
-> normal proof class N_phi
-> intrinsic statistic sigma
-> generating function T_phi^sigma(x)
-> dominant singularity / local exponent
-> prime-indexed phase character chi_p
-> multiplicativity defect zeta_p
-> possible regulator / base-manifold obstruction theory
```

## Proof-class generating function

For a proposition or type `phi`, let `N_phi` be a set of normal proof terms after a chosen normalization convention. With a fixed intrinsic statistic `sigma`, define:

```math
T_phi^sigma(x) = sum_{s in N_phi} x^{sigma(s)}.
```

The repository correction is that this object is statistic-relative. The statistic must be chosen and fixed. Constructor count, depth, and de Bruijn-weight statistics may produce different generating functions and different shell structure.

## Canonical statistic boundary

The corrected manuscript should use:

```text
sigma_C = canonical constructor-count statistic after translation into eta-long beta-normal de Bruijn lambda terms.
```

The phrase `normal lambda terms up to alpha beta eta` is too loose for size statistics. The corrected form should be one of:

```text
alpha-classes of eta-long beta-normal forms
```

or

```text
beta-eta equivalence classes represented by canonical normal forms
```

## Calculus invariance correction

The earlier source says Curry-Howard preserves both indexing set and statistic. The correction is:

```text
calculus-invariance holds only after canonicalization into a shared normal-form representation and for a fixed statistic.
```

Curry-Howard preserves proof content under translation, but it does not automatically preserve constructor counts across natural deduction, sequent calculus, and combinatory logic unless all presentations are transported into the same representation.

## Worked analytic examples

### Chain example

The source uses a family-level chain example:

```math
T_chain(x) = sum_{n >= 1} n x^n = x/(1-x)^2.
```

Correction: this is a proof-family generating function, not necessarily `T_phi` for a single fixed proposition. It can remain as an analytic calibration example.

### Catalan example

The source uses the Catalan generating function:

```math
C(x) = 1 + x C(x)^2,
C(x) = (1 - sqrt(1-4x))/(2x).
```

Correction: near `x=1/4`, the local form has an analytic constant plus a square-root Puiseux correction:

```math
C(x) = 2 - 2(1-4x)^{1/2} + ...
```

Thus the exponent `1/2` is a leading nonanalytic Puiseux channel, not the leading term of the full local germ.

## Prime-indexed phase map

For a selected local exponent channel `alpha`, the phase map is:

```math
chi_p(alpha) = exp(2 pi i * ((floor(p alpha) mod p)/p)).
```

The full object should be the prime-indexed family:

```math
bold chi(T_phi) = (chi_p(T_phi))_p in product_p mu_p.
```

It should not be written as an ordinary convergent product in `U(1)`. For example, for `alpha=1/2`, the prime components remain nontrivial at every prime.

## Finite arithmetic seed basis

The finite computational truncation is:

```math
P_13 = {2,3,5,7,11,13}.
```

For rational exponent `alpha`:

```math
k_13(alpha) = (floor(p alpha) mod p)_{p in P_13}.
```

Examples:

```math
k_13(-2) = (0,0,0,0,0,0)
```

```math
k_13(1/2) = (1,1,2,3,5,6)
```

This is a computational truncation, not a complete invariant.

## Carry defect zeta_p

The source defines:

```math
zeta_p(alpha,beta)
= floor(p(alpha+beta)) - floor(p alpha) - floor(p beta) mod p.
```

This is a true arithmetic identity and a real multiplicativity defect for the selected finite section.

Key examples:

```math
zeta_13(1/2,1/2) = (0,1,1,1,1,1)
```

```math
zeta_13(1/2,1/3) = (0,0,1,0,1,0)
```

## Critical correction: zeta_p is a coboundary

Define:

```math
f_p(alpha) = floor(p alpha) mod p.
```

Then:

```math
zeta_p(alpha,beta) = f_p(alpha+beta) - f_p(alpha) - f_p(beta).
```

Therefore, in ordinary group cohomology with arbitrary cochain changes of section allowed, `zeta_p` is a coboundary:

```math
[zeta_p] = 0.
```

Consequences:

- `zeta_p` is not by itself a nontrivial group-cohomological obstruction.
- the extension built from it is split once the cochain `f_p` is allowed;
- it is symmetric, so it does not generate a nonabelian extension;
- it is best described as a finite-resolution section defect.

This is the main correction required for v2.1.3.

## Chain-product correction

The source says the type product chain x chain gives:

```math
x^2/(1-x)^3.
```

But if ordinary generating-function multiplication is intended and:

```math
T_chain(x)=x/(1-x)^2,
```

then:

```math
T_chain(x)^2 = x^2/(1-x)^4.
```

The triangular series:

```math
x^2/(1-x)^3
```

belongs to a different same-index aggregation or quotient/symmetrized product. The product operation must be named and defined separately if the triangular form is retained.

## Multi-shell / Puiseux correction

The corrected manuscript should extract characters from exponent channels:

```math
T(x)=A_rho(t)+sum_{beta in A_rho(T)} c_{rho,beta} t^beta,
quad t=1-x/rho.
```

The shell support records:

```math
S(T) = {(rho, A_rho(T))}.
```

The shell-product theorem should be local Puiseux-support convolution, not naive leading-exponent addition.

## Regulator/Chern-class correction

The original v2 source pushes toward:

```math
omega_phi = (2 pi i)^{-1} d log T_phi.
```

and then a Chern-class lift. The correction is:

- for rational functions, `d log T` records divisor data;
- for algebraic functions, one must pass to a normalization/ramified cover where `T` becomes single-valued;
- a Chern-class construction needs a line bundle/local system, a connection, curvature, and a map from a base into a proof-moduli space;
- the current manuscript has only a candidate future direction, not a constructed Chern-class lift.

## Base-manifold pairing correction

The base-relative idea is retained, but coefficient discipline is required:

- flat `U(1)` local systems are classified by `Hom(pi_1(M), U(1))`;
- line bundles are classified by `H^2(M; Z)` via `c_1`;
- sheaf cohomology and singular cohomology should not be casually conflated.

The Klein bottle remains useful as a minimal closed surface carrying both a continuous flat direction and 2-torsion, but it should not be described as the smallest possible space with 2-torsion without qualification.

## Required v2.1.3 manuscript corrections

1. Replace nontrivial central-extension language with coboundary/section-defect language.
2. Define local exponents as Puiseux exponent channels.
3. Reclassify chain and Catalan examples as calibration unless grounded by explicit types.
4. Correct the chain-product algebra.
5. State calculus-invariance only after canonicalization.
6. Add the prime-indexed family `(chi_p)_p in product_p mu_p` before finite `P_13` truncation.
7. Demote regulator/Chern material to future construction.
8. Fix all markdown/math corruption from pasted drafts.

## Repository routing

- Current theorem core: `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`.
- Tests: `src/heller_godel/phase.py`, `tests/test_phase.py`, plus future Puiseux/statistic/chain-product tests.
- Future horizon: regulator, Chern-class, sheaves, proof moduli, operator shells, nonassociative holonomy.
