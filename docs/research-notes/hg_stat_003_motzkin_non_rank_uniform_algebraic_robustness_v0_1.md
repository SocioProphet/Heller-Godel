# HG-STAT-003: Non-Rank-Uniform Algebraic Robustness in a Motzkin-Grounded Proof Grammar

## A Successor Note to HG-STAT-002 v0.1

**Status:** v0.1 — theorem-level for the Motzkin/unary-binary proof grammar under two syntax conventions; confirms algebraic type and square-root exponent preservation without rank-uniformity; radius remains covariant, not invariant.

---

## Abstract

HG-STAT-001 established admissible-statistic robustness on two rational rank-uniform calibration families. HG-STAT-002 extended the test to the algebraic Catalan-grounded type and showed that radius preservation fails even under rank-uniformity; radius instead covaries under the monomial regrading induced by the chosen statistic.

This note tests the next adversarial case: a non-rank-uniform algebraic proof grammar. The family is the Motzkin/unary-binary grammar induced by

```text
M_A = (A -> A) -> (A -> A -> A) -> A -> A
body ::= x | u body | b body body.
```

The correct generating object is the bivariate unary-binary tree generating function

```text
F(y,z) = 1 + y F(y,z) + z F(y,z)^2,
```

where `y` marks unary constructor nodes and `z` marks binary constructor nodes. The standard Motzkin numbers arise only after the specialization `F(t, t^2)`, which assigns size one to unary nodes and size two to binary nodes. The specialization `F(t,t)` instead gives the large Schroeder numbers. This distinction is load-bearing.

The result: under admissible constructor-linear statistics, both syntax conventions give algebraic generating functions by monomial substitution into `F(y,z)`. The family is not rank-uniform, yet the dominant branch remains a simple square-root branch with Puiseux exponent `1/2` for all tested admissible weights. The dominant radius is not invariant; it covaries as the positive root of the substituted discriminant.

Thus rank-uniformity is not necessary for exponent preservation in this algebraic family. The more accurate condition is stability of the singular branch type under admissible monomial substitution.

This note does not patch HG-STAT-001, HG-STAT-002, or CIPC v2.1.3. It is a successor result.

---

## 1. Background

The prior statistic-robustness notes established the following frontier:

| Family | Rank-uniform | Analytic type | Exponent | Radius |
|---|---:|---|---|---|
| Chain | yes | rational | `-2` | invariant, `rho=1` |
| T-family | yes | rational | `-2` | invariant, `rho=1` |
| Catalan | yes | algebraic | `1/2` | covariant |

HG-STAT-002 refuted the conjecture that rank-uniformity alone preserves radius. It left open whether rank-uniformity is needed for exponent preservation.

This note answers that bounded question negatively for one algebraic family: exponent preservation can hold without rank-uniformity.

## 2. The Motzkin-grounded proof family

Consider the type

```text
M_A = (A -> A) -> (A -> A -> A) -> A -> A.
```

A normal inhabitant has shape

```text
lambda u. lambda b. lambda x. body
```

where

```text
body ::= x | u body | b body body.
```

Let `U` be the number of unary nodes, occurrences of `u body`, and let `B` be the number of binary nodes, occurrences of `b body body`.

The body grammar is the standard plane unary-binary tree grammar, with bivariate generating function

```text
F(y,z) = 1 + y F(y,z) + z F(y,z)^2.
```

Solving the quadratic gives

```text
F(y,z) = (1 - y - sqrt((1-y)^2 - 4z)) / (2z),
```

with the branch chosen so that `F(0,0)=1`.

### 2.1 Motzkin-size convention

The standard Motzkin numbers arise when unary nodes have size one and binary nodes have size two:

```text
F(t, t^2) = 1 + t F(t,t^2) + t^2 F(t,t^2)^2.
```

The coefficients are

```text
1, 1, 2, 4, 9, 21, 51, 127, 323, ...
```

The equal-node-count specialization `F(t,t)` is different and gives large Schroeder numbers:

```text
1, 2, 6, 22, 90, 394, ...
```

Therefore the correct invariant object for admissible statistics is the bivariate `F(y,z)`, not a fixed univariate Motzkin specialization.

## 3. Non-rank-uniformity

Use Motzkin level

```text
n = U + 2B.
```

The profile counts begin:

| level `n` | profile counts `(U,B) -> count` |
|---:|---|
| 0 | `{(0,0): 1}` |
| 1 | `{(1,0): 1}` |
| 2 | `{(2,0): 1, (0,1): 1}` |
| 3 | `{(3,0): 1, (1,1): 3}` |
| 4 | `{(4,0): 1, (2,1): 6, (0,2): 2}` |
| 5 | `{(5,0): 1, (3,1): 10, (1,2): 10}` |
| 6 | `{(6,0): 1, (4,1): 15, (2,2): 30, (0,3): 5}` |

The family is non-rank-uniform already at level 2, where both `(U,B)=(2,0)` and `(U,B)=(0,1)` occur.

This is a real non-uniformity under admissible constructor-linear weights: in general these profiles receive different `sigma_w` values.

## 4. Syntax conventions

As in HG-STAT-002, constructor counts depend on how applications are tokenized. We state both conventions.

### 4.1 Convention A: binary/n-ary head application

Convention A treats `u body` as one application node with one argument, and `b body body` as one application node with two arguments. The head of each application node is the corresponding variable.

For profile `(U,B)`:

```text
|lambda| = 3
|app|    = U + B
|var|    = U + 2B + 1
```

Explanation:

- three outer lambdas bind `u`, `b`, and `x`;
- there is one application node per unary or binary constructor occurrence;
- variable occurrences consist of `U` uses of `u`, `B` uses of `b`, and `B+1` leaf occurrences of `x`, totaling `U+2B+1`.

For admissible weights `w=(w_lambda,w_app,w_var)`, define

```text
c_A = 3*w_lambda + w_var
a_A = w_app + w_var
b_A = w_app + 2*w_var.
```

Then

```text
T_A^w(x) = x^(c_A) F(x^(a_A), x^(b_A)).
```

### 4.2 Convention B: curried application

Convention B treats `b body body` as `((b body) body)`, i.e. two binary application nodes. Unary application `u body` remains one application node.

For profile `(U,B)`:

```text
|lambda| = 3
|app|    = U + 2B
|var|    = U + 2B + 1
```

For admissible weights, define

```text
c_B = 3*w_lambda + w_var
a_B = w_app + w_var
b_B = 2*w_app + 2*w_var.
```

Then

```text
T_B^w(x) = x^(c_B) F(x^(a_B), x^(b_B)).
```

## 5. Theorem: Motzkin algebraic robustness

**Theorem 5.1 (Motzkin robustness, Convention A).** Under Convention A and admissible constructor-linear weights, `T_A^w(x)` is algebraic. Its dominant positive singularity is the smallest positive root of

```text
Delta_A(x) = (1 - x^(a_A))^2 - 4*x^(b_A) = 0.
```

At that root the discriminant has a simple zero, so the local Puiseux exponent is `1/2`.

**Proof.** The bivariate generating function `F(y,z)` is algebraic because it satisfies `F = 1 + yF + zF^2`. The substitution `(y,z)=(x^(a_A),x^(b_A))`, followed by multiplication by `x^(c_A)`, preserves algebraicity.

The square-root branch is controlled by the discriminant

```text
Delta_A(x) = (1 - x^(a_A))^2 - 4*x^(b_A).
```

For `0 < x < 1`, the dominant positive singularity `rho` satisfies

```text
1 - rho^(a_A) = 2*rho^(b_A/2).
```

The derivative is

```text
Delta_A'(x)
  = -2*a_A*(1 - x^(a_A))*x^(a_A-1) - 4*b_A*x^(b_A-1).
```

At `rho`, all factors are positive except the leading signs, so `Delta_A'(rho) < 0`. Thus the discriminant has a simple zero at the dominant positive singularity. The local branch is therefore square-root, with Puiseux exponent `1/2`. QED.

**Theorem 5.2 (Motzkin robustness, Convention B).** Under Convention B and admissible constructor-linear weights, `T_B^w(x)` is algebraic. Its dominant positive singularity is the smallest positive root of

```text
Delta_B(x) = (1 - x^(a_B))^2 - 4*x^(b_B) = 0.
```

At that root the discriminant has a simple zero, so the local Puiseux exponent is `1/2`.

**Proof.** Identical to Theorem 5.1 with `(a_A,b_A,c_A)` replaced by `(a_B,b_B,c_B)`. QED.

## 6. Consequences

The Motzkin-grounded grammar is not rank-uniform, yet admissible constructor-linear reweightings preserve:

- algebraic analytic type;
- square-root local exponent `1/2` at the dominant positive singularity.

They do not preserve the radius. The dominant radius covaries as the positive root of the substituted discriminant.

This strengthens the conjectural picture produced by HG-STAT-002:

- rank-uniformity is not necessary for exponent preservation;
- radius covariance is the general behavior under monomial regrading;
- the relevant exponent condition appears to be singular-branch stability under admissible monomial substitution.

## 7. Refined conjecture hierarchy

### Conjecture 7.1: analytic type preservation

For regular, algebraic, and D-finite proof grammars, admissible constructor-linear statistics preserve analytic class.

The evidence stack is now:

- chain: rational;
- T-family: rational;
- Catalan: algebraic;
- Motzkin/unary-binary: algebraic and non-rank-uniform.

### Conjecture 7.2': exponent preservation under simple-branch invariance

For proof grammars whose multivariate generating function has a stable simple algebraic branch under admissible monomial substitution, the dominant Puiseux exponent is preserved across admissible constructor-linear statistics.

This replaces the weaker rank-uniform condition as the candidate explanation for exponent preservation. Rank-uniformity is sufficient in the tested Catalan case, but not necessary; Motzkin is the counterexample to necessity.

### Conjecture 7.3: radius covariance

For proof grammars whose generating function can be expressed multivariately by constructor profiles, admissible constructor-linear statistics act by monomial substitution. Dominant radius is therefore covariant under the induced substitution, not invariant in general.

Chain and T-family had invariant radius because their underlying singular radius in the level variable was `1`. Catalan and Motzkin expose the nontrivial covariance case.

## 8. Frontier table

| Family | Rank-uniform | Type preserved | Exponent preserved | Radius preserved |
|---|---:|---|---|---|
| Chain | yes | yes, rational | yes, `-2` | yes, `rho=1` |
| T-family | yes | yes, rational | yes, `-2` | yes, `rho=1` |
| Catalan | yes | yes, algebraic | yes, `1/2` | no, covaries |
| Motzkin/unary-binary | no | yes, algebraic | yes, `1/2` | no, covaries |

## 9. What this note establishes / does not establish

### Established

For the Motzkin/unary-binary proof grammar under admissible constructor-linear statistics:

- the family is non-rank-uniform;
- the correct GF object is bivariate `F(y,z)`;
- both syntax conventions give algebraic GFs by monomial substitution;
- the dominant positive singularity is a simple square-root branch;
- the local exponent `1/2` is preserved;
- radius is covariant, not invariant.

### Not established

This note does not establish:

- the full analytic-type conjecture for all regular/algebraic/D-finite proof grammars;
- exponent preservation for arbitrary non-rank-uniform families;
- behavior of multi-shell character data under non-rank-uniformity;
- any recognition-dynamical or semantic consequence.

## 10. Relationship to prior notes

This note does not require revision of CIPC v2.1.3, HG-STAT-001 v0.1, or HG-STAT-002 v0.1.

- HG-STAT-001 remains the rational rank-uniform calibration note.
- HG-STAT-002 remains the Catalan algebraic rank-uniform note and radius-covariance correction.
- HG-STAT-003 adds a non-rank-uniform algebraic test and refines the likely condition for exponent preservation.

If a future CIPC v2.2 incorporates the statistic-robustness line, it should say that evidence now supports analytic-type preservation across rational and algebraic test families, while exponent preservation appears tied to simple-branch stability rather than rank-uniformity.

## Appendix A. Regression harness

The regression harness for this note is implemented in:

```text
tests/test_admissible_statistics_motzkin.py
```

It verifies:

- Motzkin number specialization under `U + 2B` size;
- explicit non-rank-uniform profiles at levels 2 and 4;
- Convention A bivariate substitution;
- Convention B bivariate substitution;
- radius covariance and simple branch under Convention A;
- radius covariance and simple branch under Convention B.

## Document history

- **v0.1** — initial release. Theorems 5.1 and 5.2 stated and proved. Motzkin vs. Schroeder size-convention distinction recorded. Exponent preservation refined from rank-uniformity to simple-branch invariance.
