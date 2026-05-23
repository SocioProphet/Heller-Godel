# HG-FND-001 Normalization Preflight — Restricted Proof Grammar and Canonical Statistic

Status: preflight inspection only.  
Owner: `SocioProphet/Heller-Godel`.  
Related planning issue: `#97`.  
Target surface: `HG-FND-001`.  
Claim level: inspection / implementation planning only; no normalization performed by this document.

## 1. Executive finding

`HG-FND-001` is not currently materialized as a normalized standalone framework-foundational document. It exists as a named candidate Tier-1 surface:

```text
HG-FND-001 — Restricted proof grammar and canonical statistic
candidate; active core exists, registry normalization pending
```

Repository inspection shows that downstream P3 documents use `HG-FND-001` as the candidate-grade foundation for restricted proof grammars and canonical statistics. Normalizing `HG-FND-001` is therefore substantive framework-foundational authoring, not polish.

The normalized document must define the restricted proof-grammar primitive strongly enough to discharge the candidate status used by A1 and A2/P3.a grammar work, without promoting `HG-MTH-011` to theorem-grade by itself.

## 2. Reference audit

The audit found the following active reference surfaces.

| File | Role of `HG-FND-001` reference | Preflight conclusion |
| --- | --- | --- |
| `docs/framework-core/distance-classification.md` | Canonical candidate inventory entry. | Source of current candidate status and Tier-1 promotion rules. |
| `docs/framework-core/claim-grammar.md` | Registry and downstream citation language; post-P3 cumulative grade chain. | Must be updated in implementation PR if `HG-FND-001` is normalized. |
| `docs/gate-minimality/p3-pipeline-integration-scope.md` | P3 dependency chain references P3.a attachment to `HG-FND-001`. | Historical scope; likely no language change needed except possibly post-normalization note. |
| `docs/gate-minimality/p3a-proof-grammar-p3-scope.md` | Defines P3.a obligation as restricted proof grammar at `p=3`, consistent with `HG-FND-001`. | Contains the best local statement of what `HG-FND-001` must normalize. |
| `docs/gate-minimality/p3a-proof-grammar-p3-closure.md` | Constructs the arity-three grammar and grades it modulo candidate-`HG-FND-001`. | Must be updated from candidate-modulo language to normalized-dependency language after implementation. |
| `docs/gate-minimality/p3b-generating-function-p3-scope.md` | Mentions P3.a / `HG-FND-001` as upstream for generating-function work. | May require only dependency-language adjustment after `HG-FND-001` normalization. |
| `docs/gate-minimality/p3b-generating-function-p3-closure.md` | Uses P3.a grammar and states P3.b depends on P3.a; direct grade ceiling is `HG-FND-002`. | Should not be regraded by `HG-FND-001` alone, but may cite the normalized grammar foundation. |
| `docs/gate-minimality/p3c-*` and `p3d-*` | Appear through cumulative grade-chain lists. | Do not change mathematical content during `HG-FND-001` normalization. |
| `docs/framework-core/anti-seed-framework.md` | No dedicated anti-seed for restricted proof grammar currently exists. | Implementation PR must add an anti-seed entry before positive Tier-1 normalization. |

## 3. Assumptions currently placed on HG-FND-001

Current documents assume that `HG-FND-001` supplies at least the following primitives:

1. A fixed proof fragment `F`, with intended default a simply typed lambda-calculus / implicational propositional fragment.
2. Canonical normal inhabitants represented by alpha-classes of eta-long beta-normal de Bruijn lambda terms.
3. A restricted production-rule discipline: only displayed production rules generate witnesses.
4. A typing environment discipline: variables and constructors have explicit simple types.
5. A canonical statistic on normal forms:

```text
sigma_C(s)=#lambda-nodes + #application-nodes + #variable-leaves.
```

6. A rule that any alternative statistic or grammar convention must be explicitly declared and examples recomputed.
7. A separation between the upstream type-theoretic grammar and downstream analytic/combinatorial visualizations such as rooted trees or Fuss-Catalan equations.
8. A discharge criterion determining when a proof-family example becomes theorem-bearing rather than merely analytic calibration.

## 4. Minimal mathematical objects required in the normalized document

The future implementation PR should author a standalone document, proposed path:

```text
docs/framework-foundations/HG-FND-001-restricted-proof-grammar.md
```

The normalized `HG-FND-001` document should contain these objects.

### 4.1 Typed fragment

Define a simply typed implicational fragment with:

```text
Types: A | B | ... | (T -> U)
Contexts: finite typed variable/constant environments
Terms: variables, constants/constructors, lambda abstraction, application
```

The document may keep the grammar narrow and schema-level. It should not need to formalize all of STLC; it should define the exact fragment consumed by the Heller-Godel proof-character pipeline.

### 4.2 Normal-form convention

Define canonical witnesses as alpha-classes of eta-long beta-normal forms, represented using de Bruijn indexing or an explicitly equivalent alpha-stable convention.

Required boundary:

```text
Alpha-renaming is quotient data; beta-reduction and eta-expansion are normalization conventions, not extra production rules.
```

### 4.3 Restricted production rules

Define what it means for a restricted proof grammar to be generated only by displayed production rules. The A1 and A2 examples should be canonical fixtures:

```text
A1: C_A = (A -> A -> A) -> A -> A
    T ::= x | b(T,T)

A2/P3.a: C_A^(3) = (A -> A -> A -> A) -> A -> A
         T ::= x | t(T,T,T)
```

The normalized document should state that these are grammar schemas over typed normal-form witnesses, not untyped tree claims.

### 4.4 Canonical statistic

Define `sigma_C` exactly:

```text
sigma_C(s)=#lambda-nodes + #application-nodes + #variable-leaves.
```

Then state the implementation discipline that closure documents may also use a derived constructor-shape statistic for generating-function extraction, but must declare when a derived statistic rather than full node-count statistic is being used. This is a likely load-bearing ambiguity: P3.a cites manuscript `sigma_C`, while P3.b uses constructor-shape statistic for `C_3(x)=1+xC_3(x)^3`. The normalized foundation should make this relation explicit.

### 4.5 Proof-family generating interface

Define the interface from restricted grammar to generating function without taking over `HG-FND-002`:

```text
restricted grammar + declared statistic -> countable witness family N_phi -> T_phi^sigma(x)=sum_s x^sigma(s)
```

`HG-FND-001` should stop at well-typed restricted grammar and statistic definition. `HG-FND-002` owns the generating-function construction and analytic closure.

### 4.6 Discharge criterion

Define what candidate status is discharged by `HG-FND-001` normalization:

- The grammar is fixed.
- The witness equivalence relation is fixed.
- The statistic or declared derived statistic is fixed.
- Only displayed productions generate witnesses.
- Downstream closures may cite the normalized grammar foundation without repeating the entire proof-fragment caveat.

This does not discharge `HG-FND-002` or any analytic/Puiseux/phase/carry surface.

## 5. Anti-seed requirement

Tier-1 promotion requires an anti-seed entry before positive promotion. The current anti-seed register does not contain a dedicated restricted-proof-grammar anti-seed.

The implementation PR should add an entry such as:

```text
A-HG-FND-009 — Treating untyped tree analogies as typed proof grammars
```

Failure mode:

```text
A downstream artifact cites a rooted-tree, Catalan, or Fuss-Catalan enumeration as theorem-bearing proof-family data without specifying the typed fragment, normal-form convention, witness equivalence, and statistic.
```

Correct boundary:

```text
Tree enumerations are admissible only as visualizations or derived enumerators of a normalized restricted proof grammar with typed normal-form witnesses and declared statistic.
```

The precise anti-seed identifier should be selected by inspecting the current register at implementation time. As of this preflight, the next available `A-HG-FND-*` number appears to be `A-HG-FND-009` because `A-HG-FND-001..004` are used and later entries occupy `A-HG-VOC-*`, `A-HG-MTH-*`, and `A-HG-DOC-*` namespaces.

## 6. Grade target

Target grade for the implementation PR:

```text
HG-FND-001 — framework-foundational / Tier 1 normalized surface
```

Expected effect on grade chain:

```text
HG-MTH-014 no longer modulo candidate-HG-FND-001.
HG-MTH-011 cumulative modulo chain reduces from six candidate Tier-1 surfaces to five.
```

Remaining candidate surfaces after successful `HG-FND-001` normalization:

```text
HG-FND-002
HG-FND-003
HG-VOC-006
HG-FND-006
HG-FND-007
```

This is not theorem-grade promotion of `HG-MTH-011`.

## 7. Implementation PR file plan

Expected file changes for the implementation PR:

1. New: `docs/framework-foundations/HG-FND-001-restricted-proof-grammar.md`.
2. Modify: `docs/framework-core/distance-classification.md` to move `HG-FND-001` from candidate to normalized Tier-1 status.
3. Modify: `docs/framework-core/claim-grammar.md` to add citation guidance and reduce `HG-MTH-011` dependency count if appropriate.
4. Modify: `docs/framework-core/anti-seed-framework.md` to add the restricted-grammar anti-seed.
5. Modify: `docs/gate-minimality/p3a-proof-grammar-p3-closure.md` to replace `candidate-HG-FND-001` grade ceiling with normalized `HG-FND-001` dependency language.
6. Optionally modify: `docs/gate-minimality/p3a-proof-grammar-p3-scope.md` only if a post-normalization note is necessary.
7. Optionally modify: `docs/gate-minimality/p3-pipeline-integration-closure.md` and `docs/gate-minimality/a2-minimality-candidate-theorem.md` to reduce six-surface wording to five remaining candidate surfaces after normalization. This must be handled carefully to preserve historical P3 closure text.
8. New test: a CI/lint test that verifies `HG-FND-001` has a normalized document and that no active grade declaration still says `method-grade modulo candidate-HG-FND-001`.

## 8. Validation expectation

The implementation PR should add a test, proposed path:

```text
tests/test_hg_fnd_001_normalization.py
```

Minimum assertions:

1. Normalized document exists at the selected path.
2. Document contains typed fragment, eta-long beta-normal, de Bruijn, restricted production rules, `sigma_C`, A1 and A2 grammar examples, anti-seed reference, and non-claims.
3. `distance-classification.md` marks `HG-FND-001` as normalized / active Tier 1 rather than candidate.
4. No active grade declaration contains `candidate-HG-FND-001` after normalization, except historical/provenance notes explicitly marked historical.
5. `HG-MTH-011` remaining candidate-surface count is five if the implementation PR updates the cumulative grade chain.

## 9. Non-claims for this preflight

This preflight does not normalize `HG-FND-001`.

This preflight does not author the framework-foundational document.

This preflight does not promote `HG-MTH-011` to theorem-grade.

This preflight does not discharge `HG-FND-002`, `HG-FND-003`, `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`.

This preflight does not close P1 path-beta uniqueness or P2 candidate-list exhaustion.

This preflight does not extend to `A_n`.

This preflight does not authorize Heller-Einstein realization-question work.

This preflight does not cross into downstream `SocioProphet/yang-mills`, `np-program`, `bsd-proof-program`, or `ns-program` proof claims.

This preflight does not modify Heller-Dirac.

## 10. Recommended next action after this preflight

If this preflight merges cleanly, the next authorized implementation should be a single-surface `HG-FND-001` normalization PR, not bundled with `HG-FND-002`.

Rationale: `HG-FND-001` owns the typed restricted grammar and statistic foundation. `HG-FND-002` owns the proof-family generating-function construction and should reuse the normalized grammar foundation rather than be co-defined with it.
