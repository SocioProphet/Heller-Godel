from fractions import Fraction

from heller_godel.dimension_spectrum import (
    decompose_sn_character,
    factorial_order_symmetric,
    regular_sn_decomposition,
    sn_class_sizes,
    sn_irreps,
    on_off_multiplicities,
)
from heller_godel.emr_complex import f_vector, reduced_betti, sigma_lambda, stabilizer, vertex_labels
from heller_godel.emr_decomposition import (
    decompose_lambda,
    partial_sum_positivity_rate,
    reduced_euler_matches_betti,
    sign_excess,
    sign_profile,
)


def test_sn_character_tables_burnside_for_3_4_5():
    for n in (3, 4, 5):
        dims = [irrep.dimension for irrep in sn_irreps(n)]
        assert sum(dim * dim for dim in dims) == factorial_order_symmetric(n)
        assert sum(sn_class_sizes(n).values()) == factorial_order_symmetric(n)


def test_regular_sn_decomposition_uses_irrep_dimensions():
    decomp = regular_sn_decomposition(4)
    assert decomp["trivial"] == 1
    assert decomp["sign"] == 1
    assert decomp["partition_22"] == 2
    assert decomp["standard"] == 3
    assert decomp["standard_twist"] == 3


def test_decompose_regular_character_S3():
    character = {(1, 1, 1): 6, (2, 1): 0, (3,): 0}
    assert decompose_sn_character(character, 3) == regular_sn_decomposition(3)


def test_on_off_observables_regular_S4():
    obs = on_off_multiplicities(regular_sn_decomposition(4), 4)
    assert obs["m_circle"] == 2
    assert obs["m_off"] == 8
    assert obs["mu_off"] == Fraction(31, 12)
    assert obs["R"] == Fraction(1, 5)


def test_emr_figure_1_decomposition_smoke():
    lam = (5, 1, -2, -3)
    complex_ = sigma_lambda(lam)
    assert vertex_labels(complex_) == ("{1}", "{2}", "{1,2}", "{1,3}", "{1,4}", "{1,2,3}", "{1,2,4}")
    assert f_vector(complex_) == (7, 12, 6)
    result = decompose_lambda(lam)
    assert result.n == 4
    assert result.stabilizer_order == 1
    assert result.homology_dimension == sum(reduced_betti(complex_))
    assert result.m_circle >= 0
    assert result.m_off >= 0
    assert Fraction(0) <= result.ratio <= Fraction(1)


def test_sign_profile_observables():
    lam = (5, 1, -2, -3)
    assert sign_profile(lam) == (1, 1, -1, -1)
    assert sign_excess(lam) == 0
    assert partial_sum_positivity_rate(lam) == Fraction(4, 4)


def test_reduced_euler_matches_betti_for_emr_row():
    assert reduced_euler_matches_betti(sigma_lambda((5, 1, -2, -3)))


def test_stabilizer_detects_repeated_coordinates():
    assert len(stabilizer((1, 1, -1, -1))) == 4


def test_emr_decomposition_docstring_guards():
    import inspect
    import heller_godel.emr_decomposition as emr_decomposition

    doc = inspect.getdoc(emr_decomposition)
    assert "does not reproduce" in doc
    assert "P vs NP" in doc
    assert "RH, GRH, Artin" in doc
