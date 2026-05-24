"""Regression guard for the HG-MTH-016 Lagrange-inversion surface.

This test does not add mathematics beyond the theorem document. It guards the
recorded arity-three Fuss-Catalan coefficient extraction in
``docs/gate-minimality/p3b-generating-function-p3-closure.md``.
"""

from math import comb
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
P3B = ROOT / "docs" / "gate-minimality" / "p3b-generating-function-p3-closure.md"


def fc3(n: int) -> int:
    """Return the arity-three Fuss-Catalan number FC_n^(3)."""

    return comb(3 * n, n) // (2 * n + 1)


def test_fuss_catalan_coefficients_n_0_through_10() -> None:
    expected = [1, 1, 3, 12, 55, 273, 1428, 7752, 43263, 246675, 1430715]

    assert [fc3(n) for n in range(11)] == expected


def test_hg_mth_016_records_lagrange_inversion_formula() -> None:
    text = P3B.read_text(encoding="utf-8")

    assert "1/(2n+1)" in text
    assert "binom(3n,n)" in text
    assert "Lagrange inversion" in text
    assert "Y=x(1+Y)^3" in text


def test_hg_mth_016_promotion_remains_bounded() -> None:
    text = P3B.read_text(encoding="utf-8")

    assert "theorem-grade within declared P3.b constructor-shape generating-function scope" in text
    assert "does not locate or decorate the dominant singularity" in text
    assert "Does not promote `HG-MTH-011`." in text
    assert "Does not promote or restate `HG-MTH-018`." in text
    assert "Does not extend to `A_n`" in text
    assert "Does not cross into downstream Clay-program proof claims" in text
