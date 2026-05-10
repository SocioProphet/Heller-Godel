# Claim Boundary Register

This register is the current guardrail for the Heller-Godel proof-character program.

## Defensible current core

The current core thesis is:

```text
For restricted proof grammars and a fixed canonical statistic, normal-proof families admit generating functions. Their Puiseux singularity data yield finite phase reductions. These phase reductions are strictly multiplicative in no-carry regimes and fail strict multiplicativity by an explicitly computable mod-p carry defect. The defect is a section-dependent finite-resolution artifact, not yet a nontrivial group-cohomological obstruction.
```

## Current established or computable claims

| Claim | Status | Notes |
|---|---|---|
| `T_phi^sigma(x)` depends on fixed statistic `sigma` | construction-fixed-scope | Statistic must be fixed; no statistic-free invariant is claimed. |
| Finite seed basis `P_13 = {2,3,5,7,11,13}` | construction-fixed-scope | Computational truncation, not a complete invariant. |
| `k_13(1/2) = (1,1,2,3,5,6)` | computed-identity | Catalan square-root exponent example. |
| `zeta_p(alpha,beta)` is a mod-p carry defect | computed-identity | Exact arithmetic identity. |
| `zeta_p` is symmetric | computed-identity | Consequence of commutativity of addition. |
| `zeta_p` is a coboundary of `f_p(alpha)=floor(p alpha) mod p` | computed-identity | Blocks nontrivial ordinary cohomology claim absent extra structure. |
| Puiseux shell support refines dominant exponent extraction | construction-fixed-scope | Analytic shell construction only. |

## Current non-claims

| Non-claim | Reason |
|---|---|
| Nonabelian central extension from current `zeta_p` | Current cocycle is symmetric and a coboundary in ordinary cohomology. |
| Nontrivial Chern-class lift | Requires proof-moduli, line bundle/local system, connection, curvature, and base map. Not constructed. |
| Cognitive theory of recognition | Motivation/future horizon only; no empirical or formal bridge yet. |
| Operator shell dynamics | No operator family with spectrum tied to proof-character shells has been constructed. |
| Nonassociative or Moufang-valued proof holonomy | Future horizon; requires proof-moduli and holonomy construction. |

## Required manuscript corrections

- Replace nontrivial central-extension language with section-defect/coboundary language.
- Define local exponents as Puiseux exponent channels.
- Mark chain/Catalan examples as calibration unless explicit proof types are constructed.
- Correct chain-product algebra: ordinary product of `x/(1-x)^2` with itself is `x^2/(1-x)^4`.
- State calculus-invariance only after canonicalization into a shared normal-form representation.
- Demote regulator/Chern-class material to candidate/future work.

## Promotion rule

No item in `docs/future-horizons/` may be promoted into `docs/manuscripts/` as a theorem claim without:

1. a constructed object,
2. a reproducible computation or proof,
3. a claim-boundary update,
4. and a review ledger explaining what changed.
