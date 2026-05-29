"""Young-orthogonal Cayley atlas rows for HG-EXP-008.9.

This module extends the S4 positive-control atlas to S3 and S5 using the single
Young orthogonal convention in ``young_orthogonal.py``. It also compares the
legacy hand-built S4 matrix fixtures from PR #162 with the unified Young path on
the locked EMR sanity row.
"""

from __future__ import annotations

import csv
from pathlib import Path

from heller_godel.cayley_spectrum import (
    Permutation,
    adjacency_trace,
    cayley_adjacency,
    cycle_perm,
    is_symmetric_matrix,
    on_off_summary_symmetric_group,
    row_sums,
    s4_block_eigenvalues,
    s4_emr_generators,
    symmetric_eigenvalues,
    symmetric_group_elements,
    symmetrize_generators,
)
from heller_godel.dimension_spectrum import sn_irreps
from heller_godel.young_orthogonal import young_matrix


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
    "irrep_label",
    "irrep_dim",
    "block_eigs",
)


def young_generator_sets() -> dict[int, dict[str, tuple[Permutation, ...]]]:
    return {
        3: {
            "transposition_12_cycle_123": (cycle_perm(3, (1, 2)), cycle_perm(3, (1, 2, 3))),
            "two_transpositions_12_13": (cycle_perm(3, (1, 2)), cycle_perm(3, (1, 3))),
        },
        4: {
            "emr_1432_132": s4_emr_generators(),
            "transposition_12_cycle_1234": (cycle_perm(4, (1, 2)), cycle_perm(4, (1, 2, 3, 4))),
            "adjacent_transpositions": (cycle_perm(4, (1, 2)), cycle_perm(4, (2, 3)), cycle_perm(4, (3, 4))),
            "star_transpositions": (cycle_perm(4, (1, 2)), cycle_perm(4, (1, 3)), cycle_perm(4, (1, 4))),
        },
        5: {
            "transposition_12_cycle_12345": (cycle_perm(5, (1, 2)), cycle_perm(5, (1, 2, 3, 4, 5))),
            "adjacent_transpositions": (
                cycle_perm(5, (1, 2)),
                cycle_perm(5, (2, 3)),
                cycle_perm(5, (3, 4)),
                cycle_perm(5, (4, 5)),
            ),
        },
    }


def _normalize(value: float, tolerance: float = 1e-10) -> float:
    return 0.0 if abs(value) <= tolerance else value


def fmt_eigs(values: tuple[float, ...]) -> str:
    return " ".join(f"{_normalize(value):.12g}" for value in values)


def _add_matrices(matrices):
    rows = len(matrices[0])
    cols = len(matrices[0][0])
    return tuple(
        tuple(sum(matrix[i][j] for matrix in matrices) for j in range(cols))
        for i in range(rows)
    )


def young_block_matrix(n: int, label: str, generators: tuple[Permutation, ...]):
    return _add_matrices(tuple(young_matrix(n, label, gen) for gen in generators))


def young_block_eigenvalues(n: int, label: str, generators: tuple[Permutation, ...]) -> tuple[float, ...]:
    block = young_block_matrix(n, label, generators)
    if not is_symmetric_matrix(block):
        raise ValueError("block matrix is not symmetric; symmetrize generators first")
    return symmetric_eigenvalues(block)


def young_atlas_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n, sets in young_generator_sets().items():
        group = symmetric_group_elements(n)
        for set_name, raw_generators in sets.items():
            generators = symmetrize_generators(raw_generators)
            data = cayley_adjacency(group, generators)
            summary = on_off_summary_symmetric_group(n, generators)
            degree_values = tuple(sorted(set(row_sums(data.adjacency))))
            for irrep in sn_irreps(n):
                rows.append(
                    {
                        "group": f"S{n}",
                        "generator_set": set_name,
                        "generator_count": len(generators),
                        "vertices": len(group),
                        "degree": degree_values[0],
                        "symmetric": int(is_symmetric_matrix(data.adjacency)),
                        "trace": adjacency_trace(data.adjacency),
                        "on_circle": " ".join(str(value) for value in summary.on_circle),
                        "on_circle_count": summary.on_circle_count,
                        "off_circle_count": summary.off_circle_count,
                        "total_count": summary.total_count,
                        "alpha": f"{summary.alpha.numerator}/{summary.alpha.denominator}",
                        "irrep_label": irrep.label,
                        "irrep_dim": irrep.dimension,
                        "block_eigs": fmt_eigs(young_block_eigenvalues(n, irrep.label, generators)),
                    }
                )
    return rows


def s4_legacy_vs_young_emr_agree(tolerance: float = 1e-8) -> bool:
    generators = symmetrize_generators(s4_emr_generators())
    pairs = {
        "partition_22": "partition_22",
        "standard": "standard",
        "standard_twist": "standard_twist",
    }
    for legacy_label, young_label in pairs.items():
        legacy = s4_block_eigenvalues(legacy_label, generators)
        young = young_block_eigenvalues(4, young_label, generators)
        if len(legacy) != len(young):
            return False
        for left, right in zip(legacy, young):
            if abs(left - right) > tolerance:
                return False
    return True


def write_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(young_atlas_rows())
