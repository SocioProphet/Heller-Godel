from fractions import Fraction

import pytest

from heller_godel.phase_characters import (
    carry,
    carry_cocycle_identity_holds,
    carry_table,
    common_level,
    holonomy_index,
    multiply_indices,
    normalize_exponent,
    p_primary_projection,
    phase_index,
    prime_reduction,
    tame_symbol_standard,
)


def test_normalize_exponent_reduces_modulo_integers():
    assert normalize_exponent(Fraction(5, 3)).numerator == 2
    assert normalize_exponent(Fraction(5, 3)).denominator == 3
    assert normalize_exponent(Fraction(-1, 2)).fraction == Fraction(1, 2)
    assert normalize_exponent(Fraction(4, 2)).is_trivial


def test_phase_index_on_common_cover():
    assert common_level(Fraction(1, 2), Fraction(1, 3)) == 6
    assert phase_index(Fraction(1, 2), 6) == (3, 6)
    assert phase_index(Fraction(1, 3), 6) == (2, 6)


@pytest.mark.parametrize(
    "alpha,level,prime,expected",
    [
        (Fraction(1, 6), 6, 2, (1, 2)),
        (Fraction(1, 6), 6, 3, (1, 3)),
        (Fraction(1, 6), 6, 5, (0, 1)),
    ],
)
def test_prime_reductions(alpha, level, prime, expected):
    index, level = phase_index(alpha, level)
    assert prime_reduction(index, level, prime) == expected


def test_p_primary_projection_keeps_prime_power_level():
    index, level = phase_index(Fraction(1, 12), 12)
    assert p_primary_projection(index, level, 2) == (1, 4)
    assert p_primary_projection(index, level, 3) == (1, 3)


def test_finite_character_multiplication_is_exact():
    a, level = phase_index(Fraction(1, 2), 6)
    b, _ = phase_index(Fraction(1, 3), 6)
    assert multiply_indices(a, b, level) == 5
    assert multiply_indices(a, b, level) == phase_index(Fraction(5, 6), 6)[0]


def test_carry_records_lifted_phase_section_defect():
    assert carry(1, 1, 3) == 0
    assert carry(2, 2, 3) == 1
    assert 2 + 2 == ((2 + 2) % 3) + 3 * carry(2, 2, 3)


def test_carry_tables_small_levels_match_appendix_b():
    assert carry_table(2) == (
        (0, 0),
        (0, 1),
    )
    assert carry_table(3) == (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 1),
    )
    assert carry_table(4) == (
        (0, 0, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 1),
        (0, 1, 1, 1),
    )


def test_carry_satisfies_cocycle_identity_small_range():
    for level in range(2, 12):
        for a in range(level):
            for b in range(level):
                for c in range(level):
                    assert carry_cocycle_identity_holds(a, b, c, level)


def test_tame_symbol_is_not_the_carry():
    # L=3, A=B=1 is the witness used in the manuscript capture.
    # The carry vanishes, while the tame symbol under the standard convention is -1.
    assert carry(1, 1, 3) == 0
    assert tame_symbol_standard(1, 1, 1, 1) == -1


def test_tame_symbol_uses_analytic_factors_not_only_residues():
    assert tame_symbol_standard(1, 2, h_f_0=2, h_g_0=5) == pytest.approx(4 / 5)
    assert carry(1, 2, 5) == 0


def test_sphere_pullback_is_trivial_by_absence_of_loops():
    index, level = phase_index(Fraction(1, 5))
    assert holonomy_index(index, level, winding=0) == (0, 5)


def test_torus_pullback_is_determined_by_two_winding_numbers():
    index, level = phase_index(Fraction(2, 5))
    assert (index, level) == (2, 5)
    assert holonomy_index(index, level, winding=3) == (1, 5)
    assert holonomy_index(index, level, winding=-1) == (3, 5)


def test_catalan_klein_bottle_mu2_holonomy_bookkeeping():
    # Catalan singular line: alpha=1/2, u=w, chi(gamma)=-1.
    index, level = phase_index(Fraction(1, 2))
    assert (index, level) == (1, 2)

    # Klein bottle presentation <r,s | r s r^{-1}=s^{-1}>.
    # The intended comparison map sends the orientation-reversing generator r
    # once around the puncture and sends s trivially.
    assert holonomy_index(index, level, winding=1) == (1, 2)  # -1
    assert holonomy_index(index, level, winding=0) == (0, 2)  # +1


def test_unconditional_mu2_comparison_common_generator():
    # The analytic deck generator for Catalan and the chosen Klein-bottle
    # orientation-reversing generator both factor through the nontrivial class
    # of Z/2 and therefore both evaluate to the same mu_2 element.
    analytic_index, level = phase_index(Fraction(1, 2))
    klein_r_index, _ = holonomy_index(analytic_index, level, winding=1)
    assert analytic_index == 1
    assert klein_r_index == analytic_index
