# HG-FND-008 — Deligne / Carry Separation

Status: normalized Tier 1.  
Claim level: framework-internal precision result / boundary surface.  
Upstream dependency: `HG-FND-005` as normalized on main at `08b5007161971fe6e15661c6eea852649f7ed052`.  
Upstream dependency: `HG-FND-007` as normalized on main before `HG-FND-008`.  
Operational substrate: `src/heller_godel/phase_characters.py::tame_symbol_standard` and `src/heller_godel/phase_characters.py::carry`.

## Purpose

`HG-FND-008` records the Tier 1 separation surface between the Deligne-side tame-symbol pairing and the `HG-FND-007` integer section-defect carry cocycle.

The purpose is narrow:

```text
Deligne-side tame-symbol evaluation != integer section-defect carry cocycle
```

This is a framework-internal precision result. It does not prove any external major theorem and does not promote downstream mathematical claims.

## Dependencies

`HG-FND-005` supplies the Deligne-unit / tame-symbol side:

```text
[eta_a] in H^1_D(Delta^*, Z(1))
Tame(f, g) = (-1)^(v(f)v(g)) h_f(0)^v(g) / h_g(0)^v(f)
```

`HG-FND-007` supplies the carry side:

```text
carry(a, b, N) = (section(a) + section(b) - section(a + b)) / N
```

`HG-FND-008` owns only the separation/comparison statement between those upstream surfaces.

## Deligne-side pairing

The Deligne-side surface is framed through classes of analytic units on the punctured disk:

```text
[eta_a], [eta_b] in H^1_D(Delta^*, Z(1))
```

Its executable boundary evaluation is the tame-symbol convention declared by `HG-FND-005`:

```text
Tame(f, g) = (-1)^(v(f)v(g)) h_f(0)^v(g) / h_g(0)^v(f)
```

Operationally, this is represented by:

```python
tame_symbol_standard(valuation_f, valuation_g, h_f_0=1, h_g_0=1)
```

## Carry cocycle

The carry side is the integer section defect normalized by `HG-FND-007`.

Its domain is finite-level integer residue data:

```text
(a, b) in Z/N x Z/N
```

Its executable operation is:

```python
carry(a, b, N)
```

Its law is additive cocycle coherence for the extension:

```text
0 -> Z -> Z -> Z/N -> 0
```

## Structural separation

The separation has three parts.

### Domain separation

The Deligne side takes analytic-unit class data on the punctured disk.

The carry side takes integer residues modulo a finite level.

### Codomain separation

The tame-symbol side lands in a multiplicative numeric-complex boundary value under the executable convention.

The carry side lands in integer section-defect values.

### Algebraic-law separation

The tame-symbol side is multiplicative under the declared local-unit convention.

The carry side is an additive 2-cocycle for the finite-level section extension.

These are different mathematical objects even when small integer parameters are used to exercise both functions in CI.

## Operational witness

The primary executable witness is:

```text
tame_symbol_standard(1, 1) = -1.0
carry(1, 1, 3) = 0
```

A second executable witness is:

```text
tame_symbol_standard(1, 3) = -1.0
carry(1, 1, 3) = 0
```

The values are exact under the current `phase_characters.py` implementation.

The superficial reuse of small integers in the calls does not create a structural relation. The arguments belong to distinct typed surfaces: valuations and analytic factors on the tame-symbol side; integer residues and level on the carry side.

## Discharge criterion

A citation to `HG-FND-008` is admissible only when it provides all of the following:

1. upstream `HG-FND-005` for the Deligne/tame-symbol side;
2. upstream `HG-FND-007` for the carry-cocycle side;
3. explicit domain declarations for both sides;
4. explicit codomain declarations for both sides;
5. the tame-symbol convention used by the executable substrate;
6. the operational witness with exact numeric values.

## Non-claims

`HG-FND-008` does not construct a regulator symbol.

`HG-FND-008` does not construct any analytic-number-theory bridge.

`HG-FND-008` does not identify the tame symbol and carry cocycle in a deeper sense.

`HG-FND-008` does not prove any external major theorem.

`HG-FND-008` does not promote `HG-MTH-011`, `HG-MTH-019`, or `HG-MTH-021`.

`HG-FND-008` does not perform downstream repository work.
