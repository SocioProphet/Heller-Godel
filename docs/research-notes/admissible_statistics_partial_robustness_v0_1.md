# A Partial Robustness Result for Statistic-Class Stability of Proof-Family Generating Functions

Companion note to `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`  
Tracking issue: HG-STAT-001 / #7  
Status: standalone research note; partial result; not folded into v2.1.3.

## Abstract

The parent manuscript establishes that proof-family generating functions are invariant under choice of proof calculus only after canonicalization and only for a fixed statistic. It also records that naive statistic-invariance fails: different intrinsic statistics can yield different generating functions and different analytic behavior.

This note refines the open statistic-robustness question by defining an admissible class of statistics: positive-weight linear combinations of local node counts in canonical de Bruijn syntax trees. On two calibration families, every admissible statistic gives a rational generating function with dominant radius `1` and dominant local exponent `-2`. This is stronger than mere analytic-type preservation on those families.

This is not a general theorem for all proof grammars. It is a partial robustness result plus a theorem target. In particular, the general claim that dominant radius and local exponent are preserved across all regular, algebraic, or D-finite proof grammars is not established here and should be treated cautiously. Analytic type is the safer expected invariant; radius and exponent require additional hypotheses.

## 1. Background

The parent v2.1.3 manuscript fixes the core discipline:

1. proof-family generating functions require a fixed proof fragment, canonical normal form, and fixed statistic;
2. calculus-invariance is asserted only after canonicalization;
3. statistic-relativity is real;
4. naive statistic-invariance is false;
5. statistic-class robustness is a natural sequel rather than theorem-core.

This note addresses that sequel in the smallest testable setting.

## 2. Admissible statistics

Let `s` be an eta-long beta-normal de Bruijn lambda term, viewed as a tree with three local node classes:

- lambda-abstraction nodes;
- application nodes;
- variable-occurrence leaves.

Write these counts as:

```text
|lambda(s)|, |app(s)|, |var(s)|.
```

## Definition 2.1: admissible constructor-count statistic

A statistic is admissible for this note if

```text
sigma_w(s) = w_lambda * |lambda(s)| + w_app * |app(s)| + w_var * |var(s)|
```

where

```text
w_lambda, w_app, w_var in Z_{>0}.
```

The canonical constructor-count statistic is the weight vector `(1,1,1)`.

### Motivation

The definition enforces three design constraints:

- locality: each node contributes by its local node class;
- linear comparability: positive weights make `sigma_w` comparable to total node count;
- sum-compositionality: the statistic is additive over syntax-tree decomposition.

These constraints motivate the definition. They should not be read as a complete if-and-only-if characterization of every possible statistic satisfying locality/compositionality in richer typed or annotated syntax. Future work may enlarge the admissible class.

### Non-admissible statistics from the parent falsifier

The parent manuscript's depth statistic is non-admissible because it is max-aggregated, not sum-aggregated. It also fails linear lower comparability on balanced trees.

The de Bruijn-index-sum statistic is non-admissible because variable contribution depends on binding depth/context rather than only on local node class. It can also fail uniform linear comparability depending on the term family.

Thus the parent falsifier and the present robustness result are compatible: they apply to complementary statistic classes.

## 3. Calibration family I: chain inhabitants

Let the chain family have `n` inhabitants at level `n`, each of the shape

```text
lambda x_n ... lambda x_1 . x_i, 1 <= i <= n.
```

Each inhabitant has:

```text
lambda nodes       = n
application nodes  = 0
variable nodes     = 1
```

Therefore

```text
sigma_w = w_lambda * n + w_var.
```

The family-level generating function is

```text
T_chain^sigma_w(x) = sum_{n>=1} n * x^(w_lambda*n + w_var)
                   = x^(w_lambda + w_var) / (1 - x^w_lambda)^2.
```

For all positive weights:

- analytic type: rational;
- smallest positive dominant radius: `rho = 1`;
- dominant local exponent at `rho = 1`: `alpha = -2`.

## 4. Calibration family II: `((A -> A) -> A) -> A`

The second test family is the family used in the parent manuscript's statistic-dependence falsifier. There are exactly `n` normal inhabitants `t_{n,i}`, with `1 <= i <= n`, of the form

```text
lambda f . f (lambda x_1 . f (lambda x_2 . ... f (lambda x_n . x_i) ...)).
```

Each inhabitant has:

```text
lambda nodes       = n + 1
application nodes  = n
variable nodes     = n + 1
```

Thus, with

```text
d = w_lambda + w_app + w_var
c = w_lambda + w_var,
```

we have

```text
sigma_w(t_{n,i}) = d*n + c.
```

Because there are `n` inhabitants at level `n`, the generating function is

```text
T_T^sigma_w(x) = sum_{n>=1} n * x^(d*n + c)
               = x^(d+c) / (1 - x^d)^2
               = x^(2*w_lambda + w_app + 2*w_var) / (1 - x^(w_lambda+w_app+w_var))^2.
```

For the canonical weight vector `(1,1,1)`, this gives

```text
x^5 / (1 - x^3)^2,
```

with coefficients

```text
c_5=1, c_8=2, c_11=3, c_14=4, ...
```

For all positive weights:

- analytic type: rational;
- smallest positive dominant radius: `rho = 1`;
- dominant local exponent at `rho = 1`: `alpha = -2`.

## 5. Boundary weights

The weight vector `(1,1,0)` is useful as a boundary check but is not admissible under Definition 2.1 because `w_var=0`. It still preserves rationality, radius, and exponent on the two calibration families.

This suggests a possible later relaxation to nonnegative weights, provided every relevant recursive production receives positive total weight and the statistic remains proper. That relaxation is not part of the current admissibility definition.

## 6. General theorem target

A cautious theorem target is:

> For proof families generated by regular grammars, admissible positive-weight constructor-count statistics preserve rationality of the generating function.

A broader conjecture is:

> For proof families generated by regular, algebraic, or D-finite proof grammars, admissible positive-weight constructor-count statistics preserve the analytic class: rational, algebraic, or D-finite respectively.

The stronger claim that dominant radius and dominant local exponent are always preserved is not asserted here. It holds on the two calibration families, but in general the radius can depend on the weight vector and the exponent can require nondegeneracy assumptions about the grammar and singularity schema.

## 7. Proof strategy sketch

For regular grammars, one expects a transfer-matrix construction. A positive-weight constructor count assigns monomial weights to transitions or productions. The resulting generating function remains rational because it is obtained from a finite weighted automaton or finite system of linear equations.

For algebraic grammars, positive-weight constructor counts should preserve algebraicity because the weighted generating functions remain solutions of polynomial systems.

For D-finite grammars, positive-weight substitutions and diagonal/extraction operations are expected to preserve D-finiteness under the appropriate closure hypotheses.

These are standard analytic-combinatorics directions, but they must be translated carefully into the proof-grammar setting before promotion to theorem-core.

## 8. What this note establishes

This note establishes:

1. a precise restricted admissibility class;
2. exclusion of the parent falsifier statistics from that class;
3. closed-form generating functions for two calibration families under every positive-weight admissible statistic;
4. preservation of rationality, `rho=1`, and `alpha=-2` on those two families;
5. a plausible route to a regular-grammar theorem.

## 9. What this note does not establish

This note does not establish:

1. statistic robustness for all proof families;
2. radius or exponent invariance in general;
3. any result for non-admissible statistics;
4. any result for phase characters beyond the two calibration families;
5. multi-shell robustness;
6. recognition-dynamical or semantic consequences.

## 10. Relationship to v2.1.3

This note does not require revision of v2.1.3. The parent manuscript can remain frozen with statistic-class robustness listed as conjectural.

A future v2.2 may cite this note as partial evidence and, if a rigorous regular-grammar theorem is completed, may promote the result into the parent manuscript.

## Appendix A. Tested weights

The following weights were checked against closed forms:

| weights | chain GF | `T` family GF | status |
|---|---|---|---|
| `(1,1,1)` | `x^2/(1-x)^2` | `x^5/(1-x^3)^2` | admissible |
| `(1,2,1)` | `x^2/(1-x)^2` | `x^6/(1-x^4)^2` | admissible |
| `(2,1,1)` | `x^3/(1-x^2)^2` | `x^7/(1-x^4)^2` | admissible |
| `(1,1,2)` | `x^3/(1-x)^2` | `x^7/(1-x^4)^2` | admissible |
| `(3,1,1)` | `x^4/(1-x^3)^2` | `x^9/(1-x^5)^2` | admissible |
| `(1,3,1)` | `x^2/(1-x)^2` | `x^7/(1-x^5)^2` | admissible |
| `(5,1,1)` | `x^6/(1-x^5)^2` | `x^13/(1-x^7)^2` | admissible |
| `(1,1,0)` | `x/(1-x)^2` | `x^3/(1-x^2)^2` | boundary, non-admissible |

All listed closed forms match direct enumeration through `n=8`.
