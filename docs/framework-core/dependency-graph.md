# Framework-Core Dependency Graph

Status: live declaration.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This document declares the intended dependency direction for the Heller-Godel / Clay-program estate.

## Core rule

`SocioProphet/Heller-Godel` is the framework-core repository and proof-fabric host.

It is not downstream of any Clay-program repository.

Downstream Clay-program repositories may cite Heller-Godel framework objects by stable `HG-*` identifier and merged commit SHA. Downstream repositories may also consume PFK schemas, validators, and example patterns from `proof_fabric_kernel/` once imported.

## Directed graph

```text
SocioProphet/Heller-Godel
  framework vocabulary, claim grammar, anti-seed doctrine, canonical fixtures
  proof_fabric_kernel/ schemas, validators, Event-IR, ProofArtifact mappings, claim ledgers, receipts, examples

  ├──> SocioProphet/Heller-Winters-Theorem
  ├──> SocioProphet/yang-mills
  ├──> SocioProphet/hodge-program-proof
  ├──> SocioProphet/np-program
  ├──> SocioProphet/bsd-proof-program
  ├──> SocioProphet/Heller-Dirac          [purpose declaration pending]
  └──> SocioProphet/navier-stokes-program [commission decision pending]
```

## Forbidden edges

The following edges are forbidden unless a later governance PR explicitly changes this policy:

- Clay-program repository -> modifies Heller-Godel framework objects without a Heller-Godel PR;
- Heller-Godel -> depends on a Clay-program repository as a mathematical premise;
- PFK schemas or examples -> promote a mathematical theorem claim by validation alone;
- cyclic dependencies of any length;
- Drive source -> canonical citation after a reviewed repo import exists.

## Dependency classes

| Class | Meaning | Canonical location |
| --- | --- | --- |
| Framework vocabulary | mathematical vocabulary, anti-seed doctrine, distance tiers, canonical fixtures | `SocioProphet/Heller-Godel` |
| Operational substrate | schemas, validators, Event-IR, receipts, ProofArtifact mappings, claim ledgers, examples, CI helpers | `SocioProphet/Heller-Godel/proof_fabric_kernel/` |
| Clay-program instantiation | problem-specific workstreams, theorem attempts, manuscripts, evidence ledgers | Clay-program repos |
| Provenance | Drive originals, source captures, historical drafts, supplied archive hashes | imported source/provenance directories and framework-core manifests after review |

## Consumer inventory

| Repository | Intended relationship | Bootstrap status |
| --- | --- | --- |
| `SocioProphet/Heller-Winters-Theorem` | RH / GRH program; should cite Heller-Godel framework and consume PFK from `proof_fabric_kernel/` | dependency declaration pending |
| `SocioProphet/yang-mills` | Yang-Mills program; should cite framework vocabulary only where directly used | dependency declaration pending |
| `SocioProphet/hodge-program-proof` | Hodge program; should cite framework methods/fixtures with strict distance caps | dependency declaration pending |
| `SocioProphet/np-program` | P vs NP program; should cite Catalan / mu_2 and claim grammar with fixture-grade caps | dependency declaration pending |
| `SocioProphet/bsd-proof-program` | BSD program; should import its own spec and then declare framework/PFK dependencies | spec import pending |
| `SocioProphet/hphd-zeta-mirror-lattice` | RH sub-lane; recommended absorption into Heller-Winters under `lanes/hphd/` | absorption pending |
| `SocioProphet/Heller-Dirac` | purpose unresolved; recommended index-theory bridge | purpose declaration pending |
| `SocioProphet/navier-stokes-program` | not yet commissioned | decision pending |

## PFK location policy

PFK lives in this repository under:

```text
proof_fabric_kernel/
```

It is operational, not foundational:

```text
Heller-Godel framework layer: framework vocabulary and claim grammar
Heller-Godel PFK layer: schemas, validators, receipts, and machine-checking substrate
Clay repos: problem-specific instantiations
```

PFK may be consumed by downstream repos, but PFK validation does not promote downstream theorem status.

## Citation direction

Citations flow downstream:

```text
Clay repo -> HG identifier @ merged SHA
Clay repo -> proof_fabric_kernel path or PFK identifier @ merged SHA
```

Inventory references flow upstream only as non-load-bearing consumer listings in this document.

## Maintenance rule

When a downstream repo adds or removes a Heller-Godel dependency, update this document or add a companion dependency-declaration PR here.