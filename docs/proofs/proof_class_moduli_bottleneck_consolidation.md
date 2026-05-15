# Proof-Class Moduli Bottleneck — Mode Artifact Consolidation

Status: repo-grade workbench consolidation artifact.  
Classification (Hodge Program lane): `hodge-method`. Explicitly not `core-hodge`, `hodge-arithmetic`, Hodge proof, or Hodge progress.  
Provenance: consolidates the Drive-side Mode-A, Mode-B, and Mode-C session findings after their repo-grade migration into Heller-Godel.

## 1. The convergent finding

Three independent Mode artifacts produced one structural conclusion:

1. Mode-A, Soulé-Voisin / Atiyah-Hirzebruch torsion: the `mu_2` character supplies torsion-witness-shaped data but cannot become an Atiyah-Hirzebruch-style torsion witness without a projective variety `X` and an integral Hodge class on it.
2. Mode-B, Beilinson regulator: local regulator-symbol output exists for Catalan and Motzkin, but it is a punctured-curve computation, not a global Hodge-theoretic statement on a projective variety.
3. Mode-C, Kuga-Satake / K3 technique transfer: direct K3-style transfer fails by categorical mismatch; a categorified transfer would require a weight-bearing object on the Heller-Godel side.

Single bottleneck:

```text
the central missing structure is a proof-class moduli object M_phi
with enough algebraic-geometric / Hodge-theoretic enrichment to produce
candidate Hodge target data.
```

The three Modes converge on this finding by independent paths:

| Mode | Missing structure |
| --- | --- |
| A: Atiyah-Hirzebruch / Soulé-Voisin | projective `X` realizing the flat `mu_2` local-system data |
| B: Beilinson regulator | global `X` on which local regulator output extends to global cycle data |
| C: Kuga-Satake / K3 | weight-bearing Hodge structure on which K3-style transfer can operate |

All three are aspects of the same missing object: a proof-class moduli space supporting realization-equivalence classes of proof data with enough algebraic-geometric structure to produce a candidate Hodge target.

## 2. What this consolidation establishes

This artifact moves the Mode-convergence finding from Drive-side session conclusion to repo-grade Heller-Godel workbench statement.

It establishes:

1. the statement “`M_phi` is the central bottleneck” is now repo-grade rather than session-grade;
2. the three Mode artifacts are explicitly linked;
3. their structural agreement is recorded without promoting any Mode artifact to Hodge evidence;
4. downstream work can cite this consolidation rather than Drive-side notes.

## 3. What this is and is not

### What it is

1. A repo-grade statement of structural convergence across three Mode artifacts.
2. The input for a future proof-class moduli requirements scaffold.
3. A workbench note identifying where the program's substantive work needs to land next.

### What it is not

1. Not a construction of `M_phi`.
2. Not a proof that `M_phi` exists.
3. Not a proof that `M_phi` can be smooth, Kähler, projective, algebraic, or stack-like.
4. Not a Hodge progress claim.
5. Not a substitute for the individual Mode artifacts.
6. Not evidence for the Hodge conjecture, Beilinson conjectures, Tate conjecture, or K3 Hodge theory.

## 4. Active obstruction-registry references

| Entry | Reason |
| --- | --- |
| `OBS-HODGE-002` | compact-Kähler / non-projective base risk; `M_phi` would need projective structure, not merely analytic or Kähler shape |
| `OBS-HODGE-004` | Deligne cohomology to algebraicity promotion risk; Mode-B cannot be promoted to algebraicity |
| `OBS-HODGE-005` | finite monodromy to Tate data promotion risk; Mode-C blocks finite-character-to-K3/Tate promotion |
| `OBS-HODGE-007` | regulator symbol to regulator conjecture promotion risk |
| `OBS-HODGE-008` | Hodge-origin to Hodge-proof promotion risk |

## 5. Implications for the bridge requirements scaffold

For `HODGE-EVAL-001`, this consolidation supplies a meta-input: none of the current Heller-Godel workbench artifacts is expected to satisfy the four Hodge bridge primitives in isolation, but collectively they localize what `M_phi` would need to supply.

The Hodge Program bridge primitives are:

```text
Hodge target datum
Cycle realization datum
Cycle equality obligation
Deligne-to-Hodge bridge obligation
```

The Mode convergence says that any future `M_phi` scaffold must explain how proof-class data could even become candidate inputs to those primitives.

## 6. The M_phi specification implied by Mode convergence

Drawing from the three Modes, `M_phi` would need to support, at minimum:

| Required structure | Source Mode | Bridge primitive it could enable |
| --- | --- | --- |
| proof-class realization-equivalence classes | all three | foundation for all bridge primitives |
| smooth complex projective base `X` | A, B | Hodge target datum |
| weight-bearing Hodge structure | C | Hodge target datum |
| polarization on the Hodge structure | C | cycle-realization prerequisites |
| realization functor from proof-class data to `X` | A, B | Deligne-to-Hodge bridge obligation |
| cycle-class extraction from regulator data | B | cycle realization datum |
| compatibility with finite-character monodromy | A, all | bridge between `mu_N` data and global structure |

This list is necessary, not sufficient. Even an `M_phi` supplying all of these would still need to produce `(X,k,alpha,Z_i)` and a cycle equality in a specific case before constituting Hodge progress.

## 7. Individual Mode sources

### Mode-A: Soulé-Voisin / Atiyah-Hirzebruch torsion witness

Source:

```text
docs/proofs/soule_voisin_ah_torsion_witness_artifact.md
```

Contribution:

```text
mu_2 torsion-witness-shaped data;
missing projective X and integral Hodge class.
```

### Mode-B: Beilinson regulator output

Source:

```text
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
```

Contribution:

```text
local regulator-symbol output;
Catalan: -2*pi*log(2);
Motzkin: -2*pi*log(3/2);
missing global Hodge target and cycle data.
```

### Mode-C: Kuga-Satake / K3 technique-transfer diagnostic

Source:

```text
docs/proofs/kuga_satake_k3_technique_transfer_diagnostic.md
```

Contribution:

```text
direct transfer fails;
missing weight-bearing Hodge structure and polarized object.
```

## 8. Cross-references

```text
docs/proofs/soule_voisin_ah_torsion_witness_artifact.md
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
docs/proofs/kuga_satake_k3_technique_transfer_diagnostic.md
docs/proofs/catalan_a1_realization_equivalence.md
docs/proofs/hodge_clay_target_gap_ledger.md
SocioProphet/hodge-program-proof: docs/scaffolds/hodge_bridge_requirements_scaffold.md
SocioProphet/hodge-program-proof: docs/obstruction-registry.md
```

## 9. Explicit nonclaim envelope

```text
No M_phi construction.
No proof M_phi exists.
No proof M_phi produces a smooth complex projective X.
No proof M_phi supports a polarized Hodge structure.
No Hodge class.
No algebraic cycles.
No cycle equality.
No Hodge progress.
No Clay-facing claim.
No promotion of bottleneck identification to bottleneck resolution.
```
