from fractions import Fraction

from heller_godel.phase_characters import phase_index, prime_reduction


def cubic_discriminant(a, b, c, d):
    return {
        2: 18 * a * b * c * d - 4 * b**3 * d + b**2 * c**2,
        1: -4 * a * c**3,
        0: -27 * a**2 * d**2,
    }


def manuscript_phase_index(beta: Fraction, prime: int) -> tuple[int, int]:
    return ((prime * beta.numerator) // beta.denominator) % prime, prime


def test_cubic_discriminant_identity_for_global_source():
    # Polynomial: x*y^3 - y + 1, with a=x, b=0, c=-1, d=1.
    # Represent x as polynomial degree bookkeeping: Delta = 4*x - 27*x^2.
    delta = cubic_discriminant(a=1, b=0, c=-1, d=1)
    assert delta == {2: -27, 1: 4, 0: 0}


def test_manuscript_phase_map_value_for_p3_beta_half():
    assert manuscript_phase_index(Fraction(1, 2), 3) == (1, 3)


def test_existing_phase_index_remains_denominator_level_substrate():
    # The executable substrate is denominator-level arithmetic: alpha=1/3 at level 3.
    assert phase_index(Fraction(1, 3), level=3) == (1, 3)


def test_prime_reduction_at_p3_gives_mu3_projection():
    index, level = manuscript_phase_index(Fraction(1, 2), 3)
    assert prime_reduction(index, level, 3) == (1, 3)
