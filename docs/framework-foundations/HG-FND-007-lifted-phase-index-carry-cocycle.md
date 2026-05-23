# HG-FND-007 — Lifted Phase Index and Section-Defect Carry Cocycle

Identifier: `HG-FND-007`  
Layer: framework-foundational / Tier 1.  
Status: normalized lifted phase-index / carry-cocycle foundation.  
Owner: `SocioProphet/Heller-Godel`.  
Claim level: framework-foundational carry-cocycle surface; not Deligne, tame-symbol, or regulator promotion.

## 1. Purpose and Tier 1 declaration

`HG-FND-007` normalizes the lifted phase-index and section-defect carry-cocycle surface.

It begins after `HG-FND-006` supplies multiplicative deck-character realization and records the additive defect created by choosing integer representatives for finite phase indices.

## 2. Dependency on HG-FND-006

Normalized dependency:

- `HG-FND-006`, source `docs/framework-foundations/HG-FND-006-finite-monodromy-deck-character.md`.

`HG-FND-006` supplies the multiplicative character law in the finite root-of-unity group. `HG-FND-007` supplies the integer-lift carry created by a section choice.

## 3. Section map

For a finite level `N`, let:

```text
s: Z/NZ -> {0, ..., N-1}
```

be the canonical integer representative section.

## 4. Carry definition

The section-defect carry is:

```text
carry(a,b;N) = (s(a)+s(b)-s(a+b))/N.
```

It records the integer overflow required to reconcile integer addition with finite residue addition.

## 5. Cocycle identity

The carry satisfies the 2-cocycle identity:

```text
carry(a,b;N) + carry(a+b,c;N)
= carry(b,c;N) + carry(a,b+c;N).
```

This identity is verified by CI through `carry_cocycle_identity_holds` in `src/heller_godel/phase_characters.py`.

## 6. Separation from Deligne cup-product and tame symbol

The carry is an integer-valued section defect.

It is not a Deligne cup-product.

It is not a tame symbol.

It is not a regulator residue.

The inputs are different: the carry depends on finite residue representatives and integer-section choice, while tame-symbol and regulator-symbol objects require analytic or cohomological input not supplied by this surface.

## 7. Operational substrate

`src/heller_godel/phase_characters.py` supplies executable substrate for this surface:

```text
carry
carry_table
carry_cocycle_identity_holds
tame_symbol_standard
```

The first three implement and verify the carry surface. `tame_symbol_standard` is used as a separation witness, not as an identity target.

## 8. Discharge criterion

A downstream claim may cite normalized `HG-FND-007` only when it supplies:

1. a finite level `N`;
2. finite residues or indices being lifted;
3. the section map or representative convention;
4. the carry formula;
5. the cocycle identity if associativity/2-cocycle behavior is cited;
6. explicit separation from Deligne cup-product, tame symbol, and regulator residue;
7. no claim that multiplicative deck-character triviality implies carry triviality;
8. no downstream theorem promotion unless separately normalized.

## 9. Non-claims

This document does not normalize `HG-FND-004` or `HG-FND-005`.

This document does not supply a Deligne unit, Deligne cup-product, tame-symbol identification, regulator residue, or `L`-function bridge.

This document does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This document does not authorize downstream repo work.
