# HG-EXP-008.9 Summary — S4 Cayley Spectrum Atlas

Status: partial atlas / S4 positive-control tranche.  
Date: 2026-05-29.

## Headline finding

The S4 Cayley-spectrum calibration instrument is now positive on the locked EMR-image sanity row and three additional S4 generator sets. Across all four S4 generator choices, the dimension-spectrum partition is invariant:

- on-circle count: 2;
- off-circle count: 22;
- total count: 24;
- alpha: 1/12.

The eigenvalues inside the off-circle blocks vary with the generator set, as expected. This confirms the intended distinction: the dimension-spectrum partition is group-determined, while the block eigenvalues are generator-dependent.

## Atlas rows

| Generator set | S size | On-circle | (2,2) eigenvalues | standard eigenvalues | sign-twist standard eigenvalues |
|---|---:|---|---|---|---|
| `emr_1432_132` | 4 | `4 0` | `-3 1` | `-2.56155281281 -1 1.56155281281` | `-1 0 3` |
| `transposition_12_cycle_1234` | 3 | `3 -3` | `-1.73205080757 1.73205080757` | `-2.41421356237 0.414213562373 1` | `-1 -0.414213562373 2.41421356237` |
| `adjacent_transpositions` | 3 | `3 -3` | `-1.73205080757 1.73205080757` | `-0.414213562373 1 2.41421356237` | `-2.41421356237 -1 0.414213562373` |
| `star_transpositions` | 3 | `3 -3` | `0 0` | `-1 2 2` | `-2 -2 1` |

## EMR-image sanity row

For `S4` with `g=(1,4,3,2)` and `h=(1,3,2)`, symmetrized as `{g,g^-1,h,h^-1}`:

- vertices: 24;
- degree: 4;
- trace: 0;
- on-circle spectrum: `(4,0)`;
- off-circle block eigenvalues are locked in `data/exp_008_9_results.csv`.

## Caveats

This is not yet the full HG-EXP-008.9 atlas. It is the S4 positive-control atlas over the generator sets covered by the declared S4 matrix fixtures. S3/S5 and A_n/D_n coverage should be added only after their matrix fixtures are declared with the same convention discipline and trace-vs-character tests.

This report makes no expander or Ramanujan claim. It has no P vs NP, RH, GRH, or Artin implication. It is finite-group empirical infrastructure only.

## Follow-on

The next tranche should either:

1. add S3/S5 matrix fixtures with trace-vs-character gates and extend the atlas; or
2. write the 008.8-vs-008.9 comparison note for the currently available S4 positive-control slice.
