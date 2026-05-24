"""Regression guard for the HG-MTH-018 irreducibility proof surface.

This test does not add mathematics beyond the theorem document. It guards the
recorded degree-obstruction argument in Section 6.2 of
``docs/gate-minimality/p3c-puiseux-singularity-character-p3-closure.md``.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
P3C = ROOT / "docs" / "gate-minimality" / "p3c-puiseux-singularity-character-p3-closure.md"


def degree_of_r_squared_one_minus_r(degree_r: int) -> int | None:
    """Return deg(r^2(1-r)) for polynomial r of degree degree_r.

    For constant r, the expression is constant, so no positive degree is
    returned. For nonconstant r, the leading term is -r^3, so the degree is
    exactly 3 * degree_r.
    """

    if degree_r == 0:
        return None
    return 3 * degree_r


def test_hg_mth_018_records_qx_no_root_argument() -> None:
    text = P3C.read_text(encoding="utf-8")

    for token in [
        "has no root in `Q(x)`",
        "x = r^2(1-r)",
        "If `r` is constant",
        "deg(r^2(1-r))=3n",
        "cannot equal `1`",
        "This contradiction proves that `f(z)` has no root in `Q(x)`.",
    ]:
        assert token in text


def test_polynomial_root_degree_obstruction_matches_recorded_proof() -> None:
    # Constant polynomial case: r^2(1-r) is constant, but x has degree 1.
    assert degree_of_r_squared_one_minus_r(0) is None

    # Nonconstant case: deg(r^2(1-r)) = 3n, never 1.
    for degree_r in range(1, 20):
        degree_rhs = degree_of_r_squared_one_minus_r(degree_r)
        assert degree_rhs == 3 * degree_r
        assert degree_rhs != 1


def test_cubic_irreducibility_statement_remains_bounded() -> None:
    text = P3C.read_text(encoding="utf-8")

    assert "is irreducible in `y` over `Q(x)`." in text
    assert "theorem-grade within declared `p=3` Puiseux datum and `chi_3` source-identification scope" in text
    assert "Does not promote `HG-MTH-011`." in text
    assert "Does not extend to `A_n`" in text
    assert "Does not cross into downstream Clay-program proof claims" in text
