"""Finite phase and carry-defect utilities.

These routines implement the narrow, defensible arithmetic core of the
proof-character program. They intentionally treat zeta_p as a finite-resolution
section defect, not as a nontrivial cohomological obstruction.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Iterable, Tuple

P13: tuple[int, ...] = (2, 3, 5, 7, 11, 13)


def as_fraction(value: int | str | Fraction) -> Fraction:
    """Return value as a canonical Fraction."""
    if isinstance(value, Fraction):
        return value
    return Fraction(value)


def f_p(alpha: int | str | Fraction, p: int) -> int:
    """Finite-resolution section f_p(alpha)=floor(p*alpha) mod p."""
    a = as_fraction(alpha)
    return (p * a.numerator // a.denominator) % p


def k_vector(alpha: int | str | Fraction, primes: Iterable[int] = P13) -> tuple[int, ...]:
    """Return the finite residue vector (floor(p alpha) mod p)_p."""
    return tuple(f_p(alpha, p) for p in primes)


def zeta_p(alpha: int | str | Fraction, beta: int | str | Fraction, p: int) -> int:
    """Return the mod-p carry defect.

    zeta_p(alpha,beta) = floor(p(alpha+beta)) - floor(p alpha) - floor(p beta) mod p.
    """
    a = as_fraction(alpha)
    b = as_fraction(beta)
    return (f_p(a + b, p) - f_p(a, p) - f_p(b, p)) % p


def zeta_vector(
    alpha: int | str | Fraction,
    beta: int | str | Fraction,
    primes: Iterable[int] = P13,
) -> tuple[int, ...]:
    """Return the finite carry fingerprint (zeta_p(alpha,beta))_p."""
    return tuple(zeta_p(alpha, beta, p) for p in primes)


def is_zeta_coboundary(alpha: int | str | Fraction, beta: int | str | Fraction, p: int) -> bool:
    """Check the explicit coboundary identity for zeta_p."""
    a = as_fraction(alpha)
    b = as_fraction(beta)
    lhs = zeta_p(a, b, p)
    rhs = (f_p(a + b, p) - f_p(a, p) - f_p(b, p)) % p
    return lhs == rhs


def is_zeta_symmetric(alpha: int | str | Fraction, beta: int | str | Fraction, p: int) -> bool:
    """Check symmetry of the carry defect."""
    return zeta_p(alpha, beta, p) == zeta_p(beta, alpha, p)
