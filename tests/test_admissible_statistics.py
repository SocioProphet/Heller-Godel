from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Weights:
    lam: int
    app: int
    var: int

    def admissible(self) -> bool:
        return self.lam > 0 and self.app > 0 and self.var > 0


ADMISSIBLE_WEIGHTS = [
    Weights(1, 1, 1),
    Weights(1, 2, 1),
    Weights(2, 1, 1),
    Weights(1, 1, 2),
    Weights(3, 1, 1),
    Weights(1, 3, 1),
    Weights(5, 1, 1),
]


def chain_formula(weights: Weights) -> tuple[int, int]:
    """Returns (numerator_exponent, denominator_exponent).

    Closed form: x^num / (1 - x^den)^2.
    """
    return weights.lam + weights.var, weights.lam


def t_family_formula(weights: Weights) -> tuple[int, int]:
    """Returns (numerator_exponent, denominator_exponent).

    Closed form: x^num / (1 - x^den)^2.
    """
    numerator = 2 * weights.lam + weights.app + 2 * weights.var
    denominator = weights.lam + weights.app + weights.var
    return numerator, denominator


def chain_weight(n: int, weights: Weights) -> int:
    """sigma_w(inhabitant of phi_n) for the chain family."""
    return weights.lam * n + weights.var


def t_family_weight(n: int, weights: Weights) -> int:
    """sigma_w(t_{n,i}) for the T=((A->A)->A)->A family.

    The statistic is independent of i for this rank-uniform family.
    """
    return (
        weights.lam * (n + 1)
        + weights.app * n
        + weights.var * (n + 1)
    )


def coefficient_support_for_family(
    weight_fn: Callable[[int, Weights], int],
    weights: Weights,
    n_max: int,
) -> dict[int, int]:
    """Compute coefficient support by direct enumeration up to level n_max.

    Both calibration families have exactly n inhabitants at level n.
    """
    coeffs: dict[int, int] = {}
    for n in range(1, n_max + 1):
        exponent = weight_fn(n, weights)
        coeffs[exponent] = coeffs.get(exponent, 0) + n
    return coeffs


def predicted_support(numerator: int, denominator: int, n_max: int) -> dict[int, int]:
    """Expansion of x^numerator / (1 - x^denominator)^2.

    Uses n_max terms, matching levels n=1..n_max in the calibration families.
    """
    return {numerator + denominator * k: k + 1 for k in range(n_max)}


def test_chain_formula_for_admissible_weights() -> None:
    for weights in ADMISSIBLE_WEIGHTS:
        assert weights.admissible()
        numerator, denominator = chain_formula(weights)
        observed = coefficient_support_for_family(chain_weight, weights, 8)
        expected = predicted_support(numerator, denominator, 8)
        assert observed == expected, (
            f"chain mismatch at {weights}: observed={observed}, expected={expected}"
        )


def test_t_family_formula_for_admissible_weights() -> None:
    for weights in ADMISSIBLE_WEIGHTS:
        assert weights.admissible()
        numerator, denominator = t_family_formula(weights)
        observed = coefficient_support_for_family(t_family_weight, weights, 8)
        expected = predicted_support(numerator, denominator, 8)
        assert observed == expected, (
            f"T-family mismatch at {weights}: observed={observed}, expected={expected}"
        )


def test_boundary_weight_is_not_admissible_but_matches_formula_on_test_families() -> None:
    weights = Weights(1, 1, 0)
    assert not weights.admissible()

    assert chain_formula(weights) == (1, 1)
    assert t_family_formula(weights) == (3, 2)

    observed_chain = coefficient_support_for_family(chain_weight, weights, 8)
    expected_chain = predicted_support(1, 1, 8)
    assert observed_chain == expected_chain

    observed_t = coefficient_support_for_family(t_family_weight, weights, 8)
    expected_t = predicted_support(3, 2, 8)
    assert observed_t == expected_t


def test_closed_form_table_values() -> None:
    expected = {
        Weights(1, 1, 1): ((2, 1), (5, 3)),
        Weights(1, 2, 1): ((2, 1), (6, 4)),
        Weights(2, 1, 1): ((3, 2), (7, 4)),
        Weights(1, 1, 2): ((3, 1), (7, 4)),
        Weights(3, 1, 1): ((4, 3), (9, 5)),
        Weights(1, 3, 1): ((2, 1), (7, 5)),
        Weights(5, 1, 1): ((6, 5), (13, 7)),
    }
    for weights, (chain_expected, t_expected) in expected.items():
        assert chain_formula(weights) == chain_expected
        assert t_family_formula(weights) == t_expected
