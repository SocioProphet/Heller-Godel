"""Reusable S4 Cayley spectrum atlas rows for HG-EXP-008.9.

This module keeps atlas construction inside the installed package. Scripts only
write artifacts; tests verify the package-level rows against committed data.
"""

from __future__ import annotations

import csv
from pathlib import Path

from heller_godel.cayley_spectrum import (
    adjacency_trace,
    cayley_adjacency,
    cycle_perm,
    is_symmetric_matrix,
    on_off_summary_symmetric_group,
    row_sums,
    s4_block_eigenvalues,
    s4_emr_generators,
    symmetric_group_elements,
    symmetrize_generators,
)


CSV_FIELDS = (
    "group",
    "generator_set",
    "generator_count",
    "vertices",
    "degree",
    "symmetric",
    "trace",
    "on_circle",
    "on_circle_count",
    "off_circle_count",
    "total_count",
    "alpha",
    "partition_22_eigs",
    "standard_eigs",
    "standard_twist_eigs",
)


def s4_generator_sets():
    return {
        "emr_1432_132": s4_emr_generators(),
        "transposition_12_cycle_1234": (cycle_perm(4, (1, 2)), cycle_perm(4, (1, 2, 3, 4))),
        "adjacent_transpositions": (cycle_perm(4, (1, 2)), cycle_perm(4, (2, 3)), cycle_perm(4, (3, 4))),
        "star_transpositions": (cycle_perm(4, (1, 2)), cycle_perm(4, (1, 3)), cycle_perm(4, (1, 4))),
    }


def fmt_eigs(values: tuple[float, ...]) -> str:
    return " ".join(f"{value:.12g}" for value in values)


def atlas_rows() -> list[dict[str, object]]:
    group = symmetric_group_elements(4)
    rows: list[dict[str, object]] = []
    for name, raw_generators in s4_generator_sets().items():
        generators = symmetrize_generators(raw_generators)
        data = cayley_adjacency(group, generators)
        summary = on_off_summary_symmetric_group(4, generators)
        rows.append(
            {
                "group": "S4",
                "generator_set": name,
                "generator_count": len(generators),
                "vertices": len(group),
                "degree": tuple(sorted(set(row_sums(data.adjacency))))[0],
                "symmetric": int(is_symmetric_matrix(data.adjacency)),
                "trace": adjacency_trace(data.adjacency),
                "on_circle": " ".join(str(value) for value in summary.on_circle),
                "on_circle_count": summary.on_circle_count,
                "off_circle_count": summary.off_circle_count,
                "total_count": summary.total_count,
                "alpha": f"{summary.alpha.numerator}/{summary.alpha.denominator}",
                "partition_22_eigs": fmt_eigs(s4_block_eigenvalues("partition_22", generators)),
                "standard_eigs": fmt_eigs(s4_block_eigenvalues("standard", generators)),
                "standard_twist_eigs": fmt_eigs(s4_block_eigenvalues("standard_twist", generators)),
            }
        )
    return rows


def write_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(atlas_rows())
