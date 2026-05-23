# HG-FND-004 Preflight — Branch-Killing Cover and Singular Unit Upstairs

Issue: #125  
Branch: `work/hg-fnd-004-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new theorem-grade mathematics.

## Purpose

This preflight records the `HG-FND-004` normalization surface before implementation.

`HG-FND-004` is the branch-killing cyclic cover and singular-unit-upstairs surface. It sits between the local Puiseux datum normalized by `HG-FND-003` and the deck-character action normalized by `HG-FND-006`.

## Finding 1 — Reference inventory

Reference surfaces already in the repository:

- `docs/framework-core/claim-grammar.md` supplies citation-grade discipline.
- `docs/framework-core/distance-classification.md` currently lists `HG-FND-004` as a candidate Tier 1 surface outside the exhausted issue #97 queue.
- `docs/framework-foundations/HG-FND-003-puiseux-singular-datum.md` supplies the local coordinate, puncture, branch convention, and Puiseux exponent data.
- `docs/framework-foundations/HG-FND-006-finite-monodromy-deck-character.md` cites the cover equation as an already available cover but does not construct the cover or the upstairs singular unit.
- Paper I Section 3 is the expected source locus for the branch-killing cover, upstairs unit, deck action, and normalization condition.

## Finding 2 — Interface with HG-FND-003

`HG-FND-003` supplies the base local datum:

```text
local coordinate u
puncture and branch convention
Puiseux exponent alpha = a/N
```

`HG-FND-004` owns the constructed object:

```text
u = w^N
```

and the singular unit upstairs.

Thus `HG-FND-004` cannot be cited without declaring the base Puiseux datum, the level `N`, and the branch convention inherited from `HG-FND-003`.

## Finding 3 — Interface with HG-FND-006

`HG-FND-006` uses the branch-killing cover to state the deck-character action.

`HG-FND-006` does not construct the cover, does not define the upstairs singular unit, and does not own the normalization condition at the puncture.

`HG-FND-004` owns those objects.

## Finding 4 — Active mathematical core

The active core to normalize is:

```text
cover equation: u = w^N
singular unit upstairs: eta(w)
normalization condition: eta(0) = 1
standard deck generator: w -> zeta_N w
transformation law: eta(zeta_N w) = zeta_N^a eta(w)
```

The exponent index `a` is inherited from the local Puiseux exponent `alpha = a/N` after choosing the branch-killing level.

## Finding 5 — Anti-seed requirement

A required anti-seed is:

```text
A-HG-FND-010 — Treating the branch-killing cover as constructed without declaring the Puiseux datum, level, and branch convention from HG-FND-003.
```

The failure mode is a downstream artifact citing the cover or upstairs unit as if it exists canonically without choosing the local datum, level, and branch convention.

## Finding 6 — Proposed discharge criterion

A normalized `HG-FND-004` citation must supply:

1. the base local coordinate `u`;
2. the chosen puncture and branch convention;
3. the Puiseux exponent or finite index data inherited from `HG-FND-003`;
4. the branch-killing level `N`;
5. the cover equation `u = w^N`;
6. the upstairs singular unit;
7. the normalization condition at the puncture;
8. the deck transformation convention;
9. the transformation law for the upstairs unit;
10. the explicit boundary excluding Deligne-unit and regulator content.

## Finding 7 — Boundary with HG-FND-005

`HG-FND-004` owns the branch-killing cover and singular unit as geometric/local analytic objects.

`HG-FND-005` owns the later Deligne-unit framing of the same data in `H^1_D` or any equivalent Deligne-cohomology comparison surface.

No Deligne-unit, regulator, or tame-symbol content is authorized by this preflight.

## Non-actions

This preflight does not normalize `HG-FND-004`.

This preflight does not normalize `HG-FND-005` or `HG-FND-008`.

This preflight does not add Deligne-unit, regulator-symbol, tame-symbol, or downstream repo content.

This preflight does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.
