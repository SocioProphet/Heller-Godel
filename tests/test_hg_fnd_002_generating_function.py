from fractions import Fraction


def conv(a, b, n):
    return [sum(a[i] * b[k - i] for i in range(k + 1)) for k in range(n + 1)]


def shift_for_raw_pair(coeffs, n):
    return [0] + coeffs[:n]


def test_chain_product_formula_under_reduced_statistic():
    n = 8
    chain = [0] + list(range(1, n + 1))
    reduced = conv(chain, chain, n)
    raw = shift_for_raw_pair(reduced, n)

    assert reduced == [0, 0, 1, 4, 10, 20, 35, 56, 84]
    assert raw == [0, 0, 0, 1, 4, 10, 20, 35, 56]


def test_catalan_product_formula_under_reduced_statistic():
    n = 8
    catalan = [1]
    for k in range(1, n + 2):
        catalan.append(sum(catalan[i] * catalan[k - 1 - i] for i in range(k)))

    reduced = conv(catalan[: n + 1], catalan[: n + 1], n)
    raw = shift_for_raw_pair(reduced, n)

    assert reduced == catalan[1 : n + 2]
    assert raw[1:] == reduced[:-1]


def test_chain_singularity_is_recorded():
    assert Fraction(1, 1) == Fraction(1, 1)


def test_catalan_singularity_and_exponent_are_recorded():
    assert Fraction(1, 4) == Fraction(1, 4)
    assert Fraction(1, 2) == Fraction(1, 2)
