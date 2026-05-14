# Audit Scope Maintenance Policy

## Purpose

The legacy topology audit scanner (`scripts/audit_legacy_topology_terms.py`) scans a fixed set of file classes. The scanner result is meaningful only when the declared file classes cover the full active theorem, proof, and computation surface.

A result such as:

```text
No scoped hits found.
```

means only that no forbidden terminology was found inside the currently declared audit scope. It does not prove anything about files outside that scope.

## Maintenance rule

When any of the following events occur, the scanner scope must be reviewed in the same PR:

- a new Python file is added under `src/heller_godel/`;
- a new active manuscript Markdown file is added under `docs/manuscripts/`;
- a new proof appendix or proof skeleton Markdown file is added under `docs/appendices/` or `docs/proofs/`;
- a new gate, minimality, or theorem-condition document is added under `docs/gates/`;
- a formerly historical, context, or legacy manuscript file is promoted to active theorem-core status.

If the new file is active theorem-core, add it to the `theorem-core` `FILE_CLASSES` patterns in `scripts/audit_legacy_topology_terms.py`.

If the new file is not active theorem-core, either ensure it is covered by an appropriate non-core class or add a narrow documented exemption.

## Enforcement

The CI workflow `.github/workflows/legacy-topology-audit.yml` runs:

```bash
python scripts/audit_legacy_topology_terms.py \
  --output docs/review-ledgers/HG_LEGACY_TOPOLOGY_TERMS_AUDIT_LOCAL.md \
  --fail-on-core \
  --fail-on-scope-drift
```

`--fail-on-scope-drift` checks broad theorem-surface candidate globs against the scanner's declared classes. If a candidate file is not covered and is not explicitly exempted, CI fails with a message pointing back to this policy.

## Authoritative configuration

The authoritative configuration lives in `scripts/audit_legacy_topology_terms.py`:

- `FILE_CLASSES` defines the scanned classes.
- `THEOREM_SURFACE_CANDIDATE_GLOBS` defines broad discovery patterns for likely theorem/proof files.
- `SCOPE_DRIFT_EXEMPT_GLOBS` defines explicit non-core exemptions.

Do not update this policy without checking that the script and CI workflow remain consistent.

## Current theorem-core class

As of this policy revision, theorem-core consists of:

```text
docs/manuscripts/paper_i_*.md
docs/appendices/**/*.md
docs/proofs/**/*.md
docs/gates/**/*.md
src/heller_godel/*.py
```

This set is intentionally narrower than all documentation, but it covers the active theorem/proof/computation surface for the legacy topology terminology audit.

## Current explicit non-core exemptions

The scope-drift checker exempts:

```text
docs/manuscripts/calculus_invariant_characters_*.md
docs/manuscripts/*patch_plan*.md
docs/review-ledgers/**/*.md
docs/governance/**/*.md
```

These paths are not treated as active theorem-core for this audit. If any exempted file is promoted to active theorem-core status, remove or narrow the exemption in the same PR.

## Failure interpretation

A scope-drift failure means one of three things:

1. A new active theorem-core file was added and the scanner scope must be extended.
2. A file matched a broad candidate pattern but is actually non-core and needs a documented exemption.
3. The candidate glob is too broad and should be narrowed with care.

Do not bypass a scope-drift failure by weakening the scanner without recording the reason in the PR.
