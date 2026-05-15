# HG-MODULI-004 — Stratified Registry Object for Proof-Class Analytic Objects

Status: stratified registry construction.  
Classification (Hodge Program lane): `hodge-method`.  
Claim level: weak workbench construction / nonclaim.  
Purpose: construct the weak stratified registry object recommended by `HG-MODULI-003` for proof-class analytic objects.

## 1. Scope and governing nonclaim

This artifact constructs a stratified registry object. It does not construct a parameter space.

The object constructed here is a discrete workbench registry with stratum labels, promotion criteria, and failure annotations. It has no topology, no analytic structure, no algebraic structure, no projective structure, no universal family, and no descent datum.

Nonclaim:

```text
No moduli space is constructed.
No parameter space is constructed.
No proof-class moduli M_phi is constructed.
No analytic family is constructed.
No algebraic family is constructed.
No projective variety is constructed.
No universal family is constructed.
No descent datum is supplied.
No Hodge target datum is supplied.
No algebraic cycles are supplied.
No cycle equality is supplied.
No Deligne-to-Hodge bridge theorem is supplied.
```

## 2. Input artifacts

This registry construction follows:

```text
docs/proofs/proof_class_moduli_requirements_scaffold.md
docs/proofs/proof_class_moduli_scaffold_diagnostic.md
docs/proofs/proof_class_moduli_construction_attempt.md
docs/proofs/proof_class_moduli_parameter_feasibility.md
```

The feasibility analysis concluded that only weak discrete or stratified-discrete registry organization is currently supported. This artifact constructs exactly that weak object and no stronger one.

## 3. Registry object definition

The proof-class analytic stratified registry is a finite workbench table whose rows are proof-class analytic objects and whose columns record stratum-relevant invariants.

A registry entry has the following schema:

| Field | Meaning |
| --- | --- |
| `registry_id` | stable local identifier for the row |
| `object_label` | human-readable proof-family label |
| `source_artifacts` | repo-grade artifacts supporting the row |
| `object_status` | null fixture / closed fixture / caveated local seed / candidate |
| `exponent_type` | integer / rational-noninteger / unknown / other |
| `N` | finite monodromy denominator, if known |
| `finite_character` | finite output value or status |
| `fixture_status` | closed / partial / caveated / absent |
| `regulator_status` | absent / local seed / caveated local seed / closed local computation |
| `equivalence_layers_supported` | finite-output / analytic-germ / regulator-seed |
| `missing_family_data` | missing data needed for family or parameter-space promotion |
| `missing_projectivity_data` | missing data needed for Hodge-facing promotion |
| `promotion_blockers` | explicit blockers preventing promotion beyond registry status |

The registry is intentionally finite at this stage. New rows may be added when repo-grade proof-class analytic objects are constructed or source-captured.

## 4. Strata

The registry uses four initial strata.

### 4.1 Stratum S0 — null finite-character fixtures

Criterion:

```text
N = 1 or finite character is trivial;
no nontrivial finite monodromy output;
serves as a null or control fixture.
```

Current row:

```text
chain
```

### 4.2 Stratum S1 — closed finite-character fixtures

Criterion:

```text
finite monodromy denominator N is known;
finite character is nontrivial;
finite comparison fixture is closed under current Heller-Godel gates.
```

Current row:

```text
Catalan A1
```

### 4.3 Stratum S2 — regulator-adjacent local seeds

Criterion:

```text
object supplies or participates in local regulator-symbol output;
normalization, auxiliary-unit, or globalization caveats may remain;
not a global regulator theorem.
```

Current row:

```text
Motzkin
```

### 4.4 Stratum S3 — vocabulary-only or candidate rows

Criterion:

```text
object has vocabulary or candidate-source support but no closed fixture yet.
```

Current rows:

```text
none registered in this artifact
```

The p = 3 runway may eventually populate this stratum, but HG-MODULI-004 does not import p = 3 vocabulary as a proof-class analytic object.

## 5. Registry table

| registry_id | object_label | source_artifacts | object_status | exponent_type | N | finite_character | fixture_status | regulator_status | equivalence_layers_supported | missing_family_data | missing_projectivity_data | promotion_blockers |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `HG-PCAO-CHAIN-001` | Chain | `docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md`; `docs/appendices/appendix_a_chain_catalan_witness.md` | null fixture | integer | 1 | trivial | closed null witness | absent | finite-output; analytic-germ at null level | no family containing chain with nontrivial fixtures; no transition data | no projective target; no Hodge class; no cycles | null fixture cannot imply nontrivial parameter structure |
| `HG-PCAO-CAT-A1-001` | Catalan A1 | `docs/appendices/appendix_a_chain_catalan_witness.md`; `docs/proofs/catalan_a1_realization_equivalence.md`; `docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md` | closed finite fixture | rational-noninteger | 2 | nontrivial `mu_2` output | closed Catalan A1 fixture | absent in this row | finite-output; analytic-germ | no family containing Catalan and other fixtures; no transition data; no universal cover | no projective target; no Hodge class; no cycles | `mu_2` output cannot be promoted to Hodge target or projective parameter object |
| `HG-PCAO-MOTZKIN-001` | Motzkin | `docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md`; `docs/proofs/proof_class_moduli_construction_attempt.md` | caveated local seed | rational-noninteger, subject to source verification | unknown in registry row | finite character not closed in this registry row | partial / caveated | caveated local regulator seed | regulator-seed candidate only after analytic data and auxiliary unit are re-derived | no closed finite fixture; no verified auxiliary-unit derivation; no family data | no projective target; no Hodge class; no cycles | local regulator seed cannot be promoted to global regulator, Beilinson evidence, or Hodge bridge |

## 6. Promotion criteria

Promotion is one-way and evidence-gated. Registry membership does not imply promotion.

### 6.1 Promotion to closed finite fixture

A row may be promoted to closed finite fixture only if it supplies:

1. selected singularity;
2. exponent `alpha = a/N` in verified local form;
3. finite character `chi_N`;
4. branch-killing cover and singular unit;
5. regression or proof-apparatus support comparable to the Catalan A1 fixture;
6. explicit nonclaim envelope preserving Hodge boundaries.

### 6.2 Promotion to regulator-seed row

A row may be promoted to regulator-seed status only if it supplies:

1. local unit data;
2. regulator-symbol input pair;
3. normalization convention;
4. local output value;
5. caveat status for theorem-grade use;
6. explicit statement that local regulator output is not a global regulator theorem.

### 6.3 Promotion to analytic-family candidate

A row or collection of rows may be promoted to analytic-family candidate only if it supplies:

1. a parameter variable or base;
2. a family of generating functions over that base;
3. holomorphic variation of selected singularities;
4. stable Puiseux data across the proposed family;
5. branch-cover compatibility;
6. transition or comparison data between local realizations.

No current row satisfies these criteria.

### 6.4 Promotion to algebraic or projective candidate

A row or collection of rows may be promoted to algebraic or projective candidate only if it supplies, at minimum:

1. algebraic equations or a represented functor;
2. proof that the candidate object is algebraic;
3. for projective promotion, proof of projectivity;
4. relationship to a Hodge target datum if Hodge-facing use is intended.

No current row satisfies these criteria.

## 7. Failure annotations

Failure annotations are part of the registry object, not afterthoughts.

| Failure annotation | Meaning | Current affected rows |
| --- | --- | --- |
| `no-family-data` | no parameter family connects the row to other rows | all rows |
| `no-transition-data` | no local-to-local comparison or glueing data | all rows |
| `no-projective-target` | no smooth complex projective target is supplied | all rows |
| `no-hodge-class` | no rational Hodge class is supplied | all rows |
| `no-cycle-source` | no algebraic cycles are supplied | all rows |
| `local-regulator-caveat` | regulator value is local/caveated and not theorem-grade global data | Motzkin |
| `null-fixture-only` | row is useful only as a null/control fixture | Chain |
| `finite-output-only` | finite character is closed, but no higher structure follows | Catalan A1 |

These annotations prevent accidental promotion from registry organization to parameter-space or Hodge-facing claims.

## 8. Registry-aware restatement of HG-MODULI-002

HG-MODULI-002's three candidate starting points now become registry-aware:

1. Proof-class analytic objects are registry rows.
2. Realization-equivalence layers are row-level comparison labels, not quotient construction.
3. The D1 analytic realization assignment is row-local and does not globalize across rows.

This restatement narrows the construction:

```text
The registry supports row-local analytic realization, not a global parameter-space functor.
```

## 9. Current upper bound of apparatus-supported M_phi work

With this registry, the current apparatus supports:

```text
finite workbench organization of proof-class analytic objects;
stratum labels by finite character and regulator availability;
row-local analytic realization evidence;
explicit failure annotations.
```

It does not support:

```text
analytic parameter object;
algebraic parameter object;
projective parameter object;
universal family;
descent datum;
Hodge target extraction;
cycle realization;
cycle equality;
weight-bearing Hodge structure;
polarization.
```

## 10. Decision point after HG-MODULI-004

This artifact completes the currently supported weak parameter-organization layer.

The next program decision should not be treated as automatic. The current apparatus has now supplied what it can toward `M_phi` without new mathematical input.

Possible next directions:

1. Add new proof-class analytic rows, such as a verified p = 3 source if one is constructed.
2. Attempt an analytic-family construction by supplying a one-parameter family and transition data.
3. Return to the Beilinson/Motzkin caveat and re-derive the auxiliary unit and normalization.
4. Build Hodge Program structural checkers to reduce recurring registry maintenance cost.
5. Write a strategy spine summarizing the current boundary: stratified registry achieved; projective parameter unsupported.

This artifact does not choose among those directions.

## 11. Active obstruction-registry references

| Entry | Relevance |
| --- | --- |
| `OBS-HODGE-002` | registry organization is not projectivity |
| `OBS-HODGE-004` | Deligne and regulator data do not imply algebraicity |
| `OBS-HODGE-005` | finite monodromy rows are not Tate data |
| `OBS-HODGE-006` | row comparison is not motivic comparison |
| `OBS-HODGE-007` | regulator-seed rows are not regulator conjecture evidence |
| `OBS-HODGE-008` | Hodge-method registry is not Hodge progress |

## 12. Explicit nonclaim envelope

```text
No moduli space.
No parameter space.
No full M_phi construction.
No proof M_phi exists.
No topology on the registry.
No analytic structure on the registry.
No algebraic structure on the registry.
No projective structure on the registry.
No universal family.
No descent datum.
No Hodge target datum.
No rational Hodge class.
No algebraic cycles.
No cycle equality.
No Deligne-to-Hodge bridge theorem.
No Beilinson conjecture evidence.
No Tate evidence.
No motivic framework.
No Hodge progress.
No Clay-facing claim.
```

## 13. Final verdict

```text
HG-MODULI-004 constructs the weak stratified registry object that HG-MODULI-003 identified as currently feasible.

The registry contains three initial rows: chain, Catalan A1, and Motzkin.

It supports finite workbench organization and row-local analytic realization only.

It does not support analytic, algebraic, projective, or universal-family parameter structure.

After this artifact, the current apparatus-supported M_phi runway reaches a decision point: add new rows, supply new family data, harden governance checkers, or write the strategy spine.
```
