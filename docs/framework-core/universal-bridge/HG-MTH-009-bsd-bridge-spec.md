# HG-MTH-009 — Universal Bridge: BSD Arithmetic-Geometric Domain Extension

Identifier: `HG-MTH-009`  
Distance tier: Framework-method (Tier 3)  
Status: Active after this PR  
Heller-Dirac citation pin: `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993`  
Anti-seed: `A-HG-MTH-001`, `A-HG-MTH-002`, `A-HG-MTH-003`, `A-HG-MTH-004`, `A-HG-MTH-006`, `A-HG-MTH-007`

## Status under the Universal Bridge

`HG-MTH-005` established the Universal Bridge as method-grade structural analogy with factorization:

```text
B = (M, R, A)
```

where `M` is the mean-field or smooth-expected structure, `R` is the residual obstruction, and `A` is the apex obstruction package.

This document instantiates the Birch and Swinnerton-Dyer arithmetic-geometric domain.

This document is method-grade only. It does not transfer proofs.

## Heller-Dirac dependency surface

This is Heller-Godel framework content whose mathematical vocabulary cites Heller-Dirac reference-surface objects at a pinned commit:

```text
SocioProphet/Heller-Dirac @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993
```

Cited Heller-Dirac objects:

- `HD-FND-001` — spectral triple base structure.
- `HD-FND-007` — Tomita-Takesaki modular operator and modular flow.
- `HD-EX-001` — circle spectral triple fixture as a basic spectral building block.
- `A-HD-NC-001` — reformulation is not proof.
- `A-HD-SP-001` — analog spectral data is not target spectral data.
- `A-HD-TM-001` — modular flow is not automatically physical time.
- `A-HD-FND-001` — reference surface is not reproof.

Heller-Godel remains the framework-core repository; these are content citations, not a repository-level upstream dependency change.

## Clay BSD statement

Let `E` be an elliptic curve over `Q` with L-function `L(E, s)`.

The Birch and Swinnerton-Dyer conjecture asserts two related but distinct claims:

1. BSD-rank: the order of vanishing of `L(E, s)` at `s = 1` equals the Mordell-Weil rank of `E(Q)`.
2. BSD-strong: the leading Taylor coefficient at `s = 1` equals the standard arithmetic expression involving regulator, real period, Tamagawa numbers, torsion, and the Tate-Shafarevich group.

The Clay problem requires the full statement in generality.

## BSD bridge factorization

Let `E / Q` be an elliptic curve.

### Mean-field M

```text
M_BSD(E) = E(Q) tensor_Z R
```

The mean-field is the real Mordell-Weil group. By the Mordell-Weil theorem, `E(Q)` is finitely generated; after quotienting torsion and tensoring with `R`, this becomes a finite-dimensional real vector space. Its dimension is the algebraic rank.

### Residual R

```text
R_BSD(E) = ord_{s=1} L(E, s) - rank E(Q)
```

The residual is the analytic-rank / algebraic-rank discrepancy. BSD-rank asserts `R_BSD(E) = 0` for all elliptic curves over `Q`.

BSD-strong refines the residual by comparing the leading Taylor coefficient with the Tamagawa-regulator-Sha expression. That refinement is structurally distinct and must not be collapsed into rank equality.

### Apex obstruction A

The BSD apex obstruction is a compiled triple:

```text
A_BSD in SelmerSha ∪ BostConnesEndomotive ∪ ModularityPadic
```

#### Component 1 — Selmer and Tate-Shafarevich apparatus

Selmer groups relate rational points to local-solubility data and the Tate-Shafarevich group. The exact sequence relating `E(Q)/nE(Q)`, the `n`-Selmer group, and `Sha(E/Q)[n]` is the algebraic descent surface.

The general finiteness of `Sha(E/Q)` is open and is part of BSD-strong. Any artifact assuming finiteness must state that assumption explicitly.

#### Component 2 — Bost-Connes / endomotive spectral surface

The Bost-Connes system and its endomotive extensions give a noncommutative-geometric and dynamical-system surface where L-functions appear as partition functions or spectral/arithmetic data.

Per `A-HD-NC-001` and `A-HD-SP-001`, reformulating the L-function through a spectral or noncommutative-geometric apparatus is not proof of BSD. The spectral surface is method-grade context.

#### Component 3 — Modularity and p-adic L-functions

Modularity makes the analytic continuation of `L(E, s)` available for elliptic curves over `Q`. Iwasawa theory, Euler systems, Heegner points, and p-adic L-functions provide powerful restricted-scope apparatus.

Gross-Zagier and Kolyvagin handle important rank `<= 1` regimes. Skinner-Urban and related Iwasawa-theoretic work handle additional restricted cases. These are major mathematical results, but they do not prove BSD in full generality.

## Shared missing machinery diagnosis

BSD shares the bridge diagnosis with RH, Hodge, Yang-Mills, and P vs NP:

```text
The problem requires apparatus operating below the level where current proof techniques have grip.
```

For BSD, the missing apparatus is a general mechanism relating analytic order of vanishing, Selmer/Sha structure, p-adic L-functions, and the leading coefficient formula for arbitrary elliptic curves over `Q`.

This is structurally cognate with other bridge domains. It is not the same tool, and no proof transfers.

## Method-level apparatus landscape

### Gross-Zagier-Kolyvagin

Heegner-point and Euler-system methods establish strong results for rank `<= 1` cases under appropriate hypotheses. These results are method-level apparatus for BSD, not full Clay resolution.

### Iwasawa theory

Iwasawa Main Conjecture technology relates p-adic L-functions to Selmer groups. It supplies powerful component-level apparatus, but the full generality of BSD remains open.

### Bost-Connes / endomotive framework

The noncommutative-geometric formulation provides spectral and dynamical context for zeta and L-functions. It is method-grade context, not proof.

### bsd-proof-program

The `bsd-proof-program` repo is bootstrap-stage apparatus: workstream A-F skeletons, M6 discipline, congruent-number fixtures, and promotion-gate structure. It does not claim BSD progress.

## Consumer surface

Primary consumer:

```text
SocioProphet/bsd-proof-program
```

Downstream citation form:

```text
[HG-MTH-009 @ <merged-Heller-Godel-commit-sha>]
[HD-FND-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-007 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-EX-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
```

A follow-up `bsd-proof-program` PR should advance its Heller-Godel pin, add `HG-MTH-009`, add `A-HG-MTH-007`, and add Heller-Dirac as a second pinned upstream at `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993`.

Secondary consumer:

```text
HG-MTH-010 — Clay coverage taxonomy
```

## Relationship to bsd-proof-program

Under HG-MTH-009, the current `bsd-proof-program` workstream structure is method-grade bootstrap apparatus:

| bsd-proof-program workstream | Role under HG-MTH-009 |
|---|---|
| A — Foundational typing | scope-development and claim-boundary typing |
| B — Mordell-Weil / Sha structure | future Component 1 apparatus |
| C — Tunnell-checkable cases | restricted fixture apparatus |
| D — p-adic L-functions | future Component 3 apparatus |
| E — empirical surveys | descriptive-grade only |
| F — promotion gates | audit and claim-boundary apparatus |

No workstream is positioned as apex closure.

## Boundary

This document does not:

- prove BSD-rank;
- prove BSD-strong;
- claim BSD Clay progress;
- assume `Sha` is finite;
- assume Bloch-Kato or Bloch-Beilinson;
- claim Bost-Connes or endomotive reformulation is proof;
- claim restricted-rank results solve full BSD;
- transfer methodology from RH, Hodge, Yang-Mills, P vs NP, or Navier-Stokes into BSD proof.

## Anti-seed cross-references

| Identifier | Applies because |
|---|---|
| `A-HG-MTH-001` | Universal Bridge does not transfer proofs. |
| `A-HG-MTH-002` | Catalan / mu2 fixture is not Clay progress. |
| `A-HG-MTH-003` | Fixture-grade and theorem-grade citations must not be mixed. |
| `A-HG-MTH-004` | Standard Conjectures and related conjectural apparatus are cited diagnostically, not assumed. |
| `A-HG-MTH-006` | Component apparatus diagnostic is not Clay-grade resolution. |
| `A-HG-MTH-007` | BSD-rank and BSD-strong have distinct structural status. |
| `A-HD-NC-001` | Reformulation is not proof. |
| `A-HD-SP-001` | Analog spectral data is not target spectral data. |
| `A-HD-TM-001` | Modular flow is not automatically physical or arithmetic time. |
| `A-HD-FND-001` | HD-FND identifiers are reference surface, not reproof. |

## Versioning

This is `HG-MTH-009 v1.0`. Any revision changing the BSD bridge factorization requires v2.0 and downstream migration review.
