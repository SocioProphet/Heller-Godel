# HG-VOC-006 — Character Data and Finite Phase Reductions

Identifier: `HG-VOC-006`  
Layer: framework-vocabulary / Tier 2.  
Status: normalized character-data and finite phase-reduction vocabulary.  
Owner: `SocioProphet/Heller-Godel`.  
Claim level: vocabulary and source-identification discipline; not downstream deck-character or carry-cocycle promotion.

Normalized dependency: `HG-FND-003` at merge SHA `20499fcaa535e5dd4701aaf42fa582173c3ba746`, source `docs/framework-foundations/HG-FND-003-puiseux-singular-datum.md`.

## 1. Purpose and Tier 2 declaration

`HG-VOC-006` normalizes the vocabulary that compares manuscript finite phase conventions with global character-source data.

It is Tier 2 because it depends on normalized Tier 1 local input from `HG-FND-003` and supplies controlled vocabulary for `chi_p`, roots of unity, finite phase reductions, generator conventions, and source-identification claims.

It does not normalize deck-character interpretation, lifted phase index, section-defect carry, `zeta_3`, or `U(2)` correspondence.

## 2. Dependency on HG-FND-003

`HG-FND-003` supplies the local Puiseux datum at the chosen puncture. For P3.c it records:

```text
rho_3 = 4/27
C_3(rho_3)=3/2
alpha_3 = 1/2
t = 1 - x/rho_3
```

and the principal local expansion. That local square-root behavior is `mu_2`-type Puiseux data. It is not the `chi_3` source.

## 3. Global algebraic source

The global algebraic cover is:

```text
x y^3 - y + 1 = 0.
```

With reciprocal variable `z=1/y`, this is:

```text
z^3 - z^2 + x = 0.
```

The cubic has no root in `Q(x)`, hence it is irreducible over `Q(x)`. Its discriminant is:

```text
Delta = x(4 - 27x).
```

This discriminant is not a square in `Q(x)`, because it has simple zeros at `x=0` and `x=4/27`. Therefore the Galois group is:

```text
S_3.
```

The cyclic sheet-rotation subgroup is:

```text
A_3 ~= Z/3.
```

## 4. Generator convention and character value

The positive cyclic generator is declared to be:

```text
tau = (123).
```

Let:

```text
omega = exp(2 pi i / 3).
```

The normalized character convention is:

```text
chi_3(tau)=omega.
```

The reverse generator gives the conjugate value `omega^2`. Thus the primitive element depends on the generator convention, while the global source is the cyclic sheet-rotation subgroup.

## 5. Manuscript phase-map formula and alignment

The manuscript phase-map convention is:

```text
k_p(beta)=floor(p beta) mod p
chi_p^(rho,beta)(T)=exp(2 pi i k_p(beta)/p).
```

For:

```text
p=3
beta=1/2
```

we obtain:

```text
k_3(1/2)=floor(3/2) mod 3 = 1
chi_3=exp(2 pi i / 3)=omega.
```

This aligns with the declared global generator convention:

```text
chi_3(tau)=omega.
```

## 6. Operational substrate

`src/heller_godel/phase_characters.py` supplies the executable finite-character substrate:

```text
normalize_exponent
phase_index
p_primary_projection
prime_reduction
```

These functions implement finite phase arithmetic and regression-checkable phase reductions. They are operational substrate only. They are not the global Galois source of `chi_3`; that source is the `A_3` sheet-rotation subgroup of the cubic cover.

## 7. Boundary with HG-FND-006 and HG-FND-007

`HG-VOC-006` does not own:

- deck-character interpretation as a foundational surface;
- branch-killing cover action;
- lifted phase index;
- section-defect carry cocycle;
- `zeta_3` carry defect;
- `U(2)` correspondence;
- Deligne-unit or regulator-symbol refinements.

Those remain downstream candidate surfaces, especially `HG-FND-006` and `HG-FND-007`.

## 8. Discharge criterion

A downstream claim may cite normalized `HG-VOC-006` only when it supplies:

1. normalized local input from `HG-FND-003`, if a local Puiseux singularity is involved;
2. the global algebraic cover or finite phase object being interpreted;
3. the character group or subgroup, such as `A_3 ~= Z/3`;
4. generator convention, such as `tau=(123)`;
5. character value, such as `chi_3(tau)=omega`;
6. manuscript phase-map value, such as `k_3(1/2)=1`, if manuscript alignment is claimed;
7. explicit statement that local square-root sign-change behavior is not the `mu_3` character source;
8. no carry-cocycle, `zeta_3`, `U(2)`, or downstream monodromy / deck-character interpretation unless a later normalized surface supplies it.

## 9. Non-claims

This document does not normalize `HG-FND-006` or `HG-FND-007`.

This document does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This document does not prove a deck-character action on a branch-killing cover.

This document does not define or trivialize a carry cocycle.

This document does not supply `zeta_3`, `U(2)`, Deligne-unit, tame-symbol, or regulator-symbol content.

This document does not start P1 path-beta uniqueness or P2 candidate-list exhaustion.

This document does not authorize `A_n` extension or downstream repo work.
