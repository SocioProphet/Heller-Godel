# HG-FND-006 Preflight — Finite Monodromy / Deck-Character Interpretation

Issue: #116  
Branch: `work/hg-fnd-006-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new mathematics.

## Purpose

This preflight records the `HG-FND-006` normalization surface before implementation.

`HG-FND-006` is the finite monodromy / deck-character interpretation surface. It begins after character vocabulary has been supplied by `HG-VOC-006` and asks how the declared character is realized as a deck transformation on a branch-killing cover.

## Finding 1 — Interface with HG-VOC-006

`HG-VOC-006` supplies:

```text
character vocabulary;
roots-of-unity notation;
finite phase-reduction convention;
generator convention;
comparison between manuscript phase value and global source.
```

`HG-FND-006` owns:

```text
realization of the character as a deck transformation;
branch-killing cover action;
multiplicative character interpretation on the cover.
```

Thus `HG-FND-006` does not redefine `chi_p`; it interprets an already declared character as deck-action data.

## Finding 2 — Active core in Paper I section 3

The active core is the branch-killing cover pattern:

```text
w^N = local coordinate.
```

A deck transformation acts on the branch parameter by:

```text
w -> zeta_N w.
```

A local branch or section carrying exponent/index data transforms by multiplication through the declared character value. This is the multiplicative deck-character realization surface.

For the P3.c pathway, `HG-VOC-006` supplies the `mu_3` vocabulary and generator convention; `HG-FND-006` is expected to own the deck-action realization after the branch-killing cover has been chosen.

## Finding 3 — Boundary with HG-FND-007

`HG-FND-006` owns multiplicative character realization.

`HG-FND-007` owns the section-defect carry that appears after choosing integer representatives for finite phase indices.

The distinction is structural:

```text
multiplicative deck character != additive lift carry
```

A multiplicative character may be well-defined while the chosen integer section still has a nontrivial carry under addition.

## Finding 4 — Anti-seed requirement

A future `HG-FND-006` normalization PR needs an anti-seed against treating multiplicativity as carry triviality.

Minimum failure mode:

```text
A downstream artifact treats a multiplicative deck-character law as proof that the lifted phase-index carry cocycle is trivial.
```

Correct boundary:

```text
`HG-FND-006` may prove or define multiplicative deck-character realization. `HG-FND-007` separately owns the lifted section-defect carry cocycle.
```

## Finding 5 — Proposed implementation file plan

Future normalization PR, not this preflight:

```text
docs/framework-foundations/HG-FND-006-finite-monodromy-deck-character.md
tests/test_hg_fnd_006_finite_monodromy_deck_character.py
```

Expected registry update:

```text
Move HG-FND-006 from candidate inventory to normalized Tier 1 only after its deck-character realization surface is defined and guarded.
```

## Non-actions

This preflight does not normalize `HG-FND-006`.

This preflight does not normalize or promote `HG-FND-007`.

This preflight does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This preflight does not add carry-cocycle, section-defect, Deligne, tame-symbol, or regulator-symbol content.

This preflight does not authorize downstream repo work.
