# Framework-Core Dependency Graph

Status: bootstrap declaration.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This document declares the intended dependency direction for the Heller-Godel / Clay-program estate.

## Core rule

`SocioProphet/Heller-Godel` is the framework-core repository.

It is not downstream of any Clay-program repository.

Downstream Clay-program repositories may cite Heller-Godel framework objects by stable `HG-*` identifier and merged commit SHA.

## Directed graph

```text
SocioProphet/Heller-Godel
  framework vocabulary, claim grammar, anti-seed doctrine, canonical fixtures

  ├──> SocioProphet/proof-fabric-kernel        [planned / extraction target]
  │       schemas, validators, Event IR, claim ledgers, receipts, CI helpers
  │
  │       ├──> SocioProphet/Heller-Winters-Theorem
  │       ├──> SocioProphet/yang-mills
  │       ├──> SocioProphet/hodge-program-proof
  │       ├──> SocioProphet/np-program
  │       ├──> SocioProphet/bsd-proof-program
  │       ├──> SocioProphet/Heller-Dirac          [purpose declaration pending]
  │       └──> SocioProphet/navier-stokes-program [commission decision pending]
  │
  └──> direct citation by Clay-program repositories
```

## Forbidden edges

The following edges are forbidden unless a later governance PR explicitly changes this policy:

- Clay-program repository -> modifies Heller-Godel framework objects without a Heller-Godel PR;
- Heller-Godel -> depends on a Clay-program repository as a mathematical premise;
- proof-fabric-kernel -> depends on a Clay-program repository;
- cyclic dependencies of any length;
- Drive source -> canonical citation after a reviewed repo import exists.

## Dependency classes

| Class | Meaning | Canonical location |
| --- | --- | --- |
| Framework vocabulary | mathematical vocabulary, anti-seed doctrine, distance tiers, canonical fixtures | `SocioProphet/Heller-Godel` |
| Operational substrate | schemas, validators, Event IR, receipts, CI helpers | `SocioProphet/proof-fabric-kernel` planned |
| Clay-program instantiation | problem-specific workstreams, theorem attempts, manuscripts, evidence ledgers | Clay-program repos |
| Provenance | Drive originals, source captures, historical drafts | imported source/provenance directories after review |

## Consumer inventory

| Repository | Intended relationship | Bootstrap status |
| --- | --- | --- |
| `SocioProphet/Heller-Winters-Theorem` | RH / GRH program; should cite Heller-Godel framework and consume PFK once extracted | dependency declaration pending |
| `SocioProphet/yang-mills` | Yang-Mills program; should cite framework vocabulary only where directly used | dependency declaration pending |
| `SocioProphet/hodge-program-proof` | Hodge program; should cite framework methods/fixtures with strict distance caps | dependency declaration pending |
| `SocioProphet/np-program` | P vs NP program; should cite Catalan / mu_2 and claim grammar with fixture-grade caps | dependency declaration pending |
| `SocioProphet/bsd-proof-program` | BSD program; should import its own spec and then declare framework/PFK dependencies | spec import pending |
| `SocioProphet/hphd-zeta-mirror-lattice` | RH sub-lane; recommended absorption into Heller-Winters under `lanes/hphd/` | absorption pending |
| `SocioProphet/Heller-Dirac` | purpose unresolved; recommended index-theory bridge | purpose declaration pending |
| `SocioProphet/navier-stokes-program` | not yet commissioned | decision pending |

## PFK extraction policy

The current portfolio review identifies proof-fabric-kernel as shared infrastructure that should not remain siloed inside a single Clay-program repo.

PFK extraction should be handled as a separate repository or clearly declared shared package. Its role is operational, not foundational:

```text
Heller-Godel: framework vocabulary and claim grammar
PFK: schemas, validators, receipts, and machine-checking substrate
Clay repos: problem-specific instantiations
```

Heller-Godel may declare the PFK dependency architecture but should not vendor validator code unless the code belongs to the active Paper I stack.

## Citation direction

Citations flow downstream:

```text
Clay repo -> HG identifier @ merged SHA
```

Inventory references flow upstream only as non-load-bearing consumer listings in this document.

## Maintenance rule

When a downstream repo adds or removes a Heller-Godel dependency, update this document or add a companion dependency-declaration PR here.
