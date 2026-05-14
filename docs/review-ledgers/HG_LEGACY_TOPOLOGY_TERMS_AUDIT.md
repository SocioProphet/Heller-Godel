# HG Legacy Topology Terms Audit

Status: pre-patch audit artifact.  
Branch: `hg-legacy-terms-audit`.  
Base checked: `main` at `426b1ae3c8f5fbdc407906bc05495c7b3b650dd2`.  
Generated from connector-backed repository search plus targeted file reads because the ChatGPT sandbox could not clone GitHub directly during this pass. The committed script `scripts/audit_legacy_topology_terms.py` is the authoritative scanner for local or CI re-run.

## Purpose

This audit separates terminology review from remediation. No theorem-core text is patched in this branch. Follow-on PRs should remediate by file class after reviewing this report and the script output.

The motivating discipline is:

```text
audit first -> freeze findings -> patch by file class -> preserve historical/source-capture record
```

## Scope classes

### theorem-core

Paths:

```text
docs/manuscripts/paper_i_*.md
docs/appendices/appendix_a_*.md
docs/gates/minimality.md
src/heller_godel/*.py
```

Policy: hits require remediation, an explicit inline exemption, or reclassification.

### context-no-patch

Paths:

```text
docs/context/**
sources/primary/**
sources/context/**
data/manifests/**
```

Policy: hits are review evidence only. Do not rewrite context/source evidence merely to satisfy current theorem-core terminology.

### historical-no-patch

Paths:

```text
docs/source-captures/**
**/*historical*
**/*history*
```

Policy: preserve unless a separate archival-normalization task is opened.

### legacy-manuscript-no-patch

Paths:

```text
docs/manuscripts/calculus_invariant_characters_*.md
docs/manuscripts/*patch_plan*.md
```

Policy: report separately from active Paper I theorem core. These files are superseded or transition artifacts, not the active Paper I claim surface.

## Connector-backed findings

### 1. Active Paper I is the current canonical theorem surface

The current README identifies the active capture as:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
```

It also states the current defensible core in terms of proof-class generating functions, decorated Puiseux singular data, branch-killing cyclic covers, Deligne units, finite monodromy/deck characters, lifted phase indices, and section-defect carry cocycles.

This means the old v1.6 bundle/path-category replacement plan must not be blindly applied across the whole repository. It is now a legacy-terminology hygiene pass, not a canonical architecture migration.

### 2. `Π₁(B)` exact Unicode form

Repository search for exact `Π₁` returned no scoped results in the connector surface.

Preliminary status: no active Unicode `Π₁(B)` blocker observed.

### 3. `\Pi_1` / `pi_1` style hits

Connector search for `Pi_1` returned hits in:

```text
docs/gates/minimality.md
docs/appendices/appendix_a_chain_catalan_witness.md
docs/context/proof-dynamics-mu2-bridge-artifact.md
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
docs/manuscripts/calculus_invariant_characters_v2_1_3.md
docs/source-captures/calculus_invariant_characters_capture.md
docs/manuscripts/calculus_invariant_characters_v2_1_3_patch_plan.md
```

Interpretation:

- `docs/gates/minimality.md`: theorem-core, but observed usage is about `pi_1(SO(3))`, `pi_1(SU(2))`, and the distinction between loop class and spin-lifted central element. This is not the old `\Pi_1(B)` path-category issue.
- `docs/appendices/appendix_a_chain_catalan_witness.md`: theorem-core appendix. Observed usage is fundamental-group notation for finite local-system holonomy and the conditional encoding datum. This is current architecture, not stale path-groupoid terminology.
- `docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md`: theorem-core. Observed usage is `pi_1` finite-local-system language. This is expected and should not be rewritten to `\mathsf{Path}(B)` unless a path-category transport section is introduced.
- `docs/context/*`, `docs/source-captures/*`, and `calculus_invariant_characters_*`: report-only unless a later patch PR explicitly targets legacy manuscript normalization.

### 4. `fundamental path groupoid`

Connector search returned no results.

Preliminary status: no active blocker observed.

### 5. `homotopy class` / `homotopy classes`

Connector search returned no results.

Preliminary status: no active blocker observed.

### 6. `simply connected`

Connector search returned no results for exact phrase in scoped active surfaces.

Preliminary status: no active blocker observed.

### 7. `every loop is contractible`

Connector search returned hits in:

```text
docs/context/proof-dynamics-mu2-bridge-artifact.md
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
```

Required review distinction:

- If a theorem-core sentence uses contractibility as a substitute for the current finite-local-system argument, patch it.
- If the current sphere section is only a sanity check deriving trivial finite-local-system pullback from `pi_1(S^2)=0`, it is legitimate and should remain, possibly with clearer wording.

The current Paper I sphere argument should be stated as:

```text
S^2 is a test manifold with pi_1(S^2)=0.
Therefore every homomorphism pi_1(S^2) -> mu_N is trivial.
Therefore every pulled-back finite mu_N local system on S^2 is trivial.
This is a sanity check for the finite-local-system interface, not a structural holonomy theorem.
```

Do not replace this with path-category machinery.

## Formal separation: carry versus Deligne symbol

The audit must preserve the current separation:

```text
finite arithmetic carry / section defect != Deligne cup-product regulator symbol
```

Required invariant:

- The carry term belongs to the finite lifted-index arithmetic layer. In the current implementation, it is the section-defect cocycle for `0 -> Z -> Z -> Z/L -> 0`.
- The Deligne cup-product symbol belongs to the regulator-symbol layer and lands in a degree-2 Deligne-cohomology target.
- These objects have different degrees, functoriality, and computational status.

The code should continue to tag these separately. In `phase_characters.py`, functions such as `carry`, `carry_table`, and `carry_cocycle_identity_holds` are finite-arithmetic helpers. The helper `tame_symbol_standard` records the regulator-symbol boundary convention and must not be described as computing carry.

## Pre-patch disposition

No text patches are included in this branch.

Recommended follow-on PRs:

1. Run the committed script locally or in CI:

```bash
python scripts/audit_legacy_topology_terms.py --output docs/review-ledgers/HG_LEGACY_TOPOLOGY_TERMS_AUDIT_LOCAL.md --fail-on-core
```

2. If theorem-core hits remain, open narrowly scoped patch PRs in this order:

```text
PR A: Paper I wording only
PR B: Appendix A wording only
PR C: gate/minimality wording only
PR D: optional legacy manuscript normalization, if desired
```

3. Do not rewrite source-capture, context, or historical material unless a separate archival policy is approved.

## Decision log

- The stale v1.6 replacement bundle was not applied globally.
- The audit branch is audit-only.
- The canonical active manuscript is Paper I, not the older v2.1.3 floor-function-first manuscript.
- `pi_1` notation is allowed in finite-local-system theorem-core where it denotes the domain of finite monodromy/holonomy characters.
- `\mathsf{Path}(B)` should only be introduced where actual geometric path-category transport is being defined.
- `S^2` may be used as a trivial sanity-check base via `pi_1(S^2)=0`, but not as a theorem-grade substitute for a path/holonomy construction.
