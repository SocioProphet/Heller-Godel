# Appendix A — Chain and Catalan Witnesses

This appendix records the finite and topological witness data for the chain and Catalan families. It is intentionally narrower than a general encoding theorem.

The appendix verifies the pieces of the construction that can be made explicit without claiming a universal sentence-to-gate compiler:

1. the proof-family generating functions;
2. the relevant Puiseux singular data;
3. the finite monodromy character;
4. the branch-killing cover and singular unit;
5. the Klein-bottle `mu_2` comparison map for Catalan;
6. the minimal `SO(3)` generator needed by the conditional Floquet comparison.

It does **not** prove the general encoding hypothesis. It does **not** construct a general Lawful Learning compiler from arbitrary sentences to gate constraints. It does **not** establish an empirical or optimization-theoretic convergence theorem for the full architecture.

## A.1 Chain family

**Proposition A.1 (Chain null finite-character witness).**
Let $T_{\mathrm{chain}}(x) = x/(1-x)^2$ be the chain-family generating function.
Then:
1. The radius of convergence is $\rho = 1$.
2. The singularity at $x = \rho$ is an integer-order pole (order 2); no Puiseux
   fractional exponent is present.
3. The finite phase class satisfies $\alpha_{\mathrm{chain}} = 0 \in \mathbb{Z}$,
   so the monodromy character is trivial: $\chi_{\mathrm{chain}} = +1 \in \mu_2$.
4. The chain family therefore constitutes a **null finite-character witness**:
   it contributes no nontrivial $\mu_2$ phase and does not activate the
   Klein-bottle local system.

*Proof.*
The partial-fraction expansion $T_{\mathrm{chain}}(x) = x/(1-x)^2$ is rational
with a single pole at $x=1$ of order 2. No branch cut exists, so no Puiseux
channel opens and $\alpha_{\mathrm{chain}} \in \mathbb{Z}$. The character
$(-1)^{\alpha_{\mathrm{chain}}} = (-1)^0 = +1$. $\square$

*CI witness:* `tests/test_chain_product.py` — chain product correction and
triangular-series non-conflation; `tests/test_phase_characters.py` —
trivial-character coverage for the chain family.

## A.2 Catalan family

**Proposition A.2 (Catalan finite analytic witness).**
Let $C(x) = (1 - \sqrt{1-4x})/2x$ be the Catalan generating function.
Then:
1. The radius of convergence is $\rho = 1/4$.
2. The dominant singularity admits the Puiseux expansion
   $C(x) \sim u_C \cdot t_\rho^{1/2}$ where $t_\rho = 1 - x/\rho$,
   with fractional exponent $\alpha_C = 1/2$.
3. The branch cover resolving the singular channel is $w^2 = t_\rho$,
   with unit $u_C = w$ and deck involution $w \mapsto -w$.
4. The monodromy character of the nonanalytic channel is
   $\chi_C = (-1)^{2 \cdot \alpha_C} = (-1)^1 = -1 \in \mu_2$.
5. The Catalan family therefore constitutes a **nontrivial finite analytic
   witness** activating the $\mu_2$ phase $-1$.

*Proof.*
Standard Puiseux analysis at $x = 1/4$: write $1 - 4x = t_\rho^{\,}$ and
expand $(1-4x)^{1/2} = t_\rho^{1/2}$. The covering map $w^2 = t_\rho$
has deck group $\mathbb{Z}/2$ acting by $w \mapsto -w$, giving monodromy
character $-1 \in \mu_2$. The exponent $\alpha_C = 1/2$ is well-defined
in the selected nonanalytic channel; it does not represent a scalar
monodromy of the whole local germ. $\square$

*CI witness:* `tests/test_catalan_puiseux.py` — Puiseux exponent and
channel locality; `tests/test_phase_characters.py` — Catalan $\mu_2$
character coverage.

## A.3 Klein-bottle finite local-system witness

**Proposition A.3 (Klein-bottle $\mu_2$ local-system witness).**
Let $K$ be the Klein bottle with fundamental group presentation
$$\pi_1(K) = \langle r, s \mid r s r^{-1} = s^{-1} \rangle.$$
Define a classifying homomorphism $f_K\colon \pi_1(K) \to \pi_1(B)$ by
$(f_K)_*(r) = \gamma_\rho$ (the singular-locus generator) and
$(f_K)_*(s) = 0$.
Then:
1. The reduction to $\mu_2$ satisfies $\iota_K(r) = 1$, $\iota_K(s) = 0$.
2. The holonomy of the pulled-back $\mu_2$ local system is
   $\mathrm{Hol}(r) = -1$, $\mathrm{Hol}(s) = +1$.
3. The Klein-bottle classifying map therefore realizes the Catalan
   monodromy character $-1 \in \mu_2$ as the holonomy of the generator $r$,
   constituting a **finite local-system witness** for Theorem 6.1.

*Proof.*
The assignment $\mathrm{Hol}(s) = +1$ is consistent with the presentation
relation: conjugation by $r$ acts on $s$ as inversion, and in $\mu_2$
inversion is the identity, so the relation imposes no obstruction:
$\mathrm{Hol}(r)\,\mathrm{Hol}(s)\,\mathrm{Hol}(r)^{-1} = +1 = \mathrm{Hol}(s)^{-1}$.
The holonomy of $r$ is fixed by $(f_K)_*(r) = \gamma_\rho$ and the
Puiseux character $-1$ from Proposition A.2. $\square$

*CI witness:* `tests/test_phase_characters.py` — Klein-bottle $r$-holonomy,
sphere/torus finite holonomy, and Theorem 6.1 common-generator agreement.

## A.4 A1 spin-gate witness

**Theorem A.4 (A1 Spin-Gate Witness).**
Under convention `A1-sauzin-normalization-v0`, as recorded in
`harness/reference_reports/catalan_a1_report.json`
(hash-chain head `0e8469cc953d2e340b2eda0e929e1e143bde041e82479948c4784801e13b7075`),
the Catalan A1 fixture verifies the following eight checks:

1. **Coefficient enumeration.** The Catalan coefficients $C_n = \binom{2n}{n}/(n+1)$
   are reproduced for $n = 0, \ldots, 19$.
2. **Stokes multiplier.** The square-root Stokes multiplier evaluates to $-1$.
3. **Catalan jump coefficient.** The normalized jump coefficient has absolute
   value $4$.
4. **Pairing preservation.** The symplectic pairing is preserved under the
   active-sector action.
5. **Non-abelian active witness.** The commutator norm of the active-sector
   generators is nonzero, witnessing non-abelian action.
6. **Spin lift.** The central element satisfies $\zeta = -I \in \mathrm{SU}(2)$,
   consistent with the spin-lift of the nontrivial element of $\mu_2$.
7. **Faithful spatial frame.** The spatial spin frame is a faithful
   $\mathrm{Spin}(3) \cong \mathrm{SU}(2)$ representation with
   $\rho_{\mathrm{spatial}}$ the identity on $\mathrm{SU}(2)$.
8. **Active-sector filtration.** The active sector is the irreducible
   two-dimensional spinor representation; the filtration is confirmed.

Therefore the A1 fixture supplies the finite algebraic and spin-side witness
required by the conditional Catalan comparison.

*Gate minimality.* Within admissible A1 gate data, the minimal single-group
realization is $\mathrm{Spin}(3) \cong \mathrm{SU}(2)$ with active sector the
defining two-dimensional spinor representation and central element $\zeta = -I$.
This excludes general ADE groups, $A_n$ for $n \geq 2$, orthogonal active
pairings, $\mathrm{SO}(3)$ as a single-group substitute, and non-isolated or
non-algebraic cases. See `docs/proofs/a1-gate-minimality.md` v2.

*Scope boundary.* Theorem A.4 does not construct $\Gamma_{\mathrm{Lyap}}$
or $e_*$. The Lyapunov cycle and Klein-bottle encoding homomorphism remain
open obligations; see the encoding bridge gap ledger in Appendix A.6.

*CI witness:* `tests/test_catalan_a1_harness.py` — hash-chain head and
committed report proof reference.

## A.5 Catalan encoding datum, stated as a witness schema

A Catalan encoding datum for the conditional theorem consists of:

1. a gate manifold `G_C` containing an `SO(3)` factor or a specified two-fold covering analogue;
2. a Lyapunov cycle `Gamma_Lyap` whose projection to the `SO(3)` factor is the generator loop of A.4;
3. a proof-family active set whose combinatorics is the rooted binary tree grammar;
4. an encoding homomorphism

```text
e_*: pi_1(Gamma_Lyap) -> pi_1(K)
```

sending the Lyapunov generator to the Klein-bottle orientation-reversing generator `r`;
5. a verification that the induced phase is the nontrivial element of `mu_2`.

With these data, Theorem 6.2 is immediate: the Lyapunov generator maps to `r`, `r` maps to the puncture loop, and both evaluate to `-1` in `mu_2`.

## A.6 Encoding bridge gap ledger

Theorem A.4 closes the finite algebraic and spin-side witness for the
Catalan A1 fixture. Two bridge objects remain unbuilt before
Theorem 6.2 can be upgraded to a closed Catalan instance:

| Bridge object | Obligation | Current state |
|---|---|---|
| $\Gamma_{\mathrm{Lyap}}$ | A specified loop or cycle in $G_C$ whose projection to the $\mathrm{SO}(3)$ factor (or two-fold analogue) is the generator of $\pi_1(\mathrm{SO}(3)) \cong \mathbb{Z}/2$, with Floquet phase character $\zeta = -I \in \mu_2$ | Not constructed; spin witness $\zeta = -I$ establishes the target value only |
| $e_*$ | A homomorphism $\pi_1(\Gamma_{\mathrm{Lyap}}) \to \pi_1(K)$ sending the Lyapunov generator to the Klein-bottle orientation-reversing generator $r$ | Not implemented; Appendix A.5 states the schema only |

Until both objects are constructed and verified, Theorem 6.2 remains
conditional in general. Proposition A.2, Proposition A.3, and Theorem A.4
together constitute the maximal closed Catalan witness currently available.

Promotion condition: a future PR may add **Theorem A.7 (Catalan A1 Encoding
Closure)** and **Corollary 6.2.C** only after $\Gamma_{\mathrm{Lyap}}$ and
$e_*$ are explicitly defined, with tests covering both objects.

## A.7 What this appendix verifies

This appendix verifies the following finite and topological claims:

| Claim | Status |
| --- | --- |
| Chain has trivial finite monodromy | Verified by integer exponent |
| Catalan singular line has exponent `1/2` | Verified by Puiseux expansion |
| Catalan branch-killing cover is `w^2=t_rho` | Verified |
| Catalan deck character sends generator to `-1` | Verified |
| Klein-bottle map sends `r` to the puncture loop and `s` to zero | Specified |
| Pulled-back Klein-bottle holonomy is `Hol(r)=-1`, `Hol(s)=1` | Verified |
| A1 fixture supplies finite algebraic and spin-side witness | Verified by pinned harness report |
| Lyapunov cycle and encoding homomorphism | Open; recorded in A.6 |

## A.8 What remains open

This appendix does not close the general encoding hypothesis. It leaves open:

1. a compiler from arbitrary formal sentences to gate constraints;
2. a proof that arbitrary active sets are in bijection with normal proofs counted by the chosen statistic;
3. a general Lyapunov-cycle existence theorem;
4. a moving-set / proximal-flow Floquet theorem for the full dynamics;
5. odd-prime dynamical targets beyond the `SO(3)` `mu_2` case.

Thus Appendix A supports the conditional Catalan comparison by making the finite and topological witness data explicit. It does not upgrade Theorem 6.2 into an unconditional general theorem.

## A.9 CI hooks

**A.9 CI hooks for Appendix A propositions.**

| Proposition | Test file(s) | Coverage |
|---|---|---|
| A.1 Chain null witness | `tests/test_chain_product.py`, `tests/test_phase_characters.py` | Chain product correction; trivial character |
| A.2 Catalan finite analytic witness | `tests/test_catalan_puiseux.py`, `tests/test_phase_characters.py` | Puiseux exponent; $\mu_2$ character |
| A.3 Klein-bottle local-system witness | `tests/test_phase_characters.py` | $r$-holonomy; Theorem 6.1 generator agreement |
| A.4 A1 spin-gate witness | `tests/test_catalan_a1_harness.py` | Hash-chain head; report proof reference |
| A.6 Encoding bridge gap ledger | No closure test yet | Records open $\Gamma_{\mathrm{Lyap}}$ and $e_*$ obligations |
