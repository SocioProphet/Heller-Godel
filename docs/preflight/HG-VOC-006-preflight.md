# HG-VOC-006 Preflight — Character Data and Finite Phase Reductions

Issue: #112  
Branch: `work/hg-voc-006-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new mathematics.

## Purpose

This preflight records the current `HG-VOC-006` normalization surface before any implementation PR is opened.

`HG-VOC-006` is the character-data / finite-phase-reduction vocabulary surface. It is adjacent to normalized `HG-FND-003`, but not contained by it. `HG-FND-003` owns local Puiseux datum at a chosen puncture. `HG-VOC-006` owns the global character source-identification vocabulary and finite phase-reduction vocabulary needed to interpret `chi_p` claims.

## Finding 1 — Reference inventory

| Location | Reference type | Count |
| --- | --- | ---: |
| `docs/framework-core/distance-classification.md` | Registry row with candidate status | 1 |
| `docs/framework-core/claim-grammar.md` | References in `HG-MTH-017`, `HG-MTH-018`, `HG-MTH-019`, `HG-MTH-021`, and deferred queue | active |
| `docs/framework-core/anti-seed-framework.md` | `A-HG-FND-007` boundary against treating local square-root behavior as character-source data | active |
| `docs/gate-minimality/p3c-puiseux-singularity-chi3-p3-scope.md` | P3.c scope definition for Puiseux singularity and `chi_3` at `p=3` | active |
| `docs/gate-minimality/p3c-puiseux-singularity-character-p3-closure.md` | Active source-identification core | live |
| `src/heller_godel/phase_characters.py` | Executable finite-character substrate | active |
| `tests/test_phase_characters.py` | Existing executable coverage | active |

## Finding 2 — Interface with HG-FND-003

The normalized boundary is now explicit.

`HG-FND-003` owns:

```text
chosen puncture;
local coordinate;
principal branch convention;
Puiseux expansion;
local mu_2-type sign-change behavior.
```

`HG-VOC-006` begins at:

```text
global character source-identification;
finite phase-reduction vocabulary;
chi_p notation and roots-of-unity vocabulary;
comparison between manuscript phase convention and global source convention.
```

Therefore `HG-VOC-006` must not re-own the P3.c local Puiseux expansion. It may cite normalized `HG-FND-003` as local input, then record why the local square-root channel is not the source of `chi_3 in mu_3`.

## Finding 3 — Active mathematical core

The active P3.c closure identifies the global character source for the cubic cover:

```text
x y^3 - y + 1 = 0.
```

Equivalently, with reciprocal variable `z=1/y`:

```text
z^3 - z^2 + x = 0.
```

The closure records:

```text
Galois group: S_3
cyclic sheet-rotation subgroup: A_3 ~= Z/3
positive generator: tau=(123)
chi_3(tau)=omega
omega=exp(2 pi i / 3)
```

The manuscript phase-map convention is:

```text
k_p(beta)=floor(p beta) mod p
chi_p^(rho,beta)(T)=exp(2 pi i k_p(beta)/p).
```

For:

```text
p=3, beta=1/2
```

this gives:

```text
k_3(1/2)=floor(3/2) mod 3 = 1
chi_3=exp(2 pi i / 3)=omega.
```

Thus `HG-VOC-006` must own the vocabulary alignment between the manuscript phase-map value and the global `A_3` sheet-rotation source. The local square-root Puiseux channel remains `HG-FND-003` input and is not the source of the `mu_3` character.

## Finding 4 — phase_characters.py coverage

`src/heller_godel/phase_characters.py` already supplies the executable finite-character substrate expected by `HG-VOC-006` normalization.

Operational surfaces to cite:

```text
normalize_exponent
phase_index
p_primary_projection
prime_reduction
```

Existing tests in `tests/test_phase_characters.py` already exercise the denominator-level finite-character interface. The normalization document should declare these functions as operational substrate, not as the global Galois source of `chi_3`.

The future test guard should verify the manuscript phase-map formula for:

```text
p=3, beta=1/2, k_3=1, chi_3=omega.
```

It should also verify the cubic discriminant identity:

```text
Delta(x y^3 - y + 1)=x(4-27x).
```

## Finding 5 — Boundary with HG-FND-006 and HG-FND-007

`HG-VOC-006` does not own downstream monodromy / deck-character interpretation or lifted carry-cocycle material.

Excluded from `HG-VOC-006` normalization:

- finite monodromy / deck-character interpretation as a foundational surface;
- lifted phase index;
- section-defect carry cocycle;
- `zeta_3` carry defect;
- `U(2)` correspondence;
- Deligne-unit or regulator-symbol refinements.

Those remain downstream candidate surfaces, especially `HG-FND-006` and `HG-FND-007`.

## Finding 6 — Anti-seed requirement

A VOC-specific anti-seed is needed for the positive content.

Minimum failure mode:

```text
A downstream artifact treats chi_3 as proof-grade character identification without declaring the global Galois source, cyclic sheet-rotation subgroup, generator convention, and comparison with the manuscript phase-map value.
```

The existing `A-HG-FND-007` already guards the negative boundary: local square-root behavior at the chosen puncture is not character-source data. `HG-VOC-006` normalization should preserve that boundary and add the positive character-identification anti-seed.

This preflight records the requirement only. It does not register a new anti-seed.

## Finding 7 — Proposed discharge criterion

A downstream claim may cite normalized `HG-VOC-006` only when it supplies:

1. normalized local input from `HG-FND-003`, if a local Puiseux singularity is involved;
2. the global algebraic cover or finite phase object being interpreted;
3. the character group or subgroup, such as `A_3 ~= Z/3`;
4. generator convention, such as `tau=(123)`;
5. character value, such as `chi_3(tau)=omega`;
6. manuscript phase-map value, such as `k_3(1/2)=1`, if manuscript alignment is claimed;
7. explicit statement that local square-root sign-change behavior is not the `mu_3` character source;
8. no carry-cocycle, `zeta_3`, `U(2)`, or downstream monodromy / deck-character interpretation unless a later normalized surface supplies it.

## Proposed implementation file plan

Future normalization PR, not this preflight:

```text
docs/framework-vocabulary/HG-VOC-006-character-data-finite-phase-reductions.md
tests/test_hg_voc_006_character_data_finite_phase_reductions.py
```

Expected registry update in the future normalization PR:

```text
Move HG-VOC-006 from candidate inventory to normalized Tier 2 or explicitly promoted vocabulary status in docs/framework-core/distance-classification.md.
```

Expected anti-seed update in the future normalization PR:

```text
Register a VOC-specific anti-seed against proof-grade chi_3 claims without global Galois source declaration.
```

## Non-actions

This preflight does not normalize `HG-VOC-006`.

This preflight does not register new anti-seeds.

This preflight does not add tests.

This preflight does not normalize or promote `HG-FND-006` or `HG-FND-007`.

This preflight does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This preflight does not add carry-cocycle, `zeta_3`, `U(2)`, Deligne-unit, or regulator-symbol content.

This preflight does not start P1 path-beta uniqueness or P2 candidate-list exhaustion.

This preflight does not authorize `A_n` extension.

This preflight does not authorize Heller-Einstein, Heller-Dirac, `yang-mills`, `np-program`, BSD, Heller-Winters, or `ns-program` work.

## Stop rule

After this preflight PR is opened and validated, halt.

Implementation of `HG-VOC-006` normalization requires separate authorization.
