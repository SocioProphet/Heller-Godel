"""Regression tests for HG-FND-008 Deligne/carry separation."""

from __future__ import annotations

from heller_godel.phase_characters import (
    carry,
    carry_cocycle_identity_holds,
    tame_symbol_standard,
)


def test_tame_symbol_is_complex_valued() -> None:
    assert isinstance(tame_symbol_standard(1, 1), (complex, float))
    assert tame_symbol_standard(1, 1) == -1.0


def test_carry_is_integer_valued() -> None:
    assert isinstance(carry(1, 1, 2), int)
    assert carry(1, 1, 2) == 1


def test_primary_separation_witness_different_values() -> None:
    # tame_symbol_standard(1, 3) = -1.0, carry(1, 1, 3) = 0.
    # The same small integers exercise unrelated typed surfaces.
    assert tame_symbol_standard(1, 3) == -1.0
    assert carry(1, 1, 3) == 0
    assert tame_symbol_standard(1, 3) != carry(1, 1, 3)


def test_tame_symbol_is_bilinear_not_additive_cocycle() -> None:
    # Tame symbol: Tam(a+b, N) = Tam(a,N) * Tam(b,N) — multiplicative.
    # Carry: kappa(a,b) + kappa(a+b,c) = kappa(b,c) + kappa(a,b+c) — additive cocycle.
    # These are structurally incompatible laws.
    assert tame_symbol_standard(2, 3) == tame_symbol_standard(1, 3) * tame_symbol_standard(1, 3)
    assert carry_cocycle_identity_holds(1, 1, 1, 3)


def test_separation_holds_at_level_2() -> None:
    assert tame_symbol_standard(1, 1) == -1.0
    assert carry(1, 1, 2) == 1
    assert isinstance(tame_symbol_standard(1, 1), float)
    assert isinstance(carry(1, 1, 2), int)
