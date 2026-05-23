# HG-FND-004 — Branch-Killing Cover and Singular Unit Upstairs

Identifier: `HG-FND-004`  
Layer: framework-foundational / Tier 1.  
Status: normalized branch-killing cover and singular-unit-upstairs foundation.  
Owner: `SocioProphet/Heller-Godel`.  
Claim level: local geometric / analytic construction; not Deligne-unit, tame-symbol, regulator, or downstream theorem promotion.

## 1. Purpose and Tier 1 declaration

`HG-FND-004` normalizes the branch-killing cyclic cover and the singular unit upstairs.

It constructs the cover used later by `HG-FND-006`, and it defines the upstairs singular unit as an object on that cover.

## 2. Dependency on HG-FND-003

`HG-FND-003` supplies the local Puiseux datum:

```text
local coordinate u
chosen puncture
branch convention
Puiseux exponent alpha = a/N
```

`HG-FND-004` uses those data to construct the cover. A citation to `HG-FND-004` is invalid without declaring the base local datum, level, and branch convention inherited from `HG-FND-003`.

## 3. Interface with HG-FND-006

`HG-FND-006` uses the branch-killing cover for deck-character realization.

`HG-FND-004` owns the constructed cover and singular unit upstairs. `HG-FND-006` owns the finite monodromy / deck-character interpretation after the cover exists.

## 4. Branch-killing cover

Let `u` be the local coordinate from `HG-FND-003`, and let `N` be the branch-killing level. The cover is:

```text
u = w^N.
```

The coordinate `w` is the upstairs coordinate. The standard deck generator is:

```text
w -> zeta_N w
```

where:

```text
zeta_N = exp(2 pi i / N).
```

## 5. Singular unit upstairs

For exponent index `a` at level `N`, the upstairs singular unit is represented as:

```text
eta_a(w) = w^a
```

with normalized analytic factor equal to `1` at the puncture.

The normalization condition is:

```text
h(0) = 1
```

for any analytic factor `h` in the more general form `eta_a(w)=w^a h(w)`.

## 6. Transformation law

Under the standard deck generator:

```text
eta_a(zeta_N w) = zeta_N^a eta_a(w).
```

This is the local geometric source of the character value later interpreted by `HG-FND-006`.

## 7. Level matching

The cover level must kill the denominator of the Puiseux exponent.

For the square-root channel:

```text
alpha = 1/2 implies N = 2.
```

For the cubic character channel:

```text
alpha = 1/3 implies N = 3.
```

If a common cover is used, the level must be a common multiple of all active denominators.

## 8. Boundary with HG-FND-005

`HG-FND-004` owns the cover and singular unit as local geometric / analytic objects.

`HG-FND-005` owns any Deligne-unit framing of the same data. No Deligne cohomology class is constructed here.

## 9. Discharge criterion

A downstream claim may cite normalized `HG-FND-004` only when it supplies:

1. the base local coordinate `u`;
2. the chosen puncture;
3. the branch convention;
4. the Puiseux exponent or exponent index;
5. the branch-killing level `N`;
6. the cover equation `u = w^N`;
7. the upstairs singular unit `eta_a`;
8. the normalization condition at the puncture;
9. the deck generator convention;
10. the transformation law under deck action;
11. an explicit boundary excluding Deligne-unit, tame-symbol, regulator, and downstream theorem claims.

## 10. Non-claims

This document does not normalize `HG-FND-005` or `HG-FND-008`.

This document does not construct a Deligne unit, Deligne cup-product, tame symbol, regulator symbol, or `L`-function bridge.

This document does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This document does not authorize downstream repo work.
