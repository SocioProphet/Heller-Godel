"""Cayley-spectrum calibration utilities for HG-EXP-008.9.

This module stages the finite Cayley graph positive-control instrument for the
HG-MTH-008.6 dimension-spectrum coordinate. It constructs finite permutation
groups, right-multiplication Cayley adjacency matrices, and the on-circle
trivial/sign eigenvalues for small symmetric groups.

Boundary guard: this is finite-group empirical infrastructure only. It has no
P vs NP implication, no RH/GRH/Artin implication, no expander or Ramanujan claim
without explicit spectral-gap analysis, and no extension to infinite groups,
Lie groups, or real reductive groups.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations

from heller_godel.dimension_spectrum import abelian_core_fraction, sn_irreps, symmetric_group


Permutation = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class CayleyData:
    group: tuple[Permutation, ...]
    generators: tuple[Permutation, ...]
    adjacency: Matrix
    index: dict[Permutation, int]


@dataclass(frozen=True)
class OnOffSpectrumSummary:
    on_circle: tuple[int, int]
    on_circle_count: int
    off_circle_count: int
    alpha: Fraction
    total_count: int


def identity(n: int) -> Permutation:
    return tuple(range(n))


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right for zero-based permutations."""

    if len(left) != len(right):
        raise ValueError("permutations must have the same size")
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(perm: Permutation) -> Permutation:
    out = [0] * len(perm)
    for i, image in enumerate(perm):
        out[image] = i
    return tuple(out)


def cycle_perm(n: int, cycle: tuple[int, ...]) -> Permutation:
    """Build a zero-based permutation from one one-based cycle."""

    out = list(range(n))
    if not cycle:
        return tuple(out)
    zero = [value - 1 for value in cycle]
    for current, nxt in zip(zero, zero[1:] + zero[:1]):
        out[current] = nxt
    return tuple(out)


def symmetric_group_elements(n: int) -> tuple[Permutation, ...]:
    return tuple(permutations(range(n)))


def permutation_sign(perm: Permutation) -> int:
    inversions = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] > perm[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


def symmetrize_generators(generators: tuple[Permutation, ...]) -> tuple[Permutation, ...]:
    out: list[Permutation] = []
    for gen in generators:
        for candidate in (gen, inverse(gen)):
            if candidate not in out:
                out.append(candidate)
    return tuple(out)


def cayley_adjacency(group: tuple[Permutation, ...], generators: tuple[Permutation, ...]) -> CayleyData:
    index = {element: i for i, element in enumerate(group)}
    size = len(group)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for row, element in enumerate(group):
        for gen in generators:
            target = compose(element, gen)
            matrix[row][index[target]] += 1
    return CayleyData(
        group=group,
        generators=generators,
        adjacency=tuple(tuple(row) for row in matrix),
        index=index,
    )


def adjacency_trace(matrix: Matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def is_symmetric_matrix(matrix: Matrix) -> bool:
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(len(matrix)))


def row_sums(matrix: Matrix) -> tuple[int, ...]:
    return tuple(sum(row) for row in matrix)


def trivial_on_circle_value(generators: tuple[Permutation, ...]) -> int:
    return len(generators)


def sign_on_circle_value(generators: tuple[Permutation, ...]) -> int:
    return sum(permutation_sign(gen) for gen in generators)


def block_count_by_irrep(n: int) -> dict[str, int]:
    return {irrep.label: irrep.dimension * irrep.dimension for irrep in sn_irreps(n)}


def on_off_summary_symmetric_group(n: int, generators: tuple[Permutation, ...]) -> OnOffSpectrumSummary:
    group = symmetric_group(n)
    counts = block_count_by_irrep(n)
    on_count = counts["trivial"] + counts["sign"]
    total = sum(counts.values())
    return OnOffSpectrumSummary(
        on_circle=(trivial_on_circle_value(generators), sign_on_circle_value(generators)),
        on_circle_count=on_count,
        off_circle_count=total - on_count,
        alpha=abelian_core_fraction(group),
        total_count=total,
    )


def s4_emr_generators() -> tuple[Permutation, Permutation]:
    """Return g=(1,4,3,2) and h=(1,3,2) as zero-based permutations."""

    return (cycle_perm(4, (1, 4, 3, 2)), cycle_perm(4, (1, 3, 2)))


def s4_emr_sanity() -> dict[str, object]:
    generators = symmetrize_generators(s4_emr_generators())
    data = cayley_adjacency(symmetric_group_elements(4), generators)
    summary = on_off_summary_symmetric_group(4, generators)
    return {
        "vertices": len(data.group),
        "degree": tuple(sorted(set(row_sums(data.adjacency))))[0],
        "symmetric": is_symmetric_matrix(data.adjacency),
        "trace": adjacency_trace(data.adjacency),
        "on_circle": summary.on_circle,
        "on_circle_count": summary.on_circle_count,
        "off_circle_count": summary.off_circle_count,
        "total_count": summary.total_count,
        "alpha": summary.alpha,
    }
