# Extended Heller–Gödel Future-Horizon Inventory

Status: future-horizon archive. This file preserves exploratory material that is useful to the program but not yet theorem-core. It is governed by `docs/governance/proof_falsification_infrastructure.md`.

## 1. Principle

Future-horizon material should be preserved, not discarded. But preservation is not promotion. A horizon item moves toward theorem-core only when the missing object is constructed and the claim becomes falsifiable.

Standard route:

```text
motivation -> missing construction -> bounded experiment -> falsifier -> promotion criterion
```

## 2. Regulator / Chern-class lift

### Motivation

The CIPC manuscript explored a regulator-style lift using

```math
omega_phi = (2 pi i)^(-1) d log T_phi.
```

The desired direction is to relate local analytic exponent data and finite phase shadows to integer or cohomological objects.

### Current status

`needs_formalization`.

### Missing constructions

- algebraic curve or normalization on which `T_phi` is single-valued;
- line bundle or local system;
- connection;
- curvature 2-form;
- proof-class moduli or base family;
- map from a base manifold into the relevant moduli object.

### Promotion criterion

A regulator/Chern claim can enter theorem-core only after a sentence-bundle or proof-family bundle is defined and a curvature class is actually constructed.

## 3. Proof-moduli / sentence-bundle object

### Motivation

Several future directions require a moduli object:

- regulator/Chern lift;
- Moufang or nonassociative holonomy;
- base-relative regime classification;
- recognition-dynamical operator families.

### Current status

`needs_formalization`.

### Missing constructions

- objects: propositions, proof classes, normal-form grammars, or deformation classes;
- morphisms: normalization maps, grammar transformations, proof equivalences;
- topology or site on the object;
- notion of family over a base manifold or parameter space.

### Promotion criterion

A minimal moduli object must support at least one nontrivial family and one computable pullback invariant.

## 4. Nonabelian / Heisenberg extension

### Motivation

Earlier prose considered a nonabelian central-extension interpretation of the carry defect.

### Current status

`false_as_stated` for the displayed symmetric carry cocycle under ordinary group cohomology; `future_horizon` if additional structure is added.

### Why current claim fails

The displayed carry term is symmetric and is a coboundary of the discretization cochain. Therefore it does not currently establish a nonabelian or nontrivial ordinary cohomological obstruction.

### Possible repair paths

- antisymmetric multiplier;
- two-coordinate exponent lattice with symplectic pairing;
- ordered/braided proof product;
- noncommutative product operation;
- restricted gauge group forbidding the trivializing cochain;
- categorical coherence where section choice is non-removable.

### Promotion criterion

Produce a concrete non-symmetric cocycle, commutator, or categorical obstruction with a test distinguishing it from the current coboundary.

## 5. Moufang / octonionic / nonassociative extension

### Motivation

The chat corpus explored whether binary carry defects are the wrong place to seek deeper residue, and whether ternary associators or Moufang loops provide a better future test.

### Current status

`future_horizon` / `needs_formalization`.

### Missing constructions

- proof-moduli or recognition-moduli object;
- holonomy assignment into a Moufang loop or nonassociative structure;
- ternary associator observable;
- falsifier showing whether holonomies reduce to associative behavior.

### Promotion criterion

Define an actual holonomy map and compute a nonzero associator on a named test family. If all associators vanish or reduce to associative behavior, the Moufang extension is not load-bearing.

## 6. Recognition dynamics / cognition bridge

### Motivation

The broader program wants proof-character invariants to eventually inform learning, recognition, and observer dynamics.

### Current status

`future_horizon`.

### Missing constructions

- recognition state space;
- dynamics not purely gradient if cycles are claimed;
- operator family whose spectrum can be compared with Puiseux shell support;
- observables linking proof-family invariants to recognition behavior.

### Important boundary

Pure gradient flow does not generically support periodic orbits. Any Lyapunov-cycle or shell-cycle claim requires non-gradient, forced, Hamiltonian, skew-coupled, or other non-potential dynamics.

### Promotion criterion

Construct a specific operator or dynamical system and show how a proof-family invariant predicts or constrains a measurable dynamical feature.

## 7. Spectral shell / chemistry analogy

### Motivation

The chat explored atomic/chemical shell metaphors for stabilization, valence, and recurrence.

### Current status

`future_horizon` / `context_only`.

### Safe statement

Analytic singular shells can be organized structurally, and some stabilization vocabulary may be suggestive.

### Unsafe statement

Proof or recognition dynamics literally have atomic shell structure.

### Promotion criterion

Define a quantitative shell law for proof-family GFs or an operator spectrum, then test whether shell composition obeys explicit selection rules.

## 8. Continued fractions / irrational return scales

### Motivation

Continued fractions provide intrinsic rational return scales for irrational rotations and quasi-periodic behavior.

### Current status

`future_horizon`.

### Missing constructions

- irrational parameter naturally arising from a proof-family or recognition dynamics;
- return-scale observable;
- continued-fraction sampling rule;
- comparison with prime-based phase sampling.

### Promotion criterion

Produce an example where continued-fraction convergents select a better or different finite observation basis than prime truncation.

## 9. Wythoff / Schwarz symmetry grammar

### Motivation

Wythoff/Schwarz gives a mature precedent for finite symbolic data determining a regime of geometric realization.

### Current status

`context_only` / `future_horizon`.

### Promotion criterion

Build a concrete grammar-regime classifier or parser that predicts rational/algebraic/D-finite behavior for proof-family GFs.

## 10. Projection / preimage discipline

### Motivation

Many HG invariants are shadows of richer objects. The program needs vocabulary for chart artifacts, section choice, and preimage geometry.

### Current status

`methodological` / `future_horizon`.

### Promotion criterion

Define a preimage object, projection map, section equivalence, and theorem distinguishing intrinsic from chart-dependent data.

## 11. BSD governance precedent

### Motivation

BSD work supplies a strong example of evidence gates, row-state discipline, hash manifests, and claim-tier separation.

### Current status

`context_only` for Heller–Gödel.

### Boundary

BSD does not provide proof evidence for Heller–Gödel theorem claims. It provides governance methodology.

## 12. Rule for future horizon work

Every future-horizon item must carry:

- missing object;
- falsifier;
- promotion criterion;
- explicit statement that it is not theorem-core.

If these cannot be named, the item belongs in exploratory notes only, not in the formal program ledger.
