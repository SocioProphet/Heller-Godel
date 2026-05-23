# Framework-Core Claim Grammar

Status: bootstrap governance rule.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This document defines how Heller-Godel framework objects are identified and cited by downstream program repositories.

## Stable identifier scheme

Framework objects use identifiers of the form:

```text
HG-{LAYER}-{NNN}
```

where:

- `HG` is the repository namespace for `SocioProphet/Heller-Godel`;
- `LAYER` is one of `FND`, `VOC`, `MTH`, `EX`, `REF`, or `DOC`;
- `NNN` is a zero-padded three-digit number.

Optional version tags may be used in prose when an object has materially changed:

```text
HG-FND-001 v0.2
```

The canonical citation should still include the merged commit SHA.

## Layer codes

| Layer | Meaning |
| --- | --- |
| `FND` | Framework-foundational object |
| `VOC` | Framework-vocabulary object |
| `MTH` | Framework-method or governance method |
| `EX` | Worked example or canonical fixture |
| `REF` | Bibliographic or provenance reference |
| `DOC` | Governance / doctrine object |

## Downstream citation form

Downstream Clay-program repositories should cite framework objects as:

```text
[HG-FND-001 @ <merged-main-commit-sha>]
```

The commit SHA must reference a merged commit on `main`, not a floating branch tip and not the current `main` alias.

## Required citation metadata

A downstream citation should record:

1. framework identifier;
2. merged Heller-Godel commit SHA;
3. distance tier;
4. citation grade: `theorem-grade`, `method-grade`, `fixture-grade`, or `provenance-grade`;
5. the exact local claim licensed by the citation.

## Citation grades

| Grade | Meaning | May license |
| --- | --- | --- |
| `theorem-grade` | typed proved or canonically cited object | theorem premises within declared scope |
| `method-grade` | method, governance rule, bridge specification, or classification | procedure, analogy, taxonomy, or review discipline |
| `fixture-grade` | worked example or canonical fixture | apparatus alignment only |
| `provenance-grade` | source capture, historical note, imported Drive artifact, or unpromoted draft | historical origin only |

## Forbidden citation patterns

The following are forbidden:

- citing an `HG-*` object without a merged commit SHA in downstream theorem-grade text;
- citing Drive RTF/PDF material as canonical after it has an imported repo version;
- citing a fixture as proof of progress on a Clay problem;
- citing Universal Bridge material as proof equivalence or proof transfer;
- citing an anti-seed entry as positive mathematical content;
- using downstream Clay-program success to promote an upstream Heller-Godel object without a Heller-Godel promotion PR.

## Anti-seed precedence

Every positive framework object should have an associated anti-seed entry before promotion.

The anti-seed entry does not prove the positive object. It records a failure mode and constrains unsafe uses.

## Bootstrap active identifiers

| Identifier | Object | Grade | Status |
| --- | --- | --- | --- |
| `HG-MTH-001` | Framework-core distance classification | method-grade | active |
| `HG-MTH-002` | Claim grammar and citation rule | method-grade | active |
| `HG-MTH-003` | Dependency graph | method-grade | active |
| `HG-MTH-004` | Anti-seed framework register | method-grade | active |
| `HG-MTH-005` | Universal Bridge formal specification | method-grade only | active |
| `HG-MTH-006` | Universal Bridge extension to algebraic-geometric / Hodge domain | method-grade only | active |
| `HG-MTH-007` | Universal Bridge extension to gauge / Yang-Mills domain | method-grade only | active; depends on Heller-Dirac @ `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993` |
| `HG-MTH-008` | Universal Bridge extension to complexity / P vs NP domain | method-grade only | active |
| `HG-MTH-009` | Universal Bridge extension to arithmetic-geometric / BSD domain | method-grade only | active; depends on Heller-Dirac @ `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993` |
| `HG-MTH-011` | A2 minimality candidate-theorem under path-beta gate-minimality | method-grade modulo six candidate Tier-1 surfaces after P3 closure; historical grade was method-grade as candidate theorem | active after `HG-MTH-021` if merged |
| `HG-MTH-012` | P3 pipeline-integration scope for A2 minimality candidate-theorem | method-grade as scope | active after this PR if merged |
| `HG-MTH-013` | P3.a restricted proof grammar at p=3 scope | method-grade as scope | active after this PR if merged |
| `HG-MTH-014` | P3.a restricted proof grammar at p=3 closure | method-grade modulo candidate-HG-FND-001 | active after this PR if merged |
| `HG-MTH-015` | P3.b canonical statistic and generating-function at p=3 scope | method-grade as scope | active after this PR if merged |
| `HG-MTH-016` | P3.b canonical statistic and generating-function at p=3 closure | method-grade modulo candidate-HG-FND-002 | active after this PR if merged |
| `HG-MTH-017` | P3.c Puiseux singularity and chi_3 at p=3 scope | method-grade as scope | active after this PR if merged |
| `HG-MTH-018` | P3.c Puiseux singularity and chi_3 at p=3 closure | method-grade modulo candidate-HG-FND-003 and candidate-HG-VOC-006 | active after this PR if merged |
| `HG-MTH-019` | P3.d zeta_3 carry defect and U(2) correspondence at p=3 scope | method-grade as scope | active after this PR if merged |
| `HG-MTH-020` | P3.d zeta_3 carry defect and U(2) correspondence at p=3 closure | method-grade modulo candidate-HG-FND-006 and candidate-HG-FND-007 | active after this PR if merged |
| `HG-MTH-021` | P3 pipeline-integration closure assembly for A2 minimality candidate-theorem | method-grade modulo six candidate Tier-1 surfaces | active after this PR if merged |
| `HG-EX-001` | Catalan / mu_2 canonical reference fixture | fixture-grade | active doctrine; implementation pending |
| `HG-DOC-001` | Framework-core declaration for existing Heller-Godel repo | method-grade / governance | active |

## Reserved method identifiers

The following identifiers are reserved for future source imports and may not be used by downstream repositories until a Heller-Godel PR imports the corresponding source material and declares the citation grade.

| Identifier | Reserved object | Intended grade | Status |
| --- | --- | --- |
| `HG-MTH-010` | Clay coverage / Navier-Stokes decision record | governance / method-grade | reserved; decision pending |

Reservation does not license citation. It prevents identifier collision only.

The governing anti-seed for `HG-MTH-005..009` is `A-HG-MTH-001`: Universal Bridge material does not prove cross-Clay equivalence and does not transfer proofs between Clay domains.

`HG-MTH-006` additionally cites `A-HG-MTH-004`: Standard Conjectures cited diagnostically are not assumed.

`HG-MTH-007` additionally cites `A-HG-MTH-006`: component apparatus cited diagnostically is not Clay-grade Yang-Mills resolution.

`HG-MTH-008` additionally cites `A-HG-MTH-005`: triple-barrier diagnosis is not a circumvention recipe.

`HG-MTH-009` additionally cites `A-HG-MTH-007`: BSD-rank and BSD-strong have distinct structural status.

`HG-MTH-011` additionally inherits the Heller-Godel standing non-claims for gate-minimality and the P3 assembly non-claims: it is not theorem-track promoted, does not establish absolute A2 minimality outside its candidate-list and path-beta scope, does not claim path-beta uniqueness, does not close P1 or P2, does not extend to an `A_n` theorem family, does not normalize the six candidate surfaces `HG-FND-001`, `HG-FND-002`, `HG-FND-003`, `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`, and does not cross into downstream Clay-program proof claims.

`HG-MTH-012` additionally inherits the P3 scope non-claims: it does not close P3, does not promote `HG-MTH-011`, does not specify the `chi_3` generating function / Puiseux singularity / `zeta_3` carry defect, does not authorize Heller-Einstein development, and does not cross into downstream Clay-program proof claims.

`HG-MTH-013` additionally inherits the P3.a scope non-claims: it does not close P3.a, does not select a `p=3` grammar, does not specify the `p=3` canonical statistic / generating function / Puiseux singularity / `zeta_3` carry defect, does not promote `HG-FND-001` from candidate to settled Tier-1 status, does not authorize Heller-Einstein development, and does not cross into downstream Clay-program proof claims.

`HG-MTH-014` additionally inherits the P3.a closure non-claims: it does not promote `HG-FND-001` from candidate to settled Tier-1 status, does not promote `HG-MTH-011`, does not close P3.b / P3.c / P3.d, does not make P3.c-grade Puiseux claims, does not specify `zeta_3` or its `U(2)` correspondence, does not extend to `A_n`, does not authorize Heller-Einstein development, and does not cross into downstream Clay-program proof claims.

`HG-MTH-015` additionally inherits the P3.b scope non-claims: it does not close P3.b, does not select a P3.b verification strategy, does not specify `rho_3` or `alpha_3` as closure-grade, does not specify `zeta_3` or the `U(2)` correspondence, does not promote `HG-FND-001` or `HG-FND-002`, does not promote `HG-MTH-011`, does not extend to `A_n`, does not authorize Heller-Einstein development, and does not cross into downstream Clay-program proof claims.

`HG-MTH-016` additionally inherits the P3.b closure non-claims: it does not promote `HG-FND-002` or `HG-FND-001` from candidate to settled Tier-1 status, does not close P3.c or P3.d, does not make P3.c-grade radius / Puiseux / `chi_3` claims, does not specify `zeta_3` or its `U(2)` correspondence, does not promote `HG-MTH-011`, does not extend to `A_n`, does not authorize Heller-Einstein development, and does not cross into downstream Clay-program proof claims.

`HG-MTH-017` additionally inherits the P3.c scope non-claims: it does not close P3.c, does not select among the P3.c verification strategies or Q4 character-source options, does not specify explicit Puiseux expansion constants, does not specify the precise `mu_3` element of `chi_3`, does not assert that `chi_3` emerges from local square-root monodromy, does not use `phase_characters.py` as the analytic source of `chi_3`, does not specify `zeta_3` or its `U(2)` correspondence, does not promote `HG-FND-003` or `HG-VOC-006`, does not promote `HG-MTH-011`, does not extend to `A_n`, does not authorize Heller-Einstein development, and does not cross into downstream Clay-program proof claims.

`HG-MTH-018` additionally inherits the P3.c closure non-claims: it does not promote `HG-FND-003` or `HG-VOC-006`, does not close P3.d, does not specify `zeta_3` or its `U(2)` correspondence, does not promote `HG-MTH-011`, does not retroactively promote A1 `chi_2` source identification to theorem-grade, does not extend to `A_n`, does not authorize Heller-Einstein development, does not cross into downstream Clay-program proof claims, does not normalize `HG-FND-*` or `HG-VOC-*` surfaces, does not use `phase_characters.py` as the analytic source of `chi_3`, and does not claim that the orientation convention is independent of the selected cyclic sheet generator.

`HG-MTH-019` additionally inherits the P3.d scope non-claims: it does not close P3.d, does not select among the `zeta_3` candidate structures or `U(2)` correspondence strategies, does not specify the natural character from a selected `zeta_3` host to `mu_3`, does not assemble the full P3 closure document, does not promote `HG-MTH-011`, does not promote or normalize any candidate `HG-FND-*` or `HG-VOC-006` surface, does not extend to `A_n`, does not authorize Heller-Einstein development, does not cross into downstream Clay-program proof claims, and does not retroactively promote A1 `zeta_2` source identification.

`HG-MTH-020` additionally inherits the P3.d closure non-claims: it does not claim `zeta_3` represents a nontrivial cohomology class, does not assemble the full P3 closure document, does not promote `HG-MTH-011`, does not normalize `HG-FND-006` or `HG-FND-007`, does not retroactively promote A1 `zeta_2` source identification, does not extend to `A_n`, does not authorize Heller-Einstein development, does not cross into downstream Clay-program proof claims, does not adopt the raw determinant character as the selected `mu_3` character, does not claim that `HG-FND-006` is normalized, does not claim that `Z_3` is a topological triple-cover lift of `SU(3)`, and does not identify the scalar cocycle `zeta_3(alpha,beta)` with the group element `Z_3`.

`HG-MTH-021` additionally inherits the P3 closure assembly non-claims: it does not promote `HG-MTH-011` to theorem-grade, does not introduce new mathematics, does not normalize `HG-FND-001`, `HG-FND-002`, `HG-FND-003`, `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`, does not close P1 or P2, does not extend to `A_n`, does not authorize Heller-Einstein development, does not cross into downstream Clay-program proof claims, and does not authorize Lane VIII work.

## Deferred non-blocking queue

The following observations are recorded for future authorization only. They are not actions opened by this PR:

1. Bibliography reference-hardening PR — non-blocking.
2. Claim-boundary guard extension — non-blocking CI hardening.
3. Unicode typography normalization sweep — non-blocking cosmetic.
4. PR-body verbosity convention — committed file authoritative, PR body intentionally minimal.
5. `HG-FND-001` normalization — future obligation distinct from P3.a; current status remains candidate / registry normalization pending.
6. Workflow infrastructure hardening — non-blocking; covers docs-only trigger gaps, dense PR payload blocks, and intermittent proof-apparatus controller checkout/auth flakiness.
7. `HG-FND-002` normalization — future obligation distinct from P3.b; current status remains candidate / registry normalization pending.
8. `HG-FND-003` normalization — future obligation distinct from P3.c; current status remains candidate / registry normalization pending.
9. `HG-VOC-006` normalization — future obligation distinct from P3.c; current status remains candidate / registry normalization pending.
10. `HG-FND-006` normalization — future obligation distinct from P3.d; current status remains candidate / registry normalization pending.
11. `HG-FND-007` normalization — future obligation distinct from P3.d; current status remains candidate / registry normalization pending.

## PFK namespace separation

Proof Fabric Kernel infrastructure must not consume `HG-*` identifiers for its own schemas, validators, receipts, or Event-IR objects.

PFK uses a separate namespace:

```text
PFK-{LAYER}-{NNN}
```

This keeps Heller-Godel framework vocabulary (`HG-*`) separate from proof-fabric operational substrate (`PFK-*`).

## Existing Paper I identifiers

Existing Paper I artifacts may retain their current local names and theorem labels. This bootstrap does not rewrite manuscript numbering.

Future PRs may add an identifier crosswalk mapping manuscript theorem labels and proof artifacts into the `HG-*` registry. Until that crosswalk exists, downstream repos should cite file paths and commit SHAs in addition to any manuscript-local labels.

## Example downstream citation block

```markdown
Framework citations:

- [HG-EX-001 @ <sha>] — Catalan / mu_2 fixture; citation grade: fixture-grade;
  licensed use: apparatus-alignment check only.
- [HG-MTH-002 @ <sha>] — claim grammar; citation grade: method-grade;
  licensed use: downstream citation format.
- [HG-MTH-005 @ <sha>] — Universal Bridge formal specification; citation grade: method-grade;
  licensed use: methodology transfer and shared-missing-machinery diagnosis only.
- [HG-MTH-006 @ <sha>] — Hodge-domain Universal Bridge extension; citation grade: method-grade;
  licensed use: Hodge shared-missing-machinery diagnosis only.
- [HG-MTH-007 @ <sha>] — Yang-Mills gauge-domain Universal Bridge extension; citation grade: method-grade;
  licensed use: gauge shared-missing-machinery diagnosis only.
- [HG-MTH-008 @ <sha>] — P vs NP / complexity-domain Universal Bridge extension; citation grade: method-grade;
  licensed use: complexity shared-missing-machinery diagnosis only.
- [HG-MTH-009 @ <sha>] — BSD arithmetic-geometric-domain Universal Bridge extension; citation grade: method-grade;
  licensed use: BSD shared-missing-machinery diagnosis only.
- [HG-MTH-011 @ <sha>] — A2 minimality candidate-theorem under path-beta; citation grade: method-grade modulo six candidate Tier-1 surfaces after P3 closure;
  licensed use: A2 gate-minimality candidate-list reasoning and P3-integrated proof-character attachment only, not theorem-track downstream input.
- [HG-MTH-012 @ <sha>] — P3 pipeline-integration scope for HG-MTH-011; citation grade: method-grade as scope;
  licensed use: obligation specification only, not P3 closure or theorem-track promotion.
- [HG-MTH-013 @ <sha>] — P3.a restricted proof grammar at p=3 scope; citation grade: method-grade as scope;
  licensed use: obligation specification only, not P3.a closure, grammar selection, or theorem-track promotion.
- [HG-MTH-014 @ <sha>] — P3.a restricted proof grammar at p=3 closure; citation grade: method-grade modulo candidate-HG-FND-001;
  licensed use: P3.a grammar closure only, not P3.b/P3.c/P3.d closure or theorem-track promotion.
- [HG-MTH-015 @ <sha>] — P3.b canonical statistic and generating-function at p=3 scope; citation grade: method-grade as scope;
  licensed use: P3.b obligation specification only, not P3.b closure or theorem-track promotion.
- [HG-MTH-016 @ <sha>] — P3.b canonical statistic and generating-function at p=3 closure; citation grade: method-grade modulo candidate-HG-FND-002;
  licensed use: P3.b closure only, not P3.c/P3.d closure or theorem-track promotion.
- [HG-MTH-017 @ <sha>] — P3.c Puiseux singularity and chi_3 at p=3 scope; citation grade: method-grade as scope;
  licensed use: P3.c obligation specification only, not P3.c closure, `chi_3` identification, or theorem-track promotion.
- [HG-MTH-018 @ <sha>] — P3.c Puiseux singularity and chi_3 at p=3 closure; citation grade: method-grade modulo candidate-HG-FND-003 and candidate-HG-VOC-006;
  licensed use: P3.c closure only, not P3.d closure, HG-MTH-011 promotion, or Tier-1 normalization.
- [HG-MTH-019 @ <sha>] — P3.d zeta_3 carry defect and U(2) correspondence at p=3 scope; citation grade: method-grade as scope;
  licensed use: P3.d obligation specification only, not P3.d closure, full P3 closure, HG-MTH-011 promotion, or Tier-1 normalization.
- [HG-MTH-020 @ <sha>] — P3.d zeta_3 carry defect and U(2) correspondence at p=3 closure; citation grade: method-grade modulo candidate-HG-FND-006 and candidate-HG-FND-007;
  licensed use: P3.d closure only, not full P3 closure, HG-MTH-011 promotion, or Tier-1 normalization.
- [HG-MTH-021 @ <sha>] — P3 pipeline-integration closure assembly; citation grade: method-grade modulo six candidate Tier-1 surfaces;
  licensed use: P3 closure assembly and HG-MTH-011 grade lift only, not theorem-grade promotion or Tier-1 normalization.
```

## Review rule

A PR that adds an `HG-*` identifier must update this document or `docs/framework-core/distance-classification.md` in the same PR.
