"""Cayley-spectrum calibration utilities for HG-EXP-008.9.

This module stages the finite Cayley graph positive-control instrument for the
HG-MTH-008.6 dimension-spectrum coordinate. It constructs finite permutation
groups, right-multiplication Cayley adjacency matrices, and the on-circle
trivial/sign eigenvalues for small symmetric groups.

Matrix-realization convention for tranche 2: real orthogonal realizations
compatible with Young's orthogonal convention. For S4, the standard irrep is the
orthogonal action on the sum-zero subspace of R^4; the 2-dimensional (2,2)
irrep is the orthogonal action on the sum-zero subspace of the three perfect
matchings of {1,2,3,4}; and the sign-twist is sign tensor standard. This fixes a
single basis convention for every S4 matrix fixture in this module. Matrix
entries are basis-dependent; traces and block eigenvalues are basis-invariant.

Boundary guard: this is finite-group empirical infrastructure only. It has no
P vs NP implication, no RH/GRH/Artin implication, no expander or Ramanujan claim
without explicit spectral-gap analysis, and no extension to infinite groups,
Lie groups, or real reductive groups.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from math import sqrt

from heller_godel.dimension_spectrum import (
    abelian_core_fraction,
    cycle_type,
    sn_irreps,
    symmetric_group,
)


Permutation = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]
RealMatrix = tuple[tuple[float, ...], ...]


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


def is_symmetric_matrix(matrix: Matrix | RealMatrix, tolerance: float = 1e-9) -> bool:
    return all(abs(matrix[i][j] - matrix[j][i]) <= tolerance for i in range(len(matrix)) for j in range(len(matrix)))


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


def _perm_matrix(perm: Permutation) -> RealMatrix:
    n = len(perm)
    rows = [[0.0 for _ in range(n)] for _ in range(n)]
    for i, image in enumerate(perm):
        rows[image][i] = 1.0
    return tuple(tuple(row) for row in rows)


def _transpose(matrix: RealMatrix) -> RealMatrix:
    return tuple(tuple(matrix[j][i] for j in range(len(matrix))) for i in range(len(matrix[0])))


def _matmul(left: RealMatrix, right: RealMatrix) -> RealMatrix:
    rows = len(left)
    cols = len(right[0])
    inner = len(right)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(inner)) for j in range(cols))
        for i in range(rows)
    )


def _scalar_mul(scalar: float, matrix: RealMatrix) -> RealMatrix:
    return tuple(tuple(scalar * value for value in row) for row in matrix)


def matrix_trace(matrix: RealMatrix) -> float:
    return sum(matrix[i][i] for i in range(len(matrix)))


def _basis_matrix(columns: tuple[tuple[float, ...], ...]) -> RealMatrix:
    return tuple(tuple(column[row] for column in columns) for row in range(len(columns[0])))


def _restrict_orthogonal(matrix: RealMatrix, basis_columns: tuple[tuple[float, ...], ...]) -> RealMatrix:
    basis = _basis_matrix(basis_columns)
    return _matmul(_matmul(_transpose(basis), matrix), basis)


def _matching_key(matching: tuple[frozenset[int], frozenset[int]]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return tuple(sorted((tuple(sorted(pair)) for pair in matching)))  # type: ignore[return-value]


S4_MATCHINGS: tuple[tuple[frozenset[int], frozenset[int]], ...] = (
    (frozenset((0, 1)), frozenset((2, 3))),
    (frozenset((0, 2)), frozenset((1, 3))),
    (frozenset((0, 3)), frozenset((1, 2))),
)


def _matching_perm_matrix(perm: Permutation) -> RealMatrix:
    rows = [[0.0 for _ in range(3)] for _ in range(3)]
    keys = [_matching_key(matching) for matching in S4_MATCHINGS]
    for col, matching in enumerate(S4_MATCHINGS):
        image = tuple(frozenset(perm[item] for item in pair) for pair in matching)
        row = keys.index(_matching_key(image))  # type: ignore[arg-type]
        rows[row][col] = 1.0
    return tuple(tuple(row) for row in rows)


S4_STANDARD_BASIS: tuple[tuple[float, ...], ...] = (
    (1 / sqrt(2), -1 / sqrt(2), 0.0, 0.0),
    (1 / sqrt(6), 1 / sqrt(6), -2 / sqrt(6), 0.0),
    (1 / sqrt(12), 1 / sqrt(12), 1 / sqrt(12), -3 / sqrt(12)),
)


S4_MATCHING_BASIS: tuple[tuple[float, ...], ...] = (
    (1 / sqrt(2), -1 / sqrt(2), 0.0),
    (1 / sqrt(6), 1 / sqrt(6), -2 / sqrt(6)),
)


def s4_irrep_matrix(label: str, perm: Permutation) -> RealMatrix:
    """Return one S4 irrep matrix in the documented orthogonal convention."""

    if len(perm) != 4:
        raise ValueError("S4 irrep fixtures require a permutation of length 4")
    if label == "trivial":
        return ((1.0,),)
    if label == "sign":
        return ((float(permutation_sign(perm)),),)
    if label == "standard":
        return _restrict_orthogonal(_perm_matrix(perm), S4_STANDARD_BASIS)
    if label == "standard_twist":
        return _scalar_mul(float(permutation_sign(perm)), s4_irrep_matrix("standard", perm))
    if label == "partition_22":
        return _restrict_orthogonal(_matching_perm_matrix(perm), S4_MATCHING_BASIS)
    raise KeyError(f"unknown S4 irrep label: {label}")


def s4_character_from_matrix(label: str, perm: Permutation) -> float:
    return matrix_trace(s4_irrep_matrix(label, perm))


def s4_character_table_value(label: str, perm: Permutation) -> int:
    for irrep in sn_irreps(4):
        if irrep.label == label:
            return irrep.character_by_cycle_type[cycle_type(perm)]
    raise KeyError(label)


def verify_s4_trace_matches_character(tolerance: float = 1e-9) -> bool:
    for perm in symmetric_group_elements(4):
        for irrep in sn_irreps(4):
            if abs(s4_character_from_matrix(irrep.label, perm) - s4_character_table_value(irrep.label, perm)) > tolerance:
                return False
    return True


def _add_matrices(matrices: tuple[RealMatrix, ...]) -> RealMatrix:
    if not matrices:
        raise ValueError("expected at least one matrix")
    rows = len(matrices[0])
    cols = len(matrices[0][0])
    return tuple(
        tuple(sum(matrix[i][j] for matrix in matrices) for j in range(cols))
        for i in range(rows)
    )


def s4_block_matrix(label: str, generators: tuple[Permutation, ...]) -> RealMatrix:
    return _add_matrices(tuple(s4_irrep_matrix(label, generator) for generator in generators))


def symmetric_eigenvalues(matrix: RealMatrix, tolerance: float = 1e-12) -> tuple[float, ...]:
    """Compute eigenvalues of a small real symmetric matrix by Jacobi iteration."""

    n = len(matrix)
    if n == 1:
        return (matrix[0][0],)
    a = [list(row) for row in matrix]
    for _ in range(100):
        p, q = 0, 1
        max_value = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > max_value:
                    max_value = abs(a[i][j])
                    p, q = i, j
        if max_value <= tolerance:
            break
        if abs(a[p][p] - a[q][q]) <= tolerance:
            angle = 0.7853981633974483
        else:
            angle = 0.5 * __import__("math").atan2(2 * a[p][q], a[q][q] - a[p][p])
        c = __import__("math").cos(angle)
        s = __import__("math").sin(angle)
        app = c * c * a[p][p] - 2 * s * c * a[p][q] + s * s * a[q][q]
        aqq = s * s * a[p][p] + 2 * s * c * a[p][q] + c * c * a[q][q]
        a[p][q] = a[q][p] = 0.0
        a[p][p] = app
        a[q][q] = aqq
        for r in range(n):
            if r in (p, q):
                continue
            arp = c * a[r][p] - s * a[r][q]
            arq = s * a[r][p] + c * a[r][q]
            a[r][p] = a[p][r] = arp
            a[r][q] = a[q][r] = arq
    return tuple(sorted(a[i][i] for i in range(n)))


def s4_block_eigenvalues(label: str, generators: tuple[Permutation, ...]) -> tuple[float, ...]:
    block = s4_block_matrix(label, generators)
    if not is_symmetric_matrix(block):
        raise ValueError("block matrix is not symmetric; symmetrize generators first")
    return symmetric_eigenvalues(block)


def s4_off_circle_eigenvalues(generators: tuple[Permutation, ...]) -> dict[str, tuple[float, ...]]:
    return {
        "partition_22": s4_block_eigenvalues("partition_22", generators),
        "standard": s4_block_eigenvalues("standard", generators),
        "standard_twist": s4_block_eigenvalues("standard_twist", generators),
    }


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
        "off_circle_blocks": s4_off_circle_eigenvalues(generators),
    }
