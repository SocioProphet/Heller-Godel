# Extended Heller–Gödel Chat Corpus Capture v0.1

Status: capture manifest and routing map. This document preserves the extended work from the chat corpus and assigns each major block a claim-status route. It is not a theorem, not a manuscript revision, and not a promotion of future-horizon material into theorem-core.

## 1. Purpose

The Heller–Gödel program now contains two classes of material:

1. theorem-core and computable infrastructure, where claims are stated, tested, and falsifiable;
2. exploratory prose, analogies, research directions, and philosophical framing that must be preserved for future curation without being mistaken for proof.

This capture file is the bridge between the two. It records what was generated, where it belongs, what is already upstream, and what remains future-horizon.

The governing standard is `docs/governance/proof_falsification_infrastructure.md`: every tranche must leave reusable proof/falsification infrastructure, and every nontrivial claim must be labeled by proof status.

## 2. Current theorem/computation core already captured

### 2.1 CIPC / proof-character core

Core load-bearing chain:

```text
restricted proof grammar
+ canonical normal-form representation
+ fixed statistic
-> proof-family generating function
-> Puiseux singularity / shell data
-> finite phase reductions chi_p and chi_13
-> mod-p carry defect zeta_p
-> falsifiers for overclaims
```

Status: theorem-core direction, but the corrected CIPC manuscript tranche is still governed by open issues HG-M2/HG-M3/HG-ANNEAL-001. No future-horizon object may be used as proof support until constructed.

### 2.2 HG-STAT line

Captured and merged:

- HG-STAT-001: admissible constructor-linear statistics, theorem-level on chain and T-family, with erratum after Catalan.
- HG-STAT-002: Catalan algebraic admissibility test, syntax conventions, radius covariance.
- HG-STAT-003: Motzkin/non-rank-uniform algebraic robustness, bivariate GF correction, simple-branch exponent preservation, radius covariance.

Status: computed/theorem-level for the stated families only. General regular/algebraic/D-finite extension remains conjectural.

### 2.3 Proof/falsification doctrine

Captured and merged:

```text
docs/governance/proof_falsification_infrastructure.md
```

Status: governance/process infrastructure. It does not add a theorem.

## 3. Material captured by this prose tranche

This branch captures the remaining prose/corpus work as routed documents:

```text
docs/future-horizons/wythoff_schwarz_symmetry_grammar.md
docs/future-horizons/projection_chart_vs_preimage.md
docs/future-horizons/extended_hg_future_horizon_inventory.md
docs/essays/godel_provability_irony_and_hg_program.md
docs/review-ledgers/extended_hg_prose_claim_ledger.md
```

The objective is preservation with claim discipline.

## 4. Claim-status inventory

| Topic | Route | Status | Why |
|---|---|---|---|
| `zeta_p` carry identity | CIPC theorem-core/tests | computed/proved for displayed formula | Finite arithmetic identity and coboundary test are directly checkable. |
| `zeta_p` as nontrivial group-cohomological obstruction | review ledger only | false_as_stated under ordinary cochain freedom | It is a coboundary of the discretization cochain unless extra structure is added. |
| Nonabelian / Heisenberg interpretation | future-horizon only | needs_formalization | Requires antisymmetric multiplier, ordered/braided product, enriched lattice, or higher categorical structure. |
| Regulator/Chern lift | future-horizon only | needs_formalization | Requires proof-moduli, bundle, connection, curvature, and base map. |
| Multi-shell/Puiseux support | theorem-core/analytic note | computed/proved for analytic functions | Local product theorem and shell support convolution are analytic statements. |
| Statistic-class robustness | HG-STAT-001/002/003 | computed/proved on four families; conjectural generally | Tests exist for families; general theorem still open. |
| Wythoff/Schwarz alignment | future-horizon/context | context_only/future_horizon | A mature analogy for symbolic seed -> regime realization, not proof of HG mechanisms. |
| Projection/preimage discipline | future-horizon/context | context_only/future_horizon | Useful vocabulary for chart artifacts, section choices, and coboundary dissolution. |
| AdS/CFT vocabulary | caution only | context_only | Structural analogy only; no holographic duality claim. |
| Gödel/provability irony | essay/methodology | context_only | Explains why proof-status discipline is itself central to the program. |
| BSD material | context-only / separate repo | context_only | Governance precedent for evidence gates, not HG theorem evidence. |

## 5. What this capture does not do

This tranche does not:

- modify CIPC v2.1.3;
- close HG-M2, HG-M3, HG-M4, or HG-ANNEAL-001;
- prove the regulator/Chern lift;
- construct proof-moduli;
- introduce a recognition-dynamical operator;
- justify cognition or AdS/CFT claims;
- import BSD as Heller–Gödel theorem evidence.

## 6. Next bounded work after capture

After this prose/corpus capture merges, the next bounded actions are:

1. Complete HG-M2/HG-M3: corrected manuscript plus computable verification harness.
2. Consolidate duplicate CI-observation issues and close the redundant one.
3. Promote Wythoff/Schwarz only if a concrete grammar parser or curvature-regime test is added.
4. Keep regulator/Chern and Moufang/nonassociative work blocked until proof-moduli and holonomy assignments exist.

## 7. Completion criterion for this capture tranche

This capture tranche is complete when:

- the five prose/future-horizon/essay/ledger files in §3 are committed;
- the PR body states the claim boundary;
- CI or repository validation is observed if available;
- open issues #4 and #5 are updated to point to the committed notes;
- no theorem-core issue is closed merely because exploratory prose has been preserved.
