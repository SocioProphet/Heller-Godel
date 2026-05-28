import inspect

import pytest

from heller_godel.abelian_hsp import (
    RetryReduction,
    abelian_boundary_statement,
    annihilator,
    annihilator_step,
    dft,
    dft_support,
    fourier_sample_period,
    hiding_function,
    order_finding_classical,
    period_comb,
    shor_reduction,
    subgroup_character_exponents,
    wheel_p4_context,
    wheel_period_dft_support,
)
from heller_godel.wheel_plancherel import group_exponent_from_factorization, primorial, usp


def test_shor_reduction_recovers_factor():
    factors = shor_reduction(n=15, a=7, r=4)
    assert sorted(factors) == [3, 5]


def test_order_is_period_of_hiding_function():
    f = hiding_function(a=7, n=15)
    assert f.period == order_finding_classical(7, 15) == 4
    for x in range(12):
        assert f(x) == f(x + f.period)


def test_reduction_handles_bad_a():
    with pytest.raises(RetryReduction):
        shor_reduction(n=15, a=14, r=2)  # a^(r/2) == -1 mod n
    with pytest.raises(RetryReduction):
        shor_reduction(n=21, a=4, r=3)  # odd order


def test_dft_period_r_divides_Q_is_clean_comb():
    support = dft_support(dft(period_comb(period=4, Q=16), Q=16))
    assert support == annihilator(period=4, Q=16) == (0, 4, 8, 12)


def test_dft_period_r_not_dividing_Q_leakage():
    result = fourier_sample_period(a=7, n=15, Q=253)
    assert result["period"] == 4
    assert result["recovered_period"] == 4
    assert len(result["frequencies"]) > 4  # visible leakage because r does not divide Q


def test_annihilator_duality():
    Q = 16
    period = 4
    h_perp_step = annihilator_step(period, Q)
    h_again_step = annihilator_step(h_perp_step, Q)
    assert h_perp_step == 4
    assert h_again_step == period
    assert annihilator(period, Q) == (0, 4, 8, 12)


def test_fourier_recovers_order():
    result = fourier_sample_period(a=7, n=15, Q=16)
    assert result["recovered_period"] == order_finding_classical(7, 15) == 4


def test_unit_modulus_has_trivial_period():
    f = hiding_function(a=1, n=1)
    result = fourier_sample_period(a=1, n=1, Q=8)
    assert f.period == 1
    assert result["period"] == result["recovered_period"] == 1
    assert tuple(result["frequencies"]) == (0,)


def test_prime_cyclic_wheel_single_subgroup():
    assert order_finding_classical(3, 7) == 6
    f = hiding_function(a=3, n=7)
    assert sorted({f(x) for x in range(f.period)}) == sorted([1, 2, 3, 4, 5, 6])


def test_subgroup_character_table_matches_dft_support():
    r = order_finding_classical(7, 15)
    support = wheel_period_dft_support(a=7, n=15, Q=16)
    assert subgroup_character_exponents(r) == (0, 1, 2, 3)
    assert support == tuple(k * (16 // r) for k in subgroup_character_exponents(r))


def test_wheel_P4_period_extraction_in_mu_context():
    context = wheel_p4_context()
    assert context == {"P4": 210, "unit_count": 48, "mu_exponent": 12}
    assert primorial(4) == 210
    assert group_exponent_from_factorization(usp(210).factorization) == 12
    assert order_finding_classical(11, 210) == 6


def test_abelian_hsp_boundary_documented():
    import heller_godel.abelian_hsp as abelian_hsp

    text = inspect.getdoc(abelian_hsp)
    assert "abelian case" in text
    assert "does not provide a fast classical period-finder" in text
    assert "P vs NP" in text
    assert "non-abelian world" in abelian_boundary_statement()
