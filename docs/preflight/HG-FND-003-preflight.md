# HG-FND-003 Preflight — Puiseux Singular-Datum Surface

Issue: #107  
Branch: `work/hg-fnd-003-preflight`  
Status: preflight only; no normalization performed.  
Claim level: governance / inspection; no new mathematics.

## Purpose

This preflight records the current `HG-FND-003` normalization surface before any implementation PR is opened.

`HG-FND-003` is the Puiseux singular-datum surface at a chosen puncture. It is downstream of normalized `HG-FND-002`, which identifies the dominant singularity `rho` and rational Puiseux exponent `alpha`. It is adjacent to, but distinct from, `HG-VOC-006`, which owns character data, roots of unity, and finite phase reductions.

## Finding 1 — Reference inventory

| Location | Reference type | Count |
| --- | --- | ---: |
| `docs/framework-core/distance-classification.md` | Registry row with candidate status | 1 |
| `docs/framework-core/claim-grammar.md` | Non-claim boundary in `HG-MTH-018`, `HG-MTH-021`, and deferred queue | active |
| `docs/framework-foundations/HG-FND-002-proof-class-generating-function.md` | Boundary with singularity identification discipline | active |
| `docs/framework-core/anti-seed-framework.md` | `A-HG-FND-007` boundary against undecorated singularities | active |
| `docs/gate-minimality/p3c-puiseux-singularity-character-p3-closure.md` | Active P3.c mathematical core | live |
| `docs/gate-minimality/p3-pipeline-integration-closure.md` | P3 assembly dependency chain | active |
| `docs/gate-minimality/a2-minimality-candidate-theorem.md` | A2 candidate theorem grade ceiling | active |

## Finding 2 — Interface boundary with HG-FND-002

The upstream boundary is now explicit.

`HG-FND-002` owns:

```text
proof-family generating function;
dominant singularity rho;
rational Puiseux exponent alpha in lowest terms.
```

`HG-FND-003` owns:

```text
chosen puncture;
local coordinate;
branch convention;
Puiseux expansion discipline;
decorated singular datum for downstream use.
```

The normalized surface must not re-own proof-family generating-function construction. It must start from `rho` and `alpha` as already identified data and then specify the local-puncture package.

## Finding 3 — Active mathematical core in P3.c

The active P3.c closure records the following A2 / arity-three data:

```text
C_3(x)=1+x C_3(x)^3
rho_3 = 4/27
C_3(rho_3)=3/2
alpha_3 = 1/2
```

It uses the scaled local coordinate:

```text
t = 1 - x/rho_3.
```

The principal branch expansion is:

```text
C_3(x)=3/2 - (sqrt(3)/2)t^(1/2)
       + (2/3)t
       + O(t^(3/2)).
```

This is the core candidate content for normalization into `HG-FND-003`, bounded as local Puiseux data and not as character-source data.

## Finding 4 — Boundary with HG-VOC-006

P3.c currently carries both Puiseux-singularity data and `chi_3` character-source analysis. Normalization must split these surfaces.

`HG-FND-003` may own:

```text
local square-root exponent;
local sign-change branch behavior;
principal branch convention;
Puiseux expansion at the selected puncture.
```

`HG-VOC-006` owns:

```text
chi_p;
roots of unity;
finite phase reductions;
mu_p character vocabulary;
source-identification of chi_3 in mu_3.
```

Therefore `HG-FND-003` must explicitly record that local square-root monodromy at `rho_3` is `mu_2`-type local data and is not the source of `chi_3 in mu_3`.

## Finding 5 — Boundary with HG-FND-006 and HG-FND-007

`HG-FND-003` does not own downstream monodromy, deck-character, or carry-cocycle surfaces.

Excluded from `HG-FND-003` normalization:

- finite monodromy / deck-character interpretation;
- lifted phase index;
- section-defect carry cocycle;
- `zeta_3` carry defect;
- `U(2)` correspondence;
- Deligne-unit or regulator-symbol refinements.

Those remain downstream candidate surfaces, especially `HG-FND-006` and `HG-FND-007`.

## Finding 6 — Anti-seed requirement

Existing `A-HG-FND-007` already records that undecorated singularities are not Puiseux data.

The normalization PR should either cite that entry or refine it with an `HG-FND-003`-specific boundary. Minimum failure modes to preserve:

- treating `rho` and `alpha` from `HG-FND-002` as decorated Puiseux datum without choosing puncture, local coordinate, branch convention, and expansion convention;
- treating local square-root monodromy at `rho_3` as the source of `chi_3 in mu_3`.

This preflight records the requirement only. It does not register a new anti-seed.

## Finding 7 — Proposed implementation file plan

Future normalization PR, not this preflight:

```text
docs/framework-foundations/HG-FND-003-puiseux-singular-datum.md
tests/test_hg_fnd_003_puiseux_singular_datum.py
```

Expected registry update in the future normalization PR:

```text
Move HG-FND-003 from candidate table to normalized Tier 1 table in docs/framework-core/distance-classification.md.
```

Expected claim-grammar effect, if authorized later:

```text
Reduce the HG-MTH-011 / HG-MTH-021 unresolved modulo chain by HG-FND-003 only;
do not discharge HG-VOC-006, HG-FND-006, or HG-FND-007.
```

## Non-actions

This preflight does not normalize `HG-FND-003`.

This preflight does not register new anti-seeds.

This preflight does not add tests.

This preflight does not promote `HG-VOC-006`, `HG-FND-006`, or `HG-FND-007`.

This preflight does not promote `HG-MTH-011`, `HG-MTH-018`, or `HG-MTH-021`.

This preflight does not identify local square-root monodromy at `rho_3` as the source of `chi_3 in mu_3`.

This preflight does not start P1 path-beta uniqueness or P2 candidate-list exhaustion.

This preflight does not authorize `A_n` extension.

This preflight does not authorize Heller-Einstein, Heller-Dirac, `yang-mills`, `np-program`, BSD, Heller-Winters, or `ns-program` work.

## Stop rule

After this preflight PR is opened and validated, halt.

Implementation of `HG-FND-003` normalization requires separate authorization.
