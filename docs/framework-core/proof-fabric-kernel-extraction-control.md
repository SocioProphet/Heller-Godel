# Proof Fabric Kernel Extraction Control

Status: source-supplied in-repo import control.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.  
Controlling Heller-Godel framework-core bootstrap commit: `757070c582858f32473cfc0ac5d32f5c4558cf40`.

## Purpose

This document controls the import of Proof Fabric Kernel into `SocioProphet/Heller-Godel` as the in-repo operational substrate for schemas, validators, receipts, Event-IR, proof artifacts, claim ledgers, and citation checks.

## Corrected location decision

PFK goes in Heller-Godel.

The target location is:

```text
SocioProphet/Heller-Godel/proof_fabric_kernel/
```

There is no separate `SocioProphet/proof-fabric-kernel` repository in the active architecture.

## Corrected source-location finding

PFK source content was not found in Drive source form and was not present on `SocioProphet/Heller-Winters-Theorem/main` under `proof_fabric_kernel/` during the GitHub audit.

A user-supplied archive provided the missing source tree:

```text
Heller-Winters-Theorem-main_PFK 2.zip
```

The archive contains:

```text
Heller-Winters-Theorem-main/proof_fabric_kernel/
```

with 24 source files.

The archive and file-level hashes are recorded in:

```text
docs/framework-core/pfk-source-archive-manifest.md
```

## Current conclusion

The correct import mode is:

```text
source-supplied in-repo import
```

not reconstruction and not external-repo extraction.

The extracted `proof_fabric_kernel/` tree must be imported byte-for-byte into this repository, preserving the file hashes recorded in the manifest.

## GitHub audit performed before archive upload

The following checks were performed against `SocioProphet/Heller-Winters-Theorem` before the source archive was supplied:

| Check | Result |
| --- | --- |
| Repository existence / permissions | repo exists; admin/write access available |
| Direct path: `proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md` on `main` | not found |
| Direct path: `manuscript/proof_fabric_kernel/docs/OperatorCatalog_PrimePolicyOperators_v1.md` on `main` | not found |
| Commit search for `proof_fabric_kernel` | no commits returned |
| Branch search for `pfk` | no branches returned |
| PR search for PFK/Event-IR/ProofArtifact | returns PRs referencing PFK receipts / pending native integration, not a source tree |
| Issue #28 | open issue titled `Candidate C: native PFK Event-IR integration`; states current receipts are compatible with discipline but not native PFK/Event-IR |
| Review gap register G-08 | states `PFK was referenced but not integrated`; full PFK integration awaits native Event-IR / ProofArtifact integration |

This audit remains useful because it records why the archive must be treated as supplied source provenance rather than assumed current-main GitHub state.

## Supplied archive validation

Local validation against the extracted archive passed:

```text
JSON parse: OK for all `.json` schema and example files.
Event-IR validator: OK for primes, security safe/leak, and lawful-learning traces.
ProofArtifact validator: OK for primes, security safe/leak, and lawful-learning proof artifacts.
Calibration bundle schema validation: OK for examples/primes/calibration_bundle_example.json.
```

## PFK namespace

PFK uses a separate namespace from Heller-Godel framework identifiers:

```text
PFK-{LAYER}-{NNN}
```

Suggested layer codes:

| Layer | Meaning |
| --- | --- |
| `SCH` | JSON/YAML/schema object |
| `VAL` | validator/tooling object |
| `DOC` | governance / doctrine |
| `EX` | example / fixture |
| `REC` | receipt shape |
| `EVT` | Event-IR object |
| `ART` | ProofArtifact mapping |

This prevents collision with `HG-*`, which is reserved for Heller-Godel framework vocabulary and doctrine.

## In-repo import contents

The active import target is:

```text
proof_fabric_kernel/README.md
proof_fabric_kernel/schemas/*
proof_fabric_kernel/docs/*
proof_fabric_kernel/tools/*
proof_fabric_kernel/examples/*
tests/test_proof_fabric_kernel.py
```

## Consumer integration sequence

After this import lands:

1. Update `SocioProphet/Heller-Winters-Theorem#28` to point at Heller-Godel `proof_fabric_kernel/` schema paths.
2. Update Candidate C receipts to native Event-IR / ProofArtifact-compatible output.
3. Add downstream `DEPENDENCIES.md` declarations in Clay-program repos.
4. Close any superseded external-repo creation plan.

## Heller-Winters issue linkage

Current Heller-Winters issue:

```text
SocioProphet/Heller-Winters-Theorem#28 — Candidate C: native PFK Event-IR integration
```

That issue should not be closed by PFK import alone. It closes only when Candidate C receipts emit native Event-IR / ProofArtifact-compatible output under a PFK schema.

## Non-claim boundary

This extraction control does not promote PFK schemas to mathematical theorem status. It records operational source provenance and migration policy only.

## Acceptance criteria for resolving this control artifact

This artifact is resolved when:

1. `proof_fabric_kernel/` exists in Heller-Godel;
2. the supplied source tree is imported byte-for-byte;
3. PFK validation tests run in existing CI;
4. Heller-Winters issue #28 is updated to point at the active in-repo schema paths;
5. the old `SocioProphet/proof-fabric-kernel` creation plan is marked superseded.