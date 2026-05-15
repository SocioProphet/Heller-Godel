# Source Capture — Eisenstein / `mu_3` Support for the p = 3 Front

Status: source-capture support note.  
Scope: preparatory only.  
Date: 2026-05-15.  
Depends on: `docs/proofs/p3_source_inventory.md`.

## Purpose

This capture records the minimal standard mathematical support needed before the repository defines a `p = 3` odd-prime vocabulary scaffold.

The capture is intentionally narrow. It provides support for `mu_3`, Eisenstein integers, and the basic cyclotomic structure around the primitive third root of unity. It does not introduce a `p = 3` comparison theorem, a closed `p = 3` fixture, or an odd-prime dynamical target.

## Source basis

This note records standard textbook-level material from algebraic number theory and representation-adjacent background. Suitable references for later bibliographic expansion include:

1. Henri Cohen, *A Course in Computational Algebraic Number Theory*, especially the standard treatment of cyclotomic fields and rings of integers.
2. Serge Lang, *Cyclotomic Fields I and II*, for cyclotomic-field notation and ramification structure.
3. Jean-Pierre Serre, *A Course in Arithmetic*, for basic algebraic-number-theoretic conventions.
4. James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, for later `A_2` / Lie-theoretic context if that front is opened.
5. William Fulton and Joe Harris, *Representation Theory*, for later `SU(3)` / representation-theoretic context if that front is opened.

No theorem in Paper I / D1 depends on this capture. It is support material for future vocabulary work.

## Primitive third root of unity

Let

```text
omega = exp(2*pi*i/3).
```

Then

```text
omega^3 = 1,
omega != 1,
1 + omega + omega^2 = 0.
```

The group of third roots of unity is

```text
mu_3 = {1, omega, omega^2}.
```

It is cyclic of order 3. A character from a cyclic source of order 3 into `mu_3` is determined by the image of a selected generator.

## Eisenstein integers

The Eisenstein integers are

```text
Z[omega] = {a + b omega : a,b in Z}.
```

Using `omega^2 + omega + 1 = 0`, multiplication remains in the same rank-two `Z`-module with basis `{1, omega}`.

The standard norm is

```text
N(a + b omega) = (a + b omega)(a + b omega^2) = a^2 - a*b + b^2.
```

This norm is integer-valued and multiplicative.

## Unit group

The units of `Z[omega]` are the sixth roots of unity:

```text
Z[omega]^x = {±1, ±omega, ±omega^2} = mu_6.
```

The subgroup relevant to the first odd-prime finite-output target is

```text
mu_3 = {1, omega, omega^2}.
```

For the p = 3 front, `mu_3` should be treated as the finite phase target. The larger unit group `mu_6` should not be silently substituted for `mu_3` without an explicit convention.

## Prime above 3

In `Z[omega]`, the rational prime 3 ramifies. A standard generator of the prime above 3 is

```text
1 - omega.
```

The norm satisfies

```text
N(1 - omega) = 3.
```

This fact is useful for later p = 3 arithmetic scaffolding. It does not by itself produce a dynamical gate, a proof-class realization, or a comparison theorem.

## Minimal vocabulary supported by this capture

This capture supports future definitions of:

1. `mu_3 finite-output map`;
2. `Eisenstein phase target`;
3. `p3 realization datum` if paired with an explicit source and target map;
4. `p3 admissibility conditions` if the selected generator and target phase are specified;
5. `p3 comparison boundary / nonclaim envelope`.

It does not prove those future definitions are satisfied by any fixture.

## Nonclaim envelope

This source capture does not claim:

1. no generic `p` theorem;
2. no closed `p = 3` fixture;
3. no odd-prime dynamical target;
4. no general encoding theorem;
5. no Hodge strengthening;
6. no `A_n` generalization;
7. no gate minimality claim;
8. no `SU(3)` or `A_2` representation-theoretic realization.

The last item is intentional. `SU(3)` and `A_2` may become relevant later, but this capture only establishes the cyclotomic / Eisenstein support needed for `mu_3` vocabulary.

## Relationship to Catalan A1

Catalan A1 remains the `mu_2` baseline. It should not be described through cube-root, Eisenstein, or `mu_3` language.

The `p = 3` front is separate. It asks whether a first odd-prime analogue can be scaffolded using `mu_3` as the finite output target.

## Required next step

A future PR may add a vocabulary-only proof-support note under `docs/proofs/`, using this capture and `docs/proofs/p3_source_inventory.md` as support.

That note should define:

```text
p3 realization datum
mu_3 finite-output map
Eisenstein phase target
p3 admissibility conditions
p3 comparison boundary / nonclaim envelope
```

It should not edit the D1 manuscript theorem stack unless and until a closed fixture or formally stated conjectural scaffold is ready for review.
