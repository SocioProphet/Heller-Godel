# Log-Prime-Volume Artifact Contract v0.1

Status: schema-level contract for Heller-Godel research artifacts.

Authorial boundary: the framework author is Michael Heller. Assistant contributions are review, formalization support, schema implementation support, and adversarial refinement.

Artifact kind: `log_prime_volume_candidate_ranking_artifact`.

Schema version: `heller-godel.log-prime-volume-artifact.v0.1`.

Required boundary fields:

- `claim_boundary.rh_proof_claimed` must be `false`.
- `claim_boundary.primality_certification_replaced` must be `false`.
- `claim_boundary.unconditional_error_bound_improvement_claimed` must be `false`.

Required coordinate gauge fields:

- `coordinate_gauge.coordinate`: `u = ln(x)`.
- `coordinate_gauge.ordinary_volume_element`: `dx = exp(u) du`.
- `coordinate_gauge.density_per_ordinary_x_volume`: `1/u`.
- `coordinate_gauge.log_coordinate_intensity`: `exp(u)/u`.

Required mean-field field:

- `mean_field.operator`: `PMF(u,L) = integral_u_to_u_plus_L exp(v)/v dv`.

Required residual fields:

- `residual_model.rh_envelope`: `exp(u/2)`.
- `residual_model.rh_envelope_status`: one of `conditional`, `diagnostic`.

Required ranking fields:

- `ranking_protocol.certification_separate_from_ranking` must be `true`.
- `ranking_protocol.required_baselines` must include `random_admissible_ordering` and `wheel_only_ordering`.

Required replay fields:

- `replay.code_ref`.
- `replay.input_hash`.
- `replay.output_hash`.

This contract is enforced by `src/heller_godel/schema_contracts.py` and regression tests. It exists to prevent the common failure modes: losing the log-volume element, turning RH-shaped diagnostics into proof claims, replacing certification with ranking, or dropping replay evidence.
