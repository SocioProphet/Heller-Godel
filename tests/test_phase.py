from fractions import Fraction

from heller_godel.phase import P13, f_p, k_vector, zeta_p, zeta_vector, is_zeta_coboundary, is_zeta_symmetric


def test_seed_vectors():
    assert k_vector(-2) == (0, 0, 0, 0, 0, 0)
    assert k_vector(Fraction(1, 2)) == (1, 1, 2, 3, 5, 6)


def test_zeta_examples():
    assert zeta_vector(Fraction(1, 2), Fraction(1, 2)) == (0, 1, 1, 1, 1, 1)
    assert zeta_vector(Fraction(1, 2), Fraction(1, 3)) == (0, 0, 1, 0, 1, 0)


def test_zeta_coboundary_and_symmetry():
    samples = [
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(1, 3), Fraction(2, 3)),
        (Fraction(1, 4), Fraction(3, 4)),
        (Fraction(-2), Fraction(1, 2)),
    ]
    for alpha, beta in samples:
        for p in P13:
            assert is_zeta_coboundary(alpha, beta, p)
            assert is_zeta_symmetric(alpha, beta, p)


def test_f_p_definition():
    assert f_p(Fraction(1, 2), 5) == 2
    assert f_p(Fraction(-2), 11) == 0
