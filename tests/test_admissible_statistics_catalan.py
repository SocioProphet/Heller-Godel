"""Test harness for HG-STAT-002 v0.1.

Verifies Theorems 4.1 (Convention A) and 4.2 (Convention B) for the
Catalan-grounded type C_A = (A -> A -> A) -> A -> A under admissible
constructor-linear statistics.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Weights:
    lam: int
    app: int
    var: int

    def admissible(self) -> bool:
        return self.lam > 0 and self.app > 0 and self.var > 0


def catalan(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(n):
        result = result * (2 * (2 * i + 1)) // (i + 2)
    return result


def catalan_formula_A(weights: Weights) -> tuple[int, int]:
    """Convention A: T_C^sigma_w(x) = x^b * C(x^a). Returns (b, a)."""
    a = weights.app + 2 * weights.var
    b = 2 * weights.lam + weights.var
    return b, a


def catalan_formula_B(weights: Weights) -> tuple[int, int]:
    """Convention B: T_C^sigma_w(x) = x^b * C(x^a). Returns (b, a)."""
    a = 2 * weights.app + 2 * weights.var
    b = 2 * weights.lam + weights.var
    return b, a


def catalan_weight_A(k: int, weights: Weights) -> int:
    """Profile (lam=2, app=k, var=2k+1) under Convention A."""
    return weights.lam * 2 + weights.app * k + weights.var * (2 * k + 1)


def catalan_weight_B(k: int, weights: Weights) -> int:
    """Profile (lam=2, app=2k, var=2k+1) under Convention B."""
    return weights.lam * 2 + weights.app * (2 * k) + weights.var * (2 * k + 1)


def catalan_coefficients(weight_fn, weights: Weights, k_max: int) -> dict[int, int]:
    """Coefficient sequence by direct enumeration.

    Rank-uniform: at level k there are C_k inhabitants all with the same
    sigma_w value.
    """
    coeffs: dict[int, int] = {}
    for k in range(k_max + 1):
        exponent = weight_fn(k, weights)
        coeffs[exponent] = coeffs.get(exponent, 0) + catalan(k)
    return coeffs


def predicted_catalan_coefficients(b: int, a: int, k_max: int) -> dict[int, int]:
    """Coefficients of x^b * C(x^a) up to level k_max."""
    return {b + a * k: catalan(k) for k in range(k_max + 1)}


ADMISSIBLE_WEIGHTS = [
    Weights(1, 1, 1),
    Weights(1, 2, 1),
    Weights(2, 1, 1),
    Weights(1, 1, 2),
    Weights(3, 1, 1),
    Weights(1, 3, 1),
    Weights(5, 1, 1),
]

K_MAX = 5  # Catalan numbers 1, 1, 2, 5, 14, 42


def test_catalan_convention_A() -> None:
    for weights in ADMISSIBLE_WEIGHTS:
        assert weights.admissible()
        b, a = catalan_formula_A(weights)
        observed = catalan_coefficients(catalan_weight_A, weights, K_MAX)
        expected = predicted_catalan_coefficients(b, a, K_MAX)
        assert observed == expected, (
            f"Convention A mismatch at {weights}: "
            f"observed={observed}, expected={expected}"
        )


def test_catalan_convention_B() -> None:
    for weights in ADMISSIBLE_WEIGHTS:
        assert weights.admissible()
        b, a = catalan_formula_B(weights)
        observed = catalan_coefficients(catalan_weight_B, weights, K_MAX)
        expected = predicted_catalan_coefficients(b, a, K_MAX)
        assert observed == expected, (
            f"Convention B mismatch at {weights}: "
            f"observed={observed}, expected={expected}"
        )


def test_radius_covariance_convention_A() -> None:
    """Dominant radius is 4^{-1/a}; distinct a values give distinct radii."""
    a_values = {catalan_formula_A(w)[1] for w in ADMISSIBLE_WEIGHTS}
    assert len(a_values) >= 2, (
        f"Expected multiple distinct radii under Convention A; got a values {a_values}"
    )


def test_radius_covariance_convention_B() -> None:
    a_values = {catalan_formula_B(w)[1] for w in ADMISSIBLE_WEIGHTS}
    assert len(a_values) >= 2, (
        f"Expected multiple distinct radii under Convention B; got a values {a_values}"
    )


def test_section_5_table_convention_A() -> None:
    """Reproduce HG-STAT-002 Section 5.1 table."""
    expected = [
        (Weights(1, 1, 1), 3, 3),
        (Weights(1, 2, 1), 4, 3),
        (Weights(2, 1, 1), 3, 5),
        (Weights(1, 1, 2), 5, 4),
        (Weights(3, 1, 1), 3, 7),
        (Weights(1, 3, 1), 5, 3),
        (Weights(5, 1, 1), 3, 11),
    ]
    for weights, expected_a, expected_b in expected:
        b, a = catalan_formula_A(weights)
        assert (a, b) == (expected_a, expected_b), (
            f"Section 5.1 row mismatch at {weights}: "
            f"expected (a={expected_a}, b={expected_b}), got (a={a}, b={b})"
        )


def test_section_5_table_convention_B() -> None:
    """Reproduce HG-STAT-002 Section 5.2 table."""
    expected = [
        (Weights(1, 1, 1), 4, 3),
        (Weights(1, 2, 1), 6, 3),
        (Weights(2, 1, 1), 4, 5),
        (Weights(1, 1, 2), 6, 4),
        (Weights(3, 1, 1), 4, 7),
        (Weights(1, 3, 1), 8, 3),
        (Weights(5, 1, 1), 4, 11),
    ]
    for weights, expected_a, expected_b in expected:
        b, a = catalan_formula_B(weights)
        assert (a, b) == (expected_a, expected_b), (
            f"Section 5.2 row mismatch at {weights}: "
            f"expected (a={expected_a}, b={expected_b}), got (a={a}, b={b})"
        )
