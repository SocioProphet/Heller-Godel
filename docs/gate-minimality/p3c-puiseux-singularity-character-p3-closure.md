# HG-MTH-018 — P3.c Puiseux Singularity and Character at p=3 Closure

Identifier: `HG-MTH-018`  
Status: closure document for P3.c; scoped by `HG-MTH-017`.  
Owner: `SocioProphet/Heller-Godel`.  
Track: P3.c under `HG-MTH-012`, after P3.a closure `HG-MTH-014` and P3.b closure `HG-MTH-016`.  
Claim level: method-grade modulo candidate-`HG-FND-003` and candidate-`HG-VOC-006`.

## 1. Statement of closure

P3.c closure verifies the Puiseux singular datum of the algebraic function:

```text
C_3(x)=1+x C_3(x)^3
```

Closure establishes:

```text
rho_3 = 4/27
C_3(rho_3)=3/2
alpha_3 = 1/2
```

and derives the principal-branch expansion:

```text
C_3(x)=3/2 - (sqrt(3)/2)(1 - x/rho_3)^(1/2)
       + (2/3)(1 - x/rho_3)
       + O((1 - x/rho_3)^(3/2)).
```

For Q4, this closure selects option (b) at the source-identification level: the non-local `mu_3` source is the cyclic `A_3 ~= Z/3` sheet-rotation subgroup inside the full `S_3` monodromy structure of the cubic algebraic curve:

```text
x y^3 - y + 1 = 0.
```

The manuscript finite phase map selects:

```text
k_3(1/2)=floor(3/2) mod 3 = 1
chi_3 = exp(2 pi i / 3) = omega.
```

The analytic sheet-rotation source determines a nontrivial `mu_3` character once a cyclic generator is chosen. This closure declares the positive sheet generator `tau=(123)` and sets `chi_3(tau)=omega`. Reversing orientation gives the conjugate `omega^2`.

## 2. Verification strategy

This closure selects W2 + W3 from `HG-MTH-017`.

W2 verifies Q1-Q3 by local expansion at the critical point of:

```text
F(x,y)=y-1-x y^3.
```

W3 verifies Q4 source-identification by treating:

```text
x y^3 - y + 1 = 0
```

as a degree-three algebraic cover over `Q(x)`.

W4 is compatibility analysis only. It is not the analytic source of `chi_3`.

Option (a) is rejected because local square-root monodromy is `mu_2`-type data. Option (c) is not selected as primary because finite arithmetic alone would be circular without independent analytic input. Option (d) is not selected for source-identification because the cubic sheet-rotation source supplies a concrete `mu_3` source, but the primitive element requires an orientation convention.

## 3. Q1 — Singularity location

Let:

```text
F(x,y)=y-1-x y^3.
```

The critical system is:

```text
F(x,y)=0
F_y(x,y)=0.
```

Since:

```text
F_y(x,y)=1-3xy^2,
```

we have:

```text
x=1/(3y^2).
```

Substitute into `F=0`:

```text
y - 1 - (1/(3y^2))y^3 = 0
y - 1 - y/3 = 0
(2/3)y = 1
y = 3/2.
```

Then:

```text
x = 1/(3(3/2)^2)=4/27.
```

Therefore:

```text
rho_3 = 4/27
C_3(rho_3)=3/2.
```

## 4. Q2 — Local Puiseux exponent

Set:

```text
rho = 4/27
y0 = 3/2
t = 1 - x/rho
x = rho(1-t)
y = y0 + s.
```

Substitution gives:

```text
F(rho(1-t), y0+s)
= -(2/3)s^2 - (4/27)s^3
  + t(1/2 + s + (2/3)s^2 + (4/27)s^3).
```

The leading balance is:

```text
-(2/3)s^2 + (1/2)t = 0.
```

Hence:

```text
s^2 = (3/4)t
s = +/- (sqrt(3)/2)t^(1/2).
```

Therefore:

```text
alpha_3 = 1/2.
```

This confirms that the local branch gives square-root, `mu_2`-type local monodromy; it is not the direct source of `chi_3 in mu_3`.

## 5. Q3 — Explicit Puiseux expansion

Write:

```text
s = a u + b u^2 + O(u^3)
u = t^(1/2).
```

The coefficient of `u^2` gives:

```text
a^2 = 3/4,
a = +/- sqrt(3)/2.
```

The coefficient of `u^3` gives:

```text
-(4/3)ab - (4/27)a^3 + a = 0.
```

Since `a^2=3/4`, divide by `a`:

```text
-(4/3)b - (4/27)(3/4) + 1 = 0
-(4/3)b - 1/9 + 1 = 0
b = 2/3.
```

The principal branch is selected by `C_3(0)=1`. For `0 < x < rho_3`, the branch approaches `3/2` from below, so `s<0` and:

```text
a = -sqrt(3)/2.
```

Thus:

```text
C_3(x)=3/2 - (sqrt(3)/2)(1 - x/rho_3)^(1/2)
       + (2/3)(1 - x/rho_3)
       + O((1 - x/rho_3)^(3/2)).
```

## 6. Q4 — Character source

### 6.1 Option (a) rejected

The local Puiseux exponent is `1/2`. Local traversal changes the square-root channel by sign:

```text
(1 - x/rho_3)^(1/2) -> -(1 - x/rho_3)^(1/2).
```

This is `mu_2` local monodromy. It cannot directly produce `chi_3 in mu_3`.

### 6.2 Irreducibility over Q(x)

Use the reciprocal variable:

```text
z = 1/y.
```

Then the cubic becomes:

```text
z^3 - z^2 + x = 0.
```

It is monic in `z` over `Q[x]`. If reducible over `Q(x)`, Gauss's lemma gives a nontrivial factorization over `Q[x][z]`. Specializing `x=1` gives:

```text
z^3 - z^2 + 1.
```

This cubic has no rational root because the only rational-root candidates are `1` and `-1`, and:

```text
1 - 1 + 1 = 1
-1 - 1 + 1 = -1.
```

Therefore the specialization is irreducible over `Q`. This supports irreducibility of the generic cubic over `Q(x)` for this closure. Equivalently, the original polynomial `x y^3 - y + 1` is irreducible in `y` over `Q(x)`.

### 6.3 Discriminant and group identification

For:

```text
a y^3 + b y^2 + c y + d = 0
```

with:

```text
a=x, b=0, c=-1, d=1,
```

the discriminant is:

```text
Delta = 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2
      = 4x - 27x^2
      = x(4 - 27x).
```

This is not a square in `Q(x)` because it has odd-order zeros at `x=0` and `x=4/27`.

An irreducible cubic over a characteristic-zero field has Galois group a transitive subgroup of `S_3`. The transitive subgroups of `S_3` are `A_3` and `S_3`; the group lies in `A_3` exactly when the discriminant is a square. Therefore the group is:

```text
S_3.
```

### 6.4 A_3 sheet-rotation source

Inside `S_3`, the normal cyclic subgroup:

```text
A_3 ~= Z/3
```

is generated by a 3-cycle and acts by cyclic permutation of the three sheets of the cubic cover.

The nontrivial characters of `A_3` take values in:

```text
mu_3 = {1, omega, omega^2}
omega = exp(2 pi i / 3).
```

With positive generator:

```text
tau=(123),
```

this closure uses:

```text
chi_3(tau)=omega.
```

The reverse generator gives the conjugate value `omega^2`. Thus the analytic source of a `mu_3` character is the global `A_3` sheet-rotation subgroup, not the local square-root branch at `rho_3`.

### 6.5 Primitive element convention

The manuscript defines:

```text
k_p(beta)=floor(p beta) mod p
chi_p^(rho,beta)(T)=exp(2 pi i k_p(beta)/p).
```

For `beta=1/2` and `p=3`:

```text
k_3(1/2)=1
chi_3=omega.
```

The manuscript does not separately define a sheet-orientation convention. This closure therefore declares the positive cyclic sheet generator `tau=(123)` and maps it to `omega`. The source is option (b); the primitive-element selection is convention-dependent up to conjugation.

## 7. W4 compatibility check

The manuscript finite phase map gives:

```text
k_3(1/2)=1,
chi_3=omega.
```

The `phase_characters.py` module has a denominator-level finite-character interface. For local exponent `1/2`, the expected behavior is:

```text
normalize_exponent("1/2") -> PhaseExponent(numerator=1, denominator=2)
phase_index("1/2") -> (1, 2)
p_primary_projection(1, 2, 3) -> (0, 1)
prime_reduction(1, 2, 3) -> (0, 1)
```

This is consistent with the closure: the p-primary projection of local denominator-2 monodromy is trivial at prime 3, so local Puiseux monodromy is not the source of `chi_3`. The `mu_3` value comes from the manuscript prime-indexed finite phase map and the global sheet-rotation source.

## 8. Heller-Einstein mediation status

This is pure Heller-Godel closure. Heller-Einstein may later represent the orientation convention as a typed realization interface, but this PR neither requires nor authorizes that route.

## 9. Grade declarations

| Object | Grade | Source |
| --- | --- | --- |
| `HG-FND-003` | candidate; registry normalization pending | `docs/framework-core/distance-classification.md` |
| `HG-VOC-006` | candidate; registry normalization pending | `docs/framework-core/distance-classification.md` |
| `HG-MTH-017` (P3.c scope) | method-grade as scope | PR #88 |
| `HG-MTH-018` (P3.c closure, this PR) | method-grade modulo candidate-`HG-FND-003` and candidate-`HG-VOC-006` | this PR |

Full `HG-MTH-011` theorem-grade promotion requires:

```text
HG-FND-001
HG-FND-002
HG-FND-003
HG-VOC-006
HG-FND-006
HG-FND-007
```

P3.c adds `HG-FND-003` and `HG-VOC-006`, two of the six cumulative modulo-candidate dependencies.

## 10. Retroactive A1 paradigm sharpening

This P3.c closure sharpens the manuscript's interpretation of the A1 `chi_2` paradigm.

At `p=2`, the local square-root sign change and finite phase-map output coincide in `mu_2`, masking the local-versus-global distinction. At `p=3`, the local square-root exponent still produces `mu_2` local monodromy, while the framework expects `chi_3 in mu_3`. A2 forces the distinction.

The A1 value `chi_2=-1` does not change. Its source identification sharpens: in A1, local square-root monodromy and finite phase reduction agree; in A2, they diverge and the global cubic sheet-rotation source supplies the `mu_3` character.

This is not theorem-grade promotion of A1. It is a framework-reading clarification for future `HG-FND-003` and `HG-VOC-006` normalization.

## 11. Non-claims

1. Does not promote `HG-FND-003` from candidate.
2. Does not promote `HG-VOC-006` from candidate.
3. Does not close P3.d. The `U(2)` / `zeta_3` correspondence remains downstream.
4. Does not promote `HG-MTH-011`.
5. Does not retroactively promote A1 `chi_2` source identification to theorem-grade.
6. Does not extend to `A_n` for `n >= 3`.
7. Does not authorize Heller-Einstein PRs.
8. Does not cross into downstream Clay-program proof claims, including `SocioProphet/yang-mills`.
9. Does not normalize `HG-FND-*` or `HG-VOC-*` surfaces.
10. Does not perform numerical verification beyond the symbolic calculations explicitly recorded here.
11. Does not identify local square-root monodromy at `rho_3` as the source of `chi_3 in mu_3`.
12. Does not use `phase_characters.py` as the analytic source of `chi_3`.
13. Does not claim that the orientation convention is independent of the selected cyclic sheet generator.

## 12. Future closure pathway

After this P3.c closure merges, P3.d scope is unlocked: `zeta_3` carry defect and `U(2)` correspondence at `p=3`, attaching to candidate-`HG-FND-006` and candidate-`HG-FND-007`.

P3.d is not opened by this closure and requires separate authorization.

## 13. Identifier and registry

This document assigns:

```text
HG-MTH-018
```

to the P3.c Puiseux singularity and `chi_3` closure at `p=3`.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. This PR updates that registry to register `HG-MTH-018` and record its grade ceiling as method-grade modulo candidate-`HG-FND-003` and candidate-`HG-VOC-006`.
