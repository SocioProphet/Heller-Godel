# HG-MTH-008.6 ⇄ HW-PRIME-WEIL-009 — The Dimension-Spectrum Bridge

**Primary home:** Heller-Godel — `docs/claims/HG-MTH-008.6-dimension-spectrum-bridge.md`  
**Reciprocal registration:** Heller-Winters — `docs/prime-operator-lane/HW-PRIME-WEIL-009-dimension-coordinate.md` (stub pointing here)  
**Parents:** HG-MTH-008.4 (USP ≡ factoring), HG-MTH-008.5 (factoring = abelian HSP), HW-PRIME-WEIL-008 (geometric chain: circle/hyperbola tangency, delta=0 ↔ critical line)  
**Status:** Mixed. One theorem-grade quantitative anchor (Plancherel dim²-weighting), one placement (the delta ↔ dim correspondence as analogous boundary loci), one fenced synthesis (separation). **The delta ↔ dim relation is an analogy of position relative to a boundary, NOT an equality of quantities. Do not let any artifact imply dim rho = delta.**  
**Date:** 2026-05-28

---

## 0. Purpose

Three programs keep landing on the same boundary:

- **HG-MTH-008.5**: abelian HSP is Fourier-easy; non-abelian HSP is hard.
- **HW-PRIME-WEIL-008**: the unit circle and unit hyperbola are tangent at `(1,0)`; RH is positioned as all zeros at the tangency `delta=0`, none in the hyperbolic region.
- **Group character theory**: `chi(e)=dim rho`; abelian iff all irreps are 1-dimensional.

This claim identifies the **single coordinate** that organizes all three — the representation dimension `dim rho = chi(e)` — and proposes a concrete, computable deliverable: the **dimension spectrum** as a candidate Geometric-Complexity-Theory obstruction coordinate. It is a *re-coordinatization*, explicitly not a separation proof (§5).

---

## 1. Claim Discipline (§15)

### Standard / established (citable, theorem-grade)

- (S1) `chi(e) = Tr rho(e) = dim rho`, for any representation rho.
- (S2) A finite group G is abelian iff every irreducible representation is 1-dimensional.
- (S3) For abelian G, irreducible characters take values in roots of unity: `|chi(g)|=1` for all g. Values lie on the unit circle.
- (S4) For non-abelian G, there exists an irrep with `dim rho > 1`; then `chi(e)=dim rho>1` and `chi(g)` is a sum of `dim rho` unit-modulus eigenvalues, so `|chi(g)| <= dim rho`.
- (S5) **Burnside / regular-representation identity:** `sum_{rho in G^} (dim rho)^2 = |G|`.
- (S6) **Plancherel measure on G^ (Peter-Weyl, finite case):** the Plancherel measure assigns irrep rho the weight `(dim rho)^2/|G|`. For abelian G this is the uniform measure on the `|G|` characters; for non-abelian G it is concentrated on higher-dimensional irreps by the dim² weight.
- (S7) **Abelianization count:** the number of 1-dimensional irreps of G equals `|G^ab| = |G/[G,G]|`. For `S_n`, `n >= 2`, `[S_n,S_n]=A_n`, so exactly two 1-dimensional irreps: trivial and sign.
- (S8) **GCT no-go:** Bürgisser–Ikenmeyer–Panova show occurrence obstructions cannot prove permanent vs determinant; genuine multiplicity obstructions are required and remain open.
- (S9) **Relativization barrier:** Baker–Gill–Solovay show oracle-invariant techniques cannot settle P vs NP.
- (S10) HW-PRIME-WEIL-008 geometric chain: exact circle/hyperbola tangency at `(1,0)`; `delta=0` ↔ critical line; off-line trajectory on the unit hyperbola. Established internally in Heller-Winters, with its own non-claim boundary.

### Interpretive placement (ours, defensible, NOT proved)

- (P1) **The boundary identification.** `dim rho=1` ↔ unit circle ↔ abelian ↔ Fourier-easy ↔ Dirichlet ↔ `delta=0` tangency is one locus viewed across domains. `dim rho>1` ↔ off-circle ↔ non-abelian ↔ hard ↔ Artin ↔ `delta>0` hyperbolic is the departure. This is a claim about shared position relative to a boundary, organizing five domains under one coordinate.
- (P2) **The radial reading.** `dim rho - 1 >= 0` is read as a discrete “radial displacement off the unit circle,” structurally analogous to delta, the off-critical-line distance in HW-PRIME-WEIL-008. Both vanish exactly on the boundary.
- (P3) **Dimension spectrum as obstruction coordinate.** The multiset `DimSpec(G) = {dim rho : rho in G^}` is proposed as a GCT-style invariant distinguishing the abelian/easy from non-abelian/hard regimes of a problem’s symmetry group.

### Authorial synthesis (FENCED — NOT theorem, NOT to be implied)

- (A1) **Overclaim guard:** `dim rho = delta` is FALSE and forbidden. `dim rho` is a discrete integer >= 1; delta is a continuous real off-critical-line parameter. They are analogous boundary positions, not equal quantities. Any code, doc, or comment asserting equality is a defect.
- (A2) That the dimension spectrum *separates* complexity classes. It **re-coordinatizes**; turning it into a separation is blocked by (S8) and (S9). Diagnostic, not a proof engine.
- (A3) Any RH/GRH/Artin proof claim. Preserve HW-PRIME-WEIL-008’s non-claim.
- (A4) Logos / unit-character / naming material.

---

## 2. Definitions

- `G^` = set of isomorphism classes of irreducible representations of finite group G.
- `DimSpec(G)` = multiset `{dim rho : rho in G^}`.
- **Plancherel measure** `mu_Pl(rho) = (dim rho)^2/|G|` on `G^` (S6). It is a probability measure by S5.
- **Boundary functional** `beta(G) = max_{rho in G^} dim rho`. Then `beta(G)=1 iff G` is abelian (S2). “On the circle” iff beta = 1.
- **Plancherel concentration** `kappa(G) = sum_{dim rho > 1} mu_Pl(rho)`, the mass the Plancherel measure puts off the unit circle. `kappa(G)=0 iff G` is abelian.
- **Abelian core fraction** `alpha(G) = |G^ab|/|G|`, a diagnostic of how much of G is visible on the circle.

---

## 3. Theorem-grade anchor (T1)

**T1 (the measure realizes the boundary).** For finite G:

1. `beta(G)=1 iff kappa(G)=0 iff G` is abelian (S2, S6).
2. The Plancherel measure is uniform on `G^` iff G is abelian; otherwise it is dim²-weighted toward higher-dimensional irreps (S5, S6).
3. The 1-dimensional irreps — the part supported on the unit circle — are exactly the characters of the abelianization `G^ab`, counted by `|G/[G,G]|` (S7). For `S_n`, these are precisely the even/odd sign structure.

*Proof.* These are restatements of S2, S5, S6, and S7. No new obligation. ∎

**Corollary C1 (the wheel sits on the circle).** For the wheel `G_n=(Z/nZ)^x`, which is abelian, `DimSpec(G_n) = {1}^{phi(n)}`, `beta=1`, and `kappa=0`. The factoring corner (HG-MTH-008.4/008.5) lives entirely on the unit circle. This is the representation-theoretic restatement of “abelian HSP is Fourier-easy.”

**Corollary C2 (the hard corner leaves the circle).** `DimSpec(S_n)` contains entries >1 for `n >= 3`, for example `S_3:{1,1,2}`, `S_4:{1,1,2,3,3}`, and `S_5:{1,1,4,4,5,5,6}`, each verified by `sum(dim rho)^2=|S_n|`. The graph-isomorphism / non-abelian-HSP corner has `beta>1`, `kappa>0`. Its only on-circle content is the `Z/2` abelianization, i.e. sign.

---

## 4. The bridge, stated cleanly

| Domain | On the circle (`dim=1`, `beta=1`, `kappa=0`) | Off the circle (`dim>1`, `beta>1`, `kappa>0`) |
|--------|-----------------------------------------------|------------------------------------------------|
| HSP / complexity | abelian HSP — polynomial in Shor setting | non-abelian HSP — hard frontier / GI corner |
| Characters | `chi(e)=1`, values on unit circle | `chi(e)=dim>1`, off circle |
| `S_n` | abelianization `Z/2`, sign ±1 | higher irreps |
| L-functions | Dirichlet, 1-dimensional | Artin, higher-dimensional |
| Geometry (HW-008) | unit circle, `delta=0` tangency | unit hyperbola, `delta>0` departure |
| **Coordinate** | `dim rho = chi(e) = 1` | `dim rho = chi(e) > 1` |
| **Measure** | `mu_Pl` uniform | `mu_Pl` dim²-weighted off circle |

The single organizing coordinate across all rows is `dim rho = chi(e)`. The Plancherel measure `mu_Pl` is the precise “same measure space” object the conversational work kept invoking: it is uniform-on-circle in the abelian case and dim²-displaced in the non-abelian case.

---

## 5. What this is NOT (required reading)

- It is **not** a separation of complexity classes. It is a coordinate that locates where a separation would have to live; the same service HW-PRIME-WEIL-008 performs for RH by locating the barrier, not crossing it.
- The delta ↔ dim correspondence (P2) is **analogy of boundary position, not equality** (A1). Forbidden to assert `dim rho = delta`.
- Barriers stand: occurrence obstructions are insufficient (S8); relativization blocks oracle-invariant methods (S9). A clean dimension coordinate does not bypass these. The deliverable is **diagnostic**, and any future attempt to upgrade it to a separation must confront S8/S9 head-on.
- No RH/GRH/Artin proof (A3).

**One-line guard for all docs:** *“The dimension spectrum re-coordinatizes the abelian/non-abelian boundary as position relative to the unit circle; it diagnoses the boundary, it does not cross it, and dim rho is analogous to — never equal to — the off-critical-line parameter delta.”*

---

## 6. Implementation tasks (for the agent)

New module `src/heller_godel/dimension_spectrum.py`, reusing `wheel_plancherel.py`.

- **IMPL-1** `dim_spectrum(G)`: given a finite group fixture for standard families `Z/n`, `G_n`, `S_n`, `D4`, `Q8`, `A_n`, return the multiset of irrep dimensions.
- **IMPL-2** `verify_burnside(G)`: assert `sum(dim rho)^2=|G|` (S5). Independent sanity check on any loaded spectrum.
- **IMPL-3** `plancherel_measure(G)`: return `rho -> (dim rho)^2/|G|`; assert it sums to 1; assert uniform iff abelian.
- **IMPL-4** `boundary_functional(G)`: return `beta=max dim rho` and `kappa=sum_{dim>1} mu_Pl`; assert `beta=1 iff kappa=0 iff` abelian.
- **IMPL-5** `abelianization_count(G)`: number of 1-dimensional irreps; assert equals `|G/[G,G]|` for fixtures. For `S_n`, assert it equals 2.
- **IMPL-6** wheel crosslink: import `G_n` through `wheel_plancherel.py`; assert `DimSpec(G_n)={1}^{phi(n)}`, `beta=1`, `kappa=0` (C1).
- **IMPL-7** hard-corner witness: use standard `S_3,S_4,S_5` spectra; assert C2 and `beta>1`, `kappa>0`.
- **IMPL-8** optional HW crosslink visualization: tabulate `(dim rho-1)` as discrete radial displacement alongside HW-PRIME-WEIL-008’s delta as a continuous analogue, clearly labeled “analogy, not equality” per A1.

Do NOT implement orbit-closure / coordinate-ring multiplicity computation. Full GCT machinery is out of scope, and S8 shows the easy occurrence version is insufficient. The deliverable here is the coordinate, computed for symmetry-group fixtures, not the GCT separation attempt.

---

## 7. Tests (must pass)

```python
# Burnside / spectrum correctness (S5)
test_burnside_sum_of_squares_Zn
test_burnside_sum_of_squares_S3
test_burnside_sum_of_squares_S4
test_burnside_sum_of_squares_S5
test_burnside_sum_of_squares_Q8
test_burnside_sum_of_squares_D4

# Boundary functional (T1)
test_beta_one_iff_abelian
test_kappa_zero_iff_abelian
test_plancherel_uniform_iff_abelian

# Abelianization = on-circle content (S7)
test_abelianization_count_equals_G_mod_commutator
test_Sn_has_exactly_two_one_dim_irreps

# Wheel crosslink (C1, IMPL-6)
test_wheel_spectrum_all_ones
test_wheel_on_circle

# Hard-corner witness (C2, IMPL-7)
test_Sn_off_circle

# Overclaim guard (A1, §5)
test_no_dim_equals_delta_assertion
test_module_docstring_states_boundary_only_not_separation
```

---

## 8. Documentation context

The repository also carries `docs/concepts/dimension-spectrum-coordinate.md`, which explains the same material for competent non-specialists. The explainer must end on the §5 boundary: this diagnoses, does not separate; dim is analogous to, never equal to, delta; the GCT and relativization barriers stand.

A reciprocal Heller-Winters stub should register this as `HW-PRIME-WEIL-009-dimension-coordinate.md`, pointing back to this primary Heller-Godel claim.

Citations to carry in that context:

- Serre, *Linear Representations of Finite Groups*.
- Fulton–Harris, *Representation Theory*.
- Bürgisser, Ikenmeyer, Panova (2016), *No occurrence obstructions in geometric complexity theory*, FOCS.
- Mulmuley, Sohoni (2001/2008), GCT I/II.
- Baker, Gill, Solovay (1975), *Relativizations of the P =? NP question*.
- Babai (2016, correction 2017), GI in quasipolynomial time.
- HW-PRIME-WEIL-008 internal document for the geometric chain.

---

## 9. Binds-to / crosslinks

- **HG-MTH-008.4** — wheel `G_n` abelian, `DimSpec={1}^{phi(n)}` (C1). Module reuse.
- **HG-MTH-008.5** — abelian-HSP-easy = on-circle; the boundary guard there is the dimension boundary here.
- **HW-PRIME-WEIL-008** — circle/hyperbola tangency = the `dim=1` locus (P1, P2). Reciprocal stub HW-PRIME-WEIL-009.
- **PO-18 / PO-22** — `omega(n)` multi-factor cost: each distinct prime is one cyclic dim-1 factor; relate the factor count to the on-circle Plancherel structure.

---

## 10. Proof obligations (open)

- **PO-23** Prove or refute: is there a dimension-spectrum functional invariant within a complexity class, under the relevant reductions, yet differing across the abelian/non-abelian boundary? If yes, characterize it; if no, record the barrier obstruction explicitly.
- **PO-24** Formalize the delta ↔ `(dim-1)` correspondence as a precise statement about *boundary position* in a common parameter space, with an explicit theorem stating in what sense they are analogous and in what sense they are provably distinct (discrete vs continuous, integer vs real). This is the rigorous home of the A1 guard.
- **PO-25** Connect Plancherel concentration `kappa(G)` to a known complexity measure of the isomorphism/HSP problem over G, for example Babai recursion depth or Luks divide-and-conquer bottlenecks. Empirical first.

---

## 11. Non-claims

- Does NOT separate P from NP or any complexity classes (A2; barriers S8, S9).
- Does NOT assert `dim rho = delta` (A1). Analogy of boundary position only.
- Does NOT prove RH/GRH/Artin (A3); preserves HW-PRIME-WEIL-008’s non-claim.
- Does NOT implement GCT orbit-closure machinery; computes the coordinate only.
- Does NOT depend on the Logos/naming synthesis (A4).

---

## 12. Glossary additions

| Symbol | Meaning |
|--------|---------|
| `dim rho` | dimension of irrep rho; equals `chi(e)` |
| `DimSpec(G)` | multiset of irrep dimensions of G |
| `mu_Pl` | Plancherel measure, `rho -> (dim rho)^2/|G|` |
| `beta(G)` | boundary functional, `max_rho dim rho`; equals 1 iff abelian |
| `kappa(G)` | Plancherel mass off the circle, `sum_{dim>1} mu_Pl` |
| `alpha(G)` | abelian core fraction, `|G^ab|/|G|` |
| `G^ab` | abelianization `G/[G,G]` |
| `delta` | HW-008 off-critical-line parameter; analogue of `dim rho-1`, NOT equal |
