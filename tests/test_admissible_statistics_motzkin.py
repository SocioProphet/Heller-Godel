from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass


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


def motzkin_profiles_by_size(n_max: int) -> list[dict[tuple[int, int], int]]:
    """Profiles for unary-binary bodies.

    Grammar:
        body ::= x | u body | b body body

    Profile is (U, B), where U is unary-node count and B is binary-node count.
    Motzkin size is U + 2B.
    """
    profiles: list[defaultdict[tuple[int, int], int]] = [
        defaultdict(int) for _ in range(n_max + 1)
    ]
    profiles[0][(0, 0)] = 1

    for n in range(1, n_max + 1):
        # Unary root contributes size 1.
        for (u, b), count in profiles[n - 1].items():
            profiles[n][(u + 1, b)] += count

        # Binary root contributes size 2, then splits remaining size.
        if n >= 2:
            for left_size in range(n - 1):
                right_size = n - 2 - left_size
                for (u1, b1), c1 in profiles[left_size].items():
                    for (u2, b2), c2 in profiles[right_size].items():
                        profiles[n][(u1 + u2, b1 + b2 + 1)] += c1 * c2

    return [dict(p) for p in profiles]


def motzkin_numbers(n_max: int) -> list[int]:
    profiles = motzkin_profiles_by_size(n_max)
    return [sum(p.values()) for p in profiles]


def sigma_convention_a(profile: tuple[int, int], weights: Weights) -> int:
    """Convention A: b body body is one app node with two args.

    Counts:
        lambdas = 3
        apps    = U + B
        vars    = U + 2B + 1
    """
    u, b = profile
    return (
        3 * weights.lam
        + weights.app * (u + b)
        + weights.var * (u + 2 * b + 1)
    )


def sigma_convention_b(profile: tuple[int, int], weights: Weights) -> int:
    """Convention B: b body body is curried as ((b body) body).

    Counts:
        lambdas = 3
        apps    = U + 2B
        vars    = U + 2B + 1
    """
    u, b = profile
    return (
        3 * weights.lam
        + weights.app * (u + 2 * b)
        + weights.var * (u + 2 * b + 1)
    )


def coeffs_for_profiles(
    profiles: list[dict[tuple[int, int], int]],
    weights: Weights,
    convention: str,
) -> dict[int, int]:
    coeffs: dict[int, int] = {}

    if convention == "A":
        sigma = sigma_convention_a
    elif convention == "B":
        sigma = sigma_convention_b
    else:
        raise ValueError(f"unknown convention: {convention}")

    for level_profiles in profiles:
        for profile, count in level_profiles.items():
            exponent = sigma(profile, weights)
            coeffs[exponent] = coeffs.get(exponent, 0) + count

    return dict(sorted(coeffs.items()))


def convention_a_parameters(weights: Weights) -> tuple[int, int, int]:
    """T_A^w(x) = x^c F(x^a, x^b)."""
    c = 3 * weights.lam + weights.var
    a = weights.app + weights.var
    b = weights.app + 2 * weights.var
    return c, a, b


def convention_b_parameters(weights: Weights) -> tuple[int, int, int]:
    """T_B^w(x) = x^c F(x^a, x^b)."""
    c = 3 * weights.lam + weights.var
    a = weights.app + weights.var
    b = 2 * weights.app + 2 * weights.var
    return c, a, b


def predicted_coeffs_from_bivariate_gf(
    profiles: list[dict[tuple[int, int], int]],
    c: int,
    a: int,
    b: int,
) -> dict[int, int]:
    """Coefficient support of x^c F(x^a, x^b).

    F(y,z) = sum count(U,B) y^U z^B.
    """
    coeffs: dict[int, int] = {}
    for level_profiles in profiles:
        for (u, binary), count in level_profiles.items():
            exponent = c + a * u + b * binary
            coeffs[exponent] = coeffs.get(exponent, 0) + count
    return dict(sorted(coeffs.items()))


def discriminant_radius(a: int, b: int) -> float:
    """Positive dominant root of Delta(x)=(1-x^a)^2-4x^b on (0,1)."""
    lo, hi = 0.0, 1.0

    def delta(r: float) -> float:
        return (1 - r**a) ** 2 - 4 * r**b

    for _ in range(100):
        mid = (lo + hi) / 2
        if delta(mid) > 0:
            lo = mid
        else:
            hi = mid

    return (lo + hi) / 2


def discriminant_derivative(a: int, b: int, r: float) -> float:
    return -2 * a * (1 - r**a) * r ** (a - 1) - 4 * b * r ** (b - 1)


def test_motzkin_number_specialization() -> None:
    # Motzkin numbers under size U + 2B.
    assert motzkin_numbers(8) == [1, 1, 2, 4, 9, 21, 51, 127, 323]


def test_non_rank_uniformity() -> None:
    profiles = motzkin_profiles_by_size(6)

    # Level 2 already has two different constructor profiles:
    # unary-unary and one binary root.
    assert profiles[2] == {(2, 0): 1, (0, 1): 1}

    # Level 4 has three distinct profile classes.
    assert profiles[4] == {(4, 0): 1, (2, 1): 6, (0, 2): 2}


def test_convention_a_bivariate_substitution() -> None:
    profiles = motzkin_profiles_by_size(8)
    for weights in ADMISSIBLE_WEIGHTS:
        assert weights.admissible()
        observed = coeffs_for_profiles(profiles, weights, "A")
        c, a, b = convention_a_parameters(weights)
        expected = predicted_coeffs_from_bivariate_gf(profiles, c, a, b)
        assert observed == expected


def test_convention_b_bivariate_substitution() -> None:
    profiles = motzkin_profiles_by_size(8)
    for weights in ADMISSIBLE_WEIGHTS:
        assert weights.admissible()
        observed = coeffs_for_profiles(profiles, weights, "B")
        c, a, b = convention_b_parameters(weights)
        expected = predicted_coeffs_from_bivariate_gf(profiles, c, a, b)
        assert observed == expected


def test_radius_covariance_and_simple_branch_convention_a() -> None:
    radii = set()
    for weights in ADMISSIBLE_WEIGHTS:
        _, a, b = convention_a_parameters(weights)
        r = discriminant_radius(a, b)
        radii.add(round(r, 12))
        assert 0 < r < 1
        assert discriminant_derivative(a, b, r) < 0

    assert len(radii) >= 2


def test_radius_covariance_and_simple_branch_convention_b() -> None:
    radii = set()
    for weights in ADMISSIBLE_WEIGHTS:
        _, a, b = convention_b_parameters(weights)
        r = discriminant_radius(a, b)
        radii.add(round(r, 12))
        assert 0 < r < 1
        assert discriminant_derivative(a, b, r) < 0

    assert len(radii) >= 2
