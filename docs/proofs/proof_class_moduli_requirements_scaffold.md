# Proof-Class Moduli Requirements Scaffold

Status: requirements scaffold.  
Classification (Hodge Program lane): `hodge-method`.  
Claim level: requirements / nonclaim.  
Purpose: specify what a proof-class moduli object `M_phi` would need to support before any Heller-Godel artifact could be evaluated for Hodge bridge promotion.

## 1. Provenance and scope

This scaffold is motivated by two repo-grade findings:

1. `docs/proofs/proof_class_moduli_bottleneck_consolidation.md` records that the Mode-A, Mode-B, and Mode-C artifacts independently identify proof-class moduli `M_phi` as the central structural bottleneck.
2. `SocioProphet/hodge-program-proof: docs/evaluations/hodge_eval_001_heller_godel_apparatus.md` records a negative bridge evaluation: the current Heller-Godel apparatus does not supply a Hodge target datum, algebraic cycles, cycle equality, or Deligne-to-Hodge bridge theorem.

This document specifies requirements for a future `M_phi`. It does not construct `M_phi`.

## 2. Governing nonclaim

The scaffold lists requirements. It does not establish that the requirements are satisfiable, jointly compatible, independent, exhaustive, or realizable by any mathematical object.

In particular:

```text
requirements != construction
bottleneck identification != bottleneck resolution
candidate vocabulary != existence theorem
```

## 3. Desired role of M_phi

A proof-class moduli object `M_phi` would be expected to mediate between:

```text
proof-class data
  -> analytic realization data
  -> Deligne-unit / finite-character / regulator-symbol data
  -> candidate Hodge target data, if such data can be constructed
```

The target role is deliberately conditional. A valid outcome of future work may be:

```text
No object M_phi satisfying these requirements can currently be constructed.
```

## 4. Primitive 1 — Proof-class object

A proof-class object should specify what the points or objects of `M_phi` are intended to represent.

Minimum required data:

1. a formal theory or proof calculus context;
2. a sentence or type `phi`;
3. a class of normal proofs or proof representatives;
4. a statistic or grading compatible with the Heller-Godel generating-function construction;
5. a reference to the associated proof-class generating function `T_phi` where defined.

Open requirement:

```text
Define whether proof-class objects are individual proofs, equivalence classes of proofs, generating-function germs, decorated analytic data, or a higher categorical package.
```

Nonclaim:

```text
This primitive does not define M_phi and does not establish that proof-class objects form a moduli space.
```

## 5. Primitive 2 — Realization-equivalence relation

A realization-equivalence relation should specify when two proof-class objects define the same object of the would-be moduli space.

Possible equivalence layers:

1. syntactic equivalence of normal forms;
2. equality of proof-class generating functions;
3. equality of analytic germs at the dominant singularity;
4. equality of Puiseux exponent data;
5. equality of finite `mu_N` monodromy character;
6. equality of Deligne-unit class;
7. equality after regulator-symbol evaluation.

Open requirement:

```text
Choose which equivalence layer is intended and prove that the chosen relation is stable under the operations used in D1.
```

Nonclaim:

```text
This scaffold does not choose a final equivalence relation and does not prove that any candidate relation is moduli-suitable.
```

## 6. Primitive 3 — Candidate parameter space or stack type

A future `M_phi` must specify the category in which it lives.

Candidate ambient types include:

1. finite set or finite groupoid;
2. complex analytic space;
3. algebraic variety;
4. smooth variety;
5. smooth complex projective variety;
6. Deligne-Mumford stack;
7. Artin stack;
8. derived or higher stack.

Hodge bridge relevance:

```text
A Hodge target datum ultimately requires a nonsingular complex projective variety X.
```

Therefore, a merely finite, analytic, real, compact Kahler, or stack-like object is not automatically sufficient.

Open requirement:

```text
Specify the type of M_phi and the relationship, if any, between M_phi and a projective target variety X.
```

Nonclaim:

```text
This scaffold does not assert that M_phi is projective, algebraic, smooth, Kahler, or stack-like.
```

## 7. Primitive 4 — Analytic realization functor

An analytic realization functor would map proof-class objects into the analytic data used by D1.

Desired shape:

```text
R_an: proof-class object -> (T_phi, rho, Puiseux data, branch-killing cover, singular unit)
```

Minimum output data:

1. proof-class generating function `T_phi`;
2. dominant or selected singularity `rho`;
3. Puiseux exponent `alpha = a/N` where applicable;
4. branch-killing cover;
5. Puiseux singular unit;
6. finite monodromy character.

Open requirement:

```text
Define R_an and prove it is functorial under the chosen realization-equivalence relation.
```

Nonclaim:

```text
The current Heller-Godel apparatus supplies examples of analytic realization data, not a moduli-level functor R_an.
```

## 8. Primitive 5 — Finite monodromy / mu_N local-system structure

`M_phi` must explain how finite monodromy data varies over proof-class objects.

Minimum structure:

1. a local system or character sheaf recording `mu_N` data;
2. compatibility with branch-killing covers;
3. compatibility with p-primary projections;
4. behavior under product or decorated product of proof-class data;
5. treatment of the `mu_2` Catalan A1 fixture as a closed example.

Open requirement:

```text
Define the finite-character local-system package over M_phi or over a target derived from M_phi.
```

Nonclaim:

```text
Finite monodromy is not Tate data and does not by itself define a Hodge target datum.
```

## 9. Primitive 6 — Deligne-unit family

A future `M_phi` must explain whether the D1 Deligne-unit construction can be organized in families.

Desired shape:

```text
U_D: M_phi -> Deligne-unit data
```

or, more explicitly:

```text
object of M_phi -> H^1_D(X_{phi,rho}^circ, Z(1)) class
```

Minimum requirements:

1. target spaces for the Deligne classes;
2. functoriality under realization equivalence;
3. compatibility with finite monodromy descent;
4. compatibility with local regulator-symbol operations;
5. clear separation between Bockstein carry and Deligne cup-product symbol.

Open requirement:

```text
Define whether the Deligne-unit family lives over M_phi itself, over an analytic cover, or over a separate universal space.
```

Nonclaim:

```text
A family of Deligne units is not a family of algebraic cycles and does not imply algebraicity.
```

## 10. Primitive 7 — Local regulator-symbol package

The Beilinson regulator artifact supplies local regulator-symbol output. A future `M_phi` must specify how such outputs globalize, if they do.

Required questions:

1. What is the global domain of the regulator-symbol computation?
2. Does the local punctured-curve regulator extend to a global regulator object?
3. Does the global object define a motivic cohomology class?
4. Is there any relation to special values or Beilinson-type conjectures?
5. If not, where exactly does globalization fail?

Open requirement:

```text
Define a globalization criterion for local regulator-symbol outputs.
```

Nonclaim:

```text
The local Catalan/Motzkin regulator values do not constitute Beilinson conjecture evidence or a Hodge bridge.
```

## 11. Primitive 8 — Candidate Hodge target extraction

This is the first primitive that would interact directly with the Hodge bridge scaffold.

Desired shape:

```text
E_H: M_phi -> (X, k, alpha)
```

where `(X,k,alpha)` is a Hodge target datum.

Minimum requirements:

1. definition of `X`;
2. proof `X` is nonsingular;
3. proof `X` is complex projective;
4. definition of `k`;
5. definition of `alpha` in `H^{2k}(X,Q)`;
6. proof `alpha` has Hodge type `(k,k)`.

Open requirement:

```text
Define whether E_H can exist at all for the current Heller-Godel apparatus.
```

Nonclaim:

```text
This scaffold does not construct E_H and does not provide a Hodge target datum.
```

## 12. Primitive 9 — Cycle realization candidate

If a Hodge target datum is supplied, a future `M_phi` bridge must then explain how algebraic cycles enter.

Desired shape:

```text
E_C: M_phi -> (Z_i, q_i, cl(Z_i))_{i in I}
```

Minimum requirements:

1. definitions of the algebraic cycles `Z_i`;
2. proof each `Z_i` is algebraic;
3. proof each `Z_i` has codimension `k`;
4. rational coefficients `q_i`;
5. the cycle class map;
6. compatibility with the target variety `X`.

Open requirement:

```text
Specify any plausible source of algebraic cycles from proof-class data, or explicitly record that none is known.
```

Nonclaim:

```text
No algebraic cycles are constructed here.
```

## 13. Primitive 10 — Cycle equality target

The Hodge conjecture-facing equality is:

```text
alpha = sum_i q_i cl(Z_i)
```

in `H^{2k}(X,Q)`.

A future `M_phi` construction would need to make this equality meaningful before it could prove or disprove it.

Minimum requirements:

1. common cohomology group for both sides;
2. definition of `alpha`;
3. definitions of `cl(Z_i)`;
4. proof the equality is well-typed;
5. proof the equality holds.

Open requirement:

```text
Define the cohomological target in which a future cycle equality would live.
```

Nonclaim:

```text
This scaffold does not state, prove, or even instantiate a cycle equality.
```

## 14. Primitive 11 — Weight-bearing Hodge structure

The Kuga-Satake / K3 diagnostic shows that direct transfer fails because Heller-Godel currently has weight-0 finite-character data rather than weight-2 polarized Hodge structure.

A future `M_phi` relevant to Kuga-Satake-style transfer would need:

1. a rational vector space or cohomology group;
2. Hodge decomposition or filtration;
3. weight structure;
4. polarization;
5. compatibility with proof-class realization data;
6. a reason the weight is the correct one for the intended comparison.

Open requirement:

```text
Determine whether proof-class moduli can support any weight-bearing Hodge structure at all.
```

Nonclaim:

```text
No weight-bearing Hodge structure is constructed here.
```

## 15. Primitive 12 — Polarization structure

A Hodge-theoretic target generally requires polarization or a substitute structure to support comparison, Kuga-Satake, and Hodge-Riemann-style arguments.

Minimum requirements:

1. bilinear or Hermitian form;
2. positivity or signature condition;
3. compatibility with Hodge filtration or decomposition;
4. functoriality under realization equivalence;
5. relation to the proof-class data.

Open requirement:

```text
Identify any natural polarization candidate, or record that none is known.
```

Nonclaim:

```text
No polarization is constructed here.
```

## 16. Failure modes

A future attempt to construct `M_phi` may fail in multiple ways.

Expected failure modes:

| Failure mode | Meaning |
| --- | --- |
| no stable realization equivalence | proof-class data do not admit moduli-style quotient |
| analytic-only object | `M_phi` exists analytically but not projectively |
| finite-only object | only finite monodromy data globalize |
| regulator-locality failure | local regulator outputs do not globalize |
| no Hodge target | no `(X,k,alpha)` extraction exists |
| no cycle source | no algebraic cycles arise from proof data |
| incompatibility of requirements | primitives cannot be jointly satisfied |
| overfitting to Catalan A1 | scaffold works only for the `mu_2` closed fixture |

A failure in any of these modes is a valid research result if documented precisely.

## 17. Minimal evaluation checklist for HG-MODULI-002

A future construction attempt should be evaluated against the following checklist:

| Question | Expected answer type |
| --- | --- |
| What are the objects of `M_phi`? | definition |
| What is the equivalence relation? | definition + proof of relation properties |
| What category does `M_phi` live in? | finite / analytic / algebraic / stack / other |
| Is `M_phi` projective? | proof or explicit no |
| Does it supply `(X,k,alpha)`? | construction or no |
| Does it supply cycles? | construction or no |
| Does it state a cycle equality? | theorem target or no |
| Does it globalize local regulator data? | theorem / partial / no |
| Does it support a weight-bearing Hodge structure? | theorem / partial / no |
| Are requirements jointly satisfiable? | proof / unknown / contradiction |

## 18. Relationship to HODGE-EVAL-001

`HODGE-EVAL-001` concluded that the current apparatus supplies no Hodge target datum, no algebraic cycles, no cycle equality, and no Deligne-to-Hodge bridge theorem.

This scaffold is the Heller-Godel-side response to that finding. It translates the negative evaluation into requirements for a future object.

It does not change the result of `HODGE-EVAL-001`.

## 19. Active obstruction-registry references

| Entry | Relevance |
| --- | --- |
| `OBS-HODGE-002` | `M_phi` must not be treated as projective merely because it may be analytic or compact |
| `OBS-HODGE-004` | Deligne-unit and regulator-symbol data are not algebraicity |
| `OBS-HODGE-005` | finite monodromy is not Tate data |
| `OBS-HODGE-006` | comparison diagrams are not motives |
| `OBS-HODGE-007` | regulator symbols are not regulator conjectures |
| `OBS-HODGE-008` | Hodge-origin requirements are not Hodge proof |

## 20. Cross-references

Heller-Godel:

```text
docs/proofs/proof_class_moduli_bottleneck_consolidation.md
docs/proofs/soule_voisin_ah_torsion_witness_artifact.md
docs/proofs/beilinson_regulator_catalan_motzkin_artifact.md
docs/proofs/kuga_satake_k3_technique_transfer_diagnostic.md
docs/proofs/hodge_clay_target_gap_ledger.md
docs/proofs/catalan_a1_realization_equivalence.md
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
```

Hodge Program:

```text
SocioProphet/hodge-program-proof: docs/scaffolds/hodge_bridge_requirements_scaffold.md
SocioProphet/hodge-program-proof: docs/evaluations/hodge_eval_001_heller_godel_apparatus.md
SocioProphet/hodge-program-proof: docs/obstruction-registry.md
SocioProphet/hodge-program-proof: docs/registries/heller-godel-artifact-registry.md
```

## 21. Explicit nonclaim envelope

```text
No construction of M_phi.
No proof M_phi exists.
No proof M_phi is smooth, Kahler, projective, algebraic, or stack-like.
No proof any listed requirement is satisfiable.
No proof the listed requirements are jointly satisfiable.
No proof the listed requirements are independent.
No proof the listed requirements are exhaustive.
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

## 22. Next substantive move

After this scaffold, the next substantive research move is not another registry. It is a construction attempt or impossibility/refinement pass:

```text
HG-MODULI-002: attempt to construct, partially construct, or refute a candidate M_phi against this checklist.
```

Valid outcomes of `HG-MODULI-002` include:

1. candidate construction satisfying some requirements;
2. partial construction with explicit missing primitives;
3. proof that selected requirements are incompatible;
4. proof that only a weaker analytic or finite object exists;
5. refinement of the requirements after discovering overconstraint.

All five outcomes are research-positive if documented precisely.
