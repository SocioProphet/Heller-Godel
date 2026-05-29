from fractions import Fraction

from heller_godel.cayley_spectrum import (
    adjacency_trace,
    block_count_by_irrep,
    cayley_adjacency,
    compose,
    cycle_perm,
    identity,
    inverse,
    is_symmetric_matrix,
    on_off_summary_symmetric_group,
    permutation_sign,
    row_sums,
    s4_emr_generators,
    s4_emr_sanity,
    sign_on_circle_value,
    symmetric_group_elements,
    symmetrize_generators,
    trivial_on_circle_value,
)


def test_permutation_group_helpers():
    g = cycle_perm(4, (1, 4, 3, 2))
    assert compose(g, inverse(g)) == identity(4)
    assert permutation_sign(g) == -1
    assert permutation_sign(cycle_perm(4, (1, 3, 2))) == 1


def test_s4_emr_generators_symmetrize_to_four():
    generators = symmetrize_generators(s4_emr_generators())
    assert len(generators) == 4
    assert all(inverse(generator) in generators for generator in generators)


def test_emr_image_S4_cayley_on_circle_eigenvalues():
    generators = symmetrize_generators(s4_emr_generators())
    assert trivial_on_circle_value(generators) == 4
    assert sign_on_circle_value(generators) == 0
    assert on_off_summary_symmetric_group(4, generators).on_circle == (4, 0)


def test_emr_image_S4_cayley_trace_zero():
    generators = symmetrize_generators(s4_emr_generators())
    data = cayley_adjacency(symmetric_group_elements(4), generators)
    assert adjacency_trace(data.adjacency) == 0


def test_emr_image_S4_cayley_total_count():
    summary = on_off_summary_symmetric_group(4, symmetrize_generators(s4_emr_generators()))
    assert summary.total_count == 24
    assert summary.on_circle_count == 2
    assert summary.off_circle_count == 22


def test_symmetric_cayley_adjacency_is_symmetric_and_regular():
    generators = symmetrize_generators(s4_emr_generators())
    data = cayley_adjacency(symmetric_group_elements(4), generators)
    assert is_symmetric_matrix(data.adjacency)
    assert set(row_sums(data.adjacency)) == {4}


def test_directed_cayley_adjacency_can_be_asymmetric():
    g, h = s4_emr_generators()
    data = cayley_adjacency(symmetric_group_elements(4), (g, h))
    assert not is_symmetric_matrix(data.adjacency)


def test_burnside_total_eigenvalue_count_S3_S4_S5():
    for n in (3, 4, 5):
        counts = block_count_by_irrep(n)
        assert sum(counts.values()) == len(symmetric_group_elements(n))


def test_on_circle_count_equals_G_ab():
    for n in (3, 4, 5):
        summary = on_off_summary_symmetric_group(n, symmetrize_generators((cycle_perm(n, (1, 2)),)))
        assert summary.on_circle_count == 2
        assert summary.alpha == Fraction(2, len(symmetric_group_elements(n)))


def test_s4_emr_sanity_locked_row():
    sanity = s4_emr_sanity()
    assert sanity["vertices"] == 24
    assert sanity["degree"] == 4
    assert sanity["symmetric"] is True
    assert sanity["trace"] == 0
    assert sanity["on_circle"] == (4, 0)
    assert sanity["on_circle_count"] == 2
    assert sanity["off_circle_count"] == 22
    assert sanity["total_count"] == 24
    assert sanity["alpha"] == Fraction(1, 12)


def test_cayley_spectrum_docstring_boundaries():
    import inspect
    import heller_godel.cayley_spectrum as cayley_spectrum

    doc = inspect.getdoc(cayley_spectrum)
    assert "P vs NP" in doc
    assert "RH/GRH/Artin" in doc
    assert "expander or Ramanujan" in doc
    assert "infinite groups" in doc
