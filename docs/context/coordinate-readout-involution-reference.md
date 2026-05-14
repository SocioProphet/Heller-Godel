# Coordinate-Basis vs Readout-Basis Involution Reference

Status: **thin cross-repo reference / context only / not theorem content**.  
Canonical owner: `SocioProphet/systems-learning-loops`.

## Canonical KB reference

The canonical pattern is maintained at:

```text
SocioProphet/systems-learning-loops
kb/patterns/coordinate-basis-vs-readout-basis-involution.md
```

Canonical claim record:

```text
kb/claims/coordinate-basis-vs-readout-basis.yaml
```

Canonical source record:

```text
kb/sources/cipher-involution-experiment.yaml
```

## Local interpretation for Heller-Godel

For this repository, the pattern is only a guardrail:

```text
involution is not selectivity.
```

Certificate-style or phase-channel involutions may preserve local consistency, local phase structure, or finite monodromy. They do not by themselves align with a target boundary such as `Con(PA)` or any consistency-strength observable.

The diagonal lemma is the formal candidate mechanism for readout-basis alignment: it constructs a fixed point whose self-reference is aligned to the provability boundary. This is an analogy and a future formalization direction, not a current theorem claim in this repo.

## Nonclaims

This reference does not claim:

- consistency of PA;
- movement on `Con(PA)`;
- a new incompleteness theorem;
- a nonabelian obstruction theory;
- that a finite `mu_2` phase channel is already a diagonal readout;
- that the Part B cipher experiment measures proof-character dynamics.

## Follow-up hook

If a future `06_validation.md` or `option_d5_certificates.py` lane is restored or added, its D5 section should include the local statement:

```text
D5 certificate axioms are coordinate-basis involutions. Selectivity for the consistency boundary requires a diagonal/fixed-point readout construction, tracked as D6 or equivalent.
```
