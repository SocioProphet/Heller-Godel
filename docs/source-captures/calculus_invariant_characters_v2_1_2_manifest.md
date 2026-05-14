# Source Capture Manifest — Calculus-Invariant Characters v2.1.2

Status: provenance manifest, not theorem-core.  
Capture date: 2026-05-14.  
Source observed in sandbox path: `/mnt/data/calculus_invariant_characters_v2_1_2.md`.  
SHA-256: `9eb473ce22d7a0af0c1924d3fabe4bb85a3a999dc81a443d19a735670ca72d70`.

## Purpose

This file records that a v2.1.2 source was available in the execution sandbox during the D1 reconciliation pass, even though no `v2.1.2`, `v2_1_2`, or `2.1.2` source was found on live repository `main` by GitHub search.

The manifest is retained as provenance only. It does not promote v2.1.2 claims into theorem-core.

## Section inventory

```text
# Calculus-Invariant Phase Characters from Proof-Class Generating Functions
## A Working Paper, Revision 2.1.2
### Abstract
# Part I — The Abelian Regime
## 1. Motivation and scope
## 2. The proof-class generating function
### 2.1 Definition
### 2.2 Calculus-invariance
### 2.3 Worked examples
## 3. The character chi_p — abelian regime
### 3.1 Singularity data
### 3.2 Definition
### 3.3 Worked spectra
### 3.4 Strict multiplicativity in the abelian regime
### 3.5 Finite arithmetic seed basis
# Part II — The Projective Regime and Multi-Shell Extension
## 4. The carry cocycle zeta_p
### 4.1 Definition
### 4.2 The carry interpretation
### 4.3 Worked examples
### 4.4 Cocycle property
### 4.5 Central extension
### 4.6 The character of the central extension
### 4.7 Multi-Shell Characters
### 4.8 Shell-Product Theorem
### 4.9 Worked Example: Catalan x Chain
### 4.10 Boundary of the Multi-Shell Result
### 4.11 Falsifier and Implementation Check
# Part III — The Regulator Lift
## 5. From projective to integer-valued
### 5.1 The regulator form
### 5.2 Periods
### 5.3 Relation to chi_p
### 5.4 Chern classes
### 5.5 Status of the regulator construction
# Part IV — Base-Manifold Pairings
## 6. Cohomological setup
## 7. Three bases
### 7.1 S^2
### 7.2 T^2
### 7.3 Klein bottle K (abba)
## 8. Base-relative regime classification
# Part V — Status
## 9. Summary of established results
## 10. What remains conjectural
## 11. Limitations explicitly retained
## Appendix A — Computational verification
### A.1 Catalan p-adic valuation
### A.2 Carry cocycle zeta_p table
### A.3 Triangular product
### A.4 Multi-shell composition tests
### A.5 Statistic-invariance falsifier
## Appendix B — Notation
## Appendix C — Selected references
```

## D1 reconciliation disposition

v2.1.2 is superseded by v2.1.3 and then by the D1 Deligne-cohomological rewrite.

The following v2.1.2 themes are preserved only where rewritten safely in D1:

- statistic-relative proof-class generating functions;
- finite arithmetic seed basis / phase fingerprinting;
- carry as finite arithmetic section defect;
- multi-shell analytic support as a generating-function statement;
- base-relative visibility through finite local-system data.

The following v2.1.2 themes are not promoted into D1 theorem-core:

- non-split central-extension language as theorem-core;
- regulator/Chern lift claims not routed through the D1 Deligne-unit and tame-symbol separation;
- native Chern/Deligne conclusions on real test manifolds;
- claims that the carry cocycle itself supplies regulator or Chern content.

The controlling D1 source remains:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
```
