# Framework-Core Distance Classification

Status: bootstrap taxonomy.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

Framework objects in `SocioProphet/Heller-Godel` are classified by distance from the currently defensible mathematical core. The classification controls what downstream repositories may cite and what those citations license.

## Tier 1 — Framework-foundational

Tier 1 contains load-bearing definitions, typed statements, proofs, and accepted theorem-level objects that the Heller-Godel framework rests on.

An object may be Tier 1 only if it has a stable identifier, typed statement, proof or citation, anti-seed, merged PR declaration, and no unresolved claim-boundary violation.

Normalized Tier 1 surfaces:

| Identifier | Object | Status |
| --- | --- | --- |
| `HG-FND-001` | Restricted proof grammar and declared statistics | normalized Tier 1; governed by `A-HG-FND-005`; source: `docs/framework-foundations/HG-FND-001-restricted-proof-grammar.md` |
| `HG-FND-002` | Proof-class / proof-family generating-function construction | normalized Tier 1; governed by generating-function anti-seeds in `docs/framework-core/anti-seed-framework.md`; source: `docs/framework-foundations/HG-FND-002-proof-class-generating-function.md` |
| `HG-FND-003` | Puiseux singular datum at a chosen puncture | normalized Tier 1; governed by `A-HG-FND-007`; source: `docs/framework-foundations/HG-FND-003-puiseux-singular-datum.md` |
| `HG-FND-004` | Branch-killing cyclic cover and singular unit upstairs | normalized Tier 1; governed by `A-HG-FND-010`; source: `docs/framework-foundations/HG-FND-004-branch-killing-cover-singular-unit.md` |
| `HG-FND-005` | Level-1 Deligne-unit framing | normalized Tier 1; governed by `A-HG-FND-011`; source: `docs/framework-foundations/HG-FND-005-level-1-deligne-unit-framing.md` |
| `HG-FND-006` | Finite monodromy / deck-character interpretation | normalized Tier 1; governed by `A-HG-FND-008`; source: `docs/framework-foundations/HG-FND-006-finite-monodromy-deck-character.md` |
| `HG-FND-007` | Lifted phase index and section-defect carry cocycle | normalized Tier 1; governed by `A-HG-FND-009`; source: `docs/framework-foundations/HG-FND-007-lifted-phase-index-carry-cocycle.md` |

The full normalized Tier 1 surface is now: `HG-FND-001`, `HG-FND-002`, `HG-FND-003`, `HG-FND-004`, `HG-FND-005`, `HG-FND-006`, and `HG-FND-007`.

Candidate inventory for future review:

| Candidate identifier | Object | Bootstrap status |
| --- | --- | --- |
| `HG-FND-008` | Deligne cup-product / regulator-symbol separation from carry | candidate; active core exists, registry normalization pending; best after `HG-FND-005` |

## Tier 2 — Framework-vocabulary

Tier 2 contains mathematical vocabulary, worked structures, and framework dictionaries expressed in terms of Tier 1 objects or candidate Tier 1 objects.

An object may be Tier 2 only if it has a stable identifier, construction or dictionary entry, anti-seed, and distance cap preventing theorem-grade citation.

Normalized Tier 2 surfaces:

| Identifier | Object | Status |
| --- | --- | --- |
| `HG-VOC-006` | Character data, roots of unity, and finite phase reductions | normalized Tier 2; governed by `A-HG-VOC-006`; source: `docs/framework-vocabulary/HG-VOC-006-character-data-finite-phase-reductions.md` |

Candidate inventory for future review:

| Candidate identifier | Object | Bootstrap status |
| --- | --- | --- |
| `HG-VOC-001` | Lawful Learning / Rosetta dictionary | source import pending; illustrative-grade cap required |
| `HG-VOC-002` | Lattice tower vocabulary | source import pending; load-bearing cap required |
| `HG-VOC-003` | Hopf testbed vocabulary | source import pending |
| `HG-VOC-004` | Equilateral triangle billiard A2-rung analogy | source import pending; analogy cap required |
| `HG-VOC-005` | Proof-class moduli vocabulary | active scaffold exists; nonclaim cap required |

## Tier 3 — Framework-method

Tier 3 contains methods, bridge specifications, governance rules, and apparatus-validation fixtures.

Initial bootstrap registrations:

| Identifier | Object | Status |
| --- | --- | --- |
| `HG-MTH-001` | Framework-core distance classification | active governance object |
| `HG-MTH-002` | Claim grammar and downstream citation rule | active governance object |
| `HG-MTH-003` | Framework dependency graph | active governance object |
| `HG-MTH-004` | Anti-seed framework register | active governance object |
| `HG-EX-001` | Catalan / mu_2 canonical reference fixture | active doctrine object; implementation pending |

Universal Bridge material will enter Tier 3 by default when imported. It may not be cited as proof equivalence or proof transfer.

## Tier 4 — Framework-fallout / downstream consumers

Tier 4 consists of downstream repositories that cite Heller-Godel framework objects.

Tier 4 content is not stored here except as inventory in `docs/framework-core/dependency-graph.md` and `DEPENDENCIES.md`.

## Promotion rule

New objects enter at Tier 3 by default unless the PR explicitly requests a higher tier.

Promotion toward Tier 1 requires anti-seed registration, typing, proof or citation, claim-boundary review, and registry update.

Demotion is allowed by the same procedure and must preserve the historical record.

## Hard caps

- Drive source material is provenance until imported and reviewed.
- Chat transcripts are provenance until converted into repo-grade text.
- Downstream claims do not promote upstream framework objects.
- Fixture success does not imply theorem progress.
- Structural analogy does not imply proof transfer.
