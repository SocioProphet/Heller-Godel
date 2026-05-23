# C-7 Closure Tranche 2 — U(2) Admissibility and Minimality

Status: method-grade C-7 closure tranche.  
Owner: `SocioProphet/Heller-Godel`.  
Track: A2 gate-minimality, path beta convention, p=3 proof-character / gate-minimality framework.  
Depends on: `docs/gate-minimality/c7-su3-subgroup-classification-scope.md`, `docs/gate-minimality/c8-cubic-invariant-condition.md`, `docs/gate-minimality/c7-closure-tranche-1-easy-eliminations.md`.

## Purpose

This tranche applies the C-8 cubic-invariant condition to the remaining C-7 candidates after tranche 1.

The remaining candidates are:

```text
U(2) = S(U(2) x U(1))
SU(3)
```

The result is:

```text
U(2) is admissible.
SU(3) is admissible.
U(2) is the minimal admissible connected subgroup in the C-7 candidate list under the adopted path-beta filters.
```

This closes C-7 at method grade, modulo the path-beta framework convention and the accepted closed-connected-subgroup classification surface.

## Grade discipline

The determinant-preservation calculations below are theorem-grade once the adopted path-beta filters and C-7 candidate list are accepted.

The overall tranche remains method-grade because the path-beta gate-minimality framework is still method-grade and A2 has not been promoted to theorem-track.

No claim here proves A2 minimality as a final theorem.

## Adopted active cubic invariant

C-8 selects the defining-representation volume form as primary:

```text
Omega(v1, v2, v3) = det[v1 v2 v3] = epsilon_ijk v1^i v2^j v3^k
```

For any `g in SL(3,C)`:

```text
Omega(gv1, gv2, gv3) = det(g) Omega(v1, v2, v3)
```

Therefore every `g in SU(3)` preserves `Omega`, because:

```text
det(g) = 1
```

This means C-8 preservation is necessary but not sufficient to select the full `SU(3)` group among its subgroups. C-7 minimality depends on the full path-beta filter package: center, nonabelian active witness, spatial faithfulness, and C-8.

## U(2) embedding convention

Use the standard embedding:

```text
g = [[A, 0],
     [0, conjugate(det A)]],  A in U(2)
```

Equivalently:

```text
g = diag(A, overline(det A))
```

Then:

```text
det(g) = det(A) overline(det A) = 1
```

so:

```text
g in SU(3)
```

This subgroup is the standard maximal proper connected subgroup:

```text
S(U(2) x U(1)) subset SU(3)
```

## Lemma 1 — U(2) preserves Omega

Let:

```text
g = diag(A, overline(det A)) in S(U(2) x U(1))
```

For any `v1, v2, v3 in C^3`:

```text
Omega(gv1, gv2, gv3)
  = det[gv1 gv2 gv3]
  = det(g) det[v1 v2 v3]
  = 1 * Omega(v1, v2, v3)
  = Omega(v1, v2, v3)
```

Thus `U(2)=S(U(2)xU(1))` satisfies the C-8 cubic-invariant preservation condition.

## Lemma 2 — U(2) passes the easy C-7 filters

`U(2)=S(U(2)xU(1))` is closed and connected.

It contains the scalar center of `SU(3)`:

```text
Z(SU(3)) = {I_3, omega I_3, omega^2 I_3}
```

because scalar elements can be represented inside the `S(U(2)xU(1))` form.

It is nonabelian because its `U(2)` block contains an `SU(2)` factor with nonzero commutators.

It acts faithfully in the standard defining representation inherited from `SU(3)`.

Therefore `U(2)` passes the easy C-7 filters and the C-8 cubic-invariant preservation check.

Verdict:

```text
U(2)=S(U(2)xU(1)) is admissible.
```

## Lemma 3 — Full SU(3) preserves Omega

For `g in SU(3)`:

```text
det(g) = 1
```

Therefore:

```text
Omega(gv1, gv2, gv3) = Omega(v1, v2, v3)
```

Full `SU(3)` also contains its scalar center, is nonabelian, and acts faithfully on the defining representation.

Verdict:

```text
SU(3) is admissible.
```

## Lemma 4 — No smaller connected candidate remains admissible

Tranche 1 eliminated the following proper connected candidates:

```text
{1}
rank-1 tori
T^2
standard block SU(2)
principal SO(3)
```

Those eliminations used the center and nonabelian-active-witness filters without invoking C-8.

The only proper connected candidate left by the C-7 candidate table is:

```text
U(2)=S(U(2)xU(1))
```

Since this tranche proves `U(2)` admissible and tranche 1 eliminates all smaller connected candidates in the list, `U(2)` is minimal among admissible connected subgroups in the C-7 candidate table.

This is a minimality statement relative to the adopted candidate list and filters. It is not a final A2 theorem.

## C-7 closure verdict

C-7 is closed at method grade with the following candidate verdicts:

| Candidate subgroup type | C-7 verdict |
|---|---|
| Trivial subgroup `{1}` | eliminated |
| Rank-1 tori | eliminated |
| Maximal torus `T^2` | eliminated |
| Standard block `SU(2)` | eliminated |
| Principal irreducible `SO(3)` | eliminated |
| `U(2)=S(U(2)xU(1))` | admissible; minimal connected admissible candidate |
| Full `SU(3)` | admissible; not minimal |

Thus, under the path-beta C-7 filters:

```text
U(2)=S(U(2)xU(1)) is the minimal admissible connected subgroup of SU(3).
```

## What remains after C-7

C-7 is closed as an admissibility-classification obligation.

A2 is still not theorem-track because the program still requires at least:

1. a theorem-grade statement of the full A2 gate-minimality target;
2. verification that the C-8 cubic-invariant condition is sufficient for the intended active-sector equivalence relation;
3. integration with the broader `chi_p` / `zeta_p` / proof-character framework at `p=3`.

## Non-claims

This document does not prove A2 minimality as a final theorem.

This document does not promote A2 to theorem-track.

This document does not claim `SU(3)` itself is minimal.

This document does not claim that C-8 alone determines the minimal subgroup.

This document does not imply any `SU(3)` lattice gauge theory result.

This document does not cross into `SocioProphet/yang-mills` scope.
