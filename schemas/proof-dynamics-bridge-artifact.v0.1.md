# Proof-Dynamics Bridge Artifact Contract v0.1

Status: conditional bridge contract for future-horizon Heller-Godel proof-dynamics artifacts.

Artifact kind: `proof_dynamics_bridge_artifact`.

Schema version: `heller-godel.proof-dynamics-bridge-artifact.v0.1`.

Required status:

- `claim_status` must be `conditional_construction`.

Required non-claims:

- `non_claims.p_vs_np_proof_claimed` must be `false`.
- `non_claims.empirical_validation_claimed` must be `false`.
- `non_claims.natural_canonicity_claimed` must be `false`.
- `non_claims.lawful_learning_validated` must be `false`.

Required first implementation target:

- `p_primary_case.prime`: `2`.
- `p_primary_case.torsion_group`: `mu_2`.
- `p_primary_case.expected_signature`: `-1`.

Required dynamics boundary:

- `dynamics_boundary.descent_transport_split_declared` must be `true`.
- `dynamics_boundary.floquet_unit_modulus_requires` must be `unitary_or_isometric_hypothesis`.

Required topology boundary:

- `topology_boundary.so3_action_noncommuting` must be `true`.
- `topology_boundary.pi1_so3_torsion_signature` must be `Z/2`.

Required encoding hypotheses:

- `encoding_hypotheses.proof_normal_forms_to_active_constraints`.
- `encoding_hypotheses.weight_preservation`.
- `encoding_hypotheses.rewrite_adjacency_preservation`.
- `encoding_hypotheses.cyclic_action_preservation`.
- `encoding_hypotheses.singularity_exponent_localization`.
- `encoding_hypotheses.boundary_transversality`.

All listed encoding hypotheses must be `true` before the artifact may claim the bridge contract. This does not prove canonicity; it records the assumptions required to test canonicity.

Required replay fields:

- `replay.code_ref`.
- `replay.input_hash`.
- `replay.output_hash`.

This contract is deliberately conservative. It prevents the bridge note from being misread as a proof of P vs NP, empirical validation of Lawful Learning, or a theorem about natural canonicity before the encoding functor has been constructed and tested.
