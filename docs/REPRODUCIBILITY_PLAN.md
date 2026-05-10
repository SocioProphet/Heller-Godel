# Reproducibility Plan

The Heller-Godel repository should make only the load-bearing proof-character work reproducible. Context files are preserved and hash-locked, but not executed as dependencies.

## Reproducible core

The reproducible core is:

```text
phase maps chi_p and chi_13
carry defect zeta_p
coboundary/split-extension correction
Puiseux shell extraction examples
chain-product correction
statistic falsifier
```

## Non-reproducible context

The BSD materials are retained as context. They are not part of this repository's test suite.

Temporal Mechanics is retained as future-horizon context for shell, operator, and nonassociative directions. It is not part of the proof-character test suite.

## Required tests

- `k_13(-2) = (0,0,0,0,0,0)`.
- `k_13(1/2) = (1,1,2,3,5,6)`.
- `zeta_p(alpha,beta)` equals `f_p(alpha+beta)-f_p(alpha)-f_p(beta)`.
- `zeta_p(alpha,beta) = zeta_p(beta,alpha)`.
- The ordinary extension defined by `zeta_p` is split once the cochain `f_p` is allowed.
- `x/(1-x)^2` squared equals `x^2/(1-x)^4`.
- Catalan has leading nonanalytic Puiseux exponent `1/2` at `rho=1/4`.
- Statistics can change generating functions and shell structure.

## Artifact policy

Manuscript PDFs should be generated from markdown or LaTeX source. Uploaded PDFs are source evidence, not canonical generated output.

Every generated artifact should appear in an artifact manifest with:

- path,
- source command,
- source inputs,
- SHA-256,
- timestamp,
- and validation status.
