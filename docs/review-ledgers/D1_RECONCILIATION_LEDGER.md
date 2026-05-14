# D1 Reconciliation Ledger

Status: active reconciliation ledger.  
Date: 2026-05-14.  
Branch: `hg-d1-reconciled-draft`.  
Target draft: `docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md`.

## Purpose

This ledger records the source inventory and merge decisions for promoting Paper I to the canonical D1 reconciled draft.

The goal is not to bulk-copy legacy text. The goal is to preserve the theorem-bearing content of the v2.1.3 working manuscript where it survives the Deligne-cohomological rewrite, while keeping the current claim boundaries, topology audit invariants, and carry/Deligne separation intact.

Validation note: this branch must pass `legacy-topology-audit`, `validate`, and `Proof apparatus continuous validation` before merge.

## Source inventory

### Baseline D1 skeleton

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
```

Disposition: canonical D1 theorem-core draft.

Rationale: this file already contains the Deligne-cohomological rewrite, finite local-system interface, `mu_2` comparison theorem, limitations matrix, Hodge nonclaims, CI-backed invariant summary, and appendix map.

### v2.1.3 expansion source

```text
docs/manuscripts/calculus_invariant_characters_v2_1_3.md
```

Disposition: merged where compatible; retained as legacy source.

Merged domains:

```text
finite phase maps
carry as section defect / coboundary correction
multi-shell analytic support
flat base-relative visibility
limitations and nonclaim discipline
future-horizon quarantine
```

Superseded domains:

```text
floor-function-first primary framing
prime-order-only character presentation
claims that treat carry as a nontrivial obstruction
regulator/Chern material not routed through Deligne-unit and tame-symbol separation
real-test-manifold language that could imply native Deligne/Chern classes on real bases
```

### v2.1.3 patch plan

```text
docs/manuscripts/calculus_invariant_characters_v2_1_3_patch_plan.md
```

Disposition: context for prior repair path; not theorem-core source.

Rationale: useful for historical patch intent, but the current D1 draft and audit ledger are the controlling documents.

### Source capture

```text
docs/source-captures/calculus_invariant_characters_capture.md
```

Disposition: provenance/context only.

Rationale: source captures are intentionally preserved and are not patched as theorem-core material.

### v2.1.2 expansion source

Live repository search found no file or indexed source matching:

```text
v2.1.2
v2_1_2
2.1.2
```

However, a sandbox copy was available during this pass:

```text
/mnt/data/calculus_invariant_characters_v2_1_2.md
sha256: 9eb473ce22d7a0af0c1924d3fabe4bb85a3a999dc81a443d19a735670ca72d70
```

A provenance manifest is recorded at:

```text
docs/source-captures/calculus_invariant_characters_v2_1_2_manifest.md
```

Disposition: inspected as provenance, not controlling theorem-core source.

Merge consequence: v2.1.2 does not override v2.1.3 or D1. It confirms the pre-Deligne trajectory: statistic-relative generating functions, finite phase fingerprints, carry/cocycle language, multi-shell support, regulator-lift ambitions, and base-relative visibility. D1 preserves only the portions that survive the Deligne-cohomological rewrite and claim-boundary gates.

## Locked audit invariants

The D1 draft must continue to satisfy the active governance checks:

```text
python scripts/audit_legacy_topology_terms.py --diff-against-frozen --fail-on-core --fail-on-scope-drift
python scripts/check_claim_boundaries.py
python scripts/check_ci_gate_registry.py
```

Specific locked invariants:

1. Finite `pi_1` notation is allowed for monodromy/local-system character domains.
2. Stale capital-Pi base path-category transport language is not reintroduced in theorem-core.
3. Carry remains a finite section-defect cocycle attached to lifted integer representatives.
4. Deligne cup-product/tame-symbol material remains a distinct regulator-symbol branch.
5. `S^2` appears only as a finite local-system sanity check via `pi_1(S^2)=0`.
6. Real test manifolds receive finite local systems only; no native Deligne or Chern class on `B` is claimed.
7. Hodge nonclaims remain explicit and enforced.

## Merge decisions

### Decision 1 — Name Paper I as D1

Action: update the manuscript title to:

```text
Paper I / D1 — Deligne-Cohomological Phase Characters from Proof-Class Generating Functions
```

Rationale: the live repository no longer has a separate D1 skeleton file. Paper I is the current canonical theorem-core surface and now carries the D1 reconciliation status explicitly.

### Decision 2 — Keep the Deligne-first framing

Action: D1 keeps the Deligne-unit-first construction.

Rationale: v2.1.2 and v2.1.3's floor-function-first framing is historically important but mathematically superseded. The current construction correctly makes the Puiseux singular unit on a branch-killing cover primary, with finite characters as monodromy/deck shadows.

### Decision 3 — Preserve v2.1.x finite arithmetic as shadow layer

Action: v2.1.2/v2.1.3 finite phase and carry material survives only as the finite shadow / lifted-index arithmetic layer.

Rationale: the finite character is multiplicative. The carry measures the failure of a chosen integer section to preserve addition. It is not a Deligne regulator, Chern class, nonabelian obstruction, or nontrivial ordinary group-cohomology class by itself.

### Decision 4 — Preserve v2.1.x base-relative visibility through finite local systems

Action: sphere, torus, and Klein-bottle material survives through Section 5 as finite local-system pullback data.

Rationale: this retains the useful topological tests without claiming analytic Deligne cohomology on real non-orientable manifolds.

### Decision 5 — Preserve limitations and nonclaims in D1

Action: D1 keeps the severity matrix, Hodge nonclaims, and statement that most dynamical/recognition/higher-prime gates remain open or conditional.

Rationale: this is the claim-boundary spine. It prevents v2.1.x future-horizon material from inflating into theorem-core claims.

## Divergence notes

| Topic | v2.1.x disposition | D1 disposition | Resolution |
| --- | --- | --- | --- |
| Primary object | finite phase maps from floor functions | Deligne unit on branch-killing cover | D1 wins; finite phase is a shadow. |
| Carry | finite-resolution section defect / coboundary correction, with older central-extension ambitions in v2.1.2 | finite section defect explicitly separated from Deligne symbol | D1 wins; no carry-as-regulator or carry-as-obstruction claim. |
| Regulator/Chern | future horizon / partial framework; v2.1.2 sketches stronger lift language | Deligne unit plus separate cup-product/tame-symbol branch; no Chern lift claimed | D1 wins. |
| Sphere | flat holonomy trivial because `pi_1(S^2)=0` | finite local-system sanity check | Compatible; not structural theorem substitute. |
| Klein bottle | flat torsion visibility | pulled-back finite `mu_2` local system only | D1 wins; no native Deligne class on `K`. |
| Dynamical Floquet phase | future horizon / conditional | Theorem 6.2 conditional on encoding hypothesis | Compatible with stricter conditions. |
| Odd primes | open/future | Conjecture 6.3 finite-cyclic comparison problem | Compatible; no Hodge claim. |
| Hodge relevance | explicitly nonclaimed or absent as theorem | explicitly nonclaimed and claim-guarded | D1 wins. |

## Current result

After this reconciliation pass, the D1 manuscript is not a newly invented document. It is the existing Paper I theorem-core draft made explicit as the reconciled D1 target, with the v2.1.2/v2.1.3 source relationship recorded.

The next substantive proof front is Appendix A / encoding closure:

```text
chain witness
Catalan witness
Catalan encoding hypothesis
Theorem 6.2 conditional-to-closed transition, if the encoding is completed
```

Until Appendix A is complete, Theorem 6.2 remains conditional and Theorem 6.1 remains the unconditional analytic-topological result.
