# Clay Program PFK Consumer Contract v0

Identifier: `PFK-DOC-CONSUMER-CONTRACT-001 v0.1`  
Status: Draft  
Claim level: operational substrate / governance; no mathematical claim promotion  
Authority repo: `SocioProphet/Heller-Godel`  
Authority path: `proof_fabric_kernel/`

## Purpose

This document defines how Clay/math research repositories consume the Proof Fabric Kernel (PFK) that lives inside `SocioProphet/Heller-Godel`.

PFK is research infrastructure for the Clay/math program estate. It is not standard SocioProphet product infrastructure, and this contract does not authorize general platform, agent, workroom, fraud, SCOPE-D, or Ontogenesis runtime use.

The purpose is narrower: give Clay/math repositories a common operational substrate for claim-ledger rows, Event-IR traces, ProofArtifact envelopes, calibration bundles, validators, receipts, anti-seed discipline, and dependency pins without treating those operational artifacts as theorem evidence.

## Scope

This contract applies to Clay/math research consumers, including but not limited to:

- `SocioProphet/Heller-Winters-Theorem`
- `SocioProphet/yang-mills`
- `SocioProphet/bsd-proof-program`
- `SocioProphet/hodge-program-proof`
- `SocioProphet/hphd-zeta-mirror-lattice`
- `SocioProphet/np-program`
- `SocioProphet/Heller-Dirac`, if it is used as an index-theory or Dirac-operator bridge

This contract does not make PFK a general SocioProphet standard. A later generalized artifact/governance fabric may borrow lessons from PFK, but that would be a separate extraction with separate authority and claim boundaries.

## Authority decision

PFK lives in:

```text
SocioProphet/Heller-Godel/proof_fabric_kernel/
```

Consumer repositories must not create local forks of the kernel schema family unless they are explicitly recording a compatibility fixture or migration test. The kernel authority surface remains Heller-Godel.

There is no active architecture requirement for a standalone `SocioProphet/proof-fabric-kernel` repository.

## Dependency rule

Consumers must pin to a merged Heller-Godel commit SHA.

Preferred dependency declaration form:

```text
PFK authority: SocioProphet/Heller-Godel/proof_fabric_kernel @ <merged-Heller-Godel-commit-sha>
```

Consumers must not silently consume floating `main`.

A consumer re-pin across PFK major schema versions requires a migration PR that re-validates all consumer-side PFK-compatible receipts and examples.

## Canonical schema surfaces

Consumers should cite schemas using the identifiers in `proof_fabric_kernel/docs/SchemaCatalog_v1.md`.

Current canonical surfaces are:

| Identifier | Path | Consumer use |
| --- | --- | --- |
| `PFK-SCHEMA-001` | `proof_fabric_kernel/schemas/claim_ledger_row.schema.json` | Claim-ledger row envelope for Clay-program claims. |
| `PFK-SCHEMA-002` | `proof_fabric_kernel/schemas/event_ir.schema.json` | Event-IR trace recording operator invocation or structured computation event. |
| `PFK-SCHEMA-003` | `proof_fabric_kernel/schemas/proof_artifact.schema.json` | ProofArtifact envelope for proof-step or computation-step artifacts. |
| `PFK-SCHEMA-004` | `proof_fabric_kernel/schemas/calibration_bundle.schema.json` | Calibration-run artifact envelope for numerical baseline and sanity-check outputs. |

Schema validity is envelope validity, not content validity.

## Common IR interpretation

The recovered generic IR family is a consumer-facing interpretation layer over PFK, not a replacement for PFK.

| Generic IR name | PFK interpretation |
| --- | --- |
| `ClaimIR` | Claim-ledger row surface under `PFK-SCHEMA-001`; claim grade, distance tier, citation pins, and review status remain consumer responsibilities. |
| `ObjectIR` | ProofArtifact domain-object references and artifact envelopes under `PFK-SCHEMA-003`. |
| `ContextIR` | Event scope, ProofArtifact metadata, dependency pins, framework-citation pins, and consumer repo context. |
| `EvidenceIR` | Evidence references inside Event-IR and ProofArtifact envelopes; never proof by itself. |
| `MorphismIR` | Operator invocation, transformation trace, or computation-step transition recorded through Event-IR and/or ProofArtifact. |
| `ObligationIR` | Consumer-side review obligations, claim-ledger duties, migration checks, and anti-seed compliance; not yet a separate PFK schema unless later added. |
| `VerifierIR` | Validator/tooling objects, schema validators, hash manifests, CI gates, and replay/check scripts. |
| `ReceiptIR` | Event-IR traces, ProofArtifact envelopes, calibration bundles, and receipt-compatible consumer outputs. |
| `LedgerIR` | Claim-ledger rows plus consumer-side dependency declarations and pinned receipt ledgers. |

These names may be useful for cross-repo discussion, but PFK schema identifiers and pinned paths remain canonical.

## Required consumer behavior

A Clay/math consumer repo using PFK should:

1. declare the pinned Heller-Godel commit SHA in a dependency file or equivalent authority artifact;
2. identify which PFK schemas it consumes;
3. validate PFK-shaped examples or receipts in CI when the repo claims compatibility;
4. preserve anti-seed boundaries from `proof_fabric_kernel/docs/anti-seed-pfk.md`;
5. avoid treating schema validity, validator green status, Event-IR traces, ProofArtifact envelopes, or calibration bundles as theorem-grade evidence;
6. keep mathematical interpretation inside the consumer repo's own claim discipline;
7. record migrations when PFK schema versions change.

## Non-promotion rules

The following inferences are forbidden:

- Event-IR trace exists, therefore the mathematical claim is supported.
- ProofArtifact validates, therefore the proof step is correct.
- Claim-ledger row validates, therefore the claim is true.
- Calibration bundle validates, therefore the numerical behavior is theorem evidence.
- CI is green, therefore audit is complete.
- PFK compatibility exists, therefore Clay proximity improved.

Correct interpretation:

PFK artifacts can make computation, claims, artifacts, and receipts more structured and auditable. They do not supply mathematical correctness by themselves.

## Consumer maturity levels

### M0: Citation-only dependency

The consumer cites PFK as an intended substrate but does not yet emit PFK-shaped artifacts.

Allowed statement: compatibility target identified.

Forbidden statement: native PFK integration complete.

### M1: Pinned schema dependency

The consumer declares a Heller-Godel commit SHA and lists consumed schema identifiers.

Allowed statement: dependency pinned.

Forbidden statement: receipts are PFK-native unless examples validate.

### M2: Example compatibility

The consumer provides examples that validate against one or more PFK schemas.

Allowed statement: example-level compatibility.

Forbidden statement: full pipeline integration.

### M3: Native receipt emission

The consumer emits Event-IR / ProofArtifact / claim-ledger / calibration-bundle outputs as part of its normal workflow.

Allowed statement: native PFK-compatible receipt emission.

Forbidden statement: theorem-grade evidence.

### M4: Migration-disciplined consumer

The consumer has dependency pinning, CI validation, migration notes, anti-seed compliance, and replay/revalidation behavior.

Allowed statement: mature PFK consumer.

Forbidden statement: PFK validates mathematical correctness.

## Relationship to Heller-Winters Candidate C

Heller-Winters issue `SocioProphet/Heller-Winters-Theorem#28` should not be closed by the existence of PFK in Heller-Godel alone.

It closes only when Candidate C receipts emit native Event-IR / ProofArtifact-compatible output under pinned PFK schemas and the consumer repo declares the Heller-Godel dependency pin.

## Relationship to broader SocioProphet systems

PFK is not currently a general product-plane dependency.

Ontogenesis, Prophet Platform, AgentPlane, SCOPE-D, fraud intelligence, workrooms, and general SocioProphet governance may borrow design principles later, especially:

- schema validity is not content validity;
- receipts are not proof;
- validators are preconditions for audit, not audit completion;
- dependency pins outrank floating `main`;
- anti-seed registers prevent overclaiming.

Borrowing those principles does not make those systems PFK consumers.

## Acceptance criteria for a consumer repo

A consumer repo should be considered PFK-aligned only when it has:

1. a dependency pin to Heller-Godel PFK;
2. consumed schema identifiers or paths;
3. examples or receipts validated against those schemas;
4. anti-seed acknowledgement;
5. CI or review gate for PFK-shaped artifacts;
6. explicit claim boundary saying PFK validation is not theorem evidence.

## Claim boundary

This contract does not add mathematical content. It does not assert theorem progress for any Clay-program target. It does not require all Clay repos to adopt PFK immediately. It defines how adoption must happen when a repo claims PFK compatibility.
