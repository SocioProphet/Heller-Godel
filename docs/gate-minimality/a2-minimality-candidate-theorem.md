# HG-MTH-011 — A2 Minimality Candidate-Theorem

Identifier: `HG-MTH-011`  
Distance tier: Framework-method / gate-minimality method result  
Status: Candidate; P3 lift active after `HG-MTH-021`; `HG-FND-001` normalized.  
Grade: method-grade modulo five remaining candidate Tier-1 surfaces after P3 closure and `HG-FND-001` normalization; historical grade was method-grade as candidate theorem.  
Owner: `SocioProphet/Heller-Godel`  
Track: A2 gate-minimality, path-beta convention, C-7 / C-8 closure integration

## 1. Statement

Theorem (`HG-MTH-011`: A2 Minimality, Candidate). Under the path-beta framework for A2 (gauge group `SU(3)`, central element selection from `mu_3`, condition (v) = preservation of the cubic invariant `Omega` on the fundamental `C^3` under the strict `3`-orientation), the minimal admissible closed connected subgroup of `SU(3)` is `U(2)=S(U(2) x U(1))`.

Specifically:

1. `U(2)=S(U(2) x U(1))` satisfies all path-beta admissibility conditions: it contains the center `mu_3` via its `U(1)` complement carrying `mu_3`, it is non-abelian through the `SU(2)` block, and it preserves `Omega` by the determinant-one calculation.
2. Every proper closed connected subgroup of `SU(3)` on the candidate list, up to conjugacy, other than `U(2)` and `SU(3)` itself fails at least one path-beta admissibility condition.
3. `SU(3)` is admissible but not minimal in the candidate list.

## 2. Argument structure

### 2.1 C-7 closure

C-7 was closed by PR #73 at merge SHA `c25dd3b5451fc73e3a3705fe8c272ce185454244` and PR #74 at merge SHA `98e2ceac5646c02b3efd7a8ed48c0ec43ab7f8f6`.

Those closures eliminate the trivial subgroup, rank-1 tori, maximal torus `T^2`, the standard `SU(2)` block, and the principal irreducible `SO(3)` case. They then treat `U(2)=S(U(2) x U(1))` and `SU(3)`. The resulting candidate-list minimality verdict is `U(2)=S(U(2) x U(1))`.

### 2.2 C-8 closure

C-8 was closed by PR #75 at merge SHA `e940da419474e987b87755d386f196fa34ed580f`.

C-8 records that `Omega` is the correct primary invariant for condition (v) at A2. The typing is covariant:

```text
(Lambda^3 V^*)^(SU(3)) = Lambda^3 V^*, where V = C^3.
```

This follows from `Lambda^3 V^* ~= det(V)^(-1)` and `det(g)=1` for `g in SU(3)`. Hence `Omega` is unique up to scale as the degree-3 totally alternating invariant on the fundamental, with scale fixed by `Omega(e1,e2,e3)=1`.

C-8 also records the A-series exterior-volume pattern `Lambda^(n+1)(C^(n+1))^*`, making A2 the cubic continuation of A1's exterior / symplectic invariant. The adjoint cubic Casimir `C3(X)=d_abc x^a x^b x^c` is a derived readout, not an independent primary; it inherits the strict fundamental `3` orientation selected by `Omega`.

### 2.3 Path-beta framework

The path-beta framework supplies the adopted A2 convention: central element source `mu_3`, condition (v) source `Omega in Lambda^3(C^3)^*`, and active-sector representation `C^3` with strict `3`-orientation. This convention is method-grade and was adopted through the prior Heller-Dirac path decision and Heller-Godel relocation sequence.

## 3. Grade chain

| Object | Grade | Source |
| --- | --- | --- |
| Path-beta framework adoption | method-grade | HG path-beta adoption material |
| C-7 candidate-list closure | theorem-grade modulo path-beta | PRs #73 and #74 |
| C-8 Omega-primacy closure | theorem-grade modulo path-beta | PR #75 |
| A2 minimality candidate-theorem, initial state | method-grade as candidate theorem | `HG-MTH-011` initial declaration |
| A2 minimality candidate-theorem after P3 closure | method-grade modulo six candidate Tier-1 surfaces | `HG-MTH-021` P3 closure assembly |
| A2 minimality candidate-theorem after `HG-FND-001` normalization | **method-grade modulo five remaining candidate Tier-1 surfaces** | this PR |

Overall grade after `HG-FND-001` normalization: method-grade modulo five remaining candidate Tier-1 surfaces. This is not theorem-track promoted.

The remaining candidate surfaces are:

```text
HG-FND-002
HG-FND-003
HG-VOC-006
HG-FND-006
HG-FND-007
```

`HG-FND-001` is now normalized as the restricted proof grammar and declared-statistics foundation. This reduces the P3 cumulative modulo chain but does not promote `HG-MTH-011` to theorem-grade.

## 4. Comparison to A1

At A1, the minimal admissible subgroup under the analogous framework is `Spin(3) ~= SU(2)` with condition (v) = symplectic preservation `omega_A1` on `C^2`. At A2, the minimal admissible subgroup under path-beta is `U(2)=S(U(2) x U(1))` with condition (v) = cubic preservation `Omega` on `C^3`. The structural pattern is that at `A_n`, condition (v) is preservation of `Lambda^(n+1)(C^(n+1))^*`, and the minimal admissible subgroup is observed as the stabilizer of the standard branching. This is only a pattern observation; no theorem about `A_n` minimality is claimed.

## 5. Non-claims

1. Not promoted to theorem-track. After `HG-FND-001` normalization it is method-grade modulo five remaining candidate Tier-1 surfaces.
2. Does not establish A2 minimality absolutely; only relative to the closed-connected candidate list up to conjugacy and path-beta framework.
3. Does not claim path-beta is the uniquely correct A2 framework. Path-alpha was demoted but not refuted.
4. Does not extend to `A_n` for `n >= 3`.
5. Does not normalize the five remaining Tier-1 candidate surfaces required by the post-P3 chain: `HG-FND-002`, `HG-FND-003`, `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`.
6. Does not close P1 path-beta uniqueness / characterization.
7. Does not close P2 candidate-list exhaustion.
8. Does not cross into the separate SU(2) lattice mass-gap program scope.
9. Does not authorize Heller-Einstein realization-question work to cite A2 minimality as theorem-grade input.
10. Does not prove a Chern-class lift, nonabelian obstruction theory, or cognitive theory of recognition.

## 6. Future obligations for theorem-track promotion

(P1) Path-beta uniqueness or characterization. Prove that any A2 framework satisfying a declared axiomatization selects path-beta, or prove that path-beta is canonical under a declared criterion. This would lift path-beta from method-grade to theorem-grade and lift A2 minimality with it.

(P2) Candidate-list exhaustion. Prove that the closed-connected subgroup candidate list up to conjugacy is exhaustive for the relevant minimality equivalence on `SU(3)`, so that no closed connected subgroup outside the list is admissible and strictly smaller than `U(2)=S(U(2) x U(1))`. This lifts candidate-list minimality to absolute minimality and is independent strengthening.

(P3) Pipeline integration. Attach A2 minimality to Heller-Godel's `chi_p` / proof-character framework at `p=3`. P3 is closed by `HG-MTH-021`, which assembles `HG-MTH-014`, `HG-MTH-016`, `HG-MTH-018`, and `HG-MTH-020`.

P3 closure lifted A2 minimality from method-grade as candidate theorem to method-grade modulo six candidate Tier-1 surfaces. `HG-FND-001` normalization reduces that to five remaining candidate Tier-1 surfaces. It does not promote A2 minimality to theorem-grade. Full theorem-grade promotion requires normalization or discharge of the remaining five candidate Tier-1 surfaces, or a separate authorized promotion route through P1, P2, or another explicitly scoped proof path.

## 7. Source provenance

| Source | Role | Merge SHA |
| --- | --- | --- |
| PR #73 | C-7 tranche 1 eliminations | `c25dd3b5451fc73e3a3705fe8c272ce185454244` |
| PR #74 | C-7 tranche 2 `U(2)` / `SU(3)` closure | `98e2ceac5646c02b3efd7a8ed48c0ec43ab7f8f6` |
| PR #75 | C-8 Omega-primacy closure | `e940da419474e987b87755d386f196fa34ed580f` |
| PR #82 | P3.a restricted proof grammar closure | `96f2a9015fb6bc3b62744409660e4855ed9c4014` |
| PR #86 | P3.b canonical statistic and generating function closure | `bc54fbeb5d74bdbedcc8c3d7aee85130a2ca63ac` |
| PR #90 | P3.c Puiseux singularity and `chi_3` closure | `75bc41930a4f9bd6736d4d54b8dcdf2605c520db` |
| PR #94 | P3.d `zeta_3` carry defect and `U(2)` correspondence closure | `389e473daa29ffb4c730d9c928eee7d533f22939` |
| PR #96 | P3 closure assembly `HG-MTH-021` | `c331c2bfa562b463a4f920022d2f79c247a7a665` |

Framework context is supplied by Heller-Godel's README, framework-core claim grammar, distance classification, and gate-minimality documents. Standard representation-theoretic facts follow the established source discipline; full bibliographic hardening remains deferred to a separate non-blocking PR.

## 8. Identifier and registry

This document assigns `HG-MTH-011` to the A2 minimality candidate-theorem and records its post-P3 and post-`HG-FND-001` grade lifts.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. It defines the `HG-{LAYER}-{NNN}` pattern and requires any PR adding or materially updating an `HG-*` identifier to update the registry or `docs/framework-core/distance-classification.md` in the same PR. This PR therefore updates `docs/framework-core/claim-grammar.md` and `docs/framework-core/distance-classification.md` to register normalized `HG-FND-001` and the reduced five-surface modulo chain.
