# HG-MTH-007 — Universal Bridge: Yang-Mills Gauge Domain Extension

Identifier: `HG-MTH-007`  
Distance tier: Framework-method (Tier 3)  
Status: Active after this PR  
Heller-Dirac citation pin: `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993`  
Anti-seed: `A-HG-MTH-001`, `A-HG-MTH-002`, `A-HG-MTH-003`, `A-HG-MTH-004`, `A-HG-MTH-005`, `A-HG-MTH-006`

## Status under the Universal Bridge

`HG-MTH-005` established the Universal Bridge as method-grade structural analogy with factorization:

```text
B = (M, R, A)
```

where `M` is the mean-field or smooth-expected structure, `R` is the residual obstruction, and `A` is the apex obstruction package.

`HG-MTH-006` instantiated Hodge. `HG-MTH-008` instantiated P vs NP. This document instantiates the Yang-Mills mass-gap domain.

This document is method-grade only. It does not transfer proofs.

## Heller-Dirac dependency surface

This is Heller-Godel framework content whose mathematical vocabulary cites Heller-Dirac reference-surface objects at a pinned commit:

```text
SocioProphet/Heller-Dirac @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993
```

Cited Heller-Dirac objects:

- `HD-FND-001` — spectral triple base structure.
- `HD-FND-003` — real structure and KO-dimension table.
- `HD-FND-006` — spectral action principle.
- `HD-FND-010` — Hopf-algebra action on spectral triples.
- `A-HD-FT-001` — axioms are not construction.
- `A-HD-HA-001` — Hopf scaffold encoding is not analytic-control proof.
- `A-HD-NC-001` — reformulation is not proof.
- `A-HD-SP-001` — analog spectral data is not target spectral data.
- `A-HD-FND-001` — reference surface is not reproof.

Heller-Godel remains the framework-core repository; these are content citations, not a repository-level upstream dependency change.

## Clay Yang-Mills mass-gap statement

The Clay Yang-Mills problem asks for a non-trivial relativistic quantum Yang-Mills theory on four-dimensional Euclidean / Minkowski spacetime, satisfying the appropriate Wightman or Osterwalder-Schrader axioms, for a compact simple gauge group such as `SU(N)`, together with a mass gap above the vacuum.

The problem has two inseparable requirements:

1. existence of the continuum quantum field theory;
2. positive mass gap in the spectrum above the vacuum.

A lattice finite-volume, fixed-spacing, or strong-coupling result is not by itself a Clay solution.

## Yang-Mills bridge factorization

Let `G` be a compact simple Lie group, typically `SU(N)` for `N >= 2`.

### Mean-field M

```text
M_YM(G) = classical Yang-Mills action minimum modulo gauge
```

The classical action is built from a connection `A`, curvature `F_A`, and the Yang-Mills functional:

```text
S_YM[A] = integral ||F_A||^2
```

The mean-field is the smooth classical gauge-theoretic structure: connections, curvature, gauge orbits, instantons, and classical action minima. This is well-developed differential geometry. The Clay problem concerns the quantum continuum theory, not merely the classical mean field.

### Residual R

```text
R_YM(G) = Spec(H_YM) \ {0}
```

where `H_YM` is the quantum Hamiltonian if the theory exists. The mass-gap condition asks:

```text
inf R_YM(G) > 0
```

The residual is the quantum spectrum's separation from the vacuum. The mass gap is a spectral property of the continuum quantum theory.

### Apex obstruction A

The Yang-Mills apex obstruction is a compiled triple:

```text
A_YM in ConstructiveQFT ∪ ContinuumLimit ∪ SpectralActionRealization
```

#### Component 1 — Constructive QFT existence

Wightman and Osterwalder-Schrader axioms specify what a QFT is. They do not construct it. A Clay-grade Yang-Mills result must construct a continuum non-abelian gauge theory satisfying the relevant axioms.

Per `A-HD-FT-001`, axiomatization is not construction.

#### Component 2 — Continuum limit of lattice gauge theory

Wilson lattice gauge theory is rigorous at fixed lattice spacing. The open problem is to take the continuum limit while preserving non-triviality, Osterwalder-Schrader positivity, gauge invariance, and the mass gap.

The `yang-mills` repo's v0.14.4 work sits here: method-level Wilson-lattice apparatus for `SU(2)` at fixed spacing and fixed strong-coupling regime. It is not the continuum Clay result.

#### Component 3 — Spectral-action realization

The spectral action route, through `HD-FND-006`, realizes classical Yang-Mills sectors in the noncommutative-geometric Standard Model setting. `HD-FND-003` supplies the KO-dimension table, including KO-dim 6 for the Standard Model finite triple convention.

This is a classical-action and spectral-geometry framework. It does not construct the quantum field theory or prove the mass gap.

`HD-FND-010` supplies Hopf-action vocabulary for renormalization scaffolds such as Connes-Kreimer. Per `A-HD-HA-001`, Hopf organization is not non-perturbative renormalizability proof.

## Shared missing machinery diagnosis

Yang-Mills shares the Universal Bridge diagnosis with RH, Hodge, and NP:

```text
The problem requires apparatus operating below the level where current proof techniques have grip.
```

For Yang-Mills, current techniques include classical gauge geometry, finite-lattice constructions, perturbation theory, and axiomatic QFT targets. The missing apparatus is a non-perturbative continuum construction with mass gap, simultaneously satisfying the axioms and preserving the spectral structure.

This is structurally cognate with RH's missing positivity site, Hodge's missing algebraic-cycle certification machinery, and NP's missing non-natural non-relativizing non-algebrizing technique. It is not the same tool and no proof transfers.

## Method-level apparatus landscape

### Wilson lattice approach

The `yang-mills` repo's v0.14.4 result is positioned as Component 2 method-grade apparatus: fixed lattice spacing, `SU(2)`, and a strong-coupling window. It is not the Clay mass gap.

### Spectral action approach

The Connes-Chamseddine spectral action is positioned as Component 3 method-grade apparatus: a classical action from spectral data. It is not constructive QFT existence.

### Constructive QFT approach

Constructive methods specify possible routes to Component 1. They have achieved lower-dimensional scalar examples, but four-dimensional non-abelian Yang-Mills remains open.

### Factorization-algebra and Hopf-scaffold approaches

These organize perturbative and categorical structures. They are method-grade apparatus, not Clay-grade construction.

## Consumer surface

Primary consumer:

```text
SocioProphet/yang-mills
```

Downstream citation form:

```text
[HG-MTH-007 @ <merged-Heller-Godel-commit-sha>]
[HD-FND-001 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
[HD-FND-006 @ e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993]
```

A follow-up `yang-mills` PR should advance its Heller-Godel pin, add `HG-MTH-007`, add `A-HG-MTH-006`, and add Heller-Dirac as a second pinned upstream at `e1d7c863f4e0fc6e5e2ab485370cc75b2dba3993`.

Secondary consumer:

```text
HG-MTH-010 — Clay coverage taxonomy
```

## Relationship to yang-mills v0.14.4

Under HG-MTH-007, the yang-mills v0.14.4 manuscript work is Component 2 method-grade apparatus. Its own scope remains intact:

- gauge group: `SU(2)`;
- lattice: Wilson lattice on `Z^4`;
- lattice spacing: fixed;
- coupling: strong-coupling window;
- result: transfer-matrix gap in the Osterwalder-Seiler Hilbert-space setting.

This is not a continuum construction and not Clay-grade mass gap. The bridge preserves that boundary.

## Boundary

This document does not:

- prove Yang-Mills existence;
- prove Yang-Mills mass gap;
- claim Clay progress;
- claim that `yang-mills` v0.14.4 is Clay-grade;
- claim spectral action constructs the quantum theory;
- claim Hopf-scaffold renormalization proves non-perturbative renormalizability;
- transfer methodology from RH, Hodge, NP, BSD, or Navier-Stokes into YM proof.

## Anti-seed cross-references

| Identifier | Applies because |
|---|---|
| `A-HG-MTH-001` | Universal Bridge does not transfer proofs. |
| `A-HG-MTH-002` | Catalan / mu2 fixture is not Clay progress. |
| `A-HG-MTH-003` | Fixture-grade and theorem-grade citations must not be mixed. |
| `A-HG-MTH-004` | Standard Conjectures diagnostic discipline applies by analogy. |
| `A-HG-MTH-005` | Barrier diagnosis is not a circumvention recipe. |
| `A-HG-MTH-006` | Component apparatus is not Clay-grade YM mass-gap resolution. |
| `A-HD-FT-001` | Axioms are not construction. |
| `A-HD-HA-001` | Hopf scaffold encoding is not analytic-control proof. |
| `A-HD-NC-001` | Reformulation is not proof. |
| `A-HD-SP-001` | Analog spectral data is not target spectral data. |
| `A-HD-FND-001` | HD-FND identifiers are reference surface, not reproof. |

## Versioning

This is `HG-MTH-007 v1.0`. Any revision changing the YM bridge factorization requires v2.0 and downstream migration review.
