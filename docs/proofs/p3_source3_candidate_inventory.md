# Source_3 Candidate Inventory for the p = 3 Front

Status: candidate-inventory note.  
Scope: repo-only inventory and selection criteria.  
Date: 2026-05-15.  
Depends on:

```text
docs/proofs/p3_source_inventory.md
docs/source-captures/eisenstein_mu3_capture.md
docs/proofs/p3_vocabulary_scaffold.md
```

## Purpose

This note records the current repository state for possible `Source_3` candidates and defines selection criteria a future fixture-discovery PR must satisfy before choosing a concrete `p = 3` source object.

The note is intentionally repo-only. It does not list external candidate families. External mathematical sources may be explored later through the tightened Eisenstein / `mu_3` bibliography, but this inventory does not import or rank external candidates.

## Inventory method

This inventory follows the same low-claim pattern as `docs/proofs/p3_source_inventory.md`.

The repository has already recorded that no live indexed support surface was found for:

```text
Eisenstein
mu_3
μ_3
A_2
SU(3)
T_A2
T_{A_2}
odd-prime
odd prime
Conjecture 6.3
p=3
Z/p
Z/3
mu_p
root of unity
roots of unity
cyclic
finite-cyclic
prime
deck character
```

Since then, the repository has added:

```text
docs/source-captures/eisenstein_mu3_capture.md
docs/proofs/p3_vocabulary_scaffold.md
```

Those files supply source support and vocabulary, but they do not select a `Source_3` candidate.

## Current repo inventory result

No concrete `Source_3` candidate is currently selected in the repository.

The repository currently contains:

| Surface | Status |
| --- | --- |
| p = 3 absence/source inventory | Present |
| Eisenstein / `mu_3` source capture | Present |
| p = 3 vocabulary scaffold | Present |
| concrete `Source_3` object | Not present |
| tested `p = 3` fixture | Not present |
| theorem-facing `p = 3` claim | Not present |

This is the expected state after the preparatory ladder. It is not a failure condition.

## Selection criteria for a future Source_3 candidate

A future `Source_3` fixture-discovery PR should not select a candidate unless it explicitly addresses the following criteria.

### Criterion 1 — Nontrivial `mu_3` structure

The candidate must exhibit a nontrivial `mu_3` action or output.

It is not enough that the candidate admits a formal map to `mu_3`; the selected generator must evaluate to either `omega` or `omega^2`, not to the trivial value `1`, unless the PR is explicitly documenting a null witness.

### Criterion 2 — Identifiable finite-output map

The candidate must support a well-defined finite-output map

```text
Omega_3: Source_3 -> mu_3.
```

The PR must specify the selected generator `gamma_3` and the value `Omega_3(gamma_3)`.

### Criterion 3 — Eisenstein phase target compatibility

The finite target must align with the Eisenstein phase target from `docs/source-captures/eisenstein_mu3_capture.md`:

```text
omega = exp(2*pi*i/3)
mu_3 = {1, omega, omega^2}
```

The PR must not silently replace `mu_3` with the full Eisenstein unit group `mu_6` or with an unrelated cyclic target.

### Criterion 4 — p3 admissibility alignment

The candidate must address the six `p3-admissible` requirements from `docs/proofs/p3_vocabulary_scaffold.md`:

1. selected cyclic source;
2. specified generator;
3. map to `mu_3`;
4. selected nontrivial target value;
5. source-side reason for why this is the correct comparison source;
6. explicit classification as vocabulary, candidate, tested fixture, conjectural scaffold, or theorem-grade construction.

### Criterion 5 — Scope-envelope preservation

The candidate choice must not implicitly violate the p3 comparison boundary / nonclaim envelope.

In particular, the PR must explain why the candidate does not, merely by being selected, assert a generic `p` theorem, a closed `p = 3` fixture, an odd-prime dynamical target, a general encoding theorem, a Hodge-theoretic strengthening, an `A_n` generalization, or a gate minimality result.

## Nonclaim envelope for this inventory

This inventory does not claim:

1. no generic `p` theorem;
2. no closed `p = 3` fixture;
3. no odd-prime dynamical target;
4. no general encoding theorem;
5. no Hodge strengthening;
6. no `A_n` generalization;
7. no gate minimality claim;
8. no `Source_3` selection;
9. no claim that any inventoried candidate satisfies the scaffold primitives;
10. no claim that the selection criteria are necessary or sufficient.

The last item is important. These criteria are review gates for the next fixture-discovery PR, not a theorem about all possible `Source_3` objects.

## Bibliography pointer

The tightened Eisenstein / `mu_3` capture is the correct place to look before external candidate exploration:

```text
docs/source-captures/eisenstein_mu3_capture.md
```

That file currently contains formal bibliographic entries and a citation-use map, but not page-level citations. Before theorem-grade or fixture-grade `p = 3` work depends on external sources, the relevant page-level citations should be added for the exact editions used.

## Future PR contract

A future fixture-discovery PR should cite this inventory and state which selection criteria are being addressed.

At minimum, such a PR should include:

1. the proposed `Source_3` candidate;
2. the proposed generator `gamma_3`;
3. the finite-output map `Omega_3`;
4. the selected `mu_3` value;
5. the evidence level of the proposal: candidate, tested fixture, conjectural scaffold, or theorem-grade construction;
6. a scope-boundary paragraph preserving the ten nonclaims above unless the PR explicitly changes theorem state.

No D1 manuscript update is warranted from this inventory alone.
