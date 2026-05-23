# HG-FND-005 Preflight — Level-1 Deligne-Unit Framing

Issue: #129  
Branch: `work/hg-fnd-005-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new theorem-grade mathematics.

## Purpose

This preflight records the `HG-FND-005` normalization surface before implementation.

`HG-FND-005` frames the singular unit supplied by `HG-FND-004` as a level-1 Deligne-unit datum on the punctured disk. It does not construct a Deligne cup-product, regulator symbol, or comparison with the carry cocycle.

## Finding 1 — Reference inventory

Relevant repository references:

- `docs/framework-core/claim-grammar.md` supplies the citation-grade controls used by `HG-MTH-011`, `HG-MTH-019`, and `HG-MTH-021` references.
- `docs/framework-core/distance-classification.md` lists `HG-FND-005` as a candidate Tier 1 surface after `HG-FND-004`.
- `docs/framework-foundations/HG-FND-004-branch-killing-cover-singular-unit.md` supplies the constructed cover and singular unit upstairs.
- Paper I Section 4 is the expected active-core source for the level-1 Deligne-unit framing.
- `src/heller_godel/phase_characters.py` already exposes `tame_symbol_standard`, which is the executable substrate for the tame-symbol evaluation used by this surface.

## Finding 2 — Interface with HG-FND-004

`HG-FND-004` supplies the singular unit upstairs as a local analytic object:

```text
eta_a(w) = w^a h(w)
h(0) = 1
```

`HG-FND-005` owns the promotion of this unit to an element of the analytic-unit group on the punctured disk, and records its level-1 Deligne-unit class.

In notation:

```text
eta_a in O^*(Delta^*)
[eta_a] in H^1_D(Delta^*, Z(1))
```

where `Delta^*` is the punctured disk.

## Finding 3 — Active mathematical core

The active core to normalize is:

```text
O^*(Delta^*) = analytic units on the punctured disk
eta_a in O^*(Delta^*)
[eta_a] in H^1_D(Delta^*, Z(1))
```

The class `[eta_a]` is the Deligne-unit datum.

The tame-symbol evaluation at the puncture records the boundary value:

```text
Tame(eta_a, w^N) = (-1)^(aN)
```

with the current executable convention implemented by `tame_symbol_standard`.

This recovers the finite character value on the Deligne side, while remaining distinct from the integer carry cocycle normalized by `HG-FND-007`.

## Finding 4 — phase_characters.py coverage

`phase_characters.py` already supplies:

```text
tame_symbol_standard(valuation_f, valuation_g, h_f_0=1, h_g_0=1)
```

The helper computes the tame-symbol evaluation under the local convention:

```text
(-1)^(v(f)v(g)) h_f(0)^v(g) / h_g(0)^v(f)
```

It is operational substrate for the evaluation. It is not itself the Deligne-unit class `[eta_a]`.

## Finding 5 — Boundary with HG-FND-008

`HG-FND-005` owns the Deligne-unit framing.

`HG-FND-008` owns the later separation between Deligne cup-product / regulator-symbol constructions and the carry cocycle from `HG-FND-007`.

`HG-FND-005` does not perform that comparison and does not normalize `HG-FND-008`.

## Finding 6 — Anti-seed requirement

Required anti-seed:

```text
A-HG-FND-011 — Treating tame-symbol evaluation as proof that the Deligne-unit class equals the carry cocycle.
```

Correct boundary:

```text
The tame symbol is an evaluation of a level-1 Deligne-unit datum. The carry cocycle is an integer section defect. They are not identified without a separate normalized comparison surface.
```

A second guarded failure mode is treating `[eta_a]` as proof-grade without declaring the cover, puncture, and normalization condition supplied by `HG-FND-004`.

## Finding 7 — Proposed discharge criterion

A normalized `HG-FND-005` citation must supply:

1. the upstream `HG-FND-004` cover and singular unit;
2. the punctured disk `Delta^*`;
3. the analytic-unit group `O^*(Delta^*)`;
4. the singular unit `eta_a` as an analytic unit;
5. the Deligne-unit class `[eta_a]` in `H^1_D(Delta^*, Z(1))`;
6. the tame-symbol evaluation convention and operational substrate;
7. an explicit boundary excluding Deligne cup-product, regulator-symbol, carry-cocycle identification, theorem promotion, and downstream repo work.

## Non-actions

This preflight does not normalize `HG-FND-005`.

This preflight does not construct a Deligne cup-product, regulator symbol, or L-function bridge.

This preflight does not normalize `HG-FND-008`.

This preflight does not promote `HG-MTH-011`, `HG-MTH-019`, or `HG-MTH-021`.

This preflight does not authorize downstream repo work.
