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

## Grade discipline

The representation-theoretic facts below are theorem-grade once the adopted A2 path-beta convention and fundamental active-sector realization are fixed.

The overall C-8 closure remains method-grade because A2 path-beta is still a method-grade program and not a promoted theorem-track result.

No statement below promotes A2 to theorem-track.

## 1. Uniqueness of Omega on the defining representation

Let:

```text
V = C^3
```

with the standard defining action of `SU(3)`.

The alternating degree-3 tensors on `V` form the one-dimensional line:

```text
Lambda^3 V^*.
```

Since `dim_C(V)=3`, every totally alternating trilinear form on `V` is a scalar multiple of a chosen basis element of `Lambda^3 V^*`.

Choose the determinant basis:

```text
Omega(v1, v2, v3) = det[v1 v2 v3].
```

For `g in SU(3)`:

```text
Omega(gv1, gv2, gv3)
  = det(g) Omega(v1, v2, v3)
  = Omega(v1, v2, v3),
```

because:

```text
det(g)=1.
```

Therefore `Omega` spans the `SU(3)`-invariant line inside `Lambda^3 V^*`.

Verdict:

```text
Omega is the unique-up-to-scale totally alternating degree-3 SU(3)-invariant on the defining representation C^3.
```

## 2. Omega as the A2 continuation of the A1 condition-(v) form

At A1, the active-sector representation is the defining representation:

```text
C^2.
```

The condition-(v) invariant is the degree-2 alternating volume form:

```text
omega_A1(u, v) = det[u v].
```

In dimension two, this same alternating volume form is also the standard symplectic form preserved by `SL(2,C)` and, after the compact real-form convention, by `SU(2)`.

Thus A1 condition (v) can be read in two equivalent ways:

```text
preserve the symplectic pairing on C^2;
preserve the top exterior volume form in Lambda^2(C^2)^*.
```

A2 keeps the second reading and advances the exterior degree by one:

```text
C^2  ->  Lambda^2(C^2)^*
C^3  ->  Lambda^3(C^3)^*.
```

The A-series schematic pattern is therefore:

```text
A_n defining representation: C^(n+1)
condition-(v) exterior invariant: Lambda^(n+1)(C^(n+1))^*
degree: n+1
```

For `n=1`, the degree is `2`. For `n=2`, the degree is `3`.

C-8 does not formulate an `A_n` theorem. It only records that, under path beta, A2 is the first point where the condition-(v) exterior-volume invariant becomes cubic.

Verdict:

```text
Omega on C^3 is the natural A2 degree-3 continuation of A1's degree-2 symplectic / volume form on C^2.
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

The adjoint cubic is not foreign to the fundamental representation. It is obtained from the fundamental matrix realization of `sl(3,C)` through invariant tensor algebra.

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

Schur-Weyl-type duality supplies the structural reason: invariant tensors for the defining representation and its dual control the equivariant tensor contractions from which the adjoint representation and its invariant polynomial readouts are built. In the A2 package, the fundamental determinant orientation and the fundamental matrix trace calculus belong to the same representation-theoretic invariant system.

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

This document does not prove final A2 minimality.

This document does not promote A2 to theorem-track.

This document does not claim that C-8 alone determines the minimal subgroup.

This document does not claim that `Omega` and `C3` are identical tensors.

This document does not claim that the adjoint active-sector realization has been adopted.

This document does not formulate or prove an `A_n` theorem family.

This document does not prove a nonabelian obstruction theory.

This document does not prove a Chern-class lift.

This document does not imply any `SU(3)` lattice gauge theory result.

This document does not cross into `SocioProphet/yang-mills` scope.
