# Anti-Seed: PFK Operational Failure Modes

Identifier: `PFK-AS-REGISTER-001 v1.0`  
Status: Active  
Claim level: operational anti-seed register; no mathematical claim promotion.

This register canonicalizes operational failure modes for the Proof Fabric Kernel. Entries are append-only modulo structural-elimination closure.

## A-PFK-OP-001 — Operator invocation is not evidence

A successful PFK operator invocation produces a typed, provenance-complete artifact. It does not by itself produce mathematical evidence for the result of the computation.

Manifestation: citing a PFK Event-IR trace as if it constituted empirical evidence about a Clay-program target.

Correct statement: the trace records that the operator ran with specific inputs and produced specific outputs. Interpretation of those outputs as evidence is the consuming Clay-program repo's responsibility, subject to that program's claim discipline and the Universal Bridge proof-transfer boundary.

## A-PFK-PROTOCOL-001 — Null-test passage is not theorem-grade

PrimeStatsProtocol N1/N2 null tests and S1/S2/S3 stability tests produce diagnostic evidence. Passing these tests means the empirical regularity survived declared falsifiers. It does not constitute proof.

Manifestation: citing N1+N2+S1+S2+S3 green status as proof of a mathematical claim about zeta, L-functions, Hodge, Yang-Mills, BSD, P vs NP, or any Clay-program target.

Correct statement: protocol passage licenses continued investigation and descriptive claims about the construction. It does not license theorem-grade assertions.

## A-PFK-PROTOCOL-002 — Window-shopping prevention

If a consumer runs the PrimeStatsProtocol over many window choices, base choices, or perturbation choices and reports only configurations where the regularity appeared, that is window-shopping.

Correct statement: the window schedule, base set, and perturbation set must be fixed in advance, and reports must include all declared configurations, including failures.

## A-PFK-SCHEMA-001 — Schema validity is not content validity

A claim-ledger row that passes schema validation is well-formed. It is not necessarily true, complete, or justified. Schema validation checks the envelope, not the content.

Manifestation: inferring mathematical correctness from green CI status alone.

Correct statement: green CI means the envelope is well-formed. Mathematical correctness is a separate domain review.

## A-PFK-SCHEMA-002 — Schema-version drift

Schemas evolve. A consumer pinning to PFK schema v1.0 cannot assume forward compatibility with v2.0 without explicit migration.

Manifestation: a Clay-program repo silently consuming the current `main` HEAD of Heller-Godel rather than a pinned commit.

Correct statement: Clay-program repos pin to a merged Heller-Godel commit in `DEPENDENCIES.md` and re-pin only after compatibility audit.

## A-PFK-VAL-001 — Validator green status is not audit completion

PFK validators check schema validity, dependency declarations, hash consistency, framework-citation resolution, and replay-metadata presence where implemented. They do not check that the claimed computation actually supports the mathematical interpretation.

Manifestation: treating CI green as complete audit.

Correct statement: validator green status is a precondition for audit, not a substitute for it.

## Cross-references to framework anti-seed

PFK anti-seed entries operate downstream of the framework anti-seed register at `docs/framework-core/anti-seed-framework.md`. They extend operational discipline under framework constraints.

In particular:

- Universal Bridge proof-transfer failure mode applies to all PFK invocations that consume `HG-MTH-005` method-grade analogies.
- Catalan / mu2 fixture non-promotion applies to `PFK-OP-040` invocations.
- Post-import canonicalization applies to all PFK content; source archives remain provenance after repository import.

## Versioning

This anti-seed register is `PFK-AS-REGISTER-001 v1.0`. Adding entries increments the minor version. Structural elimination of an entry marks it `CLOSED:` and increments the major version.
