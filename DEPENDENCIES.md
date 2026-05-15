# Dependency Declaration

Status: live declaration.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This document records the dependency role of `SocioProphet/Heller-Godel` in the Heller-Godel / Clay-program estate.

## Repository role

`SocioProphet/Heller-Godel` is the framework-core repository and the Proof Fabric Kernel host.

It owns:

- active proof-character / phase-character core material already in this repo;
- framework identifiers and citation grammar;
- framework anti-seed doctrine;
- framework distance classification;
- canonical apparatus fixtures such as Catalan / mu_2;
- Proof Fabric Kernel source under `proof_fabric_kernel/` once imported;
- normalized source imports after review.

It does not own:

- problem-specific Clay-program proof claims;
- downstream repo evidence ledgers except by citation or inventory;
- theorem promotion from PFK schema or fixture validation.

## Upstream dependencies

None declared at this bootstrap layer.

Drive sources and historical drafts are provenance inputs, not active upstream dependencies until imported and normalized.

## In-repo operational substrate

| Path | Relationship | Status |
| --- | --- | --- |
| `proof_fabric_kernel/` | in-repo operational substrate for schemas, validators, receipts, Event-IR, ProofArtifact mappings, calibration bundles, claim-ledger rows, examples, and proof-fabric validation helpers | source-supplied import pending |

PFK uses the separate `PFK-*` namespace for operational artifacts. Heller-Godel framework vocabulary uses `HG-*`.

## Downstream consumers

| Repository | Intended use of Heller-Godel | Status |
| --- | --- | --- |
| `SocioProphet/Heller-Winters-Theorem` | RH / GRH program citation of framework vocabulary and proof-fabric discipline | dependency declaration pending |
| `SocioProphet/yang-mills` | narrowly scoped Yang-Mills program citation of relevant framework vocabulary only | dependency declaration pending |
| `SocioProphet/hodge-program-proof` | Hodge method-lane citation of framework methods, fixtures, and anti-seed doctrine | dependency declaration pending |
| `SocioProphet/np-program` | P vs NP program citation of Catalan / mu_2 fixture and claim grammar | dependency declaration pending |
| `SocioProphet/bsd-proof-program` | BSD program citation after spec import | dependency declaration pending |
| `SocioProphet/Heller-Dirac` | purpose unresolved; recommended index-theory bridge | purpose declaration pending |
| `SocioProphet/hphd-zeta-mirror-lattice` | recommended absorption into Heller-Winters as RH sub-lane | absorption pending |

## Citation requirement for consumers

Consumers must cite Heller-Godel objects by:

```text
HG-{LAYER}-{NNN} @ <merged-main-sha>
```

and must declare citation grade:

```text
theorem-grade | method-grade | fixture-grade | provenance-grade
```

PFK operational objects use:

```text
PFK-{LAYER}-{NNN} @ <merged-main-sha>
```

when a PFK identifier registry exists. Until then, cite exact paths and merged commit SHAs.

## No-cycle rule

No dependency cycle is permitted between Heller-Godel and Clay-program repos.

Downstream consumers may cite Heller-Godel. They may not silently promote or modify framework objects outside a Heller-Godel PR.