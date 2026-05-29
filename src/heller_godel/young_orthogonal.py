"""Young-orthogonal matrix fixtures for small symmetric groups.

The convention is fixed once here: standard tableaux form the orthonormal Young orthogonal basis. Adjacent transpositions act by the usual seminormal/orthogonal
2x2 rule on tableau pairs. All downstream Cayley-spectrum experiments must use
this convention rather than mixing Specht-polytabloid or other bases.

Matrix entries are basis-dependent. The invariant gate is trace equality against
the character tables in ``dimension_spectrum.sn_irreps`` for every group element.
"""

from __future__ import annotations

from collections import deque
from functools import lru_cache
from math import sqrt

from heller_godel.cayley_spectrum import Permutation, RealMatrix, compose, identity, cycle_perm, symmetric_group_elements
from heller_godel.dimension_spectrum import cycle_type, sn_irreps


Tableau = tuple[tuple[int, ...], ...]


PARTITIONS_BY_LABEL: dict[int, dict[str, tuple[int, ...]]] = {
    3: {
        "trivial": (3,),
        "sign": (1, 1, 1),
        "standard": (2, 1),
    },
    4: {
        "trivial": (4,),
        "sign": (1, 1, 1, 1),
        "partition_22": (2, 2),
        "standard": (3, 1),
        "standard_twist": (2, 1, 1),
    },
    5: {
        "trivial": (5,),
        "sign": (1, 1, 1, 1, 1),
        "partition_41": (4, 1),
        "partition_2111": (2, 1, 1, 1),
        "partition_32": (3, 2),
        "partition_221": (2, 2, 1),
        "partition_311": (3, 1, 1),
    },
}


def _cells(shape: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    return tuple((row, col) for row, width in enumerate(shape) for col in range(width))


def _is_standard(entries: dict[tuple[int, int], int], shape: tuple[int, ...]) -> bool:
    for row, width in enumerate(shape):
        for col in range(width - 1):
            if entries[(row, col)] >= entries[(row, col + 1)]:
                return False
    for row in range(len(shape) - 1):
        for col in range(min(shape[row], shape[row + 1])):
            if entries[(row, col)] >= entries[(row + 1, col)]:
                return False
    return True


@lru_cache(maxsize=None)
def standard_tableaux(shape: tuple[int, ...]) -> tuple[Tableau, ...]:
    cells = _cells(shape)
    n = len(cells)
    out: list[Tableau] = []

    def rec(index: int, remaining: tuple[int, ...], entries: dict[tuple[int, int], int]) -> None:
        if index == n:
            if _is_standard(entries, shape):
                out.append(tuple(tuple(entries[(row, col)] for col in range(width)) for row, width in enumerate(shape)))
            return
        cell = cells[index]
        for value in remaining:
            new_entries = dict(entries)
            new_entries[cell] = value
            rec(index + 1, tuple(x for x in remaining if x != value), new_entries)

    rec(0, tuple(range(1, n + 1)), {})
    return tuple(sorted(out))


def _positions(tableau: Tableau) -> dict[int, tuple[int, int]]:
    out = {}
    for row, values in enumerate(tableau):
        for col, value in enumerate(values):
            out[value] = (row, col)
    return out


def _swap_values(tableau: Tableau, a: int, b: int) -> Tableau:
    return tuple(tuple(b if x == a else a if x == b else x for x in row) for row in tableau)


def _matmul(left: RealMatrix, right: RealMatrix) -> RealMatrix:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def _identity_matrix(size: int) -> RealMatrix:
    return tuple(tuple(1.0 if i == j else 0.0 for j in range(size)) for i in range(size))


def matrix_trace(matrix: RealMatrix) -> float:
    return sum(matrix[i][i] for i in range(len(matrix)))


def adjacent_transposition_matrix(shape: tuple[int, ...], i: int) -> RealMatrix:
    """Return the Young-orthogonal matrix for adjacent transposition s_i."""

    tabs = standard_tableaux(shape)
    index = {tab: k for k, tab in enumerate(tabs)}
    size = len(tabs)
    matrix = [[0.0 for _ in range(size)] for _ in range(size)]
    visited: set[Tableau] = set()
    for tab in tabs:
        if tab in visited:
            continue
        pos = _positions(tab)
        row_i, col_i = pos[i]
        row_j, col_j = pos[i + 1]
        k = index[tab]
        if row_i == row_j:
            matrix[k][k] = 1.0
            visited.add(tab)
            continue
        if col_i == col_j:
            matrix[k][k] = -1.0
            visited.add(tab)
            continue
        swapped = _swap_values(tab, i, i + 1)
        l = index[swapped]
        if swapped in visited:
            continue
        r = (col_j - row_j) - (col_i - row_i)
        a = 1.0 / r
        b = sqrt(max(0.0, 1.0 - a * a))
        matrix[k][k] = a
        matrix[l][l] = -a
        matrix[k][l] = b
        matrix[l][k] = b
        visited.add(tab)
        visited.add(swapped)
    return tuple(tuple(row) for row in matrix)


@lru_cache(maxsize=None)
def adjacent_generators(n: int) -> tuple[Permutation, ...]:
    return tuple(cycle_perm(n, (i, i + 1)) for i in range(1, n))


@lru_cache(maxsize=None)
def reduced_word(perm: Permutation) -> tuple[int, ...]:
    """Return adjacent-generator indices whose right product is perm.

    n<=5 in this fixture layer, so a small BFS is simpler and safer than a
    hand-rolled convention-sensitive bubble-sort word.
    """

    n = len(perm)
    start = identity(n)
    if perm == start:
        return ()
    gens = adjacent_generators(n)
    queue = deque([(start, ())])
    seen = {start}
    while queue:
        current, word = queue.popleft()
        for index, gen in enumerate(gens, start=1):
            nxt = compose(current, gen)
            if nxt == perm:
                return word + (index,)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, word + (index,)))
    raise ValueError("failed to find adjacent-generator word")


def young_matrix_by_shape(shape: tuple[int, ...], perm: Permutation) -> RealMatrix:
    tabs = standard_tableaux(shape)
    result = _identity_matrix(len(tabs))
    generators = {i + 1: adjacent_transposition_matrix(shape, i + 1) for i in range(len(perm) - 1)}
    current = identity(len(perm))
    for gen_index in reduced_word(perm):
        result = _matmul(result, generators[gen_index])
        current = compose(current, adjacent_generators(len(perm))[gen_index - 1])
    if current != perm:
        raise AssertionError("reduced word did not reconstruct permutation")
    return result


def young_matrix(n: int, label: str, perm: Permutation) -> RealMatrix:
    return young_matrix_by_shape(PARTITIONS_BY_LABEL[n][label], perm)


def young_character_value(n: int, label: str, perm: Permutation) -> float:
    return matrix_trace(young_matrix(n, label, perm))


def table_character_value(n: int, label: str, perm: Permutation) -> int:
    ctype = cycle_type(perm)
    for irrep in sn_irreps(n):
        if irrep.label == label:
            return irrep.character_by_cycle_type[ctype]
    raise KeyError(label)


def verify_young_traces(n: int, tolerance: float = 1e-8) -> bool:
    for perm in symmetric_group_elements(n):
        for irrep in sn_irreps(n):
            if abs(young_character_value(n, irrep.label, perm) - table_character_value(n, irrep.label, perm)) > tolerance:
                return False
    return True
