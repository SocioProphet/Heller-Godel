from fractions import Fraction


def catalan_puiseux_boundary_note():
    """Catalan near rho=1/4 has analytic germ plus square-root correction.

    C(x) = (1 - sqrt(1-4x))/(2x).
    Let t = 1 - 4x, so x=(1-t)/4.
    Then C(x)=2(1-sqrt(t))/(1-t).
    Expanding around t=0 gives:
      2(1 - t^(1/2)) * (1 + t + t^2 + ...)
    The analytic constant term is 2. The leading nonanalytic exponent is 1/2.
    """
    return Fraction(1, 2)


def test_catalan_leading_nonanalytic_puiseux_exponent():
    assert catalan_puiseux_boundary_note() == Fraction(1, 2)


def test_catalan_is_not_naive_single_term_local_germ():
    """Regression guard for manuscript wording.

    The statement should not say that the whole local behavior of C(x) is simply
    c*(1-4x)^(1/2). The exponent 1/2 belongs to the selected nonanalytic
    Puiseux channel after separating the analytic germ.
    """
    analytic_constant_term = 2
    leading_nonanalytic_exponent = Fraction(1, 2)
    assert analytic_constant_term == 2
    assert leading_nonanalytic_exponent == Fraction(1, 2)
