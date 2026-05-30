# Heller-Godel Framework Core

Status: bootstrap declaration.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This directory declares the existing `SocioProphet/Heller-Godel` repository as the canonical framework-core repository for the Heller-Godel / Clay-program estate.

This is not a new repository. The earlier proposed `heller-godel-core` repository is superseded by this declaration. Framework-core material belongs here unless a later governance PR explicitly moves it.

## Relationship to the existing active core

The repository already contains an active, defensible Paper I core around proof-class generating functions, Puiseux singular data, finite phase characters, Deligne units, carry defects, and regulator-symbol separation.

The framework-core layer does not erase or supersede that active core. It wraps it in a portfolio-level governance structure so downstream Clay-program repositories can cite Heller-Godel framework objects without treating exploratory or Drive-only material as theorem-grade infrastructure.

Current repo-supported active core remains:

```text
restricted proof grammar + fixed canonical statistic
-> proof-class / proof-family generating function
-> Puiseux singularity data
-> finite phase reductions chi_p and chi_13
-> explicit mod-p carry defect zeta_p under composition
```

and, in the Paper I rewrite:

```text
proof-class generating function
-> decorated Puiseux singular datum at a chosen puncture
-> branch-killing cyclic cover
-> Puiseux singular unit upstairs
-> level-1 Deligne unit
-> finite monodromy / deck character downstairs
-> lifted phase index
-> section-defect carry cocycle
```

The carry cocycle and Deligne cup-product/regulator symbol remain intentionally distinct.

## What belongs in this framework-core layer

This layer is for:

- stable framework identifiers;
- distance classification;
- anti-seed entries and failure-mode registers;
- downstream citation grammar;
- dependency graph declarations;
- canonical fixtures such as Catalan / mu_2;
- normalized imports of foundational Drive material after review;
- claim-bounded framework vocabularies such as boundary/spectral grammar.

## What does not belong here

This layer is not a Clay-proof venue. It does not claim proof of RH, GRH, Hodge, BSD, P vs NP, Yang-Mills mass gap, or Navier-Stokes.

This layer is not a proof-transfer theorem between Clay domains. Universal Bridge material, when imported, is methodology and structural analogy unless separately proved otherwise.

This layer is not a product-plane standardization venue. Framework vocabularies may inform later systems, but they do not become SocioProphet platform substrate without separate authority, extraction, and claim-boundary review.

## Bootstrap file set

This declaration is implemented by:

- `docs/framework-core/distance-classification.md`
- `docs/framework-core/claim-grammar.md`
- `docs/framework-core/anti-seed-framework.md`
- `docs/framework-core/dependency-graph.md`
- `docs/framework-core/boundary-spectral-grammar-v0.md`
- `docs/doctrine/catalan-mu2-canonical-reference.md`
- `examples/catalan-mu2/README.md`
- `DEPENDENCIES.md`

Operational substrate note: PFK now lives in-repo under `proof_fabric_kernel/`. See `docs/framework-core/proof-fabric-kernel-extraction-control.md` and `proof_fabric_kernel/docs/ClayProgram_PFK_ConsumerContract_v0.md`.

## Immediate import sequence

The next content PRs should be ordered as follows:

1. Normalize the already-active Paper I / proof-character core into the `HG-FND-*`, `HG-VOC-*`, and `HG-EX-*` identifier registry.
2. Import foundational Drive materials as provenance-preserving source captures, then promote only reviewed objects into the active registry.
3. Import Universal Bridge material as `methodology / structural analogy`, not proof equivalence.
4. Import lattice tower and Rosetta material as vocabulary, with explicit distance caps.
5. Keep PFK as the Heller-Godel in-repo operational substrate for Clay-program schema, Event-IR, ProofArtifact, receipts, and validator surfaces.

## Governing rule

No object is framework-foundational merely because it exists in a Drive source, prior draft, chat transcript, or downstream Clay repository.

Framework-foundational status requires an explicit registered identifier, a typed statement, a proof or accepted citation, an anti-seed entry, and a merged PR declaring the distance tier.
