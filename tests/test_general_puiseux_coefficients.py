from fractions import Fraction
from math import comb


def y0(p):
    return Fraction(p, p - 1)


def rho_p(p):
    return Fraction((p - 1) ** (p - 1), p**p)


def A_sq(p):
    return Fraction(2 * p, (p - 1) ** 3)


def b_p(p):
    y = y0(p)
    A2 = A_sq(p)
    num = p * y ** (p - 1) - comb(p, 3) * y ** (p - 3) * A2
    den = 2 * comb(p, 2) * y ** (p - 2)
    return num / den


def test_A_sq_formula():
    assert A_sq(3) == Fraction(3, 4)   # matches HG-MTH-018
    assert A_sq(5) == Fraction(5, 32)
    assert A_sq(7) == Fraction(7, 108)
    for p in [3, 5, 7, 11]:
        assert A_sq(p) == Fraction(2 * p, (p - 1) ** 3)


def test_b_formula():
    assert b_p(3) == Fraction(2, 3)    # matches HG-MTH-018 Section 5
    assert b_p(5) == Fraction(1, 4)    # confirmed numerically in p=5 preflight
    assert b_p(7) == Fraction(4, 27)
    assert b_p(11) == Fraction(2, 25)


def test_b7_equals_rho3():
    # Unexplained coincidence: b_7 = rho_3.
    assert b_p(7) == rho_p(3)


def test_critical_point_p5():
    y = y0(5)
    r = rho_p(5)
    assert y - 1 - r * y**5 == 0       # F(rho5, y0) = 0
    assert 1 - 5 * r * y**4 == 0       # F_y(rho5, y0) = 0


def test_critical_point_p7():
    y = y0(7)
    r = rho_p(7)
    assert y - 1 - r * y**7 == 0
    assert 1 - 7 * r * y**6 == 0


def test_j_half_connections():
    j = Fraction(1, 2)
    assert A_sq(3) == j * (j + 1)      # Casimir
    assert rho_p(2) == j**2            # Catalan singularity
    assert A_sq(2) == (2 * j + 1) ** 2
