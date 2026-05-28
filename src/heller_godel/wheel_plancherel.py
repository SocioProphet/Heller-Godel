"""Wheel and finite-character utilities for HG-MTH-008.4.

The module is intentionally finite and elementary. It demonstrates the
structured Unit-Substantiation Problem (USP): returning factor coordinates for
the trivial character, not merely returning the constant-one function.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd, isqrt, lcm, prod
import cmath


@dataclass(frozen=True)
class PrimePower:
    p: int
    e: int

    @property
    def modulus(self) -> int:
        return self.p ** self.e


@dataclass(frozen=True)
class CyclicFactor:
    """A cyclic component of a unit group for a prime-power CRT factor."""

    modulus: int
    order: int
    generator: int
    label: str


@dataclass(frozen=True)
class USPCertificate:
    n: int
    factorization: tuple[PrimePower, ...]
    cyclic_decomposition: tuple[CyclicFactor, ...]
    chi0_coordinates: tuple[int, ...]
    structured: bool = True


def factor_int(n: int) -> tuple[PrimePower, ...]:
    """Return the prime-power factorization of n by trial division.

    This is not claimed as a polynomial-time factoring algorithm; it is a small
    executable witness for the finite regression tests.
    """

    if n < 1:
        raise ValueError("n must be >= 1")
    remaining = n
    factors: list[PrimePower] = []
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            e = 0
            while remaining % p == 0:
                remaining //= p
                e += 1
            factors.append(PrimePower(p, e))
        p += 1 if p == 2 else 2
    if remaining > 1:
        factors.append(PrimePower(remaining, 1))
    return tuple(factors)


def multiply_factorization(factors: tuple[PrimePower, ...]) -> int:
    return prod(pp.p ** pp.e for pp in factors)


def units_mod(n: int) -> tuple[int, ...]:
    if n < 1:
        raise ValueError("n must be >= 1")
    return tuple(a for a in range(1, n + 1) if gcd(a, n) == 1)


def euler_phi_from_factorization(factors: tuple[PrimePower, ...]) -> int:
    if not factors:
        return 1
    return prod((pp.p - 1) * (pp.p ** (pp.e - 1)) for pp in factors)


def euler_phi(n: int) -> int:
    return euler_phi_from_factorization(factor_int(n))


def order_mod(a: int, n: int) -> int:
    if n == 1:
        return 1
    if gcd(a, n) != 1:
        raise ValueError("a must be a unit modulo n")
    order = euler_phi(n)
    for q in _prime_divisors(order):
        while order % q == 0 and pow(a, order // q, n) == 1:
            order //= q
    return order


def order_mod_by_multiplication(a: int, n: int) -> int:
    """Compute the order of a unit by repeated multiplication only.

    This intentionally avoids factoring n or phi(n). It is used only as a
    finite regression witness for small bounds, not as an efficient primitive.
    """

    if n == 1:
        return 1
    if gcd(a, n) != 1:
        raise ValueError("a must be a unit modulo n")
    x = 1
    for k in range(1, len(units_mod(n)) + 1):
        x = (x * a) % n
        if x == 1:
            return k
    raise ArithmeticError(f"unit order did not close in G_{n}")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for d in range(3, isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def _prime_divisors(n: int) -> tuple[int, ...]:
    return tuple(pp.p for pp in factor_int(n))


def _find_generator_for_cyclic_units(n: int) -> int:
    """Find a generator of (Z/nZ)^x when the group is known cyclic."""

    phi = euler_phi(n)
    if phi == 1:
        return 1
    prime_divs = _prime_divisors(phi)
    for candidate in units_mod(n):
        if all(pow(candidate, phi // q, n) != 1 for q in prime_divs):
            return candidate
    raise ArithmeticError(f"no cyclic generator found for G_{n}")


def cyclic_decomposition_prime_power(p: int, e: int) -> tuple[CyclicFactor, ...]:
    """Return invariant cyclic factors for (Z/p^e Z)^x.

    Odd prime powers are cyclic. The 2-power cases are:
    G_2 trivial, G_4 ~= C2, and G_{2^e} ~= C2 x C_{2^{e-2}} for e >= 3.
    """

    if not is_prime(p) or e < 1:
        raise ValueError("expected a prime p and exponent e >= 1")
    modulus = p**e
    if p == 2:
        if e == 1:
            return ()
        if e == 2:
            return (CyclicFactor(modulus=4, order=2, generator=3, label="C2"),)
        return (
            CyclicFactor(modulus=modulus, order=2, generator=modulus - 1, label="C2[-1]"),
            CyclicFactor(
                modulus=modulus,
                order=2 ** (e - 2),
                generator=5,
                label=f"C{2 ** (e - 2)}[5]",
            ),
        )
    order = (p - 1) * p ** (e - 1)
    return (
        CyclicFactor(
            modulus=modulus,
            order=order,
            generator=_find_generator_for_cyclic_units(modulus),
            label=f"C{order}",
        ),
    )


def crt_cyclic_decomposition(factors: tuple[PrimePower, ...]) -> tuple[CyclicFactor, ...]:
    parts: list[CyclicFactor] = []
    for pp in factors:
        parts.extend(cyclic_decomposition_prime_power(pp.p, pp.e))
    return tuple(parts)


def usp(n: int, factoring_oracle=None) -> USPCertificate:
    """Return the structured Unit-Substantiation Problem certificate for n."""

    if n < 1:
        raise ValueError("n must be >= 1")
    raw = factoring_oracle(n) if factoring_oracle is not None else factor_int(n)
    factors = tuple(
        pp if isinstance(pp, PrimePower) else PrimePower(int(pp[0]), int(pp[1]))
        for pp in raw
    )
    if multiply_factorization(factors) != n:
        raise ValueError("factoring_oracle did not return a factorization of n")
    decomposition = crt_cyclic_decomposition(factors)
    return USPCertificate(
        n=n,
        factorization=factors,
        cyclic_decomposition=decomposition,
        chi0_coordinates=tuple(0 for _ in decomposition),
    )


def factorization_from_usp(cert: USPCertificate) -> tuple[PrimePower, ...]:
    if not cert.structured:
        raise ValueError("unstructured certificate cannot recover factorization")
    if multiply_factorization(cert.factorization) != cert.n:
        raise ValueError("invalid USP certificate")
    return cert.factorization


def constant_trivial_character(n: int):
    """Return the bare constant-one character; deliberately not a USP solution."""

    if n < 1:
        raise ValueError("n must be >= 1")
    return {"n": n, "values": {u: 1 for u in units_mod(n)}, "structured": False}


def validate_usp_solution(obj, n: int) -> bool:
    return (
        isinstance(obj, USPCertificate)
        and obj.n == n
        and obj.structured
        and multiply_factorization(obj.factorization) == n
        and len(obj.chi0_coordinates) == len(obj.cyclic_decomposition)
    )


def is_cyclic_wheel_modulus(n: int) -> bool:
    """Closed-form Gauss primitive-root criterion for (Z/nZ)^x cyclic."""

    if n < 1:
        return False
    if n in (1, 2, 4):
        return True
    factors = factor_int(n)
    if len(factors) == 1:
        pp = factors[0]
        return pp.p != 2
    if len(factors) == 2:
        ps = {pp.p for pp in factors}
        if 2 in ps:
            odd = next(pp for pp in factors if pp.p != 2)
            two = next(pp for pp in factors if pp.p == 2)
            return two.e == 1 and odd.p % 2 == 1
    return False


def is_cyclic_by_enumeration(n: int) -> bool:
    """Independent finite check: some enumerated unit has order |G_n|.

    The group order is computed by counting units, and element orders are
    computed by repeated multiplication. This avoids using the prime-power
    factorization of n or the CRT decomposition being tested.
    """

    units = units_mod(n)
    group_order = len(units)
    if group_order == 1:
        return True
    return any(order_mod_by_multiplication(unit, n) == group_order for unit in units)


def cyclic_character_table(n: int) -> dict[int, dict[int, complex]]:
    """Character table for cyclic-wheel moduli, keyed by character exponent."""

    if not is_cyclic_wheel_modulus(n):
        raise ValueError("cyclic_character_table requires a cyclic-wheel modulus")
    units = units_mod(n)
    phi = len(units)
    gen = _find_generator_for_cyclic_units(n)
    logs: dict[int, int] = {}
    x = 1
    for k in range(phi):
        logs[x] = k
        x = (x * gen) % n
    return {
        a: {u: cmath.exp(2j * cmath.pi * a * logs[u] / phi) for u in units}
        for a in range(phi)
    }


def character_orthogonality_holds(n: int, tolerance: float = 1e-9) -> bool:
    table = cyclic_character_table(n)
    units = units_mod(n)
    for a, chi_a in table.items():
        for b, chi_b in table.items():
            inner = sum(chi_a[u] * chi_b[u].conjugate() for u in units) / len(units)
            target = 1 if a == b else 0
            if abs(inner - target) > tolerance:
                return False
    return True


def fourier_transform_on_cyclic_units(n: int, values: dict[int, complex]) -> dict[int, complex]:
    table = cyclic_character_table(n)
    return {
        a: sum(values[u] * chi[u].conjugate() for u in units_mod(n))
        for a, chi in table.items()
    }


def plancherel_holds(n: int, values: dict[int, complex], tolerance: float = 1e-9) -> bool:
    units = units_mod(n)
    lhs = sum(abs(values[u]) ** 2 for u in units)
    fhat = fourier_transform_on_cyclic_units(n, values)
    rhs = sum(abs(v) ** 2 for v in fhat.values()) / len(units)
    return abs(lhs - rhs) <= tolerance


def primorial(k: int) -> int:
    if k < 0:
        raise ValueError("k must be nonnegative")
    primes: list[int] = []
    candidate = 2
    while len(primes) < k:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return prod(primes) if primes else 1


def group_exponent_from_factorization(factors: tuple[PrimePower, ...]) -> int:
    decomposition = crt_cyclic_decomposition(factors)
    if not decomposition:
        return 1
    return reduce(lcm, (part.order for part in decomposition), 1)
