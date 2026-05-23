from fractions import Fraction

from heller_godel.phase_characters import phase_index, prime_reduction


def cubic_discriminant(a, b, c, d):
    return {
        2: 18 * a * b * c * d - 4 * b**3 * d + b**2 * c**2,
        1: -4 * a * c**3,
        0: -27 * a**2 * d**2,
    }


def test_cubic_discriminant_identity_for_global_source():
    # Polynomial: x*y^3 - y + 1, with a=x, b=0, c=-1, d=1.
    # Represent x as polynomial degree bookkeeping: Delta = 4*x - 27*x^2.
    delta = cubic_discriminant(a=1, b=0, c=-1, d=1)
    assert delta == {2: -27, 1: 4, 0: 0}


def test_manuscript_phase_map_value_for_p3_beta_half():
    beta = Fraction(1, 2)
    p = 3
    k = (p * beta.numerator) // beta.denominator
    assert k % p == 1


def test_phase_index_level_three_matches_manuscript_value():
    assert phase_index(Fraction(1, 2), level=3) == (1, 3)


def test_prime_reduction_at_p3_gives_mu3_projection():
    index, level = phase_index(Fraction(1, 2), level=3)
    assert prime_reduction(index, level, 3) == (1, 3)
