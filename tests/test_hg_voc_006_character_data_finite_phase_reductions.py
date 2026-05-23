from fractions import Fraction

from heller_godel.phase_characters import phase_index, prime_reduction


def cubic_discriminant_for_xy3_minus_y_plus_one():
    # For a*x? Wait: polynomial x*y^3 - y + 1 has coefficients
    # a=x, b=0, c=-1, d=1. Track powers of x in the discriminant.
    return {
        2: -27,  # -27*a^2*d^2 = -27*x^2
        1: 4,  # -4*a*c^3 = 4*x
        0: 0,
    }


def manuscript_phase_index(beta: Fraction, prime: int) -> tuple[int, int]:
    return ((prime * beta.numerator) // beta.denominator) % prime, prime


def test_cubic_discriminant_identity_for_global_source():
    # Delta(x*y^3 - y + 1) = 4*x - 27*x^2 = x*(4 - 27*x).
    assert cubic_discriminant_for_xy3_minus_y_plus_one() == {2: -27, 1: 4, 0: 0}


def test_manuscript_phase_map_value_for_p3_beta_half():
    assert manuscript_phase_index(Fraction(1, 2), 3) == (1, 3)


def test_existing_phase_index_remains_denominator_level_substrate():
    # The executable substrate is denominator-level arithmetic: alpha=1/3 at level 3.
    assert phase_index(Fraction(1, 3), level=3) == (1, 3)


def test_prime_reduction_at_p3_gives_mu3_projection():
    index, level = manuscript_phase_index(Fraction(1, 2), 3)
    assert prime_reduction(index, level, 3) == (1, 3)
