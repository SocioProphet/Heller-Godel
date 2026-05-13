import pytest

from heller_godel.proof_dynamics import (
    ProofDynamicsValidationError,
    analytic_signature_from_parity,
    branch_parity,
    catalan_closed_form,
    catalan_generating_equation,
    catalan_number,
    gate_signature,
    internal_node_count,
    is_rotation_edge,
    list_rotation_neighbors,
    normalize_tree,
    sha256_canonical,
    validate_artifact,
)


def valid_artifact():
    return {
        "fixture_id": "catalan_mu2_v0_1",
        "species": {
            "name": "CatalanFullBinaryTrees",
            "size": "internal_nodes",
            "generating_function": catalan_closed_form(),
            "equation": catalan_generating_equation(),
            "dominant_singularity": "1/4",
        },
        "branch_system": {
            "coordinate": "tau^2 = 1 - 4z",
            "fiber": "mu_2",
            "generator": "tau -> -tau",
            "analytic_signature_of_generator": -1,
        },
        "active_complex": {
            "name": "Assoc_n x mu_2",
            "n": 3,
            "state_shape": ["tree", "sheet"],
            "allowed_edge_types": ["rotation", "branch_flip"],
            "frozen": True,
        },
        "descent_phase": {
            "role": "select_active_complex",
            "output": "Assoc_3 x mu_2",
            "monodromy_claims_made": False,
        },
        "transport_phase": {
            "role": "neutral_probe",
            "mutates_active_complex": False,
            "path": [
                {
                    "type": "rotation",
                    "from": ["((ab)c)d", 1],
                    "to": ["(a(bc))d", 1],
                },
                {
                    "type": "branch_flip",
                    "from": ["(a(bc))d", 1],
                    "to": ["(a(bc))d", -1],
                },
            ],
            "declared_branch_parity": 1,
            "analytic_signature": -1,
            "gate_signature": -1,
        },
        "gate_assignment": {
            "rotation": {
                "so3_loop": "trivial",
                "spin_sign": 1,
            },
            "branch_flip": {
                "so3_loop": "2pi_rotation_SO3",
                "spin_lift_endpoint": "-I",
                "spin_sign": -1,
            },
        },
        "claims": {
            "allowed": ["fixture-level mu_2 monodromy agreement"],
            "not_claims": [
                "P vs NP",
                "closed Lyapunov cycle existence",
                "universal proof-system theorem",
                "empirical Lawful Learning validation",
                "odd-prime generalization",
            ],
        },
    }


def assert_rejects(artifact, code):
    with pytest.raises(ProofDynamicsValidationError) as excinfo:
        validate_artifact(artifact)
    assert excinfo.value.code == code


def test_catalan_species_fixture_values():
    assert [catalan_number(n) for n in range(5)] == [1, 1, 2, 5, 14]
    assert catalan_generating_equation() == "C(z) = 1 + z C(z)^2"
    assert catalan_closed_form() == "C(z) = (1 - sqrt(1 - 4z)) / (2z)"


def test_tree_normalization_and_rotation_neighbors():
    assert normalize_tree("((ab)c)d") == "(((ab)c)d)"
    assert internal_node_count("((ab)c)d") == 3
    assert is_rotation_edge("((ab)c)d", "(a(bc))d")
    assert "((a(bc))d)" in list_rotation_neighbors("((ab)c)d")


def test_branch_and_gate_signatures_are_parity():
    path = valid_artifact()["transport_phase"]["path"]
    assert branch_parity(path) == 1
    assert analytic_signature_from_parity(branch_parity(path)) == -1
    assert gate_signature(path) == -1

    doubled = path + [
        {"type": "branch_flip", "from": ["(a(bc))d", -1], "to": ["(a(bc))d", 1]}
    ]
    assert branch_parity(doubled) == 0
    assert analytic_signature_from_parity(branch_parity(doubled)) == 1
    assert gate_signature(doubled) == 1


def test_validator_accepts_valid_fixture():
    result = validate_artifact(valid_artifact())
    assert result == {
        "accepted": True,
        "fixture_id": "catalan_mu2_v0_1",
        "branch_parity": 1,
        "analytic_signature": -1,
        "gate_signature": -1,
        "commutes": True,
        "claim_status": "fixture_verified",
    }


def test_validator_rejects_overclaim_in_allowed_claims():
    artifact = valid_artifact()
    artifact["claims"]["allowed"].append("This proves P != NP.")
    assert_rejects(artifact, "PDV_CLAIM_070")


def test_validator_allows_non_claim_firewall_mentions():
    artifact = valid_artifact()
    artifact["claims"]["not_claims"].append("This is not an odd-prime generalization.")
    assert validate_artifact(artifact)["accepted"] is True


def test_validator_rejects_phase_mixing():
    artifact = valid_artifact()
    artifact["descent_phase"]["monodromy_claims_made"] = True
    assert_rejects(artifact, "PDV_PHASE_040")

    artifact = valid_artifact()
    artifact["transport_phase"]["mutates_active_complex"] = True
    assert_rejects(artifact, "PDV_PHASE_041")


def test_validator_rejects_invalid_branch_flip():
    artifact = valid_artifact()
    artifact["transport_phase"]["path"][1] = {
        "type": "branch_flip",
        "from": ["(a(bc))d", 1],
        "to": ["(a(bc))d", 1],
    }
    assert_rejects(artifact, "PDV_GRAPH_033")


def test_validator_rejects_rotation_that_changes_sheet():
    artifact = valid_artifact()
    artifact["transport_phase"]["path"][0] = {
        "type": "rotation",
        "from": ["((ab)c)d", 1],
        "to": ["(a(bc))d", -1],
    }
    assert_rejects(artifact, "PDV_GRAPH_032")


def test_validator_rejects_declared_signature_mismatch():
    artifact = valid_artifact()
    artifact["transport_phase"]["declared_branch_parity"] = 0
    assert_rejects(artifact, "PDV_MONO_060")

    artifact = valid_artifact()
    artifact["transport_phase"]["analytic_signature"] = 1
    assert_rejects(artifact, "PDV_MONO_061")

    artifact = valid_artifact()
    artifact["transport_phase"]["gate_signature"] = 1
    assert_rejects(artifact, "PDV_MONO_062")


def test_canonical_hash_changes_when_claims_or_path_change():
    artifact = valid_artifact()
    base = sha256_canonical(artifact)

    changed_claim = valid_artifact()
    changed_claim["claims"]["allowed"].append("extra fixture note")
    assert sha256_canonical(changed_claim) != base

    changed_path = valid_artifact()
    changed_path["transport_phase"]["path"].append(
        {"type": "branch_flip", "from": ["(a(bc))d", -1], "to": ["(a(bc))d", 1]}
    )
    assert sha256_canonical(changed_path) != base
