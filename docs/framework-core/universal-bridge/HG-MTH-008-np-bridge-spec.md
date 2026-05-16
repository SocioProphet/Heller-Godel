# HG-MTH-008 — Universal Bridge: P vs NP / Complexity Domain Extension

Identifier: `HG-MTH-008`  
Distance tier: Framework-method (Tier 3)  
Status: Active after this PR  
Anti-seed: `A-HG-MTH-001`, `A-HG-MTH-002`, `A-HG-MTH-003`, `A-HG-MTH-005`

## Status under HG-MTH-005 and HG-MTH-006

`HG-MTH-005` established the Universal Bridge as method-grade structural analogy with factorization:

```text
B = (M, R, A)
```

where `M` is a mean-field or smooth-expected structure, `R` is a residual obstruction, and `A` is an apex obstruction package.

`HG-MTH-006` instantiated the Hodge domain. This document instantiates the P vs NP / complexity domain.

The bridge remains methodology-transfer only. It does not license proof transfer.

## P vs NP Clay statement

The Clay P vs NP problem asks whether:

```text
P =? NP
```

`P` is the class of languages decidable by a deterministic Turing machine in polynomial time. `NP` is the class of languages `L` for which there exists a polynomial-time verifier `V` and polynomial `p` such that:

```text
x in L iff exists w in {0,1}^{<= p(|x|)} with V(x, w) = 1
```

Cook-Levin identifies SAT as NP-complete: a polynomial-time algorithm for SAT would imply `P = NP`.

## NP bridge factorization

Let `L in NP` with verifier `V` and certificate-length polynomial `p`.

### Mean-field M

```text
M_NP(L) = {(x, w) : |w| <= p(|x|) and V(x, w) = 1}
```

The verifier acceptance region is the cheap structure: membership of `(x, w)` in `M_NP(L)` is decidable in polynomial time by definition.

The existential projection of this region is `L`:

```text
pi_1(M_NP(L)) = L
```

This is the NP mean-field: verification is efficient, while generation or decision may not be.

### Residual R

```text
R_NP(L) = inf{T : L in DTIME(T)} / poly(n)
```

The residual is the deterministic-time gap modulo polynomial slack: the gap between efficient verification and the best known or possible deterministic decision procedure.

The P vs NP question can be expressed as:

```text
exists L in NP such that R_NP(L) is not polynomial?
```

A positive answer gives `P != NP`. A negative answer for all `L in NP` gives `P = NP`.

This factorization is consistent with either possible resolution. It assumes neither.

### Apex obstruction A

The NP apex obstruction is a compiled triple of proof-technique barriers.

#### Relativization

Baker-Gill-Solovay showed that there are oracle worlds where `P = NP` and oracle worlds where `P != NP`. Any proof technique that relativizes cannot resolve P vs NP.

#### Natural proofs

Razborov-Rudich showed that broad classes of combinatorial circuit-lower-bound techniques are natural: constructive and large. Under standard cryptographic hardness assumptions, natural proofs cannot establish the lower bounds required for major separations such as `P != NP`.

This does not assume the cryptographic hypotheses as theorem premises for this bridge. It records the barrier's conditional structural content.

#### Algebrization

Aaronson-Wigderson refined relativization. Many techniques that evade simple relativization still algebrize. Algebrizing techniques also cannot resolve P vs NP.

#### Compiled obstruction

```text
A_NP in Obs_NP = Relativization ∪ NaturalProofs ∪ Algebrization
```

A proof of `P != NP` must produce a method escaping the relevant force of all three barriers. A proof of `P = NP` must produce a polynomial-time algorithm for an NP-complete problem. This spec does not provide either.

## Bridge axiom restated

The NP bridge licenses methodology transfer, never proof transfer.

Allowed:

- shared claim discipline;
- anti-seed transfer;
- shared-missing-machinery diagnosis;
- comparison of obstruction shapes across domains.

Forbidden:

- using RH, Hodge, YM, BSD, or Navier-Stokes methodology as a P vs NP proof;
- claiming a candidate NP program has escaped the barriers merely because it cites this bridge;
- treating toy fixtures or proof-character diagnostics as complexity-theoretic lower bounds.

## Shared missing machinery diagnosis

The RH, Hodge, and NP bridge surfaces share a structural diagnosis:

```text
Each problem lives below the resolution of the current toolbox.
```

For RH, the missing layer is an algebraic-geometric or trace-formula site with the right positivity to force zero-location discipline.

For Hodge, the missing layer is algebraic-cycle machinery that certifies rational `(p,p)` classes as algebraic.

For NP, the missing layer is a non-naturalizing, non-relativizing, non-algebrizing lower-bound or algorithmic method that sees computational structure invisible to the known barrier classes.

The bridge identifies a shared template: a problem is blocked not merely by missing computations, but by a missing class of proof apparatus. The same template appears across domains. The same tool is not asserted to work across domains.

## Candidate apex-tool programs

The following are diagnostic references only.

### Geometric Complexity Theory

Geometric Complexity Theory seeks lower bounds using representation theory and geometric invariant theory. It is structurally relevant because it deliberately aims outside the natural-proofs template.

Status: ongoing research program. No P vs NP separation is claimed here.

### Algebraic and interactive methods

Interactive proofs, arithmetization, and PCP-style methods demonstrate that some techniques can escape simple relativization. Their algebrizing behavior remains a barrier for P vs NP.

Status: method-grade reference only.

### Meta-complexity

Meta-complexity studies complexity properties of complexity problems themselves, including problems such as minimum circuit size. It is relevant because it may expose non-naturalizing structure.

Status: emerging research surface. No separation is claimed here.

## Consumer surface

Primary consumer:

```text
SocioProphet/np-program
```

Downstream citation form:

```text
[HG-MTH-008 @ <merged-Heller-Godel-commit-sha>]
```

A follow-up `np-program` PR should advance its Heller-Godel pin and cite `HG-MTH-008` in:

- `DEPENDENCIES.md`;
- scope documentation for the 10-lane structure;
- any document connecting polarization, gate-minimality target, singular-germ regime decomposition, proof-character generating functions, or Catalan/mu2 fixture work to the bridge.

Secondary consumer:

```text
HG-MTH-010 — Clay coverage taxonomy
```

When `HG-MTH-010` is drafted, it should compile this NP factorization into the cross-Clay taxonomy table.

## Relationship to np-program's existing apparatus

The np-program's 10-lane apparatus operates at method grade. It includes polarization, gate-minimality theorem-target work, singular-germ regime decomposition, proof-character generating-function work, and Catalan/mu2 fixture protocol.

Under this bridge, those tools are organization attempts around the NP apex obstruction. They are not evidence that any of the three barriers has been escaped.

The np-program's conservative 0–5% Clay proximity posture is preserved.

## Boundary

This document is method-grade structural specification. It does not:

- prove `P != NP`;
- prove `P = NP`;
- claim progress on P vs NP;
- certify that any candidate method escapes relativization, natural proofs, or algebrization;
- endorse GCT, algebraic methods, or meta-complexity as sufficient apparatus;
- transfer proof material from RH, Hodge, YM, BSD, or Navier-Stokes into complexity;
- promote np-program lane artifacts above their declared claim grades;
- assume the existence of strong pseudorandom generators as a premise.

## Anti-seed cross-references

| Identifier | Applies because |
|---|---|
| `A-HG-MTH-001` | Universal Bridge does not transfer proofs. |
| `A-HG-MTH-002` | Catalan / mu2 fixture is not Clay progress. |
| `A-HG-MTH-003` | Fixture-grade and theorem-grade citations must not be mixed. |
| `A-HG-MTH-005` | The triple barrier is cited diagnostically, not as a circumvention recipe. |

## Versioning

This is `HG-MTH-008 v1.0`. Minor clarifications use v1.x. Any revision changing the NP bridge factorization itself requires v2.0 and downstream migration review.
