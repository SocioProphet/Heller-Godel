#!/usr/bin/env python3
"""Emit the deterministic Catalan/Tamari mu_2 bridge ledger."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from heller_godel.mu2_bridge import mu2_bridge_ledger, verify_mu2_bridge_ledger


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=5, help="largest Catalan fiber to enumerate")
    parser.add_argument("--check", action="store_true", help="verify ledger invariants before printing")
    parser.add_argument("--output", type=Path, default=None, help="optional output path")
    args = parser.parse_args()

    ledger = mu2_bridge_ledger(max_n=args.max_n)
    if args.check:
        verify_mu2_bridge_ledger(ledger)

    payload = json.dumps(ledger, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(payload, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
