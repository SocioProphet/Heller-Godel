# Paper I — Deligne-Cohomological Phase Characters from Proof-Class Generating Functions

Working capture for the Heller-Godel proof-character programme. This document supersedes the older floor-function-first framing in `calculus_invariant_characters_v2_1_3.md` where the new Deligne-cohomological rewrite applies.

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
u_{phi,rho} = w^a
```

or, with a nonvanishing analytic factor,

```text
u_{phi,rho} = q^* h_{phi,rho} · w^a.
```

This is a holomorphic unit on the cover and hence determines a level-1 Deligne class

```text
D(u_{phi,rho}) in H^1_D(X_{phi,rho}^circ, Z(1)).
```

The deck transformation `w -> zeta_N w` acts by

```text
u_{phi,rho} -> zeta_N^a u_{phi,rho}.
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
u_phi = w^A q^*h_phi,
u_psi = w^B q^*h_psi,
u_{phi box-times psi} = u_phi u_psi = w^{A+B} q^*(h_phi h_psi).
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
u = w,
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

## 6. Open gates

The following gates remain open and should not be promoted into claims:

1. General encoding hypothesis for arbitrary arithmetic sentences.
2. Construction-independent moduli of analytic realizations.
3. Algebraicity or cycle realization of the resulting classes.
4. Full Deligne-side sign convention proof for the cup-product symbol.
5. D-finite but non-algebraic cases with infinite-order local monodromy.
6. Odd-prime comparison theorem beyond the specified torsion-character target.

## CI-backed invariants

The test harness under `src/heller_godel/phase_characters.py` and `tests/test_phase_characters.py` covers the finite arithmetic and monodromy layer:

- rational exponent normalization in `Q/Z`;
- common branch-killing level;
- deck / monodromy phase indices;
- `p`-primary projection and prime reduction;
- exact multiplicativity of finite characters;
- carry as section-defect cocycle;
- carry cocycle identity;
- tame symbol not equal to carry;
- sphere trivial pullback;
- torus winding-number holonomy;
- Catalan / Klein-bottle `mu_2` holonomy bookkeeping.
