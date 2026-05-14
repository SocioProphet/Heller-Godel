# CI Gate Registry

## Purpose

This registry classifies the repository's CI checks so future PR authors can distinguish hard merge blockers from soft audit signals and artifact-only observers.

The classification is based on the workflow files currently present under `.github/workflows/` on `main`.

## Classification schema

| Classification | Meaning |
| --- | --- |
| `hard-blocker` | A failing step or reusable workflow failure should block merge until fixed. |
| `soft-signal` | A failing step is intentionally non-blocking, but the output must be reviewed because it indicates audit drift, baseline divergence, or follow-up work. |
| `artifact-observer` | The step exists primarily to publish a report, receipt, or artifact. It should normally run even when earlier checks fail. |
| `operational-prerequisite` | A setup, checkout, dependency-install, or infrastructure step required for a gate to run. If it fails, treat it as hard-blocking until proven transient. |

## Workflow inventory

### `.github/workflows/validate.yml`

Workflow name: `validate`

Job id: `tests`

Triggers:

```text
push to main
pull_request to main
```

| Gate | Job / step | Classification | Failure meaning | Remediation |
| --- | --- | --- | --- | --- |
| Checkout | `tests` / `Checkout` | `operational-prerequisite` | Repository checkout failed; downstream gates cannot be trusted. | Treat as hard-blocking infrastructure failure until proven transient. |
| Set up Python | `tests` / `Set up Python` | `operational-prerequisite` | Python runtime setup failed; downstream Python gates cannot run. | Fix workflow/runtime configuration or retry only if runner failure is clearly transient. |
| Install package and test runner | `tests` / `Install package and test runner` | `operational-prerequisite` | Package installation or test dependency setup failed. | Fix packaging, dependency metadata, or runner environment before merge. |
| Python test suite | `tests` / `Run tests` / `pytest -q` | `hard-blocker` | Executable package behavior is broken or tests are inconsistent with the current code. | Fix the code, tests, or documented executable boundary before merge. |
| Claim-boundary guard | `tests` / `Run claim-boundary guard` / `python scripts/check_claim_boundaries.py` | `hard-blocker` | Manuscript or repository claims violate the bounded nonclaim/claim-scope policy. | Narrow the claim, add an explicit nonclaim, or update the guard only with a documented governance reason. |
| CI gate registry coverage | `tests` / `Run CI gate registry coverage check` / `python scripts/check_ci_gate_registry.py` | `hard-blocker` | A workflow file under `.github/workflows/` is not represented in this registry by filename, path, workflow name, job id, named step, and reusable workflow reference. | Update this registry in the same PR that adds, removes, renames, or materially changes workflow semantics. |

Notes:

- Dependency installation and checkout/setup steps are operational prerequisites for the hard-blocking gates.
- If setup fails because of environment drift, treat it as a hard-blocking infrastructure failure until proven transient.
- The registry coverage gate prevents this document from becoming a stale point-in-time snapshot.

### `.github/workflows/proof-apparatus-continuous-validation.yml`

Workflow name: `Proof apparatus continuous validation`

Job id: `validate-with-sociosphere`

Triggers:

```text
workflow_dispatch
push touching any path
pull_request touching any path
```

| Gate | Job / step | Classification | Failure meaning | Remediation |
| --- | --- | --- | --- | --- |
| Proof apparatus reusable validation | `validate-with-sociosphere` / `SocioProphet/sociosphere/.github/workflows/proof-apparatus.yml@main` | `hard-blocker` | The domain repository failed the shared proof-apparatus validation contract. | Inspect the reusable workflow logs, determine whether the failure is in this repo or the shared workflow contract, and patch before merge. |

Notes:

- This gate delegates to SocioProphet/sociosphere and should be treated as part of the repo's proof-governance contract.
- Because it runs on all paths, it is the broadest continuous validation gate in this repo.
- Step-level classification for the reusable workflow lives in the SocioSphere controller repository. This registry tracks the local reusable workflow call by job id and reusable workflow reference.

### `.github/workflows/legacy-topology-audit.yml`

Workflow name: `legacy-topology-audit`

Job id: `audit`

Triggers:

```text
pull_request touching docs/**, src/heller_godel/**, scripts/audit_legacy_topology_terms.py, or the workflow itself
push to main touching the same paths
workflow_dispatch
```

| Gate | Job / step | Classification | Failure meaning | Remediation |
| --- | --- | --- | --- | --- |
| Check out repository | `audit` / `Check out repository` | `operational-prerequisite` | Repository checkout failed; audit output cannot be trusted. | Treat as hard-blocking infrastructure failure until proven transient. |
| Set up Python | `audit` / `Set up Python` | `operational-prerequisite` | Python runtime setup failed; audit scripts cannot run. | Fix workflow/runtime configuration or retry only if runner failure is clearly transient. |
| Legacy topology forbidden-term audit | `audit` / `Run scoped legacy topology audit` / `--fail-on-core` | `hard-blocker` | A theorem-core file contains forbidden scoped topology/path terminology. | Patch the theorem-core language or add a narrow inline exemption with mathematical justification. |
| Legacy topology scope-drift audit | `audit` / `Run scoped legacy topology audit` / `--fail-on-scope-drift` | `hard-blocker` | A theorem-surface candidate file is not covered by the scanner's declared classes. | Add the file/path to `FILE_CLASSES` or add a documented exemption. See `docs/governance/audit_scope_maintenance.md`. |
| Local audit report printout | `audit` / `Print local audit report` | `artifact-observer` | The local scanner output is not visible in logs. | Restore the print step; do not rely only on downloadable artifacts for audit review. |
| Frozen-ledger comparison | `audit` / `Compare local audit against frozen connector-backed ledger` / `--diff-against-frozen` | `soft-signal` | The local scanner output diverges from the marked authoritative payload in the frozen ledger. This step uses `continue-on-error: true`; divergence is visible but non-blocking. | Open a ledger correction PR before terminology remediation. Do not edit theorem text until the ledger state is reconciled. |
| Local audit artifact upload | `audit` / `Upload local audit report` | `artifact-observer` | The local report artifact was not uploaded. | Restore artifact upload so reviewers can inspect machine output outside logs. |

Soft-signal policy for `--diff-against-frozen`:

```text
signal_consumer: maintainer review on each PR that triggers legacy-topology-audit
promotion_condition: diff persists across 2+ PRs without documented justification
output_location: docs/review-ledgers/HG_LEGACY_TOPOLOGY_TERMS_AUDIT_LOCAL.md and the legacy-topology-audit job logs/artifact
```

Notes:

- The hard blockers are `--fail-on-core` and `--fail-on-scope-drift`.
- The frozen-ledger comparison is intentionally non-blocking because the ledger may contain historical connector-backed context outside the marked authoritative payload.
- The artifact and printout steps preserve audit observability; they are not substitute hard blockers.

## Current hard-blocker set

As of this registry revision, the hard blockers are:

```text
validate / pytest -q
validate / scripts/check_claim_boundaries.py
validate / scripts/check_ci_gate_registry.py
Proof apparatus continuous validation / reusable proof-apparatus workflow
legacy-topology-audit / --fail-on-core
legacy-topology-audit / --fail-on-scope-drift
```

## Current soft-signal set

```text
legacy-topology-audit / --diff-against-frozen
```

## Current artifact-observer set

```text
legacy-topology-audit / Print local audit report
legacy-topology-audit / Upload local audit report
```

## Current operational-prerequisite set

```text
validate / Checkout
validate / Set up Python
validate / Install package and test runner
legacy-topology-audit / Check out repository
legacy-topology-audit / Set up Python
```

## Maintenance policy

When adding, deleting, or materially changing a workflow file under `.github/workflows/`, update this registry in the same PR.

When adding, deleting, or renaming a job id or named step, update this registry in the same PR.

When changing a step from blocking to non-blocking with `continue-on-error: true`, add or update its row here and explain why the failure is a soft signal instead of a hard blocker.

When adding an artifact-producing step, state whether the artifact is evidence for a hard blocker, a soft signal, or a standalone observer.

Do not leave CI semantics implicit. A reviewer should be able to read this file and know what every gate means before inspecting workflow logs.
