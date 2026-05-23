# HG-MTH-017 — P3.c Puiseux Singularity and chi_3 at p=3 Scope

Identifier: `HG-MTH-017`  
Status: scope document for P3.c under `HG-MTH-012`.  
Owner: `SocioProphet/Heller-Godel`.  
Track: P3.c after P3.a closure `HG-MTH-014` and P3.b closure `HG-MTH-016`.  
Claim level: method-grade as scope.

## 1. Statement of obligation

P3.c is the Puiseux singularity and `chi_3` obligation at `p=3`.

It specifies the Puiseux singular datum of:

```text
C_3(x)=1+x C_3(x)^3
```

and the associated character question for `chi_3` at `p=3`, consistent with candidate-`HG-FND-003` and candidate-`HG-VOC-006`.

Specifically, P3.c closure must verify:

1. `C_3(x)` has a Puiseux singularity at:

```text
rho_3 = 4/27.
```

2. The local Puiseux exponent at this singularity is:

```text
alpha_3 = 1/2.
```

3. `C_3(x)` admits an explicit Puiseux expansion at `rho_3` of the form:

```text
C_3(x)=A + B(1 - x/rho_3)^(1/2) + C(1 - x/rho_3) + ...
```

for constants to be derived at closure.

4. The character `chi_3 in mu_3` expected by the framework must be sourced from the `p=3` algebraic-function / monodromy / finite-phase structure associated to the singularity datum. P3.c closure must determine whether `chi_3` arises from local singular monodromy, global sheet monodromy of the three-sheeted cubic curve, finite phase reduction through `HG-VOC-006`, or a composite of these. Closure must also preserve the explicit option that the expected `mu_3` character is not justified at P3.c grade without additional structure.

This document is the scope of P3.c, not its closure.

Critical framing constraint: the local Puiseux exponent `1/2` at `rho_3` produces `mu_2`-type local monodromy under branch traversal, not `mu_3`. Therefore `chi_3 in mu_3` cannot be naively identified with the local square-root Stokes multiplier at the singularity. The analytic source of `chi_3` is a load-bearing closure question.

## 2. HG-FND-003 and HG-VOC-006 attachment surfaces

`HG-FND-003` is currently registered as:

```text
Puiseux singular datum at a chosen puncture
```

with status:

```text
candidate; active core exists, registry normalization pending
```

`HG-VOC-006` is currently registered as:

```text
Character data chi_p, roots of unity, and finite phase reductions
```

with status:

```text
active core exists; registry normalization pending
```

P3.c closure must verify against both surfaces. `HG-FND-003` supplies the singular-location, local-expansion, and exponent-channel obligation. `HG-VOC-006` supplies the finite character / root-of-unity / phase-reduction obligation.

## 3. A1 paradigm at p=2

The manuscript records the A1 Catalan grammar:

```text
C(x)=1+xC(x)^2=(1-sqrt(1-4x))/(2x)
C_A=(A -> A -> A) -> A -> A
T ::= x | b(T,T)
```

The manuscript then defines Puiseux singularity channels. For a rational or algebraic `T(x)` at a singular point `rho`, it sets:

```text
t_rho = 1 - x/rho
```

and locally writes:

```text
T(x)=A_rho(t_rho)+sum_{beta in A_rho(T)} c_{rho,beta} t_rho^beta.
```

It states, verbatim:

```text
The exponent used by chi_p is a selected channel beta, not necessarily the leading term of the full local function.
```

For the Catalan warning, the manuscript says that near `rho=1/4`, the Catalan function has an analytic constant term plus a square-root singular correction. The exponent `1/2` belongs to the leading nonanalytic Puiseux channel, not to the full local germ as if the whole function were simply `c(1-4x)^(1/2)`.

The manuscript identifies `chi_p` through finite phase reduction from a selected rational exponent channel:

```text
k_p(beta)=floor(p beta) mod p
chi_p^(rho,beta)(T)=exp(2 pi i k_p(beta)/p) in mu_p.
```

The inspection did not find a manuscript sentence that explicitly designates A1 `chi_2=-1 in mu_2` as local Stokes multiplier, global monodromy character, or phase-character reduction in those exact terms. The manuscript instead gives the general finite phase-map definition above and separately records the A1 square-root Puiseux channel. Therefore this scope records the A1 source identification as partially implicit: A1 uses the selected exponent channel `beta=1/2`, and for `p=2` the finite phase-map output and local square-root sign change coincide.

This coincidence is precisely what becomes nontrivial at `p=3`: the local exponent remains `1/2`, which is square-root / `mu_2` local data, while the framework expects a `chi_3 in mu_3` finite phase. P3.c scope records this divergence as a closure obligation rather than assuming it away.

## 4. The mu_2 versus mu_3 structural tension

This section is load-bearing.

At `rho_3=4/27`, the local Puiseux exponent of `C_3(x)` is expected to be:

```text
alpha_3 = 1/2.
```

Under traversal of the branch point, the local square-root channel changes sign:

```text
(1 - x/rho_3)^(1/2) -> -(1 - x/rho_3)^(1/2).
```

This is `mu_2`-type local monodromy. It gives a character in `mu_2`, not in `mu_3`.

Therefore the `chi_3 in mu_3` character expected by the framework at `p=3` cannot be naively identified with the local Stokes multiplier at the singularity. It must arise, if justified, from a different source in the analytic / algebraic / finite-phase structure of `C_3(x)`.

Candidate sources:

### Source (a): local monodromy at rho_3

The local Puiseux exponent `1/2` produces `mu_2` characters from the square-root branch. It cannot directly produce a `mu_3` character without additional structure.

### Source (b): global monodromy of the three-sheeted cubic cover

The equation:

```text
x y^3 - y + 1 = 0
```

defines a degree-three algebraic function `y=C_3(x)` over `Q(x)`. The three sheets are the three roots of the cubic in `y` at fixed `x`.

For the cubic:

```text
a y^3 + b y^2 + c y + d = 0
```

with:

```text
a=x,
b=0,
c=-1,
d=1,
```

the discriminant computation gives the candidate closure path:

```text
Delta = 18abcd - 4b^3d + b^2c^2 - 4ac^3 - 27a^2d^2
      = 4x - 27x^2
      = x(4 - 27x).
```

This discriminant has odd-order zeros at `x=0` and `x=4/27`, so it is not a square in `Q(x)`. At scope grade, this candidate analysis suggests that the Galois / monodromy group of the cubic function-field extension should be the full `S_3`, rather than being contained in the index-2 subgroup `A_3`. This scope does not treat that group identification as closed.

If P3.c closure verifies the full `S_3` monodromy analysis, then the normal cyclic subgroup `A_3 ~= Z/3`, generated by three-cycles permuting the three sheets, becomes a candidate analytic source for `chi_3 in mu_3` through the sheet-permutation character. P3.c closure must verify the Galois / monodromy group identification, verify the `A_3` subgroup action on sheets, and verify that the resulting character matches the framework's `HG-VOC-006` expectation.

This is the strongest candidate analytic path for `chi_3`, but it is not closed by this scope document.

### Source (c): finite phase reduction through HG-VOC-006 / phase_characters.py

The manuscript defines finite phase characters by:

```text
k_p(beta)=floor(p beta) mod p,
chi_p^(rho,beta)(T)=exp(2 pi i k_p(beta)/p) in mu_p.
```

The `phase_characters.py` module supplies deterministic finite-arithmetic functions including:

```text
normalize_exponent(alpha)
phase_index(alpha, level=None)
p_primary_projection(index, level, prime)
prime_reduction(index, level, prime)
```

and carry / cocycle utilities.

Caution: if inputs are selected merely to produce the expected `mu_3` output, the module encodes rather than confirms `chi_3`. At P3.c closure, the analytic source of `chi_3` must be independently established before the module is invoked as a compatibility check.

Thus W4 is downstream verification, not the primary analytic source.

### Source (d): chi_3 not justified at P3.c grade

If sources (a), (b), and (c) do not produce a clean `mu_3` identification at the available grade, P3.c closure may declare that `chi_3` is not justified by the current apparatus and must be deferred to additional structure, possibly a later Heller-Einstein realization route or a future framework object.

## 5. Requirements on the p=3 Puiseux datum and chi_3

### Q1 — Singularity location

Verify at closure grade that:

```text
rho_3 = 4/27.
```

The natural verification path is to solve the critical-point system for:

```text
F(x,y)=y-1-x y^3 = 0,
F_y(x,y)=1-3xy^2 = 0.
```

Solving gives:

```text
y=3/2,
x=4/27.
```

This value appeared as traceability in `HG-MTH-014` and remained a P3.c-grade obligation in `HG-MTH-016`.

### Q2 — Local Puiseux exponent

Verify:

```text
alpha_3 = 1/2.
```

The natural verification path is local expansion of:

```text
F(x,y)=y-1-x y^3
```

around:

```text
(x,y)=(4/27,3/2).
```

Because:

```text
F=0,
F_y=0,
F_yy != 0,
F_x != 0
```

at the critical point, the leading local balance is square-root type. Closure must compute the constants rather than relying on this scope statement.

### Q3 — Explicit Puiseux expansion

Derive constants such as `A`, `B`, and `C` such that:

```text
C_3(x)=A + B(1 - x/rho_3)^(1/2) + C(1 - x/rho_3) + ...
```

in a neighborhood of `rho_3` on the selected branch. The sign convention must be explicit.

### Q4 — Character chi_3 in mu_3

P3.c closure must decide whether `chi_3` is:

1. directly induced by local monodromy at `rho_3`, which requires explaining how a `mu_2` local source produces a `mu_3` character;
2. induced by global monodromy of the three-sheeted algebraic curve `x y^3 - y + 1 = 0` via the `A_3 ~= Z/3` subgroup acting on sheets;
3. induced by finite phase reduction through `HG-VOC-006` / `phase_characters.py` applied to an independently justified analytic input;
4. not justified by P3.c without additional structure.

Closure must justify the selected option with an analytic / algebraic argument. Source (c) cannot be selected as the primary source without independent analytic justification of the input.

## 6. Candidate verification strategies

### W1 — Direct algebraic resolution

Solve:

```text
x y^3 - y + 1 = 0
```

explicitly as a cubic in `y` and read off the Puiseux expansion.

Strength: closed-form algebraic expression.  
Weakness: nested radicals may obscure the structural origin of `chi_3`.

### W2 — Newton-Puiseux at critical point

Use Newton-Puiseux / analytic-combinatorics methods to extract the local Puiseux data at:

```text
(x,y)=(4/27,3/2).
```

Strength: well-targeted for Q1, Q2, and Q3.  
Weakness: local analysis alone produces `mu_2` data and does not by itself justify `chi_3 in mu_3`.

### W3 — Galois / monodromy of the algebraic curve

Compute the Galois / monodromy structure of:

```text
x y^3 - y + 1 = 0
```

over `Q(x)`, verify or reject the candidate full-`S_3` monodromy path suggested by the discriminant analysis, identify any closure-grade `A_3 ~= Z/3` sheet-rotation subgroup if justified, and determine whether its sheet-permutation character is the correct `mu_3` source.

Strength: directly addresses Q4 source (b).  
Weakness: requires more algebraic-geometry / function-field machinery than local Puiseux analysis.

### W4 — phase_characters.py compatibility check

Use `phase_characters.py` only after an analytic `chi_3` source is independently justified. The module may check that the analytically derived character maps consistently into the framework-native finite-arithmetic representation.

Strength: confirms framework compatibility.  
Weakness: circular if used to define the analytic character.

P3.c closure likely uses W2 for Q1-Q3, W3 for the Q4 source candidate, and W4 only as downstream compatibility.

## 7. Heller-Einstein mediation route

If P3.c closure selects Q4 option (d), meaning `chi_3` is not justified at P3.c grade by the available Heller-Godel apparatus, the realization question may relocate to Heller-Einstein under typed-interface ontology.

That route would require separate Heller-Einstein authorization. This P3.c scope PR does not authorize Heller-Einstein development.

## 8. Grade declarations

| Object | Grade | Source |
| --- | --- | --- |
| `HG-FND-003` | candidate; registry normalization pending | `docs/framework-core/distance-classification.md` |
| `HG-VOC-006` | candidate; registry normalization pending | `docs/framework-core/distance-classification.md` |
| `HG-MTH-014` (P3.a closure) | method-grade modulo candidate-`HG-FND-001` | PR #82 |
| `HG-MTH-016` (P3.b closure) | method-grade modulo candidate-`HG-FND-002` | PR #86 |
| `HG-MTH-017` (P3.c scope, this PR) | method-grade as scope | this PR |
| P3.c closure (future) | would be method-grade modulo candidate-`HG-FND-003` and candidate-`HG-VOC-006` | not in this PR |

Cumulative-modulo accounting:

Full `HG-MTH-011` theorem-track promotion requires the following candidate surfaces to normalize or otherwise discharge:

```text
HG-FND-001
HG-FND-002
HG-FND-003
HG-VOC-006
HG-FND-006
HG-FND-007
```

P3.a contributes `HG-FND-001`. P3.b contributes `HG-FND-002`. P3.c would add `HG-FND-003` and `HG-VOC-006`. P3.d would add `HG-FND-006` and `HG-FND-007`.

Each modulo-candidate dependency is independent.

## 9. Non-claims

1. Does not close P3.c. Scope only.
2. Does not select among W1, W2, W3, and W4.
3. Does not select among Q4 options (a), (b), (c), and (d).
4. Does not specify explicit Puiseux expansion constants. That is closure work.
5. Does not specify the precise `mu_3` element of `chi_3`. That is closure work if the character is justified.
6. Does not assert that `chi_3 in mu_3` emerges from local monodromy at the singularity. The local Puiseux exponent `1/2` produces `mu_2` data; `chi_3 in mu_3`, if justified, requires a different analytic source.
7. Does not use `phase_characters.py` as the analytic source of `chi_3`; the module is downstream verification only.
8. Does not specify `zeta_3` carry defect or `U(2)` correspondence. That is P3.d.
9. Does not promote `HG-FND-003` or `HG-VOC-006` from candidate.
10. Does not promote `HG-MTH-011`.
11. Does not extend to `A_n` for `n >= 3` beyond A2.
12. Does not authorize Heller-Einstein PRs.
13. Does not cross into downstream Clay-program proof claims, including `SocioProphet/yang-mills`.

## 10. Future closure pathway

After P3.c scope merges, P3.c closure selects from W1-W4 and Q4 options (a)-(d) with explicit justification.

Closure must verify Q1-Q3 and must resolve Q4 without confusing local `mu_2` square-root monodromy with a global or finite-phase `mu_3` character.

If Q4 option (d) is selected, a later Heller-Einstein realization route may become relevant, but only under separate authorization.

P3.c closure unlocks P3.d: `zeta_3` carry defect and `U(2)` correspondence.

## 11. Identifier and registry

This document assigns:

```text
HG-MTH-017
```

to the P3.c Puiseux singularity and `chi_3` scope at `p=3`.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. This PR updates that registry to register `HG-MTH-017` and record its grade ceiling as method-grade as scope.
