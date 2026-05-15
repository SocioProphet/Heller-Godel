# p = 3 Source Inventory for the Odd-Prime Front

Status: source-inventory note.  
Scope: preparatory only.  
Date: 2026-05-15.  
Depends on: Paper I / D1, especially Conjecture 6.3 and the Catalan A1 realization-equivalence vocabulary.

## Purpose

This note records the current repository support surface for a future `p = 3` odd-prime comparison scaffold.

The purpose is negative as much as positive: before defining a `mu_3` vocabulary surface, the repository must first identify whether it already contains usable Eisenstein, `A_2`, `SU(3)`, or `mu_3` material. A vocabulary PR should not be built from conversation memory alone.

## Search record

The following repository searches were run against `SocioProphet/Heller-Godel` before this note was added:

```text
Eisenstein
mu_3
μ_3
A_2
SU(3)
T_A2
T_{A_2}
odd-prime
odd prime
Conjecture 6.3
p=3
Z/p
Z/3
mu_p
root of unity
roots of unity
cyclic
finite-cyclic
prime
deck character
```

Connector search returned no indexed p = 3 / Eisenstein / A2 support surface in the live repository.

## Inventory conclusion

Current repo-grade support for a `p = 3` odd-prime comparison scaffold is thin.

The repository has a clean `mu_2` Catalan A1 baseline:

```text
Theorem 6.1
Corollary 6.2.C
Theorem A.7
Theorem A.8
docs/proofs/catalan_a1_realization_equivalence.md
```

But this baseline does not itself define `mu_3`, Eisenstein phases, `A_2`, `SU(3)`, or a `p = 3` fixture. Therefore the next odd-prime PR should not assert a `p = 3` comparison theorem and should not edit the D1 manuscript theorem stack.

## Required support before a p = 3 vocabulary PR

A future vocabulary-only `p = 3` PR should first introduce or locate all of the following primitives:

1. `p3 realization datum`;
2. `mu_3 finite-output map`;
3. `Eisenstein phase target`;
4. `p3 admissibility conditions`;
5. `p3 comparison boundary / nonclaim envelope`.

At minimum, that PR must define these as scaffolding vocabulary, not as a closed fixture.

## Nonclaim envelope for the p = 3 front

Any first `p = 3` vocabulary PR must explicitly state:

1. no generic `p` theorem;
2. no closed `p = 3` fixture;
3. no odd-prime dynamical target;
4. no general encoding theorem;
5. no Hodge strengthening;
6. no `A_n` generalization;
7. no gate minimality claim.

This envelope should be treated as a named primitive, not merely a disclaimer paragraph.

## Recommended next PR

The next safe PR is not a theorem PR. It should be one of:

1. a vocabulary-only `p = 3` scaffold that defines the five primitives above, if we are willing to introduce them from first principles; or
2. a source-capture PR that imports verified Eisenstein / `A_2` material into the repo before defining the five primitives.

Because current search found no repo-grade support surface, option 2 is safer if external or prior conversation material is available and can be cleanly captured.

## Relationship to Catalan A1

Catalan A1 remains the `mu_2` baseline. It should not be described through cube-root or Eisenstein language.

The `p = 3` front asks for the first odd-prime analogue using `mu_3`. It may later draw on Eisenstein or `A_2` structure, but that structure is not currently present in the repository according to the search record above.

## Governance posture

This note intentionally changes no theorem state.

It does not modify:

```text
Paper I / D1 theorem statements
Appendix A
harness code
claim-boundary guard
legacy topology audit policy
```

It is a preparatory proof-support inventory only.
