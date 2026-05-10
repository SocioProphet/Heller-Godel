from fractions import Fraction


P13 = [2, 3, 5, 7, 11, 13]


def k_p(alpha: Fraction, p: int) -> int:
    return (p * alpha.numerator // alpha.denominator) % p


def k_13(alpha: Fraction) -> tuple[int, ...]:
    return tuple(k_p(alpha, p) for p in P13)


def test_chain_seed_basis_is_trivial():
    assert k_13(Fraction(-2, 1)) == (0, 0, 0, 0, 0, 0)


def test_catalan_seed_basis():
    assert k_13(Fraction(1, 2)) == (1, 1, 2, 3, 5, 6)


def test_seed_basis_is_truncation_not_full_invariant():
    """P13 is a finite observation basis. It is not the full prime-indexed family."""
    assert P13 == [2, 3, 5, 7, 11, 13]
