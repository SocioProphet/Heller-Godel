# HG-MTH-020 — P3.d zeta_3 Carry Defect and U(2) Correspondence at p=3 Closure

Identifier: `HG-MTH-020`  
Status: closure document for P3.d; scoped by `HG-MTH-019`.  
Owner: `SocioProphet/Heller-Godel`.  
Track: P3.d under `HG-MTH-012`, after P3.a closure `HG-MTH-014`, P3.b closure `HG-MTH-016`, and P3.c closure `HG-MTH-018`.  
Claim level: method-grade modulo candidate-`HG-FND-006` and candidate-`HG-FND-007`.

## 1. Type table

P3.d uses several distinct typed objects. This table is load-bearing and prevents conflating the scalar carry cocycle with its group-valued lift, the character, the embedding, or the A2 minimality target.

| Symbol | Type | Description |
| --- | --- | --- |
| `zeta_3(alpha,beta)` | `Q x Q -> Z/3` | Scalar-valued carry cocycle on selected Puiseux exponent channels. |
| `sigma_3(alpha)` / `q_3(alpha)` | `Q -> Z/3` | Finite section map `floor(3 alpha) mod 3`; manuscript notation uses `q_p`. |
| `Z_3` | element of `SU(3)` and of embedded `U(2)=S(U(2) x U(1))` | Group-valued lift / realization of the scalar carry correction selected by this closure. |
| `kappa: U(2) -> mu_3` | character on the finite `mu_3` complement surface | U(1)-complement character selecting the trailing complement entry of `S(U(2) x U(1))`. |
| `iota: U(2) -> SU(3)` | embedding | Standard block embedding `A -> diag(A, det(A)^(-1))`. |
| `U(2)=S(U(2) x U(1))` | closed connected subgroup of `SU(3)` | Minimal admissible subgroup from `HG-MTH-011`. |

The selected group-valued lift is denoted `Z_3`; the manuscript scalar cocycle remains `zeta_3(alpha,beta)`.

## 2. Statement of closure

P3.d closure verifies R1-R5 from `HG-MTH-019`.

Closure selects candidate Z3 from the P3.d scope:

```text
Z_3 = omega I_3 in Z(SU(3)) ~= mu_3,
omega = exp(2 pi i / 3).
```

Equivalently, under the standard embedding:

```text
U(2)=S(U(2) x U(1)) subset SU(3),
A |-> diag(A, det(A)^(-1)),
```

this element is represented by:

```text
A = omega I_2,
det(A)=omega^2,
det(A)^(-1)=omega,
diag(A, det(A)^(-1))=diag(omega, omega, omega)=omega I_3.
```

Closure selects the U(1)-complement character:

```text
kappa(diag(A, lambda)) = lambda
```

on the finite `mu_3` complement surface. For the selected lift:

```text
kappa(Z_3)=omega,
```

matching `chi_3=omega` from `HG-MTH-018`.

This resolves the determinant subtlety recorded in `HG-MTH-019`: the determinant of the `U(2)` block is `omega^2`, not `omega`, so the relevant character is not the raw determinant of the `2 x 2` block. It is the complement projection in the `S(U(2) x U(1))` decomposition.

The closure grade is method-grade modulo candidate-`HG-FND-006` and candidate-`HG-FND-007`.

## 3. Source surfaces and inspection findings

### 3.1 Manuscript zeta_p cocycle

The manuscript defines the carry defect:

```text
zeta_p(alpha,beta)=floor(p(alpha+beta))-floor(p alpha)-floor(p beta) mod p.
```

It records the multiplicativity-defect identity:

```text
chi_p(alpha+beta)=chi_p(alpha)chi_p(beta)exp(2 pi i zeta_p(alpha,beta)/p).
```

It records the cocycle identity:

```text
zeta_p(alpha,beta)+zeta_p(alpha+beta,gamma)
= zeta_p(beta,gamma)+zeta_p(alpha,beta+gamma) mod p.
```

It also records the coboundary form:

```text
q_p(alpha)=floor(p alpha) mod p,
zeta_p(alpha,beta)=q_p(alpha+beta)-q_p(alpha)-q_p(beta).
```

Therefore `zeta_p` is a finite-resolution section defect and a coboundary under ordinary cochain freedom. In cochain notation:

```text
zeta_p = delta q_p.
```

The cocycle identity follows automatically from the coboundary relation, because the coboundary of a coboundary is zero:

```text
delta zeta_p = delta(delta q_p)=0.
```

This closure does not treat `zeta_3` as a nontrivial cohomology class.

### 3.2 phase_characters.py carry table at p=3

The code surface defines:

```text
section(residue, level)=residue mod level
carry(a,b,level)=(section(a,level)+section(b,level)-section(a+b,level))/level
carry_table(level)=((carry(row,col,level))...)
```

For `level=3`, the normalized carry table is:

```text
carry_table(3)=
row 0: (0, 0, 0)
row 1: (0, 0, 1)
row 2: (0, 1, 1)
```

Equivalently:

```text
((0,0,0),(0,0,1),(0,1,1)).
```

For residues `a,b in {0,1,2}`, this table is exactly the addition-carry cocycle for the canonical section `Z/3 -> {0,1,2}`:

```text
carry(a,b,3)=1 if a+b >= 3,
carry(a,b,3)=0 if a+b < 3.
```

Thus the nonzero carries occur exactly when representatives in `{0,1,2}` cross the mod-3 section boundary. This is the residue-level implementation of the manuscript formula for `zeta_3(alpha,beta)` after applying the finite section map `q_3`.

### 3.3 HG-FND-006 and HG-FND-007 surfaces

Current registry surfaces:

```text
HG-FND-006 — Finite monodromy / deck-character interpretation
candidate; active core exists, registry normalization pending
```

```text
HG-FND-007 — Lifted phase index and section-defect carry cocycle
candidate; active core exists, registry normalization pending
```

Repository inspection did not surface a more detailed manuscript passage for `HG-FND-006` deck-character interpretation beyond the candidate registry surface. This closure therefore treats the `HG-FND-006` correspondence as method-grade and candidate-limited.

## 4. Z_3 lift candidate selection

P3.d scope `HG-MTH-019` recorded four candidate lift structures:

1. Z1: `omega I_2 in U(2)`.
2. Z2: `tau=(123) in A_3 subset S_3`.
3. Z3: `omega I_3 in Z(SU(3)) ~= mu_3`.
4. Z4: triple-cover candidate.

This closure selects Z3:

```text
Z_3 = omega I_3 in Z(SU(3)).
```

Justification:

1. `Z(SU(3)) ~= mu_3`, so `omega I_3` is a canonical `mu_3` element inside the A2 gauge group.
2. `omega I_3` preserves the cubic invariant `Omega` because scalar multiplication by `omega` on each basis vector multiplies `Omega` by `omega^3=1`.
3. Under the standard embedding `U(2)=S(U(2) x U(1)) subset SU(3)`, the same element lies in the embedded `U(2)`:

```text
A=omega I_2,
det(A)=omega^2,
det(A)^(-1)=omega,
diag(A,det(A)^(-1))=omega I_3.
```

4. The U(1)-complement projection reads the trailing entry `omega`, matching the manuscript-selected and P3.c-identified value `chi_3=omega`.
5. Z4 is rejected for this closure because `SU(3)` is simply connected; the triple structure supplied by P3.c is Galois / sheet-rotation, not a nontrivial topological triple cover of `SU(3)`.
6. Z2 remains the analytic monodromy source from P3.c, but by itself lives in the abstract Galois group and would require an additional representation into the gauge side.
7. Z1 is essentially the `U(2)` block component of Z3, but raw block determinant gives `omega^2`; Z3 plus complement projection records the full `S(U(2) x U(1))` geometry and avoids misidentifying the determinant character.

## 5. R1 — Z_3 as element of a definite group

R1 is verified.

The scalar carry cocycle is:

```text
zeta_3(alpha,beta): Q x Q -> Z/3.
```

The selected group-valued lift is:

```text
Z_3 = omega I_3.
```

It lies in:

```text
Z(SU(3)) ~= mu_3 subset SU(3).
```

It also lies in the standard embedded subgroup:

```text
U(2)=S(U(2) x U(1)) subset SU(3),
```

because:

```text
omega I_3 = diag(omega I_2, omega)
          = diag(A, det(A)^(-1)), A=omega I_2.
```

Thus the lift host is definite: `G` may be read as `Z(SU(3))` for the central lift, or as the finite central `mu_3` surface inside embedded `U(2)` for the correspondence.

## 6. R2 — Z_3 as lift of chi_3

R2 is verified.

P3.c closure `HG-MTH-018` identified:

```text
chi_3(tau)=omega,
tau=(123),
omega=exp(2 pi i / 3),
```

under the positive cyclic sheet-generator convention.

For P3.d, define the finite complement character on the selected finite surface by:

```text
kappa(diag(A,lambda)) = lambda,
```

restricted to the `mu_3` subgroup represented by:

```text
diag(omega^r I_2, omega^r), r in Z/3.
```

For the selected lift:

```text
Z_3=omega I_3=diag(omega I_2, omega),
```

we have:

```text
kappa(Z_3)=omega.
```

This matches the `HG-MTH-018` primitive value `chi_3=omega`.

The raw determinant of the `2 x 2` block is explicitly rejected as the selected `mu_3` character:

```text
det(omega I_2)=omega^2.
```

It gives the conjugate primitive element, not the manuscript-selected `omega` under the positive-orientation convention. The selected character is the U(1)-complement projection in the `S(U(2) x U(1))` decomposition, not the block determinant.

## 7. R3 — carry-cocycle compatibility

R3 is verified at method-grade modulo candidate-`HG-FND-007`.

The manuscript identity says:

```text
chi_3(alpha+beta)
= chi_3(alpha) chi_3(beta) exp(2 pi i zeta_3(alpha,beta)/3).
```

The code-level carry table at level 3 records the section-defect values:

```text
((0,0,0),(0,0,1),(0,1,1)).
```

For residues `a,b in {0,1,2}`, these are the explicit composition adjustments:

```text
zeta_3(a,b)=0 for (a,b)=(0,0),(0,1),(0,2),(1,0),(1,1),(2,0),
zeta_3(a,b)=1 for (a,b)=(1,2),(2,1),(2,2).
```

Equivalently:

```text
zeta_3(a,b)=1 if a+b >= 3,
zeta_3(a,b)=0 if a+b < 3.
```

The group-valued lift sends a carry value `c in Z/3` to:

```text
c |-> Z_3^c = (omega I_3)^c.
```

Thus the table realizes the composition adjustments explicitly as:

```text
0 |-> Z_3^0 = I_3,
1 |-> Z_3^1 = omega I_3.
```

Applying the complement character gives:

```text
kappa(Z_3^c)=omega^c=exp(2 pi i c/3).
```

Therefore the selected lift reproduces exactly the scalar correction factor in the manuscript multiplicativity-defect identity:

```text
exp(2 pi i zeta_3(a,b)/3)=kappa(Z_3^zeta_3(a,b)).
```

The cocycle identity recorded in the manuscript corresponds to associativity of multiplication of the lift factors:

```text
Z_3^zeta(alpha,beta) Z_3^zeta(alpha+beta,gamma)
= Z_3^zeta(beta,gamma) Z_3^zeta(alpha,beta+gamma),
```

because `zeta_p=delta q_p`, so `delta zeta_p=0`, and because powers of the central element `Z_3` commute.

This is not a claim that `zeta_3` is a nontrivial cohomology class. It is a claim that the explicit section-defect cochain is realized by powers of the selected central lift.

## 8. R4 — U(2) correspondence via HG-FND-006

R4 is verified at method-grade modulo candidate-`HG-FND-006`.

The correspondence strategy selected is a hybrid of C1 and C3:

1. C1, embedding-based: `Z_3=omega I_3` lies in the standard embedded `U(2)=S(U(2) x U(1))`.
2. C3, deck-character disciplined: the finite correction factor is interpreted through the character `kappa` on the finite complement surface, not as an untyped cohomology class.

Because `HG-FND-006` is only recorded as:

```text
Finite monodromy / deck-character interpretation
candidate; active core exists, registry normalization pending
```

this closure uses `deck-character interpretation` as the name of the intended candidate surface, not as an independently normalized covering-theory construction. The precise deck-character formalization remains deferred to `HG-FND-006` normalization.

The bounded correspondence is:

```text
zeta_3(alpha,beta)
-> Z_3^zeta_3(alpha,beta)
-> kappa(Z_3^zeta_3(alpha,beta))=omega^zeta_3(alpha,beta).
```

On the gauge side, `Z_3` acts on the fundamental `C^3` by scalar multiplication by `omega`. It preserves the A2 cubic invariant `Omega` because:

```text
Omega(omega v1, omega v2, omega v3)=omega^3 Omega(v1,v2,v3)=Omega(v1,v2,v3).
```

`HG-MTH-011` states that under path-beta for A2, the minimal admissible closed connected subgroup of `SU(3)` is:

```text
U(2)=S(U(2) x U(1)).
```

Since `Z_3` lies in this embedded `U(2)`, and since the complement projection supplies the `mu_3` character matching `chi_3=omega`, the scalar carry defect corresponds, at method-grade modulo candidate-`HG-FND-006`, to the finite central/complement surface of the minimal admissible subgroup.

Thus the carry defect under composition is realized as multiplication by powers of `Z_3` in the finite `mu_3` surface contained in the embedded `U(2)`, with the U(1)-complement projection reading out the required `mu_3` phase.

This closure does not claim that `Z_3` has been constructed as a deck transformation of a specific normalized cover, and it does not claim that `HG-FND-006` is settled. Because `HG-FND-006` remains unnormalized, this correspondence is not promoted beyond method-grade modulo candidate-`HG-FND-006`.

## 9. R5 — cumulative grade-chain integration

R5 is verified as P3.d closure.

| Sub-obligation | Closure | Modulo Tier-1 surface |
| --- | --- | --- |
| P3.a | `HG-MTH-014` | `HG-FND-001` |
| P3.b | `HG-MTH-016` | `HG-FND-002` |
| P3.c Puiseux | `HG-MTH-018` | `HG-FND-003` |
| P3.c character | `HG-MTH-018` | `HG-VOC-006` |
| P3.d cocycle | `HG-MTH-020` | `HG-FND-007` |
| P3.d correspondence | `HG-MTH-020` | `HG-FND-006` |

After this closure, all four P3 sub-obligations are closed individually. The full P3 closure assembly remains a separate PR. That assembly PR should cite `HG-MTH-014`, `HG-MTH-016`, `HG-MTH-018`, and `HG-MTH-020` and state the cumulative-modulo grade chain for `HG-MTH-011`.

This PR does not itself assemble full P3 and does not promote `HG-MTH-011`.

## 10. Heller-Einstein mediation status

This is pure Heller-Godel closure.

No Heller-Einstein typed-interface ontology, `HE-INT-*`, or realization-question machinery is used. The selected lift and correspondence are stated inside the current Heller-Godel candidate-grade surfaces.

## 11. Grade declarations

| Object | Grade |
| --- | --- |
| `HG-FND-006` | candidate; registry normalization pending |
| `HG-FND-007` | candidate; registry normalization pending |
| `HG-MTH-019` (P3.d scope) | method-grade as scope |
| `HG-MTH-020` (P3.d closure, this PR) | method-grade modulo candidate-`HG-FND-006` and candidate-`HG-FND-007` |

After this PR, full P3 closure assembly is unlocked as a separate PR. `HG-MTH-011` promotion remains a separate act and remains bounded by the six candidate Tier-1 surfaces unless those surfaces are normalized or otherwise discharged by an authorized route.

## 12. Non-claims

1. Does not claim `zeta_3` represents a nontrivial cohomology class. Per the manuscript, `zeta_p` is a coboundary of `q_p` under ordinary cochain freedom.
2. Does not assemble the full P3 closure document.
3. Does not promote `HG-MTH-011` directly; the cumulative-modulo lift belongs to the assembly PR.
4. Does not normalize `HG-FND-006` or `HG-FND-007`.
5. Does not retroactively promote A1 `zeta_2` source identification.
6. Does not extend to `A_n` for `n >= 3`.
7. Does not authorize Heller-Einstein PRs beyond already merged authorization paths.
8. Does not cross into downstream Clay-program proof claims, including `SocioProphet/yang-mills`.
9. Does not adopt the determinant character `det: U(2) -> U(1)` as the natural `mu_3` character for this closure. The selected character is the U(1)-complement projection in the `S(U(2) x U(1))` decomposition.
10. Does not claim that the `HG-FND-006` deck-character surface is normalized.
11. Does not claim that `Z_3` is a topological triple-cover lift of `SU(3)`.
12. Does not identify the scalar cocycle `zeta_3(alpha,beta)` with the group element `Z_3`; it only realizes the scalar carry values by powers of `Z_3`.
13. Does not claim that `Z_3` is a deck transformation of a specific normalized cover; the deck-character language remains bounded by candidate-`HG-FND-006`.

## 13. Identifier and registry

This document assigns:

```text
HG-MTH-020
```

to the P3.d `zeta_3` carry defect and `U(2)` correspondence closure at `p=3`.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. This PR updates that registry to register `HG-MTH-020` and record its grade ceiling as method-grade modulo candidate-`HG-FND-006` and candidate-`HG-FND-007`.
