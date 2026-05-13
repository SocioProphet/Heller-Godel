from __future__ import annotations

import pytest

from heller_godel.schema_contracts import SchemaContractError, validate_artifact


def valid_log_prime_volume_artifact() -> dict:
    return {
        "schema_version": "heller-godel.log-prime-volume-artifact.v0.1",
        "artifact_kind": "log_prime_volume_candidate_ranking_artifact",
        "authorship": {
            "framework_author": "Michael Heller",
            "assistant_role": "schema_implementation_support",
        },
        "claim_boundary": {
            "rh_proof_claimed": False,
            "primality_certification_replaced": False,
            "unconditional_error_bound_improvement_claimed": False,
        },
        "coordinate_gauge": {
            "coordinate": "u = ln(x)",
            "ordinary_volume_element": "dx = exp(u) du",
            "density_per_ordinary_x_volume": "1/u",
            "log_coordinate_intensity": "exp(u)/u",
            "base_change_status": "linear_rescaling_of_frequency_axis",
        },
        "mean_field": {
            "operator": "PMF(u,L) = integral_u_to_u_plus_L exp(v)/v dv",
            "approximation_status": "definition",
        },
        "residual_model": {
            "residual_operator": "R(u,L) = prime_count(exp(u), exp(u+L)) - PMF(u,L)",
            "phase_channel": ["cos(gamma u)", "sin(gamma u)"],
            "rh_envelope": "exp(u/2)",
            "rh_envelope_status": "diagnostic",
        },
        "ranking_protocol": {
            "certification_separate_from_ranking": True,
            "normalized_rank_metric": "rho = first_certified_prime_rank / candidate_count",
            "required_baselines": [
                "random_admissible_ordering",
                "wheel_only_ordering",
                "ascending_ordering",
            ],
        },
        "replay": {
            "code_ref": "schema/log-prime-volume-contracts",
            "input_hash": "sha256:input-placeholder",
            "output_hash": "sha256:output-placeholder",
        },
    }


def valid_proof_dynamics_bridge_artifact() -> dict:
    return {
        "schema_version": "heller-godel.proof-dynamics-bridge-artifact.v0.1",
        "artifact_kind": "proof_dynamics_bridge_artifact",
        "claim_status": "conditional_construction",
        "non_claims": {
            "p_vs_np_proof_claimed": False,
            "empirical_validation_claimed": False,
            "natural_canonicity_claimed": False,
            "lawful_learning_validated": False,
        },
        "p_primary_case": {
            "prime": 2,
            "torsion_group": "mu_2",
            "expected_signature": "-1",
        },
        "dynamics_boundary": {
            "descent_transport_split_declared": True,
            "floquet_unit_modulus_requires": "unitary_or_isometric_hypothesis",
        },
        "topology_boundary": {
            "so3_action_noncommuting": True,
            "pi1_so3_torsion_signature": "Z/2",
        },
        "encoding_hypotheses": {
            "proof_normal_forms_to_active_constraints": True,
            "weight_preservation": True,
            "rewrite_adjacency_preservation": True,
            "cyclic_action_preservation": True,
            "singularity_exponent_localization": True,
            "boundary_transversality": True,
        },
        "replay": {
            "code_ref": "schema/log-prime-volume-contracts",
            "input_hash": "sha256:input-placeholder",
            "output_hash": "sha256:output-placeholder",
        },
    }


def test_valid_log_prime_volume_artifact_passes() -> None:
    validate_artifact(valid_log_prime_volume_artifact())


def test_log_prime_volume_rejects_lost_volume_element() -> None:
    artifact = valid_log_prime_volume_artifact()
    artifact["coordinate_gauge"]["log_coordinate_intensity"] = "1/u"

    with pytest.raises(SchemaContractError, match="log_coordinate_intensity"):
        validate_artifact(artifact)


def test_log_prime_volume_rejects_rh_proof_claim() -> None:
    artifact = valid_log_prime_volume_artifact()
    artifact["claim_boundary"]["rh_proof_claimed"] = True

    with pytest.raises(SchemaContractError, match="rh_proof_claimed"):
        validate_artifact(artifact)


def test_log_prime_volume_rejects_ranking_as_certification() -> None:
    artifact = valid_log_prime_volume_artifact()
    artifact["ranking_protocol"]["certification_separate_from_ranking"] = False

    with pytest.raises(SchemaContractError, match="certification"):
        validate_artifact(artifact)


def test_valid_proof_dynamics_bridge_artifact_passes() -> None:
    validate_artifact(valid_proof_dynamics_bridge_artifact())


def test_proof_dynamics_rejects_p_vs_np_proof_claim() -> None:
    artifact = valid_proof_dynamics_bridge_artifact()
    artifact["non_claims"]["p_vs_np_proof_claimed"] = True

    with pytest.raises(SchemaContractError, match="p_vs_np_proof_claimed"):
        validate_artifact(artifact)


def test_proof_dynamics_rejects_odd_prime_first_target() -> None:
    artifact = valid_proof_dynamics_bridge_artifact()
    artifact["p_primary_case"]["prime"] = 3

    with pytest.raises(SchemaContractError, match="p = 2"):
        validate_artifact(artifact)


def test_proof_dynamics_rejects_missing_encoding_hypothesis() -> None:
    artifact = valid_proof_dynamics_bridge_artifact()
    artifact["encoding_hypotheses"]["boundary_transversality"] = False

    with pytest.raises(SchemaContractError, match="boundary_transversality"):
        validate_artifact(artifact)
