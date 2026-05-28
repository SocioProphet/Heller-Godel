# Dimension Spectrum as a Boundary Coordinate

This note explains HG-MTH-008.6 for a competent reader who does not need the full representation-theory machinery. The thesis is narrow: a single coordinate, `dim rho = chi(e)`, organizes the abelian/non-abelian boundary across the HSP, character, symmetric-group, L-function, and HW geometric pictures. It diagnoses the boundary. It does not cross it.

## 1. The same boundary keeps reappearing

In the factoring corner, the group is the wheel

```text
G_n = (Z/nZ)^x.
```

This group is abelian. Its irreducible representations are all 1-dimensional characters. That is why Fourier sampling is clean in HG-MTH-008.5: the transform is reading an abelian character space.

In the graph-isomorphism / non-abelian HSP corner, the symmetry group is no longer abelian. Symmetric groups such as `S_n` have higher-dimensional irreducible representations. That is where the easy Fourier story stops.

In the HW-PRIME-WEIL-008 geometric chain, the boundary appears as the unit-circle / unit-hyperbola tangency. The boundary is `delta=0`; departure is measured by a continuous off-critical-line parameter delta.

The same shape is visible in all three cases: boundary versus departure.

## 2. The coordinate is dim rho = chi(e)

For any representation rho with character chi,

```text
chi(e) = dim rho.
```

This is the coordinate. It is not invented here; it is standard representation theory.

When `dim rho = 1`, the character is on the unit circle. For a finite abelian group, every irrep has dimension 1. When `dim rho > 1`, the character at the identity leaves the unit circle radius and records a genuinely non-abelian representation.

Thus:

```text
dim rho = 1  <->  abelian / on-circle / Fourier-easy

dim rho > 1  <->  non-abelian / off-circle / hard frontier
```

## 3. The Plancherel measure is the measure space

The finite Plancherel measure on irreps is

```text
mu_Pl(rho) = (dim rho)^2 / |G|.
```

Burnside's identity says

```text
sum_rho (dim rho)^2 = |G|,
```

so this is a probability measure.

For abelian groups, every dimension is 1, so the measure is uniform. For non-abelian groups, higher-dimensional irreps receive quadratic weight. This is the precise measure-level form of the boundary: uniform on the circle in the abelian case, dim²-displaced off the circle in the non-abelian case.

## 4. The symmetric-group example

For `S_n`, the only 1-dimensional irreps for `n >= 2` are the trivial representation and the sign representation. That is the abelianization:

```text
S_n / A_n ~= Z/2.
```

The even/odd sign structure is the only part of `S_n` still visible on the unit circle. The rest of the representation theory lives in higher-dimensional irreps.

Examples:

```text
S_3: {1, 1, 2}
S_4: {1, 1, 2, 3, 3}
S_5: {1, 1, 4, 4, 5, 5, 6}
```

Each satisfies Burnside's identity by sum of squares.

## 5. Relation to the HW geometric chain

HW-PRIME-WEIL-008 uses the circle/hyperbola tangency as the geometric boundary. The dimension-spectrum bridge reads the representation-theoretic boundary in the same positional way:

```text
dim rho - 1 = 0     on the representation boundary

delta = 0           on the HW critical-line boundary
```

Both vanish at the boundary. But they are not the same quantity. `dim rho` is a discrete integer. Delta is a continuous real parameter. The bridge is an analogy of boundary position, not equality.

## 6. What this diagnoses

The dimension spectrum gives a compact diagnostic:

```text
DimSpec(G) = { dim rho : rho in G^ }
```

From it we compute:

```text
beta(G)  = max dim rho
kappa(G) = Plancherel mass on dim rho > 1
alpha(G) = |G^ab| / |G|
```

Then `beta=1` and `kappa=0` exactly in the abelian case. For the wheel `G_n`, this means `DimSpec(G_n) = {1}^{phi(n)}`. For `S_n`, `n >= 3`, we have `beta>1` and `kappa>0`.

## 7. What this does not prove

The dimension spectrum re-coordinatizes the abelian/non-abelian boundary as position relative to the unit circle; it diagnoses the boundary, it does not cross it, and dim rho is analogous to — never equal to — the off-critical-line parameter delta.

This is not a separation of complexity classes. It does not prove P != NP. It does not prove RH, GRH, or Artin. It does not implement GCT orbit-closure multiplicity machinery. It does not bypass the Bürgisser-Ikenmeyer-Panova occurrence-obstruction no-go or the Baker-Gill-Solovay relativization barrier.

## 8. References

- Serre, *Linear Representations of Finite Groups*.
- Fulton and Harris, *Representation Theory*.
- Bürgisser, Ikenmeyer, Panova (2016), *No occurrence obstructions in geometric complexity theory*.
- Mulmuley and Sohoni, GCT I/II.
- Baker, Gill, Solovay (1975), *Relativizations of the P =? NP question*.
- Babai (2016, correction 2017), graph isomorphism in quasipolynomial time.
- HW-PRIME-WEIL-008 internal document for the circle/hyperbola geometric chain.
