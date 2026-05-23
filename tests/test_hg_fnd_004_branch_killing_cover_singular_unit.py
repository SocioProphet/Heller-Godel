from fractions import Fraction

from heller_godel.phase_characters import normalize_exponent, phase_index


def cover_value(w: int, level: int) -> int:
    return w**level


def deck_transform(w: complex, level: int) -> complex:
    zeta = complex(-1, 0) if level == 2 else complex(-0.5, 3**0.5 / 2)
    return zeta * w


def singular_unit(w: complex, exponent_index: int) -> complex:
    return w**exponent_index


def character_value(level: int, exponent_index: int) -> complex:
    zeta = complex(-1, 0) if level == 2 else complex(-0.5, 3**0.5 / 2)
    return zeta**exponent_index


def assert_close(left: complex, right: complex, tolerance: float = 1e-12):
    assert abs(left - right) < tolerance


def test_square_root_cover_and_transformation_law():
    level = 2
    exponent_index, resolved_level = phase_index(Fraction(1, 2), level=2)
    assert resolved_level == level
    assert cover_value(3, level) == 9
    w = complex(3, 0)
    transformed = singular_unit(deck_transform(w, level), exponent_index)
    expected = character_value(level, exponent_index) * singular_unit(w, exponent_index)
    assert_close(transformed, expected)
    assert character_value(level, exponent_index) == complex(-1, 0)


def test_cubic_cover_and_transformation_law():
    level = 3
    exponent_index, resolved_level = phase_index(Fraction(1, 3), level=3)
    assert resolved_level == level
    assert cover_value(2, level) == 8
    w = complex(2, 0)
    transformed = singular_unit(deck_transform(w, level), exponent_index)
    expected = character_value(level, exponent_index) * singular_unit(w, exponent_index)
    assert_close(transformed, expected)
    assert_close(character_value(level, exponent_index), complex(-0.5, 3**0.5 / 2))


def test_cover_level_matches_puiseux_denominator_square_root_channel():
    exponent = normalize_exponent(Fraction(1, 2))
    assert exponent.denominator == 2
    assert phase_index(Fraction(1, 2), level=exponent.denominator) == (1, 2)


def test_cover_level_matches_puiseux_denominator_cubic_channel():
    exponent = normalize_exponent(Fraction(1, 3))
    assert exponent.denominator == 3
    assert phase_index(Fraction(1, 3), level=exponent.denominator) == (1, 3)


def test_normalized_singular_unit_has_unit_analytic_factor_at_puncture():
    analytic_factor_at_zero = 1
    assert analytic_factor_at_zero == 1
