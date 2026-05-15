#!/usr/bin/env python3
"""Minimal CI guard for the Paper I claim boundary and done-state matrix."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "docs" / "manuscripts" / "paper_i_deligne_cohomological_phase_characters.md"

REQUIRED_CLAIM_BOUNDARY_PHRASES = [
    "does **not** claim progress on the Hodge conjecture itself",
    "does **not** assert algebraicity",
    "does **not** construct algebraic cycles",
    "The finite character is multiplicative",
    "it is not the carry cocycle",
    "No Deligne class on `B` is produced",
    "No Chern class on `B` is produced",
    "No algebraic cycle is produced",
    "does **not** close the general encoding hypothesis for arbitrary arithmetic sentences",
    "Theorem 6.2 remains conditional as a general comparison theorem",
    "Theorem A.8 further shows that the `mu_2` output of that Catalan A1 instance is independent",
]

REQUIRED_DONE_MATRIX_ROWS = [
    "| I.1 | Encoding hypothesis: sentence to gate constraints | Closed for Catalan A1 fixture; open in general | 6.4, 7.1, Appendix A |",
    "| I.2 | Multiplicativity correction term uncharacterized | Closed: character multiplies exactly; carry is lifted-index section defect | 4.5, 4.6 |",
    "| I.3 | Choice of statistic underdetermined | Closed via reduced statistic | 2.2 |",
    "| A.8 | Catalan A1 realization independence | Closed for Catalan A1 fixture; mu_2 output only | Appendix A |",
    "| II.1 | Transcendental species | Open; bracketed | 7.2 |",
    "| II.4 | Proof-class moduli absent | Open | 7.3 |",
    "| III.4 | Floquet phase matching | Closed for Catalan A1 fixture; open in general | 6.4, Appendix A |",
    "| III.5 | Odd-prime case | Open as Conjecture 6.3 | 6.6 |",
    "| V.1 | Beilinson regulator framework | Partially addressed: framework in place; Chern lifts case-by-case | 7.5, 4.5 |",
    "| Hodge | Progress on Hodge conjecture | Not claimed | 7.6 |",
    "| Hodge | Algebraicity of Deligne classes | Not claimed | 7.6 |",
    "| Hodge | Deligne / Chern class on real `B` | Not claimed | 7.6 |",
    "| Hodge | Algebraic cycle existence | Not claimed | 7.6 |",
    "| Hodge | Hodge relevance of Conjecture 6.3 | Not claimed | 7.6 |",
]


def require_phrases(text: str, phrases: list[str], label: str) -> list[str]:
    return [f"missing {label}: {phrase}" for phrase in phrases if phrase not in text]


def main() -> int:
    if not MANUSCRIPT.exists():
        print(f"missing manuscript: {MANUSCRIPT}", file=sys.stderr)
        return 1

    text = MANUSCRIPT.read_text(encoding="utf-8")
    failures: list[str] = []
    failures.extend(require_phrases(text, REQUIRED_CLAIM_BOUNDARY_PHRASES, "claim-boundary phrase"))
    failures.extend(require_phrases(text, REQUIRED_DONE_MATRIX_ROWS, "definition-of-done matrix row"))

    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1

    print("claim-boundary and definition-of-done guards passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
