#!/usr/bin/env python3
"""Write the HG-EXP-008.9 S4 Cayley spectrum atlas.

This is the tranche-3 atlas around the locked S4 matrix fixtures. It does not
claim a full S3/S5 or A_n/D_n atlas; those require their own matrix-realization
fixtures and trace-vs-character gates.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from heller_godel.cayley_atlas import write_csv


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("data/exp_008_9_results.csv"))
    args = parser.parse_args()
    write_csv(args.out)
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
