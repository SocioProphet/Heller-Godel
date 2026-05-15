# PFK Schema Catalog v1

Identifier: `PFK-SCHEMA-CATALOG-001 v1.0`  
Status: Active  
Claim level: operational substrate; no mathematical claim promotion.  
Anti-seed: `A-PFK-SCHEMA-001`, `A-PFK-SCHEMA-002`

## Purpose

This catalog canonicalizes the four PFK schemas as stable identifiers, mapping each identifier to its canonical path in the Heller-Godel repository. Consumer-side citations using these identifiers can be resolved to the canonical schema file via a merged-commit-SHA pin.

## Canonical identifiers

### PFK-SCHEMA-001 — Claim Ledger Row Schema

Canonical path: `proof_fabric_kernel/schemas/claim_ledger_row.schema.json`

Purpose: schema for a single row in a Clay-program claim ledger.

The seed-tree schema is structural and permissive. Consumer-side discipline, including anti-seed citation, distance-tier declaration, framework-citation pinning, and claim-grade review, is enforced by consuming repos and their CI.

Primary anti-seed: `A-PFK-SCHEMA-001` — schema validity is not content validity.

### PFK-SCHEMA-002 — Event-IR Trace Schema

Canonical path: `proof_fabric_kernel/schemas/event_ir.schema.json`

Purpose: schema for a single Event-IR trace recording an operator invocation.

Required structural fields in the current seed tree: `id`, `kind`, `scope`, `time`, `props`. Additional properties are permitted.

### PFK-SCHEMA-003 — Proof Artifact Schema

Canonical path: `proof_fabric_kernel/schemas/proof_artifact.schema.json`

Purpose: schema for a single proof-step or computation-step artifact envelope.

### PFK-SCHEMA-004 — Calibration Bundle Schema

Canonical path: `proof_fabric_kernel/schemas/calibration_bundle.schema.json`

Purpose: schema for calibration-run artifacts, including numerical-baseline sanity checks.

## Citation form

Preferred identifier form:

```text
[PFK-SCHEMA-001 @ <merged-Heller-Godel-commit-sha>]
```

Path form is also accepted:

```text
[proof_fabric_kernel/schemas/claim_ledger_row.schema.json @ <merged-Heller-Godel-commit-sha>]
```

Identifier form is preferred for stability across future path reorganizations.

## Schema-version policy

Schema major-version changes are breaking by default. Schema minor changes are non-breaking additions, such as new optional fields. Schema patch changes are documentation-only.

Consumer-side `DEPENDENCIES.md` files pin to a specific Heller-Godel commit SHA. Re-pinning across a major version requires a migration PR that re-validates all consumer-side receipts against the new schemas.

Per `A-PFK-SCHEMA-002`, consumers must not silently consume the current `main` HEAD. They pin to a merged commit.
