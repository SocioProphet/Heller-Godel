# Appendix C — Deligne Cup Product, Tame Symbol, and Sign Conventions

This appendix fixes the convention used in Section 4.5.2 and records the load-bearing tame-symbol witness needed by Paper I.

The scope is deliberately bounded. We commit to the Esnault–Viehweg Deligne-cohomology framework used throughout the paper, and to the standard Quillen–Tate tame-symbol normalization stated below. We verify the Catalan `mu_2` witness explicitly. The full general Cech-cocycle bookkeeping for arbitrary `A`, `B`, and analytic factors is recorded as a technical-note obligation, not as a completed computation in this appendix.

## C.1 Convention commitment

The paper uses the analytic Deligne complex convention

```text
Z(p)_D = (Z(p) -> O_X -> Omega_X^1 -> ... -> Omega_X^{p-1}).
```

This is the convention cited in the main text through Esnault–Viehweg.

For level-1 units

```text
f, g in H^0(U, O_U^*),
```

the Deligne cup product is treated as the regulator-symbol class

```text
D(f) cup D(g) in H^2_D(U, Z(2)).
```

Its local boundary at a divisor is the tame-symbol boundary. This is the regulator-symbol branch of the construction and must remain separate from the carry cocycle.

## C.2 Tame-symbol normalization

Let `w` be a local parameter at a divisor `D = {w=0}`. For local units written as

```text
f = w^A h_f,
g = w^B h_g,
```

where `h_f` and `h_g` extend holomorphically and nonvanishingly to `w=0`, use the tame-symbol convention

```text
partial{f,g}
  = (-1)^{v(f)v(g)} (f^{v(g)} / g^{v(f)}) |_{w=0}.
```

Since

```text
v(f)=A,
v(g)=B,
```

this gives

```text
partial{f,g}
  = (-1)^{AB} h_f(0)^B / h_g(0)^A.
```

The inverse formula appears if the cup product or symbol order is reversed. The main manuscript therefore treats this as the fixed Paper I convention and notes that opposite symbol order inverts the boundary value.

## C.3 Catalan witness

For the Catalan singular line,

```text
alpha = 1/2,
N = 2,
w^2 = t_rho,
u = w.
```

The load-bearing local symbol witness is obtained by taking

```text
f = w,
g = w.
```

Thus

```text
A = 1,
B = 1,
h_f(0) = 1,
h_g(0) = 1.
```

Under the convention of C.2,

```text
partial{w,w}
  = (-1)^{1*1} * 1^1 / 1^1
  = -1.
```

This matches the nontrivial `mu_2` phase used by the Catalan comparison theorem.

## C.4 Separation from carry

The same Catalan-like witness also demonstrates that the tame-symbol branch and the carry branch are different structures.

At level `L=3`, take residue indices

```text
A = 1,
B = 1.
```

The section-defect carry is

```text
kappa_3(1,1) = (1 + 1 - 2)/3 = 0.
```

But for the local units `f=w`, `g=w`, the tame symbol is still

```text
partial{w,w} = -1.
```

Thus the carry can vanish while the tame symbol is nontrivial. The Deligne cup-product/tame-symbol structure is not the carry cocycle.

This is the only fact needed to protect Section 4.5 from the earlier mistaken identification.

## C.5 Status of the general formula

The general tame-symbol formula under the Paper I convention is

```text
partial{w^A h_f, w^B h_g}
  = (-1)^{AB} h_f(0)^B / h_g(0)^A.
```

The appendix verifies the load-bearing Catalan case directly and records the general formula as the convention-compatible local expression. A full derivation from Esnault–Viehweg Cech representatives for arbitrary `A`, `B`, `h_f`, and `h_g` is deferred to a technical note.

Therefore Section 4.5.2 should be read as follows:

1. the Deligne cup product is the regulator-symbol refinement of two level-1 units;
2. its local boundary is the tame symbol under the convention fixed here;
3. the Catalan witness is explicitly verified;
4. the general formula is used as the standard local tame-symbol expression, with full Cech bookkeeping deferred;
5. none of this identifies the tame symbol with the carry cocycle.

## C.6 CI relevance

The finite harness cannot mechanize Deligne Cech cocycles. It can, however, keep the arithmetic distinction live:

- `tests/test_phase_characters.py` checks that `kappa_3(1,1)=0`;
- the same test checks that the standard tame symbol for `w,w` is `-1`;
- therefore CI catches any future collapse of the tame-symbol branch into the carry branch at the finite witness level.

This is the correct executable boundary for the present repository.
