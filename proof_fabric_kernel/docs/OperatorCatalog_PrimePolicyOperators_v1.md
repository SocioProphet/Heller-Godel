# Operator Catalog — Prime Policy Operators v1

Status: operational catalog seed plus v1.1 registry expansion.  
Claim level: operational substrate; no mathematical claim promotion.

## Existing canonical entries

The six canonical seed-tree entries remain unchanged:

| Identifier | Description | Category |
|---|---|---|
| `PFK-OP-001` | Event ingestion | C-LEDGER |
| `PFK-OP-010` | Phase-map operator | C-SPECTRAL |
| `PFK-OP-020` | Null-model operator | C-STAT |
| `PFK-OP-030` | Calibration operator | C-MEAN-FIELD |
| `PFK-OP-040` | Catalan / mu2 fixture operator | C-CHARACTER |
| `PFK-OP-050` | PrimeStatsProtocol operator family | C-STAT |

## Registry expansion — v1.1

The six canonical entries above are operator families. The following granular operators canonicalize specific computational primitives invoked by consumer-side apparatuses, including Heller-Winters PR #39 and future Clay-program migrations.

All entries are flat sequential identifiers under the same `PFK-OP-NNN` namespace. Category attribution and family relationships are explicit.

### PFK-OP-002 — pi(x) prime-counting

Family: `PFK-OP-030` Calibration  
Category: C-MEAN-FIELD  
Signature: `(x: int) -> (pi_x: int)`

Prime-counting function. For small windows, exact table/sieve/symbolic implementations are admissible; for large windows, implementations must declare their algorithm.

Invariants: integer-valued; monotone non-decreasing; `pi(x) = #{p <= x : p prime}`.

### PFK-OP-005 — Li(x) logarithmic integral

Family: `PFK-OP-030` Calibration  
Category: C-MEAN-FIELD  
Signature: `(x: float, precision_bits: int) -> (Li_x: float)`

Logarithmic integral baseline at declared precision.

Invariants: precision setting declared; numerical backend declared; tolerance declared before use.

### PFK-OP-031 — log-phase embedding

Family: `PFK-OP-010` Phase-map  
Category: C-SPECTRAL  
Signature: `(n: int) -> (phi: float)`

Computes `phi(n) = log(n) mod 2*pi`.

Invariants: `phi in [0, 2*pi)`; branch and base declared.

### PFK-OP-032 — mean resultant length R

Family: `PFK-OP-010` Phase-map  
Category: C-SPECTRAL  
Signature: `(phis: list[float]) -> (R: float)`

Computes `R = |N^-1 sum_j exp(i phi_j)|`.

Invariants: `0 <= R <= 1`; sample size declared; input phase-list content hash recorded.

### PFK-OP-051 — N1 random-phase null

Family: `PFK-OP-020` Null-model and `PFK-OP-050` PrimeStatsProtocol  
Category: C-STAT  
Signature: `(N: int, seed: int) -> (phis: list[float])`

Generates an i.i.d. uniform-phase sample of size `N` with declared seeded RNG.

Invariants: seed declared; RNG implementation declared; sample size preserved.

### PFK-OP-052 — N2 wheel-admissible null

Family: `PFK-OP-020` Null-model and `PFK-OP-050` PrimeStatsProtocol  
Category: C-STAT  
Signature: `(x_lo: int, x_hi: int, Q: int, seed: int) -> (phis: list[float])`

Generates phases from wheel-admissible integers in `[x_lo, x_hi]` for wheel modulus `M = product_{q <= Q} q`, optionally subsampled with declared seed.

Invariants: `gcd(m, M) = 1` for all sampled `m`; subsampling reproducible.

### PFK-OP-053 — S1 scale stability

Family: `PFK-OP-050` PrimeStatsProtocol  
Category: C-STAT  
Signature: `(statistic: callable, schedule: list[Window]) -> (per_window_results: list)`

Runs a statistic across a pre-declared geometric window schedule and reports every window.

Invariants: schedule fixed before invocation; all windows reported, including failures.

### PFK-OP-054 — S2 base / representation stability

Family: `PFK-OP-050` PrimeStatsProtocol  
Category: C-STAT  
Signature: `(statistic: callable, base_set: list[BaseSpec]) -> (per_base_results: list)`

Runs a statistic across a declared base or representation set.

Invariants: base set fixed before invocation; all bases reported.

### PFK-OP-055 — S3 perturbation stability

Family: `PFK-OP-050` PrimeStatsProtocol  
Category: C-STAT  
Signature: `(statistic: callable, perturbations: list[PerturbationSpec]) -> (per_perturbation_results: list)`

Runs a statistic under declared perturbations such as subsampling, additive noise, or window shift.

Invariants: perturbation set fixed before invocation; each perturbation declares reproducibility settings.

## Provenance of expanded entries

The granular entries canonicalize identifiers already emitted or forward-referenced in consumer-side work, especially Heller-Winters PR #39 (`75ce9c68eea01211ac5683c38773011be96e3f41`) and the downstream dependency declarations that follow it.

This PR makes those identifiers catalog-native rather than forward conventions.

## Anti-seed cross-references

| Operator | Primary anti-seed |
|---|---|
| `PFK-OP-002`, `PFK-OP-005` | `A-PFK-OP-001` — operator invocation is not evidence |
| `PFK-OP-031`, `PFK-OP-032` | `A-PFK-OP-001` |
| `PFK-OP-051`, `PFK-OP-052` | `A-PFK-PROTOCOL-001` — null-test passage is not theorem-grade |
| `PFK-OP-053`, `PFK-OP-054`, `PFK-OP-055` | `A-PFK-PROTOCOL-002` — window-shopping prevention |

## Versioning

This catalog is `PFK-OP-CATALOG-001 v1.1`. Adding operator entries is a non-breaking minor-version expansion for consumers that cite by identifier with merged commit pin.
