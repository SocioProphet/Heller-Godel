"""Regression tests for the Catalan A1 reference harness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


EXPECTED_HASH_CHAIN_HEAD = "0e8469cc953d2e340b2eda0e929e1e143bde041e82479948c4784801e13b7075"


def test_catalan_a1_harness_hash_chain_head() -> None:
    """The harness must reproduce the pinned reference hash-chain head."""

    script = Path("harness/catalan_a1_harness.py")
    result = subprocess.run(
        [sys.executable, str(script), "--summary-only", "--assert-reference-head"],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)

    assert payload["all_passed"] is True
    assert payload["hash_chain_head"] == EXPECTED_HASH_CHAIN_HEAD
    assert all(status == "PASS" for status in payload["summary"].values())


def test_catalan_a1_reference_report_pins_same_head() -> None:
    """The committed reference report must pin the same chain head as the harness."""

    report_path = Path("harness/reference_reports/catalan_a1_report.json")
    payload = json.loads(report_path.read_text(encoding="utf-8"))

    assert payload["all_passed"] is True
    assert payload["hash_chain"]["head"] == EXPECTED_HASH_CHAIN_HEAD
    assert payload["proof_reference"] == "docs/proofs/a1-gate-minimality.md v2"
    assert payload["checks"]["spin_lift_provenance"]["zeta_matrix"] == [
        [-1.0, -0.0],
        [-0.0, -1.0],
    ]
