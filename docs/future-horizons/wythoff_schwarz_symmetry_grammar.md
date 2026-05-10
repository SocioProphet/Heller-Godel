# Wythoff / Schwarz Symmetry Grammar — Alignment Note

Tracking issue: HG-M5  
Lane: future-horizons / symmetry grammar  
Status: structural analogy and exposition only. No theorem about proof-character generating functions is claimed in this note. No mechanism of the Heller-Godel program is justified by this note.

## 0. Scope and disclaimer

This document records a structural alignment between Wythoff / Schwarz triangle theory in classical reflection geometry and the base-relative discipline of the Heller-Godel proof-character program. It is exposition, not theorem. The alignment is used as:

1. a worked example of the pattern `small symbolic data determines regime-dependent realization`, for which Wythoff/Schwarz is a mature mathematical precedent;
2. a structural model for what a future Heller-Godel theorem of similar shape could aim for;
3. a vocabulary source for projection vs. preimage, chart vs. intrinsic geometry, and exception handling.

Wythoff/Schwarz theory does not prove anything about Heller-Godel. The shared word `regime` does not imply shared mathematical mechanism. Where this note borrows AdS/CFT vocabulary, the borrowing is structural only; no holographic duality is claimed for Heller-Godel.

## 1. Wythoff and Schwarz symbols as finite generative syntax

### 1.1 The Wythoff symbol grammar

A Wythoff symbol is a triple `(p,q,r)` of rational numbers together with a marking convention specifying which vertex or mirror relation in a fundamental triangle is active. The four standard forms are:

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

for the great dirhombicosidodecahedron, which requires a modification of the standard construction.

Within the standard grammar, admissible rational entries are highly constrained. Integer entries produce the familiar convex cases; rational entries extend the construction into star and nonconvex regimes.

### 1.2 Case dictionary

The Wythoff cases have standard vertex-configuration interpretations:

| Case | Form | Structural reading |
|---|---|---|
| 1 | `p | q r` | regular and quasi-regular; alternating `q,r` faces around vertices |
| 2 | `p q | r` | semiregular / truncated forms; vertex configuration `{p,2r,q,2r}` before removing trivial faces |
| 3 | `p q r |` | even-faced forms; vertex configuration `{2p,2q,2r}` |
| 4 | `| p q r` | snub forms; chiral left/right variants often appear |
| exception | `| 3/2 5/3 3 5/2` | great dirhombicosidodecahedron, outside the standard Wythoff construction |

The exception is methodologically important: a classification can be powerful and still have a boundary case outside its generative grammar.

### 1.3 Integer vs. rational entries: convex / nonconvex split

Integer `(p,q,r)` entries produce convex uniform polyhedra. Rational entries such as `5/2`, `5/3`, `4/3`, and `3/2` extend the construction to nonconvex realizations: star polyhedra, retrograde traversals, self-intersecting faces, and winding behavior.

This integer / rational split is structurally parallel to a conservative / extended regime distinction in Heller-Godel:

```text
integer / clean symbolic regime
-> controlled, well-behaved realization

rational / extended symbolic regime
-> winding, carry, retrograde, or defect-like behavior requiring extra structure
```

The analogy is pattern-level only. Wythoff rationals produce nonconvex polyhedra by reflection-group action. Heller-Godel rational exponent channels produce finite phase and carry effects through floor-arithmetic discretization. Different mechanism; similar dichotomy shape.

### 1.4 Fundamental triangle as minimal generating data

In Wythoff construction, one fundamental triangle plus a reflection rule generates the full polyhedron or tiling. The triangle is the minimal local datum; the global object is its orbit under the reflection group.

This is the cleanest structural analogy for Heller-Godel. A normal-form grammar plays the role of minimal local data. Closure operations on that grammar generate proof families, just as reflections of a fundamental triangle generate a tiling or polyhedron.

The analogy stops at `minimal local data plus closure operation`. Heller-Godel closure operations are not literal reflections, and proof classes do not literally tile a hyperbolic plane.

### 1.5 Exception handling

The great dirhombicosidodecahedron is the unique uniform polyhedron outside ordinary Wythoff construction. It has more faces around a vertex than the standard cases allow and requires modified construction.

Heller-Godel lesson: expect boundary cases. A grammar-based theorem may need an exception register. Exceptions should be captured and classified rather than treated as automatic refutations of the entire scheme.

## 2. Curvature / base-regime split: spherical, Euclidean, hyperbolic

### 2.1 Angle-sum condition

A Schwarz triangle `(p,q,r)` has interior angles:

```math
pi/p, pi/q, pi/r.
```

The angle sum determines the curvature regime:

```text
1/p + 1/q + 1/r > 1  -> spherical realization
1/p + 1/q + 1/r = 1  -> Euclidean realization
1/p + 1/q + 1/r < 1  -> hyperbolic realization
```

This is a single inequality on three symbolic inputs determining global geometric realization.

### 2.2 Spherical realizations

Spherical Schwarz triangles tile the 2-sphere by reflections. The familiar orbifold families include the dihedral sequences and the tetrahedral, octahedral, and icosahedral cases:

```text
*222, *322, *422, *522, *622, *332, *432, *532
```

These correspond to finite spherical reflection groups and finite polyhedral realizations.

### 2.3 Euclidean realizations

The Euclidean Schwarz triangles are:

```text
*442, *333, *632
```

They tile the plane periodically. These are the planar wallpaper-like analogs of the spherical finite cases.

### 2.4 Hyperbolic realizations

Infinitely many hyperbolic Schwarz triangles exist. Examples include:

```text
*732, *542, *433
```

They tile the hyperbolic plane. In the Poincare disk presentation, tiles visually concentrate toward the boundary. This is a chart effect, not intrinsic shrinking.

### 2.5 Base-regime determination

The trichotomy is the strongest structural feature for Heller-Godel: a compact symbolic prescription determines a realization regime. A future Heller-Godel theorem of comparable shape might say:

```text
proof grammar class + statistic class + base/projection choice
-> rational / algebraic / D-finite / transcendental generating-function regime
```

Wythoff/Schwarz is a precedent for this kind of theorem shape. It is not the proof of such a theorem.

## 3. Alignment to Heller-Godel: scope and limits

### 3.1 What transfers legitimately

Four legitimate carry-forwards:

1. **Small symbolic data -> regime-determined realization.** Wythoff/Schwarz is a mature example of the kind of compact generative regime theorem Heller-Godel may eventually seek.
2. **Grammar-driven enumeration.** Fundamental-domain reflections generate structures; normal-form grammars generate proof families.
3. **Integer / rational regime distinction.** Integer regimes are clean; rational regimes introduce winding or defect-like behavior requiring additional care.
4. **Exception handling.** Boundary cases outside a grammar are part of classification methodology, not automatic failure.

### 3.2 What does not transfer

The analogy does not provide:

1. a theorem about `T_phi`;
2. a resolution of the `zeta_p` coboundary issue;
3. a construction of proof-class moduli;
4. a justification of any Heller-Godel mechanism such as `chi_p`, `zeta_p`, regulator, or Chern class.

Those are Heller-Godel-internal mathematical tasks.

### 3.3 Conceptual dictionary

| Wythoff / Schwarz theory | Heller-Godel alignment |
|---|---|
| Wythoff symbol | compact syntax / generative code |
| Schwarz triangle `(p,q,r)` | local seed / fundamental-domain data |
| fundamental triangle | minimal proof / operation domain |
| reflections | closure operations / normalization-generated orbit |
| spherical realization | finite closed regime |
| Euclidean realization | periodic / translational regime |
| hyperbolic realization | infinite expansion regime |
| rational Wythoff entries | winding / star / nonconvex extension |
| great dirhombicosidodecahedron | boundary case outside the main generation method |
| uniform tiling / polyhedron | realized orbit of symbolic grammar |

This dictionary is vocabulary, not mechanism identification.

## 4. Projection chart vs. preimage geometry

### 4.1 Poincare disk as chart of the hyperbolic plane

The hyperbolic plane `H^2` is homogeneous: every point looks like every other point. The Poincare disk model presents `H^2` in a bounded disk, visually choosing one point as center and compactifying the boundary at infinity.

In the disk chart:

- the center looks privileged;
- tiles appear smaller near the boundary;
- the boundary circle appears finite.

Intrinsically:

- no point is privileged;
- tiles have equal hyperbolic size;
- the boundary is at infinity.

This provides a precise projection/preimage example.

### 4.2 Apparent boundaries that dissolve in the preimage

The disk boundary is a coordinate artifact. It appears in the chart but not as an ordinary finite boundary of `H^2`.

Heller-Godel analog: `zeta_p` appears in the finite projected phase picture as a multiplicativity obstruction, but in ordinary cohomology it is a coboundary:

```math
zeta_p(alpha,beta)=f_p(alpha+beta)-f_p(alpha)-f_p(beta),
quad f_p(alpha)=floor(p alpha) mod p.
```

Thus `[zeta_p]=0` if arbitrary cochain changes of section are allowed. The apparent obstruction dissolves in the cochain-level preimage. This does not make `zeta_p` useless; it makes it a section-dependent finite-resolution defect rather than a nontrivial ordinary cohomology class.

### 4.3 Gauge / section choice

Choosing the disk center is a chart choice. Any point of the intrinsic hyperbolic plane can be moved to the disk center by an isometry.

Heller-Godel analog: choosing a finite phase section, canonical statistic, or normal-form representation shapes the observed invariant. This is why Heller-Godel must track grammar, statistic, and section explicitly.

### 4.4 AdS/CFT disclaimer

AdS/CFT is not merely boundary visualization. It is a physical duality claim between a bulk gravity theory and boundary conformal field theory, with a rigorous dictionary in successful cases.

Heller-Godel does not currently instantiate such a duality. It has projection/preimage discipline, not a holographic duality theorem.

Safe statement:

```text
Poincare disk and Schwarz tilings model chart/projection effects. AdS/CFT shows the level of rigor a real bulk-boundary dictionary would require. Heller-Godel does not yet have such a dictionary.
```

Unsafe statement:

```text
Heller-Godel is AdS/CFT for proof classes.
```

## 5. Fibers, sheaves, and eventual mathematical home

Fiber and sheaf language is relevant but belongs after a proof-moduli construction exists.

A mature program might define:

- a moduli object of proof classes;
- sheaves over that base;
- fibers carrying local proof-family data;
- restriction maps carrying local phase or shell information.

Only then could `chi_p`, `zeta_p`, and higher refinements be organized as sheaf-theoretic data. This is target language, not current machinery.

## 6. Fractal / heavy-tail dynamics note

A user-side future analogy mentions fractal Brownian motion and chaotic domains with no mean or infinite variance. This needs a correction before it is used technically.

- Standard Brownian motion has mean zero and finite variance at fixed time.
- Fractional Brownian motion is Gaussian and also has finite variance at fixed time, though it has long-range dependence or roughness depending on the Hurst parameter.
- Infinite variance is characteristic of heavy-tailed stable processes such as Levy flights with stability index below 2, not ordinary fractional Brownian motion.

The safe future-horizon language is:

```text
rough/self-similar dynamics and heavy-tailed stochastic processes may provide analogies for chaotic recognition or shell-return behavior, but fractional Brownian motion and infinite-variance Levy-stable processes must be distinguished.
```

This material does not currently bear on the Heller-Godel theorem core.

## 7. Promotion conditions

This note can move from future-horizon to theorem-core only if the following land:

1. a specific proof fragment is fixed;
2. a grammar of normal-form inhabitants is produced;
3. a theorem classifies generating-function regimes from grammar data;
4. the integer/rational/carry distinction is made formal in that grammar;
5. proof-class moduli and base maps are constructed if regulator/Chern language is used.

Until then, this note remains structural exposition.

## 8. Repository boundary

This note supports HG-M5. It may inform exposition and future computational experiments, such as a Wythoff-symbol parser or curvature-regime classifier. It must not be used as theorem support for the main proof-character manuscript unless a formal bridge is constructed.
