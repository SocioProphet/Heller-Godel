# HG-MTH-018 Theorem-Promotion Preflight

Issue: `#136`  
Target identifier: `HG-MTH-018`  
Target object: P3.c Puiseux singularity and `chi_3` at `p=3` closure  
Preflight base: `0f8c87516bae8aaf2f4781d1e3570a06608ab78f`  
Preflight status: scope assessment only  
Promotion status: not authorized by this document

## 1. Existing document content and current claim level

The current `HG-MTH-018` document is:

```text
docs/gate-minimality/p3c-puiseux-singularity-character-p3-closure.md
```

It currently declares:

```text
Claim level: method-grade modulo candidate-HG-FND-003 and candidate-HG-VOC-006.
```

The document already contains the four mathematical surfaces needed for theorem-grade promotion after dependency discharge:

1. the `p=3` critical point and dominant singularity data for `C_3(x)=1+xC_3(x)^3`;
2. the scaled local Puiseux exponent and principal-branch expansion;
3. the cubic-cover irreducibility and discriminant calculation identifying `S_3` monodromy;
4. the global `A_3` sheet-rotation source and manuscript phase-map agreement after declaring the positive generator `tau=(123)`.

No new identifier is required. Promotion, if later authorized, should be an in-place grade promotion of `HG-MTH-018`.

## 2. Proof components

The promotion theorem is assembled from already-normalized surfaces and existing verification tests. The proposed theorem does not introduce new mathematics; it changes the claim grade after dependency discharge.

| Component | Source object | Verification surface |
| --- | --- | --- |
| `rho_3=4/27`, `C_3(rho_3)=3/2`, `alpha_3=1/2` | `HG-FND-003` | `test_p3c_critical_point_data` |
| Puiseux coefficients `a^2=3/4`, `b=2/3` | `HG-FND-003` | `test_p3c_scaled_local_expansion_coefficients` |
| cubic discriminant `Delta=x(4-27x)` and `S_3` monodromy | `HG-VOC-006` | `test_cubic_discriminant_identity` |
| phase map `k_3(1/2)=1`, `chi_3=omega` | `HG-VOC-006` | `test_manuscript_phase_map` |

Promotion theorem candidate:

```text
HG-MTH-018 Theorem. The algebraic function C_3(x)=1+xC_3(x)^3 has dominant singularity rho_3=4/27 with C_3(rho_3)=3/2, Puiseux exponent alpha_3=1/2, and principal branch expansion

C_3(x)=3/2 - (sqrt(3)/2)(1 - x/rho_3)^(1/2)
       + (2/3)(1 - x/rho_3)
       + O((1 - x/rho_3)^(3/2)).

The monodromy group of x y^3 - y + 1 over Q(x) is S_3. The cyclic subgroup A_3 acts by positive sheet rotation tau=(123). Under the manuscript phase map k_3(1/2)=1, the selected character is chi_3(tau)=omega.
```

Scope of theorem candidate: the `p=3` Puiseux datum and `chi_3` character source identification, with declared positive-generator orientation convention.

## 3. Dependency check

The dependency ceiling has been discharged in the framework registry:

| Dependency | Current registry status | Recorded normalization SHA |
| --- | --- | --- |
| `HG-FND-003` | normalized Tier 1 | `20499fcaa535e5dd4701aaf42fa582173c3ba746` |
| `HG-VOC-006` | normalized Tier 2 | `86b4327b831c79b9ea58c2d56291dffeba0db50f` |

`docs/framework-core/distance-classification.md` records `HG-FND-003` as normalized Tier 1 and `HG-VOC-006` as normalized Tier 2.

`docs/framework-core/claim-grammar.md` already records that the `HG-MTH-018` candidate ceilings have been discharged, while keeping `HG-MTH-018` method-grade.

Therefore the promotion PR, if later authorized, would not need to normalize `HG-FND-003` or `HG-VOC-006`; it would only update the grade of `HG-MTH-018` and record the corresponding anti-seed and registry changes.

## 4. Anti-seed requirement

The promotion PR must add a new anti-seed entry:

```text
A-HG-MTH-002 — Treating HG-MTH-018 as theorem-grade without declaring the orientation convention
```

Failure mode:

```text
A downstream artifact cites HG-MTH-018 as theorem-grade chi_3 data without declaring the positive cyclic sheet generator tau=(123), or treats the primitive value omega as independent of orientation.
```

Correct boundary:

```text
HG-MTH-018 theorem-grade citation requires the declared positive generator tau=(123). Reversing the generator conjugates the selected character from omega to omega^2.
```

This anti-seed is mandatory because `HG-MTH-018` itself states that reversing orientation gives the conjugate value `omega^2`.

Implementation note: `A-HG-MTH-002` already exists as Catalan / `mu_2` anti-seed doctrine in the current anti-seed register. The promotion PR must not silently reuse that identifier for a different failure mode. It must either:

1. renumber the new orientation anti-seed to the next available `A-HG-MTH-*` identifier; or
2. first perform a governed anti-seed identifier cleanup if `A-HG-MTH-002` must be reserved for this promotion.

The preferred promotion-path recommendation is to use the next available anti-seed identifier and keep existing `A-HG-MTH-002` unchanged.

## 5. Distance-classification placement

`HG-MTH-018` should move into Tier 1 only as a theorem-grade MTH object, not as a framework-foundational `HG-FND-*` surface.

The promotion PR should add a new subsection under Tier 1:

```text
Theorem-grade MTH objects:
```

with row:

```text
| `HG-MTH-018` | P3.c Puiseux singularity and chi_3 at p=3 closure | theorem-grade; depends on normalized `HG-FND-003` and normalized `HG-VOC-006`; orientation governed by <anti-seed-id>; source: `docs/gate-minimality/p3c-puiseux-singularity-character-p3-closure.md` |
```

This avoids misclassifying a method identifier as an `HG-FND-*` surface while still allowing theorem-grade citation within its declared scope.

## 6. Claim-grammar updates required

A later promotion PR must update `docs/framework-core/claim-grammar.md` in three places:

1. Bootstrap active identifiers table:

```text
HG-MTH-018 ... theorem-grade within declared p=3 Puiseux datum and chi_3 source-identification scope; depends on normalized HG-FND-003 and HG-VOC-006; orientation convention required
```

2. The `HG-MTH-018` non-claims block:

Keep all non-promotion boundaries, but remove any wording that suggests `HG-MTH-018` itself remains method-grade only. Preserve:

- no `HG-MTH-011` promotion;
- no P3.d closure;
- no `zeta_3` / `U(2)` correspondence;
- no A1 retroactive promotion;
- no `A_n` theorem;
- no Clay claim;
- no Heller-Einstein authorization;
- no orientation-independence claim.

3. Example downstream citation block:

Update the `HG-MTH-018` row to theorem-grade only within the declared local theorem scope:

```text
[HG-MTH-018 @ <sha>] — P3.c Puiseux singularity and chi_3 at p=3 closure; citation grade: theorem-grade within declared p=3 Puiseux / chi_3 source-identification scope; licensed use: rho_3, alpha_3, principal Puiseux expansion, S_3 monodromy, A_3 positive-generator source, and chi_3(tau)=omega only.
```

## 7. Non-promotion checklist

The promotion PR must explicitly state that it does not:

1. promote `HG-MTH-011`;
2. promote `HG-MTH-016`;
3. promote `HG-MTH-020`;
4. promote `HG-MTH-021`;
5. close P3.d;
6. prove or extend to an `A_n` family;
7. authorize Heller-Einstein work;
8. cross into any Clay-program proof claim;
9. perform downstream repo work;
10. claim orientation independence of `chi_3`.

## 8. Promotion PR file set if authorized later

If this preflight merges and the promotion is subsequently authorized, the promotion PR should modify exactly four files:

1. `docs/gate-minimality/p3c-puiseux-singularity-character-p3-closure.md` — add formal theorem statement and proof block citing normalized `HG-FND-003` and `HG-VOC-006` SHAs.
2. `docs/framework-core/claim-grammar.md` — update `HG-MTH-018` grade and example citation block.
3. `docs/framework-core/distance-classification.md` — add `HG-MTH-018` under a Tier 1 theorem-grade MTH subsection.
4. `docs/framework-core/anti-seed-framework.md` — add the orientation-convention anti-seed under the next available non-conflicting `A-HG-MTH-*` identifier.

## 9. Preflight conclusion

`HG-MTH-018` is the correct first candidate for theorem-grade promotion beyond the Catalan/A1 fixture because its required proof components are already present, normalized, and bounded.

The promotion should be in-place under the existing identifier `HG-MTH-018`. No suffix identifier is allowed under the current `HG-{LAYER}-{NNN}` scheme.

This preflight does not authorize the promotion PR. It records the exact promotion boundary and the required file set for later authorization.
