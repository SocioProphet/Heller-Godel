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

## B.1 Level 2

Rows and columns are residues `0,1` in `Z/2`.

| `kappa_2(a,b)` | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |

The only nonzero carry occurs when `1+1` crosses the modulus:

```text
s(1)+s(1)=2=s(0)+2*kappa_2(1,1).
```

Thus `kappa_2(1,1)=1`.

## B.2 Level 3

Rows and columns are residues `0,1,2` in `Z/3`.

| `kappa_3(a,b)` | 0 | 1 | 2 |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 1 |
| 2 | 0 | 1 | 1 |

This table is the witness used to separate carry from tame symbol:

```text
kappa_3(1,1)=0,
```

while Appendix C verifies that the local tame symbol for `f=w`, `g=w` is `-1` under the fixed Paper I convention. The two structures are therefore distinct.

## B.3 Level 4

Rows and columns are residues `0,1,2,3` in `Z/4`.

| `kappa_4(a,b)` | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 1 | 1 |
| 3 | 0 | 1 | 1 | 1 |

## B.4 Level 5

Rows and columns are residues `0,1,2,3,4` in `Z/5`.

| `kappa_5(a,b)` | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 0 | 0 | 0 | 1 |
| 2 | 0 | 0 | 0 | 1 | 1 |
| 3 | 0 | 0 | 1 | 1 | 1 |
| 4 | 0 | 1 | 1 | 1 | 1 |

## B.5 General pattern

For residues `a,b in {0, ..., L-1}`,

```text
kappa_L(a,b) = 0  if a+b < L,
kappa_L(a,b) = 1  if a+b >= L.
```

Thus the table is a threshold matrix. The zero region lies below the anti-diagonal `a+b=L`; the one region lies on and above that anti-diagonal.

## B.6 Cocycle identity

The carry satisfies the normalized 2-cocycle identity

```text
kappa_L(a,b) + kappa_L(a+b,c)
  = kappa_L(b,c) + kappa_L(a,b+c).
```

This follows by expanding both sides through the section equation:

```text
s(a)+s(b)+s(c)
```

can be reduced either by first grouping `(a,b)` or by first grouping `(b,c)`. The final residue is the same, and the total number of modulus crossings is the same.

## B.7 CI coverage

The tables for levels `2`, `3`, and `4` are regression-tested directly in `tests/test_phase_characters.py`. The cocycle identity is tested exhaustively for levels `2` through `11`.

The tests are intentionally finite. They verify the arithmetic section-defect layer, not any Deligne-cohomology statement.
