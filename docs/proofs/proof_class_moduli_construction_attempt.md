# HG-MODULI-002 — Proof-Class Moduli Construction Attempt

Status: construction proposal with evaluation.  
Classification (Hodge Program lane): `hodge-method`.  
Claim level: candidate construction / partial support / nonclaim.  
Purpose: attempt the first three construction steps recommended by `docs/proofs/proof_class_moduli_scaffold_diagnostic.md`: proof-class objects, realization-equivalence relation, and D1 analytic realization assignment.

## 1. Scope and governing nonclaim

This artifact is a construction proposal, not a construction proof.

It proposes candidate definitions for:

1. proof-class objects;
2. realization-equivalence relation;
3. analytic realization assignment.

It then evaluates those candidates against `docs/proofs/proof_class_moduli_requirements_scaffold.md` and `docs/proofs/proof_class_moduli_scaffold_diagnostic.md`.

Nonclaim:

```text
This artifact does not construct a full M_phi.
This artifact does not prove M_phi exists.
This artifact does not prove the three candidate definitions are unique.
This artifact does not prove the three candidate definitions extend to satisfy the remaining HG-MODULI-001 requirements.
This artifact does not supply Hodge target data, algebraic cycles, a cycle equality, or a Deligne-to-Hodge bridge.
```

## 2. Input apparatus

This proposal uses the following repo-grade inputs:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
docs/appendices/appendix_a_chain_catalan_witness.md
docs/proofs/catalan_a1_realization_equivalence.md
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
docs/proofs/proof_class_moduli_requirements_scaffold.md
docs/proofs/proof_class_moduli_scaffold_diagnostic.md
```

The construction starts concretely because the diagnostic showed partial support on the proof/analytic/finite/regulator side and no support on the Hodge target/cycle/weight/polarization side.

## 3. Candidate proof-class object

### 3.1 Definition

A proof-class analytic object is a tuple

```text
P = (phi, T_phi, rho, alpha, N, a, V_rho^x, q, X_rho^x, u, chi_N)
```

where:

| Component | Meaning |
| --- | --- |
| `phi` | sentence, type, or proof-family label |
| `T_phi` | proof-class generating function where defined |
| `rho` | selected singularity of `T_phi` |
| `alpha = a/N` | selected local Puiseux exponent in lowest terms |
| `N` | denominator of `alpha` |
| `a` | numerator of `alpha` |
| `V_rho^x` | punctured local neighborhood of `rho` |
| `q` | branch-killing cover `X_rho^x -> V_rho^x` |
| `X_rho^x` | cover on which the singular unit is single-valued |
| `u` | Puiseux singular unit on `X_rho^x` |
| `chi_N` | finite monodromy character valued in `mu_N` |

The superscript `x` is a plain-text stand-in for the punctured notation used in D1. It avoids importing additional topology notation into this scaffold.

### 3.2 Intended interpretation

The object is not an individual proof. It is an analytic-decorated proof-family object: a proof-class generating-function germ plus the local analytic data needed for the D1 construction.

This choice is deliberate. The diagnostic suggested that individual proofs are too low-level for the current apparatus, while generating-function germs are the objects the existing Deligne-unit construction actually consumes.

### 3.3 Canonical examples

#### Chain null object

The chain object has integer exponent:

```text
alpha = -2
N = 1
chi_N = 1
```

It supplies the null finite-character example. It instantiates the candidate object definition but does not stress nontrivial monodromy.

#### Catalan A1 object

The Catalan object has:

```text
rho = 1/4
alpha = 1/2
N = 2
a = 1
chi_N = -1 in mu_2
```

It instantiates the nontrivial finite-character object and is the canonical worked example for this construction attempt.

#### Motzkin regulator-adjacent object

The Motzkin object is admitted only as a regulator-adjacent proof-class analytic object when the local decomposition data are fixed. It carries the Beilinson artifact caveat that the auxiliary unit value should be re-derived before theorem-grade use.

### 3.4 Evaluation against HG-MODULI-001 primitive 1

Verdict: partial construction.

Satisfied:

1. object vocabulary is specified;
2. Catalan and chain instantiate it;
3. the object carries the D1 analytic data needed downstream.

Not satisfied:

1. no general proof that every sentence or type has such an object;
2. no category of proof objects;
3. no morphisms;
4. no moduli quotient;
5. no proof that this object layer is unique or optimal.

Finding:

```text
The right first object layer for the current apparatus is analytic-decorated proof-family data, not raw proof syntax.
```

## 4. Candidate realization-equivalence relation

### 4.1 Definition

For proof-class analytic objects

```text
P = (phi, T_phi, rho, alpha, N, a, V_rho^x, q, X_rho^x, u, chi_N)
P' = (phi', T_phi', rho', alpha', N', a', V_rho'^x, q', X_rho'^x, u', chi_N')
```

we define three nested candidate equivalence relations.

### 4.2 Finite-output equivalence

`P ~_fin P'` if:

```text
N = N'
chi_N = chi_N'
```

This relation preserves finite monodromy output only.

Use:

```text
appropriate for finite-character comparison and Catalan A1 output independence;
not sufficient for Deligne-unit or regulator-symbol comparison.
```

### 4.3 Analytic-germ equivalence

`P ~_an P'` if:

```text
alpha = alpha'
N = N'
a = a'
```

and the local Puiseux singular data agree after an allowed local coordinate change preserving the selected punctured neighborhood and branch-killing cover convention.

Use:

```text
appropriate for D1 analytic realization comparison;
stronger than finite-output equivalence.
```

### 4.4 Regulator-seed equivalence

`P ~_reg P'` if `P ~_an P'` and the local regulator-symbol input data also agree at the level of:

```text
(a, |h(0)|)
```

where `h(0)` is the auxiliary-unit value used in the Beilinson regulator artifact.

Use:

```text
appropriate only for local regulator-symbol comparison;
not a global regulator or Hodge equivalence.
```

### 4.5 Equivalence hierarchy

The relations form an intended hierarchy:

```text
regulator-seed equivalence
  -> analytic-germ equivalence
  -> finite-output equivalence
```

The reverse implications are not asserted.

### 4.6 Catalan A1 compatibility

The Catalan A1 realization-equivalence result is classified here as a finite-output and analytic-germ equivalence result at `N = 2`. It does not establish regulator-seed equivalence for arbitrary objects and does not establish a general moduli quotient.

### 4.7 Evaluation against HG-MODULI-001 primitive 2

Verdict: partial construction.

Satisfied:

1. candidate equivalence relations are defined;
2. the relations distinguish finite, analytic, and regulator-relevant comparison layers;
3. the Catalan A1 fixture fits the finite and analytic layers.

Not satisfied:

1. no proof that these relations are final;
2. no proof that they produce a useful quotient;
3. no family-level stability theorem;
4. no compatibility theorem across products or p-primary projections;
5. no claim that finite-output equivalence is enough for `M_phi`.

Finding:

```text
A single equivalence relation is currently too coarse. M_phi likely needs a stratified or layered equivalence discipline.
```

## 5. Candidate D1 analytic realization assignment

### 5.1 Definition

Let `PCO` denote the tentative collection of proof-class analytic objects defined in Section 3.

Define the analytic realization assignment

```text
R_an(P) = (V_rho^x, q: X_rho^x -> V_rho^x, u, chi_N)
```

where the components are taken from the object tuple `P`.

This is an assignment on already-decorated objects. It is not yet a functor from raw proof syntax or from an independent moduli space.

### 5.2 Compatibility with D1

For a valid proof-class analytic object, `R_an` recovers the D1 local construction:

1. punctured local neighborhood;
2. branch-killing cover;
3. single-valued Puiseux singular unit;
4. finite monodromy character by deck/descent.

### 5.3 Behavior under equivalence layers

| Equivalence layer | What `R_an` preserves |
| --- | --- |
| `~_fin` | finite monodromy output only |
| `~_an` | local analytic realization data up to allowed coordinate convention |
| `~_reg` | local analytic realization plus regulator-seed input |

This records why the hierarchy matters. A finite-output quotient would forget analytic and regulator-relevant data. A regulator-seed quotient may overfit to local regulator data.

### 5.4 Evaluation against HG-MODULI-001 primitive 4

Verdict: partial construction.

Satisfied:

1. an analytic realization assignment is defined on decorated objects;
2. it recovers the D1 analytic local construction;
3. it is compatible with the proposed equivalence hierarchy at the descriptive level.

Not satisfied:

1. no independent domain category;
2. no morphisms;
3. no functoriality proof;
4. no global family;
5. no parameter object;
6. no universal cover or universal singular-unit family.

Finding:

```text
The current apparatus supports an analytic realization assignment only after analytic decoration is included in the object definition.
```

This is useful but narrow. It suggests the first viable `M_phi` candidate may be a moduli object of decorated analytic proof-family data rather than raw proof objects.

## 6. Joint consistency check for the three starting points

The three candidate pieces are mutually consistent at the definition level:

1. proof-class analytic objects carry the data consumed by `R_an`;
2. the equivalence hierarchy explains which parts of the data are preserved;
3. `R_an` can be evaluated on the object tuple without requiring Hodge target data or algebraic cycles.

No contradiction is found among the three candidate definitions.

However, this is a local consistency check only. It does not prove extension to the remaining `HG-MODULI-001` requirements.

## 7. What remains unconstructed

This construction attempt does not address the following `HG-MODULI-001` requirements:

| Requirement | Status after HG-MODULI-002 |
| --- | --- |
| candidate parameter space or stack type | still open |
| finite monodromy / `mu_N` local-system structure | partially addressed only for individual objects |
| Deligne-unit family | not constructed |
| local regulator-symbol package | not globalized |
| candidate Hodge target extraction | not constructed |
| cycle realization candidate | not constructed |
| cycle equality target | not constructed |
| weight-bearing Hodge structure | not constructed |
| polarization structure | not constructed |
| failure-mode criteria | not formalized beyond reporting discipline |

## 8. Substantive finding

The first construction attempt identifies a narrower viable starting object:

```text
proof-class analytic object = proof-family generating-function germ + selected singularity + Puiseux/cover/unit/finite-character data.
```

This object is narrower than a raw proof moduli object but is directly supported by the D1 apparatus.

The key tradeoff:

```text
raw proof objects are conceptually upstream but currently unsupported;
analytic-decorated proof-family objects are downstream but constructible from current apparatus.
```

## 9. Implication for HG-MODULI-003

The next construction step should not jump to Hodge targets. It should attempt one of:

1. define a parameter object or weaker substitute for proof-class analytic objects;
2. define morphisms between proof-class analytic objects;
3. prove basic properties of the equivalence hierarchy;
4. test whether the Catalan and Motzkin objects coexist inside one finite or analytic parameter object.

Recommended next target:

```text
HG-MODULI-003: parameter-object feasibility for proof-class analytic objects.
```

The first question should be:

```text
Can the decorated proof-class analytic objects form a finite or analytic parameter space without pretending to be projective?
```

## 10. Relationship to Hodge Program evaluations

This construction attempt does not change `HODGE-EVAL-001`.

It confirms the evaluation's conclusion that current Heller-Godel work is method-side only. The attempt creates a more precise method-side object but does not produce any of the Hodge bridge primitives.

## 11. Active obstruction-registry references

| Entry | Relevance |
| --- | --- |
| `OBS-HODGE-002` | parameter object must not be treated as projective without proof |
| `OBS-HODGE-004` | Deligne-unit data are not algebraicity |
| `OBS-HODGE-005` | finite monodromy output is not Tate data |
| `OBS-HODGE-006` | equivalence hierarchy is not motivic comparison |
| `OBS-HODGE-007` | regulator-seed equivalence is not a regulator conjecture |
| `OBS-HODGE-008` | construction proposal is not Hodge progress |

## 12. Explicit nonclaim envelope

```text
No full M_phi construction.
No proof M_phi exists.
No construction proof.
No proof the candidate definitions are unique.
No proof the candidate definitions are final.
No proof the candidate definitions extend to all HG-MODULI-001 requirements.
No proof the candidate definitions produce a parameter space.
No proof of functoriality from raw proof syntax.
No Hodge target datum.
No algebraic cycles.
No cycle equality.
No weight-bearing Hodge structure.
No polarization.
No Deligne-to-Hodge bridge theorem.
No Beilinson conjecture evidence.
No Tate evidence.
No motivic framework.
No Hodge progress.
No Clay-facing claim.
```

## 13. Final verdict

```text
HG-MODULI-002 partially constructs the proof/analytic starting wedge.

It defines candidate proof-class analytic objects, a layered realization-equivalence discipline, and a D1 analytic realization assignment on decorated objects.

The construction is narrow but nonempty: chain and Catalan instantiate it, and Motzkin is admitted subject to its local regulator caveat.

The next obstruction is not Hodge target extraction. It is parameter-object feasibility for the decorated analytic object layer.
```
