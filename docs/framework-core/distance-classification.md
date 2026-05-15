# Framework-Core Distance Classification

Status: bootstrap taxonomy.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

Framework objects in `SocioProphet/Heller-Godel` are classified by distance from the currently defensible mathematical core. The classification controls what downstream Clay-program repositories may cite and what those citations license.

## Tier 1 — Framework-foundational

Tier 1 contains load-bearing definitions, typed statements, proofs, and accepted theorem-level objects that the Heller-Godel framework rests on.

An object may be Tier 1 only if it has:

1. a stable `HG-FND-NNN` identifier;
2. a typed mathematical statement;
3. a proof or precise citation to a canonical proof;
4. an anti-seed entry naming at least one failure mode;
5. a merged PR declaring Tier 1 status;
6. no unresolved claim-boundary violation.

Initial Tier 1 candidates are not automatically promoted by this bootstrap. They must be normalized in later PRs.

Candidate inventory for future review:

| Candidate identifier | Object | Bootstrap status |
| --- | --- | --- |
| `HG-FND-001` | Restricted proof grammar and canonical statistic | candidate; active core exists, registry normalization pending |
| `HG-FND-002` | Proof-class / proof-family generating-function construction | candidate; active core exists, registry normalization pending |
| `HG-FND-003` | Puiseux singular datum at a chosen puncture | candidate; active core exists, registry normalization pending |
| `HG-FND-004` | Branch-killing cyclic cover and singular unit upstairs | candidate; active core exists, registry normalization pending |
| `HG-FND-005` | Level-1 Deligne-unit framing | candidate; active core exists, registry normalization pending |
| `HG-FND-006` | Finite monodromy / deck-character interpretation | candidate; active core exists, registry normalization pending |
| `HG-FND-007` | Lifted phase index and section-defect carry cocycle | candidate; active core exists, registry normalization pending |
| `HG-FND-008` | Deligne cup-product / regulator-symbol separation from carry | candidate; active core exists, registry normalization pending |

Historical or broader framework objects such as Trinitarian Unity, Compat = `(nabla, A_C, partial)`, epsilon-time, `S_4`, `Curv_3 in H^3`, and TQFT-functor vocabulary are not promoted by this bootstrap. They require source import, anti-seed registration, typing, and review.

## Tier 2 — Framework-vocabulary

Tier 2 contains mathematical vocabulary, worked structures, and framework dictionaries expressed in terms of Tier 1 objects or candidate Tier 1 objects.

An object may be Tier 2 only if it has:

1. a stable `HG-VOC-NNN` identifier;
2. a construction or dictionary entry with explicit dependency on Tier 1 or candidate Tier 1 objects;
3. an anti-seed entry;
4. a distance cap preventing theorem-grade citation.

Candidate inventory for future review:

| Candidate identifier | Object | Bootstrap status |
| --- | --- | --- |
| `HG-VOC-001` | Lawful Learning / Rosetta dictionary | source import pending; illustrative-grade cap required |
| `HG-VOC-002` | Lattice tower vocabulary | source import pending; load-bearing cap required |
| `HG-VOC-003` | Hopf testbed vocabulary | source import pending |
| `HG-VOC-004` | Equilateral triangle billiard A2-rung analogy | source import pending; analogy cap required |
| `HG-VOC-005` | Proof-class moduli vocabulary | active scaffold exists; nonclaim cap required |
| `HG-VOC-006` | Character data `chi_p`, roots of unity, and finite phase reductions | active core exists; registry normalization pending |

## Tier 3 — Framework-method

Tier 3 contains methods, bridge specifications, governance rules, and apparatus-validation fixtures.

An object may be Tier 3 only if it has:

1. a stable `HG-MTH-NNN` or `HG-EX-NNN` identifier;
2. explicit input/output typing or governance scope;
3. an anti-seed entry;
4. a statement of what the method does not license.

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

Tier 4 consists of downstream Clay-program repositories that cite Heller-Godel framework objects.

Tier 4 content is not stored here except as inventory in `docs/framework-core/dependency-graph.md` and `DEPENDENCIES.md`.

Downstream consumers include:

- `SocioProphet/Heller-Winters-Theorem`
- `SocioProphet/yang-mills`
- `SocioProphet/hodge-program-proof`
- `SocioProphet/np-program`
- `SocioProphet/bsd-proof-program`
- `SocioProphet/Heller-Dirac` after purpose declaration
- `SocioProphet/navier-stokes-program` only if commissioned

## Promotion rule

New objects enter at Tier 3 by default unless the PR explicitly requests a higher tier.

Promotion toward Tier 1 requires:

1. a PR labeled or titled as a promotion;
2. an anti-seed entry before positive promotion;
3. typed statement and dependency declaration;
4. proof, citation, or evidence class;
5. claim-boundary review;
6. registry update in this file.

Demotion is allowed by the same procedure and must preserve the historical record.

## Hard caps

- Drive source material is provenance until imported and reviewed.
- Chat transcripts are provenance until converted into repo-grade text.
- Downstream Clay-program claims do not promote upstream framework objects.
- Fixture success does not imply theorem progress.
- Structural analogy does not imply proof transfer.
