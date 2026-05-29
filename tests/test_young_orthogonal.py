import inspect

from heller_godel.cayley_spectrum import compose, identity, is_symmetric_matrix, symmetric_group_elements
from heller_godel.dimension_spectrum import sn_irreps
from heller_godel.young_orthogonal import (
    PARTITIONS_BY_LABEL,
    adjacent_transposition_matrix,
    reduced_word,
    standard_tableaux,
    table_character_value,
    verify_young_traces,
    young_character_value,
    young_matrix,
)


def test_standard_tableaux_counts_match_irrep_dimensions():
    for n in (3, 4, 5):
        dims = {irrep.label: irrep.dimension for irrep in sn_irreps(n)}
        for label, shape in PARTITIONS_BY_LABEL[n].items():
            assert len(standard_tableaux(shape)) == dims[label]


def test_adjacent_transposition_matrices_are_symmetric_orthogonal():
    shape = PARTITIONS_BY_LABEL[5]["partition_32"]
    for i in range(1, 5):
        matrix = adjacent_transposition_matrix(shape, i)
        assert is_symmetric_matrix(matrix)
        product = tuple(
            tuple(sum(matrix[k][i0] * matrix[k][j0] for k in range(len(matrix))) for j0 in range(len(matrix)))
            for i0 in range(len(matrix))
        )
        for row_index, row in enumerate(product):
            for col_index, value in enumerate(row):
                assert abs(value - (1.0 if row_index == col_index else 0.0)) <= 1e-8


def test_reduced_word_reconstructs_permutations():
    from heller_godel.young_orthogonal import adjacent_generators

    for n in (3, 4, 5):
        gens = adjacent_generators(n)
        for perm in symmetric_group_elements(n):
            current = identity(n)
            for index in reduced_word(perm):
                current = compose(current, gens[index - 1])
            assert current == perm


def test_young_traces_match_character_tables_S3_S4_S5():
    assert verify_young_traces(3)
    assert verify_young_traces(4)
    assert verify_young_traces(5)


def test_young_trace_gate_explicit_samples():
    samples = [
        (3, "standard", (1, 2, 0)),
        (4, "partition_22", (1, 0, 3, 2)),
        (5, "partition_311", (1, 2, 3, 4, 0)),
    ]
    for n, label, perm in samples:
        assert abs(young_character_value(n, label, perm) - table_character_value(n, label, perm)) <= 1e-8


def test_young_matrices_have_expected_dimensions():
    for n in (3, 4, 5):
        dims = {irrep.label: irrep.dimension for irrep in sn_irreps(n)}
        for label in PARTITIONS_BY_LABEL[n]:
            matrix = young_matrix(n, label, identity(n))
            assert len(matrix) == dims[label]
            assert len(matrix[0]) == dims[label]


def test_young_orthogonal_docstring_declares_basis_convention():
    import heller_godel.young_orthogonal as young_orthogonal

    doc = inspect.getdoc(young_orthogonal)
    assert "Young orthogonal basis" in doc
    assert "trace equality" in doc
    assert "basis-dependent" in doc
