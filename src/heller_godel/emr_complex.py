"""EMR Coxeter sub-complex construction routines for HG-EXP-008.8.

This module implements the finite combinatorial core only: ordered set
partitions, the EMR positive-partial-sum sub-complex Sigma(lambda), f-vectors,
reduced rational Betti numbers, and stabilizers of lambda under S_n.

Boundary posture: this is an exploratory empirical experiment support module.
It does not claim to reproduce, improve, or contradict EMR's identities. It
does not compute L^2-cohomology of Siegel modular varieties or Shimura
varieties. It has no P vs NP implication and no RH, GRH, Artin, or motives
implication.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from typing import Iterable


Block = tuple[int, ...]
OrderedPartition = tuple[Block, ...]
Simplex = tuple[frozenset[int], ...]


@dataclass(frozen=True)
class SigmaComplex:
    """Finite simplicial complex encoded as chains of positive proper subsets."""

    n: int
    lam: tuple[int | float, ...]
    faces: frozenset[Simplex]

    @property
    def faces_by_dim(self) -> tuple[tuple[Simplex, ...], ...]:
        if not self.faces:
            return ()
        max_dim = max(len(face) - 1 for face in self.faces)
        grouped: list[list[Simplex]] = [[] for _ in range(max_dim + 1)]
        for face in self.faces:
            grouped[len(face) - 1].append(face)
        return tuple(tuple(sorted(group, key=_simplex_sort_key)) for group in grouped)

    @property
    def vertices(self) -> tuple[frozenset[int], ...]:
        if not self.faces:
            return ()
        verts = {face[0] for face in self.faces if len(face) == 1}
        return tuple(sorted(verts, key=_subset_sort_key))


def _subset_sort_key(subset: frozenset[int]) -> tuple[int, tuple[int, ...]]:
    return (len(subset), tuple(sorted(subset)))


def _simplex_sort_key(simplex: Simplex) -> tuple[tuple[int, tuple[int, ...]], ...]:
    return tuple(_subset_sort_key(vertex) for vertex in simplex)


def subset_label(subset: Iterable[int]) -> str:
    """Return the EMR-figure-style label for a subset, for exact sanity tests."""

    return "{" + ",".join(str(i) for i in sorted(subset)) + "}"


def vertex_labels(complex_: SigmaComplex) -> tuple[str, ...]:
    """Return sorted vertex labels for Sigma(lambda)."""

    return tuple(subset_label(vertex) for vertex in complex_.vertices)


def ordered_set_partitions(n: int) -> tuple[OrderedPartition, ...]:
    """Enumerate all ordered set partitions of [n] = {1,...,n}.

    Counts are the ordered Bell/Fubini numbers: 13 for n=3, 75 for n=4,
    and 541 for n=5. The empty n=0 case is included only as the recursion
    base and returns the unique empty ordered partition.
    """

    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return ((),)

    previous = ordered_set_partitions(n - 1)
    out: list[OrderedPartition] = []
    seen: set[OrderedPartition] = set()

    for partition in previous:
        # Insert n into each existing block.
        for block_index in range(len(partition)):
            blocks = [list(block) for block in partition]
            blocks[block_index].append(n)
            candidate = tuple(tuple(sorted(block)) for block in blocks)
            if candidate not in seen:
                seen.add(candidate)
                out.append(candidate)

        # Insert n as a new singleton block at every ordered position.
        for position in range(len(partition) + 1):
            blocks = tuple(tuple(block) for block in partition)
            candidate = blocks[:position] + ((n,),) + blocks[position:]
            if candidate not in seen:
                seen.add(candidate)
                out.append(candidate)

    return tuple(out)


def _chain_from_partition(partition: OrderedPartition) -> Simplex:
    running: set[int] = set()
    chain: list[frozenset[int]] = []
    for block in partition[:-1]:
        running.update(block)
        chain.append(frozenset(running))
    return tuple(chain)


def _partial_sums_positive(partition: OrderedPartition, lam: tuple[int | float, ...]) -> bool:
    running: set[int] = set()
    for block in partition[:-1]:
        running.update(block)
        if sum(lam[index - 1] for index in running) <= 0:
            return False
    return True


def sigma_lambda(lam: Iterable[int | float]) -> SigmaComplex:
    """Construct Sigma(lambda) from EMR's positive-partial-sum rule.

    A non-empty face is encoded by the chain of proper initial unions attached
    to an ordered partition B_1|...|B_k with k >= 2. The k=1 ordered partition
    corresponds only to the empty face and is not listed among non-empty faces.
    """

    lam_tuple = tuple(lam)
    if not lam_tuple:
        raise ValueError("lambda must have at least one coordinate")

    n = len(lam_tuple)
    faces: set[Simplex] = set()
    for partition in ordered_set_partitions(n):
        if len(partition) < 2:
            continue
        if _partial_sums_positive(partition, lam_tuple):
            faces.add(_chain_from_partition(partition))

    return SigmaComplex(n=n, lam=lam_tuple, faces=frozenset(faces))


def f_vector(complex_: SigmaComplex) -> tuple[int, ...]:
    """Return the non-empty f-vector by dimension."""

    return tuple(len(group) for group in complex_.faces_by_dim)


def reduced_euler_characteristic(complex_: SigmaComplex) -> int:
    """Return reduced Euler characteristic: -1 + sum_d (-1)^d f_d."""

    if not complex_.faces:
        return 0
    return -1 + sum(((-1) ** dim) * count for dim, count in enumerate(f_vector(complex_)))


def _boundary_rank(
    domain: tuple[Simplex, ...],
    codomain: tuple[Simplex, ...],
) -> int:
    if not domain or not codomain:
        return 0
    row_index = {face: i for i, face in enumerate(codomain)}
    matrix = [[Fraction(0) for _ in domain] for _ in codomain]
    for col, face in enumerate(domain):
        for remove_index in range(len(face)):
            boundary_face = face[:remove_index] + face[remove_index + 1 :]
            matrix[row_index[boundary_face]][col] += Fraction((-1) ** remove_index)
    return _rank_fraction_matrix(matrix)


def _rank_fraction_matrix(matrix: list[list[Fraction]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows = [row[:] for row in matrix]
    n_rows = len(rows)
    n_cols = len(rows[0])
    rank = 0

    for col in range(n_cols):
        pivot = None
        for row in range(rank, n_rows):
            if rows[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue

        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][col]
        rows[rank] = [entry / pivot_value for entry in rows[rank]]

        for row in range(n_rows):
            if row == rank or rows[row][col] == 0:
                continue
            factor = rows[row][col]
            rows[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(rows[row], rows[rank], strict=True)
            ]

        rank += 1
        if rank == n_rows:
            break

    return rank


def reduced_betti(complex_: SigmaComplex) -> tuple[int, ...]:
    """Compute reduced Betti numbers over Q for the non-empty dimensions."""

    faces_by_dim = complex_.faces_by_dim
    if not faces_by_dim:
        return ()

    max_dim = len(faces_by_dim) - 1
    boundary_ranks = [0 for _ in range(max_dim + 2)]
    for dim in range(1, max_dim + 1):
        boundary_ranks[dim] = _boundary_rank(faces_by_dim[dim], faces_by_dim[dim - 1])

    betti: list[int] = []
    for dim in range(max_dim + 1):
        chain_dim = len(faces_by_dim[dim])
        ordinary = chain_dim - boundary_ranks[dim] - boundary_ranks[dim + 1]
        if dim == 0:
            ordinary -= 1
        betti.append(ordinary)

    while betti and betti[-1] == 0:
        betti.pop()
    return tuple(betti)


def stabilizer(lam: Iterable[int | float]) -> tuple[tuple[int, ...], ...]:
    """Return permutations of zero-based coordinates preserving lambda exactly."""

    lam_tuple = tuple(lam)
    n = len(lam_tuple)
    out = []
    for perm in permutations(range(n)):
        if tuple(lam_tuple[perm[i]] for i in range(n)) == lam_tuple:
            out.append(tuple(perm))
    return tuple(out)


def permute_lambda(lam: Iterable[int | float], perm: Iterable[int]) -> tuple[int | float, ...]:
    """Apply a zero-based coordinate permutation to lambda."""

    lam_tuple = tuple(lam)
    perm_tuple = tuple(perm)
    if sorted(perm_tuple) != list(range(len(lam_tuple))):
        raise ValueError("perm must be a permutation of zero-based coordinate indices")
    return tuple(lam_tuple[perm_tuple[i]] for i in range(len(lam_tuple)))


def full_coxeter_f_vector(n: int) -> tuple[int, ...]:
    """Return the f-vector of the full Coxeter complex of S_n."""

    return f_vector(sigma_lambda([1] * n))
