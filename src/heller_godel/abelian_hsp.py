"""Classical witnesses for factoring as abelian HSP / period finding.

This module simulates the abelian-HSP mechanism behind Shor's factoring
reduction: factoring reduces to order-finding, order-finding is period-finding
for f_a(x) = a^x mod n, and Fourier analysis over a finite cyclic sampling
window exposes the period through the annihilator.

Reduction chain: factoring <= randomized order-finding = abelian HSP over Z;
Fourier sampling over the abelian dual recovers the hidden period in the
standard quantum algorithm.

Boundary guard: Fourier-on-the-wheel solves the abelian case, which is exactly
the easy case; the difficulty of P vs NP lives in the non-abelian world this
construction does not enter. The DFT here is a classical simulation witness and
does not provide a fast classical period-finder.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, sqrt
import cmath

from heller_godel.wheel_plancherel import (
    order_mod_by_multiplication,
    primorial,
    units_mod,
)


class RetryReduction(Exception):
    """Signal that Shor post-processing needs another base or sample."""


@dataclass(frozen=True)
class HidingFunction:
    """The hiding function f_a(x) = a^x mod n with its hidden period."""

    a: int
    n: int
    period: int

    def __call__(self, x: int) -> int:
        if self.n == 1:
            return 0
        return pow(self.a, x, self.n)


def order_finding_classical(a: int, n: int) -> int:
    """Naively compute ord_n(a) by search; this has no polynomial-time claim."""

    if n == 1:
        return 1
    if gcd(a, n) != 1:
        raise ValueError("a must be a unit modulo n")
    return order_mod_by_multiplication(a % n, n)


def shor_reduction(n: int, a: int, r: int) -> tuple[int, int]:
    """Recover nontrivial factors from a successful order-finding sample.

    This is only the polynomial-time classical post-processing step. Bad bases
    or bad periods raise RetryReduction rather than being treated as failures of
    the reduction.
    """

    if n <= 1:
        raise ValueError("n must be > 1")
    g = gcd(a, n)
    if 1 < g < n:
        return (g, n // g)
    if r % 2 == 1:
        raise RetryReduction("order is odd; choose another base")
    half = pow(a, r // 2, n)
    if half == n - 1:
        raise RetryReduction("a^(r/2) = -1 mod n; choose another base")
    p = gcd(half - 1, n)
    q = gcd(half + 1, n)
    factors = tuple(sorted({x for x in (p, q) if 1 < x < n}))
    if not factors:
        raise RetryReduction("post-processing did not produce a nontrivial factor")
    factor = factors[0]
    return (factor, n // factor)


def hiding_function(a: int, n: int) -> HidingFunction:
    """Return f_a(x)=a^x mod n and expose its period for finite tests."""

    return HidingFunction(a=a % n if n > 1 else 0, n=n, period=order_finding_classical(a, n))


def period_comb(period: int, Q: int, offset: int = 0) -> list[complex]:
    """Indicator of a period-r coset in Z/QZ."""

    if period < 1 or Q < 1:
        raise ValueError("period and Q must be positive")
    return [1 if (x - offset) % period == 0 else 0 for x in range(Q)]


def dft(signal: list[complex] | tuple[complex, ...], Q: int | None = None) -> list[complex]:
    """Classical unitary DFT over Z/QZ; this only simulates the QFT step."""

    values = list(signal)
    if Q is None:
        Q = len(values)
    if Q != len(values):
        raise ValueError("Q must equal len(signal)")
    root = -2j * cmath.pi / Q
    scale = 1 / sqrt(Q)
    return [
        scale * sum(values[x] * cmath.exp(root * k * x) for x in range(Q))
        for k in range(Q)
    ]


def dft_support(signal_hat: list[complex] | tuple[complex, ...], tolerance: float = 1e-9) -> tuple[int, ...]:
    """Return frequency indices with nonzero numerical support."""

    return tuple(k for k, value in enumerate(signal_hat) if abs(value) > tolerance)


def annihilator(period: int, Q: int) -> tuple[int, ...]:
    """Return H^perp for H=<period> in Z/QZ as frequency indices."""

    if period < 1 or Q < 1:
        raise ValueError("period and Q must be positive")
    step = Q // gcd(Q, period)
    return tuple(range(0, Q, step))


def annihilator_step(subgroup_step: int, Q: int) -> int:
    """Return the generator step of the annihilator of <subgroup_step>."""

    if subgroup_step < 1 or Q < 1:
        raise ValueError("subgroup_step and Q must be positive")
    return Q // gcd(Q, subgroup_step)


def continued_fraction_recover(c: int, Q: int, max_denominator: int) -> int:
    """Recover a candidate period denominator from c/Q."""

    if c == 0:
        return 1
    return Fraction(c, Q).limit_denominator(max_denominator).denominator


def recover_order_from_frequencies(a: int, n: int, Q: int, frequencies: tuple[int, ...]) -> int:
    """Recover and verify an order from deterministic Fourier peak candidates."""

    candidates: list[int] = []
    for c in frequencies:
        if c == 0:
            continue
        denom = continued_fraction_recover(c, Q, max(1, n))
        if denom not in candidates:
            candidates.append(denom)
    for candidate in candidates:
        if candidate >= 1 and pow(a, candidate, n) == 1:
            return order_finding_classical(a, n)
    raise RetryReduction("continued fractions did not recover a verified order")


def fourier_sample_period(a: int, n: int, Q: int) -> dict[str, object]:
    """Classically simulate Fourier localization for the hidden period.

    The function computes the true order by naive search to build a finite
    witness signal, then applies the DFT and continued-fraction recovery. It is
    a structural demonstration, not a fast classical factoring routine.
    """

    r = order_finding_classical(a, n)
    signal = period_comb(r, Q)
    transformed = dft(signal, Q)
    max_amp = max(abs(v) for v in transformed) if transformed else 0
    threshold = max_amp * 0.50 if Q % r else 1e-9
    frequencies = tuple(k for k, value in enumerate(transformed) if abs(value) >= threshold)
    recovered = 1 if r == 1 else recover_order_from_frequencies(a % n, n, Q, frequencies)
    return {
        "period": r,
        "frequencies": frequencies,
        "recovered_period": recovered,
        "amplitudes": transformed,
    }


def subgroup_character_exponents(period: int) -> tuple[int, ...]:
    """Character exponents of <a> ~= Z/rZ."""

    if period < 1:
        raise ValueError("period must be positive")
    return tuple(range(period))


def wheel_period_dft_support(a: int, n: int, Q: int) -> tuple[int, ...]:
    """Return DFT support for the period comb attached to <a> <= G_n."""

    period = order_finding_classical(a, n)
    return dft_support(dft(period_comb(period, Q), Q))


def wheel_p4_context() -> dict[str, int]:
    """Small crosslink to the HG-MTH-008.4 primorial wheel context."""

    p4 = primorial(4)
    return {"P4": p4, "unit_count": len(units_mod(p4)), "mu_exponent": 12}


def abelian_boundary_statement() -> str:
    return (
        "Fourier-on-the-wheel solves the abelian case, which is exactly the easy case; "
        "the difficulty of P vs NP lives in the non-abelian world this construction does not enter."
    )
