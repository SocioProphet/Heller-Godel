# v1/v2 Proof-Character Claim-Diff Ledger

Tracking issue: HG-ANNEAL-001 / #6

Status: active annealing ledger. This document is designed to preserve intellectual exploration while preventing theorem inflation. It does not delete speculative material. It classifies it so that theorem-core, conjecture, future-horizon, false-as-stated, and context material can all survive in the correct lane.

## 0. Source pair

The comparison is between:

- v1 / flat-only draft: `calculus invariant characters(2).pdf` and related flat-character material.
- v2 / expanded draft: `calculus invariant characters v2(2).pdf` and subsequent v2.1.x chat amendments.

The v1 draft functions as a regression oracle because it stayed closer to flat finite-order phase data and did not fully promote the regulator, Chern-class, moduli, or recognition-dynamics claims. The v2 draft is more ambitious and contains valuable material, but some strengthened claims exceed what has been constructed.

## 1. Claim-status vocabulary

Every strengthened claim receives exactly one primary status:

```text
proved
computed
definition
conjecture
future_horizon
false_as_stated
delete
```

Secondary route tags:

```text
theorem_core
corrected_core
future_horizon
context_only
quarantine
```

## 2. Delta table

| ID | Claim / topic | v1 status | v2 status | Delta | Decision | Required edit |
|---|---|---|---|---|---|---|
| D01 | Proof-class generating function `T_phi^sigma(x)` | Core construction, but flat/narrow | Core construction retained | Stable core | definition / theorem_core | Keep, but define canonical fragment, normal forms, and statistic explicitly. |
| D02 | Calculus invariance | Presentation-invariance asserted for proof classes | Still asserted, sometimes too strongly | Needs canonicalization | conjecture/definition boundary | State: invariant after translation to canonical eta-long beta-normal de Bruijn forms and fixed statistic. |
| D03 | Statistic invariance | Under-discussed / implicit | Later falsified by statistic examples | Strengthened then corrected | false_as_stated for naive invariance | Keep statistic-relative formulation; add admissible-statistic robustness as open problem. |
| D04 | Normal forms up to alpha/beta/eta | Present but imprecise | Still imprecise in places | Needs representation convention | definition | Use `alpha-classes of eta-long beta-normal forms` or `canonical beta-eta representatives`; do not mix. |
| D05 | Singularity exponent extraction | Dominant exponent used | Catalan and algebraic cases require Puiseux channels | Needs correction | corrected_core | Define exponent as selected leading nonanalytic/singular Puiseux channel after analytic germ separation. |
| D06 | `chi_p` as character | Flat phase map / finite-order character | Called character globally | Overstates outside no-carry regimes | definition with qualification | Use `phase map` or `finite phase character`; strict character only in no-carry regime. |
| D07 | Prime-indexed family | Sometimes treated adelically | Later repaired to prime-indexed family | Needs locked wording | definition | Define `(chi_p)_p in product_p mu_p`; do not write convergent product in U(1). |
| D08 | Finite seed basis `P_13` | Not present or less explicit | Introduced as computational truncation | Valuable addition | computed/definition | Keep as executable fingerprint, not full invariant. |
| D09 | No-carry multiplicativity | Flat multiplicativity present | Retained with carry condition | Stable if scoped | proved under hypotheses | State exact hypotheses: selected exponent channels add, no carry, product operation defined. |
| D10 | Carry identity `zeta_p` | May be implicit | Explicit closed form | Strong addition | computed / corrected_core | Keep. This is a real arithmetic identity and useful section defect. |
| D11 | `zeta_p` as 2-cocycle | Not central in v1 | Central in v2 | True but incomplete | proved/definition | Keep cocycle identity, but distinguish cocycle from nontrivial cohomology class. |
| D12 | `zeta_p` as nontrivial cohomological obstruction | Not claimed in flat-only form | Claimed / implied in v2 | Overreach | false_as_stated | Replace with: `zeta_p = delta q_p` under ordinary cochain freedom; class vanishes unless extra structure restricts gauges. |
| D13 | Heisenberg-style / nonabelian central extension | Not load-bearing in v1 | Present in v2 | Incorrect for displayed symmetric cocycle | false_as_stated | Remove. Future nonabelian claims require antisymmetric multiplier, ordered product, braid data, or richer exponent lattice. |
| D14 | Non-split abelian extension | Not established in v1 | Claimed in v2.1.x variants | Incorrect under unrestricted cochains | false_as_stated | Treat the extension as split under explicit cochain trivialization unless a restricted section category is specified. |
| D15 | Multi-shell Puiseux support | Not present or minor | Added as v2 extension | Strong if scoped analytically | theorem_core / proved analytic statement | Keep as analytic theorem about rational/algebraic functions; do not import recognition dynamics. |
| D16 | Shell-product theorem | Not in flat-only form | Added in v2.1.x | Valuable but needs cancellation caveats | proved under analytic hypotheses | Keep with local Puiseux support convolution and cancellation caveat. |
| D17 | Chain example | Calibration example | Sometimes treated as proof-theoretic fixed-phi case | Type/family mismatch | future_horizon / calibration | Mark as proof-family or analytic calibration unless a fixed type grammar is constructed. |
| D18 | Catalan example | Calibration example | Used as algebraic proof-class test | Needs proof-type grounding | future_horizon / calibration | Ground with a type such as `(A -> A -> A) -> A -> A` or label analytic calibration. |
| D19 | Chain x chain product `x^2/(1-x)^3` | Present in appendix material | Repeated in v2.1.2 | Algebraic error for ordinary product | false_as_stated | Ordinary product is `x^2/(1-x)^4`; triangular series needs separate same-index/symmetrized operation. |
| D20 | Regulator form `(2pi i)^-1 dlog T` | Future/flat limitation in v1 | Elevated in v2 | Useful local object, overpromoted globally | future_horizon with local definition | Keep local analytic `dlog` object; for algebraic functions pass to normalization/cover. |
| D21 | Regulator periods integer-valued | Not established | Claimed in v2 | False in branch cases as stated | false_as_stated | Period/residue can be rational around branch exponents; integral only under divisor/cover interpretation. |
| D22 | Chern-class lift | Absent / acknowledged missing | Claimed as regulator lift target | Underconstructed | future_horizon | Blocked on proof moduli, line bundle/local system, connection, curvature, and base map. |
| D23 | Base-relative flat visibility | Present in flat draft | Expanded in v2 | Valuable core/context bridge | theorem_core if flat-only | Keep for flat holonomy/local-system data; do not imply Chern lift. |
| D24 | `S^2`, `T^2`, Klein bottle comparison | Present in base-relative material | Expanded with torsion claims | Useful but needs coefficient discipline | future_horizon/context | Distinguish Hom(pi1,U(1)), H^1(M;U(1)), H^1(M;U(1) sheaf), H^2(M;Z). |
| D25 | Klein bottle as smallest `p=2` detector | Overstated | Repeated | Needs qualification | future_horizon/context | Say minimal useful closed surface with continuous flat direction plus 2-torsion, not absolute smallest torsion example. |
| D26 | `K_0(Types)` homomorphism | Premature | Repeated | Underdefined | future_horizon or definition if formalized | Define the category/semiring/Grothendieck relation or use `type-product monoid` language. |
| D27 | Non-disjoint vocabularies | Open | Sometimes minimized as inclusion-exclusion | Underconstructed | future_horizon | Shared atoms may create dependencies/unification constraints; do not claim simple inclusion-exclusion theorem. |
| D28 | Predicate logic / arithmetic extension | Acknowledged hard | Still aspirational | Beyond current fragment | future_horizon | Keep as future work only. |
| D29 | Recognition / cognition bridge | Not constructed | Mentioned in broader program | Underconstructed | future_horizon | Requires recognition kernels or semantic-energy dynamics linked to proof-character data. |
| D30 | Wythoff/Schwarz alignment | Not in v1/v2 core | Added by chat development | Useful precedent only | future_horizon/context | Preserve as grammar-regime theorem-shape, not theorem evidence. |
| D31 | Temporal Mechanics / S4 / ordering | External future-horizon | Potential bridge | Useful but not core | future_horizon | Route to recognition dynamics only after kernels exist. |
| D32 | AdS/CFT / holography vocabulary | Not in core | Appears as tempting analogy | Metaphor drift | quarantine | Use `projection/preimage discipline`; avoid holography unless explicitly non-claim. |
| D33 | Moufang / octonionic associator | External future-horizon | Tempting extension | Blocked on moduli/holonomy object | quarantine/future_horizon | Preserve as future horizon; no current proof-character claim. |
| D34 | Superconductivity / Fermi-Bose | External rescued material | Tempting analogy | Not load-bearing | quarantine/context_only | Preserve separately; do not import into proof-character core. |

## 3. Immediate core corrections for v2.1.3

The corrected manuscript must make these edits before any broader bridge work:

1. Replace cohomological-obstruction language around `zeta_p` with section/coboundary language.
2. Remove `Heisenberg-style`, `nonabelian`, and `non-split` claims unless a new restricted-cochain or noncommutative structure is explicitly constructed.
3. Define local exponent through Puiseux singular channels.
4. Add canonicalization requirement to calculus invariance.
5. State statistic-relativity as part of the construction.
6. Fix chain product algebra.
7. Demote regulator/Chern-class to candidate local/future global lift.
8. Retain base-relative flat visibility but separate it from regulator claims.
9. Ground examples in proof grammars or label them analytic calibration examples.
10. Route Wythoff, Temporal Mechanics, S4, Moufang, AdS/CFT, superconductivity, and Fermi/Bose to future horizon or quarantine.

## 4. Principle

The exploration is preserved by classification, not by deletion. A claim that is not yet theorem-core remains alive as conjecture, future horizon, or quarantine with blockers. The only material to delete is material that is both false-as-stated and not useful after correction.
