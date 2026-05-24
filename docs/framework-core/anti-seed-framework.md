# Framework-Core Anti-Seed Register

Status: bootstrap register.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This register names known failure modes, category mistakes, unsafe promotions, and overclaim patterns at the Heller-Godel framework level.

An anti-seed entry must exist before a positive framework object is promoted toward framework-foundational status.

## A-HG-FND-004 — Confusing carry cocycle with Deligne cup-product/regulator symbol

The active Paper I core separates the finite-resolution carry defect from Deligne cup-product / regulator-symbol data.

Failure mode:

```text
zeta_p or the section-defect carry cocycle is identified with the Deligne cup-product symbol or a regulator residue.
```

Correct boundary:

```text
The carry term is a finite-resolution section defect. The Deligne cup-product symbol is a regulator-symbol refinement of level-1 units. They are not identified.
```

Status: active boundary already enforced by the existing Paper I claim grammar and CI claim-boundary guard.

## A-HG-FND-005 — Treating untyped tree analogies as typed proof grammars

Failure mode:

```text
A downstream artifact cites a rooted-tree, Catalan, or Fuss-Catalan enumeration as theorem-bearing proof-family data without specifying the typed fragment, normal-form convention, witness equivalence, and statistic.
```

Correct boundary:

```text
Tree enumerations are admissible only as visualizations or derived enumerators of a normalized restricted proof grammar with typed normal-form witnesses and a declared statistic.
```

Status: active; governs `HG-FND-001`.

## A-HG-FND-006 — Treating unstatted series as proof-family generating functions

Failure mode:

```text
A downstream artifact cites a power series as a proof-class generating function without specifying the `HG-FND-001` restricted grammar, witness family `N_phi`, and statistic `sigma` that produce it.
```

Correct boundary:

```text
A proof-family generating function must declare its typed witness family and statistic before it can be cited through `HG-FND-002`.
```

Status: active; governs `HG-FND-002`.

## A-HG-FND-007 — Treating undecorated singularities as Puiseux data

Failure mode:

```text
A downstream artifact treats the singularity of a proof-family generating function as proof-grade Puiseux datum without choosing the puncture, coordinate, branch convention, and local expansion required by `HG-FND-003`.
```

Second failure mode:

```text
A downstream artifact treats local square-root sign-change behavior at a chosen puncture as character-source data owned by `HG-VOC-006`.
```

Correct boundary:

```text
`HG-FND-002` may identify `rho` and `alpha`; `HG-FND-003` owns the chosen-puncture Puiseux datum; `HG-VOC-006` owns character data, roots of unity, and finite phase reductions.
```

Status: active; governs the `HG-FND-002` / `HG-FND-003` / `HG-VOC-006` boundary.

## A-HG-FND-008 — Treating deck-character multiplicativity as carry triviality

Failure mode:

```text
A downstream artifact asserts that because characters multiply in the finite root-of-unity group, the carry cocycle of the integer lift is zero.
```

Correct boundary:

```text
Multiplicativity is a property of the character in the finite root-of-unity group; the carry is a section-defect of the integer lift and is generically nonzero.
```

Status: active; governs `HG-FND-006` and its boundary with `HG-FND-007`.

## A-HG-FND-009 — Section carry comparison boundary

Boundary: `HG-FND-007` owns the integer-valued section-defect carry only. Any comparison with another mathematical surface requires a separate normalized typed bridge.

Status: active; governs `HG-FND-007`.

## A-HG-FND-010 — Treating branch-killing cover as constructed without source datum

Failure mode:

```text
A downstream artifact cites the branch-killing cover or singular unit upstairs without declaring the Puiseux datum, branch-killing level, and branch convention supplied by `HG-FND-003`.
```

Correct boundary:

```text
`HG-FND-004` citation requires the base Puiseux datum, local coordinate, level, branch convention, cover equation, upstairs unit, and normalization convention.
```

Status: active; governs `HG-FND-004`.

## A-HG-FND-011 — Treating tame-symbol evaluation as carry-cocycle identification

Failure mode:

```text
A downstream artifact treats a tame-symbol evaluation as proof that the Deligne-unit class equals the carry cocycle without a separate normalized comparison surface.
```

Second failure mode:

```text
A downstream artifact treats the Deligne-unit class as proof-grade without declaring the cover, puncture, and normalization condition supplied by `HG-FND-004`.
```

Correct boundary:

```text
The tame symbol is the evaluation of a level-1 Deligne-unit datum. The carry cocycle is an integer section defect. They are not identified without `HG-FND-008` or another separately normalized comparison surface.
```

Status: active; governs `HG-FND-005`.

## A-HG-FND-012 — Treating the operational separation witness as a complete structural proof

Failure mode:

```text
A downstream artifact treats numeric disagreement between tame-symbol and carry test outputs as a complete structural proof without declaring the domain, codomain, and algebraic-law distinction.
```

Second failure mode:

```text
A downstream artifact treats the operational witness as an identification in a deeper shared object rather than as a typed separation witness.
```

Correct boundary:

```text
The operational witness demonstrates non-equality in concrete test cases. The structural separation requires the domain, codomain, and algebraic-law argument normalized by `HG-FND-008`.
```

Status: active; governs `HG-FND-008`.

## A-HG-VOC-001 — Treating Rosetta dictionary rows as proved identifications

Failure mode:

```text
A downstream repo cites a Rosetta row as a theorem-grade identity.
```

Correct boundary:

```text
Rosetta material enters as framework-vocabulary with an illustrative or method-grade cap until row-level proof exists.
```

Status: source import pending.

## A-HG-VOC-002 — Treating lattice-tower or Cayley-Dickson material as load-bearing by default

Failure mode:

```text
A downstream repo cites lattice-tower vocabulary as theorem infrastructure without a registered, typed, reviewed object.
```

Correct boundary:

```text
Lattice-tower material enters as vocabulary unless and until promoted by a dedicated PR.
```

Status: source import pending.

## A-HG-VOC-006 — Treating chi_3 as proof-grade without source declaration

Failure mode:

```text
A downstream artifact treats chi_3 as proof-grade without declaring global Galois source, generator convention, and manuscript alignment.
```

Correct boundary:

```text
`HG-VOC-006` citation requires all three: global Galois source, generator convention, and manuscript alignment.
```

Status: active; governs `HG-VOC-006`.

## A-HG-MTH-001 — Treating Universal Bridge as proof transfer

Failure mode:

```text
A downstream repo asserts that multiple Clay-style targets are equivalent because the bridge aligns their obstruction forms.
```

Correct boundary:

```text
The bridge may license shared vocabulary, claim-discipline, and missing-machinery comparisons. It does not license proof transfer or cross-problem equivalence.
```

Status: active; governs HG-MTH-005 and extensions.

## A-HG-MTH-002 — Treating Catalan / mu_2 as Clay progress

Failure mode:

```text
Catalan / mu_2 output is cited as progress on a downstream target.
```

Correct boundary:

```text
Catalan / mu_2 validates apparatus alignment only. It does not advance any Clay target by itself.
```

Status: active as `HG-EX-001` doctrine; implementation pending.

## A-HG-MTH-003 — Mixing fixture-grade and theorem-grade citations

Failure mode:

```text
A downstream proof cites a fixture output as if it were a theorem-grade framework lemma.
```

Correct boundary:

```text
Every downstream citation must state citation grade: theorem-grade, method-grade, fixture-grade, or provenance-grade.
```

Status: governed by `docs/framework-core/claim-grammar.md`.

## A-HG-MTH-004 — Citing HG-MTH-018 theorem-grade without declared orientation convention

Failure mode:

```text
A downstream artifact cites HG-MTH-018 as theorem-grade chi_3 data without declaring the positive cyclic sheet generator tau=(123), or treats chi_3=omega as orientation-independent.
```

Correct boundary:

```text
HG-MTH-018 theorem-grade citation requires declared positive generator tau=(123). Reversing gives chi_3(tau^{-1})=omega^2. The character value is not orientation-independent.
```

Status: active; governs `HG-MTH-018`.

## A-HG-MTH-005 — Citing HG-MTH-016 theorem-grade without declared statistic and branch

Failure mode:

```text
A downstream artifact cites HG-MTH-016 as theorem-grade generating-function data without declaring the constructor-shape statistic and selected local branch C_3(0)=1, or treats the P3.b closure as a decorated Puiseux singular datum.
```

Correct boundary:

```text
HG-MTH-016 theorem-grade citation licenses only the constructor-shape P3.b generating-function equation, coefficient extraction, and selected local analytic branch at the origin. Dominant singularity decoration, Puiseux coefficients, monodromy, and chi_3 source identification belong to HG-MTH-018 / HG-FND-003 / HG-VOC-006.
```

Status: active; governs `HG-MTH-016`.

## Register maintenance

Anti-seed entries are append-preserving. Entries may be marked closed only when a structural correction makes the failure mode impossible or explicitly superseded.

Closed entries remain visible and cite the PR that closed them.
