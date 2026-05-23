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

## Grade discipline

The eliminations below are definition-following once the path-beta filters are accepted. However, the path-beta convention itself is currently method-grade framework discipline rather than a completed A2 theorem.

Therefore this tranche is recorded as:

```text
theorem-grade modulo path-beta convention; method-grade overall
```

No result here promotes A2 to theorem-track.

## Adopted A2 filters

The path beta A2 convention uses:

```text
SU(3) + central Z/3 + cubic invariant
```

The active C-7 filters are:

1. closed and connected subgroup of `SU(3)`;
2. compatibility with the scalar central `Z/3 = {I_3, omega I_3, omega^2 I_3}`;
3. nonabelian active witness: active-sector generators must not all commute;
4. compatibility with the C-8 cubic-invariant condition;
5. spatial faithfulness for the A2 active sector;
6. no collapse back to a path-alpha `Spin(3)` encoding.

This tranche applies filters 1, 2, 3, 5, and 6 where they are already decisive.

It intentionally does not invoke C-8. Any candidate whose verdict requires the cubic-invariant preservation calculation is deferred to the next tranche.

## Verdict table

| Candidate subgroup type | Verdict in this tranche | Decisive failing filter |
|---|---|---|
| Trivial subgroup `{1}` | eliminated | fails nonabelian active witness and spatial faithfulness; center also fails |
| Rank-1 torus `U(1)` root-circle embeddings | eliminated | fails nonabelian active witness; center containment is insufficient even in special embeddings |
| Maximal torus `T^2` | eliminated | passes center but fails nonabelian active witness |
| Standard block `SU(2)` | eliminated | passes nonabelian witness but fails scalar `Z/3` center containment and fixes a line |
| Principal irreducible `SO(3)` | eliminated | passes nonabelian witness and irreducibility but fails scalar `Z/3` center containment |
| `U(2)=S(U(2)xU(1))` | not decided | passes easy filters; final verdict requires C-8 |
| Full `SU(3)` | not decided as theorem | expected admissible; final theorem status requires complete C-7/C-8 closure |

## Lemma 1 — Trivial subgroup eliminated

The trivial subgroup contains only:

```text
{I_3}
```

It does not contain `omega I_3` or `omega^2 I_3`, so it fails the scalar `Z/3` center filter.

The decisive structural failure is stronger: the trivial subgroup has only the trivial active-sector action. It preserves every tensor vacuously, but it witnesses no nontrivial A2 active-sector structure. Equivalently, all active-sector commutators vanish and the active witness has commutator norm zero.

This is not a C-8 cubic-preservation argument. It is an active-witness failure.

Verdict: eliminated.

## Lemma 2 — Rank-1 tori eliminated

A rank-1 torus is abelian and one-dimensional. Root-circle embeddings are obtained along A2 root directions. A special rank-1 circle may pass through scalar center elements, but center containment by itself is not sufficient for admissibility.

For any rank-1 torus, the Lie algebra is abelian. Hence all active-sector generator commutators vanish:

```text
[X, Y] = 0
```

for all torus generators `X, Y`. Thus the nonabelian active witness has commutator norm zero.

This eliminates rank-1 tori regardless of whether a special embedding intersects the scalar center.

Verdict: eliminated.

## Lemma 3 — Maximal torus eliminated

The maximal torus `T^2` contains the scalar center of `SU(3)`. Every central element lies in every maximal torus of `SU(3)`, so center containment does not eliminate `T^2`.

However, `T^2` is abelian. Its Lie algebra satisfies:

```text
[X, Y] = 0
```

for all `X, Y in Lie(T^2)`. Therefore the nonabelian active witness fails.

An abelian torus can preserve restricted diagonal data, but it cannot realize the full nonabelian A2 active-sector gate required by the path-beta convention.

Verdict: eliminated.

This elimination uses the nonabelian active-witness filter, not C-8.

## Lemma 4 — Standard block SU(2) eliminated

The standard block embedding is:

```text
A in SU(2) -> diag(A, 1) in SU(3)
```

This subgroup is nonabelian. Its active-sector generators may have nonzero commutators, so the nonabelian active witness is not the failing filter.

The decisive failure is scalar `Z/3` center containment. Elements of the standard block have third diagonal entry `1`. The scalar element:

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

and fixes a line. This confirms that it is a path-alpha comparison surface rather than a path-beta A2 active sector.

Verdict: eliminated.

This elimination is structurally important: the standard `SU(2)` block is exactly the kind of subgroup path alpha would try to preserve. Under path beta it is eliminated by the scalar `Z/3` center filter.

## Lemma 5 — Principal SO(3) eliminated

The principal SU(2)-type embedding in dimension 3 is the spin-1 representation. Its image is naturally read as an `SO(3)` subgroup of `SU(3)`.

This subgroup is nonabelian and acts irreducibly on the complexified three-dimensional representation. Thus neither abelianness nor reducibility is the decisive failure.

The decisive failure is scalar `Z/3` center containment. The center of `SU(2)` acts trivially in the spin-1 representation. Consequently, the image is `SO(3)`, whose center is trivial and whose elements do not include the non-real scalar elements:

```text
omega I_3, omega^2 I_3
```

with `omega^3 = 1`, `omega != 1`.

Verdict: eliminated.

This subgroup remains useful only as a path-alpha comparison surface.

## C-8 non-use statement

None of the five tranche-1 eliminations depends on cubic-invariant preservation.

The trivial subgroup, tori, and maximal torus are eliminated by active-witness failure. The standard block `SU(2)` and principal `SO(3)` are eliminated by scalar-center failure. C-8 is intentionally deferred.

## Remaining candidates

After this tranche, the only proper connected candidate still requiring a substantive verdict is:

```text
U(2) = S(U(2) x U(1))
```

It is nonabelian and contains the scalar `Z/3`, so the easy filters do not eliminate it. Its final verdict requires C-8: preservation of the selected A2 cubic invariant in the active-sector realization.

Full `SU(3)` remains the expected admissible candidate, but that status is not promoted to theorem-grade here.

## Updated C-7 status

This tranche discharges the easy eliminations:

```text
{1}, rank-1 tori, T^2, standard block SU(2), principal SO(3)
```

C-7 remains open because `U(2)` and the final full-`SU(3)` admissibility/minimality statement still require C-8-dependent closure.

## Non-claims

This document does not prove A2 minimality.

This document does not fully close C-7.

This document does not close C-8.

This document does not prove full `SU(3)` terminality or uniqueness.

This document does not imply any `SU(3)` lattice gauge theory result.

This document does not cross into `SocioProphet/yang-mills` scope.
