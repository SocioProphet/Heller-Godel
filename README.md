# Heller-Godel

Research corpus for the Extended Heller-Godel / proof-character program.

This repository studies analytic invariants of proof-normalization families. The current defensible core is:

```text
restricted proof grammar + fixed canonical statistic
-> proof-class / proof-family generating function
-> Puiseux singularity data
-> finite phase reductions chi_p and chi_13
-> explicit mod-p carry defect zeta_p under composition
```

## Claim boundary

This repository does **not** currently prove a nonabelian obstruction theory, a Chern-class lift, or a cognitive theory of recognition. Those are future-horizon programs gated on additional constructions: proof-moduli, bundle/connection data, operator spectra, and nonassociative holonomy.

The carry term `zeta_p` is currently treated as a finite-resolution section defect. In the ordinary group-cohomological setting it is a coboundary of `f_p(alpha)=floor(p alpha) mod p`, so it is not by itself a nontrivial nonabelian or nonassociative obstruction.

## Source taxonomy

Load-bearing source material lives in `sources/primary/` once binary sources are imported. Context and methodological precedent live in `sources/context/`. The BSD program material is context only: it demonstrates evidence gates, rollback discipline, and reproducibility practice, but it is not a dependency of the Heller-Godel theorem stack.

The initial connector bootstrap records the complete source inventory and hashes in `docs/SOURCE_CLASSIFICATION.md` and `data/manifests/SOURCE_MANIFEST.*`. Binary PDFs and ZIPs are not committed by this connector pass; they are hash-locked for follow-up source import.

## Current milestones

- HG-M0: bootstrap repository and source taxonomy.
- HG-M1: import uploaded sources and freeze hashes.
- HG-M2: produce corrected `calculus_invariant_characters_v2_1_3.md`.
- HG-M3: implement verification tests for phase maps, carry coboundary, Puiseux shells, chain-product correction, and statistic falsifier.
- HG-M4: preserve future horizons without promoting them into current theorem claims.
