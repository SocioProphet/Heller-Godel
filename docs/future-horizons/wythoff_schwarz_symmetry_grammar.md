# Wythoff / Schwarz Symmetry Grammar

Status: future-horizon / context note. This document is not a theorem claim for the Heller-Godel proof-character manuscript.

## 1. Wythoff and Schwarz symbols as finite generative syntax

Wythoff symbols and Schwarz triangles provide a mature example of finite symbolic data generating rich geometric realizations.

A Wythoff symbol records a constrained reflection construction inside a fundamental triangle. The same symbolic grammar can generate regular, quasiregular, truncated, even-faced, and snub families. Schwarz triangle data extend the integer triangle setting to rational parameters, allowing star and nonconvex uniform polyhedra.

This aligns with Heller-Godel at the level of generative discipline:

```text
finite symbolic seed
-> rule/constraint grammar
-> closure under operations
-> realized family
```

In Heller-Godel, the parallel finite seed is not a triangle group. It is a proof grammar plus fixed statistic plus singularity extraction. The phase data `chi_p`, finite seed basis `P_13`, and carry defect `zeta_p` are finite symbolic shadows of a richer proof-family object.

## 2. Curvature and base-regime split

For Schwarz triangle data `(p,q,r)`, the curvature regime is controlled by the angle-sum criterion:

```text
1/p + 1/q + 1/r > 1  -> spherical regime
1/p + 1/q + 1/r = 1  -> Euclidean regime
1/p + 1/q + 1/r < 1  -> hyperbolic regime
```

This is the cleanest alignment to Heller-Godel's base-relative regime discipline. A symbolic seed does not have one absolute realization. Its realization depends on the base geometry.

The Heller-Godel analogue is:

```text
proof-family data + statistic + base/projection choice
-> realized phase/shell/cohomological interpretation
```

The Schwarz/Wythoff lesson is not that proof characters are tilings. The lesson is that syntax and realization must be separated.

## 3. Projection chart vs preimage geometry

The Poincare disk presentation of the hyperbolic plane is a precise model of projection/preimage discipline.

Intrinsic hyperbolic space is homogeneous: no interior point is distinguished by the geometry itself. In the disk chart, one point is visually chosen as the center, tiles appear to shrink toward the boundary, and the unit circle appears as an edge. But the shrinking is a chart effect. Intrinsically, every tile in a regular hyperbolic tiling has the same hyperbolic size; the boundary circle is the boundary at infinity.

This gives a useful analogy:

| Hyperbolic tiling | Heller-Godel projection discipline |
|---|---|
| Intrinsic hyperbolic plane | full proof/preimage object |
| Poincare disk chart | projected finite invariant |
| choice of disk center | choice of section / normalization |
| isometry moving any point to center | gauge/cochain freedom |
| apparent boundary effect | projected artifact that may dissolve upstream |

The most important Heller-Godel example is `zeta_p`. In the projected finite phase picture, `zeta_p` appears as a carry obstruction to strict multiplicativity. In ordinary group cohomology, once the cochain `f_p(alpha)=floor(p alpha) mod p` is allowed, `zeta_p` is a coboundary. The apparent obstruction dissolves in the cochain-level preimage.

This does not mean `zeta_p` is useless. It records the failure of the chosen finite-resolution section to be additive. It means the object is section-dependent, not a nontrivial ordinary cohomology class.

## 4. Gauge and section choice in projections

The choice of center in the Poincare disk is a chart choice. Any point of the intrinsic hyperbolic plane can be moved to the disk center by an isometry.

The Heller-Godel analogue is section choice. Choosing a finite phase section, canonical statistic, or normal-form representation shapes the observed invariant. This is why the repository treats these as explicit parameters rather than hidden defaults.

The current theorem boundary is:

```text
fixed grammar + fixed statistic + fixed section
-> computable phase/carry data
```

not:

```text
all presentations and all statistics produce one absolute invariant
```

## 5. AdS/CFT disclaimer

AdS/CFT is a physical duality claim, not just a metaphor of boundary visualization. A genuine AdS/CFT-style statement would require a bulk theory, a boundary theory, and a rigorous dictionary between their observables or partition functions.

Heller-Godel does not currently provide that. Its phase data are lossy finite projections of proof-family structure, not a complete boundary dual of a proof-theoretic bulk.

The honest alignment is narrower:

```text
Poincare disk / Schwarz tilings show how homogeneous bulk geometry can appear boundary-concentrated in a projection chart.
AdS/CFT is a target-level example of what a true bulk-boundary dictionary would require.
Heller-Godel currently has projection/preimage discipline, not a holographic duality theorem.
```

Therefore this note may use vocabulary such as projection, preimage, chart, section, and boundary with care. It must not claim that Heller-Godel instantiates AdS/CFT.

## 6. Fibers, sheaves, and the eventual mathematical home

The language of fibers and sheaves is relevant, but it belongs after a proof-moduli construction exists.

A mature version of the program might define a moduli object of proof classes, sheaves over that base, local fibers carrying proof-family data, and restriction maps carrying local phase or shell information. In that setting, `chi_p`, `zeta_p`, and their higher refinements could be organized as local or sheaf-theoretic data.

That construction is not present yet. The current repository therefore treats sheaf/fiber language as future-horizon target language, not current machinery.

## 7. Repository boundary

This note supports HG-M5. It may inform exposition and future computational experiments, such as a small Wythoff-symbol parser or curvature-regime classifier. It must not be used as theorem support for the main proof-character manuscript unless a formal bridge is later constructed.
