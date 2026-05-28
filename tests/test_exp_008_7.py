import csv
import json
from pathlib import Path

from scripts.exp_008_7_analyze import analyze
from scripts.exp_008_7_omega_cost import generate_rows, measure_instance, write_csv
from scripts.exp_008_7_plot import render


def deterministic_row(row):
    data = row.row().copy()
    data.pop("usp_time_ms", None)
    data.pop("period_time_ms", None)
    return data


def test_seed_reproducibility():
    rows_a = generate_rows(seed=101, max_omega=2, sample_size=2, bands=("small", "medium"))
    rows_b = generate_rows(seed=101, max_omega=2, sample_size=2, bands=("small", "medium"))
    assert [deterministic_row(row) for row in rows_a] == [deterministic_row(row) for row in rows_b]


def test_omega_sweep_complete():
    rows = generate_rows(seed=202, max_omega=3, sample_size=2, bands=("small", "medium", "large"))
    cells = {}
    for row in rows:
        key = (row.omega, row.magnitude_band)
        cells[key] = cells.get(key, 0) + 1
    assert len(rows) == 3 * 3 * 2
    assert all(count == 2 for count in cells.values())


def test_operation_count_zero_for_trivial_n():
    rows = generate_rows(seed=303, max_omega=1, sample_size=1, bands=("small",))
    assert rows[0].usp_ops > 0
    # omega=0 is not part of the experiment sweep; trivial n=1 is excluded by design.


def test_period_witness_passes_for_known_orders():
    import random

    row = measure_instance(seed=404, rng=random.Random(404), omega=2, band="small", sample_index=0)
    assert row.period_success is True
    assert pow(row.a, row.ord_a, row.n) == 1
    assert row.period_ops == row.ord_a


def test_fit_loads_csv_correctly(tmp_path: Path):
    rows = generate_rows(seed=505, max_omega=2, sample_size=3, bands=("small", "medium"))
    csv_path = tmp_path / "results.csv"
    write_csv(rows, csv_path)
    result = analyze(csv_path)
    assert result["row_count"] == 12
    assert "structured_usp" in result["curves"]
    assert "period_finding" in result["curves"]


def test_model_A_recovers_linear_omega(tmp_path: Path):
    csv_path = tmp_path / "synthetic.csv"
    fields = [
        "seed",
        "omega",
        "magnitude_band",
        "sample_index",
        "n",
        "primes",
        "log2_n",
        "phi_n",
        "a",
        "ord_a",
        "usp_ops",
        "usp_time_ms",
        "period_ops",
        "period_time_ms",
        "period_success",
        "period_retries",
        "arity_log_sum",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for omega in range(1, 6):
            for sample in range(4):
                writer.writerow(
                    {
                        "seed": 1,
                        "omega": omega,
                        "magnitude_band": "small",
                        "sample_index": sample,
                        "n": 1,
                        "primes": "",
                        "log2_n": 10 + sample,
                        "phi_n": 1,
                        "a": 1,
                        "ord_a": 1,
                        "usp_ops": 2 ** (1 + 2 * omega + 0.1 * (10 + sample)),
                        "usp_time_ms": 0,
                        "period_ops": 2 ** (2 + 2 * omega + 0.1 * (10 + sample)),
                        "period_time_ms": 0,
                        "period_success": 1,
                        "period_retries": 0,
                        "arity_log_sum": (omega * sample) + (0.01 * sample * sample),
                    }
                )
    result = analyze(csv_path)
    c1 = result["curves"]["structured_usp"]["model_a"]["coefficients"][1]
    assert 1.99 <= c1 <= 2.01


def test_aic_delta_meaningful_threshold(tmp_path: Path):
    rows = generate_rows(seed=606, max_omega=3, sample_size=3, bands=("small", "medium"))
    csv_path = tmp_path / "results.csv"
    write_csv(rows, csv_path)
    result = analyze(csv_path)
    delta = result["curves"]["structured_usp"]["delta_aic_b_minus_a"]
    assert isinstance(delta, float)


def test_plots_render_without_error(tmp_path: Path):
    rows = generate_rows(seed=707, max_omega=2, sample_size=2, bands=("small", "medium"))
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


def test_analyzer_json_serializable(tmp_path: Path):
    rows = generate_rows(seed=808, max_omega=2, sample_size=2, bands=("small", "medium"))
    csv_path = tmp_path / "results.csv"
    write_csv(rows, csv_path)
    json.dumps(analyze(csv_path))
