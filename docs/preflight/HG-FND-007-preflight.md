# HG-FND-007 Preflight — Lifted Phase Index and Section-Defect Carry Cocycle

Issue: #117  
Branch: `work/hg-fnd-007-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new mathematics.

## Purpose

This preflight records the `HG-FND-007` normalization surface before implementation.

`HG-FND-007` is the lifted phase index and section-defect carry-cocycle surface. It begins after `HG-FND-006` supplies multiplicative deck-character realization and then studies the additive carry induced by choosing integer section representatives.

## Finding 1 — Interface with HG-FND-006

`HG-FND-006` gives the multiplicative character or deck-action realization.

`HG-FND-007` owns the additive section-defect carry:

```text
carry(a,b;N) = (s(a)+s(b)-s(a+b))/N
```

where `s` is the chosen section into integer representatives.

Thus `HG-FND-007` does not redefine the character. It records the obstruction produced by lifting finite indices to integer representatives.

## Finding 2 — Active core

The carry is a `Z`-valued 2-cocycle for the finite-index section.

It is not a Deligne class.

It is not the tame symbol.

The cocycle identity is:

```text
carry(a,b;N) + carry(a+b,c;N)
= carry(b,c;N) + carry(a,b+c;N).
```

Existing CI already checks the cocycle identity over finite ranges and checks separation from the tame symbol through the executable phase-character module.

## Finding 3 — phase_characters.py executable coverage

The executable substrate already contains:

```text
carry
carry_table
carry_cocycle_identity_holds
tame_symbol_standard
```

Existing tests already verify:

- small carry tables;
- cocycle identity over finite ranges;
- witness separation between carry and tame symbol;
- tame-symbol dependence on analytic factors rather than residues alone.

This gives `HG-FND-007` a stronger executable basis than earlier purely documentary surfaces.

## Finding 4 — Anti-seed requirement

`A-HG-FND-004` already guards the broad error of confusing carry cocycle with Deligne cup-product or regulator-symbol data.

A future `HG-FND-007` normalization PR needs a narrower entry specific to the lifted phase-index surface.

Minimum failure mode:

```text
A downstream artifact identifies the section-defect carry cocycle with a Deligne cup-product, tame symbol, or regulator residue without a separate normalized comparison surface.
```

Correct boundary:

```text
`HG-FND-007` owns the integer-section carry cocycle. Deligne cup-product, tame symbol, and regulator-symbol comparisons require separate typed surfaces.
```

## Finding 5 — Proposed implementation file plan

Future normalization PR, not this preflight:

```text
docs/framework-foundations/HG-FND-007-lifted-phase-index-carry-cocycle.md
tests/test_hg_fnd_007_lifted_phase_index_carry_cocycle.py
```

Expected registry update:

```text
Move HG-FND-007 from candidate inventory to normalized Tier 1 only after the carry-cocycle surface is defined and guarded.
```

## Non-actions

This preflight does not normalize `HG-FND-007`.

This preflight does not normalize or promote `HG-FND-006`.

This preflight does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This preflight does not add Deligne-unit, tame-symbol, regulator-symbol, or downstream repo content.

This preflight does not authorize downstream repo work.
