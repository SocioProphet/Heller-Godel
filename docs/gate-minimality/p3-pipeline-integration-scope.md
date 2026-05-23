# HG-MTH-012 — P3 Pipeline Integration Scope

Identifier: `HG-MTH-012`  
Status: scope document; obligation not closed.  
Owner: `SocioProphet/Heller-Godel`.  
Track: A2 gate-minimality, `HG-MTH-011`, proof-character pipeline at `p=3`.  
Claim level: method-grade as obligation specification; not theorem-grade.

## 1. Statement of obligation

P3 is the third of three promotion obligations recorded in `HG-MTH-011` (A2 minimality candidate-theorem).

P3 — Pipeline Integration. Closure requires attachment of the A2 minimality candidate-theorem (`HG-MTH-011`) to the `chi_p` / `zeta_p` / proof-character pipeline at `p=3`. Specifically: demonstration that the `U(2)=S(U(2) x U(1))` minimal admissible subgroup result corresponds to a specific identifiable object in the `chi_3` phase reduction or the `zeta_3` carry defect under composition. Closure of P3 lifts `HG-MTH-011` from method-grade-as-candidate to theorem-grade.

This document is the scope of that obligation, not its closure.

## 2. The pipeline as currently established

Heller-Godel's README gives the current defensible core as:

```text
restricted proof grammar + fixed canonical statistic
-> proof-class / proof-family generating function
-> Puiseux singularity data
-> finite phase reductions chi_p and chi_13
-> explicit mod-p carry defect zeta_p under composition
```

The repository currently exposes this pipeline as follows.

| Pipeline stage | Current HG surface |
| --- | --- |
| Restricted proof grammar | `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 2; candidate Tier-1 item `HG-FND-001` in `docs/framework-core/distance-classification.md` |
| Fixed canonical statistic | `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 2.2; candidate Tier-1 item `HG-FND-001` |
| Proof-class / proof-family generating function | `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 2.3; candidate Tier-1 item `HG-FND-002` |
| Puiseux singularity data | `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 4; candidate Tier-1 item `HG-FND-003` |
| Finite phase reductions `chi_p` and `chi_13` | `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 5; candidate Tier-2 item `HG-VOC-006`; executable arithmetic in `src/heller_godel/phase_characters.py` |
| Explicit mod-`p` carry defect `zeta_p` | `docs/manuscripts/calculus_invariant_characters_v2_1_3.md`, Section 6; executable carry table and carry cocycle checks in `src/heller_godel/phase_characters.py` |

`calculus_invariant_characters_v2_1_3.md` exists in `docs/manuscripts/` and is the current manuscript-level pipeline surface. The finite arithmetic layer exists in `src/heller_godel/phase_characters.py`; it includes rational exponent normalization, phase index, `p`-primary projection, prime reduction, section-defect carry, carry tables, and carry cocycle identity checks.

The inspection did not find a separate dedicated `chi_3` / `zeta_3` attachment document. Therefore P3 currently attaches to the general `chi_p` / `zeta_p` surfaces, specialized to `p=3`, unless a later PR creates a narrower `chi_3` or `zeta_3` artifact.

## 3. The A1 instantiation as paradigm

The A1 fixture is the worked `p=2` paradigm for the pipeline. It is a paradigm, not an automatic transfer rule.

| Pipeline abstraction | A1 instance at `p=2` |
| --- | --- |
| Restricted proof grammar | Typed witness grammar for the A1 fixture |
| Fixed canonical statistic | Catalan coefficients `C_n = binom(2n,n)/(n+1)` |
| Proof-class generating function | `C(x) = (1 - sqrt(1-4x))/(2x)` |
| Puiseux singularity data | Branch point at `x = 1/4`, exponent `1/2` |
| Finite phase reduction `chi_p` | `chi_2`, interpreted in the A1 fixture as Stokes multiplier `-1` |
| Mod-`p` carry defect `zeta_p` | `zeta_2 = -I in Spin(3) ~= SU(2)` in the A1 fixture notation |

P3 closure requires producing the analogous `p=3` instance and showing that the `U(2)=S(U(2) x U(1))` minimality result of `HG-MTH-011` corresponds to a specific object in that instance.

## 4. The p=3 attachment question, decomposed

P3 decomposes into four sub-obligations.

### P3.a — Restricted proof grammar at p=3

What is the proof grammar whose canonical statistic generates the `p=3` finite phase reduction `chi_3`?

At `p=2`, the paradigm is the typed witness grammar for the A1 fixture. At `p=3`, the natural candidate is a typed witness grammar for an A2 fixture, with witness data corresponding to the path-beta framework:

```text
SU(3), Z/3 center, cubic invariant Omega.
```

The sub-obligation is to specify this grammar.

### P3.b — Canonical statistic and generating function at p=3

What is the analog of the Catalan generating function at `p=3`?

Candidate structures include ternary-tree generating functions, 3-Catalan-like sequences, and Fuss-Catalan numbers:

```text
FC_n^(3) = 1/(2n+1) * binom(3n,n)
```

The sub-obligation is to identify the canonical statistic and its generating function.

### P3.c — Puiseux singularity and chi_3

What is the Puiseux singularity of the `p=3` generating function, and what is `chi_3` as the finite phase / Stokes multiplier at that singularity?

At `p=2`, the A1 paradigm uses the singularity at `x=1/4` with exponent `1/2`. At `p=3`, the natural candidate is a singularity whose finite phase involves a primitive cube root of unity in `mu_3`.

The sub-obligation is to identify the singularity location, the Puiseux exponent, and the value of `chi_3`.

### P3.d — zeta_3 carry defect and U(2) correspondence

What is `zeta_3` as a mod-3 carry defect under composition, and where does the `U(2)=S(U(2) x U(1))` minimal admissible subgroup of `SU(3)` appear in its structure?

At `p=2`, the carry-defect paradigm is recorded as `zeta_2 = -I` in the A1 fixture notation. At `p=3`, the sub-obligation is to identify `zeta_3` in an appropriate lift of the finite phase data and demonstrate the correspondence between `U(2)` and a specific feature of `zeta_3`.

## 5. The Heller-Einstein mediation route

P3 explicitly states that pipeline integration may be mediated by Heller-Einstein typed-interface ontology and the realization question under a separately authorized HE path.

The realization question relocated to Heller-Einstein under the typed-interface framing asks what type of morphism connects HG proof-character data to HD spectral / Hopf / Borel-side data, and whether that relation factors through HE projection-stochasticity. This is structurally a typed-interface question, which is exactly what HE was set up to host.

P3 closure may route through HE either by:

1. using the typed-interface ontology to formalize the `chi_3`-to-`U(2)` attachment as a typed morphism in `HE-INT-*`; or
2. using the projection-stochasticity / sufficiency hierarchy layer to explain how `U(2)` emerges as a sufficient projection in the `HE-SH-*` hierarchy; or
3. using both, if the interface and sufficiency conditions are both needed.

This is a route, not a requirement. P3 could also close purely within HG if a direct algebraic attachment between `chi_3` / `zeta_3` and `U(2)` is constructible.

Use of the HE route requires separate authorization beyond this scope PR. This document does not start HE development.

## 6. Grade declarations

| Object | Grade | Source |
| --- | --- | --- |
| `HG-MTH-011` (A2 minimality candidate-theorem) | method-grade as candidate | PR #77, merge SHA `bf3bf77cba9d8cb56d8379a3f7379d7357f70692` |
| P3 obligation scope (`HG-MTH-012`) | method-grade as scope | this PR |
| P3.a through P3.d sub-obligations | unopened | future scope-narrowing documents |
| Closure of P3 | would be theorem-grade per cited closure | not in this PR |

The closure of P3 itself, if achieved, would promote `HG-MTH-011` from method-grade-as-candidate to theorem-grade. This document does not perform that promotion; it specifies what would be required.

## 7. Non-claims

1. Does not close P3. This is a scope document.
2. Does not promote `HG-MTH-011` from method-grade-as-candidate to theorem-grade.
3. Does not specify the `chi_3` generating function, Puiseux singularity, or `zeta_3` carry defect; those are sub-obligations P3.b, P3.c, and P3.d to be opened in future PRs.
4. Does not authorize any Heller-Einstein PR. The HE mediation route is named as available but its use requires separate authorization.
5. Does not extend to `A_n` for `n >= 3`. The `p=3` case is the immediate scope; `A_n` is not in scope here.
6. Does not cross into `SocioProphet/yang-mills`. The proof-character pipeline is HG-internal; yang-mills is a downstream Clay consumer with its own non-claim discipline.
7. Does not authorize Lane VIII residue-hunt work. That track remains separately gated.
8. Does not claim that the Catalan / A1 paradigm carries over identically to `p=3`. The candidate structures in Section 4 are starting points for sub-obligations, not asserted analogs.

## 8. Future sub-obligation pathway

After this scope PR merges, the natural next PRs are the four P3.x sub-scope documents, one per sub-obligation:

```text
P3.a — proof grammar
P3.b — canonical statistic and generating function
P3.c — Puiseux singularity and chi_3
P3.d — zeta_3 carry defect and U(2) correspondence
```

They can be opened in any order, but the dependency structure is:

```text
P3.a -> P3.b -> P3.c -> P3.d
```

Each is a separately authorized track. None is opened by this PR.

## 9. Identifier and registry

This document assigns:

```text
HG-MTH-012
```

to the P3 pipeline-integration scope obligation.

`docs/framework-core/claim-grammar.md` is the canonical identifier registry. It defines the `HG-{LAYER}-{NNN}` pattern and requires any PR adding an `HG-*` identifier to update the registry or `docs/framework-core/distance-classification.md` in the same PR. This PR therefore updates `docs/framework-core/claim-grammar.md` to register `HG-MTH-012`.
