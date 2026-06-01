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
G = SU(3)
Omega in Lambda^3 V^*
Omega(v1,v2,v3) = det[v1 v2 v3]
```

For `g in SU(3)`:

```text
Omega(gv1, gv2, gv3) = det(g) Omega(v1,v2,v3) = Omega(v1,v2,v3)
```

because `det(g)=1`.

Since `Lambda^3 V^*` is one-dimensional, any totally alternating trilinear form on `V` is a scalar multiple of `Omega`. Thus `Omega` is unique up to scale among degree-3 totally alternating invariant forms on the defining representation.

This is the exact A2 analogue of the A1 exterior/symplectic volume primitive, but in degree 3 rather than degree 2.

## 2. A1 to A2 continuation

For A1:

```text
V_2 = C^2
Lambda^2 V_2^*
```

is one-dimensional, and the canonical alternating degree-2 form gives the symplectic / determinant gate primitive.

For A2:

```text
V_3 = C^3
Lambda^3 V_3^*
```

is one-dimensional, and the canonical alternating degree-3 form is `Omega`.

Thus the continuation pattern is:

```text
A1: Lambda^2(C^2)^*
A2: Lambda^3(C^3)^*
An: Lambda^(n+1)(C^(n+1))^*
```

within the defining representation.

This supports the C-8 choice of `Omega` as primary when the active sector is explicitly the A2 defining representation. It does not assert an unrestricted `A_n` theorem family for the whole Heller-Godel program.

## 3. Adjoint cubic Casimir as derived readout

The adjoint representation of `su(3)` has the symmetric cubic invariant:

```text
C3(X) = d_abc x^a x^b x^c
```

This object is central in SU(3) representation theory and is the familiar cubic Casimir.

However, under the adopted path-beta convention, the active sector for C-8 is the defining representation `C^3`, not the adjoint representation.

Therefore:

```text
Omega is primary for C-8.
C3 is a derived consistency/readout invariant for adjoint-coordinate diagnostics.
```

The reason is not that `C3` is unimportant. The reason is that the primitive gate datum must live on the active sector fixed by the path-beta convention.

If a later branch changes the active sector to adjoint coordinates, then `C3` may become primary in that branch. That would be a different gate formulation and must be explicitly documented.

## 4. Closure statement

C-8 required a primary A2 cubic invariant condition.

The closure is:

```text
C-8 primary gate primitive = Omega in Lambda^3(C^3)^*
```

with adjoint cubic Casimir treated as:

```text
derived readout / consistency invariant
```

This closes the C-8 Omega-primacy justification for the A2 path-beta gate-minimality program.

## 5. Nonclaims

This document does not claim:

1. final A2 minimality;
2. theorem-track promotion of A2 path-beta;
3. an `A_n` theorem family;
4. replacement of adjoint invariant theory;
5. any Yang-Mills consequence;
6. any physical gauge-theory result.

## 6. Downstream use

Downstream references may cite this document only for:

```text
C-8 Omega primacy in the defining A2 active sector.
```

They must not cite it as a proof of:

```text
A2 minimality theorem
A_n generalization
Yang-Mills gap
Hodge/HG bridge theorem
```

## 7. Status

C-8 Omega-primacy justification is closed for the current method-grade A2 path-beta gate-minimality program.
