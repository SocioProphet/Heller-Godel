# Spectral Boundary Grammar

## Equilateral Triangle Billiards as a Model of Lawful Recurrence

### Status

This note is a controlled bridge artifact for the Heller–Gödel / Lawful Learning / boundary-consciousness theory stack. It does **not** claim that quantum billiards, cognition, proof search, or governed agent runtimes are literally the same physical system. It isolates a reusable formal pattern:

```text
boundary constraints
-> admissible modes
-> spectral / arithmetic grammar
-> trace evidence
-> recurrence / replay / revival
```

The reference model is Doncheski and Robinett, *Quantum mechanical analysis of the equilateral triangle billiard: periodic orbit theory and wave packet revivals* (`quant-ph/0307063`). The paper is useful because the full chain is visible in one exactly solvable system:

```text
boundary
-> admissible eigenbasis
-> quadratic spectrum
-> periodic-orbit trace
-> wave-packet autocorrelation
-> revival invariant
```

Promoted cautiously into our language:

```text
policy/schema/trust boundary
-> admissible runtime or proof modes
-> lawful transition grammar
-> provenance/evidence trace
-> coherent replay or state revival
```

---

## 1. Core thesis

A boundary is not merely a wall. A boundary is a selector of lawful modes.

Once a boundary selects admissible modes, the system is no longer governed by unconstrained motion. It is governed by the arithmetic of the permitted mode grammar. In the equilateral triangle billiard, the hard-wall boundary selects a triangular-lattice spectral form:

\[
Q_{A_2}(m,n)=m^2-mn+n^2.
\]

That quadratic form controls the energy spectrum, the periodic orbit structure, the autocorrelation peaks, and the exact revival time. The billiard therefore gives a compact exact model of lawful recurrence under boundary constraint.

For this repository, the corresponding principle is:

> Governed systems become predictable only when their boundaries induce stable admissible modes, and those modes carry an arithmetic strong enough to support recurrence, replay, and coherent reassembly.

---

## 2. The exact billiard pattern

The equilateral triangular infinite well has closed-form eigenstates and energy spectrum

\[
E(m,n)=\frac{\hbar^2}{2\mu a^2}\left(\frac{4\pi}{3}\right)^2(m^2+n^2-mn),
\qquad m\ge 2n.
\]

For \(m>2n\), the spectrum has two degenerate symmetry sectors: one odd and one even under reflection \(x\mapsto -x\). For \(m=2n\), there is a single non-degenerate state. This shows that the spectral object is not merely a scalar energy list. It is a symmetry-graded admissible basis.

The hard-wall boundary condition determines the domain of the Hamiltonian. The parity sectors determine which modes survive under folding. In the half-triangle, the odd sector vanishes along the bisector and therefore already satisfies the new hard-wall boundary. The half-triangle is not an arbitrary smaller system; it is a quotient/subsector of the full system.

General lesson:

> Lawful reduction is symmetry-sector restriction, not arbitrary truncation.

---

## 3. Folding and quotient discipline

The paper’s folding logic gives an exact model for admissible reduction. If a mode already vanishes along a proposed fold boundary, then imposing that boundary does not invent a new mode law; it selects a lawful subset of the existing eigenbasis.

This is directly relevant to governed runtimes.

A policy-restricted runtime should not be a hacked-down copy of the unrestricted runtime. It should be a lawful sector of the larger runtime, defined by admissibility conditions that can be verified at the boundary.

In billiard language:

\[
\text{full triangle}\rightarrow \text{odd parity sector}\rightarrow \text{half-triangle billiard}.
\]

In runtime language:

\[
\text{full capability space}\rightarrow \text{policy-admissible sector}\rightarrow \text{restricted runtime}.
\]

The fold is valid because the surviving modes satisfy the new boundary condition. The corresponding runtime reduction is valid only if the surviving actions satisfy the imposed policy boundary.

---

## 4. Spectral arithmetic and the \(A_2\) norm

The governing quadratic form

\[
Q_{A_2}(m,n)=m^2-mn+n^2
\]

is the triangular-lattice / Eisenstein-type norm. It appears first as spectral arithmetic and then reappears in orbit-length arithmetic.

Closed-path lengths can be written as

\[
d(p,q)=a\sqrt{3}\sqrt{p^2+pq+q^2}.
\]

This is the same lattice grammar in geometric form. The duality is the essential point:

\[
\text{spectral norm}\quad \leftrightarrow \quad \text{orbit recurrence norm}.
\]

This makes the equilateral triangle billiard an exact demonstration of boundary-induced arithmetic recurrence.

For our work, this is the model for a lawful substrate. We want domains where admissibility does not merely exclude illegal actions, but induces a stable arithmetic of recurrence, replay, and audit.

---

## 5. Periodic-orbit trace as evidence channel

Periodic orbit theory splits the density of states into a smooth Weyl term and an oscillatory term associated with classical closed paths.

The finite spectral transform

\[
\rho_N(L)=\sum_{n=1}^{N} e^{ik_nL}
\]

produces peaks at classical closed-path lengths.

Evidence principle:

> The spectrum carries memory of the lawful trajectories.

In the billiard, the length-domain trace reveals classical closed orbits. In a governed agent system, the provenance/event trace should reveal lawful operational recurrence. If the trace does not exhibit the expected recurrence, the system’s claimed mode grammar is wrong, the implementation has drifted, or the evidence channel is incomplete.

---

## 6. Autocorrelation and coherence return

The wave-packet autocorrelation

\[
A(t)=\langle \psi(t)\mid \psi(0)\rangle
\]

measures return to the initial state. At short times, peaks in \(|A(t)|\) occur where the corresponding classical packet would return to its initial phase-space location. This ties spectral evolution, boundary geometry, and orbit closure into a measurable return signal.

The governance analogue is replay fidelity:

\[
A_{\mathrm{runtime}}(t)=\mathrm{sim}(S(t),S(0)),
\]

where \(S(t)\) is a ledgered state bundle containing provenance, policy context, identity, active constraints, and event trace. A high return score means the system can reassemble coherent state after bounded exploration.

Operational analogy:

\[
\text{autocorrelation peak}\quad \leftrightarrow \quad \text{coherent replay / state revival}.
\]

---

## 7. Exact revival and fragility of symmetry

The triangular billiard has exact revivals for all wave packets at

\[
T_{\mathrm{rev}}=\frac{9\mu a^2}{4\hbar\pi}.
\]

The exactness depends on the integral quadratic structure of the spectrum. Special shorter revivals occur for zero-momentum packets initialized at special symmetry points, but those shorter revivals disappear when nonzero momentum breaks the required symmetry.

Systems lesson:

> Fast coherence cycles are symmetry-conditioned. They are not generic.

For engineered substrates, exact rollback, deterministic replay, audit recovery, or clean state reassembly require integral, schema-stable structure. If the domain becomes continuous, irregular, weakly constrained, or symmetry-breaking, exact revival becomes approximate at best.

---

## 8. Endomorphism grammar

The Appendix defines transformations

\[
T_{(p,q)}[m,n]=(pm-qn,(p-q)m-pn)
\]

with multiplicative action on the dimensionless energy:

\[
\epsilon(T_{(p,q)}[m,n])=(p^2-pq+q^2)\epsilon(m,n).
\]

Some maps correspond to visible foldings. Others preserve spectral arithmetic without an obvious simple geometric interpretation.

This distinction matters:

> Algebraic admissibility can exceed visual foldability.

For our theory, this is a warning against over-reliance on intuitive geometry. Some lawful transformations will be verified algebraically before they are visually interpretable. That is acceptable if the admissibility-preserving map is explicit and checkable.

---

## 9. Lawful Learning alignment

Lawful Learning treats inference as constrained optimization over an admissible manifold. The billiard provides a physical-mathematical reference model for this claim.

| Billiard term | Lawful Learning term |
|---|---|
| hard-wall boundary | constraint set |
| Hamiltonian domain | admissible parameter space |
| eigenbasis | lawful representational modes |
| parity sector | active constraint sector |
| spectral norm | invariant metric / admissible energy |
| periodic orbit | lawful optimization trajectory |
| autocorrelation | representation stability |
| exact revival | deterministic replay / convergence-reassembly |

The lesson is that constraints do not merely reduce freedom. Proper constraints create the arithmetic that makes recurrence possible.

---

## 10. Boundary-consciousness alignment

The boundary-consciousness thesis says that conscious content is a compressed, reportable, action-guiding surface reconstruction of a larger world-flow under finite attention.

The billiard adds a sharper model:

> Conscious content is an admissible mode pattern selected by a boundary, stabilized by recurrence, and recognized through return signals.

A conscious system does not merely receive sensory data. It admits certain modes of interpretation. Those modes disperse through experience and later reassemble as memory, identity, expectation, or reportability.

The revival analogy is useful but must remain controlled:

- A quantum wave packet revives because of unitary evolution and integral spectral arithmetic.
- A cognitive/agentic state revives only if its substrate preserves identity, provenance, constraints, and replayable transition grammar.

Thus, consciousness requires not just information, but recurrence-supporting lawful structure.

---

## 11. Heller–Gödel / proof-character alignment

The Heller–Gödel proof-character lane studies invariant-preserving traversal through proof spaces, symbolic regimes, and generating-function structures.

The billiard gives a model for proof-character dynamics:

| Billiard | Proof-character system |
|---|---|
| boundary domain | formal system / proof rules |
| admissible eigenmodes | normal proof forms |
| spectral arithmetic | proof-class generating function |
| orbit closure | rewrite/path recurrence |
| trace peaks | detectable proof-family signatures |
| revival | recovery of proof-character after transformation |
| folding | quotient by symmetry / proof-sector restriction |

A proof system is a billiard when its rules are walls and its proof objects are admissible modes. The central question becomes: what recurrence arithmetic is induced by the proof boundary?

This links directly to proof-generating functions and singularity exponents. A proof-class spectrum should not only count. It should expose recurrence, obstruction, and phase structure.

---

## 12. P vs NP / proof-search boundary

This note does not attack P vs NP. Its relevance is at the verification/generation boundary.

The billiard shows that when a domain has strong admissible arithmetic, recurrence and trace evidence become computable from the spectrum. In proof complexity, the analogous question is whether certificate spaces have lawful structure that can be verified, indexed, compressed, or replayed without solving the full discovery problem.

Safe claim:

> Spectral boundary grammar is a model for studying proof-search spaces as constrained recurrence systems, not a shortcut proof of complexity separation.

This is useful because it gives us a disciplined way to study proof artifacts as dynamic, traceable, admissibility-preserving objects.

---

## 13. SourceOS / Fog / SocioProphet alignment

A governed runtime is a billiard.

The walls are:

- schemas,
- policies,
- trust boundaries,
- identity constraints,
- capability constraints,
- data locality boundaries,
- provenance requirements,
- runtime admission rules.

Agents are not literally quantum wave packets. But their state trajectories can disperse across a bounded operational space and later require coherent reassembly.

The engineered analogue of revival is:

> the ability to restore a coherent state bundle containing identity, intent, provenance, active constraints, evidence lineage, and policy authorization after exploration or interruption.

This is why deterministic replay, signed receipts, content-addressed state, and policy-bound event traces are not auxiliary engineering details. They are the recurrence substrate.

---

## 14. Canonical pattern for reuse

The reusable pattern is:

1. Define the boundary.
2. Define the admissible domain.
3. Determine the mode grammar.
4. Extract the spectral/arithmetic invariant.
5. Identify recurrence classes.
6. Define the trace transform.
7. Measure return/coherence.
8. Classify symmetry-conditioned accelerated cycles.
9. Record fragility under perturbation.
10. Implement replay tests.

This should become a generic design checklist for lawful runtime, proof-dynamics, and consciousness-model artifacts.

---

## 15. Claim boundary

This note supports the following claims:

1. The equilateral triangle billiard is an exact model of boundary-induced spectral recurrence.
2. Its governing quadratic form is naturally read as triangular-lattice / \(A_2\)-type arithmetic.
3. Folding provides a disciplined example of symmetry-sector restriction.
4. Periodic-orbit traces provide evidence of classical recurrence encoded in the quantum spectrum.
5. Exact revivals require integral spectral structure.
6. Shorter revivals are symmetry-conditioned and fragile.
7. These features provide a reusable formal analogy for governed recurrence in learning, proof dynamics, and agent runtimes.

This note does not claim:

1. that cognition is literally a quantum billiard;
2. that agent systems are unitary quantum systems;
3. that spectral boundary grammar proves P vs NP;
4. that all governed systems have exact revivals;
5. that visual folding exhausts lawful algebraic transformations.

---

## 16. Next implementation targets

### Target A: theory-stack integration

Use this note as a worked reference model inside the Lawful Boundary Consciousness stack.

### Target B: formal object

Define a minimal abstract structure:

\[
\mathcal{B}=(\Omega,\partial\Omega,D(H),\mathcal{M},Q,\mathcal{T},\rho,A,T_{\mathrm{rev}})
\]

where:

- \(\Omega\) is the domain;
- \(\partial\Omega\) is the boundary;
- \(D(H)\) is the operator domain;
- \(\mathcal{M}\) is the admissible mode set;
- \(Q\) is the spectral/arithmetic form;
- \(\mathcal{T}\) is the admissibility-preserving transformation grammar;
- \(\rho\) is the trace transform;
- \(A\) is the return/autocorrelation functional;
- \(T_{\mathrm{rev}}\) is the recurrence/reassembly invariant when it exists.

### Target C: runtime analogue

Define a governed runtime analogue:

\[
\mathcal{R}=(S,\partial S,\Pi,\mathcal{A},Q_R,\mathcal{T}_R,\rho_R,A_R,T_R)
\]

where:

- \(S\) is runtime state space;
- \(\partial S\) is policy/schema boundary;
- \(\Pi\) is the admission operator;
- \(\mathcal{A}\) is the admissible action/mode set;
- \(Q_R\) is transition cost or lawful-state metric;
- \(\mathcal{T}_R\) is the admissibility-preserving transition grammar;
- \(\rho_R\) is provenance/event trace transform;
- \(A_R\) is replay/coherence autocorrelation;
- \(T_R\) is replay or recovery period when present.

### Target D: first computable demo

Build a toy triangular-lattice state machine with:

- admissible states indexed by \((m,n)\);
- energy/cost \(Q_{A_2}(m,n)\);
- admissibility-preserving transformations \(T_{(p,q)}\);
- trace peaks over recurrence lengths;
- a simple packet dispersion/reassembly analogue.

This becomes the first computational proof-of-concept for spectral boundary grammar.

---

## 17. Closing statement

The equilateral triangle billiard is strategically valuable because it gives an exact, non-handwavy model of lawful dynamics under boundary constraint. It shows that boundary, symmetry, arithmetic, trace evidence, and recurrence can be one system.

That is the pattern we need across the whole estate.

Lawful systems are not made lawful by prose. They are made lawful when their boundaries select admissible modes, their modes induce computable invariants, their traces reveal recurrence, and their state can revive coherently under replay.
