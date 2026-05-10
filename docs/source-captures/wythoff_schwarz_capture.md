# Wythoff / Schwarz Symmetry Grammar - Markdown Capture

Sources:

- Uploaded image: `image(32).png`  
  Classification: context / future-horizon  
  SHA-256: `6e2589b67fa18b226507627dcc05ebcc9ba158e944964bb030b9dd47cc9b9c67`
- External URL: `https://en.wikipedia.org/wiki/Lists_of_uniform_tilings_on_the_sphere,_plane,_and_hyperbolic_plane`  
  Classification: external URL context / future-horizon
- User-provided Wythoff symbol exposition from the conversation  
  Classification: context / future-horizon

## Role in Heller-Godel

This material supports HG-M5: Wythoff / Schwarz symmetry grammar alignment. It is a structural analogy and future-horizon testbed, not a theorem source for the current proof-character manuscript.

## Core Wythoff grammar

A Wythoff symbol uses rational parameters `p, q, r` plus a marking convention. The four standard forms are:

```text
p | q r       regular and quasi-regular polyhedra
p q | r       semiregular polyhedra
p q r |       even-faced polyhedra
| p q r       snub polyhedra
```

There is also one exceptional pseudo-Wythoff case:

```text
| 3/2 5/3 3 5/2
```

for the great dirhombicosidodecahedron.

## Integer / rational split

Integer Wythoff data produce convex uniform polyhedra and classical tiling regimes. Rational data such as `5/2`, `5/3`, `4/3`, and `3/2` produce nonconvex, star, retrograde, or self-intersecting behavior.

Heller-Godel alignment:

```text
integer / clean symbolic regime
-> controlled, well-behaved realization

rational / extended symbolic regime
-> winding, carry, retrograde, or defect-like behavior requiring extra structure
```

This is only a structural analogy. Wythoff rationals produce nonconvex polyhedra through reflection geometry; Heller-Godel rational exponents produce mod-p carry defects through finite-resolution floor arithmetic.

## Schwarz triangle curvature trichotomy

A Schwarz triangle `(p,q,r)` has angles:

```math
pi/p, pi/q, pi/r.
```

The regime is determined by:

```text
1/p + 1/q + 1/r > 1  -> spherical
1/p + 1/q + 1/r = 1  -> Euclidean
1/p + 1/q + 1/r < 1  -> hyperbolic
```

This is the strongest alignment to Heller-Godel's base-relative regime discipline: small symbolic data determine realized geometry once the base curvature condition is fixed.

## Projection chart vs preimage geometry

The hyperbolic tilings in the Poincare disk are especially useful. The disk picture makes one tile appear central and makes tiles appear to shrink toward the boundary. But intrinsically, the hyperbolic plane is homogeneous; every tile has the same hyperbolic size and any point can be mapped to the disk center by an isometry.

Heller-Godel analogy:

| Hyperbolic tiling | Heller-Godel projection discipline |
|---|---|
| intrinsic hyperbolic plane | full proof/preimage object |
| Poincare disk chart | projected finite invariant |
| choice of disk center | choice of section / normalization |
| isometry moving any point to center | gauge/cochain freedom |
| apparent boundary effect | projected artifact that may dissolve upstream |

The concrete Heller-Godel example is `zeta_p`: it appears as a carry obstruction in the finite projected picture, but it is a coboundary of `f_p(alpha)=floor(p alpha) mod p` in ordinary cohomology once the cochain-level preimage is admitted.

## AdS/CFT boundary

AdS/CFT should be treated only as a target-level example of what a real bulk-boundary dictionary would require. Heller-Godel currently has projection/preimage discipline, not a holographic duality theorem.

Do not write:

```text
Heller-Godel is AdS/CFT for proof classes.
```

Safe wording:

```text
Poincare disk and Schwarz tilings provide a structural model of chart/projection effects. AdS/CFT shows the level of rigor required for a genuine bulk-boundary duality. Heller-Godel does not yet have such a duality.
```

## Fibers and sheaves

Fiber/sheaf language is relevant only after a proof-moduli construction exists. A mature theory might define sheaves over proof-class moduli, local fibers carrying phase/shell data, and restriction maps carrying projected invariants. That is future target language, not current machinery.

## Repository routing

The full exposition is materialized in:

```text
docs/future-horizons/wythoff_schwarz_symmetry_grammar.md
```

This source capture is the compact source summary.
