from fractions import Fraction

from heller_godel.phase_characters import carry, holonomy_index, multiply_indices, phase_index


def test_multiply_indices_computes_character_product_modulo_level():
    left, level = phase_index(Fraction(1, 3), level=6)
    right, _ = phase_index(Fraction(1, 2), level=6)
    assert multiply_indices(left, right, level) == 5


def test_holonomy_index_returns_winding_result():
    index, level = phase_index(Fraction(1, 3), level=6)
    assert holonomy_index(index, level, winding=4) == (2, 6)


def test_mu2_self_product_is_trivial_but_carry_is_nonzero():
    index, level = phase_index(Fraction(1, 2), level=2)
    product = multiply_indices(index, index, level)
    assert product == 0
    assert carry(index, index, level) == 1


def test_mu3_square_product_is_nontrivial():
    index, level = phase_index(Fraction(1, 3), level=3)
    product = multiply_indices(index, index, level)
    assert product == 2


def test_multiplicative_product_does_not_imply_carry_zero():
    index, level = phase_index(Fraction(1, 2), level=2)
    assert multiply_indices(index, index, level) == 0
    assert carry(index, index, level) != 0
