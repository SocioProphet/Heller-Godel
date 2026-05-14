# V4 Readout Basis and Diagonalization

Status: **context / interpretive guardrail / not a current theorem dependency**.  
Scope: proof-character dynamics, finite phase channels, `mu_2` bridge artifacts, and future diagonal-lemma gates.

## 0. Purpose

This note imports the readout-basis distinction from the cipher / Latin-square experiment into the Heller-Godel proof-character lane.

The structural rule is:

```text
involution is not selectivity.
```

A coordinate-basis involution can flip a symbol, certificate, local phase, or finite character without aligning to the boundary direction that the theory is trying to read. A readout-basis involution is stronger: it flips the declared observable direction and leaves an auditable trace in the intended boundary coordinate.

## 1. Order-four guardrail

The correct order-four sign structure is the Klein four-group

```text
V4 = Z/2 x Z/2,
```

modeled as the additive group of `GF(4)`. The cyclic group `Z/4` is rejected for this purpose because it contains order-four elements and does not supply the all-involutive balanced readout structure required by the doctrine.

For this repository, the point is not to import a finite-geometry theorem as a new proof result. The point is to prevent a single observed `mu_2` sign from being overread as a full order-four symmetry.

## 2. Coordinate-basis certificates

A certificate axiom or local proof marker may behave like a coordinate-basis involution. It can be stable under a formal operation, reversible under a declared encoding, or compatible with a finite phase channel.

That does not imply selectivity for a target obstruction such as `O_Con(PA)`.

Safe statement:

```text
Certificate-style involutions may preserve local consistency or local phase structure,
but they do not by themselves align with the Con(PA) boundary direction.
```

Unsafe statement:

```text
A certificate involution moves Con(PA) or proves consistency strength.
```

The unsafe statement is forbidden unless a formal fixed-point or interpretability argument supplies the missing alignment.

## 3. Diagonal lemma as readout-basis mechanism

The diagonal lemma is the natural formal analogy for readout-basis alignment. It does not add another coordinate-level certificate. It constructs a sentence whose self-reference is aligned to the provability boundary:

```text
G <-> not Prov(<G>).
```

In the readout-basis language, `G` is not merely another vector in the coordinate basis. It is the formula whose observable direction is locked to the boundary being read.

This gives the right interpretation of any future D6-style gate:

```text
D5-style certificate additions: coordinate-basis involutions.
D6-style diagonal construction: candidate readout-basis alignment.
```

This is only an interpretation until formalized inside the repo's proof system.

## 4. Relation to the existing `mu_2` bridge artifact

The existing `mu_2` bridge artifact isolates a clean two-torsion test and explicitly treats canonicity as the anomalous seam. This note sharpens that seam:

```text
a `mu_2` sign detects one involutive channel;
a V4/GF(4) readout structure is needed to distinguish channels;
diagonalization is the proof-theoretic mechanism that can align the channel to a boundary direction.
```

Therefore, a finite sign channel is admissible evidence only for its declared finite channel. It is not evidence for a consistency-strength statement or a nonabelian obstruction unless the readout map is separately constructed.

## 5. Claim boundary

Permitted:

```text
- using the V4/GF(4) language as a structural guardrail;
- distinguishing coordinate-basis sign flips from readout-basis selectivity;
- treating diagonalization as the formal mechanism that may supply readout alignment;
- keeping the `mu_2` bridge as context until the encoding map is constructed.
```

Forbidden:

```text
- claiming progress on Con(PA);
- claiming that certificate axioms alone identify O_Con(PA);
- claiming that a single `mu_2` channel identifies a full V4 action;
- substituting cyclic Z/4 for the GF(4)/V4 readout structure;
- promoting this interpretive note into Paper I theorem content without proof obligations.
```

## 6. Future formalization gate

A future formal gate may promote this note only if it supplies:

```text
1. a declared proof grammar;
2. a declared coordinate basis;
3. a declared readout observable;
4. a diagonal or fixed-point construction aligning the observable to the target boundary;
5. a proof that the coordinate-basis certificate action commutes with the readout construction;
6. claim-boundary tests rejecting Con(PA) inflation.
```

Until those objects exist, this file remains context and governance, not theorem content.

## 7. Nonclaims

This note does not prove consistency of PA, does not move the Gödel incompleteness boundary, does not identify a new obstruction theory, and does not prove that the current finite phase characters have a canonical diagonal readout.

It records a discipline: sign involution is cheap; selective readout is the hard object.