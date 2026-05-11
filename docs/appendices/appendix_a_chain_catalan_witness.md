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

The chain family has generating function

```text
T_chain(x) = sum_{n >= 1} n x^n = x/(1-x)^2.
```

The dominant singularity is

```text
rho = 1.
```

The singular behavior is a pole of integer order. The finite phase class is therefore trivial in `Q/Z`:

```text
alpha_chain = 0 mod Z.
```

Consequently the finite monodromy character is trivial:

```text
chi_chain: pi_1(V_1^times) -> mu_1.
```

The chain family is useful as a null witness. It checks that integer exponents do not create spurious finite torsion phase characters.

## A.2 Catalan family

The Catalan generating function is

```text
C(x) = (1 - sqrt(1 - 4x))/(2x).
```

The dominant singularity is

```text
rho = 1/4.
```

Near `rho`,

```text
C(x) = 2 - 2(1 - 4x)^{1/2} + O(1 - 4x).
```

The finite character attaches to the singular line

```text
(1 - 4x)^{1/2},
```

not to the full function `C(x)` as a scalar-monodromy object.

Write

```text
t_rho = 1 - x/rho = 1 - 4x.
```

The rational exponent is

```text
alpha_C = 1/2.
```

Thus

```text
N = 2,
a = 1.
```

The branch-killing cover is

```text
w^2 = t_rho.
```

On this cover the Puiseux singular unit is

```text
u_C = w.
```

The deck generator acts by

```text
w -> -w,
```

so the deck character is

```text
chi_C(gamma_rho) = -1 in mu_2.
```

This is the analytic side of the `mu_2` comparison theorem.

## A.3 Klein-bottle finite local-system witness

Use the Klein-bottle presentation

```text
pi_1(K) = < r, s | r s r^{-1} = s^{-1} >.
```

For the Catalan `mu_2` test, choose the classifying homomorphism

```text
(f_K)_*(r) = gamma_rho,
(f_K)_*(s) = 0,
```

where `gamma_rho` is the positive local loop around `rho = 1/4` in the punctured monodromy base.

After reducing mod 2, this gives

```text
iota_K(r) = 1,
iota_K(s) = 0.
```

The pulled-back finite local system therefore has holonomy

```text
Hol(r) = -1,
Hol(s) = 1.
```

This is the topological side of Theorem 6.1. It is independent of the dynamical encoding hypothesis.

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

The finite arithmetic side of this appendix is covered by `tests/test_phase_characters.py`:

- Catalan exponent `1/2` normalizes to index `1` at level `2`;
- the Klein-bottle orientation-reversing generator has holonomy index `1` at level `2`;
- the second generator has trivial holonomy;
- the analytic generator and the Klein-bottle generator agree at the common `Z/2` level.
