from heller_godel.young_cayley_atlas import (
    s4_legacy_vs_young_emr_agree,
    young_atlas_rows,
    young_block_eigenvalues,
    young_generator_sets,
)


def test_young_atlas_covers_s3_s4_s5_generator_sets():
    sets = young_generator_sets()
    assert set(sets) == {3, 4, 5}
    assert len(sets[3]) == 2
    assert len(sets[4]) == 4
    assert len(sets[5]) == 2


def test_S4_pr162_and_young_orthogonal_agree_on_emr_row():
    # Both matrix realizations of S4's irreps must yield identical block
    # eigenvalues on the locked sanity row. This is the deduplication gate for
    # retiring the PR #162 fixtures later.
    assert s4_legacy_vs_young_emr_agree()


def test_young_atlas_has_expected_row_count():
    rows = young_atlas_rows()
    # S3: 2 generator sets * 3 irreps; S4: 4 * 5; S5: 2 * 7.
    assert len(rows) == (2 * 3) + (4 * 5) + (2 * 7)


def test_young_atlas_partition_counts_are_group_invariant():
    for row in young_atlas_rows():
        n = int(row["group"][1:])
        assert row["vertices"] == {3: 6, 4: 24, 5: 120}[n]
        assert row["on_circle_count"] == 2
        assert row["off_circle_count"] == {3: 4, 4: 22, 5: 118}[n]
        assert row["total_count"] == {3: 6, 4: 24, 5: 120}[n]


def test_young_block_eigenvalues_known_samples():
    generators = young_generator_sets()[3]["transposition_12_cycle_123"]
    from heller_godel.cayley_spectrum import symmetrize_generators

    sym = symmetrize_generators(generators)
    assert young_block_eigenvalues(3, "trivial", sym) == (3.0,)
    assert young_block_eigenvalues(3, "sign", sym) == (-1.0,)


def test_young_atlas_rows_have_block_eigenvalues_for_every_irrep():
    for row in young_atlas_rows():
        assert row["block_eigs"] != ""
        assert row["irrep_dim"] >= 1
        assert row["symmetric"] == 1
        assert row["trace"] == 0
