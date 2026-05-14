# Singularity-Class Scope Boundary

Status: aligned with `docs/proofs/a1-gate-minimality.md` v2.

This document records the scope boundary for invoking the A1 gate-minimality claim and its Catalan reference harness.

## In-scope base declaration

The base claim is scoped to:

| Dimension | Value |
| --- | --- |
| Singularity type | algebraic isolated `A_1`, local model `sqrt(t)` |
| Active set | `dim_C V_A = 2` |
| Pairing | symplectic `Q_A`, Frobenius-Schur indicator `epsilon = -1` |
| Spatial action target | `Spin(3) ~= SU(2)`, faithful |
| Convention | `A1-sauzin-normalization-v0` |
| Lift | Spin lift built into condition (ii); `zeta = -I in SU(2)` realizes the loop class |

Default declaration, if no other scope is stated:

```text
Scope: A1-sauzin-normalization-v0; algebraic isolated A_1; dim_C V_A = 2; symplectic Q_A; spatial target Spin(3); no extension claims.
```

## Out-of-scope cases

Each row requires an extension theory declaration before any theorem, implementation, or manuscript section may invoke T2 outside the base case.

| # | Case | What breaks under T2 hypotheses | Extension required |
| --- | --- | --- | --- |
| 1 | `A_n`, `n >= 2` | `dim V_A > 2`; pairing signature changes; Milnor lattice rank exceeds 1 | Re-derive minimal `G`; candidate may be `SU(n+1)` or `Sp(floor((n+1)/2))` depending on pairing |
| 2 | `D_n`, `E_6`, `E_7`, `E_8` | Different Milnor lattice and monodromy structure | Case-by-case minimality theorem; not implied by T2 |
| 3 | Orthogonal `Q_A`, `epsilon = +1`, `dim V_A = 2` | Current non-abelian spinor branch no longer applies; minimal orthogonal candidates are abelian in rank 1 | Empty admissible class under current T1 unless the framework is reformulated |
| 4 | Higher-dimensional symplectic `Q_A`, `dim V_A = 2n > 2` | Minimal group is `Sp(n)`, strictly larger than `SU(2)` | Rank-`n` analogue of T2 |
| 5 | Non-algebraic isolated singularities | Local model is not `sqrt(t)`; Stokes structure differs | Full resurgent-transseries framework; T2's Catalan Stokes data does not transfer |
| 6 | Spatial target `SO(3)` instead of `Spin(3)` | Single-`G` framing breaks; `zeta=-I` is not a group element of `SO(3)` | Pair theorem `(G_spatial, G_active) = (SO(3), SU(2))`; see C-2 in the proof note |
| 7 | `Spin^c` structure | `U(1)` extension of Spin lift; central element promotes to a `U(1)` family | Open extension, C-4 in proof note |
| 8 | Real-form variations such as `SL(2,R)` | Noncompact group and different polarization condition | Open extension, C-5 in proof note |
| 9 | Non-isolated singularities | Active set `V_A` is not currently well-defined | Out of scope; not currently planned |

## Required declarations for downstream work

Any document, theorem, or implementation invoking T2 must declare:

1. **Convention.** Default: `A1-sauzin-normalization-v0`. Any other convention must be named and referenced.
2. **Active set.** Dimension and pairing signature: symplectic, orthogonal, or Hermitian.
3. **Spatial target.** `Spin(3)` under the current single-group framing, or `SO(3)` under an explicitly separate pair-framing theorem.
4. **Extension claims.** Which out-of-scope rows the work claims to handle, and which extension theory is invoked.
5. **Spin lift status.** Whether the Spin lift is built into condition (ii), as in the default A1 case, or supplied as external data.

## Branch-boundary notice

Condition (v) in `docs/gates/minimality.md` locks the framework to the spinor/symplectic branch:

```text
epsilon = -1.
```

Rows 3, 4, and 6 cross or stress the spinor/orientation boundary. Row 4 remains symplectic but exits rank 1. Any branch-crossing extension must explicitly declare which side of the `epsilon` boundary it occupies.

## Cross-references

- `docs/proofs/a1-gate-minimality.md`
- `docs/gates/minimality.md`
- `docs/appendices/appendix_a_chain_catalan_witness.md`
- `docs/context/proof-dynamics-mu2-bridge-artifact.md`
- `harness/catalan_a1_harness.py`
- `harness/reference_reports/catalan_a1_report.json`
