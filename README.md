# Heller-Godel

Research corpus for the Extended Heller-Godel / proof-character program.

This repository is also the canonical framework-core repository for the Heller-Godel / Clay-program estate. The framework-core declaration lives in `docs/framework-core/`; no separate `heller-godel-core` repository is required.

This repository studies analytic invariants of proof-normalization families. The current defensible core is:

```text
restricted proof grammar + fixed canonical statistic
-> proof-class / proof-family generating function
-> Puiseux singularity data
-> finite phase reductions chi_p and chi_13
-> explicit mod-p carry defect zeta_p under composition
```

The newer Paper I rewrite sharpens this core into a Deligne-cohomological framing:

```text
proof-class generating function
-> decorated Puiseux singular datum at a chosen puncture
-> branch-killing cyclic cover
-> Puiseux singular unit upstairs
-> level-1 Deligne unit
-> finite monodromy / deck character downstairs
-> lifted phase index
-> section-defect carry cocycle
```

A separate regulator branch is tracked in parallel:

```text
two level-1 Deligne units
-> level-2 Deligne cup-product symbol
-> tame-symbol / regulator residue
```

The carry cocycle and Deligne cup-product symbol are intentionally not identified.

## Framework-core role

`SocioProphet/Heller-Godel` is the upstream framework-core repository for the Clay-program portfolio.

It owns:

- framework identifiers and downstream citation grammar;
- distance classification for framework-foundational, framework-vocabulary, framework-method, and fixture-grade objects;
- anti-seed doctrine and claim-boundary failure modes;
- canonical apparatus fixtures such as Catalan / `mu_2`;
- normalized source imports after review.

It does not own problem-specific Clay proof claims. RH / GRH, Hodge, BSD, P vs NP, Yang-Mills, and Navier-Stokes work remains in the corresponding program repositories.

The framework-core bootstrap documents are:

- `docs/framework-core/README.md`
- `docs/framework-core/distance-classification.md`
- `docs/framework-core/claim-grammar.md`
- `docs/framework-core/anti-seed-framework.md`
- `docs/framework-core/dependency-graph.md`
- `docs/doctrine/catalan-mu2-canonical-reference.md`
- `DEPENDENCIES.md`

## Current Paper I

The active capture is:

- `docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md`

This document is the working Deligne-cohomological rewrite of the older floor-function-first manuscript. It records the current claim boundary, proof architecture, finite local-system interpretation on real test manifolds, and open gates.

## Claim boundary

This repository does **not** currently prove a nonabelian obstruction theory, a Chern-class lift, a cognitive theory of recognition, progress on the Hodge conjecture, algebraicity of the resulting classes, or algebraic-cycle realization.

The framework-core layer also does **not** claim proof of RH, GRH, BSD, P vs NP, Yang-Mills mass gap, or Navier-Stokes. Universal Bridge material, when imported, is method-grade structural analogy unless separately promoted by proof.

The carry term is now treated as a finite-resolution section defect: it measures the failure of canonical residue representatives modulo `L` to add. The actual finite monodromy character is multiplicative.

The Deligne cup-product symbol is the regulator-symbol refinement of a pair of level-1 units. Its local boundary is a tame symbol. It is not the carry cocycle.

## Reproducibility contract

Every mathematical claim that can be reduced to finite arithmetic should have a regression test. Current executable coverage lives in:

- `src/heller_godel/phase_characters.py`
- `tests/test_phase_characters.py`
- `scripts/check_claim_boundaries.py`
- `.github/workflows/validate.yml`

The CI currently checks:

- rational exponent normalization in `Q/Z`;
- common branch-killing levels;
- deck / monodromy phase indices;
- `p`-primary projection and prime reduction;
- exact multiplicativity of finite characters;
- carry as a section-defect cocycle;
- carry cocycle identity;
- tame symbol not equal to carry;
- Catalan / Klein-bottle `mu_2` holonomy bookkeeping;
- manuscript claim-boundary guardrails.

Local verification:

```bash
python -m pip install -e .[dev]
pytest -q
python scripts/check_claim_boundaries.py
```

## Source taxonomy

Load-bearing source material lives in `sources/primary/` once binary sources are imported. Context and methodological precedent live in `sources/context/`. The BSD program material is context only: it demonstrates evidence gates, rollback discipline, and reproducibility practice, but it is not a dependency of the Heller-Godel theorem stack.

The initial connector bootstrap records the complete source inventory and hashes in `docs/SOURCE_CLASSIFICATION.md` and `data/manifests/SOURCE_MANIFEST.*`. Binary PDFs and ZIPs are not committed by this connector pass; they are hash-locked for follow-up source import.

After a source is imported, normalized, and merged into this repository, the repo version is canonical for downstream citation. Drive originals remain provenance.

## Current milestones

- HG-M0: bootstrap repository and source taxonomy.
- HG-M1: import uploaded sources and freeze hashes.
- HG-M2: produce corrected `calculus_invariant_characters_v2_1_3.md`.
- HG-M3: implement verification tests for phase maps, carry coboundary, Puiseux shells, chain-product correction, and statistic falsifier.
- HG-M4: preserve future horizons without promoting them into current theorem claims.
- HG-M5: develop Paper I Deligne-cohomological rewrite into a submission-ready manuscript.
- HG-M6: expand executable coverage from finite arithmetic into symbolic proof obligations where feasible.
- HG-M7: maintain framework-core identity, dependency graph, and downstream citation grammar for the Clay-program estate.
