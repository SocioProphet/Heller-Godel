# Proof and Falsification Infrastructure Standard

Status: governance doctrine for Heller–Gödel research tranches. This is process infrastructure, not a theorem and not a promotion of future-horizon material into theorem-core.

## 1. Operating principle

Every Heller–Gödel research tranche must leave behind reusable, testable infrastructure for proof and falsification.

A tranche is not complete merely because it produced prose. A tranche is complete only when its claims can be inspected, replayed, falsified, or explicitly routed as future-horizon material.

The standard form is:

```text
claim -> status label -> evidence artifact -> reproducibility path -> falsifier / boundary
```

## 2. Required claim statuses

Every nontrivial claim must be one of:

```text
proved
computed
definition
conjecture
future_horizon
false_as_stated
superseded
context_only
needs_formalization
delete
```

These labels are not cosmetic. They decide where a claim may live.

- `proved`: theorem-core; proof appears in note/manuscript.
- `computed`: theorem-supporting or hypothesis-supporting computation; must have tests or replay instructions.
- `definition`: terminology or construction boundary; must not be mistaken for a theorem.
- `conjecture`: open but stated sharply enough to be attacked.
- `future_horizon`: exploratory, useful, and preserved, but not load-bearing.
- `false_as_stated`: retained only if it teaches a correction or erratum.
- `superseded`: historical claim replaced by a sharper statement.
- `context_only`: methodological, analogical, or precedent material.
- `needs_formalization`: plausible but missing the object required to state it rigorously.
- `delete`: do not preserve except in a review ledger.

## 3. Required artifacts by claim type

### 3.1 Theorem-core claims

A theorem-core claim requires:

- exact statement;
- proof or derivation;
- named hypotheses;
- examples or boundary cases;
- explicit non-goals;
- regression tests when computable.

### 3.2 Computed claims

A computed claim requires:

- source inputs or hash-locked fixtures;
- executable test or replay command;
- expected output;
- failure condition;
- claim-boundary note explaining what the computation does not prove.

### 3.3 Conjectures

A conjecture requires:

- minimal statement;
- known positive evidence;
- known negative evidence or counterexample class;
- at least one falsifier;
- next bounded experiment.

### 3.4 Future horizons

Future-horizon material must be preserved, not discarded. But it must be routed away from theorem-core until its missing objects exist.

A future-horizon note requires:

- motivation;
- analogy or candidate mechanism;
- missing constructions;
- promotion criteria;
- explicit statement that it is not evidence for current theorem claims.

## 4. Standard research-tranche file set

A mature tranche should produce some subset of:

```text
docs/research-notes/<note>.md
docs/review-ledgers/<claim-ledger>.md
docs/future-horizons/<horizon-note>.md
docs/governance/<process-note>.md
tests/test_<claim>.py
data/fixtures/<fixture>.json
reports/<version>/<manifest>.sha256
```

A prose-only tranche is acceptable only when the object is explicitly `context_only` or `future_horizon` and no computable claim is made.

## 5. Application to current Heller–Gödel work

### 5.1 CIPC / proof-character manuscript

The load-bearing core is:

```text
restricted proof grammar + fixed canonical statistic
-> proof-family generating function
-> Puiseux singularity data
-> finite phase reductions chi_p / chi_13
-> mod-p carry defect zeta_p
```

Required infrastructure:

- claim-status ledger;
- carry-coboundary regression;
- chain-product regression;
- Puiseux-channel regression;
- statistic-dependence and admissible-statistics tests.

### 5.2 HG-STAT-001 / 002 / 003

These are model examples of this standard.

HG-STAT-001:

- theorem-level on two rational calibration families;
- tests for admissible constructor-linear statistics;
- erratum routing after Catalan refuted radius preservation.

HG-STAT-002:

- theorem-level on Catalan algebraic family;
- tests for both syntax conventions;
- radius covariance captured as correction to the strong conjecture.

HG-STAT-003:

- theorem-level on non-rank-uniform Motzkin/unary-binary grammar;
- bivariate GF made load-bearing;
- tests for non-rank-uniformity, bivariate substitution, radius covariance, and simple branch.

### 5.3 Wythoff / Schwarz material

Wythoff / Schwarz alignment is context and future horizon unless converted into a theorem about proof grammars.

It should live under:

```text
docs/future-horizons/
```

It may supply vocabulary for finite symbolic seeds, curvature regimes, and projection/preimage discipline, but it must not be used as proof of any Heller–Gödel mechanism.

### 5.4 BSD material

BSD material is context-only for Heller–Gödel.

It demonstrates:

- evidence gates;
- rollback discipline;
- exact row-state accounting;
- manifest/hash discipline;
- claim-tier hygiene.

It does not support Heller–Gödel theorem claims and must not enter HG tests except as governance precedent.

## 6. Falsification standard

Every conjecture should expose at least one concrete way to fail.

Examples:

- If `zeta_p` is claimed to be a nontrivial cohomological obstruction, the coboundary test falsifies that claim under ordinary cochain freedom.
- If ordinary chain product is claimed to be `x^2/(1-x)^3`, polynomial multiplication falsifies it; the correct ordinary product is `x^2/(1-x)^4`.
- If rank-uniformity is claimed to preserve dominant radius, Catalan falsifies it.
- If exponent preservation is claimed to require rank-uniformity, Motzkin/unary-binary weakens that requirement by counterexample.

Falsifiers are assets. They narrow the theorem.

## 7. PR checklist

Every research PR should answer:

1. What claims are added?
2. What status does each claim have?
3. Which claims are theorem-core?
4. Which claims are computed?
5. Which claims are conjectural?
6. Which claims are future-horizon only?
7. What tests or replay commands exist?
8. What fixtures or hashes are required?
9. What would falsify the central conjecture?
10. What is explicitly out of scope?

A PR that cannot answer these questions should be draft-only.

## 8. Non-negotiable boundary

Exploration is allowed. Speculation is allowed. Analogy is allowed. But theorem-core promotion requires reusable proof/falsification infrastructure.

The repository must preserve intellectual exploration without converting unconstructed ideas into claims.
