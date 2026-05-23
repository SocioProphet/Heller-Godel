# P3 — A2 Minimality Pipeline-Integration Scope

Status: scope document; obligation not closed.  
Owner: `SocioProphet/Heller-Godel`.  
Track: A2 gate-minimality, `HG-MTH-011`, proof-character pipeline at `p=3`.  
Claim level: scope / admissibility planning only.  
Identifier posture: no new `HG-*` identifier is assigned by this scope note.

## Purpose

This document scopes P3, the pipeline-integration obligation recorded in `HG-MTH-011`.

`HG-MTH-011` states A2 minimality at candidate grade: under the adopted path-beta convention, the minimal admissible closed connected subgroup of `SU(3)` on the C-7 candidate list is `U(2)=S(U(2) x U(1))`. P3 asks how that result attaches to Heller-Godel's proof-character pipeline at `p=3`.

The goal of this scope note is not to prove the integration. The goal is to define what must be exhibited in a later closure PR before A2 minimality can be promoted through P3.

## Inputs

The scope depends on these already-merged inputs:

| Input | Role | Commit / source |
| --- | --- | --- |
| `HG-MTH-011` | A2 minimality candidate-theorem | PR #77, merge SHA `bf3bf77cba9d8cb56d8379a3f7379d7357f70692` |
| C-7 closure tranche 1 | subgroup eliminations | PR #73, merge SHA `c25dd3b5451fc73e3a3705fe8c272ce185454244` |
| C-7 closure tranche 2 | `U(2)` / `SU(3)` minimality verdict | PR #74, merge SHA `98e2ceac5646c02b3efd7a8ed48c0ec43ab7f8f6` |
| C-8 closure | `Omega` primacy and orientation inheritance | PR #75, merge SHA `e940da419474e987b87755d386f196fa34ed580f` |
| Heller-Einstein typed-interface ontology | optional mediation surface only | `SocioProphet/Heller-Einstein`, v0.1 / v1.7 source-derived surface |

## P3 obligation statement

P3 is satisfied only if a later closure PR constructs a typed attachment from:

```text
A2 gate-minimality result:
U(2)=S(U(2) x U(1)) minimal admissible subgroup under path-beta
```

to at least one proof-character pipeline object at `p=3`:

```text
chi_3 phase reduction
zeta_3 carry defect under composition
```

The attachment must preserve grade discipline. It may upgrade `HG-MTH-011` through P3 only if the attachment is explicit, typed, and testable within Heller-Godel's proof-character framework.

## Candidate attachment forms

A later P3 closure PR may choose one or more of the following attachment forms.

### A. Phase-reduction attachment

Construct a map from the A2 minimal admissible subgroup package to a `chi_3` phase object.

The closure must specify:

1. the source object: `U(2)=S(U(2) x U(1))` inside `SU(3)` under strict `3`-orientation;
2. the target object: a `chi_3` phase datum already present in, or added to, the proof-character pipeline;
3. the invariant preserved by the attachment;
4. what information is lost in the reduction;
5. the test or finite arithmetic check that verifies the attachment.

### B. Carry-defect attachment

Construct a map from the A2 minimal admissible subgroup package to a `zeta_3` carry-defect object under composition.

The closure must specify:

1. the source composition law or subgroup action being reduced;
2. the residue or phase representatives used at `p=3`;
3. the precise carry-defect expression;
4. why the defect is a proof-character object and not merely group-theoretic notation;
5. the executable or symbolic regression that prevents conflating carry defect with the finite monodromy character.

### C. Typed-interface mediation through Heller-Einstein

Use Heller-Einstein only as a typed mediation layer, not as an independent proof source.

A typed HE-mediated attachment must name:

1. what HG object is being exposed through the interface;
2. what trace, projection, or semantic lift is being used;
3. what is preserved;
4. what is projected away;
5. what remains deferred;
6. why the interface does not promote HE material into HG theorem content by prose.

The relevant HE vocabulary is the typed access chain, trace map, semantic lift, reconstruction map, latent fiber, semantic equivalence, sufficiency hierarchy, and semantic right-inverse criterion. The relocated realization question may be used only to formulate the interface obligation; it does not by itself close P3.

## Minimal closure conditions

A P3 closure PR must include all of the following:

1. A formal source object: the `HG-MTH-011` A2 minimal admissible subgroup package.
2. A formal target object: either `chi_3`, `zeta_3`, or both.
3. A typed attachment relation from source to target.
4. A proof sketch explaining why the attachment is intrinsic to the path-beta A2 package and not an arbitrary analogy.
5. A grade declaration explaining whether P3 is fully closed or only partially closed.
6. At least one regression target if the attachment reduces to finite arithmetic.
7. Explicit non-claims preserving the limits of HG, HE, and downstream Clay consumers.

## Out of scope for this P3 scope note

This scope note does not:

1. close P3;
2. promote `HG-MTH-011` to theorem-track;
3. prove path-beta uniqueness or P1;
4. prove candidate-list exhaustion or P2;
5. create a theorem about `A_n` for `n >= 3`;
6. start Heller-Einstein development;
7. authorize Heller-Einstein to cite A2 minimality as theorem-grade input;
8. transfer this result into `SocioProphet/yang-mills`;
9. change the status of Lane VIII residue work.

## HE boundary

Heller-Einstein may be relevant to P3 because its typed-interface ontology asks how latent structure, traces, semantic lift, reconstruction, and projection-induced stochasticity relate. That is close to the P3 problem: attach an algebraic gate-minimality result to a proof-character pipeline object without collapsing distinct layers.

However, HE is not imported as theorem content here. In any closure PR, HE citations must state the typed interface used and the grade of the HE object cited. HE cannot serve as a prose bridge that turns candidate-grade A2 minimality into theorem-grade HG content.

## Expected next closure artifact

The expected next artifact, if this scope is accepted, is a P3 closure PR with one of these names:

```text
docs/gate-minimality/p3-a2-chi3-attachment.md
docs/gate-minimality/p3-a2-zeta3-attachment.md
docs/gate-minimality/p3-a2-proof-character-attachment.md
```

That later closure PR should choose the least ambiguous target first. If both `chi_3` and `zeta_3` are needed, the closure should state the dependency order rather than merging them by analogy.

## Review checklist for P3 closure

Before a future P3 closure PR can promote `HG-MTH-011`, reviewers must verify:

1. the attachment is typed;
2. the source and target objects are explicitly named;
3. the target is actually a proof-character pipeline object;
4. no HE object is grade-inflated;
5. no downstream Clay consumer imports the result before promotion;
6. finite arithmetic claims have tests;
7. non-claims are preserved.
