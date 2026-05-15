# Beilinson Regulator Output for Catalan and Motzkin (Mode-B Artifact)

Status: repo-grade workbench artifact; method-adjacent.  
Classification (Hodge Program lane): `hodge-method`. Explicitly not `core-hodge`, `hodge-arithmetic`, Hodge proof, or Hodge progress.  
Provenance: consolidated from Drive-side Mode-B session work (`HG_BR_001`) into repo-grade form for evaluation against the Hodge Program bridge requirements scaffold.  
Purpose: make the local Beilinson regulator output available as a repo-grade input for `HODGE-EVAL-001` in `SocioProphet/hodge-program-proof`.

## 1. Setup and notation

Let `phi` be a proof-class whose generating function `T_phi(x)` has dominant singularity at `x = rho` with local exponent `alpha`. Let `h` denote an auxiliary holomorphic unit, nonvanishing near the singular locus. Write

```text
w = (1 - x/rho)^{1/N}
```

for the local branch-killing coordinate, and write the Puiseux singular unit in the form

```text
u = w^a h.
```

The local punctured-curve setup near `x = rho` produces `K_2` symbols whose Beilinson / Deligne regulator can be evaluated against the puncture loop `gamma` encircling the singularity.

| Object | Role in this artifact |
| --- | --- |
| `K_2` symbol `{f,g}` | local symbol on the punctured curve neighborhood |
| Beilinson / Deligne regulator `r_D` | maps the local symbol to a regulator pairing |
| Puncture loop `gamma` | loop around the dominant singularity |
| Auxiliary unit `h` | holomorphic nonvanishing factor producing the nonzero cross-symbol value |

## 2. Self-symbol vanishing

Claim:

```text
r_D({u,u})_gamma = 0.
```

Reason: `K_2` symbols satisfy the skew-symmetry relation that forces the self-symbol `{f,f}` into the 2-torsion / sign part of the symbol calculus. Under the regulator pairing used here, the self-symbol contributes trivially. Thus the self-symbol is not the meaningful Mode-B output.

This is the first correction from the Drive-side Mode-B session: the object of interest is not `{u,u}`. The meaningful local regulator output is the cross-symbol `{w^a,h}`.

## 3. Cross-symbol regulator

Claim:

```text
r_D({w^a,h})_gamma = -2*pi*a*log(|h(0)|).
```

Here `h(0)` denotes the value of the auxiliary unit at the singular point in the local `w` coordinate.

Derivation sketch: the regulator pairing for symbols on a punctured curve evaluates as the loop contribution of the logarithmic variation of the two units. For `f = w^a` and `g = h`:

1. `h` is holomorphic and nonvanishing, so its argument has no singular monodromy contribution around the small puncture loop;
2. `w^a` contributes argument variation `2*pi*a` around `gamma`;
3. the remaining local contribution is weighted by `log(|h(0)|)`;
4. with the convention used in this artifact, the sign is negative.

Therefore:

```text
r_D({w^a,h})_gamma = -2*pi*a*log(|h(0)|).
```

### Normalization caveat

The numerical factor and sign depend on the chosen Deligne / regulator normalization: real-Deligne versus integral-Deligne, the twist convention for `Z(2)`, and the regulator formula convention. The value above is recorded in the standard convention used by the Mode-B computation. Downstream theorem-grade use must verify the convention against the exact Esnault-Viehweg / Beilinson normalization being cited.

This caveat does not change the artifact's classification. It is a precision issue for theorem-grade comparison, not a bridge-primitive claim.

## 4. Specific values

### Catalan

For the Catalan generating function

```text
T_C(x) = (1 - sqrt(1 - 4x))/(2x),
```

the dominant singularity is `rho = 1/4` and the local exponent is `1/2`. In the local decomposition used by the Mode-B computation, the auxiliary unit has singular-point value

```text
h(0) = 2.
```

For `a = 1`, the cross-symbol regulator value is

```text
r_D({w,h})_gamma = -2*pi*log(2).
```

### Motzkin

For the Motzkin generating function

```text
T_M(x) = (1 - x - sqrt(1 - 2x - 3x^2))/(2x^2),
```

the dominant singularity is `rho = 1/3` and the local exponent is `1/2`. In the local decomposition used by the Mode-B computation, the auxiliary unit has singular-point value

```text
h(0) = 3/2.
```

For `a = 1`, the cross-symbol regulator value is

```text
r_D({w,h})_gamma = -2*pi*log(3/2).
```

### Motzkin verification caveat

The value `h(0) = 3/2` is carried over from the Drive-side Mode-B computation. It should be re-derived explicitly before any theorem-grade downstream use. For this repo-grade workbench artifact, it is sufficient to record the value and mark the verification obligation.

## 5. Coarseness diagnosis

The local regulator output depends only on the pair

```text
(a, |h(0)|).
```

This means the computation is informative but coarse. It distinguishes Catalan and Motzkin at the level of their local auxiliary-unit value, but it does not encode a global Hodge target, an algebraic cycle, or a motivic cohomology class.

This coarseness is useful for Hodge Program evaluation because it makes the bridge failure precise: the artifact produces a local regulator-symbol value, not the global structures required by the Hodge bridge scaffold.

## 6. What this output is and is not

### What it is

1. A local regulator-symbol computation on a punctured curve neighborhood of a dominant singularity.
2. A `hodge-method` artifact.
3. A repo-grade consolidation of Drive-side Mode-B work.
4. A fixed input for Hodge Program bridge evaluation.
5. A concrete local output:

```text
Catalan: -2*pi*log(2)
Motzkin: -2*pi*log(3/2)
```

### What it is not

1. Not an algebraic cycle.
2. Not a Hodge class.
3. Not a Hodge target datum.
4. Not a cycle realization datum.
5. Not a cycle-class equality.
6. Not Beilinson conjecture evidence.
7. Not regulator-conjecture closure.
8. Not a motivic cohomology construction.
9. Not a Deligne-to-Hodge bridge.
10. Not Hodge progress.

## 7. Inputs supplied for HODGE-EVAL-001

For evaluation against the four Hodge bridge primitives, this artifact supplies:

| Bridge primitive | What this artifact supplies | What it does not supply |
| --- | --- | --- |
| Hodge target datum `(X,k,alpha)` | Nothing | projective variety `X`; rational Hodge class `alpha` |
| Cycle realization datum `(Z_i,q_i,cl(Z_i))` | Nothing | algebraic cycles `Z_i` |
| Cycle equality obligation `alpha = sum_i q_i cl(Z_i)` | Nothing | the equality itself |
| Deligne-to-Hodge bridge obligation | a local Deligne / regulator-symbol output | bridge mapping local regulator output to global Hodge-theoretic data |

Expected evaluation result against this artifact alone:

```text
No valid Hodge target datum currently follows.
```

This is a valid outcome under the Hodge bridge requirements scaffold.

## 8. Active obstruction-registry references

This artifact is explicitly within the scope of these Hodge Program obstruction-registry entries:

| Entry | Reason |
| --- | --- |
| `OBS-HODGE-004` | Deligne cohomology to algebraicity promotion risk |
| `OBS-HODGE-007` | regulator symbol to regulator conjecture promotion risk |
| `OBS-HODGE-008` | Hodge-origin to Hodge-proof promotion risk |

The artifact respects those entries by remaining `hodge-method` and by preserving a strict nonclaim envelope.

## 9. Sources and citation level

| Reference | Use in this artifact |
| --- | --- |
| Milnor, *Introduction to Algebraic K-theory*, Princeton, 1971 | `K_2` skew-symmetry / self-symbol behavior |
| Beilinson, “Higher regulators and values of L-functions,” J. Soviet Math. 30 (1985), 2036-2070 | Beilinson regulator framework |
| Esnault-Viehweg, “Deligne-Beilinson cohomology,” in *Beilinson's Conjectures on Special Values of L-functions*, Academic Press, 1988, pp. 43-91 | Deligne-Beilinson cohomology, cup products, regulator-symbol conventions |
| Quillen, “Higher algebraic K-theory: I,” LNM 341, Springer, 1973, pp. 85-147 | higher algebraic `K`-theory background |

This bibliography is sufficient for a repo-grade `hodge-method` artifact. Page-level or theorem-level citations are required before theorem-grade downstream use.

## 10. Cross-references

Heller-Godel:

```text
docs/proofs/catalan_a1_realization_equivalence.md
docs/proofs/hodge_clay_target_gap_ledger.md
docs/governance/hodge_program_cross_repo_pointer.md
```

Hodge Program:

```text
SocioProphet/hodge-program-proof: docs/scaffolds/hodge_bridge_requirements_scaffold.md
SocioProphet/hodge-program-proof: docs/obstruction-registry.md
SocioProphet/hodge-program-proof: docs/registries/heller-godel-artifact-registry.md
```

## 11. Explicit nonclaim envelope

```text
No Hodge class.
No algebraic cycle.
No projective variety X.
No cycle equality.
No Deligne-to-Hodge bridge constructed.
No Beilinson conjecture evidence.
No regulator conjecture closure.
No promotion of regulator-symbol output to Hodge-grade material.
No claim that this artifact satisfies any of the four bridge primitives.
No generic odd-prime extension.
No proof-class moduli M_phi construction.
No theorem-facing claim.
```

## 12. Status as input for HODGE-EVAL-001

This artifact is repo-grade and citable as a Heller-Godel workbench artifact. It is suitable as input for `HODGE-EVAL-001` after the Hodge Program Heller-Godel artifact registry is updated to include it.

The Hodge Program evaluation should not treat this artifact as Hodge evidence. It should treat it as a `hodge-method` input whose expected bridge evaluation is negative with respect to the four Hodge bridge primitives.
