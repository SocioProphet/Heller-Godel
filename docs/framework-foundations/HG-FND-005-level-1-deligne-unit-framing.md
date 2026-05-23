# HG-FND-005 — Level-1 Deligne-Unit Framing

Status: normalized Tier 1.  
Claim level: framework-foundational definition / boundary surface.  
Upstream dependency: `HG-FND-004` as normalized on main at `e54b47006a28a5619d4776ae69d964b16e07dfdb`.  
Operational substrate: `src/heller_godel/phase_characters.py::tame_symbol_standard`.

## Purpose

`HG-FND-005` records the level-1 Deligne-unit framing of the singular unit constructed upstairs by `HG-FND-004`.

The purpose is narrow:

```text
singular unit upstairs -> analytic unit on the punctured disk -> level-1 Deligne-unit datum
```

This surface does not construct a Deligne cup-product, regulator symbol, L-function bridge, or carry-cocycle comparison.

## Dependency on HG-FND-004

`HG-FND-004` supplies the branch-killing cover and singular unit upstairs:

```text
u = w^N
eta_a(w) = w^a h(w)
h(0) = 1
```

`HG-FND-005` assumes that cover, puncture, coordinate, level, and normalization convention. It does not reconstruct them.

## The punctured disk

Let:

```text
Delta^* = { 0 < |w| < epsilon }
```

where `w` is the upstairs coordinate from the branch-killing cover.

The puncture is the divisor at `w = 0`.

## Analytic units

Let:

```text
O^*(Delta^*)
```

be the group of analytic units on the punctured disk.

The singular unit from `HG-FND-004` is treated as an analytic unit on the punctured disk:

```text
eta_a in O^*(Delta^*)
```

with local form:

```text
eta_a(w) = w^a h(w)
h(0) = 1
```

## Deligne-unit class

The level-1 Deligne-unit framing is the class:

```text
[eta_a] in H^1_D(Delta^*, Z(1))
```

This class is the Deligne-unit datum attached to the singular unit upstairs.

The normalized claim is only that `eta_a` is framed as a level-1 unit datum. No cup-product or regulator operation is performed here.

## Tame-symbol evaluation at the puncture

The tame-symbol convention used operationally is:

```text
Tame(f, g) = (-1)^(v(f)v(g)) h_f(0)^v(g) / h_g(0)^v(f)
```

for:

```text
f = w^A h_f(w)
g = w^B h_g(w)
h_f(0), h_g(0) != 0
```

For the normalized singular-unit side with default analytic factors equal to `1`, this becomes:

```text
Tame(w^a, w^N) = (-1)^(aN)
```

This recovers the finite character value on the Deligne side under the declared tame-symbol convention.

## Operational substrate

The repository implementation point is:

```python
tame_symbol_standard(valuation_f, valuation_g, h_f_0=1, h_g_0=1)
```

in `src/heller_godel/phase_characters.py`.

This function computes the tame-symbol evaluation. It is not the Deligne cohomology class `[eta_a]` itself.

## Boundary with HG-FND-008

`HG-FND-005` owns the level-1 Deligne-unit framing.

`HG-FND-008` owns the later comparison surface separating:

```text
Deligne cup-product / regulator-symbol data
```

from:

```text
HG-FND-007 integer section-defect carry cocycle
```

`HG-FND-005` does not identify the tame symbol with the carry cocycle and does not construct the cup-product or regulator symbol.

## Discharge criterion

A citation to `HG-FND-005` is admissible only when it supplies all of the following:

1. the upstream `HG-FND-004` cover and singular unit;
2. the punctured disk `Delta^*`;
3. the analytic-unit group `O^*(Delta^*)`;
4. the singular unit `eta_a` as an analytic unit;
5. the Deligne-unit class `[eta_a] in H^1_D(Delta^*, Z(1))`;
6. the tame-symbol evaluation convention and operational substrate;
7. the boundary excluding Deligne cup-product, regulator-symbol construction, carry-cocycle identification, theorem promotion, and downstream repo work.

## Non-claims

`HG-FND-005` does not prove or construct a Deligne cup-product.

`HG-FND-005` does not define a regulator symbol.

`HG-FND-005` does not identify the tame-symbol evaluation with the `HG-FND-007` carry cocycle.

`HG-FND-005` does not normalize `HG-FND-008`.

`HG-FND-005` does not promote `HG-MTH-011`, `HG-MTH-019`, or `HG-MTH-021`.

`HG-FND-005` does not perform downstream repository work.
