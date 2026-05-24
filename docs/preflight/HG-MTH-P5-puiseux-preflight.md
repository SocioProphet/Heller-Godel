# HG-MTH-P5 — p=5 Puiseux Preflight

Status: preflight / theorem-grade candidate  
Dependency: `HG-FND-003` Puiseux singular datum  
Claim class: exact algebraic preflight plus numerical confirmation  
Mathematical content added by this document: candidate Puiseux datum for the arity-5 algebraic branch

This preflight records the `p=5` Puiseux datum for the algebraic generating function

```text
C_p(x) = 1 + x C_p(x)^p.
```

It is a theorem-grade candidate, not yet promoted to an `HG-MTH-*` theorem.

## 1. Critical point

Let

```text
F(x,y) = y - 1 - x y^p.
```

At arity `p`, the critical point is determined by

```text
F(rho_p,y_0)=0,
F_y(rho_p,y_0)=0.
```

The exact solution is

```text
y_0 = p/(p-1),
rho_p = (p-1)^(p-1)/p^p.
```

For `p=5`, this gives

```text
y_0 = 5/4,
rho_5 = 4^4/5^5 = 256/3125.
```

Exact verification:

```text
y_0 - 1 - rho_5 y_0^5 = 0,
1 - 5 rho_5 y_0^4 = 0.
```

## 2. Leading Puiseux coefficient

Write

```text
t = 1 - x/rho_p,
C_p(x) = y_0 - A_p t^(1/2) + b_p t + O(t^(3/2)).
```

The leading balance gives

```text
A_p^2 = 2p/(p-1)^3.
```

For `p=5`,

```text
A_5^2 = 10/64 = 5/32,
A_5 = sqrt(10)/8.
```

This matches the general pattern recorded in the Heller-Winters Puiseux open-problem register.

## 3. Second Puiseux coefficient

The order-`t` balance gives

```text
b_p = (p y_0^(p-1) - binom(p,3)y_0^(p-3)A_p^2)
      / (2 binom(p,2)y_0^(p-2)).
```

For `p=5`, this simplifies to

```text
b_5 = 1/4.
```

Therefore the two-term `p=5` expansion is

```text
C_5(x)
  = 5/4
    - (sqrt(10)/8) (1 - x/rho_5)^(1/2)
    + (1/4) (1 - x/rho_5)
    + O((1 - x/rho_5)^(3/2)).
```

## 4. Numerical confirmation boundary

The leading coefficient `A_5` has been checked numerically against the algebraic branch near `rho_5` to high precision. The second coefficient is numerically consistent with `b_5=1/4`.

The numerical check is supporting evidence only. The proof component is the exact critical-point calculation and coefficient-balance calculation above.

## 5. Relation to prior theorem surfaces

`HG-FND-003` supplies the Puiseux singular-datum frame. `HG-MTH-018` supplies the earlier arity-3 datum. This preflight extends the same algebraic surface to arity 5.

The candidate promotion path is:

1. retain this preflight as the arithmetic derivation surface;
2. add exact rational guards for `A_p^2` and `b_p`;
3. promote a normalized theorem statement only after the proof and normalization convention are reconciled with the existing `HG-MTH-*` numbering.

## 6. Non-claims

This preflight does not prove RH or GRH.

This preflight does not assert any zero-location result.

This preflight does not assert a Hilbert-Pólya operator.

This preflight does not close any Yang-Mills mass-gap statement.

This preflight does not yet promote the `p=5` datum to theorem grade. It records the exact candidate datum and its proof components.
