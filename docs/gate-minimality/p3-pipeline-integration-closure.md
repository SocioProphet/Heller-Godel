# HG-MTH-021 — P3 Pipeline Integration Closure Assembly

Identifier: `HG-MTH-021`  
Status: closure assembly for P3, scoped by `HG-MTH-012`.  
Owner: `SocioProphet/Heller-Godel`.  
Track: A2 gate-minimality, `HG-MTH-011`, proof-character pipeline at `p=3`.  
Claim level: method-grade modulo six candidate Tier-1 surfaces.

## 1. Statement of P3 closure

P3 — Pipeline Integration is closed by this assembly.

The P3 obligation scoped at `HG-MTH-012` required attachment of the A2 minimality candidate-theorem `HG-MTH-011` to the `chi_p` / `zeta_p` / proof-character pipeline at `p=3`, specifically by demonstrating that the `U(2)=S(U(2) x U(1))` minimal admissible subgroup corresponds to an identifiable object in the `chi_3` phase reduction or `zeta_3` carry defect under composition.

This document introduces no new mathematics. It assembles the four sub-obligation closures already merged:

1. P3.a (`HG-MTH-014`, PR #82): restricted proof grammar at `p=3`, including type expression `C` with `sigma_C` statistic and ternary constructor structure.
2. P3.b (`HG-MTH-016`, PR #86): canonical statistic and generating function at `p=3`, including the ternary/Fuss-Catalan generating-function closure and coefficient identity.
3. P3.c (`HG-MTH-018`, PR #90): Puiseux singularity and `chi_3` at `p=3`, including `rho_3=4/27`, `alpha_3=1/2`, and `chi_3=omega` from the cubic Galois / sheet-rotation source.
4. P3.d (`HG-MTH-020`, PR #94): `zeta_3` carry cocycle and `U(2)` correspondence, including scalar-valued carry cocycle, group-valued lift `Z_3=omega I_3`, and U(1)-complement character `kappa`.

By this assembly, P3 is closed at method-grade modulo the six candidate Tier-1 surfaces recorded in Section 3.

## 2. Sub-obligation citation table

| Sub-obligation | Closure identifier | Closure PR | Merge SHA | Modulo dependency |
| --- | --- | --- | --- | --- |
| P3.a — restricted proof grammar at `p=3` | `HG-MTH-014` | PR #82 | `96f2a9015fb6bc3b62744409660e4855ed9c4014` | `HG-FND-001` |
| P3.b — canonical statistic and generating function at `p=3` | `HG-MTH-016` | PR #86 | `bc54fbeb5d74bdbedcc8c3d7aee85130a2ca63ac` | `HG-FND-002` |
| P3.c — Puiseux singularity and `chi_3` at `p=3` | `HG-MTH-018` | PR #90 | `75bc41930a4f9bd6736d4d54b8dcdf2605c520db` | `HG-FND-003`, `HG-VOC-006` |
| P3.d — `zeta_3` carry defect and `U(2)` correspondence at `p=3` | `HG-MTH-020` | PR #94 | `389e473daa29ffb4c730d9c928eee7d533f22939` | `HG-FND-006`, `HG-FND-007` |

## 3. Cumulative grade chain

| Modulo dependency | Source sub-obligation | Tier-1 surface status |
| --- | --- | --- |
| `HG-FND-001` | P3.a (`HG-MTH-014`) | candidate; registry normalization pending |
| `HG-FND-002` | P3.b (`HG-MTH-016`) | candidate; registry normalization pending |
| `HG-FND-003` | P3.c (`HG-MTH-018`) | candidate; registry normalization pending |
| `HG-VOC-006` | P3.c (`HG-MTH-018`) | candidate; registry normalization pending |
| `HG-FND-006` | P3.d (`HG-MTH-020`) | candidate; registry normalization pending |
| `HG-FND-007` | P3.d (`HG-MTH-020`) | candidate; registry normalization pending |

The cumulative grade chain is therefore:

```text
HG-MTH-011
  lifted by P3 closure HG-MTH-021
  modulo HG-FND-001, HG-FND-002, HG-FND-003,
         HG-VOC-006, HG-FND-006, HG-FND-007.
```

## 4. HG-MTH-011 grade lift

By the cumulative-modulo grade chain, `HG-MTH-011` lifts from:

```text
method-grade as candidate theorem
```

to:

```text
method-grade modulo six candidate Tier-1 surfaces
```

by P3 closure in this PR.

The six candidate surfaces are:

```text
HG-FND-001
HG-FND-002
HG-FND-003
HG-VOC-006
HG-FND-006
HG-FND-007
```

Each of these surfaces remains candidate-grade until independently normalized or otherwise discharged by an authorized route. Full theorem-grade promotion requires the relevant surfaces to be normalized or replaced by a dedicated promotion proof.

The path-beta framework itself remains method-grade. The independent P1 and P2 obligations from `HG-MTH-011` Section 6 remain available as alternative or complementary promotion paths.

## 5. HG-MTH-011 source-document update

This PR updates `docs/gate-minimality/a2-minimality-candidate-theorem.md` to reflect the P3 lift.

The historical grade is retained:

```text
A2 minimality candidate-theorem — method-grade as candidate theorem — HG-MTH-011 initial state
```

A new row records the post-P3 lift:

```text
A2 minimality candidate-theorem after P3 closure — method-grade modulo six candidate Tier-1 surfaces — HG-MTH-021
```

This is a grade lift, not theorem-grade promotion.

## 6. Path to theorem-grade promotion

The three promotion obligations from `HG-MTH-011` Section 6 have the following post-P3 status:

1. P1 — Path-beta uniqueness / characterization: independent obligation, unchanged.
2. P2 — Candidate-list exhaustion: independent obligation, unchanged.
3. P3 — Pipeline integration: closed by this PR; `HG-MTH-011` grade lift performed.

P3 closure alone does not promote `HG-MTH-011` to theorem-grade. It lifts `HG-MTH-011` from method-grade as candidate theorem to method-grade modulo six candidate Tier-1 surfaces.

Theorem-grade promotion requires further normalization of the six Tier-1 surfaces, or a separate authorized promotion route through P1, P2, or another explicitly scoped proof path.

## 7. Non-claims

1. Does not promote `HG-MTH-011` to theorem-grade. It lifts `HG-MTH-011` to method-grade modulo six candidate Tier-1 surfaces.
2. Does not introduce new mathematics. It references and assembles the four sub-obligation closures.
3. Does not normalize `HG-FND-001`, `HG-FND-002`, `HG-FND-003`, `HG-FND-006`, `HG-FND-007`, or `HG-VOC-006`.
4. Does not close P1, the path-beta characterization obligation.
5. Does not close P2, the candidate-list exhaustion obligation.
6. Does not extend to `A_n` for `n >= 3`.
7. Does not authorize Heller-Einstein PRs beyond already merged authorization paths.
8. Does not cross into downstream Clay-program proof claims, including `SocioProphet/yang-mills`.
9. Does not authorize Lane VIII residue-hunt work.
10. Does not retroactively promote A1 `zeta_2` source identification or other A1 surfaces beyond the P3.c sharpening already recorded.

## 8. Future promotion pathway

After this PR merges, the natural next directions become available, but none is authorized by this PR:

1. Tier-1 normalization tracks for `HG-FND-001`, `HG-FND-002`, `HG-FND-003`, `HG-FND-006`, `HG-FND-007`, and `HG-VOC-006`.
2. P1 — path-beta characterization.
3. P2 — candidate-list exhaustion.
4. `A_n` extension once A2 is treated as settled modulo the six explicit surfaces.
5. Lane VIII v0.2.3 residue hunt in `SocioProphet/yang-mills`, separately gated.
6. Heller-Einstein realization-question development, separately gated.

## 9. Identifier and registry

This document assigns:

```text
HG-MTH-021
```

to the P3 pipeline integration closure assembly.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. This PR updates that registry to register `HG-MTH-021` and updates the `HG-MTH-011` registry entry to reflect the P3 grade lift.
