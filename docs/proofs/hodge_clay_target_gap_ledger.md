# Hodge / Clay Target Gap Ledger

Status: Clay-facing target and gap ledger.  
Scope: proof-strategy control document, not a theorem.  
Date: 2026-05-15.  
Depends on:

```text
docs/manuscripts/paper_i_deligne_cohomological_phase_characters.md
docs/appendices/appendix_a_chain_catalan_witness.md
docs/proofs/catalan_a1_realization_equivalence.md
docs/proofs/p3_source_inventory.md
docs/source-captures/eisenstein_mu3_capture.md
docs/proofs/p3_vocabulary_scaffold.md
docs/proofs/p3_source3_candidate_inventory.md
```

## Purpose

This ledger separates the current Heller-Godel proof surface from the Clay-facing Hodge target.

The repository has useful finite-character, Deligne-unit, Catalan A1, and p = 3 scaffolding work. None of that currently constitutes progress on the Hodge conjecture. A Clay-facing path requires explicit construction of the geometric objects that the Hodge conjecture actually asks about: smooth complex projective varieties, rational Hodge classes, algebraic cycles, and cycle-class realization.

This document records the gap without weakening the existing nonclaim boundary.

## Clay-facing target, stated operationally

A Clay-facing Hodge proof would need to address the following target shape:

```text
Given a nonsingular complex projective variety X and a rational Hodge class alpha in H^{2k}(X,Q) cap H^{k,k}(X), prove that alpha is a rational linear combination of cohomology classes of algebraic subvarieties of codimension k.
```

For this repository, that target decomposes into operational proof obligations:

1. specify the projective variety `X`;
2. specify the cohomological degree `2k` and Hodge type `(k,k)`;
3. construct or identify the rational Hodge class `alpha`;
4. construct algebraic cycles `Z_i` of codimension `k`;
5. prove the cycle-class equality

```text
alpha = sum_i q_i [Z_i],    q_i in Q;
```

6. prove that all constructions are functorial or invariant enough to survive changes of realization.

No current theorem in this repository supplies these six obligations.

## Current closed repository results

The current closed results are local, finite, and fixture-level:

```text
Theorem 6.1: analytic-topological mu_2 comparison
Proposition A.1: chain null finite-character witness
Proposition A.2: Catalan finite analytic witness
Proposition A.3: Klein-bottle mu_2 local-system witness
Theorem A.4: A1 spin-gate witness, convention A1-sauzin-normalization-v1
Theorem A.7: Catalan A1 encoding closure, convention A1-sauzin-normalization-v1
Theorem A.8: Catalan A1 mu_2 realization independence, output only
Corollary 6.2.C: Catalan A1 closed instance of Theorem 6.2
```

These results are valuable, but none constructs a smooth complex projective variety `X`, a rational Hodge class `alpha`, or algebraic cycles realizing that class.

## Current p = 3 runway

The p = 3 front is preparatory:

```text
p3 source inventory
Eisenstein / mu_3 source capture
p3 vocabulary scaffold
Source_3 candidate inventory
```

The p = 3 front currently has:

```text
no selected Source_3 candidate
no tested p = 3 fixture
no odd-prime dynamical target
no theorem-facing p = 3 claim
```

Therefore p = 3 work should not be described as Clay progress. It is only a possible future support lane for finite-phase arithmetic if a candidate and fixture are later constructed.

## Clay gap table

| Gap | Required for Clay-facing Hodge work | Current repository state |
| --- | --- | --- |
| Projective variety `X` | A nonsingular complex projective variety must be specified | Not constructed |
| Hodge class `alpha` | A rational class in `H^{2k}(X,Q) cap H^{k,k}` must be constructed | Not constructed |
| Algebraic cycles | Codimension-`k` algebraic subvarieties or cycle classes must be constructed | Not constructed |
| Cycle-class equality | A proof that `alpha = sum_i q_i[Z_i]` must be given | Not present |
| Realization independence | The class/cycle construction must not depend on arbitrary proof encoding choices | Only `mu_2` output independence for Catalan A1 is proved |
| Deligne-to-Hodge bridge | The current Deligne-unit/regulator framework must be connected to Hodge classes on projective varieties | Not constructed |
| p = 3 support | If used, a p = 3 source, fixture, and finite-output map must be built | Preparatory vocabulary only |
| Citation precision | The theorem-facing source chain must have page-level or theorem-level citations | Not complete |

## Nonclaim boundary

This ledger does not claim:

1. progress on the Hodge conjecture;
2. construction of a Hodge class;
3. construction of algebraic cycles;
4. a cycle-class equality;
5. a projective variety carrying the repository's proof-class invariant;
6. a Deligne-to-Hodge comparison theorem;
7. a p = 3 fixture;
8. an odd-prime dynamical target;
9. a general sentence-to-gate compiler;
10. a Clay-ready proof.

The ledger exists to keep those absences explicit.

## Optimal next proof front

The optimal next proof front is not yet another p = 3 preparatory note. The next Clay-facing front should define a **Hodge bridge requirements scaffold**.

That scaffold should introduce, without claiming existence:

1. `Hodge target datum`:

```text
(X, k, alpha)
```

where `X` is intended to be a smooth complex projective variety and `alpha` a rational Hodge class.

2. `Cycle realization datum`:

```text
(Z_i, q_i, cl(Z_i))
```

where `Z_i` are codimension-`k` algebraic cycles and `q_i in Q`.

3. `Cycle equality obligation`:

```text
alpha = sum_i q_i cl(Z_i)
```

4. `Deligne-to-Hodge bridge obligation`:

```text
current Deligne-unit / finite-character data -> candidate Hodge class alpha
```

5. `Clay nonclaim envelope`:

```text
no Hodge proof
no algebraic-cycle construction
no projective-variety construction
no theorem-grade bridge
```

Only after this Hodge bridge scaffold exists should the repository decide whether the p = 3 front is relevant to the Clay-facing path.

## Future PR contract

The next Clay-facing PR should add a Hodge bridge requirements scaffold under `docs/proofs/` or `docs/governance/`, without touching Paper I / D1 theorem statements.

A later PR may then evaluate whether the current Deligne-unit construction can define any candidate Hodge target datum. That later PR must be allowed to conclude negatively.

A theorem-facing Hodge PR is not warranted until the repository has at least:

1. a candidate projective variety `X`;
2. a candidate Hodge class `alpha`;
3. a candidate cycle family `Z_i`;
4. a precise equality obligation;
5. page-level or theorem-level citations for the external algebraic-geometry facts used.
