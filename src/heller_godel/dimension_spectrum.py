"""Dimension-spectrum coordinates for the abelian/non-abelian boundary.

This module computes finite-group irrep dimension spectra, Plancherel weights,
and boundary functionals for small standard symmetry groups. The bridge is that
``dim rho = chi(e)`` is the shared coordinate: dim 1 is the abelian/on-circle
locus, while dim > 1 is the non-abelian/off-circle departure.

The dimension spectrum re-coordinatizes the abelian/non-abelian boundary as
position relative to the unit circle. It diagnoses the boundary; it does not cross
it. Dim rho is analogous to -- never equal to -- the off-critical-line parameter
delta. No separation of P from NP, RH/GRH/Artin proof, or GCT orbit-closure
computation is claimed here.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import factorial

from heller_godel.wheel_plancherel import euler_phi


@dataclass(frozen=True)
class GroupSpectrum:
    """Finite-group dimension-spectrum fixture."""

    name: str
    order: int
    dimensions: tuple[int, ...]
    abelianization_order: int
    abelian: bool


@dataclass(frozen=True)
class SnIrrep:
    """Small symmetric-group irrep fixture indexed by partition label."""

    label: str
    dimension: int
    character_by_cycle_type: dict[tuple[int, ...], int]


STANDARD_SPECTRA: dict[str, GroupSpectrum] = {
    "S2": GroupSpectrum("S2", 2, (1, 1), 2, True),
    "S3": GroupSpectrum("S3", 6, (1, 1, 2), 2, False),
    "S4": GroupSpectrum("S4", 24, (1, 1, 2, 3, 3), 2, False),
    "S5": GroupSpectrum("S5", 120, (1, 1, 4, 4, 5, 5, 6), 2, False),
    "S6": GroupSpectrum("S6", 720, (1, 1, 5, 5, 5, 5, 9, 9, 10, 10, 16), 2, False),
    "Q8": GroupSpectrum("Q8", 8, (1, 1, 1, 1, 2), 4, False),
    "D4": GroupSpectrum("D4", 8, (1, 1, 1, 1, 2), 4, False),
    "A3": GroupSpectrum("A3", 3, (1, 1, 1), 3, True),
    "A4": GroupSpectrum("A4", 12, (1, 1, 1, 3), 3, False),
    "A5": GroupSpectrum("A5", 60, (1, 3, 3, 4, 5), 1, False),
}


SN_CLASS_SIZES: dict[int, dict[tuple[int, ...], int]] = {
    3: {(1, 1, 1): 1, (2, 1): 3, (3,): 2},
    4: {(1, 1, 1, 1): 1, (2, 1, 1): 6, (2, 2): 3, (3, 1): 8, (4,): 6},
    5: {
        (1, 1, 1, 1, 1): 1,
        (2, 1, 1, 1): 10,
        (2, 2, 1): 15,
        (3, 1, 1): 20,
        (3, 2): 20,
        (4, 1): 30,
        (5,): 24,
    },
}


SN_IRREPS: dict[int, tuple[SnIrrep, ...]] = {
    3: (
        SnIrrep("trivial", 1, {(1, 1, 1): 1, (2, 1): 1, (3,): 1}),
        SnIrrep("sign", 1, {(1, 1, 1): 1, (2, 1): -1, (3,): 1}),
        SnIrrep("standard", 2, {(1, 1, 1): 2, (2, 1): 0, (3,): -1}),
    ),
    4: (
        SnIrrep("trivial", 1, {(1, 1, 1, 1): 1, (2, 1, 1): 1, (2, 2): 1, (3, 1): 1, (4,): 1}),
        SnIrrep("sign", 1, {(1, 1, 1, 1): 1, (2, 1, 1): -1, (2, 2): 1, (3, 1): 1, (4,): -1}),
        SnIrrep("partition_22", 2, {(1, 1, 1, 1): 2, (2, 1, 1): 0, (2, 2): 2, (3, 1): -1, (4,): 0}),
        SnIrrep("standard", 3, {(1, 1, 1, 1): 3, (2, 1, 1): 1, (2, 2): -1, (3, 1): 0, (4,): -1}),
        SnIrrep("standard_twist", 3, {(1, 1, 1, 1): 3, (2, 1, 1): -1, (2, 2): -1, (3, 1): 0, (4,): 1}),
    ),
    5: (
        SnIrrep("trivial", 1, {(1, 1, 1, 1, 1): 1, (2, 1, 1, 1): 1, (2, 2, 1): 1, (3, 1, 1): 1, (3, 2): 1, (4, 1): 1, (5,): 1}),
        SnIrrep("sign", 1, {(1, 1, 1, 1, 1): 1, (2, 1, 1, 1): -1, (2, 2, 1): 1, (3, 1, 1): 1, (3, 2): -1, (4, 1): -1, (5,): 1}),
        SnIrrep("partition_41", 4, {(1, 1, 1, 1, 1): 4, (2, 1, 1, 1): 2, (2, 2, 1): 0, (3, 1, 1): 1, (3, 2): -1, (4, 1): 0, (5,): -1}),
        SnIrrep("partition_2111", 4, {(1, 1, 1, 1, 1): 4, (2, 1, 1, 1): -2, (2, 2, 1): 0, (3, 1, 1): 1, (3, 2): 1, (4, 1): 0, (5,): -1}),
        SnIrrep("partition_32", 5, {(1, 1, 1, 1, 1): 5, (2, 1, 1, 1): 1, (2, 2, 1): 1, (3, 1, 1): -1, (3, 2): 1, (4, 1): -1, (5,): 0}),
        SnIrrep("partition_221", 5, {(1, 1, 1, 1, 1): 5, (2, 1, 1, 1): -1, (2, 2, 1): 1, (3, 1, 1): -1, (3, 2): -1, (4, 1): 1, (5,): 0}),
        SnIrrep("partition_311", 6, {(1, 1, 1, 1, 1): 6, (2, 1, 1, 1): 0, (2, 2, 1): -2, (3, 1, 1): 0, (3, 2): 0, (4, 1): 0, (5,): 1}),
    ),
}


def cyclic_group(n: int) -> GroupSpectrum:
    if n < 1:
        raise ValueError("n must be positive")
    return GroupSpectrum(
        name=f"Z/{n}Z",
        order=n,
        dimensions=tuple(1 for _ in range(n)),
        abelianization_order=n,
        abelian=True,
    )


def wheel_group(n: int) -> GroupSpectrum:
    if n < 1:
        raise ValueError("n must be positive")
    phi = euler_phi(n)
    return GroupSpectrum(
        name=f"G_{n}",
        order=phi,
        dimensions=tuple(1 for _ in range(phi)),
        abelianization_order=phi,
        abelian=True,
    )


def symmetric_group(n: int) -> GroupSpectrum:
    if n == 1:
        return GroupSpectrum("S1", 1, (1,), 1, True)
    key = f"S{n}"
    if key not in STANDARD_SPECTRA:
        raise NotImplementedError("standard fixture includes S1 through S6")
    return STANDARD_SPECTRA[key]


def dim_spectrum(group: GroupSpectrum) -> tuple[int, ...]:
    return group.dimensions


def verify_burnside(group: GroupSpectrum) -> bool:
    return sum(dim * dim for dim in group.dimensions) == group.order


def plancherel_measure(group: GroupSpectrum) -> tuple[Fraction, ...]:
    weights = tuple(Fraction(dim * dim, group.order) for dim in group.dimensions)
    if sum(weights, Fraction(0, 1)) != Fraction(1, 1):
        raise ValueError(f"Plancherel weights do not sum to 1 for {group.name}")
    return weights


def is_plancherel_uniform(group: GroupSpectrum) -> bool:
    weights = plancherel_measure(group)
    return len(set(weights)) <= 1


def beta(group: GroupSpectrum) -> int:
    return max(group.dimensions)


def kappa(group: GroupSpectrum) -> Fraction:
    return sum(
        (Fraction(dim * dim, group.order) for dim in group.dimensions if dim > 1),
        Fraction(0, 1),
    )


def boundary_functional(group: GroupSpectrum) -> dict[str, object]:
    return {"beta": beta(group), "kappa": kappa(group), "abelian": group.abelian}


def abelianization_count(group: GroupSpectrum) -> int:
    one_dimensional = sum(1 for dim in group.dimensions if dim == 1)
    if one_dimensional != group.abelianization_order:
        raise ValueError(
            f"1-dimensional irrep count {one_dimensional} != abelianization order "
            f"{group.abelianization_order} for {group.name}"
        )
    return one_dimensional


def abelian_core_fraction(group: GroupSpectrum) -> Fraction:
    return Fraction(abelianization_count(group), group.order)


def assert_boundary_equivalence(group: GroupSpectrum) -> bool:
    on_circle = beta(group) == 1
    no_off_circle_mass = kappa(group) == 0
    return on_circle == no_off_circle_mass == group.abelian


def dimension_displacement(group: GroupSpectrum) -> tuple[int, ...]:
    """Return dim(rho)-1 as a discrete radial-displacement diagnostic."""

    return tuple(dim - 1 for dim in group.dimensions)


def analogy_not_equality_guard() -> str:
    return (
        "dim rho and delta are analogous boundary-position coordinates only; "
        "dim rho is a discrete integer and delta is a continuous real parameter, "
        "so dim rho = delta is forbidden."
    )


def known_family() -> tuple[GroupSpectrum, ...]:
    return (
        cyclic_group(1),
        cyclic_group(5),
        wheel_group(15),
        symmetric_group(2),
        symmetric_group(3),
        symmetric_group(4),
        symmetric_group(5),
        symmetric_group(6),
        STANDARD_SPECTRA["Q8"],
        STANDARD_SPECTRA["D4"],
        STANDARD_SPECTRA["A3"],
        STANDARD_SPECTRA["A4"],
        STANDARD_SPECTRA["A5"],
    )


def factorial_order_symmetric(n: int) -> int:
    return factorial(n)


def cycle_type(perm: tuple[int, ...]) -> tuple[int, ...]:
    """Return the integer partition cycle type of a zero-based permutation."""

    seen = [False] * len(perm)
    lengths: list[int] = []
    for start in range(len(perm)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = perm[current]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def sn_irreps(n: int) -> tuple[SnIrrep, ...]:
    if n not in SN_IRREPS:
        raise NotImplementedError("small S_n character table fixture is available for n=3,4,5")
    return SN_IRREPS[n]


def sn_class_sizes(n: int) -> dict[tuple[int, ...], int]:
    if n not in SN_CLASS_SIZES:
        raise NotImplementedError("small S_n class-size fixture is available for n=3,4,5")
    return SN_CLASS_SIZES[n]


def sn_character_value(irrep: SnIrrep, perm_or_cycle_type: tuple[int, ...]) -> int:
    ctype = perm_or_cycle_type if sum(perm_or_cycle_type) == len(perm_or_cycle_type) else cycle_type(perm_or_cycle_type)
    # The branch above cannot distinguish a permutation from a cycle-type with the same sum/length reliably.
    # Fall back to direct lookup first, then cycle-type lookup.
    return irrep.character_by_cycle_type.get(perm_or_cycle_type, irrep.character_by_cycle_type[cycle_type(perm_or_cycle_type)])


def decompose_sn_character(character_by_cycle_type: dict[tuple[int, ...], int], n: int) -> dict[str, int]:
    """Decompose a class function on S_n against the small hardcoded character table."""

    order = factorial(n)
    out: dict[str, int] = {}
    for irrep in sn_irreps(n):
        numerator = sum(
            sn_class_sizes(n)[ctype] * character_by_cycle_type.get(ctype, 0) * irrep.character_by_cycle_type[ctype]
            for ctype in sn_class_sizes(n)
        )
        multiplicity = Fraction(numerator, order)
        if multiplicity.denominator != 1:
            raise ValueError(f"non-integral multiplicity for {irrep.label}: {multiplicity}")
        out[irrep.label] = multiplicity.numerator
    return out


def regular_sn_decomposition(n: int, scalar: int = 1) -> dict[str, int]:
    """Return decomposition of scalar copies of the regular S_n representation."""

    return {irrep.label: scalar * irrep.dimension for irrep in sn_irreps(n)}


def on_off_multiplicities(decomposition: dict[str, int], n: int) -> dict[str, Fraction | int]:
    """Compute on/off-circle observables for an S_n irrep multiplicity dictionary."""

    irreps = {irrep.label: irrep for irrep in sn_irreps(n)}
    m_circle = sum(decomposition.get(label, 0) for label in ("trivial", "sign"))
    m_off = sum(mult for label, mult in decomposition.items() if irreps[label].dimension > 1)
    mu_off = sum(
        Fraction(mult * irreps[label].dimension * irreps[label].dimension, factorial(n))
        for label, mult in decomposition.items()
        if irreps[label].dimension > 1
    )
    denominator = m_circle + m_off
    ratio = Fraction(m_circle, denominator) if denominator else Fraction(0)
    return {"m_circle": m_circle, "m_off": m_off, "mu_off": mu_off, "R": ratio}
