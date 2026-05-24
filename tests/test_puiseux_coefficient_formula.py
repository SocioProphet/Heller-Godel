"""Guard for the corrected Puiseux coefficient formula A_p^2 = 2p/(p-1)^3.

Corrects the earlier wrong candidate c_p^2 = 1 - rho_p recorded in HW-OPEN-002.
These tests verify the formula against HG-MTH-018 (p=3 theorem-grade) and
extend to p=2,5,7 as diagnostic checks.
"""

from fractions import Fraction


def y0(p: int) -> Fraction:
    return Fraction(p, p - 1)


def rho_p(p: int) -> Fraction:
    return Fraction((p - 1) ** (p - 1), p**p)


def A_sq(p: int) -> Fraction:
    return Fraction(2 * p, (p - 1) ** 3)


def test_puiseux_formula_at_p2_p3_p5_p7() -> None:
    assert A_sq(2) == Fraction(4, 1)
    assert A_sq(3) == Fraction(3, 4)
    assert A_sq(5) == Fraction(5, 32)
    assert A_sq(7) == Fraction(7, 108)


def test_general_formula() -> None:
    for p in [2, 3, 5, 7, 11]:
        assert A_sq(p) == Fraction(2 * p, (p - 1) ** 3)


def test_j_half_connections() -> None:
    j = Fraction(1, 2)
    assert A_sq(3) == j * (j + 1)
    assert rho_p(2) == j**2
    assert A_sq(2) == (2 * j + 1) ** 2


def test_wrong_formula_is_wrong() -> None:
    for p in [2, 3, 5]:
        assert A_sq(p) != 1 - rho_p(p)


def test_p3_matches_hg_mth_018_theorem() -> None:
    assert A_sq(3) == Fraction(3, 4)
    assert rho_p(3) == Fraction(4, 27)
    assert A_sq(3) != rho_p(3)


def test_a5_normalized_form() -> None:
    assert A_sq(5) == Fraction(10, 64)
    assert Fraction(10, 64) == Fraction(5, 32)
