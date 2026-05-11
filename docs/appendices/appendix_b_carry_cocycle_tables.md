# Appendix B — Carry Cocycle Tables

This appendix records the finite section-defect carry tables used by Paper I.

The carry cocycle is attached to the coefficient extension

```text
0 -> Z --times L--> Z -> Z/L -> 0.
```

Choose the canonical section

```text
s: Z/L -> Z,
s(a mod L) = [a]_L in {0, ..., L-1}.
```

The carry is

```text
kappa_L(a,b) = (s(a) + s(b) - s(a+b))/L.
```

Equivalently,

```text
s(a) + s(b) = s(a+b) + L kappa_L(a,b).
```

The carry is not a failure of finite-character multiplicativity. The character multiplies exactly in `mu_L`; the carry measures only the failure of the chosen integer section `s` to preserve addition.

## B.1 Tables

For each table, rows and columns are residues in `Z/L`, and the entry in row `a`, column `b` is `kappa_L(a,b)`.

### L = 2

| `kappa_2(a,b)` | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |

### L = 3

| `kappa_3(a,b)` | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 2 | 0 | 1 | 1 |

### L = 4

| `kappa_4(a,b)` | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 1 | 1 |
| 3 | 0 | 1 | 1 | 1 |

### L = 5

| `kappa_5(a,b)` | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 1 | 1 |
| 3 | 0 | 0 | 1 | 1 | 1 |
| 4 | 0 | 1 | 1 | 1 | 1 |

### L = 6

| `kappa_6(a,b)` | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 0 | 1 | 1 |
| 3 | 0 | 0 | 0 | 1 | 1 | 1 |
| 4 | 0 | 0 | 1 | 1 | 1 | 1 |
| 5 | 0 | 1 | 1 | 1 | 1 | 1 |

### L = 7

| `kappa_7(a,b)` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| 3 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |
| 4 | 0 | 0 | 0 | 1 | 1 | 1 | 1 |
| 5 | 0 | 0 | 1 | 1 | 1 | 1 | 1 |
| 6 | 0 | 1 | 1 | 1 | 1 | 1 | 1 |

## B.2 Structural features

Symmetry. `kappa_L(a,b)=kappa_L(b,a)` for all residues `a,b` because the section-defect formula is symmetric in the two arguments.

Normalization. `kappa_L(0,a)=kappa_L(a,0)=0` for all `a`.

Anti-diagonal threshold. For residues `a,b in {0, ..., L-1}`,

```text
kappa_L(a,b) = 0  if a+b < L,
kappa_L(a,b) = 1  if a+b >= L.
```

Thus the one region lies on and above the anti-diagonal `a+b=L`.

Catalan witness. At `L=2`, `kappa_2(1,1)=1`. This is the `mu_2` Catalan carry value at the lifted-index level.

Structural-separation witness. At `L=3`, `kappa_3(1,1)=0`, while Appendix C verifies that the local tame symbol for `f=w`, `g=w` is `-1` under the fixed Paper I convention. Thus the carry can vanish while the tame symbol is nontrivial. The carry cocycle and the Deligne cup-product/tame-symbol branch are distinct secondary structures.

## B.3 Cocycle identity

The carry satisfies the normalized 2-cocycle identity

```text
kappa_L(a,b) + kappa_L(a+b,c)
  = kappa_L(b,c) + kappa_L(a,b+c).
```

This follows by expanding both sides through the section equation. The expression

```text
s(a)+s(b)+s(c)
```

can be reduced either by first grouping `(a,b)` or by first grouping `(b,c)`. The final residue is the same, and the total number of modulus crossings is the same.

## B.4 CI coverage

The tables for levels `2`, `3`, and `4` are regression-tested directly in `tests/test_phase_characters.py`. The cocycle identity is tested exhaustively for levels `2` through `11`.

The tests are intentionally finite. They verify the arithmetic section-defect layer, not any Deligne-cohomology statement.
