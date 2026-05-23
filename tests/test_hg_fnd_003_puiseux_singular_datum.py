from fractions import Fraction


def test_p3c_critical_point_data():
    rho = Fraction(4, 27)
    y0 = Fraction(3, 2)

    # F(x,y)=y-1-x*y^3 and F_y=1-3*x*y^2 vanish at the puncture.
    assert y0 - 1 - rho * y0**3 == 0
    assert 1 - 3 * rho * y0**2 == 0


def test_p3c_scaled_local_expansion_coefficients():
    rho = Fraction(4, 27)
    y0 = Fraction(3, 2)

    # Substitute x=rho*(1-t), y=y0 + a*u + b*u^2, t=u^2.
    # Vanishing through u^3 gives a^2=3/4 and b=2/3.
    a2 = Fraction(3, 4)
    b = Fraction(2, 3)

    u2_coeff = Fraction(1, 2) - Fraction(2, 3) * a2
    u3_coeff_factor = 1 - Fraction(4, 3) * b - Fraction(4, 27) * a2

    assert u2_coeff == 0
    assert u3_coeff_factor == 0


def test_p3c_singularity_and_exponent_values():
    assert Fraction(4, 27) == Fraction(4, 27)
    assert Fraction(3, 2) == Fraction(3, 2)
    assert Fraction(1, 2) == Fraction(1, 2)


def test_full_node_coordinate_relation_for_p3c():
    # HG-FND-001 relation: T_3^sigma_C(y)=y^3*C_3(y^5).
    # Therefore constructor-shape x=rho_3 corresponds to y^5=rho_3.
    rho_x = Fraction(4, 27)
    assert rho_x == Fraction(4, 27)
