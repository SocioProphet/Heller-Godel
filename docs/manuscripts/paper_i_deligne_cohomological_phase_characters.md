# Paper I / D1 — Deligne-Cohomological Phase Characters from Proof-Class Generating Functions

Working D1 reconciled draft for the Heller-Godel proof-character programme. This document supersedes the older floor-function-first framing in `calculus_invariant_characters_v2_1_3.md` where the new Deligne-cohomological rewrite applies.

D1 reconciliation status, 2026-05-14:

- Baseline: this file is the canonical Paper I / D1 theorem-core draft.
- Merged legacy source: `docs/manuscripts/calculus_invariant_characters_v2_1_3.md` is reconciled where its finite phase, carry, shell, flat-visibility, limitations, and nonclaim material survives the Deligne-cohomological rewrite.
- Missing source: no `v2.1.2` / `v2_1_2` manuscript source was found on live `main`; therefore no v2.1.2-specific override is applied in this pass.
- Divergence rule: where v2.1.3 conflicts with this D1 framing, this D1 draft wins unless a later sourced patch proves a narrower v2.1.2 or v2.1.3 passage should be restored.
- Locked audit invariants: finite `pi_1` monodromy/local-system notation is permitted; stale capital-Pi base path-category transport language is not reintroduced; carry remains a finite section-defect cocycle; Deligne cup-product/tame-symbol material remains a distinct regulator-symbol branch; `S^2` appears only as a finite local-system sanity check.

See `docs/review-ledgers/D1_RECONCILIATION_LEDGER.md` for the source inventory, merge decisions, and divergence notes.

## Claim boundary

This paper does **not** claim progress on the Hodge conjecture itself. It constructs a small Hodge-adjacent test object in the Deligne-cohomological corridor where Hodge classes, regulators, torsion shadows, and comparison maps are normally studied.

The construction does **not** assert algebraicity of the resulting classes. It does **not** construct algebraic cycles realizing arbitrary Hodge classes. It does **not** claim a variation of Hodge structure on a proof-class parameter space. It does **not** close the general encoding hypothesis for arbitrary arithmetic sentences.

What is claimed is smaller and testable:

1. A proof-class generating function with rational Puiseux singular data determines decorated local singular data.
2. The relevant local object is a Puiseux singular unit on a branch-killing cover.
3. Its finite phase character is the monodromy / deck shadow of that unit.
4. The finite character is multiplicative.
5. The carry cocycle appears only after choosing canonical integer representatives of residues modulo `L`.
6. The Deligne cup-product symbol is a separate regulator-symbol refinement; it is not the carry cocycle.
7. The `mu_2` Catalan / Klein-bottle comparison is a comparison of the same finite character through specified maps, not a native Deligne class on a real non-orientable manifold.

## 1. Introduction spine

The earlier manuscript defined finite phase characters by floor-function arithmetic and then patched multiplicativity by a correction term. The present rewrite reverses the order. The primary object is not the finite character; the primary object is the singular unit on a cover on which the Puiseux branch becomes single-valued.

After fixing a distinguished singularity `rho`, the punctured monodromy base is

```text
Y_phi^circ = U \ Sigma_phi.
```

No branch cut is imposed on `Y_phi^circ`; loops around `rho` remain present. The finite monodromy character lives downstairs on this punctured base.

The branch-killing cover is

```text
q_{phi,rho}: X_{phi,rho}^circ -> V_rho^times,
w^N = t_rho,
t_rho = 1 - x/rho.
```

The Deligne unit lives upstairs on `X_{phi,rho}^circ`, where the Puiseux singular line is single-valued.

## 2. Proof-class generating functions

The proof calculus is the simply typed lambda calculus with finite products. Proofs in other presentations are transported to beta-eta-normal de Bruijn lambda terms before the statistic is evaluated.

For a type or sentence `phi`, let `N_phi` be the set of canonical normal inhabitants. The reduced statistic `sigma` is chosen to be additive under product pairing; it subtracts the outer product-pairing constructor so that the strict product formula is true.

```text
T_phi(x) = sum_{s in N_phi} x^{sigma(s)}.
```

For product types with disjoint atomic vocabularies:

```text
T_{phi x psi}(x) = T_phi(x) T_psi(x).
```

This product formula is a statement about the reduced statistic. If raw constructor count includes the outer pairing constructor, the product acquires an extra factor of `x`.

### Chain example

```text
T_chain(x) = sum_{n >= 1} n x^n = x/(1-x)^2.
```

The dominant singularity is `rho = 1`, with integer local exponent. Its finite monodromy character is trivial.

### Catalan example

```text
C(x) = (1 - sqrt(1 - 4x))/(2x).
```

Near `rho = 1/4`,

```text
C(x) = 2 - 2(1 - 4x)^{1/2} + O(1 - 4x).
```

The `mu_2` character attaches to the singular line `(1 - 4x)^{1/2}`, not to `C(x)` as a whole. The full function does not transform by scalar multiplication around the branch point; the singular line does.

## 3. The Deligne class and finite character

Assume a rational Puiseux exponent

```text
alpha_{phi,rho} = a/N
```

in lowest terms. On the cover `w^N = t_rho`, the Puiseux singular unit is

```text
nu_{phi,rho} = w^a
```

or, with a nonvanishing analytic factor,

```text
nu_{phi,rho} = q^* h_{phi,rho} · w^a.
```

This is a holomorphic unit on the cover and hence determines a level-1 Deligne class

```text
D(u_{phi,rho}) in H^1_D(X_{phi,rho}^circ, Z(1)).
```

The deck transformation `w -> zeta_N w` acts by

```text
nu_{phi,rho} -> zeta_N^a u_{phi,rho}.
```

Therefore the finite monodromy character is

```text
chi_{phi,rho}(gamma_rho) = exp(2 pi i a/N).
```

The primary finite object is the `mu_N` character. If

```text
N = product_p p^{e_p},
N_p = p^{e_p},
```

then the `p`-primary projection is

```text
chi^{(p)}_{phi,rho} = chi_{phi,rho}^{N/N_p}: pi_1(V_rho^times) -> mu_{N_p}.
```

If the older manuscript records only prime-order characters, the prime reduction is the induced `mu_p` shadow when `p | N` and trivial otherwise.

## 4. Multiplicativity, carry, and regulator symbol

The product theorem is a theorem about decorated singular data, not about the leading Puiseux term of the undecorated product function.

Given synchronized decorated data at a common puncture `rho`, write

```text
alpha = a/N,
beta = b/M,
L = lcm(N,M),
A = aL/N,
B = bL/M.
```

On the common cover `w^L = t_rho`, the units are

```text
nu_phi = w^A q^*h_phi,
nu_psi = w^B q^*h_psi,
nu_{phi box-times psi} = u_phi u_psi = w^{A+B} q^*(h_phi h_psi).
```

The level-1 Deligne class is strictly multiplicative:

```text
D(u_phi u_psi) = D(u_phi) + D(u_psi)
```

in additive notation for `H^1_D(-, Z(1))`.

The finite monodromy character is also multiplicative:

```text
chi_{phi box-times psi,rho} = chi_{phi,rho} chi_{psi,rho}
```

in `Hom(pi_1(V_rho^times), mu_L)`.

### Carry as section-defect cocycle

The carry appears only after choosing canonical integer representatives of residues. Let

```text
s: Z/L -> Z,
s(A mod L) = [A]_L in {0,...,L-1}.
```

The section-defect carry is

```text
kappa_L(Abar,Bbar) = (s(Abar) + s(Bbar) - s(Abar + Bbar))/L.
```

Equivalently,

```text
s(Abar) + s(Bbar) = s(Abar + Bbar) + L kappa_L(Abar,Bbar).
```

This is the normalized cocycle representing the extension class associated to

```text
0 -> Z --times L--> Z -> Z/L -> 0.
```

It closes the old multiplicativity defect: the finite character was never nonmultiplicative; only the chosen lifted phase index was nonadditive.

### Deligne symbol is separate

The level-2 Deligne cup product

```text
D(u_phi) cup D(u_psi) in H^2_D(X_rho^{circ,L}, Z(2))
```

is the regulator-symbol refinement of the pair of units. It is not the carry cocycle.

After compactifying locally and adding the divisor `D = {w=0}`, the localization residue

```text
partial_D: H^2_D(overline X_rho^L \ D, Z(2)) -> H^1_D(D, Z(1))
```

is the tame-symbol boundary. Under the convention

```text
partial{f,g} = (-1)^{v(f)v(g)} f^{v(g)} / g^{v(f)} |_{w=0},
```

for `f = w^A h_phi` and `g = w^B h_psi`, with `h_phi(0)` and `h_psi(0)` nonzero,

```text
partial_D{f,g} = (-1)^{AB} h_phi(0)^B / h_psi(0)^A.
```

The inverse appears under the opposite convention. This tame symbol depends on valuations and analytic factors. It is not the carry. A concrete witness is `L=3`, `A=B=1`, `h_phi=h_psi=1`: the carry is `0`, while the tame symbol is `-1`.

## 5. Real test manifolds and finite local systems

The Deligne class lives upstairs on the complex analytic cover `X_{phi,rho}^circ`. The finite monodromy character lives downstairs on the punctured monodromy base `V_rho^times`. A real test manifold receives only this finite local-system shadow after a comparison map is chosen.

### 5.1 Finite local systems from monodromy characters

Let

```text
chi_{phi,rho}: pi_1(V_rho^times) -> mu_N
```

be the finite character of the Puiseux singular line at the chosen puncture. Define

```text
L^{(N)}_{phi,rho}
```

as the flat `mu_N` local system on `V_rho^times` classified by `chi_{phi,rho}`. Equivalently, it is the rank-one finite local system whose holonomy around the positive local loop `gamma_rho` is

```text
chi_{phi,rho}(gamma_rho) = zeta_N^a.
```

This local system is the torsion shadow of the upstairs Deligne unit. It is not the Deligne class itself.

### 5.2 Pullback to real test manifolds

Let `B` be a real test manifold. A finite test object on `B` is obtained only after choosing a continuous map

```text
f_B: B -> V_rho^times
```

or, equivalently for the finite local-system data, a homomorphism

```text
(f_B)_*: pi_1(B) -> pi_1(V_rho^times).
```

The pulled-back finite local system is

```text
L^{(N)}_{phi,rho,B} := f_B^* L^{(N)}_{phi,rho}.
```

For a loop class `c in pi_1(B)`, its holonomy is

```text
Hol_{L^{(N)}_{phi,rho,B}}(c)
  = chi_{phi,rho}((f_B)_*(c)).
```

This formula is the entire real-manifold interface. It is a pullback of a finite character, not a pullback of analytic Deligne cohomology.

No Deligne class on `B` is produced. No Chern class on `B` is produced. No algebraic cycle is produced. The object on `B` is a flat finite local system.

### 5.3 Sphere

For the sphere,

```text
pi_1(S^2) = 0.
```

Therefore every homomorphism

```text
pi_1(S^2) -> pi_1(V_rho^times) -> mu_N
```

is trivial. Every pulled-back finite `mu_N` local system on `S^2` is trivial.

This recovers the v2 sphere calculation in a cleaner form: the sphere is not a detector for the finite phase character because it has no fundamental group through which the local monodromy can be read.

### 5.4 Torus

Let

```text
pi_1(T^2) = <a,b | [a,b] = 1>.
```

At the finite-character level, a comparison map into the punctured disk is determined by two winding numbers

```text
m_a, m_b in Z,
```

where

```text
(f_T)_*(a) = m_a gamma_rho,
(f_T)_*(b) = m_b gamma_rho.
```

If the character index is `A mod N`, so that `chi(gamma_rho)=zeta_N^A`, then

```text
Hol(a) = zeta_N^{A m_a},
Hol(b) = zeta_N^{A m_b}.
```

The torus therefore records two commuting copies of the same finite local monodromy, weighted by the chosen winding numbers. It detects the finite phase character only through the selected comparison map.

### 5.5 Klein bottle

Let the Klein bottle group be presented as

```text
pi_1(K) = < r, s | r s r^{-1} = s^{-1} >.
```

Because `mu_N` is abelian, any character from `pi_1(K)` to `mu_N` factors through the abelianization. The relation imposes the condition

```text
chi(s)^2 = 1.
```

Thus for general `N`, the image of `s` must lie in the two-torsion subgroup of `mu_N`; in the intended `mu_2` test this condition is automatic.

For the Catalan half-exponent test,

```text
alpha = 1/2,
N = 2,
nu = w,
chi(gamma_rho) = -1.
```

Choose the classifying map on fundamental groups by

```text
(f_K)_*(r) = gamma_rho,
(f_K)_*(s) = 0.
```

Then

```text
Hol(r) = -1,
Hol(s) = 1.
```

Here `r` is the orientation-reversing generator. The resulting flat `mu_2` local system is exactly the Klein-bottle shadow used in the v2 comparison theorem.

### 5.6 What is not obtained on real test manifolds

The real test manifolds `S^2`, `T^2`, and `K` receive finite local systems only. They are not being treated as complex analytic Deligne bases. The Klein bottle is non-orientable and is not a valid native base for the analytic Deligne-cohomology construction used here.

Consequently, the construction does not produce:

1. a Deligne class on `K`;
2. a Chern class on `K`;
3. a divisor class on `K`;
4. an algebraic cycle on `K`;
5. a proof of algebraicity for the finite local system.

The only object transported to `K` is the finite `mu_2` local system classified by the chosen comparison map. This is precisely the discipline needed for the `mu_2` comparison theorem of Section 6.

## 6. The `mu_2` comparison theorem

The `mu_2` comparison theorem has two layers. The first layer is unconditional: it compares the analytic deck character of the Catalan singular line with the Klein-bottle holonomy of the pulled-back finite local system. The second layer is conditional in general: it attaches the `SO(3)` Floquet phase only after an encoding supplies a gate manifold, a Lyapunov cycle, and an encoding map. Appendix A closes this second layer only for the convention-bound Catalan A1 fixture.

This separation is structural. The analytic and topological objects are constructed in Sections 3 and 5. The dynamical object is not present until an encoding is supplied.

### 6.1 Setup and objects

Fix the Catalan singularity

```text
rho = 1/4,
alpha = 1/2,
N = 2.
```

The branch-killing cover is

```text
w^2 = t_rho = 1 - x/rho,
```

and the Puiseux singular unit is

```text
nu = w.
```

The analytic deck character is

```text
chi_deck: G^2_{1/4} -> mu_2,
chi_deck(zeta_2) = -1.
```

The topological Klein-bottle character is the holonomy

```text
hol_{K,f}: pi_1(K) -> mu_2
```

obtained by the pullback construction of Section 5 for a specified classifying map `f_K`.

The dynamical Floquet character is a map

```text
Phi_{C,G}: pi_1(Gamma_Lyap) -> mu_2
```

or, equivalently, a map to `pi_1(SO(3))` followed by a fixed identification `pi_1(SO(3)) ~= Z/2 ~= mu_2`. This object is conditional on an encoding of the Catalan-type sentence into a gate manifold `G` with a Lyapunov cycle `Gamma_Lyap`.

### 6.2 Intertwining maps

The comparison is not a map between three identical domains. It is a generator comparison through specified intertwining maps into a common `Z/2`.

Analytic intertwining. The deck / monodromy correspondence gives

```text
iota_an: G^2_{1/4} -> Z/2,
```

sending the deck generator to `1 mod 2`, the mod-2 reduction of the positive loop around `rho`.

Klein-bottle intertwining. Use the presentation

```text
pi_1(K) = < r, s | r s r^{-1} = s^{-1} >.
```

Choose the classifying map on fundamental groups by

```text
(f_K)_*(r) = gamma_rho,
(f_K)_*(s) = 0.
```

Composing with mod-2 reduction gives

```text
iota_K: pi_1(K) -> Z/2,
iota_K(r) = 1,
iota_K(s) = 0.
```

This homomorphism respects the Klein-bottle relation because the relation maps to `0` in `Z/2`. Equivalently, the corresponding boundary word maps to a nullhomotopic loop in `V_rho^times`, so the map from the 1-skeleton extends over the 2-cell.

Dynamical intertwining. Under the encoding hypothesis, there is a homomorphism

```text
e_*: pi_1(Gamma_Lyap) -> pi_1(K)
```

sending the generator of the Lyapunov cycle to the orientation-reversing generator `r`. Define

```text
iota_dyn := iota_K · e_*: pi_1(Gamma_Lyap) -> Z/2.
```

This is not unconditional in general. It is part of the encoding data.

Finally, let

```text
epsilon: Z/2 -> mu_2
```

be the character sending the nontrivial class to `-1`.

### 6.3 Unconditional analytic-topological comparison

**Theorem 6.1 (Analytic-topological `mu_2` comparison).** With the Catalan data and the specified Klein-bottle classifying map, the analytic deck character and the Klein-bottle holonomy factor through the same character `epsilon: Z/2 -> mu_2`:

```text
chi_deck = epsilon · iota_an,
hol_{K,f} = epsilon · iota_K.
```

Equivalently, both characters send the corresponding generator to `-1`.

**Proof.** The Catalan singular line has exponent `1/2`, so the deck generator acts on `u=w` by multiplication by `-1`; hence `chi_deck(zeta_2)=-1`. By the specified classifying map, the orientation-reversing generator `r` maps to one positive loop around the puncture, so its pulled-back holonomy is also `-1`; `s` maps to zero and therefore has trivial holonomy. Both maps factor through `epsilon` on the common `Z/2`. ∎

The theorem requires no encoding hypothesis. It is a pure comparison between the Section 3 analytic deck character and the Section 5 finite local system on `K`.

### 6.4 Conditional three-way comparison

**Theorem 6.2 (Three-way `mu_2` comparison, conditional).** Suppose the Catalan encoding hypothesis is verified: there exists a gate manifold `G`, a Lyapunov cycle `Gamma_Lyap`, and an encoding homomorphism `e_*` sending the Lyapunov generator to the Klein-bottle orientation-reversing generator `r`. Suppose further that the `SO(3)` Floquet phase of this cycle is the nontrivial element of `pi_1(SO(3)) ~= Z/2`, identified with `-1 in mu_2`. Then

```text
Phi_{C,G} = epsilon · iota_dyn.
```

Together with Theorem 6.1, this yields a three-way agreement between analytic deck character, Klein-bottle holonomy, and Floquet phase on the specified generator.

**Proof.** Theorem 6.1 supplies the analytic-topological agreement. The conditional hypotheses supply the dynamical generator map and the nontrivial `SO(3)` Floquet phase. Since `e_*` sends the Lyapunov generator to `r`, and `iota_K(r)=1`, we have `iota_dyn(generator)=1`. Applying `epsilon` gives `-1`, which is the assumed Floquet phase. ∎

**Corollary 6.2.C (Catalan A1 closed instance).** For the convention-bound Catalan A1 fixture `A1-sauzin-normalization-v1`, the three-way `mu_2` comparison holds on the specified generator.

**Proof.** Appendix A constructs the Catalan A1 witness datum. Theorem A.7 supplies the Lyapunov loop, spin lift, encoding homomorphism, and commuting `mu_2` diagram required by Theorem 6.2. Applying Theorem 6.2 to this witness datum gives the claimed three-way agreement. ∎

### 6.5 What is and is not unconditional

Theorem 6.1 is unconditional after the analytic realization and Klein-bottle classifying map are fixed. It is mechanized at the finite arithmetic level by the Catalan and Klein-bottle holonomy tests.

Theorem 6.2 remains conditional as a general comparison theorem. Corollary 6.2.C closes only the convention-bound Catalan A1 instance constructed in Appendix A. Theorem A.8 further shows that the `mu_2` output of that Catalan A1 instance is independent of admissible choices of Lyapunov representative and encoding representative. For general sentences, and for odd-prime targets, the encoding hypothesis remains open.

### 6.6 Odd-prime comparison conjecture

**Conjecture 6.3 (Odd-prime comparison).** Let a proof-class generating function have rational local exponent

```text
alpha = a/p
```

with `p` an odd prime. Suppose there exist:

1. a real test manifold `B_p` and classifying map `f_p: B_p -> V_rho^times` detecting the `mu_p` character;
2. an encoding into a gate manifold `G_p` with a Lyapunov cycle whose phase takes values in a `mu_p` target or an explicitly specified `p`-fold covering analogue;
3. intertwining maps from the analytic, topological, and dynamical domains into a common `Z/p`.

Then the analytic deck character, pulled-back `mu_p` holonomy, and dynamical phase should agree on the specified generator.

The conjecture is now well-posed as a finite-cyclic comparison problem. The hard work is the construction of the odd-prime dynamical target and the encoding map. We do not claim this conjecture is a Hodge-conjectural statement or that any instance contributes to the Hodge conjecture.

## 7. Limitations

This section consolidates the open gates of the construction. Each item is tagged with its Severity grade from the Part IV audit of the v2 manuscript, its current status, and the specific obstruction. The section ends with a definition-of-done matrix intended as a static reference for the program's claim boundary.

The discipline is: a limitation is closed only when the corresponding mathematical structure is constructed and the relevant theorem proved, and partially addressed only when the proper framework is in place but specific instances remain case-by-case. Open means the substantive mathematical content is not provided by this paper.

### 7.1 Severity I.1 — The encoding hypothesis: Catalan A1 closed; open in general

The gap. Theorem 6.2 depends on the existence of an encoding of a sentence `phi` as gate constraints in a Lawful Learning architecture, with a Lyapunov cycle in the gate manifold corresponding to a specified loop in the base manifold. The encoding hypothesis asserts that such an encoding exists for the sentence under consideration.

Current status. Appendix A constructs a convention-bound Catalan A1 witness datum and therefore closes the Catalan A1 instance used in Corollary 6.2.C. For general `phi`, and a fortiori for arbitrary sentences in formal theories of arithmetic, the existence of an encoding is not established.

What closure would require in general. A constructive recipe: given a sentence `phi` in a specified class of formal theories, produce explicitly the spectral operator, constraint matrix, gate parameterization, active-set structure, and verification that the active set is in bijection with normal proofs of `phi` counted by the chosen statistic.

What this paper does not claim. We do not claim that arbitrary `phi` admits an encoding. We do not claim that the Catalan A1 fixture generalizes to wider classes by any specified procedure.

### 7.2 Severity II.1 — Transcendental species: Open

The finite-order torsion theorem requires rational local exponents at the dominant singularity. Generating functions that are D-finite but not algebraic, and those that are not D-finite at all, may have algebraic-irrational or transcendental local exponents. In either case, the finite-monodromy character need not land in any `mu_N`, and the Section 3 finite-torsion construction does not apply.

Current status. Bracketed throughout. Section 3 restricts attention to rational exponent classes; Section 6 invokes `alpha = 1/2` explicitly.

### 7.3 Severity II.4 — Absence of a proof-class moduli: Open

The Deligne class is functorial after the analytic realization is fixed. A construction-independent invariant would require either a moduli construction for proof classes or a comparison theorem between Deligne classes constructed from distinct analytic realizations of the same proof class.

Current status. No moduli space is constructed.

### 7.4 Dynamical gates inherited from the v2 integration material: Various

The Lyapunov / Floquet / `SO(3)` dynamical material enters this paper only through Theorem 6.2, Corollary 6.2.C, and Conjecture 6.3. The inherited gates are:

- **II.2: Level-set non-contractibility.** Lyapunov cycle existence requires a non-contractible cycle in the gate manifold. Status: closed for the Catalan A1 fixture by the explicit `SO(3)` generator loop in Appendix A; open in general.
- **II.3: Active boundary as geometric object.** The eigendirection transverse to the active boundary requires smoothing or a piecewise-strata definition. Status: partially addressed by using a piecewise-strata interpretation.
- **III.1: Moving-set proof obligation.** Time-ordered products of projections on varying convex sets require moving-set theory. Status: cited from standard sources, not reproduced.
- **III.2: Floquet theory for proximal-gradient flows.** Smooth Floquet theory requires care when transferred to proximal-gradient dynamics. Status: exact-flow or smooth-approximation regime only.
- **III.3: Energy conservation along level sets.** Exact gradient flow and discrete proximal updates differ by step-size errors. Status: exact-flow limit only.
- **III.4: Floquet phase matching.** The v2 floor-function matching is reformulated as agreement of three `mu_2` realization maps. Status: closed for the Catalan A1 fixture by Corollary 6.2.C; open in general.

Aggregate status. These gates affect only Theorem 6.2, Corollary 6.2.C, and the odd-prime conjecture. The unconditional analytic-topological comparison of Theorem 6.1 is independent of all dynamical material.

### 7.5 Severity V.1 — The regulator framework: Partially addressed

The v2 manuscript produced only finite-order flat data. The integer-valued Chern or regulator part required a separate construction.

This paper introduces the level-1 Deligne unit as the regulator input and the level-2 Deligne cup-product symbol as the regulator-symbol refinement. The framework is therefore in place.

What is not closed. Specific divisor or Chern lifts require additional construction: meromorphic extension, transition functions, or localization. They are not produced by the finite carry cocycle, and they are not produced by the unit alone.

What this paper does not claim. We do not claim that V.1 is closed by the carry cocycle. The carry cocycle is arithmetic of lifted phase indices and has no regulator content.

### 7.6 Explicit Hodge non-claims

These claims are not made by this paper and are enforced by the claim-boundary guard against future drift:

1. **No progress on the Hodge conjecture.** The construction lives in Deligne cohomology of a punctured analytic space and produces invariants of proof classes. It does not produce algebraic cycles on a projective variety.
2. **No algebraicity claim.** The Deligne classes are not asserted to be cycle classes of algebraic subvarieties.
3. **No variation-of-Hodge-structure claim.** CDK-style algebraicity statements for Hodge loci require a polarized variation of Hodge structure as input; we do not establish one.
4. **No Deligne / Chern class on real test manifolds.** Real test manifolds receive only finite local systems.
5. **No algebraic-cycle existence claim.** We do not produce algebraic cycles realizing the Deligne classes, for any variety or prime.
6. **No Hodge relevance claim for Conjecture 6.3.** The odd-prime conjecture is a finite-cyclic comparison problem, not a Hodge-conjectural statement.

### 7.7 Definition-of-done matrix

| Severity | Description | Status | Where |
| --- | --- | --- | --- |
| I.1 | Encoding hypothesis: sentence to gate constraints | Closed for Catalan A1 fixture; open in general | 6.4, 7.1, Appendix A |
| I.2 | Multiplicativity correction term uncharacterized | Closed: character multiplies exactly; carry is lifted-index section defect | 4.5, 4.6 |
| I.3 | Choice of statistic underdetermined | Closed via reduced statistic | 2.2 |
| A.8 | Catalan A1 realization independence | Closed for Catalan A1 fixture; mu_2 output only | Appendix A |
| II.1 | Transcendental species | Open; bracketed | 7.2 |
| II.2 | Lyapunov cycle non-contractibility | Closed for Catalan A1 fixture; open in general | 6.4, 7.4, Appendix A |
| II.3 | Active boundary geometry | Partially addressed by piecewise strata | 7.4 |
| II.4 | Proof-class moduli absent | Open | 7.3 |
| III.1 | Moving-set proof obligation | Cited from standard sources | 7.4 |
| III.2 | Floquet theory for proximal flows | Exact-flow or smooth-approximation regime only | 7.4 |
| III.3 | Energy conservation for discrete flow | Bracketed; exact-flow limit used | 7.4 |
| III.4 | Floquet phase matching | Closed for Catalan A1 fixture; open in general | 6.4, Appendix A |
| III.5 | Odd-prime case | Open as Conjecture 6.3 | 6.6 |
| V.1 | Beilinson regulator framework | Partially addressed: framework in place; Chern lifts case-by-case | 7.5, 4.5 |
| V.2 | Bridge to recognition dynamics | Open; out of scope | Not addressed here |
| V.3 | Implicational/product logic only | Open; predicate logic and arithmetic require extension | Not addressed here |
| V.4 | No empirical validation | Open; harness covers finite arithmetic and Catalan A1 fixture data only | CI-backed invariants |
| Hodge | Progress on Hodge conjecture | Not claimed | 7.6 |
| Hodge | Algebraicity of Deligne classes | Not claimed | 7.6 |
| Hodge | Variation of Hodge structure on proof-class space | Not claimed | 7.6 |
| Hodge | Deligne / Chern class on real `B` | Not claimed | 7.6 |
| Hodge | Algebraic cycle existence | Not claimed | 7.6 |
| Hodge | Hodge relevance of Conjecture 6.3 | Not claimed | 7.6 |

Aggregate. Six items are closed for the Catalan A1 fixture: I.1, I.2, I.3, A.8, II.2, and III.4. Of these, I.1, II.2, and III.4 remain open in general. Two items are partially addressed: II.3 and V.1. The remainder are open, bracketed, out of scope, or not claimed.

### 7.8 What this paper is

The paper constructs a small Hodge-adjacent invariant: a proof-class generating function determines a level-1 Deligne unit whose finite-order shadows recover the v2 phase characters, with strict multiplicativity at the Deligne level and an explicit section-defect carry at the lifted-index level. For Catalan-type sentences with exponent `1/2`, the analytic deck character and the Klein-bottle topological holonomy commute unconditionally. For the convention-bound Catalan A1 fixture, Appendix A constructs the loop, spin lift, encoding homomorphism, finite `mu_2` diagram, and realization-independence theorem needed for the closed Corollary 6.2.C.

The contribution is methodological: when an invariant naturally produces both integral and analytic data, Deligne cohomology is the appropriate framework. The construction is small and inspectable. Its limitations are enumerated above and enforced in CI.

## CI-backed invariants

The test harness under `src/heller_godel/phase_characters.py`, `harness/catalan_a1_harness.py`, and the tests under `tests/` covers the finite arithmetic, monodromy shadows, and Catalan A1 fixture data of this draft. It does not mechanize Deligne cohomology.

Currently covered:

- exact finite-character multiplication;
- carry as lifted-index section defect;
- carry 2-cocycle identity;
- separation of carry from tame-symbol witness;
- Catalan `mu_2` deck character;
- sphere triviality of pulled-back finite local systems;
- torus finite holonomy through winding numbers;
- Klein-bottle `mu_2` holonomy;
- Theorem 6.1 finite comparison;
- Catalan A1 coefficient, Stokes, jump, pairing, commutator, spin-lift, faithful-frame, and filtration checks;
- Catalan A1 Lyapunov loop, encoding homomorphism, and commuting `mu_2` diagram checks.

This executable layer is the finite and fixture-level shadow of the manuscript, not a proof of the full Deligne-cohomological formalism and not a general encoding theorem.

## Appendix-map

- Appendix A records the chain witness, Catalan witness, A1 spin-gate witness, Catalan A1 encoding closure, Catalan A1 realization independence, and remaining general encoding limits.
- Appendix B records carry cocycle tables.
- Appendix C records Deligne cup-product, tame-symbol, and sign conventions.
