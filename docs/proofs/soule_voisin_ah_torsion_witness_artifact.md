# Soulé–Voisin / Atiyah–Hirzebruch Torsion Witness Artifact

Status: repo-grade workbench artifact. Method-adjacent.  
Classification (Hodge Program lane): `hodge-method`. Explicitly not `core-hodge`, `hodge-arithmetic`, Hodge proof, or Hodge progress.  
Provenance: consolidated from Drive-side Mode-A session work (`HG_AH_001`) into repo-grade form for evaluation against the Hodge Program bridge requirements scaffold and as input for `HODGE-EVAL-001`.

## 1. Setup

The integral Hodge conjecture is false in general. Atiyah and Hirzebruch constructed the first counterexamples using torsion phenomena, and later work, including Soulé–Voisin, refined the torsion-cohomology and algebraic-cycle boundary.

The rational Hodge conjecture is not falsified by these examples. The counterexamples show that the integral version requires additional torsion control beyond the rational case.

## 2. What this artifact records

This artifact records the Heller-Godel-side observation about the relationship between:

1. the `mu_2` finite character data produced by the Deligne-unit construction in the Catalan A1 case;
2. integral-cohomological / torsion structure of the small Hodge-shaped object;
3. the question of whether the `mu_2` character produces a torsion witness adjacent to an Atiyah-Hirzebruch-style obstruction.

The Catalan A1 `mu_2` character takes values in `{1,-1}`. Under the realization equivalence, this character is a finite-monodromy datum on a flat local system. The relationship between this finite torsion datum and the Atiyah-Hirzebruch obstruction is:

```text
the mu_2 character is torsion-witness-shaped data, not an Atiyah-Hirzebruch obstruction.
```

It supplies one factor of what an Atiyah-Hirzebruch-obstruction-grade torsion witness would require. The missing factors are:

1. a smooth complex projective variety `X` on which the flat bundle is realized;
2. a specific integral Hodge class on `X` whose torsion structure is detected by the bundle;
3. a proof that this class is not in the integral image of the relevant Chow group.

## 3. What this is and is not

### What it is

1. A method-adjacent observation that the Catalan A1 `mu_2` character produces torsion-witness-shaped data.
2. A workbench note that the gap between this and an Atiyah-Hirzebruch-style result is precisely the gap named in the Hodge Program obstruction registry.
3. A repo-grade input for future Hodge Program evaluation.

### What it is not

1. Not an Atiyah-Hirzebruch-style counterexample to the integral Hodge conjecture.
2. Not a torsion class on a projective variety.
3. Not evidence against the rational Hodge conjecture.
4. Not a Hodge progress claim.
5. Not a construction of algebraic cycles.

## 4. Active obstruction-registry references

| Entry | Reason |
| --- | --- |
| `OBS-HODGE-001` | integral Hodge false-positive risk; this artifact discusses integral-vs-rational torsion structure |
| `OBS-HODGE-008` | Hodge-origin to Hodge-proof promotion risk; the `mu_2` torsion-witness-candidate language must not be promoted to a torsion witness without the missing projective structures |

## 5. Inputs supplied for HODGE-EVAL-001

| Bridge primitive | What this artifact supplies | What it does not supply |
| --- | --- | --- |
| Hodge target datum `(X,k,alpha)` | Nothing | projective `X`; class `alpha` |
| Cycle realization datum | Nothing | algebraic cycles |
| Cycle equality obligation | Nothing | the equality |
| Deligne-to-Hodge bridge obligation | torsion-witness-shaped local-system input only | bridge from local torsion data to global cycle structure on a projective variety |

Expected evaluation result against this artifact:

```text
No Hodge target datum follows.
```

## 6. Sources and citation level

| Reference | Use |
| --- | --- |
| Atiyah-Hirzebruch, “Analytic cycles on complex manifolds,” Topology 1 (1962), 25–45 | integral-Hodge counterexample context |
| Soulé-Voisin, “Torsion cohomology classes and algebraic cycles on complex projective manifolds,” Adv. Math. 198 (2005), 107–127 | torsion cohomology and algebraic-cycle context |
| Voisin, *Hodge Theory and Complex Algebraic Geometry I/II* | standard integral-vs-rational Hodge distinction |

Bibliographic level only. Theorem-grade locators are not yet added and are required before theorem-grade downstream use.

## 7. Cross-references

```text
docs/proofs/catalan_a1_realization_equivalence.md
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
docs/proofs/hodge_clay_target_gap_ledger.md
SocioProphet/hodge-program-proof: docs/obstruction-registry.md
```

## 8. Explicit nonclaim envelope

```text
No projective variety X.
No integral Hodge class alpha.
No Atiyah-Hirzebruch-style counterexample.
No torsion class on a projective variety.
No algebraic cycles.
No cycle equality.
No claim against the rational Hodge conjecture.
No Hodge progress claim.
No promotion of torsion-witness-shaped data to torsion witness.
No proof-class moduli construction.
```
