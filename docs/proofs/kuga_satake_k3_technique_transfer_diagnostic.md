# Kuga–Satake / K3 Technique-Transfer Diagnostic

Status: repo-grade workbench artifact. Method-adjacent negative result.  
Classification (Hodge Program lane): `hodge-method`. Explicitly not `core-hodge`, `hodge-arithmetic`, Hodge proof, or Hodge progress.  
Provenance: consolidated from Drive-side Mode-C session work (`HG_K3_001`) into repo-grade form. Records a negative technique-transfer result and its structural implication.

## 1. Setup

For K3 surfaces, the Kuga-Satake construction attaches an abelian variety to a polarized weight-2 Hodge structure. The technique is useful because it transports questions about K3 Hodge structures into an abelian-variety environment where more structure is available.

The Drive-side question was whether the Kuga-Satake construction, or a categorified analogue, transfers to the Heller-Godel apparatus: from K3 weight-2 Hodge structures to the `mu_2` finite-character Catalan A1 case.

## 2. Result: direct transfer fails

Direct Kuga-Satake transfer from K3 to Heller-Godel fails by categorical mismatch.

Reason:

```text
Kuga-Satake operates on weight-2 polarized Hodge structures.
Heller-Godel's mu_2 character is a finite-cyclic character valued in {1,-1}.
That character is a weight-0 finite local-system object, not a weight-2 Hodge structure.
```

The Kuga-Satake morphism has no domain in the Heller-Godel apparatus as currently constructed.

A categorified transfer would require:

1. a weight-bearing object on the Heller-Godel side;
2. a polarized Hodge structure on that object;
3. a Kuga-Satake-style morphism into an abelian-variety-like target.

All three are currently absent.

## 3. What this records

This artifact records a precise negative technique-transfer result:

1. it identifies the categorical mismatch: weight-0 finite character versus weight-2 polarized Hodge structure;
2. it names the missing intermediate object: proof-class moduli `M_phi` with Hodge-theoretic enrichment;
3. it excludes premature claims that K3 Tate or Kuga-Satake methods apply directly to the Heller-Godel apparatus.

## 4. What this is and is not

### What it is

1. A negative diagnostic preventing premature transfer of K3 Tate methods to Heller-Godel apparatus.
2. A structural specification of what `M_phi` would need to supply for such transfer to be formally available.
3. A workbench-grade record of why “we have a Hodge-shaped object, K3 has Hodge structure, so K3 methods apply” is false.

### What it is not

1. Not evidence that K3 methods can never transfer.
2. Not a Hodge progress claim.
3. Not a result about K3 surfaces.
4. Not a contribution to the Hodge conjecture for K3.
5. Not a Tate, Kuga-Satake, or abelian-variety theorem.

## 5. Active obstruction-registry references

| Entry | Reason |
| --- | --- |
| `OBS-HODGE-005` | finite monodromy to Tate data promotion risk |
| `OBS-HODGE-008` | Hodge-origin to Hodge-proof promotion risk |

## 6. Inputs supplied for HODGE-EVAL-001

| Bridge primitive | What this artifact supplies | What it does not supply |
| --- | --- | --- |
| Hodge target datum | Nothing; it explicitly blocks one false route | projective `X`; Hodge class `alpha` |
| Cycle realization datum | Nothing | algebraic cycles |
| Cycle equality obligation | Nothing | the equality |
| Deligne-to-Hodge bridge obligation | negative diagnostic: one route that does not work | working bridge |

Its contribution to `HODGE-EVAL-001` is to block a specific false-positive evaluation: the Heller-Godel `mu_2` apparatus must not be credited with K3-adjacent Hodge structure merely because both involve comparison techniques.

## 7. Implication for the program

The negative Kuga-Satake transfer is one of three Mode artifacts that independently identify the absence of proof-class moduli `M_phi` with Hodge-theoretic enrichment as the central structural gap.

This convergence is structurally informative but does not constitute construction of `M_phi`. The next move toward closing this gap is a proof-class moduli requirements scaffold, not this artifact.

## 8. Sources and citation level

| Reference | Use |
| --- | --- |
| Kuga-Satake, “Abelian varieties attached to polarized K3 surfaces,” Math. Ann. 169 (1967), 239–242 | original Kuga-Satake construction |
| Deligne, “La conjecture de Weil pour les surfaces K3,” Invent. Math. 15 (1972), 206–226 | K3 / Kuga-Satake Hodge context |
| Voisin, *Hodge Theory and Complex Algebraic Geometry II* | standard exposition |
| André, “On the Shafarevich and Tate conjectures for hyperkähler varieties,” Math. Ann. 305 (1996), 205–248 | categorified Kuga-Satake context |

Bibliographic level only. Theorem-grade locators are not yet added and are required before theorem-grade downstream use.

## 9. Cross-references

```text
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
docs/proofs/soule_voisin_ah_torsion_witness_artifact.md
docs/proofs/hodge_clay_target_gap_ledger.md
SocioProphet/hodge-program-proof: docs/obstruction-registry.md
```

## 10. Explicit nonclaim envelope

```text
No Hodge progress.
No K3 result.
No Tate result.
No abelian-variety result.
No transfer of K3 Hodge-conjecture status to Heller-Godel apparatus.
No claim that the mu_2 character is K3-adjacent in any constructive sense.
No proof-class moduli construction.
No promotion of finite-character data to a weight-bearing Hodge structure.
```
