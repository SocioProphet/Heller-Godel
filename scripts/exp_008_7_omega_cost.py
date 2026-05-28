#!/usr/bin/env python3
"""Generate HG-EXP-008.7 omega cost-scaling measurements.

The primary period metric is the exact naive order-walk operation count, computed
from local prime orders and CRT/lcm. This keeps the full synthetic sweep feasible
while measuring the cost that a naive classical period walk would incur.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from math import gcd, lcm, log, log2, prod
from pathlib import Path
import random
import time

from heller_godel.abelian_hsp import verify_period_candidate
from heller_godel.wheel_plancherel import PrimePower, is_prime, usp


BANDS = ("small", "medium", "large")
SMALL_ODD_PRIMES = (5, 7, 11, 13, 17, 19, 23, 29)
CSV_FIELDS = (
    "seed",
    "omega",
    "magnitude_band",
    "sample_index",
    "n",
    "primes",
    "log2_n",
    "phi_n",
    "a",
    "ord_a",
    "usp_ops",
    "usp_time_ms",
    "period_ops",
    "period_time_ms",
    "period_success",
    "period_retries",
    "arity_log_sum",
)


@dataclass(frozen=True)
class Measurement:
    seed: int
    omega: int
    magnitude_band: str
    sample_index: int
    primes: tuple[int, ...]
    n: int
    log2_n: float
    phi_n: int
    a: int
    ord_a: int
    usp_ops: int
    usp_time_ms: float
    period_ops: int
    period_time_ms: float
    period_success: bool
    period_retries: int
    arity_log_sum: float

    def row(self) -> dict[str, object]:
        return {
            "seed": self.seed,
            "omega": self.omega,
            "magnitude_band": self.magnitude_band,
            "sample_index": self.sample_index,
            "n": self.n,
            "primes": " ".join(str(p) for p in self.primes),
            "log2_n": f"{self.log2_n:.12g}",
            "phi_n": self.phi_n,
            "a": self.a,
            "ord_a": self.ord_a,
            "usp_ops": self.usp_ops,
            "usp_time_ms": f"{self.usp_time_ms:.12g}",
            "period_ops": self.period_ops,
            "period_time_ms": f"{self.period_time_ms:.12g}",
            "period_success": int(self.period_success),
            "period_retries": self.period_retries,
            "arity_log_sum": f"{self.arity_log_sum:.12g}",
        }


def primes_in_range(low: int, high: int) -> tuple[int, ...]:
    return tuple(n for n in range(low, high + 1) if is_prime(n))


def sample_primes(rng: random.Random, omega: int, band: str) -> tuple[int, ...]:
    if band == "small":
        if omega > len(SMALL_ODD_PRIMES):
            raise ValueError("omega exceeds small-prime fixture length")
        return SMALL_ODD_PRIMES[:omega]
    if band == "medium":
        pool = primes_in_range(1_000, 10_000)
    elif band == "large":
        pool = primes_in_range(10_000, 100_000)
    else:
        raise ValueError(f"unknown band: {band}")
    return tuple(sorted(rng.sample(pool, omega)))


def phi_squarefree(primes: tuple[int, ...]) -> int:
    return prod(p - 1 for p in primes)


def multiplicative_order_mod_prime(a: int, p: int) -> int:
    if gcd(a, p) != 1:
        raise ValueError("a must be coprime to p")
    x = 1
    for k in range(1, p):
        x = (x * a) % p
        if x == 1:
            return k
    raise ArithmeticError(f"order did not close modulo prime {p}")


def order_mod_squarefree(a: int, primes: tuple[int, ...]) -> int:
    order = 1
    for p in primes:
        order = lcm(order, multiplicative_order_mod_prime(a % p, p))
    return order


def choose_coprime_a(rng: random.Random, n: int) -> tuple[int, int]:
    retries = 0
    while True:
        a = rng.randrange(2, max(3, n - 1))
        if gcd(a, n) == 1:
            return a, retries
        retries += 1


def usp_operation_count(primes: tuple[int, ...]) -> int:
    """Deterministic proxy for structured-USP operations.

    Counts one CRT/factor coordinate step per prime plus one generator-search
    candidate check per factor, using the known fixture primes. This measures
    structured-output cost, not factoring difficulty.
    """

    ops = 0
    for p in primes:
        ops += 1  # factor coordinate emission
        generator = 2
        while generator < p:
            ops += 1
            if multiplicative_order_mod_prime(generator, p) == p - 1:
                break
            generator += 1
    return ops


def measure_instance(seed: int, rng: random.Random, omega: int, band: str, sample_index: int) -> Measurement:
    primes = sample_primes(rng, omega, band)
    n = prod(primes)
    phi_n = phi_squarefree(primes)
    a, retries = choose_coprime_a(rng, n)

    usp_start = time.perf_counter()
    cert = usp(n, factoring_oracle=lambda _: tuple(PrimePower(p, 1) for p in primes))
    if len(cert.factorization) != omega:
        raise AssertionError("USP certificate did not preserve omega")
    usp_time_ms = (time.perf_counter() - usp_start) * 1000
    usp_ops = usp_operation_count(primes)

    period_start = time.perf_counter()
    ord_a = order_mod_squarefree(a, primes)
    witness = verify_period_candidate(a, n, ord_a)
    period_time_ms = (time.perf_counter() - period_start) * 1000

    return Measurement(
        seed=seed,
        omega=omega,
        magnitude_band=band,
        sample_index=sample_index,
        primes=primes,
        n=n,
        log2_n=log2(n),
        phi_n=phi_n,
        a=a,
        ord_a=ord_a,
        usp_ops=usp_ops,
        usp_time_ms=usp_time_ms,
        period_ops=witness.candidate,
        period_time_ms=period_time_ms,
        period_success=witness.verified_identity,
        period_retries=retries,
        arity_log_sum=sum(log((2 * p) / ((p - 1) ** 3)) for p in primes),
    )


def generate_rows(seed: int, max_omega: int, sample_size: int, bands: tuple[str, ...]) -> list[Measurement]:
    rows: list[Measurement] = []
    for omega in range(1, max_omega + 1):
        for band in bands:
            for sample_index in range(sample_size):
                cell_seed = seed + omega * 10_000 + BANDS.index(band) * 1_000 + sample_index
                rng = random.Random(cell_seed)
                rows.append(measure_instance(seed, rng, omega, band, sample_index))
    return rows


def write_csv(rows: list[Measurement], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for row in rows:
            writer.writerow(row.row())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=8721)
    parser.add_argument("--max-omega", type=int, default=6)
    parser.add_argument("--sample-size", type=int, default=30)
    parser.add_argument("--bands", nargs="+", default=list(BANDS), choices=list(BANDS))
    parser.add_argument("--out", type=Path, default=Path("data/exp_008_7_results.csv"))
    args = parser.parse_args()

    rows = generate_rows(args.seed, args.max_omega, args.sample_size, tuple(args.bands))
    write_csv(rows, args.out)
    print(f"wrote {len(rows)} rows to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
