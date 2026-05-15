"""CI validation harness for the source-supplied Proof Fabric Kernel import.

This test file is intentionally CI-first. It skips while `proof_fabric_kernel/`
has not yet been imported, and becomes a hard validation gate the moment the
source-supplied directory exists in the repository.

The tests validate schemas and supplied examples without promoting any
mathematical claim. Passing PFK validation means the operational substrate is
well-formed; it does not imply theorem progress.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest


ROOT = Path(__file__).resolve().parents[1]
PFK = ROOT / "proof_fabric_kernel"

pytestmark = pytest.mark.skipif(
    not PFK.exists(),
    reason="proof_fabric_kernel/ source tree not imported yet; see Heller-Godel issue #62",
)


EVENT_TRACES = [
    PFK / "examples/primes/primes_phase_example_trace.json",
    PFK / "examples/security/hsm_safe_trace.json",
    PFK / "examples/security/hsm_leak_trace.json",
    PFK / "examples/lawful_learning/lawful_learning_example_trace.json",
]


PROOF_ARTIFACTS = [
    PFK / "examples/primes/proof_artifact_primes_example.json",
    PFK / "examples/security/proof_artifact_hsm_safe.json",
    PFK / "examples/security/proof_artifact_hsm_leak.json",
    PFK / "examples/lawful_learning/proof_artifact_lawful_learning_example.json",
]


REQUIRED_IMPORT_PATHS = [
    PFK / "README.md",
    PFK / "schemas/event_ir.schema.json",
    PFK / "schemas/proof_artifact.schema.json",
    PFK / "schemas/calibration_bundle.schema.json",
    PFK / "schemas/claim_ledger_row.schema.json",
    PFK / "docs/PrimeStatsProtocol_v1.md",
    PFK / "docs/OperatorCatalog_PrimePolicyOperators_v1.md",
    PFK / "tools/hash_manifest.py",
    PFK / "tools/validate_event_ir.py",
    PFK / "tools/validate_proof_artifact.py",
]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def test_source_supplied_import_paths_exist() -> None:
    missing = [path.relative_to(ROOT).as_posix() for path in REQUIRED_IMPORT_PATHS if not path.exists()]
    assert not missing, f"Missing expected PFK import paths: {missing}"


def test_event_ir_examples_validate_against_imported_schema() -> None:
    schema = load_json(PFK / "schemas/event_ir.schema.json")
    validator = jsonschema.Draft202012Validator(schema)

    for trace in EVENT_TRACES:
        data = load_json(trace)
        events = data if isinstance(data, list) else [data]
        for event in events:
            validator.validate(event)


def test_proof_artifact_examples_validate_against_imported_schema() -> None:
    schema = load_json(PFK / "schemas/proof_artifact.schema.json")
    validator = jsonschema.Draft202012Validator(schema)

    for artifact in PROOF_ARTIFACTS:
        validator.validate(load_json(artifact))


def test_calibration_bundle_example_validates_against_imported_schema() -> None:
    schema = load_json(PFK / "schemas/calibration_bundle.schema.json")
    data = load_json(PFK / "examples/primes/calibration_bundle_example.json")
    jsonschema.validate(data, schema)


def test_claim_ledger_schema_is_valid_draft_2020_12_schema() -> None:
    schema = load_json(PFK / "schemas/claim_ledger_row.schema.json")
    jsonschema.Draft202012Validator.check_schema(schema)
