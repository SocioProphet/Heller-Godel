"""Executable schema-boundary checks for Heller-Godel research artifacts.

These validators intentionally avoid adding a JSON Schema dependency. The repository
still stores schema contract documents, while this module enforces the boundary
invariants that are load-bearing for CI:

* the log-prime-volume contract must preserve the density/intensity distinction;
* RH-shaped envelopes must remain diagnostic or conditional, never proof claims;
* ranking artifacts must not replace primality certification;
* proof-dynamics bridge artifacts must remain conditional until canonicity is proved.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class SchemaContractError(ValueError):
    """Raised when a research artifact violates a schema-level contract."""


LPV_SCHEMA_VERSION = "heller-godel.log-prime-volume-artifact.v0.1"
PROOF_DYNAMICS_SCHEMA_VERSION = "heller-godel.proof-dynamics-bridge-artifact.v0.1"

LPV_ARTIFACT_KIND = "log_prime_volume_candidate_ranking_artifact"
PROOF_DYNAMICS_ARTIFACT_KIND = "proof_dynamics_bridge_artifact"

FORBIDDEN_LPV_TRUE_FLAGS = {
    "rh_proof_claimed",
    "primality_certification_replaced",
    "unconditional_error_bound_improvement_claimed",
}

FORBIDDEN_PROOF_DYNAMICS_TRUE_FLAGS = {
    "p_vs_np_proof_claimed",
    "empirical_validation_claimed",
    "natural_canonicity_claimed",
    "lawful_learning_validated",
}


PathLike = str | Path
Artifact = dict[str, Any]


def load_json(path: PathLike) -> Artifact:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SchemaContractError(f"artifact must be a JSON object: {path}")
    return data


def _require(mapping: Artifact, key: str) -> Any:
    if key not in mapping:
        raise SchemaContractError(f"missing required key: {key}")
    return mapping[key]


def _require_mapping(mapping: Artifact, key: str) -> Artifact:
    value = _require(mapping, key)
    if not isinstance(value, dict):
        raise SchemaContractError(f"{key} must be an object")
    return value


def _require_false_flags(mapping: Artifact, flags: set[str], namespace: str) -> None:
    for flag in flags:
        if mapping.get(flag) is not False:
            raise SchemaContractError(f"{namespace}.{flag} must be false")


def validate_log_prime_volume_artifact(artifact: Artifact) -> None:
    """Validate the log-prime-volume artifact boundary contract."""

    if artifact.get("schema_version") != LPV_SCHEMA_VERSION:
        raise SchemaContractError("unexpected log-prime-volume schema_version")
    if artifact.get("artifact_kind") != LPV_ARTIFACT_KIND:
        raise SchemaContractError("unexpected log-prime-volume artifact_kind")

    authorship = _require_mapping(artifact, "authorship")
    if authorship.get("framework_author") != "Michael Heller":
        raise SchemaContractError("framework_author must preserve Heller authorship")

    claim_boundary = _require_mapping(artifact, "claim_boundary")
    _require_false_flags(claim_boundary, FORBIDDEN_LPV_TRUE_FLAGS, "claim_boundary")

    coordinate_gauge = _require_mapping(artifact, "coordinate_gauge")
    expected_gauge = {
        "coordinate": "u = ln(x)",
        "ordinary_volume_element": "dx = exp(u) du",
        "density_per_ordinary_x_volume": "1/u",
        "log_coordinate_intensity": "exp(u)/u",
    }
    for key, expected in expected_gauge.items():
        if coordinate_gauge.get(key) != expected:
            raise SchemaContractError(f"coordinate_gauge.{key} must be {expected!r}")

    mean_field = _require_mapping(artifact, "mean_field")
    if mean_field.get("operator") != "PMF(u,L) = integral_u_to_u_plus_L exp(v)/v dv":
        raise SchemaContractError("mean_field.operator must encode the corrected PMF integral")

    residual_model = _require_mapping(artifact, "residual_model")
    if residual_model.get("rh_envelope_status") not in {"conditional", "diagnostic"}:
        raise SchemaContractError("RH envelope must be conditional or diagnostic")
    if residual_model.get("rh_envelope") != "exp(u/2)":
        raise SchemaContractError("residual_model.rh_envelope must be exp(u/2)")

    ranking_protocol = _require_mapping(artifact, "ranking_protocol")
    baselines = ranking_protocol.get("required_baselines")
    if not isinstance(baselines, list) or "random_admissible_ordering" not in baselines:
        raise SchemaContractError("ranking_protocol must include random_admissible_ordering baseline")
    if "wheel_only_ordering" not in baselines:
        raise SchemaContractError("ranking_protocol must include wheel_only_ordering baseline")
    if ranking_protocol.get("certification_separate_from_ranking") is not True:
        raise SchemaContractError("certification must remain separate from ranking")

    replay = _require_mapping(artifact, "replay")
    for key in ("code_ref", "input_hash", "output_hash"):
        _require(replay, key)


def validate_proof_dynamics_bridge_artifact(artifact: Artifact) -> None:
    """Validate the conditional proof-dynamics bridge artifact boundary contract."""

    if artifact.get("schema_version") != PROOF_DYNAMICS_SCHEMA_VERSION:
        raise SchemaContractError("unexpected proof-dynamics schema_version")
    if artifact.get("artifact_kind") != PROOF_DYNAMICS_ARTIFACT_KIND:
        raise SchemaContractError("unexpected proof-dynamics artifact_kind")
    if artifact.get("claim_status") != "conditional_construction":
        raise SchemaContractError("proof-dynamics bridge must remain a conditional construction")

    non_claims = _require_mapping(artifact, "non_claims")
    _require_false_flags(non_claims, FORBIDDEN_PROOF_DYNAMICS_TRUE_FLAGS, "non_claims")

    p_primary = _require_mapping(artifact, "p_primary_case")
    if p_primary.get("prime") != 2:
        raise SchemaContractError("first bridge artifact must be restricted to p = 2")
    if p_primary.get("torsion_group") != "mu_2":
        raise SchemaContractError("p = 2 bridge must target mu_2")
    if p_primary.get("expected_signature") != "-1":
        raise SchemaContractError("p = 2 expected signature must be -1")

    dynamics = _require_mapping(artifact, "dynamics_boundary")
    if dynamics.get("descent_transport_split_declared") is not True:
        raise SchemaContractError("descent/transport split must be declared")
    if dynamics.get("floquet_unit_modulus_requires") != "unitary_or_isometric_hypothesis":
        raise SchemaContractError("Floquet phase claims require unitary/isometric hypotheses")

    topology = _require_mapping(artifact, "topology_boundary")
    if topology.get("so3_action_noncommuting") is not True:
        raise SchemaContractError("SO(3) action boundary must preserve noncommuting action")
    if topology.get("pi1_so3_torsion_signature") != "Z/2":
        raise SchemaContractError("SO(3) torsion signature must be Z/2")

    encoding = _require_mapping(artifact, "encoding_hypotheses")
    required_hypotheses = {
        "proof_normal_forms_to_active_constraints",
        "weight_preservation",
        "rewrite_adjacency_preservation",
        "cyclic_action_preservation",
        "singularity_exponent_localization",
        "boundary_transversality",
    }
    missing = sorted(name for name in required_hypotheses if encoding.get(name) is not True)
    if missing:
        raise SchemaContractError(f"missing encoding hypotheses: {', '.join(missing)}")

    replay = _require_mapping(artifact, "replay")
    for key in ("code_ref", "input_hash", "output_hash"):
        _require(replay, key)


def validate_artifact(artifact: Artifact) -> None:
    """Dispatch to the correct artifact validator."""

    kind = artifact.get("artifact_kind")
    if kind == LPV_ARTIFACT_KIND:
        validate_log_prime_volume_artifact(artifact)
        return
    if kind == PROOF_DYNAMICS_ARTIFACT_KIND:
        validate_proof_dynamics_bridge_artifact(artifact)
        return
    raise SchemaContractError(f"unknown artifact_kind: {kind!r}")
