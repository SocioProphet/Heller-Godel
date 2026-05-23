# HG-FND-006 — Finite Monodromy / Deck-Character Interpretation

Identifier: `HG-FND-006`  
Layer: framework-foundational / Tier 1.  
Status: normalized finite-monodromy / deck-character foundation.  
Owner: `SocioProphet/Heller-Godel`.  
Claim level: framework-foundational deck-character realization; not carry-cocycle or Deligne promotion.

## 1. Purpose and Tier 1 declaration

`HG-FND-006` normalizes the finite monodromy / deck-character interpretation surface.

It explains how an already declared finite character is realized as a multiplicative deck action on a branch-killing cover. It does not define the character vocabulary and it does not define the lifted carry cocycle.

## 2. Dependencies

Normalized dependencies:

- `HG-FND-003` at merge SHA `20499fcaa535e5dd4701aaf42fa582173c3ba746`, source `docs/framework-foundations/HG-FND-003-puiseux-singular-datum.md`.
- `HG-VOC-006` at merge SHA `86b4327b831c79b9ea58c2d56291dffeba0db50f`, source `docs/framework-vocabulary/HG-VOC-006-character-data-finite-phase-reductions.md`.

`HG-FND-003` supplies the local Puiseux datum and local coordinate. `HG-VOC-006` supplies the character vocabulary, root-of-unity notation, generator convention, and finite phase alignment.

## 3. Branch-killing cover construction

Let `u` be a chosen local coordinate and let `N` be the branch-killing level. The branch-killing cover is:

```text
u = w^N.
```

Equivalently, `w` is an `N`th-root coordinate above the punctured local coordinate.

## 4. Deck transformation

Let:

```text
zeta_N = exp(2 pi i / N).
```

The standard deck generator acts by:

```text
w -> zeta_N w.
```

This is a deck action on the branch-killing cover. It is multiplicative in the root coordinate.

## 5. Section carrying exponent data

Let a section carry exponent index `A` at level `N`. Under the deck generator, the section transforms by:

```text
s_A(w) -> zeta_N^A s_A(w).
```

Thus the associated multiplicative character is:

```text
chi_A(gamma)=zeta_N^A.
```

This is the deck-character realization licensed by `HG-FND-006`.

## 6. Product formula on a common cover

For synchronized data `(A,N)` and `(B,N)` on a common branch-killing cover, the product character is:

```text
chi_A chi_B = chi_{A+B mod N}.
```

Equivalently:

```text
zeta_N^A zeta_N^B = zeta_N^{A+B mod N}.
```

This is multiplicativity in `mu_N`. It does not state anything about section-defect carry.

## 7. Boundary with HG-FND-007

`HG-FND-006` owns multiplicative deck-character realization.

`HG-FND-007` owns the additive carry created by choosing integer representatives for finite phase indices.

The hard boundary is:

```text
multiplicativity in mu_N != carry triviality for integer lifts.
```

For example, `zeta_2^1 zeta_2^1 = zeta_2^0` is a trivial product in `mu_2`, while the integer lift may still carry because `1+1 = 0 mod 2` with carry `1`.

## 8. Discharge criterion

A downstream claim may cite normalized `HG-FND-006` only when it supplies:

1. normalized local datum from `HG-FND-003` if a branch point is involved;
2. normalized character vocabulary from `HG-VOC-006`;
3. the branch-killing level `N`;
4. the cover equation `u=w^N` or equivalent local cover;
5. the deck generator convention;
6. the phase index `A` and character value `zeta_N^A`;
7. the product law, if multiplicativity is cited;
8. explicit statement that multiplicativity does not trivialize the `HG-FND-007` carry.

## 9. Non-claims

This document does not normalize `HG-FND-007`.

This document does not define or trivialize the section-defect carry cocycle.

This document does not supply `zeta_3` carry, `U(2)`, Deligne-unit, tame-symbol, or regulator-symbol content.

This document does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This document does not authorize downstream repo work.
