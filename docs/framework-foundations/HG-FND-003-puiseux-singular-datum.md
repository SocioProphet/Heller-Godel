# HG-FND-003 — Puiseux Singular Datum at a Chosen Puncture

Identifier: `HG-FND-003`  
Layer: framework-foundational / Tier 1.  
Status: normalized Puiseux singular-datum foundation.  
Owner: `SocioProphet/Heller-Godel`.  
Claim level: framework-foundational definition and local-expansion discipline; not downstream character or carry promotion.

Normalized dependencies:

- `HG-FND-001`, source `docs/framework-foundations/HG-FND-001-restricted-proof-grammar.md`.
- `HG-FND-002`, source `docs/framework-foundations/HG-FND-002-proof-class-generating-function.md`.

## 1. Purpose

`HG-FND-003` normalizes the Puiseux singular datum attached to a chosen puncture of a declared proof-family generating function.

It begins after `HG-FND-002` has identified:

```text
rho = dominant singularity
alpha = rational Puiseux exponent
```

and records the additional local data required before downstream surfaces may cite a Puiseux expansion.

This document does not own character data, roots of unity, finite phase reductions, monodromy / deck-character interpretation, or lifted carry-cocycle material.

## 2. Puiseux singular-datum package

A normalized Puiseux singular datum consists of:

1. a declared generating function `T(x)` already licensed by `HG-FND-002`;
2. a chosen puncture `rho`;
3. a local coordinate, such as `t = 1 - x/rho`;
4. a chosen branch convention;
5. a rational exponent `alpha` in lowest terms;
6. a local expansion through the declared order;
7. an explicit statement of what downstream interpretation is not licensed by the local expansion.

For P3.c, the generating function is:

```text
C_3(x)=1+x C_3(x)^3.
```

## 3. Coordinate relation with HG-FND-001 and HG-FND-002

The arity-three constructor-shape coordinate `x` and the full node-count coordinate `y` are related by the normalized `HG-FND-001` statistic relation:

```text
T_3^{sigma_C}(y) = y^3 C_3(y^5).
```

Thus the constructor-shape singularity:

```text
x = rho_3 = 4/27
```

corresponds in full node-count coordinate to any declared fifth root:

```text
y^5 = 4/27.
```

A downstream citation must declare which coordinate system it uses before citing the puncture or Puiseux expansion. The P3.c local expansion below is in constructor-shape coordinate `x`, not full node-count coordinate `y`.

## 4. P3.c chosen puncture and local coordinate

The normalized A2 / arity-three puncture is:

```text
rho_3 = 4/27.
```

The critical value is:

```text
C_3(rho_3)=3/2.
```

The local coordinate is the scaled coordinate:

```text
t = 1 - x/rho_3.
```

The exponent is:

```text
alpha_3 = 1/2.
```

## 5. Principal branch expansion

With:

```text
x = rho_3(1-t)
y = C_3(x) = 3/2 + s,
```

the defining equation gives the local balance:

```text
s^2 = (3/4)t.
```

For the principal branch selected by `C_3(0)=1`, the branch approaches `3/2` from below as `x -> rho_3^-`, so:

```text
s = -(sqrt(3)/2)t^(1/2) + (2/3)t + O(t^(3/2)).
```

Therefore:

```text
C_3(x)=3/2 - (sqrt(3)/2)t^(1/2)
       + (2/3)t
       + O(t^(3/2)).
```

This is the normalized Puiseux singular datum for the P3.c constructor-shape coordinate.

## 6. Boundary with HG-VOC-006

The local square-root channel has sign-change behavior under a loop around the puncture:

```text
t^(1/2) -> -t^(1/2).
```

This is local `mu_2`-type Puiseux behavior. It is not the source of `chi_3 in mu_3`.

`HG-VOC-006` owns character data, roots of unity, finite phase reductions, and any source-identification of `chi_3`. `HG-FND-003` supplies only the local Puiseux singular datum.

## 7. Boundary with HG-FND-006 and HG-FND-007

`HG-FND-003` does not own:

- finite monodromy / deck-character interpretation;
- lifted phase index;
- section-defect carry cocycle;
- `zeta_3` carry defect;
- `U(2)` correspondence;
- Deligne-unit or regulator-symbol refinements.

Those remain downstream candidate surfaces.

## 8. Discharge criterion

A downstream claim may cite normalized `HG-FND-003` only when it supplies:

1. a generating function already licensed by `HG-FND-002`;
2. the coordinate system used for the singularity;
3. the chosen puncture `rho`;
4. the local coordinate;
5. branch convention;
6. rational exponent `alpha`;
7. local expansion through the cited order;
8. an explicit statement that local Puiseux behavior is not character-source data unless a downstream normalized surface supplies that interpretation.

## 9. Non-claims

This document does not normalize `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`.

This document does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This document does not identify local square-root monodromy at `rho_3` as the source of `chi_3 in mu_3`.

This document does not supply finite phase reductions, roots-of-unity character data, deck-character interpretation, carry-cocycle material, or `U(2)` correspondence.

This document does not prove path-beta uniqueness or candidate-list exhaustion.

This document does not extend the framework to an `A_n` family.

This document does not authorize Heller-Einstein, Heller-Dirac, `yang-mills`, `np-program`, BSD, Heller-Winters, or `ns-program` work.
