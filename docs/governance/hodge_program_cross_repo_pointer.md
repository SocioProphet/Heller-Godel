# Hodge Program Cross-Repo Pointer

Status: operational governance note.  
Scope: cross-repo coordination only.  
Date: 2026-05-15.  
Target repo: `SocioProphet/hodge-program-proof`.

## Purpose

This note records the cross-repo relationship between `SocioProphet/Heller-Godel` and `SocioProphet/hodge-program-proof`.

Heller-Godel remains the theorem/proof workbench for finite-character, Deligne-unit, Catalan A1, p = 3 scaffolding, and local proof-fabric work. Hodge Program Proof is the Hodge-origin registry, anti-seed, obstruction, claim-ledger, and Clay-facing artifact fabric.

This note is operational. It does not change theorem state.

## Canonical Hodge Program tracking documents

Heller-Godel proof-fabric artifacts are tracked in `SocioProphet/hodge-program-proof` through:

```text
docs/intake/heller-godel-proof-fabric-intake.md
docs/registries/heller-godel-artifact-registry.md
docs/scaffolds/hodge_bridge_requirements_scaffold.md
```

These documents were added to the Hodge Program repository to classify Heller-Godel work by distance from the Hodge core and to prevent finite-character work from being promoted into Hodge proof/progress.

## Hodge Program classification of Heller-Godel

Heller-Godel is classified in the Hodge Program as:

```text
hodge-method
```

It is explicitly not classified as:

```text
core-hodge
hodge-arithmetic
Hodge proof
Hodge progress
```

Current interpretation: Heller-Godel provides method-adjacent proof fabric, Deligne-adjacent finite-character constructions, comparison diagrams, and governance artifacts. It does not currently provide algebraic cycles, rational Hodge classes, or a Hodge theorem.

## Controlling anti-seed

The controlling anti-seed for HG-to-Hodge promotion is:

```text
Finite phase characters, Deligne units, or Catalan A1 comparison diagrams must not be promoted into Hodge proof/progress.
```

This sentence should be treated as the cross-repo boundary between Heller-Godel method work and Hodge Program proof claims.

## When Heller-Godel should update Hodge Program

A future Heller-Godel PR should trigger a corresponding Hodge Program registry update if it adds or materially changes a proof-fabric artifact involving any of the following:

1. Deligne-unit or regulator-symbol structure;
2. finite monodromy / finite-character constructions with Hodge-facing relevance;
3. Catalan A1 theorem or fixture state;
4. p = 3 / odd-prime scaffolding that is intended to remain in the Hodge-facing runway;
5. Hodge / Clay target or gap ledgers;
6. cross-repo proof-fabric governance;
7. source packets, reconciliation ledgers, or evidence ledgers relevant to Hodge-facing interpretation.

If a Heller-Godel PR is purely local implementation, formatting, typo cleanup, or finite-character work with no Hodge-facing trajectory, a Hodge Program update is not required.

## Hodge bridge requirements scaffold

The Hodge Program bridge scaffold defines the Hodge-facing requirements for any future promotion attempt:

```text
Hodge target datum
Cycle realization datum
Cycle equality obligation
Deligne-to-Hodge bridge obligation
```

This Heller-Godel pointer does not duplicate those definitions. The source of truth is:

```text
SocioProphet/hodge-program-proof: docs/scaffolds/hodge_bridge_requirements_scaffold.md
```

No current Heller-Godel artifact is recorded as satisfying those bridge requirements.

## Validation posture

This document is a governance pointer. It should pass the standard Heller-Godel governance, topology, and proof-apparatus checks without changing any theorem adapter or claim status.

## Nonclaims

This pointer does not claim:

1. Hodge proof or Hodge progress from any Heller-Godel artifact;
2. automatic synchronization between Heller-Godel and Hodge Program;
3. that the Hodge Program registry is exhaustive of all Heller-Godel artifacts;
4. that any Heller-Godel artifact satisfies any Hodge bridge primitive;
5. that finite phase characters are Hodge classes;
6. that Deligne units are algebraic cycles;
7. that comparison diagrams are motives;
8. that p = 3 scaffolding is an odd-prime theorem.

## Future author checklist

When adding a new Heller-Godel proof-fabric artifact, ask:

1. Does this artifact change the Hodge-facing interpretation of Heller-Godel?
2. Does it change theorem state, fixture state, source support, or gap posture?
3. Does it belong in the Hodge Program artifact registry?
4. Does it require a new anti-seed block in Hodge Program?
5. Does it risk violating the controlling anti-seed above?

If the answer to 1, 2, or 3 is yes, open a corresponding Hodge Program update PR.

If the answer is no, record no cross-repo action.
