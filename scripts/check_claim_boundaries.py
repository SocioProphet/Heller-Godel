#!/usr/bin/env python3
"""Minimal CI guard for the Paper I claim boundary."""

from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "docs" / "manuscripts" / "paper_i_deligne_cohomological_phase_characters.md"

REQUIRED = [
    "does **not** claim progress on the Hodge conjecture itself",
    "does **not** assert algebraicity",
    "does **not** construct algebraic cycles",
    "The finite character is multiplicative",
    "it is not the carry cocycle",
    "No Deligne class on `B` is produced",
    "No Chern class on `B` is produced",
    "No algebraic cycle is produced",
]


def main() -> int:
    if not MANUSCRIPT.exists():
        print(f"missing manuscript: {MANUSCRIPT}", file=sys.stderr)
        return 1
    text = MANUSCRIPT.read_text(encoding="utf-8")
    missing = [phrase for phrase in REQUIRED if phrase not in text]
    if missing:
        for phrase in missing:
            print(f"missing required claim-boundary phrase: {phrase}", file=sys.stderr)
        return 1
    print("claim-boundary guard passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
