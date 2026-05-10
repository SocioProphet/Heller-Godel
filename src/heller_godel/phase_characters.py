"""Finite phase-character arithmetic for the Heller-Godel programme.

This module intentionally models only the finite arithmetic layer that can be
regression-tested without pretending to mechanize Deligne cohomology itself.

Hierarchy captured here:

    rational Puiseux exponent -> finite monodromy index -> lifted phase index
    -> section-defect carry cocycle

Separately, a helper for the tame symbol records the regulator-symbol boundary
of a pair of units. Tests assert that this tame symbol is not the carry cocycle.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable


@dataclass(frozen=True)
class PhaseExponent:
    """Rational exponent reduced modulo integers.

    ``numerator`` and ``denominator`` encode the class of ``alpha`` in
    ``Q/Z`` as ``numerator / denominator`` with ``0 <= numerator < denominator``.
    The denominator is 1 exactly for the trivial finite monodromy character.
    """

    numerator: int
    denominator: int

    @property
    def is_trivial(self) -> bool:
        return self.denominator == 1 or self.numerator == 0

    @property
    def fraction(self) -> Fraction:
        return Fraction(self.numerator, self.denominator)


def normalize_exponent(alpha: Fraction | int | str) -> PhaseExponent:
    """Normalize a rational local exponent as a finite phase class in Q/Z."""

    value = Fraction(alpha)
    denominator = value.denominator
    residue = value.numerator % denominator
    if residue == 0:
        return PhaseExponent(0, 1)
    common = gcd(residue, denominator)
    return PhaseExponent(residue // common, denominator // common)


def lcm(values: Iterable[int]) -> int:
    result = 1
    for value in values:
        if value <= 0:
            raise ValueError("lcm inputs must be positive")
        result = result * value // gcd(result, value)
    return result


def common_level(*alphas: Fraction | int | str) -> int:
    """Least common branch-killing level for rational exponent classes."""

    return lcm(normalize_exponent(alpha).denominator for alpha in alphas)


def phase_index(alpha: Fraction | int | str, level: int | None = None) -> tuple[int, int]:
    """Return the finite character index at a given root-of-unity level.

    If ``alpha = a/N`` and ``level = L`` with ``N | L``, the index is
    ``A = a L / N`` so that the character value is represented by ``zeta_L^A``.
    """

    exponent = normalize_exponent(alpha)
    if level is None:
        level = exponent.denominator
    if level <= 0:
        raise ValueError("level must be positive")
    if level % exponent.denominator != 0:
        raise ValueError("level must be a multiple of the exponent denominator")
    return (exponent.numerator * (level // exponent.denominator)) % level, level


def multiply_indices(left: int, right: int, level: int) -> int:
    """Product of two finite characters represented by exponents modulo level."""

    if level <= 0:
        raise ValueError("level must be positive")
    return (left + right) % level


def p_primary_level(level: int, prime: int) -> int:
    """Return the exact p-primary divisor of ``level``."""

    if level <= 0:
        raise ValueError("level must be positive")
    if prime < 2:
        raise ValueError("prime must be at least 2")
    result = 1
    remaining = level
    while remaining % prime == 0:
        result *= prime
        remaining //= prime
    return result


def p_primary_projection(index: int, level: int, prime: int) -> tuple[int, int]:
    """Project a mu_level character to its p-primary component."""

    primary = p_primary_level(level, prime)
    if primary == 1:
        return 0, 1
    return index % primary, primary


def prime_reduction(index: int, level: int, prime: int) -> tuple[int, int]:
    """Reduce a finite character to prime order, when that prime divides level."""

    if level % prime != 0:
        return 0, 1
    return index % prime, prime


def section(residue: int, level: int) -> int:
    """Canonical section Z/L -> {0, ..., L-1}."""

    if level <= 0:
        raise ValueError("level must be positive")
    return residue % level


def carry(residue_left: int, residue_right: int, level: int) -> int:
    """Section-defect carry cocycle for 0 -> Z -> Z -> Z/L -> 0."""

    left = section(residue_left, level)
    right = section(residue_right, level)
    combined = section(residue_left + residue_right, level)
    return (left + right - combined) // level


def carry_cocycle_identity_holds(a: int, b: int, c: int, level: int) -> bool:
    """Check d carry = 0 for the normalized carry 2-cocycle."""

    left = carry(a, b, level) + carry(a + b, c, level)
    right = carry(b, c, level) + carry(a, b + c, level)
    return left == right


def holonomy_index(character_index: int, level: int, winding: int) -> tuple[int, int]:
    """Holonomy of a pulled-back finite local system along a winding class."""

    if level <= 0:
        raise ValueError("level must be positive")
    return (character_index * winding) % level, level


def tame_symbol_standard(
    valuation_f: int,
    valuation_g: int,
    h_f_0: complex = 1,
    h_g_0: complex = 1,
) -> complex:
    """Tame symbol under the convention (-1)^{v(f)v(g)} f^{v(g)} / g^{v(f)}.

    For f = w^A h_f and g = w^B h_g with h_f(0), h_g(0) nonzero, this is
    (-1)^{AB} h_f(0)^B / h_g(0)^A.
    """

    if h_f_0 == 0 or h_g_0 == 0:
        raise ValueError("analytic factors must be nonzero at the divisor")
    sign = -1 if (valuation_f * valuation_g) % 2 else 1
    return sign * (h_f_0**valuation_g) / (h_g_0**valuation_f)
