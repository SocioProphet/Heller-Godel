# Dependency Declaration

Status: bootstrap declaration.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.

This document records the dependency role of `SocioProphet/Heller-Godel` in the Heller-Godel / Clay-program estate.

## Repository role

`SocioProphet/Heller-Godel` is the framework-core repository.

It owns:

- active proof-character / phase-character core material already in this repo;
- framework identifiers and citation grammar;
- framework anti-seed doctrine;
- framework distance classification;
- canonical apparatus fixtures such as Catalan / mu_2;
- normalized source imports after review.

It does not own:

- problem-specific Clay-program proof claims;
- shared validator/runtime infrastructure planned for `proof-fabric-kernel`;
- downstream repo evidence ledgers except by citation or inventory.

## Upstream dependencies

None declared at this bootstrap layer.

Drive sources and historical drafts are provenance inputs, not active upstream dependencies until imported and normalized.

## Planned peer / downstream infrastructure

| Repository | Relationship | Status |
| --- | --- | --- |
| `SocioProphet/proof-fabric-kernel` | planned operational substrate for schemas, validators, receipts, Event IR, and citation checks | extraction/bootstrap pending |

`proof-fabric-kernel` may depend on Heller-Godel framework identifiers and citation grammar. Heller-Godel should not depend on PFK for mathematical content.

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

## No-cycle rule

No dependency cycle is permitted between Heller-Godel, PFK, and Clay-program repos.

Downstream consumers may cite Heller-Godel. They may not silently promote or modify framework objects outside a Heller-Godel PR.
