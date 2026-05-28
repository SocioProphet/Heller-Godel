import inspect
from fractions import Fraction

from heller_godel.dimension_spectrum import (
    STANDARD_SPECTRA,
    abelian_core_fraction,
    abelianization_count,
    analogy_not_equality_guard,
    assert_boundary_equivalence,
    beta,
    boundary_functional,
    cyclic_group,
    dim_spectrum,
    factorial_order_symmetric,
    kappa,
    known_family,
    plancherel_measure,
    symmetric_group,
    verify_burnside,
    wheel_group,
)


def test_burnside_sum_of_squares_Zn():
    for n in [1, 2, 5, 12]:
        assert verify_burnside(cyclic_group(n))


def test_burnside_sum_of_squares_S3():
    assert dim_spectrum(symmetric_group(3)) == (1, 1, 2)
    assert verify_burnside(symmetric_group(3))


def test_burnside_sum_of_squares_S4():
    assert dim_spectrum(symmetric_group(4)) == (1, 1, 2, 3, 3)
    assert verify_burnside(symmetric_group(4))


def test_burnside_sum_of_squares_S5():
    assert dim_spectrum(symmetric_group(5)) == (1, 1, 4, 4, 5, 5, 6)
    assert verify_burnside(symmetric_group(5))
    assert symmetric_group(5).order == factorial_order_symmetric(5) == 120


def test_burnside_sum_of_squares_Q8():
    assert dim_spectrum(STANDARD_SPECTRA["Q8"]) == (1, 1, 1, 1, 2)
    assert verify_burnside(STANDARD_SPECTRA["Q8"])


def test_burnside_sum_of_squares_D4():
    assert dim_spectrum(STANDARD_SPECTRA["D4"]) == (1, 1, 1, 1, 2)
    assert verify_burnside(STANDARD_SPECTRA["D4"])


def test_beta_one_iff_abelian():
    for group in known_family():
        assert (beta(group) == 1) == group.abelian
        assert assert_boundary_equivalence(group)


def test_kappa_zero_iff_abelian():
    for group in known_family():
        assert (kappa(group) == 0) == group.abelian


def test_plancherel_uniform_iff_abelian():
    for group in known_family():
        assert (len(set(plancherel_measure(group))) == 1) == group.abelian


def test_abelianization_count_equals_G_mod_commutator():
    for group in known_family():
        assert abelianization_count(group) == group.abelianization_order
    assert abelian_core_fraction(symmetric_group(3)) == Fraction(2, 6)


def test_Sn_has_exactly_two_one_dim_irreps():
    for n in [2, 3, 4, 5]:
        assert abelianization_count(symmetric_group(n)) == 2


def test_wheel_spectrum_all_ones():
    group = wheel_group(210)
    assert group.order == 48
    assert set(dim_spectrum(group)) == {1}
    assert len(dim_spectrum(group)) == 48


def test_wheel_on_circle():
    for n in [1, 2, 15, 210]:
        group = wheel_group(n)
        assert boundary_functional(group) == {"beta": 1, "kappa": 0, "abelian": True}


def test_Sn_off_circle():
    for n in [3, 4, 5]:
        group = symmetric_group(n)
        assert beta(group) > 1
        assert kappa(group) > 0


def test_no_dim_equals_delta_assertion():
    import heller_godel.dimension_spectrum as dimension_spectrum

    text = inspect.getsource(dimension_spectrum)
    guard = analogy_not_equality_guard()
    assert "dim rho = delta is forbidden" in text
    assert "dim rho = delta" in guard
    assert "dim_rho" not in text
    assert "delta_is_dim" not in text


def test_module_docstring_states_boundary_only_not_separation():
    import heller_godel.dimension_spectrum as dimension_spectrum

    doc = inspect.getdoc(dimension_spectrum)
    assert "re-coordinatizes" in doc
    assert "does not cross" in doc
    assert "No separation" in doc
    assert "never equal to" in doc
