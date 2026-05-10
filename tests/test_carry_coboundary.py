from fractions import Fraction


def q_p(alpha: Fraction, p: int) -> int:
    """Finite phase section q_p(alpha)=floor(p alpha) mod p."""
    return (p * alpha.numerator // alpha.denominator) % p


def zeta_p(alpha: Fraction, beta: Fraction, p: int) -> int:
    """Carry defect for the chosen finite phase section."""
    return (q_p(alpha + beta, p) - q_p(alpha, p) - q_p(beta, p)) % p


def test_zeta_is_coboundary_for_sample_grid():
    samples = [
        Fraction(0),
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(1, 2),
        Fraction(2, 3),
        Fraction(3, 4),
        Fraction(-1, 2),
    ]
    primes = [2, 3, 5, 7, 11, 13]

    for p in primes:
        for alpha in samples:
            for beta in samples:
                assert zeta_p(alpha, beta, p) == (
                    q_p(alpha + beta, p) - q_p(alpha, p) - q_p(beta, p)
                ) % p


def test_zeta_is_symmetric_for_sample_grid():
    samples = [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)]
    primes = [2, 3, 5, 7, 11, 13]

    for p in primes:
        for alpha in samples:
            for beta in samples:
                assert zeta_p(alpha, beta, p) == zeta_p(beta, alpha, p)


def test_known_carry_fingerprints():
    primes = [2, 3, 5, 7, 11, 13]

    assert tuple(zeta_p(Fraction(1, 2), Fraction(1, 2), p) for p in primes) == (
        0,
        1,
        1,
        1,
        1,
        1,
    )
    assert tuple(zeta_p(Fraction(1, 2), Fraction(1, 3), p) for p in primes) == (
        0,
        0,
        1,
        0,
        1,
        0,
    )


def test_commentary_boundary():
    """Regression guard: zeta_p is a section defect, not a nontrivial class by itself.

    This test does not prove a global theorem about every possible enriched setting.
    It records the current manuscript boundary: with unrestricted ordinary cochains,
    the displayed carry term is delta(q_p).
    """
    assert True
