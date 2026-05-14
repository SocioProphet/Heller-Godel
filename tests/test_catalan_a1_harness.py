"""Regression tests for the Catalan A1 reference harness."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


EXPECTED_HASH_CHAIN_HEAD = "861248792d5cc44569ee9d6d51fb443db4b200f3e532c7ad85cc9903588ae2c3"


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
    assert payload["summary"]["gamma_lyap_loop"] == "PASS"
    assert payload["summary"]["encoding_homomorphism"] == "PASS"
    assert payload["summary"]["mu2_diagram_commutes"] == "PASS"


def test_catalan_a1_reference_report_pins_same_head() -> None:
    """The committed reference report must pin the same chain head as the harness."""

    report_path = Path("harness/reference_reports/catalan_a1_report.json")
    payload = json.loads(report_path.read_text(encoding="utf-8"))

    assert payload["all_passed"] is True
    assert payload["convention_id"] == "A1-sauzin-normalization-v1"
    assert payload["hash_chain"]["head"] == EXPECTED_HASH_CHAIN_HEAD
    assert payload["proof_reference"] == "docs/proofs/a1-gate-minimality.md v2"
    assert payload["checks"]["spin_lift_provenance"]["zeta_matrix"] == [
        [-1.0, -0.0],
        [-0.0, -1.0],
    ]
    assert payload["checks"]["gamma_lyap_loop"]["is_loop"] is True
    assert payload["checks"]["gamma_lyap_loop"]["mu2_phase"] == -1
    assert payload["checks"]["encoding_homomorphism"]["map"] == {"lyap_generator": "r"}
    assert payload["checks"]["mu2_diagram_commutes"]["diagram_commutes"] is True
