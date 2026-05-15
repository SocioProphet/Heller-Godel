# Catalan / mu_2 Canonical Reference Fixture

Stable identifier: `HG-EX-001`  
Distance tier: framework-method / fixture  
Citation grade: fixture-grade  
Status: doctrine active; executable reference implementation pending  
Anti-seed: `A-HG-MTH-002`

## Purpose

The Catalan / mu_2 fixture is the canonical cross-program apparatus-alignment test for the Heller-Godel framework.

It does not constitute progress on RH, GRH, Hodge, BSD, P vs NP, Yang-Mills mass gap, or Navier-Stokes.

It tests whether a downstream apparatus can reproduce the expected local singularity and finite phase data on a controlled toy object.

## Definition

The Catalan generating function is:

```text
T_C(x) = (1 - sqrt(1 - 4x)) / (2x)
```

with:

| Quantity | Value |
| --- | --- |
| dominant singular point | `rho = 1/4` |
| local Puiseux exponent | `alpha = 1/2` |
| canonical two-torsion phase | `chi_2 = -1` |

The canonical apparatus-alignment triple is:

```text
(rho, alpha, chi_2) = (1/4, 1/2, -1)
```

## Finite character table

Using the finite phase rule already studied in the active Heller-Godel phase-character stack, the expected floor-index values for small odd primes are:

| p | p alpha | floor(p alpha) | floor(p alpha) mod p | character |
| --- | --- | --- | --- | --- |
| 2 | 1 | 1 | 1 | `-1` |
| 3 | 3/2 | 1 | 1 | `exp(2*pi*i/3)` |
| 5 | 5/2 | 2 | 2 | `exp(4*pi*i/5)` |
| 7 | 7/2 | 3 | 3 | `exp(6*pi*i/7)` |
| 11 | 11/2 | 5 | 5 | `exp(10*pi*i/11)` |
| 13 | 13/2 | 6 | 6 | `exp(12*pi*i/13)` |

The `p = 2` row is the canonical mu_2 anchor.

## What this fixture licenses

This fixture licenses only apparatus-alignment statements of the form:

```text
This program's implementation reproduces the Heller-Godel Catalan / mu_2 reference triple.
```

It may support regression tests, finite-character sanity checks, and cross-repo fixture comparison.

## What this fixture does not license

This fixture does not license:

```text
Hodge progress.
RH or GRH progress.
BSD progress.
P vs NP progress.
Yang-Mills mass-gap progress.
Navier-Stokes progress.
Proof transfer between Clay domains.
A claim that mu_2 parity is a universal obstruction.
A claim that all framework rows are theorem-grade.
```

## Cross-program role

Current or intended consumers:

| Consumer | Expected use | Citation cap |
| --- | --- | --- |
| `SocioProphet/Heller-Godel` | active local fixture / phase-character stack | fixture-grade |
| `SocioProphet/hodge-program-proof` | apparatus-alignment check only | fixture-grade; no Hodge progress |
| `SocioProphet/np-program` | Catalan / mu_2 toy protocol alignment | fixture-grade; no P vs NP progress |
| `SocioProphet/Heller-Winters-Theorem` | possible RH-lane two-torsion sanity check | fixture-grade; no RH progress |
| `SocioProphet/yang-mills` | possible SU(2) parity analogy only | analogy / fixture-grade; no mass-gap progress |

## Implementation status

The executable reference implementation is intentionally not added in this bootstrap PR.

A later PR should add:

```text
examples/catalan-mu2/reference.py
examples/catalan-mu2/receipt.json
examples/catalan-mu2/README.md update
```

and connect the output to proof-fabric-kernel schemas once PFK is extracted.

## Provenance

The Catalan / mu_2 fixture is already part of the Heller-Godel active proof-character apparatus and appears in the repository's Paper I / appendices / tests surface. This document does not introduce the mathematics; it declares the cross-program citation boundary.
