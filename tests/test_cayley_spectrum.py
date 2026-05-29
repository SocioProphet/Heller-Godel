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
    s4_block_eigenvalues,
    s4_character_from_matrix,
    s4_character_table_value,
    s4_emr_generators,
    s4_emr_sanity,
    s4_irrep_matrix,
    sign_on_circle_value,
    symmetric_group_elements,
    symmetrize_generators,
    trivial_on_circle_value,
    verify_s4_trace_matches_character,
)


def assert_close_tuple(actual, expected, tolerance=1e-8):
    assert len(actual) == len(expected)
    for got, want in zip(actual, expected):
        assert abs(got - want) <= tolerance


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


def test_s4_trace_matches_character_table_for_every_fixture():
    assert verify_s4_trace_matches_character()
    for perm in symmetric_group_elements(4):
        for label in ("trivial", "sign", "partition_22", "standard", "standard_twist"):
            assert abs(s4_character_from_matrix(label, perm) - s4_character_table_value(label, perm)) <= 1e-8


def test_s4_irrep_matrices_are_orthogonal_fixtures():
    perm = cycle_perm(4, (1, 4, 3, 2))
    for label in ("partition_22", "standard", "standard_twist"):
        matrix = s4_irrep_matrix(label, perm)
        product = tuple(
            tuple(sum(matrix[k][i] * matrix[k][j] for k in range(len(matrix))) for j in range(len(matrix)))
            for i in range(len(matrix))
        )
        for i, row in enumerate(product):
            for j, value in enumerate(row):
                assert abs(value - (1.0 if i == j else 0.0)) <= 1e-8


def test_emr_image_S4_off_circle_fixture_values():
    generators = symmetrize_generators(s4_emr_generators())
    assert_close_tuple(s4_block_eigenvalues("partition_22", generators), (-3.0, 1.0))
    assert_close_tuple(
        s4_block_eigenvalues("standard", generators),
        (-2.56155281280883, -1.0, 1.56155281280883),
    )
    assert_close_tuple(s4_block_eigenvalues("standard_twist", generators), (-1.0, 0.0, 3.0))


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
    assert_close_tuple(sanity["off_circle_blocks"]["partition_22"], (-3.0, 1.0))


def test_cayley_spectrum_docstring_boundaries_and_basis():
    import inspect
    import heller_godel.cayley_spectrum as cayley_spectrum

    doc = inspect.getdoc(cayley_spectrum)
    assert "Young's orthogonal" in doc
    assert "P vs NP" in doc
    assert "RH/GRH/Artin" in doc
    assert "expander or Ramanujan" in doc
    assert "infinite groups" in doc
