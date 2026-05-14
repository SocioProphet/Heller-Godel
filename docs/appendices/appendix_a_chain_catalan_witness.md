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
The presentation relation $r s r^{-1} = s^{-1}$ is compatible with
$\mathrm{Hol}(s) = +1$: conjugation by $r$ sends $s \mapsto s^{-1}$,
which in $\mu_2$ is the identity since $(-1)^{-1} = -1 = \mathrm{Hol}(s)$
only if $\mathrm{Hol}(s) = \pm 1$ — the trivial assignment $+1$ is consistent.
The holonomy of $r$ is fixed by $(f_K)_*(r) = \gamma_\rho$ and the
Puiseux character $-1$ from Proposition A.2. $\square$

*CI witness:* `tests/test_phase_characters.py` — Klein-bottle $r$-holonomy,
sphere/torus finite holonomy, and Theorem 6.1 common-generator agreement.

## A.4 Minimal `SO(3)` generator for the conditional Floquet corner

The conditional Floquet corner needs a loop representing the nontrivial class in

```text
pi_1(SO(3)) ~= Z/2.
```

A standard representative is the loop

```text
R(t) = rotation about a fixed axis by angle 2*pi*t,
0 <= t <= 1.
```

In `SO(3)`, the endpoints agree because a `2*pi` rotation is the identity. The loop is non-contractible and represents the generator of `pi_1(SO(3))`. Under the double cover

```text
SU(2) -> SO(3),
```

this loop lifts from `+1` to `-1`, hence has `mu_2` phase

```text
-1.
```

This supplies the target value required by Theorem 6.2 once an encoding identifies the Lyapunov cycle with this loop.

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

## A.6 What this appendix verifies

This appendix verifies the following finite and topological claims:

| Claim | Status |
| --- | --- |
| Chain has trivial finite monodromy | Verified by integer exponent |
| Catalan singular line has exponent `1/2` | Verified by Puiseux expansion |
| Catalan branch-killing cover is `w^2=t_rho` | Verified |
| Catalan deck character sends generator to `-1` | Verified |
| Klein-bottle map sends `r` to the puncture loop and `s` to zero | Specified |
| Pulled-back Klein-bottle holonomy is `Hol(r)=-1`, `Hol(s)=1` | Verified |
| `SO(3)` generator has nontrivial `Z/2` class | Standard topological fact |

## A.7 What remains open

This appendix does not close the general encoding hypothesis. It leaves open:

1. a compiler from arbitrary formal sentences to gate constraints;
2. a proof that arbitrary active sets are in bijection with normal proofs counted by the chosen statistic;
3. a general Lyapunov-cycle existence theorem;
4. a moving-set / proximal-flow Floquet theorem for the full dynamics;
5. odd-prime dynamical targets beyond the `SO(3)` `mu_2` case.

Thus Appendix A supports the conditional Catalan comparison by making the finite and topological witness data explicit. It does not upgrade Theorem 6.2 into an unconditional general theorem.

## A.8 CI hooks

**A.8 CI hooks for Appendix A propositions.**

| Proposition | Test file(s) | Coverage |
|---|---|---|
| A.1 Chain null witness | `tests/test_chain_product.py`, `tests/test_phase_characters.py` | Chain product correction; trivial character |
| A.2 Catalan finite analytic witness | `tests/test_catalan_puiseux.py`, `tests/test_phase_characters.py` | Puiseux exponent; $\mu_2$ character |
| A.3 Klein-bottle local-system witness | `tests/test_phase_characters.py` | $r$-holonomy; Theorem 6.1 generator agreement |
| A1 harness (Spin-gate, PR B) | `tests/test_catalan_a1_harness.py` | Hash-chain head; report proof reference |
