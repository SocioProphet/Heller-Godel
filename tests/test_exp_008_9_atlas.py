import csv
from pathlib import Path

from scripts.exp_008_9_cayley_atlas import atlas_rows, write_csv


def test_atlas_rows_cover_four_s4_generator_sets():
    rows = atlas_rows()
    assert len(rows) == 4
    assert {row["generator_set"] for row in rows} == {
        "emr_1432_132",
        "transposition_12_cycle_1234",
        "adjacent_transpositions",
        "star_transpositions",
    }


def test_emr_s4_atlas_row_locked():
    row = next(row for row in atlas_rows() if row["generator_set"] == "emr_1432_132")
    assert row["vertices"] == 24
    assert row["degree"] == 4
    assert row["trace"] == 0
    assert row["on_circle"] == "4 0"
    assert row["on_circle_count"] == 2
    assert row["off_circle_count"] == 22
    assert row["total_count"] == 24
    assert row["alpha"] == "1/12"
    assert row["partition_22_eigs"] == "-3 1"
    assert row["standard_twist_eigs"] == "-1 0 3"


def test_all_s4_atlas_rows_have_invariant_partition_counts():
    for row in atlas_rows():
        assert row["group"] == "S4"
        assert row["vertices"] == 24
        assert row["on_circle_count"] == 2
        assert row["off_circle_count"] == 22
        assert row["total_count"] == 24
        assert row["alpha"] == "1/12"


def test_atlas_writer_reproduces_csv(tmp_path: Path):
    out = tmp_path / "exp_008_9_results.csv"
    write_csv(out)
    with out.open(newline="", encoding="utf-8") as handle:
        generated = list(csv.DictReader(handle))
    committed_path = Path("data/exp_008_9_results.csv")
    with committed_path.open(newline="", encoding="utf-8") as handle:
        committed = list(csv.DictReader(handle))
    assert generated == committed
