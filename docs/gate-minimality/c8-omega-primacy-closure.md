# C-8 Closure — Omega Primacy Justification

Status: method-grade C-8 closure document; theorem-grade representation facts inside the adopted A2 path-beta convention.  
Owner: `SocioProphet/Heller-Godel`.  
Track: A2 gate-minimality, path beta convention, p=3 proof-character / gate-minimality framework.  
Depends on: `docs/gate-minimality/c8-cubic-invariant-condition.md`, `docs/gate-minimality/c7-closure-tranche-2-u2-minimality.md`.

## Purpose

This document closes the C-8 Omega-primacy justification for the A2 path-beta gate-minimality program.

The existing C-8 formulation document selected the defining-representation cubic invariant:

```text
Omega(v1, v2, v3) = det[v1 v2 v3] = epsilon_ijk v1^i v2^j v3^k
```

as the primary A2 condition-(v) invariant on the fundamental active sector `C^3`.

This closure document justifies that choice by recording three structural facts:

1. `Omega` is the unique-up-to-scale degree-3 totally alternating `SU(3)`-invariant on the defining representation `C^3`.
2. `Omega` is the natural degree-`n+1` continuation of the A1 degree-2 symplectic form on `C^2`, through the exterior-volume pattern `Lambda^(n+1)(C^(n+1))^*` for the `A_n` defining representation.
3. The adjoint cubic Casimir `C3(X)=d_abc x^a x^b x^c` is a derived readout of the same `A2` cubic invariant package through the fundamental matrix realization and Schur-Weyl-type tensor duality; it is not an independent primary gate primitive for C-8 unless a later active-sector document explicitly moves the active sector to adjoint coordinates.

This closes C-8 as an Omega-primacy obligation. It does not close the full A2 minimality theorem.

## Grade discipline and source standard

The representation-theoretic facts below are theorem-grade once the adopted A2 path-beta convention and fundamental active-sector realization are fixed.

The overall C-8 closure remains method-grade because A2 path-beta is still a method-grade program and not a promoted theorem-track result.

The source standard is ordinary representation theory of the classical groups and their tensor invariants. For citation discipline, use Fulton-Harris, *Representation Theory: A First Course*, especially the chapters on classical groups, tensor constructions, and the representation theory of `sl_3(C)` / `SU(3)`, together with standard classical-invariant-theory treatments of exterior powers and determinant representations.

No statement below promotes A2 to theorem-track.

## 1. Uniqueness of Omega on the defining representation

Let:

```text
V = C^3
```

with the standard defining action of `SU(3)`.

The degree-3 totally alternating tensors on `V` form:

```text
Lambda^3 V^*.
```

The invariant-space statement is:

```text
(Lambda^3 V^*)^(SU(3)) = Lambda^3 V^*.
```

The reason is that `Lambda^3 V^*` is the dual determinant representation:

```text
Lambda^3 V^* ~= det(V)^(-1).
```

For `SU(3)`, the determinant character is trivial:

```text
det(g) = 1 for every g in SU(3).
```

Therefore `SU(3)` acts trivially on `Lambda^3 V^*`. Since `dim_C(V)=3`, this exterior power is one-dimensional:

```text
dim_C Lambda^3 V^* = 1.
```

Thus the space of degree-3 totally alternating `SU(3)`-invariants is a one-dimensional line. Any nonzero generator is a valid `Omega`, and any two such generators differ by multiplication by a nonzero scalar.

The canonical scale is fixed by the standard ordered basis `e1,e2,e3`:

```text
Omega(e1, e2, e3) = 1.
```

With that normalization:

```text
Omega(v1, v2, v3) = det[v1 v2 v3]
                         = epsilon_ijk v1^i v2^j v3^k.
```

For `g in SU(3)`:

```text
Omega(gv1, gv2, gv3)
  = det(g) Omega(v1, v2, v3)
  = Omega(v1, v2, v3).
```

The load-bearing point is uniqueness, not mere existence:

```text
Omega is unique up to scale as the degree-3 totally alternating SU(3)-invariant on the fundamental representation C^3.
```

This is theorem-grade as a standard exterior-power / determinant-representation fact. Its use here remains method-grade because the surrounding A2 path-beta closure is method-grade.

## 2. Omega as the A2 continuation of the A1 condition-(v) form

For the `A_n` defining representation, the compact group is:

```text
SU(n+1)
```

acting on:

```text
C^(n+1).
```

The top exterior power is:

```text
Lambda^(n+1)(C^(n+1))^* ~= det^(-1) ~= 1
```

because the determinant character is trivial on `SU(n+1)`.

Thus the condition-(v) exterior invariant has the uniform form:

```text
Omega^(n)(v1, ..., v_(n+1)) = det[v1 v2 ... v_(n+1)].
```

Side-by-side:

| Case | Group | Fundamental active sector | Top exterior invariant | Degree | Condition-(v) reading |
|---|---|---|---|---|---|
| A1 | `SU(2)` | `C^2` | `Lambda^2(C^2)^*` | 2 | symplectic / area form `omega_A1(u,v)=det[u v]` |
| A2 | `SU(3)` | `C^3` | `Lambda^3(C^3)^*` | 3 | cubic volume form `Omega(v1,v2,v3)=det[v1 v2 v3]` |
| A_n | `SU(n+1)` | `C^(n+1)` | `Lambda^(n+1)(C^(n+1))^*` | `n+1` | determinant volume form on `n+1` vectors |

At A1, the condition-(v) invariant is the degree-2 alternating volume form:

```text
omega_A1(u, v) = det[u v].
```

In dimension two, this same alternating volume form is the standard symplectic form preserved by `SL(2,C)` and, after compact real-form restriction, by `SU(2)`.

Thus A1 condition (v) has two equivalent descriptions:

```text
preserve the symplectic pairing on C^2;
preserve the top exterior volume form in Lambda^2(C^2)^*.
```

A2 keeps the top-exterior-power description and advances one rank:

```text
C^2  ->  Lambda^2(C^2)^*  -> degree 2
C^3  ->  Lambda^3(C^3)^*  -> degree 3.
```

Therefore path beta at A2 is not introducing an unrelated invariant. It is applying the same condition-(v) construction one rank higher in the A-series defining representation.

Verdict:

```text
Omega on C^3 is the natural A2 degree-3 continuation of A1's degree-2 symplectic / exterior-volume form on C^2.
```

Non-claim:

```text
This establishes the condition-(v) exterior-invariant pattern at A_n. It does not formulate, prove, or close an A_n minimality theorem for n >= 3.
```

## 3. Relation between Omega and the adjoint cubic Casimir

C-8 distinguishes two cubic objects:

```text
Omega(v1, v2, v3) = epsilon_ijk v1^i v2^j v3^k
C3(X) = d_abc x^a x^b x^c,  X = x^a T_a in sl(3,C) or su(3)_C.
```

They live on different representation spaces:

| Object | Space | Symmetry type | C-8 role |
|---|---|---|---|
| `Omega` | fundamental `C^3` | alternating trilinear | primary active-sector gate primitive |
| `C3` | adjoint coordinates | symmetric cubic | derived readout / consistency invariant |

With Gell-Mann normalization:

```text
T_a = lambda_a / 2
Tr(T_a T_b) = (1/2) delta_ab
{T_a, T_b} = (1/3) delta_ab I_3 + d_abc T_c
```

one has, up to the declared normalization convention:

```text
Tr(X^3)  ~  d_abc x^a x^b x^c.
```

This trace expression is an invariant polynomial on the adjoint representation induced from the defining matrix representation.

The structural relation is Schur-Weyl-type: invariant tensors for the defining representation and its dual control the equivariant contractions from which both the fundamental determinant orientation and the adjoint polynomial readouts are assembled. In the A2 package, `Omega` supplies the fundamental determinant orientation, while the trace algebra of the same fundamental matrix realization supplies the symmetric adjoint cubic.

The primitive-degree signal is the same A-series fact:

```text
primitive invariant degrees for sl_(n+1): 2, 3, ..., n+1.
```

For `SU(2)` / A1, only the degree-2 primitive invariant appears, so there is no nonzero adjoint `d_abc` cubic. For `SU(3)` / A2, degree 3 is the first new primitive degree, and the adjoint cubic Casimir appears.

But the C-8 primary condition is still `Omega`, for three reasons:

1. `Omega` lives on the fundamental representation, which is where condition (v) is imposed in the A-series exterior-volume pattern.
2. `C3` lives on the adjoint, a different vector space obtained from the fundamental matrix realization and its invariant trace contractions.
3. The fundamental `3` versus antifundamental `3bar` orientation ambiguity is resolved at the `Omega` level by the strict convention in `docs/gate-minimality/c8-cubic-invariant-condition.md`. The adjoint readout inherits that declared orientation package; it does not independently choose it.

In short:

```text
Omega determines the primary active-sector orientation data. C3 is then constructible as an adjoint consistency/readout invariant from the same representation-theoretic package. Starting from C3 alone would not recover the selected fundamental orientation without additional convention choices.
```

However, C-8 must not overstate this relation. `Omega` and `C3` are not the same tensor, and `C3` is not imposed as an additional independent primary condition while the active sector remains the defining `C^3`.

Verdict:

```text
The adjoint cubic Casimir is a derived consistency/readout invariant for the A2 cubic package, not an independent C-8 primary gate primitive under the current fundamental active-sector convention.
```

## C-8 closure verdict

C-8 is closed at method grade as an Omega-primacy justification.

The closed C-8 rule is:

```text
For A2 path beta, condition (v) is imposed first on the defining active sector C^3 by requiring preservation of the selected determinant volume form Omega in Lambda^3(C^3)^*. The adjoint cubic Casimir C3 is recorded as a derived consistency/readout invariant unless a later document explicitly changes the active-sector realization to adjoint coordinates.
```

This closure supports the C-7 tranche-2 result:

```text
U(2)=S(U(2)xU(1)) and SU(3) both preserve Omega by determinant one.
```

It also prepares the later A2 minimality candidate statement, which may integrate:

```text
path-beta convention
C-7 connected-subgroup closure
C-8 Omega-primacy closure
```

into a single method-grade A2 candidate theorem statement.

## What remains after C-8

After this closure, the remaining A2 path-beta work is not to re-open Omega primacy. The next authorized mathematical integration step would be a separate A2 minimality candidate statement combining:

1. the adopted path-beta convention;
2. the C-7 admissible-candidate closure;
3. the C-8 Omega-primacy closure;
4. the claim-grade restrictions of the Heller-Godel proof-character framework.

That later integration is not performed here.

## Non-claims

This document closes C-8 as an Omega-primacy justification, not as final A2 minimality.

This document records theorem-grade representation-theoretic facts only inside the adopted A2 path-beta and fundamental-active-sector convention; the overall closure posture remains method-grade.

This document does not promote A2 to theorem-track. That requires a separate integration PR after C-7 and C-8 are both closed.

This document does not claim that C-8 alone determines the minimal subgroup.

This document does not claim that `Omega` and `C3` are identical tensors.

This document does not claim that the adjoint active-sector realization has been adopted.

This document does not formulate or prove an `A_n` theorem family. It only records the condition-(v) exterior-invariant pattern.

This document does not prove a nonabelian obstruction theory.

This document does not prove a Chern-class lift.

This document does not imply any `SU(3)` lattice gauge theory result.

This document does not cross into `SocioProphet/yang-mills` scope. The SU(3) gate-minimality work here is structurally disjoint from the `SocioProphet/yang-mills` SU(2) fixed-spacing lattice mass-gap proof-seed scope under the cofoundational architecture.
