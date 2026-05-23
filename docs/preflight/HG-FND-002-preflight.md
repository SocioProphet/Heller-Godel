# HG-FND-002 Preflight — Proof-Class Generating-Function Surface

Issue: #104  
Branch: `work/hg-fnd-002-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new mathematics.

## Purpose

This preflight records the current `HG-FND-002` normalization surface before any implementation PR is opened.

`HG-FND-002` is the proof-class / proof-family generating-function construction surface. It is downstream of normalized `HG-FND-001`, which supplies the restricted typed grammar, canonical witness convention, and declared statistic discipline. It is upstream of `HG-FND-003`, which owns the Puiseux singular datum at a chosen puncture.

## Finding 1 — Reference inventory

| Location | Reference type | Count |
| --- | --- | ---: |
| `docs/framework-core/distance-classification.md` | Registry row with candidate status | 1 |
| `docs/framework-core/claim-grammar.md` | Non-claim boundary in `HG-MTH-016` and `HG-MTH-021`; deferred queue entry | 8 |
| `docs/framework-core/anti-seed-framework.md` | Existing anti-seed entry `A-HG-FND-002` | 1 |
| `docs/framework-foundations/HG-FND-001-restricted-proof-grammar.md` | Interface boundary Section 7 and non-claims Section 11 | 6 |
| Paper I / D1 Section 2 | Active mathematical core | live |

## Finding 2 — Interface boundary

The left/right split is already typed by `HG-FND-001`.

`HG-FND-001` owns:

```text
restricted typed grammar + canonical witness convention + declared statistic discipline
```

`HG-FND-002` owns:

```text
proof-class / proof-family generating-function construction
and analytic extraction discipline
```

Interface:

```text
restricted grammar + declared statistic
  -> countable witness family N_phi
  -> T_phi^sigma(x) = sum_{s in N_phi} x^{sigma(s)}
```

The normalized surface must own exactly this right side. It must not absorb `HG-FND-001` grammar obligations or downstream `HG-FND-003` puncture decoration.

## Finding 3 — Active mathematical core in Paper I Section 2

Content expected to belong in normalized `HG-FND-002`:

1. Typed definition:

```text
T_phi(x) = sum_{s in N_phi} x^{sigma(s)}
```

with explicit dependency on `HG-FND-001` for `N_phi` and `sigma`.

2. Product formula under reduced statistic:

```text
T_{phi x psi}(x) = T_phi(x) T_psi(x)
```

with an explicit note that the raw constructor count shifts by `x` if the outer pairing constructor is included; the reduced statistic subtracts that constructor.

3. Canonical witnesses:

```text
Chain:   T_chain(x) = x/(1-x)^2, dominant singularity rho=1, integer exponent.
Catalan: C(x) = (1 - sqrt(1-4x))/(2x), dominant singularity rho=1/4.
```

4. Singularity extraction discipline:

```text
identify dominant rho;
state rational Puiseux exponent alpha_{phi,rho}=a/N in lowest terms.
```

This is the `HG-FND-002` / `HG-FND-003` boundary: `HG-FND-002` identifies `rho` and `alpha`; `HG-FND-003` decorates the puncture datum.

## Finding 4 — Anti-seed status

The existing `A-HG-FND-002` entry in `docs/framework-core/anti-seed-framework.md` covers `Curv_3` as elementary abelian cohomology. That is a framework-vocabulary anti-seed, not a generating-function-specific anti-seed.

The normalization PR should register at least one generating-function-specific anti-seed. Candidate failure modes:

- unstatted series: citing a power series as a proof-class generating function without declaring which restricted grammar and which statistic produced it;
- singularity conflation: treating the singularity of a generating function as proof-grade Puiseux datum without the decoration step owned by `HG-FND-003`.

This preflight records the requirement only. It does not register a new anti-seed.

## Finding 5 — Existing test coverage gap

`tests/test_phase_characters.py` contains `test_catalan_klein_bottle_mu2_holonomy_bookkeeping`, but it does not directly validate:

- the product formula `T_{phi x psi}(x) = T_phi(x) T_psi(x)`;
- the reduced-vs-raw statistic distinction;
- the chain example `T_chain(x) = x/(1-x)^2`.

The normalization PR should add a guard such as:

```text
tests/test_hg_fnd_002_generating_function.py
```

The guard should verify the product formula under the reduced statistic for at least the A1 Catalan and chain examples.

## Finding 6 — Proposed discharge criterion

A downstream claim may cite normalized `HG-FND-002` when it supplies:

1. target type `phi` with witness family `N_phi` from `HG-FND-001`;
2. declared statistic `sigma`, either full node-count or constructor-shape;
3. explicit statement of whether reduced or raw statistic is used;
4. dominant singularity `rho` identified;
5. rational Puiseux exponent `alpha_{phi,rho}` in lowest terms stated;
6. no undecorated Puiseux datum claimed as `HG-FND-003` content.

## Proposed implementation file plan

Future normalization PR, not this preflight:

```text
docs/framework-foundations/HG-FND-002-proof-class-generating-function.md
tests/test_hg_fnd_002_generating_function.py
```

Expected registry update in the future normalization PR:

```text
Move HG-FND-002 from candidate table to normalized Tier 1 table in docs/framework-core/distance-classification.md.
```

## Non-actions

This preflight does not normalize `HG-FND-002`.

This preflight does not register new anti-seeds; it records the anti-seed requirement only.

This preflight does not write the normalization test guard; it records the validation expectation only.

This preflight does not promote `HG-MTH-011` or `HG-MTH-016`.

This preflight does not discharge `HG-FND-003`, `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`.

This preflight does not start P1 path-beta uniqueness or P2 candidate-list exhaustion.

This preflight does not authorize `A_n` extension.

This preflight does not authorize Heller-Einstein, Heller-Dirac, `yang-mills`, `np-program`, BSD, Heller-Winters, or `ns-program` work.

## Stop rule

After this preflight PR is opened and validated, halt.

Implementation of `HG-FND-002` normalization requires separate authorization.
