import csv
import json
from pathlib import Path
import random

from scripts.exp_008_7_analyze import analyze
from scripts.exp_008_7_omega_cost import generate_rows, measure_instance, sample_primes, write_csv
from scripts.exp_008_7_plot import render


def deterministic_row(row):
    data = row.row().copy()
    data.pop("usp_time_ms", None)
    data.pop("period_time_ms", None)
    return data


def test_seed_reproducibility_small_band():
    rows_a = generate_rows(seed=101, max_omega=2, sample_size=2, bands=("small",))
    rows_b = generate_rows(seed=101, max_omega=2, sample_size=2, bands=("small",))
    assert [deterministic_row(row) for row in rows_a] == [deterministic_row(row) for row in rows_b]


def test_omega_sweep_complete_small_band():
    rows = generate_rows(seed=202, max_omega=3, sample_size=2, bands=("small",))
    cells = {}
    for row in rows:
        key = (row.omega, row.magnitude_band)
        cells[key] = cells.get(key, 0) + 1
    assert len(rows) == 6
    assert all(count == 2 for count in cells.values())


def test_large_band_sampling_without_measurement():
    primes = sample_primes(random.Random(203), omega=2, band="large")
    assert len(primes) == 2
    assert all(10_000 <= prime <= 100_000 for prime in primes)


def test_period_witness_passes_for_known_orders():
    row = measure_instance(seed=404, rng=random.Random(404), omega=2, band="small", sample_index=0)
    assert row.period_success is True
    assert pow(row.a, row.ord_a, row.n) == 1
    assert row.period_ops == row.ord_a


def test_analyzer_outputs_models(tmp_path: Path):
    rows = generate_rows(seed=505, max_omega=3, sample_size=3, bands=("small",))
    csv_path = tmp_path / "results.csv"
    write_csv(rows, csv_path)
    result = analyze(csv_path)
    assert result["row_count"] == 9
    structured = result["curves"]["structured_usp"]
    assert structured["model_a_terms"] == ["intercept", "omega", "log2_n"]
    assert structured["model_b_terms"] == ["intercept", "omega", "log2_n", "arity_log_sum"]
    assert len(structured["model_a"]["coefficients"]) == 3
    assert len(structured["model_b"]["coefficients"]) == 4
    json.dumps(result)


def test_plots_render_without_error(tmp_path: Path):
    rows = generate_rows(seed=707, max_omega=2, sample_size=2, bands=("small",))
    csv_path = tmp_path / "results.csv"
    write_csv(rows, csv_path)
    with csv_path.open(newline="", encoding="utf-8") as handle:
        loaded = list(csv.DictReader(handle))
    usp_png = tmp_path / "usp.png"
    period_png = tmp_path / "period.png"
    render(loaded, "usp_ops", usp_png)
    render(loaded, "period_ops", period_png)
    png_magic = bytes([137, 80, 78, 71])
    assert usp_png.read_bytes().startswith(png_magic)
    assert period_png.read_bytes().startswith(png_magic)
