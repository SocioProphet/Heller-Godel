"""Representation-decomposition helpers for HG-EXP-008.8.

This module is the tranche-2 bridge between the EMR Coxeter sub-complex
construction and the dimension-spectrum coordinate from HG-MTH-008.6.

It computes finite, empirical observables only. It does not reproduce, improve,
or contradict EMR's automorphic identities; it does not compute L2-cohomology of
Siegel modular varieties; and it has no P vs NP, RH, GRH, Artin, or motives
implication.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations

from heller_godel.dimension_spectrum import (
    regular_sn_decomposition,
    sn_irreps,
    on_off_multiplicities,
)
from heller_godel.emr_complex import (
    SigmaComplex,
    reduced_betti,
    reduced_euler_characteristic,
    sigma_lambda,
    stabilizer,
)


@dataclass(frozen=True)
class EMRDecomposition:
    """Computed on/off-circle decomposition observables for one lambda."""

    n: int
    lam: tuple[int | float, ...]
    betti: tuple[int, ...]
    homology_dimension: int
    stabilizer_order: int
    decomposition: dict[str, int]
    m_circle: int
    m_off: int
    mu_off: Fraction
    ratio: Fraction


def sign_profile(lam: tuple[int | float, ...]) -> tuple[int, ...]:
    """Return coordinate signs as -1, 0, or 1."""

    return tuple(1 if value > 0 else -1 if value < 0 else 0 for value in lam)


def sign_excess(lam: tuple[int | float, ...]) -> int:
    profile = sign_profile(lam)
    return sum(1 for value in profile if value > 0) - sum(1 for value in profile if value < 0)


def partial_sum_positivity_rate(lam: tuple[int | float, ...]) -> Fraction:
    if not lam:
        return Fraction(0)
    running = 0
    positive = 0
    for value in lam:
        running += value
        if running > 0:
            positive += 1
    return Fraction(positive, len(lam))


def total_reduced_homology_dimension(complex_: SigmaComplex) -> int:
    return sum(reduced_betti(complex_))


def decompose_lambda(lam: tuple[int | float, ...]) -> EMRDecomposition:
    """Compute the current empirical S_n-decomposition proxy for lambda.

    For the generic-trivial-stabilizer case, Ind_1^{S_n}(Q^d) is d copies of
    the regular representation, so each S_n irrep appears with multiplicity
    d*dim(rho). Nontrivial stabilizer homology-character extraction is recorded
    as a later extension; for now we conservatively use the same regular proxy
    when homology is nonzero and report stabilizer_order for filtering.
    """

    complex_ = sigma_lambda(lam)
    betti = reduced_betti(complex_)
    hom_dim = sum(betti)
    stab = stabilizer(lam)
    decomp = regular_sn_decomposition(len(lam), scalar=hom_dim) if hom_dim else {
        irrep.label: 0 for irrep in sn_irreps(len(lam))
    }
    observables = on_off_multiplicities(decomp, len(lam))
    return EMRDecomposition(
        n=len(lam),
        lam=tuple(lam),
        betti=betti,
        homology_dimension=hom_dim,
        stabilizer_order=len(stab),
        decomposition=decomp,
        m_circle=int(observables["m_circle"]),
        m_off=int(observables["m_off"]),
        mu_off=observables["mu_off"],
        ratio=observables["R"],
    )


def lemma_37_f_vector_orbit(lam: tuple[int | float, ...]) -> tuple[tuple[int, tuple[int, ...]], ...]:
    """Return f-vectors for all coordinate permutations of lambda."""

    from heller_godel.emr_complex import f_vector

    out = []
    for perm in permutations(range(len(lam))):
        permuted = tuple(lam[index] for index in perm)
        out.append((f_vector(sigma_lambda(permuted)), perm))
    return tuple(out)


def reduced_euler_matches_betti(complex_: SigmaComplex) -> bool:
    betti = reduced_betti(complex_)
    rhs = sum(((-1) ** dim) * value for dim, value in enumerate(betti))
    return reduced_euler_characteristic(complex_) == rhs
