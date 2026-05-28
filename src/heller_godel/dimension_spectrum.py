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


STANDARD_SPECTRA: dict[str, GroupSpectrum] = {
    "S2": GroupSpectrum("S2", 2, (1, 1), 2, True),
    "S3": GroupSpectrum("S3", 6, (1, 1, 2), 2, False),
    "S4": GroupSpectrum("S4", 24, (1, 1, 2, 3, 3), 2, False),
    "S5": GroupSpectrum("S5", 120, (1, 1, 4, 4, 5, 5, 6), 2, False),
    "Q8": GroupSpectrum("Q8", 8, (1, 1, 1, 1, 2), 4, False),
    "D4": GroupSpectrum("D4", 8, (1, 1, 1, 1, 2), 4, False),
    "A3": GroupSpectrum("A3", 3, (1, 1, 1), 3, True),
    "A4": GroupSpectrum("A4", 12, (1, 1, 1, 3), 3, False),
    "A5": GroupSpectrum("A5", 60, (1, 3, 3, 4, 5), 1, False),
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
        raise NotImplementedError("standard fixture includes S1 through S5")
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
        STANDARD_SPECTRA["Q8"],
        STANDARD_SPECTRA["D4"],
        STANDARD_SPECTRA["A3"],
        STANDARD_SPECTRA["A4"],
        STANDARD_SPECTRA["A5"],
    )


def factorial_order_symmetric(n: int) -> int:
    return factorial(n)
