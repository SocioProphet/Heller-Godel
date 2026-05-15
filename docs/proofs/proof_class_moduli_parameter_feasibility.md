# HG-MODULI-003 — Parameter-Object Feasibility for Proof-Class Analytic Objects

Status: feasibility analysis.  
Classification (Hodge Program lane): `hodge-method`.  
Claim level: feasibility / obstruction analysis / nonclaim.  
Purpose: evaluate whether the proof-class analytic objects introduced in `HG-MODULI-002` can plausibly be organized into a parameter object without promoting that object to a Hodge target, projective variety, or moduli construction.

## 1. Scope and governing nonclaim

This artifact analyzes parameter-object feasibility. It does not construct a parameter object.

It addresses four sub-questions:

1. structural feasibility: can chain, Catalan A1, and Motzkin be treated as objects in one organizing class?
2. type-theoretic feasibility: what kind of mathematical object could organize them?
3. projectivity risk: does any natural organizing object satisfy the projective requirement needed for Hodge target extraction?
4. next-step feasibility: what should `HG-MODULI-004` attempt or refuse?

Nonclaim:

```text
No parameter object is constructed.
No moduli space is constructed.
No proof-class moduli M_phi is constructed.
No projective variety is supplied.
No Hodge target datum is supplied.
No algebraic cycles are supplied.
No cycle equality is supplied.
No Deligne-to-Hodge bridge theorem is supplied.
```

## 2. Input from HG-MODULI-002

`HG-MODULI-002` introduced proof-class analytic objects of the form:

```text
P = (phi, T_phi, rho, alpha, N, a, V_rho^x, q, X_rho^x, u, chi_N)
```

and identified three instantiations:

| Object | Role |
| --- | --- |
| Chain | null finite-character object |
| Catalan A1 | nontrivial `mu_2` object |
| Motzkin | regulator-adjacent object subject to local-regulator caveats |

It then identified the next obstruction:

```text
parameter-object feasibility for proof-class analytic objects
```

This document analyzes that obstruction.

## 3. Structural feasibility

### 3.1 Common organizing class

The three examples share a common tuple schema:

```text
proof-family label
proof-class generating function or local generating-function representative
selected singularity
Puiseux / exponent data where applicable
finite monodromy character where applicable
analytic cover / singular unit where applicable
optional regulator-seed data
```

Therefore they can be organized at the level of a common class of decorated analytic proof-family objects.

Verdict:

```text
structural feasibility: yes, at the class-of-objects level.
```

### 3.2 Limits of structural feasibility

This does not imply any of the following:

1. that the class has a natural topology;
2. that it has an analytic structure;
3. that it has algebraic structure;
4. that it has finite type;
5. that it is projective;
6. that it represents a moduli functor;
7. that it supports a universal family.

Finding:

```text
The current apparatus supports a common organizing class, not yet a parameter space.
```

## 4. Type-theoretic feasibility

Candidate organizing types are evaluated below.

### 4.1 Discrete registry type

A discrete registry type is simply a finite or countable catalog of proof-class analytic objects.

Support:

```text
chain, Catalan A1, and Motzkin can be listed immediately.
```

Strength:

```text
lowest risk; preserves nonclaims; compatible with current apparatus.
```

Weakness:

```text
no topology, no deformation theory, no family, no Hodge target extraction.
```

Verdict:

```text
feasible now, but too weak for later Hodge bridge primitives.
```

### 4.2 Stratified discrete type

A stratified discrete type organizes objects by finite invariants such as:

```text
integer exponent versus rational noninteger exponent
monodromy denominator N
finite character value
available regulator-seed data
known closed fixture status
```

Support:

```text
current examples naturally occupy different strata:
chain: N = 1;
Catalan A1: N = 2;
Motzkin: regulator-adjacent stratum, subject to local caveats.
```

Strength:

```text
preserves current distinctions and supports construction sequencing.
```

Weakness:

```text
still no analytic family or projective structure.
```

Verdict:

```text
best currently feasible weak parameter substitute.
```

### 4.3 Complex analytic parameter type

A complex analytic parameter object would require the proof-class analytic objects to vary holomorphically in parameters.

Current support:

```text
none established.
```

Necessary additional data:

1. a parameter variable or base;
2. a family of generating functions `T_phi_s`;
3. holomorphic variation of selected singularities;
4. stable Puiseux data across strata;
5. branch-cover compatibility across the family.

Verdict:

```text
not feasible from current apparatus without new family data.
```

### 4.4 Algebraic parameter type

An algebraic parameter object would require algebraic equations or functor-of-points style data organizing the proof-class analytic objects.

Current support:

```text
none established.
```

Risk:

```text
would invite false promotion from analytic generating-function data to algebraic geometry.
```

Verdict:

```text
not feasible now.
```

### 4.5 Projective parameter type

A smooth complex projective variety would be the relevant kind of object for Hodge target extraction.

Current support:

```text
none.
```

OBS-HODGE-002 boundary:

```text
A compact, analytic, finite, or stratified object is not enough.
Projectivity cannot be inferred from organization of proof-class analytic objects.
```

Verdict:

```text
not feasible now; no projectivity evidence.
```

## 5. Dimensionality question

The current examples support at most a discrete or stratified-discrete organizing object.

Supported dimensions:

```text
0-dimensional discrete catalog: feasible.
positive-dimensional analytic family: unsupported.
algebraic finite-type family: unsupported.
projective family: unsupported.
```

Finding:

```text
The current data do not justify a continuous parameter object.
```

This is a substantive limitation. It means the current construction path remains proof-fabric and analytic-method oriented, not moduli-geometric.

## 6. Descent and glueing question

A parameter object would need local analytic realizations to glue or descend into global family data.

Current status:

```text
chain, Catalan, and Motzkin are separate local examples.
No transition functions exist between them.
No common family is known.
No descent datum is defined.
```

Verdict:

```text
descent/glueing feasibility: no support.
```

Construction implication:

```text
Do not attempt a universal family in HG-MODULI-004 unless new transition or family data are first supplied.
```

## 7. Projectivity and OBS-HODGE-002 risk

The natural object currently available is a stratified registry of analytic-decorated examples. Such an object is not projective and should not be treated as a proxy for a projective variety.

OBS-HODGE-002 applies directly:

```text
Projectivity is not a cosmetic condition.
It is part of the Hodge target requirement.
A non-projective or non-algebraic parameter object cannot satisfy the Hodge target primitive.
```

Finding:

```text
The currently feasible organizing object is non-Hodge-facing.
It may be useful for workbench sequencing, but it does not advance Hodge target extraction.
```

## 8. Feasibility verdict matrix

| Candidate parameter type | Feasibility from current apparatus | Hodge relevance | Verdict |
| --- | --- | --- | --- |
| discrete registry | yes | none by itself | feasible weak substitute |
| stratified discrete registry | yes | none by itself | recommended next workbench object |
| complex analytic space | no current support | insufficient even if found | defer |
| algebraic variety | no current support | potential future relevance | defer |
| smooth complex projective variety | no current support | required for Hodge target extraction | not feasible now |
| universal family / descent object | no current support | potential future relevance | defer |

## 9. Recommended HG-MODULI-004 target

The next constructive artifact should not attempt a projective parameter space.

Recommended target:

```text
HG-MODULI-004: stratified registry object for proof-class analytic objects.
```

Minimum content:

1. define a stratified registry schema;
2. register chain, Catalan A1, and Motzkin objects;
3. record stratum labels: exponent type, denominator `N`, finite character, regulator availability, fixture status;
4. record missing family/descent/projectivity data per object;
5. define promotion criteria from registry object to analytic family candidate.

Expected result:

```text
A workbench parameter substitute, not a moduli space.
```

## 10. What would be needed for stronger parameter feasibility

To move beyond a stratified registry, the program would need at least one of:

1. a one-parameter family of proof-class generating functions containing known examples;
2. a deformation theory for proof-class analytic objects;
3. transition data between local analytic realizations;
4. a functor represented by the candidate parameter object;
5. algebraic equations defining a candidate family;
6. proof that a candidate algebraic family is projective or maps to a projective target.

None of these are currently supplied.

## 11. Relationship to HODGE-EVAL-001

This feasibility analysis does not change the negative bridge evaluation.

It sharpens one item from that evaluation:

```text
The current apparatus cannot supply a Hodge target because even the parameter-object layer is only feasible as a weak stratified registry.
```

## 12. Active obstruction-registry references

| Entry | Relevance |
| --- | --- |
| `OBS-HODGE-002` | projectivity cannot be inferred from finite or analytic organization |
| `OBS-HODGE-004` | analytic and Deligne data are not algebraicity |
| `OBS-HODGE-006` | organizing comparisons is not motivic realization |
| `OBS-HODGE-008` | Hodge-origin method structure is not Hodge progress |

## 13. Explicit nonclaim envelope

```text
No parameter object construction.
No moduli space construction.
No proof M_phi exists.
No analytic family construction.
No algebraic family construction.
No projective variety.
No universal family.
No descent datum.
No Hodge target datum.
No algebraic cycles.
No cycle equality.
No Deligne-to-Hodge bridge theorem.
No Hodge progress.
No Clay-facing claim.
```

## 14. Final verdict

```text
Parameter-object feasibility is positive only at the weak workbench level.

The current apparatus supports a discrete or stratified-discrete registry of proof-class analytic objects.

It does not support a complex analytic, algebraic, projective, or universal-family parameter object.

HG-MODULI-004 should construct the stratified registry object explicitly, with promotion criteria and failure annotations.
```
