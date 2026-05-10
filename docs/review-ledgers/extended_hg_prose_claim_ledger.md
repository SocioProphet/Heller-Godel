# Extended Heller–Gödel Prose Claim Ledger

Status: review ledger for extended prose, analogies, and future-horizon material. This ledger exists to preserve exploratory work while preventing claim inflation.

## 1. Ledger rule

Every major prose claim is assigned a status:

```text
proved
computed
definition
conjecture
future_horizon
false_as_stated
superseded
context_only
needs_formalization
delete
```

This file should be updated whenever new prose introduces a claim that might be mistaken for theorem-core.

## 2. Core proof-character claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| A fixed statistic on canonical normal forms defines a proof-family GF. | definition / theorem-core target | CIPC | Requires restricted grammar/canonicalization. |
| The construction is statistic-relative. | computed / established by falsifier | CIPC + HG-STAT | Naive statistic-invariance failed. |
| Admissible constructor-linear statistics preserve analytic type on chain/T/Catalan/Motzkin families. | computed | HG-STAT-001/002/003 | Theorem-level only for those families. |
| General admissible-statistic robustness for regular/algebraic/D-finite grammars. | conjecture | future theorem | Needs grammar-class proof. |
| Dominant radius is preserved under rank-uniformity. | false_as_stated | HG-STAT-002 erratum | Catalan refutes this. Radius covaries. |
| Exponent preservation may follow from simple-branch stability. | conjecture | HG-STAT-003 | Motzkin weakens rank-uniformity as necessary condition. |

## 3. Carry / cocycle claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| `zeta_p(alpha,beta)` computes finite carry defect. | computed/proved | theorem core | Direct floor arithmetic. |
| `zeta_p` is symmetric. | computed/proved | theorem core | Immediate from addition symmetry. |
| `zeta_p` is a 2-cocycle. | computed/proved | theorem core | Associativity of addition. |
| `zeta_p` is a coboundary under ordinary cochain freedom. | computed/proved | theorem core / correction | `zeta_p = delta f_p`. |
| The displayed `zeta_p` proves a nontrivial cohomological obstruction. | false_as_stated | ledger only | It does not under ordinary cochain freedom. |
| The displayed `zeta_p` produces a nonabelian Heisenberg extension. | false_as_stated | ledger only | Symmetric cocycle gives abelian multiplication in the shown extension. |
| Nonabelian structure may arise from extra skew, braided, or categorical structure. | future_horizon | future work | Needs new construction. |

## 4. Regulator / topology claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| `(2 pi i)^(-1) d log T_phi` records local exponent/residue data. | definition / analytic target | CIPC future | Must treat algebraic functions on normalization/cover. |
| The regulator immediately gives a Chern class for sentence bundles. | needs_formalization | future horizon | Bundle, connection, curvature, and base map missing. |
| Base-relative visibility matters. | context/conjectural | future horizon | Good principle; needs moduli/bundle object for theorem-core. |
| Klein bottle has useful `Z/2` torsion visibility. | context | future horizon | True topology, not yet tied to proof-family bundle. |

## 5. Wythoff / Schwarz claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| Wythoff/Schwarz gives precedent for finite symbolic seed -> regime realization. | context_only | future horizon | Useful analogy. |
| Schwarz triangle inequality determines spherical/Euclidean/hyperbolic regimes. | context/math fact | future horizon | Independent geometry fact. |
| This proves HG grammar regimes. | false_as_stated if asserted | ledger | No direct proof transfer. |
| Wythoff exception handling suggests boundary-case discipline. | context_only | governance analogy | Methodological value. |

## 6. Projection / preimage claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| Poincare disk chart has projection artifacts. | context/math fact | future horizon | Good model of chart/preimage distinction. |
| `zeta_p` projected obstruction dissolves as coboundary in ordinary cohomology. | computed/corrective | theorem-core correction | This is a concrete HG case of projection/preimage discipline. |
| Heller–Gödel is holographic / AdS-CFT-like. | false_as_stated if literal | ledger | Only analogy currently. |
| A mature HG theory would need a precise bulk-boundary dictionary to use holographic language. | context_only | future horizon | Good caution. |

## 7. Recognition / cognition / dynamics claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| Pure gradient recognition dynamics support periodic orbits. | false_as_stated generally | ledger | Gradient flows require caveats; periodic orbits need non-gradient structure. |
| Non-gradient recognition dynamics might support cycles or quasi-periodic returns. | future_horizon | future work | Needs dynamical system. |
| Continued fractions are natural sampling for irrational rotations. | context/math fact | future horizon | Needs HG parameter/observable. |
| Continued fractions are proven fingerprints of recognition-time structure. | false_as_stated if asserted | ledger | Not established. |
| Atomic/chemical shell analogy directly explains proof dynamics. | false_as_stated if literal | ledger | Structural analogy only. |

## 8. Gödel / provability prose claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| The program’s proof-status discipline is itself Gödelian in spirit. | context_only / essay | essays | Methodological framing. |
| The program proves new Gödel incompleteness theorems. | false_as_stated unless separately proven | ledger | Not claimed. |
| The irony of provability is operational: claims about proof require proof ledgers. | context_only / governance | essay + governance | Good program narrative. |

## 9. BSD context claims

| Claim | Status | Route | Notes |
|---|---|---|---|
| BSD repo work supplies evidence-gate discipline. | context_only | separate BSD repo + governance | Useful precedent. |
| BSD computations prove HG theorem claims. | false_as_stated | ledger | No direct theorem support. |
| BSD artifacts should remain sourced in bsd-proof-program. | definition / governance | BSD repo | HG may reference only as context. |

## 10. Required action when a claim changes status

When a claim changes status:

1. update this ledger;
2. add or update tests if it becomes computed;
3. add an erratum if an existing note is superseded or false as stated;
4. add a future-horizon route if it is preserved but unconstructed;
5. never close a theorem-core issue merely because prose was preserved.
