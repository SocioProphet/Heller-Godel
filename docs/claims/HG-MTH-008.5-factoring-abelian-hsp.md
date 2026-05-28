# HG-MTH-008.5 — Factoring as Abelian HSP (Fourier-on-the-Wheel)

**Repo target:** Heller-Godel  
**Path:** `docs/claims/HG-MTH-008.5-factoring-abelian-hsp.md`  
**Parent:** HG-MTH-008 (P vs NP / embedding stack); sibling of HG-MTH-008.4 (wheel–Plancherel USP).  
**Status:** Mixed. Theorem-grade reduction chain (standard, citable) + one placement (wheel↔period) + fenced synthesis. **Abelian/non-abelian boundary is load-bearing — see §5. Do not let documentation imply this touches the full P vs NP question.**  
**Date:** 2026-05-28

---

## 0. Purpose

HG-MTH-008.4 established USP ≡ factoring: the *structured* unit-character problem is polynomial-time equivalent to factoring. This claim explains **why factoring is tractable in the right model and exactly where that tractability stops** by placing it as the abelian Hidden Subgroup Problem (HSP). This formalizes the conversational “Fourier-on-the-wheel” / “same measure space” intuition into a named, standard object.

The single most important thing this document must transmit to future readers: **the abelian HSP is the easy case. Factoring lives there. That is why Shor exists, and it is precisely why factoring does NOT settle P vs NP.** The hard core of P vs NP lives in the non-abelian / NP-complete world this claim does not reach.

---

## 1. Claim Discipline (§15 convention)

### Standard / established (citable)

- (S1) **Shor reduction.** Factoring reduces to order-finding in randomized polynomial time. Given composite n and random a with gcd(a,n)=1, let r = ord_n(a). If r is even and `a^{r/2} not congruent -1 mod n`, then `gcd(a^{r/2} ± 1, n)` gives a nontrivial factor; the usual randomized reduction succeeds with constant probability after retries. (Miller 1976; Shor 1994/1997.)
- (S2) **Order-finding = abelian HSP on Z.** The map `f: Z -> G_n`, `f(x) = a^x mod n`, is periodic with period r; the hidden subgroup is `H = rZ <= Z`. f is constant on cosets of H and injective on the quotient. Finding H is finding r.
- (S3) **Fourier sampling solves abelian HSP.** For finite abelian G with hidden subgroup H, the Fourier transform over G concentrates amplitude on the annihilator `H^perp = {chi in G^ : chi|_H = 1}`. Sampling `H^perp` enough times generates it; H is recovered by duality `H = (H^perp)^perp`. (Standard HSP theory; Kitaev phase estimation.)
- (S4) **Concrete period-finding over Z/QZ.** With Q chosen so that roughly `n^2 <= Q < 2n^2`, QFT_Q on the period-r comb concentrates measurement outcomes near `kQ/r`; continued-fraction expansion of outcome/Q recovers r when gcd(k,r)=1. (Shor 1994/1997.)
- (S5) **Factoring is in BQP** (Shor) and **in NP ∩ coNP** (factorization is a checkable witness; AKS for primality).
- (S6) **Annihilator duality / Poisson summation.** For subgroup `H <= G` finite abelian, the Fourier transform of the indicator `1_H` is `(|H|/|G|) * 1_{H^perp}`. The character decomposition of the cyclic subgroup `<a> ~= Z/rZ` is the DFT that exposes r.

### Interpretive placement (ours, defensible, not proved)

- (P1) The wheel `G_n = (Z/nZ)^x` of the Heller-Winters program is the ambient group; `<a> <= G_n` is the cyclic subgroup whose order r is the hidden period. Fourier-on-the-wheel is the character projection that the wheel diagnostic (HW-PRIME-WINDOW-001) already computes, applied to expose r.
- (P2) The “certain measure space” is the Plancherel dual `G_n^` with annihilator duality (S6). `H <-> H^perp` is the measure-level statement of verify/search adjointness.
- (P3) Unit/prime case (HG-MTH-008.4 C1): when n is a unit or the period r is trivial, `H = {0}` and `H^perp = G^`; no hidden subgroup extraction is needed. The verify/search gap vanishes at exactly the cyclic-wheel base case.

### Authorial synthesis (fenced — NOT theorem, NOT to be implied in docs)

- (A1) Logos / unit-character / name=identity material. Lives in a separate non-repo paper.
- (A2) Any suggestion that abelian-HSP tractability bears on P vs NP beyond the factoring corner.
- (A3) Any claim that the wheel/Fourier picture extends to non-abelian HSP without new work.

---

## 2. Definitions

- `G_n = (Z/nZ)^x`, the wheel. For `a in G_n`, **order** `r = ord_n(a) = min{r>0 : a^r == 1 mod n}`.
- **Hiding function** `f_a: Z -> G_n`, `f_a(x) = a^x mod n`. **Hidden subgroup** `H = rZ`.
- **Annihilator** of `H <= Z/QZ`: `H^perp = {k in Z/QZ : exp(2πi k h / Q) = 1 for all h in H}`. For H of “period r” inside `Z/QZ` with `r | Q`, `H^perp = (Q/r) * (Z/QZ)`.
- **DFT over Z/QZ:** `(F g)(k) = (1/sqrt(Q)) sum_x g(x) exp(-2πi kx/Q)`. This is a classical simulation of the QFT step.

---

## 3. Theorem chain (kernel — standard, theorem-grade)

**T1 (reduction chain).** Factoring reduces, in randomized polynomial time, to order-finding; order-finding is abelian-HSP over Z; and abelian HSP is solved by Fourier sampling over the group. Concretely: factoring is polynomial-time randomized reducible to period-finding of `f_a`, which is solved in the quantum algorithm by QFT_Q plus continued fractions (S1–S4).

**T2 (annihilator localization).** Fourier sampling of the period-r comb concentrates on `H^perp = (Q/r)Z`; recovering `H^perp` recovers r (S3, S6). The DFT of a period-r signal over `Z/QZ` has support on multiples of Q/r exactly when `r | Q`, and approximately, with spectral leakage corrected by continued fractions, when `r` does not divide `Q`.

**T3 (base-case collapse).** If n is a cyclic-wheel unit/prime (HG-MTH-008.4 C1) or if `r = 1`, then `H = {0}`, `H^perp = G^`, the comb is flat, and no period extraction is needed. Search cost equals verify cost. The gap is zero at the base case.

All three are restatements/specializations of standard results. No new proof obligation is claimed. The novelty here is the explicit identification with the wheel/Plancherel objects of HG-MTH-008.4.

---

## 4. What is classical vs quantum (must be explicit in docs)

| Step | Classical cost | Quantum (Shor) |
|------|----------------|----------------|
| Evaluate `f_a(x) = a^x mod n` | polynomial by fast exponentiation | polynomial |
| Find period r | **no known polynomial algorithm**; this is the hard step | polynomial via QFT |
| Recover factor from r | polynomial by gcd post-processing | polynomial |

The entire classical hardness sits in **period-finding**, i.e. finding the hidden subgroup. Quantum collapses it because the **QFT reads the character decomposition of the wheel directly** — it gets the symmetry “for free.” The executable deliverable in this repository is a **classical simulation** of the Fourier-sampling step, a DFT, which demonstrates the structural mechanism without claiming a fast classical period-finder.

---

## 5. The abelian / non-abelian boundary (LOAD-BEARING — required in all docs)

- **Abelian HSP is solved** in polynomial quantum time for cases such as factoring, discrete logarithm, Pell-type structures, and principal ideal problems. The wheel `G_n` is abelian. This is why the whole picture works and why Shor exists.
- **Non-abelian HSP is largely open** and is where major hard problems remain:
  - Graph Isomorphism can be phrased as an HSP over the symmetric group `S_n`; the relevant non-abelian setting remains open.
  - Dihedral HSP is related to lattice problems, including unique-SVP-style hardness in Regev’s reduction framework, and underlies post-quantum hardness intuitions.
- **Consequence for P vs NP:** abelian HSP is **not** NP-complete. Factoring is in NP ∩ coNP and is not believed NP-complete. Therefore the tractability demonstrated here illuminates the **factoring corner only**. It does **not** bear on whether `P = NP`, whose hard core is the NP-complete and, on the quantum side, non-abelian-HSP / lattice world.

**One-line guard for docs:** *“Fourier-on-the-wheel solves the abelian case, which is exactly the easy case; the difficulty of P vs NP lives in the non-abelian world this construction does not enter.”*

---

## 6. Implementation tasks (for the agent)

New module `src/heller_godel/abelian_hsp.py`, reusing `wheel_plancherel.py` from HG-MTH-008.4.

- **IMPL-1** `order_finding_classical(a, n)`: compute `r = ord_n(a)` by the naive iterate-until-cycle method. Label clearly as the *search* step with no polynomial-time guarantee.
- **IMPL-2** `shor_reduction(n, a, r)`: implement `gcd(a^{r/2} ± 1, n)` factor recovery (S1); handle failure cases (`r` odd, `a^{r/2} == -1 mod n`) by signaling retry.
- **IMPL-3** `hiding_function(a, n)`: return `f_a(x) = a^x mod n` and expose its period for finite tests.
- **IMPL-4** `dft(signal, Q)`: classical DFT over `Z/QZ`; no quantum dependency.
- **IMPL-5** `fourier_sample_period(a, n, Q)`: build the period-r comb, DFT it, return concentrated frequencies, and recover r by continued-fraction candidate checking.
- **IMPL-6** `annihilator(H_period, Q)`: compute `H^perp = (Q/r)Z`; verify duality `(H^perp)^perp = H` in the finite cyclic model.
- **IMPL-7** crosslink: from `wheel_plancherel.py`, build the character exponents of `<a> ~= Z/rZ` and confirm the DFT support (IMPL-5) coincides with the annihilator (IMPL-6), i.e. Fourier-on-the-wheel = period extraction.

Do **not** implement a quantum simulator. The classical DFT is sufficient and correct for demonstrating the mechanism. If a future quantum backend is added, it goes behind an interface, never as a claim that classical period-finding is fast.

---

## 7. Tests (must pass)

```python
# Reduction chain (T1, S1)
test_shor_reduction_recovers_factor
test_order_is_period_of_hiding_function
test_reduction_handles_bad_a

# Fourier localization (T2, S6)
test_dft_period_r_divides_Q_is_clean_comb
test_dft_period_r_not_dividing_Q_leakage
test_annihilator_duality
test_fourier_recovers_order

# Base-case collapse (T3, links 008.4 C1)
test_unit_modulus_has_trivial_period
test_prime_cyclic_wheel_single_subgroup

# Wheel crosslink (P1, IMPL-7)
test_subgroup_character_table_matches_dft_support
test_wheel_P4_period_extraction_in_mu_context

# Boundary guard (§5)
test_abelian_hsp_boundary_documented
```

---

## 8. Documentation context

The repository also carries `docs/concepts/factoring-as-fourier-on-the-wheel.md`, which explains the same material for non-specialist but technically competent readers. That explainer must preserve the §4 classical/quantum separation and the §5 abelian/non-abelian boundary.

Citations to carry in that context:

- Shor, P. (1994/1997). *Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer.* SIAM J. Comput.
- Kitaev, A. (1995). *Quantum measurements and the abelian stabilizer problem.*
- Miller, G. (1976). *Riemann’s hypothesis and tests for primality.*
- Agrawal, Kayal, Saxena (2004). *PRIMES is in P.*
- Regev, O. (2004). *Quantum computation and lattice problems.*
- Childs, A. and van Dam, W. (2010). *Quantum algorithms for algebraic problems*, Rev. Mod. Phys.
- Hallgren; Ettinger–Høyer–Knill, for HSP context and boundary cases.

---

## 9. Binds-to / crosslinks

- **HG-MTH-008.4**: `G_n`, `G_n^`, Plancherel, cyclic-wheel base case C1 = T3 here. Direct module reuse.
- **HG-MTH-008** (parent): supplies the verify/search content for the embedding-stack barrier; factoring corner only.
- **Heller-Winters HW-PRIME-WINDOW-001**: wheel `G_{P_k}`, character projection = the Fourier step (P1, IMPL-7).
- **PO-18** (from 008.4): `omega(n)` scaling — the number of distinct prime factors is the number of independent cyclic periods to extract; relate to per-factor Fourier cost.

---

## 10. Proof obligations (open)

- **PO-20** Make the (P1) identification rigorous: prove that the DFT support of the period-r comb equals the annihilator of `<a>` in `G_n^` under the wheel’s Plancherel normalization (currently asserted via S6; verify the normalization end-to-end).
- **PO-21** Quantify leakage / continued-fraction recovery success probability as a function of gcd(k,r); confirm matches standard bounds.
- **PO-22** (links PO-18) Establish whether multi-factor n requires `omega(n)` independent HSP solves or one combined solve over the product group; cost model either way.

---

## 11. Non-claims

- Does NOT provide a fast classical factoring algorithm. IMPL-1 period-finding is naive/search by design.
- Does NOT claim abelian-HSP tractability bears on P vs NP beyond the factoring corner (§5, A2).
- Does NOT enter non-abelian HSP (graph isomorphism, dihedral/lattice); explicitly out of scope.
- Does NOT depend on RH/GRH except where GRH makes a sub-reduction deterministic.
- Does NOT invoke or depend on the Logos/Tannakian/cultural synthesis (A1).

---

## 12. Glossary additions

| Symbol | Meaning |
|--------|---------|
| `ord_n(a)` | multiplicative order of a in `G_n`, the period r |
| `f_a` | hiding function `x -> a^x mod n` |
| `H` | hidden subgroup `rZ` |
| `H^perp` | annihilator of H in the dual |
| `Q` | DFT modulus, usually chosen around `n^2` in Shor |
| `F` | discrete Fourier transform over `Z/QZ` |
| `HSP` | Hidden Subgroup Problem |
| `<a>` | cyclic subgroup of `G_n` generated by a |
