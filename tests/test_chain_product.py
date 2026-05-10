def chain_series_coeff(n: int) -> int:
    """Coefficient of x^n in x/(1-x)^2: n for n >= 1, else 0."""
    return n if n >= 1 else 0


def ordinary_product_coeff(n: int) -> int:
    """Coefficient of x^n in (x/(1-x)^2)^2."""
    return sum(chain_series_coeff(k) * chain_series_coeff(n - k) for k in range(n + 1))


def closed_form_x2_over_1_minus_x_4_coeff(n: int) -> int:
    """Coefficient of x^n in x^2/(1-x)^4 is binomial(n+1,3) for n>=2."""
    if n < 2:
        return 0
    return (n + 1) * n * (n - 1) // 6


def triangular_series_coeff(n: int) -> int:
    """Coefficient of x^n in x^2/(1-x)^3 is binomial(n,2) for n>=2."""
    if n < 2:
        return 0
    return n * (n - 1) // 2


def test_chain_ordinary_product_is_fourth_order_pole_coefficients():
    for n in range(0, 20):
        assert ordinary_product_coeff(n) == closed_form_x2_over_1_minus_x_4_coeff(n)


def test_triangular_series_is_not_ordinary_chain_product():
    disagreements = []
    for n in range(0, 20):
        if ordinary_product_coeff(n) != triangular_series_coeff(n):
            disagreements.append(n)

    assert disagreements, "triangular series must not be conflated with ordinary product"
    assert 3 in disagreements
    assert ordinary_product_coeff(3) == 4
    assert triangular_series_coeff(3) == 3
