# Proof Fabric Kernel Extraction Control

Status: source-supplied extraction control.  
Claim level: governance / architecture.  
Mathematical content added by this document: none.  
Controlling Heller-Godel framework-core bootstrap commit: `757070c582858f32473cfc0ac5d32f5c4558cf40`.

## Purpose

This document controls the next architecture move after the Heller-Godel framework-core declaration: extracting or creating `SocioProphet/proof-fabric-kernel` as the shared operational substrate for schemas, validators, receipts, Event-IR, proof artifacts, claim ledgers, and citation checks.

## Corrected source-location finding

PFK source content was not found in Drive source form and was not present on `SocioProphet/Heller-Winters-Theorem/main` under `proof_fabric_kernel/` during the GitHub audit.

A user-supplied archive has now provided the missing source tree:

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

The correct extraction mode is now:

```text
source-supplied extraction
```

not reconstruction.

The PFK target repository should receive the extracted `proof_fabric_kernel/` tree byte-for-byte, preserving the file hashes recorded in the manifest.

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

## Blocker

The current GitHub connector can create branches, files, issues, and PRs in existing repositories, but it does not expose repository creation.

Because `SocioProphet/proof-fabric-kernel` does not yet exist, the bootstrap PR cannot be opened directly through this connector session.

## PFK repository bootstrap target

Target repository:

```text
SocioProphet/proof-fabric-kernel
```

Target description:

```text
Shared proof-fabric operational substrate for the SocioProphet Clay-program estate: schemas, validators, Event-IR, ProofArtifact mappings, claim-ledger rows, receipts, examples, and citation checks.
```

Target visibility: public.

Target license: MIT unless repository policy requires otherwise.

Target topic suggestions:

```text
proof-fabric
schema-validation
event-ir
claim-ledger
provenance
socioprophet
heller-godel
```

## PFK namespace

PFK should use a separate namespace from Heller-Godel framework identifiers:

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

## PFK PR sequence

### PR #1 — identity and source import

Because the source archive is now supplied and validated, the first PFK PR may include both identity files and the byte-preserving source tree import.

Required files:

```text
README.md
LICENSE
CITATION.cff
CONTRIBUTING.md
.gitignore
DEPENDENCIES.md
proof_fabric_kernel/README.md
proof_fabric_kernel/schemas/*
proof_fabric_kernel/docs/*
proof_fabric_kernel/tools/*
proof_fabric_kernel/examples/*
docs/source-audit/pfk-source-archive-manifest.md
```

The PR body must state:

```text
This is source-supplied extraction from Heller-Winters-Theorem-main_PFK 2.zip, not reconstruction.
```

### PR #2 — normalization / packaging

Only after PR #1 lands:

- decide whether to keep nested `proof_fabric_kernel/` or flatten to repo root;
- add package metadata if desired;
- add CI workflow for validators;
- add schema validation matrix;
- add manifest regeneration command.

### PR #3 — consumer integration

- update `SocioProphet/Heller-Winters-Theorem#28` to point at the PFK repo and schema paths;
- update Candidate C receipts to native Event-IR / ProofArtifact-compatible output;
- add downstream `DEPENDENCIES.md` declarations in Clay-program repos.

## Heller-Winters issue linkage

Current Heller-Winters issue:

```text
SocioProphet/Heller-Winters-Theorem#28 — Candidate C: native PFK Event-IR integration
```

That issue should not be closed by PFK repository bootstrap alone. It closes only when Candidate C receipts emit native Event-IR / ProofArtifact-compatible output under a PFK schema.

## Non-claim boundary

This extraction control does not promote PFK schemas to mathematical theorem status. It records operational source provenance and migration policy only.

## Acceptance criteria for resolving this control artifact

This artifact is resolved when:

1. `SocioProphet/proof-fabric-kernel` exists;
2. the supplied archive manifest is copied into the new repo;
3. the extracted source tree is imported byte-for-byte;
4. PFK validation CI runs in the new repo;
5. Heller-Winters issue #28 is updated to point at the PFK repo and active schema paths.
