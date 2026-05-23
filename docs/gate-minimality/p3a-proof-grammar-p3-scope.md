# HG-MTH-013 — P3.a Proof Grammar at p=3 Scope

Identifier: `HG-MTH-013`  
Status: scope document; obligation not closed.  
Owner: `SocioProphet/Heller-Godel`.  
Track: P3.a under `HG-MTH-012`, A2 gate-minimality, `HG-MTH-011`, proof-character pipeline at `p=3`.  
Claim level: method-grade as obligation specification; not theorem-grade.

## 1. Statement of obligation

P3.a is the first of four sub-obligations under P3 (`HG-MTH-012`, pipeline integration scope).

P3.a — Restricted Proof Grammar at `p=3`. Specify a restricted proof grammar with fixed canonical statistic at `p=3`, consistent with `HG-FND-001` (restricted proof grammar and canonical statistic), such that the grammar's proof-class generating function (per P3.b, attaching to `HG-FND-002`) admits Puiseux singularity data (per P3.c, attaching to `HG-FND-003`) compatible with a finite phase reduction `chi_3` in `mu_3`, and the mod-3 carry defect `zeta_3` under composition (per P3.d, attaching to `HG-FND-007`) corresponds to the `U(2)=S(U(2) x U(1))` minimal admissible subgroup result of `HG-MTH-011`.

This document is the scope of P3.a, not its closure. Closure requires constructing the grammar and verifying its compatibility with the downstream P3.b / P3.c / P3.d obligations.

## 2. HG-FND-001 attachment surface

`docs/framework-core/distance-classification.md` records the current `HG-FND-001` candidate inventory entry as:

```text
| `HG-FND-001` | Restricted proof grammar and canonical statistic | candidate; active core exists, registry normalization pending |
```

The operative manuscript-level definition appears in `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 2:

```text
Let F be a fixed proof fragment. For this revision, the intended default is a simply typed lambda-calculus / implicational propositional fragment where normal inhabitants can be represented by alpha-classes of eta-long beta-normal de Bruijn lambda terms.

A stronger version of the paper should define F completely. Until then, all examples that do not specify a fixed type grammar are analytic calibration examples rather than theorem-bearing proof-class examples.

Let sigma: N_phi -> Z_{>= 0} be a statistic on alpha-classes of canonical normal forms. The construction is statistic-relative. When the statistic is left implicit, this manuscript uses sigma_C, the canonical constructor statistic.

This revision recommends:

sigma_C(s)=#lambda-nodes + #application-nodes + #variable-leaves.

If a different convention is used, the convention must be explicitly stated and examples recomputed.
```

P3.a attaches to `HG-FND-001` by specifying a `p=3` instantiation of this restricted proof grammar and canonical-statistic framework. The instantiation is parallel to the A1 fixture's `p=2` instance, but tuned for the path-beta / `SU(3)` / cubic-invariant active sector inherited from `HG-MTH-011`.

## 3. The A1 paradigm at p=2

The existing A1 / Catalan paradigm is documented at manuscript level and appendix level.

In `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 3.2 records the Catalan grammar:

```text
C(x)=1+xC(x)^2=(1 - sqrt(1-4x))/(2x)

C_A=(A -> A -> A) -> A -> A

T ::= x | b(T,T)

where x:A and b:A -> A -> A.
```

The manuscript states that this can ground the Catalan generating function proof-theoretically, but also records the caveat that a final manuscript must either include this grounding or label the Catalan example as analytic calibration only.

`docs/appendices/appendix_a_chain_catalan_witness.md` supplies the closed A1 witness context. It records the Catalan finite analytic witness, the `mu_2` monodromy character, the A1 spin-gate witness, and the Catalan encoding datum. In particular, Appendix A.5 records the proof-family active set as the rooted binary-tree grammar, and Theorem A.4 records the Catalan A1 fixture checks under `A1-sauzin-normalization-v1`.

The executable arithmetic layer is not the proof grammar itself. `src/heller_godel/phase_characters.py` consumes finite arithmetic data derived downstream from the grammar and generating-function layer, especially rational local exponents and finite phase indices.

## 4. Requirements on the p=3 proof grammar

P3.a closure must verify four requirements.

### R1 — Restricted typing

The grammar must be restricted in the sense of `HG-FND-001`: only specified production rules generate well-typed witnesses.

The witness data must be compatible with the path-beta framework at A2:

```text
SU(3) gauge structure
Z/3 central element selection
cubic invariant Omega as condition (v)
```

### R2 — Fixed canonical statistic

The grammar must equip each generated witness with a canonical statistic: an integer or rational invariant whose generating function over the grammar's productions defines the proof-class / proof-family generating function specified by `HG-FND-002`.

At `p=2`, the Catalan coefficients are:

```text
C_n = binom(2n,n)/(n+1)
```

At `p=3`, candidate canonical statistics include Fuss-Catalan numbers, ternary-tree counts, or another structure to be determined in P3.a closure.

### R3 — Downstream compatibility with phase_characters.py

The grammar's witness data structure must be compatible with the executable finite-arithmetic layer after P3.b and P3.c derive the relevant generating-function and Puiseux-exponent data.

`src/heller_godel/phase_characters.py` expects downstream arithmetic inputs of the following forms:

1. rational local exponents accepted by `normalize_exponent(alpha)`;
2. one or more rational exponents accepted by `common_level(*alphas)`;
3. a rational exponent plus optional finite level accepted by `phase_index(alpha, level=None)`;
4. finite character indices and levels accepted by `multiply_indices(left, right, level)`, `p_primary_projection(index, level, prime)`, and `prime_reduction(index, level, prime)`;
5. finite residues and levels accepted by `section(residue, level)`, `carry(residue_left, residue_right, level)`, and `carry_table(level)`;
6. residue triples and a level accepted by `carry_cocycle_identity_holds(a, b, c, level)`.

For P3.a, this means the proof grammar need not directly emit `phase_characters.py` inputs. It must, however, be specified in a way that P3.b and P3.c can derive rational Puiseux exponent channels and finite phase data that are consumable by this module at `p=3`.

### R4 — Active-sector compatibility with HG-MTH-011

The grammar's witnesses must distinguish between active-sector data and non-active gauge data.

The active-sector data must correspond to the `U(2)=S(U(2) x U(1))` minimal admissible subgroup under path-beta. This distinction is the structural hook by which P3.d's eventual `zeta_3` / `U(2)` correspondence becomes constructible.

## 5. Candidate grammar structures

This section is not a specification. It records candidate starting points for P3.a closure. Each candidate is a starting hypothesis to be evaluated, not an adopted choice.

### Candidate G1: Ternary tree grammar

Productions generate rooted ternary trees with leaves labeled by `SU(3)` fundamental-representation vectors.

Candidate canonical statistic: number of internal nodes.

Candidate generating family: Fuss-Catalan / ternary-tree counts with appropriate scaling.

Strength: direct ternary analog of the Catalan binary-tree paradigm at A1.

Weakness: branching structure `3` may not be the right structural choice. The relevant trinity could be `Z/3`, `SU(3)`, or cubic degree, and those are not the same object.

### Candidate G2: SU(3) chain-witness grammar

Productions generate chain witnesses in `SU(3)`, analogous to the chain witness structure used in the A1 fixture, with witnesses typed by `Z/3` central element selection.

Candidate canonical statistic: chain length or a more refined chain-character invariant.

Strength: closer to the structural pattern of the A1 fixture if A1 chain witnesses are chosen as the paradigm.

Weakness: the A1 chain family is explicitly a null finite-character witness in Appendix A.1, so an A2 chain-witness grammar would require careful justification and cannot simply inherit nontrivial phase behavior.

### Candidate G3: Cubic-invariant witness grammar

Productions directly enumerate triples `(v1,v2,v3)` with `Omega`-preservation typing under an active-sector group action.

Candidate canonical statistic: an `Omega`-related invariant of the triple.

Strength: most directly bound to `HG-MTH-011` condition (v).

Weakness: the connection to Puiseux singularity data at `p=3` under P3.c is not obvious in this form.

P3.a closure work would evaluate these and other candidates, select one or a hybrid, and verify R1-R4 against the selection. This document does not select.

## 6. Heller-Einstein mediation route

P3.a closure may route through Heller-Einstein typed-interface ontology in either of two ways, consistent with the P3 scope (`HG-MTH-012`).

1. Type-declared production rules. The `p=3` grammar's production rules may be specified as typed morphisms in `HE-INT-*`, with witness data carrying explicit type signatures. This formalizes R1 at the HE-INT level.
2. Placeholder discipline for open structures. Aspects of the grammar that remain underdetermined during P3.a closure, such as the exact canonical statistic if multiple candidates remain viable, may be recorded as `HE-PLC-*` placeholder spaces, deferring their specification while preserving type discipline.

HE involvement remains a route, not a requirement. P3.a may also close purely within HG if the grammar specification is direct.

## 7. Grade declarations

| Object | Grade | Source |
| --- | --- | --- |
| `HG-MTH-011` (A2 minimality candidate-theorem) | method-grade as candidate | PR #77 |
| `HG-MTH-012` (P3 pipeline integration scope) | method-grade as scope | PR #78 |
| `HG-MTH-013` (this P3.a sub-obligation scope) | method-grade as scope | this PR |
| P3.a closure | would be method-grade per the constructed grammar | not in this PR |

Closure of P3.a does not itself promote `HG-MTH-011`. All four sub-obligations P3.a through P3.d must close to close P3, and P3 closure is what promotes `HG-MTH-011`.

## 8. Non-claims

1. Does not close P3.a. This is a scope document.
2. Does not select among candidate grammars G1, G2, G3, or any other.
3. Does not specify the canonical statistic, generating function, or Puiseux singularity at `p=3`. Those are downstream P3.b and P3.c obligations.
4. Does not specify `zeta_3` or its `U(2)` correspondence. That is P3.d.
5. Does not promote `HG-MTH-011` or P3 (`HG-MTH-012`) from their current grades.
6. Does not authorize any Heller-Einstein PR. HE mediation is named as available but its use requires separate authorization.
7. Does not extend to `A_n` for `n >= 3`.
8. Does not cross into `SocioProphet/yang-mills`. The proof-character pipeline is HG-internal.

## 9. Future closure pathway

After this scope PR merges, the natural next PR is P3.a closure: construct the grammar, selecting from candidate structures or a refinement, verify R1-R4, and emit the closure document with the constructed grammar specification.

P3.a closure unlocks P3.b authorization (canonical statistic and generating function), which unlocks P3.c (Puiseux singularity and `chi_3`), which unlocks P3.d (`zeta_3` and `U(2)` correspondence). The dependency chain is sequential per Section 8 of `HG-MTH-012`.

## 10. Identifier and registry

This document assigns:

```text
HG-MTH-013
```

to the P3.a restricted proof grammar at `p=3` scope obligation.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. It defines the `HG-{LAYER}-{NNN}` pattern and requires any PR adding an `HG-*` identifier to update the registry or `docs/framework-core/distance-classification.md` in the same PR. This PR therefore updates `docs/framework-core/claim-grammar.md` to register `HG-MTH-013`.
