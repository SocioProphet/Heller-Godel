# C-7 Closure Tranche 1 — Easy Eliminations

Status: method-grade admissibility verdict tranche; C-7 not fully closed.  
Owner: `SocioProphet/Heller-Godel`.  
Track: A2 gate-minimality, path beta convention, p=3 proof-character / gate-minimality framework.  
Depends on: `docs/gate-minimality/c7-su3-subgroup-classification-scope.md`, `docs/gate-minimality/c8-cubic-invariant-condition.md`.

## Purpose

This tranche begins substantive C-7 closure work by proving the easy inadmissibility verdicts from the C-7 candidate table.

It does not close all of C-7. The remaining major proper connected candidate is:

```text
U(2) = S(U(2) x U(1))
```

whose final verdict depends on C-8.

## Adopted A2 filters

The path beta A2 convention uses:

```text
SU(3) + central Z/3 + cubic invariant
```

The active C-7 filters are:

1. closed and connected subgroup of `SU(3)`;
2. compatibility with the scalar central `Z/3 = {I_3, omega I_3, omega^2 I_3}`;
3. compatibility with the C-8 cubic-invariant condition;
4. spatial faithfulness for the A2 active sector;
5. no collapse back to a path-alpha `Spin(3)` encoding.

This tranche applies filters 1, 2, 4, and 5 where they are already decisive.

## Verdict table

| Candidate subgroup type | Verdict in this tranche | Reason |
|---|---|---|
| Trivial subgroup `{1}` | eliminated | Fails central `Z/3`, nonabelian active-sector, and spatial faithfulness requirements. |
| Rank-1 torus `U(1)` root-circle embeddings | eliminated | Abelian and dimension 1; ordinary root circles miss the full scalar center, and center-passing special circles still fail nonabelian active-sector and spatial faithfulness requirements. |
| Maximal torus `T^2` | eliminated | Contains the scalar center but is abelian; cannot realize the full nonabelian A2 active-sector gate. |
| Standard block `SU(2)` | eliminated | Misses scalar `omega I_3`, fixes a line in `C^3`, and collapses toward a path-alpha-style `SU(2)` encoding. |
| Principal irreducible `SO(3)` | eliminated | The spin-1 image kills the `SU(2)` center and does not contain scalar `omega I_3`; it is a path-alpha comparison surface, not path-beta A2 admissible. |
| `U(2)=S(U(2)xU(1))` | not decided | Contains scalar `Z/3`; final verdict requires C-8. |
| Full `SU(3)` | not decided as theorem | Expected admissible candidate, but final A2 theorem status requires complete C-7/C-8 closure. |

## Lemma 1 — Trivial subgroup eliminated

The trivial subgroup contains only:

```text
{I_3}
```

It does not contain `omega I_3` or `omega^2 I_3`. Therefore it fails the central `Z/3` requirement.

It also cannot act faithfully on the A2 active sector in a way that realizes the path beta nonabelian gate.

Verdict: eliminated.

## Lemma 2 — Rank-1 tori eliminated

A rank-1 torus is abelian and one-dimensional. Ordinary root-circle embeddings do not contain the full scalar center `Z/3` as a distinguished path beta central datum.

Even if a special circle embedding is chosen so that scalar center elements lie inside the circle, the candidate remains abelian and one-dimensional. It cannot carry the full nonabelian `SU(3)` active-sector gate required by the adopted A2 convention.

Verdict: eliminated.

## Lemma 3 — Maximal torus eliminated

The maximal torus `T^2` contains the scalar center of `SU(3)`, so center containment alone does not eliminate it.

However, `T^2` is abelian. The adopted path beta convention requires the A2 active-sector gate to retain the nonabelian `SU(3)` structure associated with the cubic invariant. An abelian torus can preserve restricted diagonal data but cannot realize the full nonabelian active-sector gate.

Verdict: eliminated.

This elimination uses nonabelian active-sector admissibility, not center containment.

## Lemma 4 — Standard block SU(2) eliminated

The standard block embedding is:

```text
A in SU(2) -> diag(A, 1) in SU(3)
```

Its elements have third diagonal entry `1`. The scalar element:

```text
omega I_3 = diag(omega, omega, omega)
```

has third diagonal entry `omega`, where `omega != 1`.

Therefore:

```text
omega I_3 notin standard block SU(2)
```

The standard block also preserves a splitting:

```text
C^3 = C^2 + C
```

and therefore fixes a line. This is incompatible with the adopted path beta target as a full `SU(3)` active-sector gate.

Verdict: eliminated.

## Lemma 5 — Principal SO(3) eliminated

The principal SU(2)-type embedding in dimension 3 is the spin-1 representation. Its image is naturally read as an `SO(3)` subgroup of `SU(3)`.

The center of `SU(2)` acts trivially in the spin-1 representation. Consequently, the image does not contain the scalar order-3 center of `SU(3)`.

Equivalently, the real `SO(3)` subgroup does not contain:

```text
omega I_3
```

with non-real `omega` satisfying `omega^3 = 1`, `omega != 1`.

Verdict: eliminated.

This subgroup remains useful only as a path-alpha comparison surface.

## Remaining candidates

After this tranche, the only proper connected candidate still requiring a substantive verdict is:

```text
U(2) = S(U(2) x U(1))
```

It contains the scalar `Z/3`, so center containment cannot eliminate it. Its final verdict requires C-8: preservation of the selected A2 cubic invariant in the active-sector realization.

Full `SU(3)` remains the expected admissible candidate, but that status is not promoted to theorem-grade here.

## Updated C-7 status

This tranche discharges the easy eliminations:

```text
{1}, rank-1 tori, T^2, standard block SU(2), principal SO(3)
```

C-7 remains open because `U(2)` and the final full-`SU(3)` admissibility statement still require C-8-dependent closure.

## Non-claims

This document does not prove A2 minimality.

This document does not fully close C-7.

This document does not close C-8.

This document does not prove full `SU(3)` terminality or uniqueness.

This document does not imply any `SU(3)` lattice gauge theory result.

This document does not cross into `SocioProphet/yang-mills` scope.
