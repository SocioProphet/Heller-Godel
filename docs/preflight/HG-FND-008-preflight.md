# HG-FND-008 Preflight — Deligne / Carry Separation

Issue: #132  
Branch: `work/hg-fnd-008-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new theorem-grade mathematics.

## Purpose

This preflight records the normalization surface for `HG-FND-008`.

`HG-FND-008` owns the framework-internal separation statement between the Deligne-side tame-symbol pairing and the `HG-FND-007` integer section-defect carry cocycle. It does not own either upstream object.

## Finding 1 — Reference inventory

Relevant repository references:

- `A-HG-FND-004` is the broad active guard against conflating framework notation with proved theorem-grade content.
- `A-HG-FND-009` is the narrower `HG-FND-007` guard against treating the carry cocycle as a regulator or tame-symbol construction.
- `docs/framework-core/claim-grammar.md` records non-claim discipline relevant to `HG-MTH-011`, `HG-MTH-019`, and `HG-MTH-021` references.
- `docs/framework-foundations/HG-FND-005-level-1-deligne-unit-framing.md` declares the Deligne-unit / tame-symbol side and explicitly leaves the comparison to `HG-FND-008`.
- `docs/framework-foundations/HG-FND-007-lifted-phase-index-carry-cocycle.md` declares the integer section-defect carry side and explicitly excludes regulator/tame-symbol identification.
- `src/heller_godel/phase_characters.py` exposes both `tame_symbol_standard` and `carry`, the two operational witnesses used by this surface.

## Finding 2 — What FND-008 owns

`HG-FND-008` owns the structural separation statement between:

1. the Deligne-side pairing computed by tame-symbol evaluation under the `HG-FND-005` convention; and
2. the `HG-FND-007` integer section-defect carry cocycle.

It owns the comparison boundary only. It does not construct the Deligne-unit class, the pairing object, or the carry cocycle.

## Finding 3 — Structural separation

The two sides have different domains:

```text
Deligne side: classes of analytic units on the punctured disk
Carry side: integer residues modulo a finite level
```

The two sides have different codomains:

```text
Deligne/tame-symbol side: multiplicative complex-valued boundary evaluation
Carry side: integer-valued section defect
```

The two sides have different algebraic laws:

```text
Deligne/tame-symbol side: bilinear pairing of cohomology-class data, evaluated multiplicatively
Carry side: additive 2-cocycle for the extension 0 -> Z -> Z -> Z/N -> 0
```

## Finding 4 — Operational separation witness

The executable substrate gives the clean witness:

```text
tame_symbol_standard(1, 1) = -1.0
carry(1, 1, 3) = 0
```

The same integer-looking inputs are being sent to two different functions with different meanings, domains, codomains, and laws.

A second witness is:

```text
tame_symbol_standard(1, 3) = -1.0
carry(1, 1, 3) = 0
```

The tame-symbol value is multiplicative and numeric-complex/float-valued under the executable convention; the carry value is integer-valued.

## Finding 5 — Anti-seed status

Existing guards:

- `A-HG-FND-004` guards the broad failure mode.
- `A-HG-FND-009` guards the `HG-FND-007`-specific failure mode.
- `A-HG-FND-011` guards the `HG-FND-005` failure mode that treats tame-symbol evaluation as carry-cocycle identification.

Required closing entry:

```text
A-HG-FND-012 — Treating the operational separation witness as a structural proof without declaring the domain, codomain, and algebraic-law distinction.
```

Correct boundary:

```text
The operational witness demonstrates non-equality in concrete test cases. The structural separation requires the domain/codomain/algebraic-law argument normalized by HG-FND-008.
```

## Finding 6 — Proposed discharge criterion

A normalized `HG-FND-008` citation must provide:

1. upstream `HG-FND-005` for the Deligne/tame-symbol side;
2. upstream `HG-FND-007` for the carry-cocycle side;
3. explicit domain declarations for both sides;
4. explicit codomain declarations for both sides;
5. the tame-symbol convention used by the executable substrate;
6. the operational witness with exact numeric values.

## Non-actions

This preflight does not normalize `HG-FND-008`.

This preflight does not construct regulator machinery or analytic-number-theory bridges.

This preflight does not promote `HG-MTH-011`, `HG-MTH-019`, or `HG-MTH-021`.

This preflight does not make any major-theorem claim.

This preflight does not perform downstream repo work.
