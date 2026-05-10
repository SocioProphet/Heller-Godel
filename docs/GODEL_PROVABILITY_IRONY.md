# Gödel, Provability, and the Heller-Godel Irony

This repository invokes Gödel carefully.

Gödel's first incompleteness theorem does not say that proof is useless. It says that any sufficiently expressive, effectively axiomatized, consistent formal system fails to prove every truth about its intended arithmetic model. The proof works by arithmetizing syntax: formulas, proofs, and proof-checking are encoded as natural numbers. A provability predicate is then represented inside arithmetic, and diagonalization constructs a sentence that asserts its own unprovability.

The Heller-Godel program studies the geometry of proof families without claiming to collapse truth into provability.

The irony is productive:

```text
Gödel shows that provability cannot exhaust truth.
Heller-Godel studies the analytic structure of provability itself.
```

The current technical path is:

```text
normal proof classes
-> generating functions
-> singularity data
-> finite phase reductions
-> carry defects under composition
```

This should be read as a study of the structure of derivability landscapes, not as an escape from incompleteness.

## Boundary

The program must preserve the distinction between:

- truth in an intended model,
- provability inside a formal system,
- normal proof enumeration,
- analytic invariants of proof families,
- and cognitive/observer projection metaphors.

A result about `T_phi^sigma(x)` is a result about a chosen proof grammar and statistic. It is not a result saying that all mathematical truth has been made internal to a formal theory.

## Working thesis

The defensible thesis is:

```text
Proof-normalization classes can have analytic and arithmetic structure.
That structure can be studied without denying Gödelian incompleteness.
```

This note should remain near the front of the repo because it prevents the central overclaim: treating a theory of proof-family invariants as a theory that defeats incompleteness.
