# HG-MTH-008.4 — Wheel–Plancherel Reformulation of Unit-Character Substantiation

**Repo target:** Heller-Godel  
**Path:** `docs/claims/HG-MTH-008.4-wheel-plancherel.md`  
**Parent claim:** HG-MTH-008 (P vs NP / triple-barrier embedding stack)  
**Status:** Mixed — see Claim Discipline. Contains one theorem-grade equivalence, one one-directional implication, and one synthesis-tier framing. **Do not promote the synthesis tier to theorem grade.**  
**Date:** 2026-05-28

---

## 0. Status and source provenance

This claim formalizes a conversational result. Its purpose is to **separate the provable kernel from the synthesis framing** that generated it, so the agent implements only what is sound.

- Theorem-grade kernel: the polynomial-time equivalence between structured unit-character substantiation and integer factorization.
- One-directional implication: P=NP implies factoring is in P.
- Synthesis tier (NOT to be implemented as theorem): the identification of the trivial character with a “Logos invariant,” and any biconditional linking factoring to P=NP.

The conversational form asserted a biconditional `P=NP <=> factoring in P`. **That biconditional is false** and is corrected here (§5). Only the forward implication holds.

---

## 1. Claim Discipline (per §15 convention)

### Standard / established (citable, not ours)

- (S1) Integer factoring is in NP ∩ coNP. A factorization is a polynomial-size witness verifiable in P (multiplication + AKS primality, Agrawal–Kayal–Saxena 2004).
- (S2) Computing Euler’s totient phi(n) is randomized polynomial-time equivalent to factoring n (Miller 1976; deterministic under GRH).
- (S3) Computing the abelian group structure of `(Z/nZ)^x` — i.e. its invariant-factor / CRT-cyclic decomposition — is randomized polynomial-time equivalent to factoring n. Follows from (S2) + CRT + Gauss primitive-root theorem.
- (S4) `(Z/nZ)^x` is cyclic iff `n in {1, 2, 4, p^k, 2p^k}` for odd prime p (Gauss, primitive-root theorem).
- (S5) Plancherel theorem on a finite abelian group G: for `f: G -> C`,
  `sum_g |f(g)|^2 = (1/|G|) sum_chi |fhat(chi)|^2`,
  with `fhat(chi) = sum_g f(g) conjugate(chi(g))`. The dual `G^` is isomorphic to G for finite abelian G.
- (S6) If P = NP then every problem in NP is in P; in particular factoring is in P (from S1).

### Interpretive placement (ours, defensible, not proved)

- (P1) The trivial character chi_0 in `G_n^` is the “unit character” / wheel fixed point. Its *structured* form (expressed in CRT-factor coordinates) is the object of interest, not the bare constant function.
- (P2) The wheel `G_{P_k} = (Z/P_kZ)^x` of the Heller-Winters prime-window program (HW-PRIME-WINDOW-001) is the k-th primorial instance of the general `G_n` studied here.
- (P3) The “certain measure space” is the Plancherel-normalized dual (S5). Clean substantiation of chi_0 in factor coordinates is well-posed exactly when the CRT decomposition of `G_n^` is known.

### Authorial synthesis (NOT to be implemented or cited as result)

- (A1) Identification of chi_0 with the CPGF “Logos invariant” / Tannakian unit motive.
- (A2) Any reading of monotheism/polytheism as CRT factoring of a cultural wheel.
- (A3) Any biconditional between factoring and P=NP. (Explicitly retracted in §5.)

---

## 2. Definitions

Let `n >= 1`. Write `G_n = (Z/nZ)^x`, the multiplicative group of units mod n, with character group `G_n^ = Hom(G_n, C^x)`.

**Definition (CRT-structured trivial character).**
Given the prime-power factorization `n = prod_i p_i^{e_i}`, CRT gives
`G_n ~= prod_i G_{p_i^{e_i}}`, and `G_n^ ~= prod_i G_{p_i^{e_i}}^`.
The trivial character factors as `chi_0 = tensor_i chi_0^{(i)}`, where `chi_0^{(i)}` is the trivial character of the i-th factor.

**Definition (USP — Unit-Substantiation Problem).**
`USP(n)`: output
(a) the prime-power factorization `{(p_i, e_i)}`;
(b) the cyclic decomposition of each `G_{p_i^{e_i}}` (order and a generator / primitive root);
(c) `chi_0` expressed in the resulting factor coordinates.

USP requires the *structured* object (a)–(c), not merely the constant-1 function. The bare chi_0 as the all-ones function is trivially computable and is NOT what USP asks for; see §5 Pitfall.

**Definition (cyclic-wheel modulus).** `n` is a *cyclic-wheel modulus* iff `G_n` is cyclic, iff (S4) `n in {1, 2, 4, p^k, 2p^k}` for odd prime p.

---

## 3. Theorem (kernel — theorem-grade)

**Theorem T1 (USP ≡ factoring).**
USP is in randomized P if and only if integer factorization is in randomized P. Deterministically under GRH.

*Proof.*
(<=) Given a factoring oracle, factor n to get (a). Each factor group `G_{p^e}` is cyclic of order `p^{e-1}(p-1)` for odd p, with standard 2-power exceptions. A generator is found in randomized polynomial time given the factorization of the group order, using standard primitive-root search. This yields (b), and (c) is immediate.

(=>) Given a USP oracle, output (a) directly contains the factorization of n. So factoring is in the same complexity class as USP. ∎

**Corollary C1 (cyclic-wheel base case).**
For cyclic-wheel moduli (S4), USP restricted to that family is in P without a general factoring oracle: `n=1` trivial; `n=p` prime detected by AKS, `G_p ~= Z/(p-1)` with primitive root found in randomized polynomial time; `n in {4, p^k, 2p^k}` analogous. The “identity or prime” regime is exactly where chi_0 is substantiable with a single cyclic generator and no nontrivial CRT split.

---

## 4. Proposition (P=NP link — one direction only)

**Proposition P-fwd.** If P = NP then USP is in P deterministically.

*Proof.* By (S1) factoring is in NP. By (S6) `P=NP => factoring in P` deterministically. By T1, `factoring in P => USP in P`. ∎

**Non-implication (recorded, NOT a theorem).** The converse `USP in P => P=NP` is **not** established and is believed false: see §5.

---

## 5. Correction of the conversational biconditional (REQUIRED reading)

The originating conversation asserted `P=NP <=> factoring in P`. This is **false** as a biconditional and must not be implemented or cited.

- Forward (`P=NP => factoring in P`): TRUE (Prop P-fwd).
- Converse (`factoring in P => P=NP`): **NOT believed true.** Factoring is in NP ∩ coNP and is not known (and widely conjectured not) to be NP-complete. If factoring were NP-complete, NP = coNP would follow, which is believed false. Hence an efficient factoring algorithm would *not* collapse P and NP.

**Pitfall to encode in tests.** The bare trivial character (constant function 1) is computable in O(1) and requires no factoring. The factoring-hardness lives entirely in the *structured* decomposition (a)–(c). Any implementation that “computes chi_0” by returning the constant function and claims to have solved USP is wrong. The test suite must assert that USP returns the factor structure, and that withholding the factorization makes (b)/(c) unavailable.

---

## 6. Implementation tasks (for the GitHub agent)

Target a new module in Heller-Godel, with a crosslink to the Heller-Winters wheel diagnostic.

- **IMPL-1** `wheel_plancherel.py`: construct `G_n = (Z/nZ)^x` for given n — element list, order phi(n), group operation. Pure, no theorem-grade factoring shortcut.
- **IMPL-2** character utilities: build `G_n^` for n a cyclic-wheel modulus directly (single generator -> character table as powers of a root of unity in `mu_{phi(n)}`); verify orthogonality and Plancherel (S5).
- **IMPL-3** `usp(...)`: implement USP(n) as defined — factor n, decompose `G_n` via CRT into cyclic factors with generators, express chi_0 in factor coordinates. Expose a `factoring_oracle` injection point so the equivalence T1 is demonstrated structurally (oracle in => USP fast; USP out => factorization recovered).
- **IMPL-4** cyclic-wheel predicate: decide the cyclic-wheel predicate; verify against the closed form `{1,2,4,p^k,2p^k}` (S4) by an independent group-exponent criterion for n up to a bound.
- **IMPL-5** crosslink: import the wheel `G_{P_k}` from the Heller-Winters `prime-window-repunit-diagnostic` and confirm it is the primorial instance `G_{P_k}` of IMPL-1 (P2). Character values land in `mu_{exp(G_{P_k})}` (e.g. `mu_12` at `P_4 = 210`).

---

## 7. Tests (concrete, must pass)

```python
# T1 structural equivalence
test_usp_with_oracle_is_poly
test_usp_output_recovers_factorization
test_factoring_reduces_to_usp

# Cyclic-wheel base case (C1, S4)
test_cyclic_wheel_predicate_matches_closed_form
test_prime_modulus_has_single_generator
test_composite_noncyclic_requires_crt_split

# Plancherel / measure (S5)
test_plancherel_identity_holds_on_G_n
test_character_orthogonality

# Pitfall guard (§5)
test_constant_function_is_not_usp_solution
test_withholding_factorization_blocks_structured_chi0

# Crosslink (P2 / IMPL-5)
test_wheel_P4_equals_G_210
test_character_values_in_mu_12_at_P4
```

Implementation note: the checked crosslink establishes the primorial instance and exponent landing claim inside this repository. Direct import from Heller-Winters remains a later cross-repo integration task because this repo currently has no vendored Heller-Winters package dependency.

---

## 8. Binds-to / crosslinks

- **HG-MTH-008** (parent): T1 supplies the arithmetic content for the Level 2–3 (generating-function -> analytic-continuation) barrier. The complexity phase-transition Puiseux exponent `alpha = 1/2` (HG-MTH-008.1) is the *same* Galois-involution fixed point `sigma_11: zeta_12 -> zeta_12^{-1}` appearing in the chi_3 / 1-half-five-ways result (Heller-Einstein). Record as a placement, not a proof.
- **HG-MTH-009** (BSD): shared L-function structure `L(s, chi) = prod_p (1 - chi(p) p^{-s})^{-1}` over `G_n^`.
- **Heller-Winters HW-PRIME-WINDOW-001**: `G_{P_k}` wheel, repunit `R_k = (10^k-1)/9`, Stieltjes tower. IMPL-5 makes the identification concrete.
- **`A_p^2 = 2p/(p-1)^3`** (arity scaling): open question whether the USP cost scales with the number of distinct prime factors `omega(n)`; see PO-18.

---

## 9. Proof obligations (open)

- **PO-16** Verify Plancherel-measure compatibility of USP across all n (not just cyclic-wheel): confirm the dual normalization is consistent under CRT product.
- **PO-17** Make the cyclic-wheel ⇔ uniquely-substantiable-chi_0 correspondence rigorous: state precisely “single generator ⇒ chi_0 uniquely identified without CRT split.”
- **PO-18** Test whether structured-USP cost scales with `omega(n)` (number of distinct prime factors) and whether that scaling matches `A_p^2 = 2p/(p-1)^3` for the per-prime factor cost. Empirical first, then conjecture.
- **PO-19** (synthesis crosslink, LOW priority, do NOT block on this) Record — without asserting — the CPGF reading that the structured chi_0 is the computational substantiation of the Tannakian unit object. Marked (A1); kept out of the theorem chain.

---

## 10. Non-claims

- This claim does NOT assert P != NP or P = NP.
- This claim does NOT assert factoring notin P.
- This claim does NOT assert the biconditional factoring <=> P=NP (explicitly retracted, §5).
- This claim does NOT depend on RH, GRH (except where GRH is named to make a reduction deterministic), or the CPGF/Logos synthesis.
- The Galois / Logos / cultural-projection material is synthesis tier and lives in a separate document, not here.

---

## 11. Glossary additions

| Symbol | Meaning |
|--------|---------|
| `G_n` | `(Z/nZ)^x`, the wheel at modulus n |
| `G_n^` | character group of `G_n` |
| `chi_0` | trivial (unit) character |
| `chi_0^{(i)}` | trivial character of i-th CRT factor |
| `phi(n)` | Euler totient |
| `omega(n)` | number of distinct prime factors of n |
| `P_k` | k-th primorial, `prod_{p <= p_k} p` |
| `R_k` | repunit `(10^k - 1)/9` |
| `mu_m` | group of m-th roots of unity |
| `USP` | unit-substantiation problem (Def §2) |
