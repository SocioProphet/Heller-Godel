# Framework-Core Anti-Seed Register

Status: bootstrap register.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This register names known failure modes, category mistakes, unsafe promotions, and overclaim patterns at the Heller-Godel framework level.

An anti-seed entry must exist before a positive framework object is promoted toward framework-foundational status.

## A-HG-FND-001 — Treating epsilon-time as physical time

The epsilon-time vocabulary in prior framework drafts is a curvature-defect or compatibility-failure vocabulary, not a physical duration, proper-time scalar, or empirical clock.

Failure mode:

```text
epsilon-time is cited as if it directly measures physical time.
```

Correct boundary:

```text
epsilon-time vocabulary must be typed as a compatibility or curvature-defect construction before it can be cited as framework content.
```

Status: source import and typing pending.

## A-HG-FND-002 — Treating Curv_3 as elementary abelian group cohomology

The broader framework vocabulary uses a `Curv_3 in H^3` apex obstruction phrase. This bootstrap does not promote that phrase as a mathematical object.

Failure mode:

```text
Curv_3 is computed or cited as an ordinary abelian cohomology class without specifying the relevant categorical, crossed-module, gerbe, or other typed structure.
```

Correct boundary:

```text
Curv_3 requires source import, typing, and proof/citation before any foundational promotion.
```

Status: source import and typing pending.

## A-HG-FND-003 — Treating broad Trinitarian Unity vocabulary as already theorem-grade

The Trinitarian Unity / Compat vocabulary from prior drafts may be important framework material, but this bootstrap does not make it theorem-grade.

Failure mode:

```text
A downstream repo cites Trinitarian Unity or Compat = (nabla, A_C, partial) as load-bearing infrastructure before this repo supplies a typed registered object.
```

Correct boundary:

```text
Drive-origin vocabulary remains provenance-grade until imported, typed, assigned an HG-* identifier, and reviewed.
```

Status: source import and typing pending.

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

## A-HG-VOC-001 — Treating Rosetta dictionary rows as proved identifications

Rosetta-style dictionary rows are target propositions or vocabulary alignments unless separately proved.

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

The lattice-tower vocabulary may be useful, but tower extensions beyond the currently active proof-character core are not automatically load-bearing.

Failure mode:

```text
A downstream repo cites A2 -> D4 -> E8 or sedenion/S15 vocabulary as theorem infrastructure without a registered, typed, reviewed object.
```

Correct boundary:

```text
Lattice-tower material enters as vocabulary unless and until promoted by a dedicated PR.
```

Status: source import pending.

## A-HG-MTH-001 — Treating Universal Bridge as proof transfer

Universal Bridge material, when imported, is a structural-analogy and methodology-transfer specification unless separately proved otherwise.

Failure mode:

```text
A downstream repo asserts that RH, Hodge, BSD, YM, P vs NP, or Navier-Stokes are equivalent because the bridge aligns their obstruction forms.
```

Correct boundary:

```text
The bridge may license shared vocabulary, claim-discipline, and missing-machinery comparisons. It does not license proof transfer or cross-Clay equivalence.
```

Status: active; governs HG-MTH-005 and extensions.

## A-HG-MTH-002 — Treating Catalan / mu_2 as Clay progress

The Catalan / mu_2 fixture is a cross-program apparatus-validation fixture.

Failure mode:

```text
Catalan / mu_2 output is cited as Hodge progress, RH progress, P vs NP progress, or Yang-Mills mass-gap progress.
```

Correct boundary:

```text
Catalan / mu_2 validates apparatus alignment only. It does not advance any Clay target by itself.
```

Status: active as `HG-EX-001` doctrine; implementation pending.

## A-HG-MTH-003 — Mixing fixture-grade and theorem-grade citations

Fixture-grade outputs are not theorem premises unless promoted by separate proof.

Failure mode:

```text
A downstream proof cites a fixture output as if it were a theorem-grade framework lemma.
```

Correct boundary:

```text
Every downstream citation must state citation grade: theorem-grade, method-grade, fixture-grade, or provenance-grade.
```

Status: governed by `docs/framework-core/claim-grammar.md`.

## A-HG-MTH-004 — Standard Conjectures cited diagnostically are not assumed

The `HG-MTH-006` Hodge bridge spec references Grothendieck Standard Conjectures B and D as diagnostic structural apparatus identifying shared missing machinery. The reference is diagnostic, not assumptive.

Failure mode:

```text
A downstream artifact cites HG-MTH-006 as if it assumed Standard Conjecture B or D for the variety under discussion.
```

Correct boundary:

```text
HG-MTH-006 references Standard Conjectures B and D as structural-obstruction diagnostic apparatus. Any artifact that assumes them as premises must declare that assumption explicitly and cannot invoke HG-MTH-006 as license for the assumption.
```

Closure condition:

```text
A-HG-MTH-004 closes only if the relevant Standard Conjectures are proven in the required generality. Until then, it remains active.
```

## A-HG-MTH-005 — Triple barrier cited diagnostically is not a circumvention recipe

The `HG-MTH-008` P vs NP bridge spec references the relativization / natural-proofs / algebrization triple as the structural apex obstruction for the complexity domain. The reference is diagnostic: the triple identifies classes of techniques that cannot resolve P vs NP.

Failure mode:

```text
A downstream artifact cites HG-MTH-008 as if the citation certifies that its technique evades relativization, natural proofs, or algebrization.
```

Correct boundary:

```text
HG-MTH-008 references the triple barrier as structural-obstruction diagnostic apparatus. A downstream artifact citing HG-MTH-008 inherits the diagnosis, not a license to claim that any candidate program has escaped all three barriers.
```

Closure condition:

```text
A-HG-MTH-005 closes only if the three-barrier obstruction is formally resolved by a corresponding separation result or a meta-theorem that subsumes the barriers. Until then, it remains active.
```

## A-HG-MTH-006 — Component apparatus cited diagnostically is not Clay-grade YM resolution

The `HG-MTH-007` Yang-Mills bridge spec references three component structural obstructions: constructive QFT existence, continuum limit of lattice gauge theory, and spectral-action realization. Each component has substantial method-level apparatus.

Failure mode:

```text
A downstream artifact cites HG-MTH-007 as if method-level apparatus in one component constitutes Clay-grade Yang-Mills existence or mass-gap resolution.
```

Correct boundary:

```text
HG-MTH-007 references each component diagnostically. A downstream artifact citing HG-MTH-007 inherits the diagnostic reference for its component, not a license to claim Clay resolution. A fixed-lattice or narrow-scope theorem remains method-grade unless it supplies the full continuum constructive QFT and mass-gap result required by the Clay problem.
```

Closure condition:

```text
A-HG-MTH-006 closes only if the Clay Yang-Mills mass-gap problem is resolved with the required existence and mass-gap conditions in the continuum for non-abelian gauge groups. Until then, it remains active.
```

## A-HG-DOC-001 — Creating a second framework-core repo without need

The portfolio already has `SocioProphet/Heller-Godel`. Creating a separate `heller-godel-core` repo would split the canonical framework record.

Failure mode:

```text
Foundational material is placed in a new repo while Heller-Godel remains the active proof-character repo, producing two canonical framework homes.
```

Correct boundary:

```text
Use the existing Heller-Godel repo as framework core. Add directories and governance here.
```

Status: closed by this bootstrap declaration.

## A-HG-DOC-002 — Treating Drive originals as canonical after import

Once a Drive document is imported, normalized, and merged into this repo, the repo version becomes canonical for citation.

Failure mode:

```text
Downstream repos cite Drive RTF/PDF originals after a merged repo version exists.
```

Correct boundary:

```text
Drive originals remain provenance. Canonical citations use repo paths and merged commit SHAs.
```

Status: source import pending.

## Register maintenance

Anti-seed entries are append-preserving. Entries may be marked closed only when a structural correction makes the failure mode impossible or explicitly superseded.

Closed entries remain visible and cite the PR that closed them.
