# HG-MTH-018 — P3.c Puiseux Singularity and Character at p=3 Closure

Identifier: `HG-MTH-018`  
Status: theorem-grade closure document for P3.c; scoped by `HG-MTH-017`.  
Owner: `SocioProphet/Heller-Godel`.  
Track: P3.c under `HG-MTH-012`, after P3.a closure `HG-MTH-014` and P3.b closure `HG-MTH-016`.  
Claim level: theorem-grade within declared `p=3` Puiseux datum and `chi_3` source-identification scope; governed by `A-HG-MTH-004`.

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

## 1a. Formal theorem statement (theorem-grade promotion)

`HG-MTH-018` Theorem. The algebraic function `C_3(x)=1+xC_3(x)^3` has dominant singularity `rho_3=4/27` with `C_3(rho_3)=3/2`, Puiseux exponent `alpha_3=1/2`, and principal-branch expansion:

```text
C_3(x)=3/2 - (sqrt(3)/2)(1 - x/rho_3)^(1/2)
       + (2/3)(1 - x/rho_3)
       + O((1 - x/rho_3)^(3/2)).
```

The monodromy group of `x y^3 - y + 1` over `Q(x)` is `S_3`. The cyclic subgroup `A_3` acts by positive sheet rotation `tau=(123)`. Under the manuscript phase map `k_3(1/2)=1`, the selected character is `chi_3(tau)=omega`.

Proof: four components, each CI-tested:

1. Critical point: `F(rho_3, C_3(rho_3))=0`, `F_y(rho_3, C_3(rho_3))=0` — `HG-FND-003 @ 20499fcaa535e5dd4701aaf42fa582173c3ba746`, `test_p3c_critical_point_data`.
2. Puiseux coefficients `a^2=3/4`, `b=2/3` via coefficient equations — `HG-FND-003`, `test_p3c_scaled_local_expansion_coefficients`.
3. `S_3` monodromy: discriminant `Delta=x(4-27x)` of `xy^3-y+1`, not a square in `Q(x)` — `HG-VOC-006 @ 86b4327b831c79b9ea58c2d56291dffeba0db50f`, `test_cubic_discriminant_identity`.
4. Character identification: `k_3(1/2)=floor(3/2) mod 3=1`, `chi_3=omega` — `HG-VOC-006`, `test_manuscript_phase_map`.

Orientation note: reversing the generator convention gives `chi_3(tau^{-1})=omega^2`. Governed by `A-HG-MTH-004`.

Grade: theorem-grade within declared `p=3` Puiseux datum and `chi_3` source-identification scope.

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

This closure uses the scaled critical-distance convention:

```text
t = 1 - x/rho.
```

Thus `t` is dimensionless and is not the unscaled displacement `rho-x` or `x-rho`.

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

The cubic equation becomes:

```text
z^3 - z^2 + x = 0.
```

It suffices to show that:

```text
f(z)=z^3-z^2+x
```

has no root in `Q(x)`, because a reducible cubic over a field has a linear factor.

Suppose, for contradiction, that `r(x) in Q(x)` is a root:

```text
r^3-r^2+x=0,
x=r^2(1-r).
```

Write `r=a/b` with coprime `a,b in Q[x]`. Then:

```text
x b^3 = a^2(b-a).
```

Since `gcd(a,b)=1`, we also have `gcd(a,b-a)=1`. Therefore `a^2` divides `x` in `Q[x]`. Hence `a` has degree at most `0` with possible linear factor support only at `x`; in either case the degree comparison below rules out a nonconstant rational root. The direct polynomial-root form is cleaner: the divisibility relation forces the denominator to be constant, so any rational-function root would be a polynomial root `r in Q[x]`. Then:

```text
x = r^2(1-r).
```

If `r` is constant, the right-hand side is constant, contradicting degree `1` on the left. If `deg r = n > 0`, then `deg(r^2(1-r))=3n`, which cannot equal `1`. This contradiction proves that `f(z)` has no root in `Q(x)`.

Therefore `z^3-z^2+x` is irreducible over `Q(x)`, and equivalently the original polynomial:

```text
x y^3 - y + 1
```

is irreducible in `y` over `Q(x)`.

The specialization check at `x=1` gives the same diagnostic evidence:

```text
z^3-z^2+1
```

has no rational root, but the closure-grade irreducibility argument is the direct no-root argument over `Q(x)` above.

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

This is not a square in `Q(x)`: a square in `Q(x)` has zeros and poles of even order, while `x(4-27x)` has simple zeros at `x=0` and `x=4/27`. These are odd-order zeros.

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

### 6.5 Manuscript phase convention and Galois agreement

The manuscript defines:

```text
k_p(beta)=floor(p beta) mod p
chi_p^(rho,beta)(T)=exp(2 pi i k_p(beta)/p).
```

For `beta=1/2` and `p=3`:

```text
k_3(1/2)=floor(3/2) mod 3 = 1
chi_3=exp(2 pi i / 3)=omega.
```

The manuscript does not separately define a sheet-orientation convention. The Galois-side analysis supplies the global source: the `A_3` sheet-rotation subgroup. This closure aligns the two by declaring the positive cyclic sheet generator:

```text
tau=(123)
```

and identifying its sheet-rotation character with the manuscript-selected finite phase value:

```text
chi_3(tau)=omega.
```

Thus the manuscript phase-map convention and the Galois sheet-rotation character visibly agree after the positive-generator convention is fixed. Reversing the sheet generator maps the same analytic source to the conjugate value `omega^2`, so the primitive-element selection is convention-dependent up to conjugation.

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

The central compatibility insight is that the local denominator-2 monodromy class has trivial 3-primary projection. Therefore local Puiseux monodromy does not feed into `chi_3`. This confirms the anti-circularity constraint from `HG-MTH-017`: the `mu_3` value cannot be sourced from local square-root monodromy or from a denominator-2 p-primary projection.

The `mu_3` value comes from the manuscript prime-indexed finite phase map and the global sheet-rotation source. `phase_characters.py` is compatibility evidence for this separation, not the analytic source of `chi_3`.

## 8. Heller-Einstein mediation status

This is pure Heller-Godel closure. Heller-Einstein may later represent the orientation convention as a typed realization interface, but this PR neither requires nor authorizes that route.

## 9. Grade declarations

| Object | Grade | Source |
| --- | --- | --- |
| `HG-FND-003` | normalized Tier 1 | `20499fcaa535e5dd4701aaf42fa582173c3ba746` |
| `HG-VOC-006` | normalized Tier 2 | `86b4327b831c79b9ea58c2d56291dffeba0db50f` |
| `HG-MTH-017` (P3.c scope) | method-grade as scope | `docs/framework-core/claim-grammar.md` |
| `HG-MTH-018` (P3.c closure, this PR) | theorem-grade within declared `p=3` Puiseux datum and `chi_3` source-identification scope | this PR |

Full `HG-MTH-011` theorem-grade promotion requires the separate general encoding hypothesis. This promotion does not promote `HG-MTH-011`.

## 10. Retroactive A1 paradigm sharpening

This P3.c closure sharpens the manuscript's interpretation of the A1 `chi_2` paradigm.

At `p=2`, the local square-root sign change, the finite phase-map output, and the available two-sheet algebraic monodromy all coincide in `mu_2`, masking the local-versus-global distinction. At `p=3`, the local square-root exponent still produces `mu_2` local monodromy, while the framework expects `chi_3 in mu_3`. A2 forces the distinction.

The A1 value `chi_2=-1` does not change. Its source identification sharpens: in A1, local square-root monodromy, finite phase reduction, and two-sheet global monodromy agree; in A2, they diverge and the global cubic sheet-rotation source supplies the `mu_3` character.

This is not theorem-grade promotion of A1. It is a framework-reading clarification only.

## 11. Non-claims

1. Does not promote `HG-MTH-011`.
2. Does not promote `HG-MTH-016`.
3. Does not promote `HG-MTH-020`.
4. Does not promote `HG-MTH-021`.
5. Does not close P3.d. The `U(2)` / `zeta_3` correspondence remains downstream.
6. Does not retroactively promote A1 `chi_2` source identification to theorem-grade.
7. Does not extend to `A_n` for `n >= 3`.
8. Does not authorize Heller-Einstein PRs.
9. Does not cross into downstream Clay-program proof claims, including `SocioProphet/yang-mills`.
10. Does not perform downstream repo work.
11. Does not perform numerical verification beyond the symbolic calculations explicitly recorded here.
12. Does not identify local square-root monodromy at `rho_3` as the source of `chi_3 in mu_3`.
13. Does not use `phase_characters.py` as the analytic source of `chi_3`.
14. Does not claim that the orientation convention is independent of the selected cyclic sheet generator.

## 12. Future closure pathway

After this theorem-grade P3.c closure, P3.d scope remains separately governed: `zeta_3` carry defect and `U(2)` correspondence at `p=3`.

P3.d is not opened by this closure and requires separate authorization.

## 13. Identifier and registry

This document assigns:

```text
HG-MTH-018
```

to the P3.c Puiseux singularity and `chi_3` closure at `p=3`.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. This PR updates that registry to record `HG-MTH-018` as theorem-grade within its declared `p=3` Puiseux / `chi_3` scope.
