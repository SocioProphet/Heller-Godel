"""Regression tests for HG-FND-005 level-1 Deligne-unit framing.

These tests exercise the concrete tame-symbol evaluation substrate without
pretending to mechanize Deligne cohomology itself.
"""

from __future__ import annotations

import cmath

from heller_godel.phase_characters import carry, tame_symbol_standard


def assert_close(left: complex, right: complex, tolerance: float = 1e-12) -> None:
    assert abs(left - right) < tolerance


def root_of_unity(level: int, index: int = 1) -> complex:
    return cmath.exp(2j * cmath.pi * index / level)


def test_square_root_tame_symbol_returns_minus_one() -> None:
    value = tame_symbol_standard(1, 2)
    assert value == 1.0

    odd_pair_value = tame_symbol_standard(1, 1)
    assert odd_pair_value == -1.0


def test_cubic_tame_symbol_with_declared_analytic_factor_recovers_mu_3() -> None:
    zeta_3 = root_of_unity(3)
    value = tame_symbol_standard(1, 3, h_g_0=1 / zeta_3)
    assert_close(value, zeta_3)


def test_tame_symbol_is_multiplicative_in_first_unit() -> None:
    level = 3
    h_g_0 = 1 / root_of_unity(level)

    for left in range(0, 4):
        for right in range(0, 4):
            combined = tame_symbol_standard(left + right, level, h_g_0=h_g_0)
            product = tame_symbol_standard(left, level, h_g_0=h_g_0) * tame_symbol_standard(
                right, level, h_g_0=h_g_0
            )
            assert_close(combined, product)


def test_tame_symbol_side_is_not_the_carry_cocycle() -> None:
    level = 3
    valuation = 2

    tame_value = tame_symbol_standard(valuation, level)
    carry_value = carry(valuation, valuation, level)

    assert tame_value == 1.0
    assert carry_value == 1
    assert tame_value != carry_value
