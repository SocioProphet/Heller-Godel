# HG-FND-002 — Proof-Class Generating-Function Construction

Identifier: `HG-FND-002`  
Layer: framework-foundational / Tier 1.  
Status: normalized proof-class / proof-family generating-function foundation.  
Owner: `SocioProphet/Heller-Godel`.  
Claim level: framework-foundational definition and discipline; not downstream promotion.

Normalized dependency: `HG-FND-001` at merge SHA `38f89aefa9fa3238171e451dfe9bf49ac0d1352c`, source `docs/framework-foundations/HG-FND-001-restricted-proof-grammar.md`.

## 1. Purpose

`HG-FND-002` normalizes the generating-function construction used by the proof-character pipeline.

It applies only after `HG-FND-001` has supplied the restricted typed grammar, canonical witness convention, witness family `N_phi`, and declared statistic `sigma`.

This document discharges the candidate status of the proof-class / proof-family generating-function construction surface. It does not discharge the Puiseux singular-datum surface `HG-FND-003` or any phase, cover, monodromy, or carry-cocycle surface.

## 2. Typed definition

Let `phi` be a target type with a normalized restricted proof grammar governed by `HG-FND-001`.

Let:

```text
N_phi = alpha-classes of eta-long beta-normal witnesses of phi
```

under the declared context and production rules.

Let `sigma:N_phi -> N` be a declared statistic, either full node-count or constructor-shape when a constructor-skeleton quotient has been explicitly declared.

The proof-family generating function is:

```text
T_phi^sigma(x) = sum_{s in N_phi} x^{sigma(s)}.
```

When the statistic is clear from context, write `T_phi(x)`. A citation to this construction must still declare the statistic actually used.

## 3. Reduced and raw statistic discipline

For product witnesses, distinguish raw statistic from reduced statistic.

If an outer pairing constructor is counted, the raw statistic satisfies:

```text
sigma_raw(pair(s,t)) = 1 + sigma(s) + sigma(t).
```

The reduced statistic subtracts the outer pairing constructor:

```text
sigma_red(pair(s,t)) = sigma(s) + sigma(t).
```

Therefore the product formula licensed by `HG-FND-002` is the reduced-statistic formula:

```text
T_{phi x psi}^{sigma_red}(x) = T_phi^sigma(x) T_psi^sigma(x).
```

If a downstream document uses the raw statistic, it must record the additional factor:

```text
T_{phi x psi}^{sigma_raw}(x) = x T_phi^sigma(x) T_psi^sigma(x).
```

## 4. Canonical witnesses

### 4.1 Chain witness

The chain family has ordinary generating function:

```text
T_chain(x) = x/(1-x)^2 = sum_{n>=1} n x^n.
```

Its dominant singularity is `rho = 1`. The local singular order is integral. No branch decoration is asserted here.

### 4.2 Catalan witness

The A1 Catalan constructor-shape witness family has ordinary generating function:

```text
C(x) = (1 - sqrt(1-4x))/(2x) = 1 + x C(x)^2.
```

Its dominant singularity is `rho = 1/4`. The rational Puiseux exponent at the dominant singularity is `alpha = 1/2`.

This records the generating-function singular structure only. It does not decorate the puncture as `HG-FND-003` data.

## 5. Singularity extraction discipline

`HG-FND-002` permits extraction of:

```text
rho = dominant singularity;
alpha_{phi,rho} = rational Puiseux exponent in lowest terms.
```

The extraction must be tied to the declared statistic. A change from constructor-shape coordinate to full node-count coordinate changes the singularity location by the declared monomial substitution from `HG-FND-001`:

```text
T_r^sigma_C(y) = y^3 C_r(y^(2r-1)).
```

## 6. Boundary with HG-FND-003

`HG-FND-002` identifies `rho` and `alpha_{phi,rho}` for a declared proof-family generating function.

`HG-FND-003` owns the Puiseux singular datum at a chosen puncture.

Therefore, `HG-FND-002` does not license a downstream claim to treat an undecorated singularity as a decorated Puiseux datum. It supplies input to `HG-FND-003`; it does not replace `HG-FND-003`.

## 7. Discharge criterion

A downstream claim may cite normalized `HG-FND-002` only when it supplies:

1. target type `phi` with witness family `N_phi` from normalized `HG-FND-001`;
2. declared statistic `sigma`, either full node-count or constructor-shape;
3. explicit statement of whether reduced or raw statistic is used;
4. dominant singularity `rho` identified;
5. rational Puiseux exponent `alpha_{phi,rho}` in lowest terms stated;
6. no undecorated Puiseux datum claimed as `HG-FND-003` content.

## 8. Non-claims

This document does not normalize `HG-FND-003`, `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`.

This document does not promote `HG-MTH-011` or `HG-MTH-016`.

This document does not decorate any Puiseux puncture datum.

This document does not prove path-beta uniqueness or candidate-list exhaustion.

This document does not extend the framework to an `A_n` family.

This document does not authorize Heller-Einstein, Heller-Dirac, `yang-mills`, `np-program`, BSD, Heller-Winters, or `ns-program` work.
