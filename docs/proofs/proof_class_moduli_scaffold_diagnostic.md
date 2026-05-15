# Proof-Class Moduli Scaffold Diagnostic

Status: scaffold-diagnostic evaluation.  
Classification (Hodge Program lane): `hodge-method`.  
Claim level: evaluation / construction-prep / nonclaim.  
Purpose: evaluate the current Heller-Godel apparatus against the `M_phi` requirements specified in `docs/proofs/proof_class_moduli_requirements_scaffold.md`, and use the result to sequence `HG-MODULI-002`.

## 1. Provenance and scope

This diagnostic follows three repo-grade artifacts:

1. `docs/proofs/proof_class_moduli_bottleneck_consolidation.md`, which identifies proof-class moduli `M_phi` as the central structural bottleneck.
2. `SocioProphet/hodge-program-proof: docs/evaluations/hodge_eval_001_heller_godel_apparatus.md`, which evaluates the current Heller-Godel apparatus against the Hodge bridge primitives and returns a negative bridge evaluation.
3. `docs/proofs/proof_class_moduli_requirements_scaffold.md`, which specifies requirements that a future `M_phi` would need to support.

This diagnostic evaluates support. It does not construct `M_phi`.

## 2. Verdict scale

Each requirement is classified as one of:

```text
full support
partial support
no support
contradicted
overconstrained
```

Definitions:

| Verdict | Meaning |
| --- | --- |
| full support | current apparatus already supplies the requirement in a usable form |
| partial support | current apparatus supplies examples, vocabulary, or local data, but not the requirement itself |
| no support | current apparatus does not supply relevant structure |
| contradicted | current apparatus supplies evidence that the requirement cannot hold as stated |
| overconstrained | the requirement appears too strong or internally incompatible with adjacent requirements |

No requirement receives `full support` in this diagnostic.

## 3. Summary matrix

| Requirement | Current apparatus components | Verdict | Construction-sequencing implication |
| --- | --- | --- | --- |
| Proof-class object | D1 manuscript; Catalan A1 fixture | partial support | start here; define the object vocabulary precisely |
| Realization-equivalence relation | Catalan A1 realization equivalence; A1 output invariance | partial support | extend from `mu_2` fixture to general equivalence candidates |
| Candidate parameter space or stack type | none beyond requirements vocabulary | no support | postpone until object/equivalence are fixed |
| Analytic realization functor | D1 analytic realization; Puiseux data; branch-killing cover | partial support | define a functorial package from existing local constructions |
| Finite monodromy / `mu_N` local-system structure | D1 finite characters; Catalan `mu_2`; p = 3 vocabulary | partial support | generalize from fixture-level to family-level data |
| Deligne-unit family | D1 Deligne unit; finite descent | partial support | attempt a family packaging after analytic functor is specified |
| Local regulator-symbol package | Beilinson regulator Catalan/Motzkin artifact | partial support | formalize globalization criteria; do not globalize by assertion |
| Candidate Hodge target extraction | Hodge gap ledger; HODGE-EVAL-001 negative result | no support | do not attempt until parameter/family structures exist |
| Cycle realization candidate | none | no support | depends on Hodge target extraction; postpone |
| Cycle equality target | none | no support | depends on cycles and target; postpone |
| Weight-bearing Hodge structure | Kuga-Satake/K3 diagnostic identifies absence | no support | treat as major missing object; do not infer from finite characters |
| Polarization structure | none | no support | depends on weight-bearing Hodge structure |
| Failure modes | HG-MODULI-001 failure-mode table | partial support | use immediately as construction-attempt reporting discipline |

Aggregate verdict:

```text
partial support: 7 requirements
no support: 6 requirements
full support: 0 requirements
contradicted: 0 requirements
overconstrained: 0 requirements
```

## 4. Requirement-by-requirement diagnostic

### 4.1 Proof-class object

Verdict: partial support.

Relevant apparatus:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
docs/proofs/catalan_a1_realization_equivalence.md
```

The D1 manuscript defines proof-class generating functions and the Catalan A1 fixture supplies a closed example. This gives concrete proof-class-adjacent data, but not a final definition of the objects of `M_phi`.

Missing:

1. whether objects are proofs, proof equivalence classes, generating-function germs, analytic-decorated packages, or another structure;
2. whether `M_phi` is indexed by a single sentence `phi`, a family of sentences, or a category of proof data;
3. stability under type-product and realization operations.

Construction implication:

```text
HG-MODULI-002 should begin by defining the object layer.
```

### 4.2 Realization-equivalence relation

Verdict: partial support.

Relevant apparatus:

```text
docs/proofs/catalan_a1_realization_equivalence.md
docs/proofs/proof_class_moduli_bottleneck_consolidation.md
```

The Catalan A1 realization-equivalence artifact gives a controlled `mu_2` output-equivalence surface. Theorem A.8 records output-level realization independence for the Catalan A1 fixture. This is a genuine seed, but it is fixture-specific.

Missing:

1. general equivalence relation across proof-class objects;
2. proof that equivalence is stable under analytic realization;
3. proof that equivalence respects Deligne-unit and regulator-symbol data;
4. decision whether equivalence should preserve full analytic data or only finite output.

Construction implication:

```text
Extend the Catalan A1 equivalence discipline into a candidate general relation, but do not assume output-equivalence is enough.
```

### 4.3 Candidate parameter space or stack type

Verdict: no support.

Relevant apparatus:

```text
docs/proofs/proof_class_moduli_requirements_scaffold.md
```

The scaffold lists possible ambient types, but no candidate parameter object has been proposed.

Missing:

1. finite versus analytic versus algebraic target;
2. moduli quotient construction;
3. topology, analytic structure, or algebraic structure;
4. relationship to any projective target variety.

Construction implication:

```text
Do not start by choosing an ambient parameter space. It depends on object and equivalence definitions.
```

### 4.4 Analytic realization functor

Verdict: partial support.

Relevant apparatus:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
```

D1 already constructs local analytic realization data: proof-class generating function, singularity, Puiseux exponent, branch-killing cover, singular unit, and finite monodromy character. This is the strongest positive support for an `M_phi` primitive.

Missing:

1. functorial domain;
2. morphisms or maps between proof-class objects;
3. proof of functoriality under realization-equivalence;
4. global compatibility across families.

Construction implication:

```text
After defining objects and equivalence, package the existing D1 construction as an analytic realization assignment.
```

### 4.5 Finite monodromy / mu_N local-system structure

Verdict: partial support.

Relevant apparatus:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
docs/appendices/appendix_a_chain_catalan_witness.md
docs/proofs/p3_vocabulary_scaffold.md
```

The `mu_2` Catalan fixture is closed and the D1 manuscript uses `mu_N` / finite monodromy language. The p = 3 runway supplies vocabulary but not a closed fixture.

Missing:

1. family-level local system over a parameter object;
2. compatibility across denominators `N`;
3. `mu_3` or odd-prime closed source;
4. proof that finite monodromy packages vary coherently.

Construction implication:

```text
Use the closed mu_2 case as seed; do not generalize to mu_N family structure without a parameter object.
```

### 4.6 Deligne-unit family

Verdict: partial support.

Relevant apparatus:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
docs/proofs/proof_class_moduli_requirements_scaffold.md
```

The D1 manuscript supplies individual Deligne units and strict separation between Deligne units, finite monodromy, Bockstein carry, and regulator-symbol data. It does not supply a family.

Missing:

1. universal space or family of covers;
2. base parameter object;
3. functorial assignment of Deligne classes over that base;
4. comparison across different singularities and denominators.

Construction implication:

```text
A Deligne-unit family is a second-stage task after analytic realization functor and parameter candidate are fixed.
```

### 4.7 Local regulator-symbol package

Verdict: partial support.

Relevant apparatus:

```text
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
```

The Beilinson artifact supplies local regulator-symbol outputs:

```text
Catalan: -2*pi*log(2)
Motzkin: -2*pi*log(3/2)
```

It explicitly carries normalization and Motzkin auxiliary-unit caveats. It is local, not global.

Missing:

1. theorem-grade normalization verification;
2. Motzkin auxiliary-unit re-derivation;
3. global domain of regulator computation;
4. motivic cohomology class, if any;
5. special-value or Beilinson-conjecture relation, if any.

Construction implication:

```text
Treat regulator-symbol package as a local seed. HG-MODULI-002 should not globalize it until normalization and domain are fixed.
```

### 4.8 Candidate Hodge target extraction

Verdict: no support.

Relevant apparatus:

```text
docs/proofs/hodge_clay_target_gap_ledger.md
SocioProphet/hodge-program-proof: docs/evaluations/hodge_eval_001_heller_godel_apparatus.md
```

The gap ledger and HODGE-EVAL-001 identify the missing target. They do not supply one.

Missing:

1. nonsingular complex projective variety `X`;
2. codimension `k`;
3. rational Hodge class `alpha`;
4. proof of Hodge type `(k,k)`;
5. extraction map from proof-class data to `(X,k,alpha)`.

Construction implication:

```text
Do not attempt Hodge target extraction first. It depends on prior construction of object, equivalence, parameter, analytic realization, and possibly family data.
```

### 4.9 Cycle realization candidate

Verdict: no support.

Relevant apparatus:

```text
docs/proofs/hodge_clay_target_gap_ledger.md
```

No algebraic cycles are constructed anywhere in the current Heller-Godel apparatus.

Missing:

1. algebraic cycles `Z_i`;
2. proof of codimension;
3. rational coefficients;
4. cycle class map;
5. relation to any target class.

Construction implication:

```text
Cycle realization cannot begin until a Hodge target datum exists.
```

### 4.10 Cycle equality target

Verdict: no support.

Relevant apparatus:

```text
docs/proofs/hodge_clay_target_gap_ledger.md
```

No equality of the form

```text
alpha = sum_i q_i cl(Z_i)
```

is stated or typeable because neither side exists.

Missing:

1. cohomology group;
2. target class;
3. cycle classes;
4. equality theorem.

Construction implication:

```text
This is a late-stage target, not an early construction primitive.
```

### 4.11 Weight-bearing Hodge structure

Verdict: no support.

Relevant apparatus:

```text
docs/proofs/kuga_satake_k3_technique_transfer_diagnostic.md
```

The Kuga-Satake diagnostic is explicitly negative: the current apparatus has weight-0 finite-character data, not a weight-2 polarized Hodge structure.

Missing:

1. rational vector space or cohomology group;
2. Hodge filtration or decomposition;
3. weight;
4. polarization;
5. compatibility with proof-class data.

Construction implication:

```text
This is a major missing object. Do not infer weight structure from finite characters.
```

### 4.12 Polarization structure

Verdict: no support.

Relevant apparatus:

```text
docs/proofs/kuga_satake_k3_technique_transfer_diagnostic.md
```

No polarization candidate exists. The K3 diagnostic identifies polarization as part of the missing weight-bearing structure.

Missing:

1. bilinear or Hermitian form;
2. positivity or signature condition;
3. compatibility with a Hodge structure;
4. relation to proof-class data.

Construction implication:

```text
Polarization depends on first producing a weight-bearing Hodge structure or a substitute object.
```

### 4.13 Failure modes

Verdict: partial support.

Relevant apparatus:

```text
docs/proofs/proof_class_moduli_requirements_scaffold.md
```

The scaffold already names failure modes: no stable realization equivalence, analytic-only object, finite-only object, regulator-locality failure, no Hodge target, no cycle source, incompatibility of requirements, and overfitting to Catalan A1.

Missing:

1. criteria for detecting each failure mode in a construction attempt;
2. required evidence for declaring a failure mode closed;
3. examples of failure-mode reporting.

Construction implication:

```text
Use the failure-mode table immediately as HG-MODULI-002 reporting discipline.
```

## 5. Support-level sequencing

A cheapest-first construction sequence would begin with partially supported requirements:

1. proof-class object;
2. realization-equivalence relation;
3. analytic realization functor;
4. finite monodromy / `mu_N` local-system structure;
5. Deligne-unit family;
6. local regulator-symbol package;
7. failure-mode reporting discipline.

Then it would address unsupported requirements:

1. candidate parameter space;
2. candidate Hodge target extraction;
3. cycle realization candidate;
4. cycle equality target;
5. weight-bearing Hodge structure;
6. polarization structure.

Benefit:

```text
This route maximizes reuse of current apparatus.
```

Risk:

```text
It may overfit to existing finite-character and local analytic data before the parameter-space question is settled.
```

## 6. Dependency-order sequencing

A structurally cleaner construction sequence is:

1. proof-class object;
2. realization-equivalence relation;
3. analytic realization assignment;
4. candidate parameter space or weaker substitute;
5. finite monodromy package over the candidate;
6. Deligne-unit family over the candidate;
7. local regulator-symbol package and globalization criterion;
8. decide whether candidate Hodge target extraction is possible;
9. if possible, define weight-bearing Hodge structure and polarization;
10. if possible, seek cycle realization;
11. if possible, state cycle equality target.

Benefit:

```text
This route respects mathematical dependency order.
```

Risk:

```text
It reaches the unsupported parameter-space requirement earlier and may stall sooner.
```

## 7. Recommended HG-MODULI-002 starting point

Recommendation:

```text
HG-MODULI-002 should start with a three-part construction attempt:

A. define proof-class objects;
B. define a candidate realization-equivalence relation;
C. attempt to package the D1 analytic realization as an assignment on those objects.
```

This is the best starting point because these three requirements are both partially supported and structurally prior to the others.

Expected valid outcomes:

1. a partial construction of object/equivalence/analytic assignment;
2. discovery that equivalence cannot be made stable under analytic realization;
3. discovery that only generating-function germs, not proofs, form the right object layer;
4. refinement of `HG-MODULI-001` if the current primitives are overconstrained.

## 8. No contradicted or overconstrained requirements found

This diagnostic found no current requirement that is contradicted by the existing apparatus.

It also found no requirement that is demonstrably overconstrained from current evidence.

This does not prove the requirements are jointly satisfiable. It only means the current apparatus does not yet expose a direct contradiction.

## 9. Relationship to HODGE-EVAL-001

`HODGE-EVAL-001` evaluated the current apparatus against the Hodge bridge primitives and returned a negative bridge evaluation.

This diagnostic evaluates the current apparatus against the Heller-Godel-side `M_phi` requirements and returns a mixed result:

```text
partial support on the proof/analytic/finite/regulator side;
no support on the Hodge target/cycle/weight/polarization side.
```

Together, the two evaluations localize the next research phase:

```text
construct or refute the proof/analytic side of M_phi first;
do not attempt Hodge target or cycle extraction yet.
```

## 10. Active obstruction-registry references

| Entry | Relevance |
| --- | --- |
| `OBS-HODGE-002` | unsupported projective target and candidate parameter-space issues |
| `OBS-HODGE-004` | Deligne-unit and regulator-symbol partial support must not be promoted to algebraicity |
| `OBS-HODGE-005` | finite monodromy partial support must not be promoted to Tate data |
| `OBS-HODGE-006` | comparison and equivalence data must not be promoted to motivic structure |
| `OBS-HODGE-007` | local regulator-symbol package is not a regulator conjecture |
| `OBS-HODGE-008` | partial support is not Hodge progress |

## 11. Explicit nonclaim envelope

```text
No M_phi construction.
No proof M_phi exists.
No proof any requirement is fully supported.
No proof any partial-support verdict can be upgraded to full support.
No proof no-support verdicts are impossible to close.
No proof the requirements are jointly satisfiable.
No proof the requirements are exhaustive.
No Hodge target datum.
No algebraic cycles.
No cycle equality.
No weight-bearing Hodge structure.
No polarization.
No Deligne-to-Hodge bridge theorem.
No Hodge progress.
No Clay-facing claim.
No claim that the recommended HG-MODULI-002 sequence is the only valid sequence.
```

## 12. Final verdict

```text
The current Heller-Godel apparatus partially supports the proof/analytic/finite/regulator side of the M_phi requirements.

It does not support the Hodge target/cycle/weight/polarization side.

No requirements are currently contradicted or shown overconstrained.

HG-MODULI-002 should begin with proof-class objects, realization-equivalence, and analytic realization assignment.
```
