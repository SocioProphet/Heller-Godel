#!/usr/bin/env python3
"""Analyze HG-EXP-008.7 omega cost-scaling CSV output."""

from __future__ import annotations

import argparse
import csv
import json
from math import log, sqrt
from pathlib import Path


def load_rows(path: Path) -> list[dict[str, float | str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    parsed: list[dict[str, float | str]] = []
    for row in rows:
        parsed.append(
            {
                "omega": float(row["omega"]),
                "magnitude_band": row["magnitude_band"],
                "log2_n": float(row["log2_n"]),
                "arity_log_sum": float(row["arity_log_sum"]),
                "usp_ops": float(row["usp_ops"]),
                "period_ops": float(row["period_ops"]),
            }
        )
    return parsed


def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [list(col) for col in zip(*matrix)]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def matvec(a: list[list[float]], b: list[float]) -> list[float]:
    return [sum(x * y for x, y in zip(row, b)) for row in a]


def invert(matrix: list[list[float]]) -> list[list[float]]:
    n = len(matrix)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-12:
            raise ValueError("singular design matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [a - factor * b for a, b in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def ols(y: list[float], x: list[list[float]]) -> dict[str, object]:
    xt = transpose(x)
    xtx = matmul(xt, x)
    xtx_inv = invert(xtx)
    beta = matvec(xtx_inv, matvec(xt, y))
    fitted = [sum(b * xi for b, xi in zip(beta, row)) for row in x]
    residuals = [yi - fi for yi, fi in zip(y, fitted)]
    n = len(y)
    k = len(beta)
    rss = sum(r * r for r in residuals)
    sigma2 = rss / max(1, n - k)
    stderr = [sqrt(max(0.0, sigma2 * xtx_inv[i][i])) for i in range(k)]
    ci95 = [[b - 1.96 * s, b + 1.96 * s] for b, s in zip(beta, stderr)]
    aic = n * log(max(rss / n, 1e-12)) + 2 * k
    return {
        "coefficients": beta,
        "stderr": stderr,
        "ci95": ci95,
        "rss": rss,
        "residual_standard_error": sqrt(sigma2),
        "aic": aic,
        "n": n,
        "k": k,
    }


def design(rows: list[dict[str, float | str]], include_arity: bool) -> list[list[float]]:
    matrix: list[list[float]] = []
    for row in rows:
        values = [1.0, float(row["omega"]), float(row["log2_n"])]
        if include_arity:
            values.append(float(row["arity_log_sum"] ))
        matrix.append(values)
    return matrix


def fit_curve(rows: list[dict[str, float | str]], cost_field: str) -> dict[str, object]:
    filtered = [row for row in rows if float(row[cost_field]) > 0]
    y = [log(float(row[cost_field]), 2) for row in filtered]
    model_a = ols(y, design(filtered, include_arity=False))
    model_b = ols(y, design(filtered, include_arity=True))
    return {
        "cost_field": cost_field,
        "model_a_terms": ["intercept", "omega", "log2_n"],
        "model_b_terms": ["intercept", "omega", "log2_n", "arity_log_sum"],
        "model_a": model_a,
        "model_b": model_b,
        "delta_aic_b_minus_a": float(model_b["aic"]) - float(model_a["aic"]),
    }


def analyze(path: Path) -> dict[str, object]:
    rows = load_rows(path)
    cells: dict[str, int] = {}
    for row in rows:
        key = f"omega={int(float(row['omega']))}|band={row['magnitude_band']}"
        cells[key] = cells.get(key, 0) + 1
    return {
        "source_csv": str(path),
        "row_count": len(rows),
        "cells": dict(sorted(cells.items())),
        "curves": {
            "structured_usp": fit_curve(rows, "usp_ops"),
            "period_finding": fit_curve(rows, "period_ops"),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=Path("data/exp_008_7_results.csv"))
    parser.add_argument("--out", type=Path, default=Path("reports/exp_008_7_fit.json"))
    args = parser.parse_args()

    result = analyze(args.csv)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
