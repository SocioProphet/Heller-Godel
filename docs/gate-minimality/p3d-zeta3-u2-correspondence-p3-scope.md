# HG-MTH-019 — P3.d zeta_3 Carry Defect and U(2) Correspondence at p=3 Scope

Identifier: `HG-MTH-019`  
Status: scope document for P3.d under `HG-MTH-012`.  
Owner: `SocioProphet/Heller-Godel`.  
Track: P3.d after P3.a closure `HG-MTH-014`, P3.b closure `HG-MTH-016`, and P3.c closure `HG-MTH-018`.  
Claim level: method-grade as scope.

## 1. Statement of obligation

P3.d is the `zeta_3` carry defect and `U(2)` correspondence obligation at `p=3`.

It specifies the construction obligation for the mod-3 carry defect:

```text
zeta_3
```

under composition in the sense of candidate-`HG-FND-007`:

```text
Lifted phase index and section-defect carry cocycle
```

and the correspondence obligation between `zeta_3` and the minimal admissible subgroup from `HG-MTH-011`:

```text
U(2)=S(U(2) x U(1)) subset SU(3).
```

The correspondence is scoped in the sense of candidate-`HG-FND-006`:

```text
Finite monodromy / deck-character interpretation
```

Closure of P3.d, together with the already-merged P3.a, P3.b, and P3.c closures, assembles the full P3 pipeline integration path for `HG-MTH-011`.

This document is the scope of P3.d, not its closure.

## 2. HG-FND-006 and HG-FND-007 attachment surfaces

The current framework-core registry defines:

```text
HG-FND-006 — Finite monodromy / deck-character interpretation
```

with status:

```text
candidate; active core exists, registry normalization pending
```

The current framework-core registry defines:

```text
HG-FND-007 — Lifted phase index and section-defect carry cocycle
```

with status:

```text
candidate; active core exists, registry normalization pending
```

P3.d closure must verify against both candidate surfaces.

Load-bearing distinction:

1. `HG-FND-006` is the deck-character / monodromy interpretation surface.
2. `HG-FND-007` is the lifted phase-index and carry-cocycle surface.
3. P3.d.1, the `zeta_3` construction, attaches primarily to `HG-FND-007`.
4. P3.d.2, the `U(2)` correspondence, attaches primarily to `HG-FND-006`.

Neither surface is normalized by this scope PR.

## 3. A1 paradigm at p=2

The manuscript defines finite phase maps by selecting a rational exponent channel `beta` and setting:

```text
k_p(beta)=floor(p beta) mod p
chi_p^(rho,beta)(T)=exp(2 pi i k_p(beta)/p) in mu_p.
```

It defines the carry defect by:

```text
zeta_p(alpha,beta)=floor(p(alpha+beta))-floor(p alpha)-floor(p beta) mod p.
```

and records:

```text
chi_p(alpha+beta)=chi_p(alpha)chi_p(beta)exp(2 pi i zeta_p(alpha,beta)/p).
```

The manuscript further states that `zeta_p` is a finite-resolution section defect, equivalently a coboundary under ordinary cochain freedom. It is computationally meaningful, but it does not by itself establish a nonabelian extension, a nonsplit central extension, or a nontrivial cohomology class.

At A1, P3.c retroactively sharpened the character side: `chi_2=-1` is compatible with local square-root monodromy, finite phase reduction, and two-sheet global monodromy because all land in `mu_2`.

For P3.d scope, the A1 / A2 distinction is structural:

1. At A1, the `zeta_2` lift is expected to live in the same group as the minimal admissible subgroup, conventionally the spin double-cover setting `Spin(3) ~= SU(2)` for the A1 path.
2. At A2, `zeta_3` is not automatically a topological triple-cover lift of `SU(3)`. P3.c located the `mu_3` source in the Galois / sheet-rotation structure of the cubic algebraic curve.
3. Therefore the A2 `zeta_3` home must be constructed. The leading candidates place it in `U(2)`, in the `SU(3)` center, or in the abstract Galois sheet-rotation group before representation into `U(2)`.
4. At A2, `U(2)` is a proper subgroup of `SU(3)`, so the relation between the carry defect and the minimal admissible subgroup is nontrivial.

P3.d closure must not assume that the A1 lift pattern transfers unchanged to A2.

## 4. Requirements on zeta_3 and the U(2) correspondence

### R1 — zeta_3 as element of a definite group

P3.d closure must specify what kind of object `zeta_3` is.

At `p=2`, the expected paradigm has `zeta_2` as an element of a definite group, not merely a formal symbol. At `p=3`, `zeta_3` must likewise be placed in an explicitly identified group.

### R2 — zeta_3 as lift of chi_3

P3.c closure identified:

```text
chi_3(tau)=omega,
tau=(123),
omega=exp(2 pi i / 3),
```

under the positive sheet-generator convention.

P3.d closure must specify a natural map from the group hosting `zeta_3` to `mu_3`, and must verify that `zeta_3` maps to `omega` under that map.

### R3 — Carry-cocycle compatibility

The manuscript and `phase_characters.py` define carry in terms of finite phase-section arithmetic.

The code surface includes:

```text
section(residue: int, level: int) -> int
carry(residue_left: int, residue_right: int, level: int) -> int
carry_table(level: int) -> tuple[tuple[int, ...], ...]
carry_cocycle_identity_holds(a: int, b: int, c: int, level: int) -> bool
```

P3.d closure must verify that the composition law in the proof-character pipeline lifts consistently to the group hosting `zeta_3`.

### R4 — U(2) correspondence via HG-FND-006

P3.d closure must demonstrate that `zeta_3` corresponds to:

```text
U(2)=S(U(2) x U(1)) subset SU(3)
```

being the minimal admissible subgroup from `HG-MTH-011`, in the sense of candidate-`HG-FND-006`.

The correspondence should relate:

1. the group hosting `zeta_3` and its phase/deck-character action; and
2. the embedding of `U(2)` into `SU(3)` with the `Z/3`-fixed scalar surface and residual `SU(2)` block action.

### R5 — Cumulative grade-chain integration

P3.d closure, combined with P3.a/b/c closures, must assemble the full P3 obligation.

The full P3 route would put `HG-MTH-011` at method-grade modulo the six expected candidate Tier-1 surfaces:

```text
HG-FND-001
HG-FND-002
HG-FND-003
HG-VOC-006
HG-FND-006
HG-FND-007
```

This scope PR does not perform the full P3 assembly.

## 5. Candidate zeta_3 structures

This section records candidates for P3.d.1 closure. It does not select among them.

### Z1 — zeta_3 = omega * I_2 in U(2)

Candidate:

```text
zeta_3 = omega I_2 in U(2).
```

This lives in the scalar `U(1)` part of the center of `U(2)`. It makes the `U(2)` correspondence direct because `zeta_3` already lives in `U(2)`.

Caution: the determinant of `omega I_2` is `omega^2`, not `omega`. Closure must verify whether the natural character is determinant, an inverse/half-determinant convention, a block-complement character under the embedding into `S(U(2) x U(1))`, or another map.

### Z2 — zeta_3 = tau in A_3 subset S_3

Candidate:

```text
tau=(123) in A_3 subset S_3.
```

This is the Galois sheet-rotation generator from P3.c. It lives in the abstract monodromy group rather than in a Lie group.

Closure would need to provide a representation or character from the sheet-rotation group into `U(2)` or into a subgroup associated with `U(2)`.

### Z3 — zeta_3 in the center of SU(3)

Candidate:

```text
zeta_3 = omega I_3 in Z(SU(3)) ~= mu_3.
```

This places `zeta_3` in `SU(3)` directly. The `U(2)` correspondence would then have to be expressed through the embedding of `U(2)=S(U(2) x U(1))` into `SU(3)` and the way the center acts on the active sector.

### Z4 — zeta_3 in a triple cover

Candidate:

```text
zeta_3 lives in a triple cover of a relevant quotient.
```

At A1, the lift paradigm uses the spin double cover. At A2, `SU(3)` is simply connected, so there is no analogous nontrivial topological triple cover of `SU(3)` itself. P3.c located the triple structure in the Galois cover rather than a topological cover of `SU(3)`.

Z4 is therefore likely rejected unless closure identifies a precise non-topological or quotient-cover structure.

## 6. Candidate U(2) correspondence strategies

This section records candidates for P3.d.2 closure. It does not select among them.

### C1 — Embedding-based correspondence

Identify `zeta_3` with an element of `U(2)`, likely through Z1 or an equivalent construction, and use the standard embedding:

```text
U(2)=S(U(2) x U(1)) subset SU(3)
```

as the correspondence.

Strength: direct.  
Weakness: requires closure to prove the selected `zeta_3` naturally lives in `U(2)` and maps to `omega` under the correct character.

### C2 — Action-based correspondence

Treat `zeta_3` as acting on a vector space or module and identify `U(2)` as the stabilizer, centralizer, or minimal admissible subgroup compatible with that action.

Strength: representation-theoretic.  
Weakness: requires explicit action construction and verification that `U(2)`, not a larger or smaller subgroup, is the relevant object.

### C3 — Deck-character correspondence via HG-FND-006

Treat the `zeta_3 -> U(2)` relation as a deck-character map from the finite monodromy structure to the gauge-side active-sector structure.

Strength: closest to candidate-`HG-FND-006`.  
Weakness: `HG-FND-006` remains candidate and is not normalized; closure must be explicit about the grade ceiling.

P3.d closure may select one strategy or a hybrid.

## 7. Heller-Einstein mediation route

Pure Heller-Godel closure remains the default.

If P3.d.2 cannot close the `zeta_3` / `U(2)` correspondence using the current candidate-`HG-FND-006` and candidate-`HG-FND-007` surfaces, the realization question may route through Heller-Einstein typed-interface ontology.

That route could formalize `zeta_3 -> U(2)` as a typed morphism. It would require separate authorization. This scope PR does not authorize Heller-Einstein development.

## 8. Grade declarations

| Object | Grade | Source |
| --- | --- | --- |
| `HG-FND-006` | candidate; registry normalization pending | `docs/framework-core/distance-classification.md` |
| `HG-FND-007` | candidate; registry normalization pending | `docs/framework-core/distance-classification.md` |
| `HG-MTH-018` (P3.c closure) | method-grade modulo candidate-`HG-FND-003` and candidate-`HG-VOC-006` | PR #90 |
| `HG-MTH-019` (P3.d scope, this PR) | method-grade as scope | this PR |
| P3.d closure (future) | would be method-grade modulo candidate-`HG-FND-006` and candidate-`HG-FND-007` | not in this PR |
| Full P3 closure (future) | would be method-grade modulo six candidate Tier-1 surfaces | not in this PR |
| `HG-MTH-011` promotion (future) | requires the relevant Tier-1 normalizations or discharge route | not in this PR |

Cumulative-modulo accounting:

```text
HG-FND-001
HG-FND-002
HG-FND-003
HG-VOC-006
HG-FND-006
HG-FND-007
```

With P3.d scoped, all six expected Tier-1 candidate dependencies are explicit. Promotion of `HG-MTH-011` to theorem-grade requires these candidate surfaces to normalize or otherwise discharge under an authorized promotion route.

## 9. Non-claims

1. Does not close P3.d. Scope only.
2. Does not select among `zeta_3` candidates Z1, Z2, Z3, and Z4.
3. Does not select among `U(2)` correspondence strategies C1, C2, and C3.
4. Does not specify the natural character from the selected `zeta_3` host to `mu_3`; determinant, inverse determinant, block-complement character, or another map remains closure work.
5. Does not assemble the full P3 closure document.
6. Does not promote `HG-MTH-011`.
7. Does not promote any candidate `HG-FND-*` or `HG-VOC-006` surface from candidate.
8. Does not extend to `A_n` for `n >= 3`.
9. Does not authorize Heller-Einstein PRs beyond already merged authorization paths.
10. Does not cross into downstream Clay-program proof claims, including `SocioProphet/yang-mills`.
11. Does not retroactively promote A1 `zeta_2` source identification.
12. Does not normalize `HG-FND-006` or `HG-FND-007`.

## 10. Future closure pathway

After P3.d scope merges, P3.d closure selects a `zeta_3` candidate and a `U(2)` correspondence strategy, verifies R1-R5, and emits the closure document.

P3.d closure unlocks the full P3 closure document, expected to assign `HG-MTH-020`, which assembles all four sub-obligation closures and lifts `HG-MTH-011` by the cumulative-modulo grade chain.

P3.d closure and full P3 closure are not opened by this scope PR.

## 11. Identifier and registry

This document assigns:

```text
HG-MTH-019
```

to the P3.d `zeta_3` carry defect and `U(2)` correspondence scope at `p=3`.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. This PR updates that registry to register `HG-MTH-019` and record its grade ceiling as method-grade as scope.
