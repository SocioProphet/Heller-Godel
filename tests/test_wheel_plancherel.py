import pytest

from heller_godel.wheel_plancherel import (
    PrimePower,
    USPCertificate,
    character_orthogonality_holds,
    constant_trivial_character,
    euler_phi,
    factorization_from_usp,
    group_exponent_from_factorization,
    is_cyclic_by_enumeration,
    is_cyclic_wheel_modulus,
    order_mod,
    plancherel_holds,
    primorial,
    units_mod,
    usp,
    validate_usp_solution,
)


def oracle(n):
    fixtures = {
        15: ((3, 1), (5, 1)),
        45: ((3, 2), (5, 1)),
        210: ((2, 1), (3, 1), (5, 1), (7, 1)),
    }
    return fixtures[n]


def test_usp_with_oracle_is_poly():
    cert = usp(210, factoring_oracle=oracle)
    assert validate_usp_solution(cert, 210)
    assert [(pp.p, pp.e) for pp in cert.factorization] == [(2, 1), (3, 1), (5, 1), (7, 1)]


def test_usp_output_recovers_factorization():
    cert = usp(45)
    assert [(pp.p, pp.e) for pp in factorization_from_usp(cert)] == [(3, 2), (5, 1)]


def test_factoring_reduces_to_usp():
    assert [(pp.p, pp.e) for pp in usp(84).factorization] == [(2, 2), (3, 1), (7, 1)]


def test_cyclic_wheel_predicate_matches_closed_form():
    for n in range(1, 10_001):
        assert is_cyclic_wheel_modulus(n) == is_cyclic_by_enumeration(n)


def test_prime_modulus_has_single_generator():
    cert = usp(17)
    assert len(cert.cyclic_decomposition) == 1
    part = cert.cyclic_decomposition[0]
    assert part.order == 16
    assert order_mod(part.generator, 17) == 16


def test_composite_noncyclic_requires_crt_split():
    cert = usp(15)
    assert [part.order for part in cert.cyclic_decomposition] == [2, 4]
    assert not is_cyclic_wheel_modulus(15)


def test_plancherel_identity_holds_on_G_n():
    n = 13
    values = {u: complex((u % 5) - 2, (u % 3) - 1) for u in units_mod(n)}
    assert plancherel_holds(n, values)


def test_character_orthogonality():
    assert character_orthogonality_holds(17)


def test_constant_function_is_not_usp_solution():
    bare = constant_trivial_character(15)
    assert bare["structured"] is False
    assert not validate_usp_solution(bare, 15)


def test_withholding_factorization_blocks_structured_chi0():
    bare = constant_trivial_character(21)
    with pytest.raises(ValueError):
        factorization_from_usp(
            USPCertificate(
                n=21,
                factorization=(),
                cyclic_decomposition=(),
                chi0_coordinates=(),
                structured=False,
            )
        )
    assert "factorization" not in bare


def test_wheel_P4_equals_G_210():
    assert primorial(4) == 210
    assert units_mod(primorial(4)) == units_mod(210)
    assert euler_phi(210) == 48


def test_character_values_in_mu_12_at_P4():
    assert group_exponent_from_factorization(usp(primorial(4)).factorization) == 12
