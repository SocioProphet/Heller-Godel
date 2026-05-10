# Calculus-Invariant Phase Characters from Proof-Family Generating Functions

Revision: v2.1.3 working manuscript skeleton  
Status: annealed draft; theorem-core narrowed; future-horizon material preserved but not promoted.

## Abstract

For a restricted proof fragment, a canonical normal-form representation, and a fixed statistic \(\sigma\), proof-family generating functions

\[
T_\phi^\sigma(x)=\sum_{s\in \mathcal N_\phi} x^{\sigma(s)}
\]

provide analytic objects whose local singularity data can be studied by ordinary generating-function methods. This paper fixes a canonical statistic \(\sigma_C\) and treats the resulting construction as statistic-relative: different intrinsic statistics may produce different generating functions and different shell structures.

The local Puiseux singularity channels of \(T_\phi^\sigma\) yield finite phase reductions \(\chi_p\) and a finite seed-basis fingerprint \(\chi_{13}\) over \(\mathcal P_{13}=\{2,3,5,7,11,13\}\). In no-carry regimes the selected phase map is strictly multiplicative under the scoped product operation. In general strict multiplicativity fails by an explicitly computable mod-\(p\) carry term \(\zeta_p\).

The main correction of this revision is that the displayed carry term is not a nontrivial group-cohomological obstruction in the ordinary unrestricted cochain setting. If

\[
q_p(\alpha)=\lfloor p\alpha\rfloor \bmod p,
\]

then

\[
\zeta_p(\alpha,\beta)=q_p(\alpha+\beta)-q_p(\alpha)-q_p(\beta).
\]

Thus \(\zeta_p\) is a finite-resolution section defect, equivalently a coboundary under ordinary cochain freedom. It remains computationally meaningful, but it does not by itself establish a nonabelian extension, a non-split central extension, or a nontrivial cohomology class. Such structures require additional hypotheses or additional objects not constructed here.

A multi-shell extension records all relevant Puiseux exponent channels rather than only the dominant channel. For rational and algebraic generating functions, shell-product behavior is governed by local Puiseux-support convolution with analytic-term collection and coefficient-cancellation caveats.

Regulator, Chern-class, proof-moduli, recognition-dynamical, Moufang, and holographic interpretations remain future-horizon material. They are not theorem-core claims of this manuscript.

## 0. Claim-status discipline

Every substantive assertion in this manuscript should be read under one of the following statuses.

| Status | Meaning |
|---|---|
| Definition | A chosen object or convention. |
| Computed identity | An identity verified by direct symbolic or arithmetic computation. |
| Proposition | A proved claim under stated hypotheses. |
| Analytic theorem | A standard analytic-combinatorial theorem applied to scoped generating functions. |
| Conjecture | Plausible but not proved. |
| Future horizon | Preserved research direction blocked on missing objects. |
| Non-claim | Explicitly rejected interpretation. |

This revision is designed to preserve exploration while preventing theorem inflation.

## 1. Scope and non-scope

### 1.1 Scope

This paper studies analytic and finite phase invariants of proof families after the following choices have been fixed:

1. a restricted proof fragment \(\mathcal F\);
2. a canonical normal-form representation;
3. a statistic \(\sigma\) on alpha-classes of canonical normal forms;
4. a generating-function construction for the resulting family;
5. a selected local Puiseux exponent channel.

The core path is:

\[
\text{proof family}\to T_\phi^\sigma(x)\to \text{Puiseux shell data}\to \chi_p,\chi_{13},\zeta_p.
\]

### 1.2 Non-scope

This manuscript does not establish:

- a nonabelian obstruction theory;
- a nontrivial central-extension class from the displayed \(\zeta_p\);
- a completed regulator or Chern-class lift;
- a proof-moduli space;
- a recognition-dynamical operator;
- a cognitive theory of recognition;
- a Moufang or octonionic proof-character holonomy;
- an AdS/CFT or holographic duality.

These are routed to future-horizon documents only.

## 2. Proof-family generating functions

### 2.1 Canonical normal forms

Let \(\mathcal F\) be a fixed proof fragment. For this revision, the intended default is a simply typed lambda-calculus / implicational propositional fragment where normal inhabitants can be represented by alpha-classes of eta-long beta-normal de Bruijn lambda terms.

A stronger version of the paper should define \(\mathcal F\) completely. Until then, all examples that do not specify a fixed type grammar are analytic calibration examples rather than theorem-bearing proof-class examples.

### 2.2 Fixed statistic

Let

\[
\sigma:\mathcal N_\phi\to \mathbb Z_{\ge 0}
\]

be a statistic on alpha-classes of canonical normal forms. The construction is statistic-relative. When the statistic is left implicit, this manuscript uses \(\sigma_C\), the canonical constructor statistic.

A precise implementation must state whether variables/leaves are counted. This revision recommends:

\[
\sigma_C(s)=\#\lambda\text{-nodes}+\#\mathrm{application}\text{-nodes}+\#\mathrm{variable}\text{-leaves}.
\]

If a different convention is used, the convention must be explicitly stated and examples recomputed.

### 2.3 Definition

For a proposition or proof-family index \(\phi\), define

\[
T_\phi^\sigma(x)=\sum_{s\in\mathcal N_\phi} x^{\sigma(s)}\in\mathbb Z[[x]].
\]

When \(\sigma=\sigma_C\) is fixed, write \(T_\phi(x)\).

### 2.4 Calculus-invariance after canonicalization

**Proposition 2.1.** Fix a proof fragment, a canonical translation from each presentation calculus into eta-long beta-normal de Bruijn representatives, and a statistic \(\sigma\) on those representatives. Then \(T_\phi^\sigma(x)\) is independent of the source presentation calculus.

**Reason.** Each source calculus is first transported into the same canonical representation. The statistic is then applied after transport, not separately in each presentation. Under that convention, the indexing set and the statistic are presentation-independent.

**Boundary.** This proposition does not say that natural-deduction constructor count, sequent-calculus rule count, and combinatory-logic symbol count agree before canonicalization. It also does not say that different statistics produce the same generating function.

## 3. Calibration examples and proof-grounding obligations

### 3.1 Chain family

The chain series

\[
R(x)=\sum_{n\ge 1} n x^n=\frac{x}{(1-x)^2}
\]

is used as a rational calibration example. Unless a fixed proposition/type grammar is supplied, it should be treated as a proof-family series rather than a single fixed-proposition \(T_\phi\).

### 3.2 Catalan grammar

The Catalan generating function

\[
C(x)=1+xC(x)^2=\frac{1-\sqrt{1-4x}}{2x}
\]

is used as an algebraic calibration example. It can be grounded proof-theoretically by a type grammar such as

\[
C_A=(A\to A\to A)\to A\to A,
\]

with normal forms generated by

\[
T ::= x \mid b(T,T),
\]

where \(x:A\) and \(b:A\to A\to A\). A final manuscript must either include this grounding or label the Catalan example as analytic calibration only.

### 3.3 Chain product correction

If \(R(x)=x/(1-x)^2\), then ordinary generating-function multiplication gives

\[
R(x)^2=\frac{x^2}{(1-x)^4}.
\]

The triangular series

\[
\frac{x^2}{(1-x)^3}=\sum_{n\ge 0}\binom n2 x^n
\]

is not the ordinary Cauchy product \(R(x)^2\). It may arise from a distinct same-index, quotient, or symmetrized aggregation operation, but that operation must be separately defined.

## 4. Puiseux singularity channels

### 4.1 Local expansion

Let \(T(x)\) be rational or algebraic over \(\mathbb Q(x)\). At a singular point \(\rho\), set

\[
t_\rho=1-x/\rho.
\]

Locally write

\[
T(x)=A_\rho(t_\rho)+\sum_{\beta\in\mathcal A_\rho(T)} c_{\rho,\beta}t_\rho^\beta,
\]

where \(A_\rho\) is analytic and \(\mathcal A_\rho(T)\) records singular or nonanalytic Puiseux exponent channels relevant to the selected extraction.

The exponent used by \(\chi_p\) is a selected channel \(\beta\), not necessarily the leading term of the full local function.

### 4.2 Catalan warning

Near \(\rho=1/4\), the Catalan function has an analytic constant term plus a square-root singular correction. The exponent \(1/2\) belongs to the leading nonanalytic Puiseux channel, not to the full local germ as if the whole function were simply \(c(1-4x)^{1/2}\).

## 5. Prime-indexed phase fingerprints

### 5.1 Phase map

For a selected rational exponent channel \(\beta\) and prime \(p\), define

\[
k_p(\beta)=\lfloor p\beta\rfloor\bmod p
\]

and

\[
\chi_p^{(\rho,\beta)}(T)=\exp\left(2\pi i\frac{k_p(\beta)}{p}\right)\in\mu_p.
\]

Strictly speaking, \(\chi_p\) is a finite phase map. It is a strict character only in regimes where the scoped product operation and no-carry condition make it multiplicative.

### 5.2 Full prime-indexed family

The full prime-indexed fingerprint is

\[
\boldsymbol\chi(T)=(\chi_p(T))_{p\ \mathrm{prime}}\in\prod_p\mu_p.
\]

This is not interpreted as a convergent product in \(U(1)\).

### 5.3 Finite seed basis

The first finite observation basis is

\[
\mathcal P_{13}=\{2,3,5,7,11,13\}.
\]

For \(\beta\in\mathbb Q\), define

\[
\mathbf k_{13}(\beta)=(k_p(\beta))_{p\in\mathcal P_{13}}.
\]

Worked values:

\[
\mathbf k_{13}(-2)=(0,0,0,0,0,0),
\]

\[
\mathbf k_{13}(1/2)=(1,1,2,3,5,6).
\]

The seed basis is a finite computational truncation, not the full invariant.

## 6. Multiplicativity and the carry defect

### 6.1 No-carry regime

Suppose selected exponent channels \(\alpha\) and \(\beta\) compose additively under the scoped product operation. If

\[
\lfloor p(\alpha+\beta)\rfloor\equiv \lfloor p\alpha\rfloor+\lfloor p\beta\rfloor\pmod p,
\]

then

\[
\chi_p(\alpha+\beta)=\chi_p(\alpha)\chi_p(\beta).
\]

### 6.2 Carry defect

Define

\[
\zeta_p(\alpha,\beta)=\lfloor p(\alpha+\beta)\rfloor-\lfloor p\alpha\rfloor-\lfloor p\beta\rfloor\pmod p.
\]

Then

\[
\chi_p(\alpha+\beta)=\chi_p(\alpha)\chi_p(\beta)\exp\left(2\pi i\frac{\zeta_p(\alpha,\beta)}p\right).
\]

### 6.3 Cocycle identity

The carry term satisfies the cocycle identity

\[
\zeta_p(\alpha,\beta)+\zeta_p(\alpha+\beta,\gamma)
=\zeta_p(\beta,\gamma)+\zeta_p(\alpha,\beta+\gamma)\pmod p.
\]

This records associativity of addition at the finite phase-section level.

### 6.4 Coboundary correction

Let

\[
q_p(\alpha)=\lfloor p\alpha\rfloor\bmod p.
\]

Then

\[
\zeta_p(\alpha,\beta)=q_p(\alpha+\beta)-q_p(\alpha)-q_p(\beta).
\]

Thus \(\zeta_p\) is a coboundary in ordinary group cohomology when unrestricted cochains are allowed. It should be read as a section defect of the chosen finite-resolution phase map.

### 6.5 Non-claims

The displayed \(\zeta_p\) does not by itself establish:

- a nontrivial ordinary group-cohomology class;
- a non-split central extension;
- a nonabelian or Heisenberg extension;
- a nonassociative residue;
- a Moufang or octonionic structure.

Those claims require additional mathematical structure not present in this construction.

## 7. Multi-shell extension

### 7.1 Shell support

For each singular point \(\rho\), let \(\mathcal E_\rho(T)\) denote the local exponent support needed for product calculations, including analytic integer channels and singular/nonanalytic Puiseux channels.

The shell support is the collection

\[
\mathfrak S(T)=\{(\rho,\mathcal A_\rho(T))\}.
\]

Radius shells group singular points by \(|\rho|=r\).

### 7.2 Shell-product theorem

For rational or algebraic \(F,G\) with local Puiseux expansions, local exponent support of \(FG\) at \(\rho\) is contained in the convolution

\[
\mathcal E_\rho(F)+\mathcal E_\rho(G),
\]

with coefficient cancellations and analytic-term collection handled after convolution.

This is an analytic statement about generating functions. It is not a recognition-dynamical shell law.

### 7.3 Rational case

For rational meromorphic functions, the shell-product theorem reduces to the divisor law: zero and pole orders add under multiplication.

### 7.4 Boundary

No operator \(\mathcal L_\phi\), Hamiltonian, Laplacian, recognition kernel, or cognitive process is constructed here. Any claim relating Puiseux shell support to dynamical spectra is future-horizon material.

## 8. Base-relative flat visibility

### 8.1 Flat data only

Flat \(U(1)\)-local systems are classified by representations

\[
\operatorname{Hom}(\pi_1(M),U(1)).
\]

This should not be casually conflated with sheaf cohomology classifying line bundles or with integral Chern classes.

### 8.2 Examples

- On \(S^2\), flat holonomy is trivial because \(\pi_1(S^2)=0\).
- On \(T^2\), flat holonomy is visible through two commuting generators.
- On the Klein bottle, flat holonomy includes a continuous direction and a \(\mu_2\)-type torsion feature.

The Klein bottle should be treated as a useful base exhibiting continuous flat direction plus 2-torsion behavior, not as the absolute smallest possible 2-torsion detector.

## 9. Candidate regulator and global lift

### 9.1 Local analytic object

For rational \(T\),

\[
\omega_T=(2\pi i)^{-1}d\log T
\]

is a local analytic object recording divisor data.

### 9.2 Algebraic case

For algebraic \(T\), the correct setting is the normalization or a ramified cover on which \(T\) becomes single-valued. Branch exponents can produce rational residues before cover/divisor normalization, so integer-period claims require care.

### 9.3 Future global lift

A Chern-class lift requires:

1. a proof-moduli object;
2. a sentence-bundle or local system;
3. a connection;
4. a curvature form;
5. a base map \(M\to\mathcal M_{\mathrm{proof}}(\phi)\).

None of these is constructed here. The regulator/Chern program remains future horizon.

## 10. Future horizons and quarantined analogies

### 10.1 Future horizons

The following are preserved but not promoted:

- Wythoff/Schwarz symmetry grammar;
- projection chart vs preimage geometry;
- observer groupoids and proof moduli;
- \(S_4\) recognition diagnostics;
- Borsuk-Ulam boundary encoding;
- heavy-tail/no-mean falsification.

### 10.2 Quarantine

The following require separate construction before they can influence the proof-character manuscript:

- AdS/CFT or holographic duality language;
- Moufang or octonionic holonomy;
- superconductivity;
- Fermi/Bose complementarity;
- unified field theory claims;
- Heller-Winters bridge claims lacking exact theorem statement.

## 11. Summary of theorem-core

The theorem-core after this annealing pass is:

1. fixed statistic and canonical normal form;
2. proof-family generating function;
3. Puiseux channel extraction;
4. finite phase maps \(\chi_p\);
5. seed fingerprint \(\chi_{13}\);
6. no-carry multiplicativity;
7. carry defect identity;
8. carry coboundary correction;
9. multi-shell analytic support theorem for rational/algebraic functions;
10. flat base-relative visibility where scoped to local systems.

Everything else is future horizon or context.

## Appendix A. Regression obligations

The repository test suite must include:

- `test_carry_coboundary.py`;
- `test_chain_product.py`;
- `test_seed_basis.py`;
- `test_catalan_puiseux.py`;
- a future `test_claim_text_boundaries.py` preventing reintroduction of nonabelian/cohomological overclaims.

## Appendix B. Exploratory preservation rule

Exploratory material is not deleted merely because it is not theorem-core. It is routed. The allowed routes are:

- theorem core;
- corrected core;
- conjecture;
- future horizon;
- context only;
- quarantine;
- delete only if false-as-stated and not recoverable by correction.
