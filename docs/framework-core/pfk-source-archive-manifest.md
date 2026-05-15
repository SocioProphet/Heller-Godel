# PFK Source Archive Manifest

Status: source-supplied archive manifest.  
Claim level: provenance / extraction control.  
Mathematical content added by this document: none.  

## Source archive

| Field | Value |
| --- | --- |
| Uploaded archive | `Heller-Winters-Theorem-main_PFK 2.zip` |
| Archive SHA-256 | `92d34a45f5cb684a21a85639cb39f980e5279af48923fd6e87890a9e8f288cc8` |
| Archive size | `6522495` bytes |
| Extracted source root | `Heller-Winters-Theorem-main/proof_fabric_kernel/` |
| PFK file count | `24` |

## Inventory

| Path | Bytes | SHA-256 |
| --- | ---: | --- |
| `README.md` | 1626 | `c6664b19d6d9d5b44d33ed0c0fdc8ca2283fffeb593b4795d0b1bcf67ced956d` |
| `docs/CryptographicLanguagePolicy_v1.md` | 1825 | `9351ebae9eaf4fa4b3f1c4b2f5206e0c43c3aea1bf442f56b9426bde6aeba788` |
| `docs/FieldCalculus_PFK_Mapping_v1.md` | 6346 | `958ba7129a7307de66ec87fbd643a5d14d580526503f3dd9c25a3dd54cacf319` |
| `docs/IntegrationGuide_HellerWinters_SourceOS_v1.md` | 4116 | `71061feeb9c8a90b76457e543936f68ae599b6627ecba63416179fc01df4519d` |
| `docs/OperatorCatalog_PrimePolicyOperators_v1.md` | 6187 | `9c40eaec1339388216a260bf3b31a15143317e1871e2c2bace7ae259a9bf7c56` |
| `docs/PrimeStatsProtocol_v1.md` | 7407 | `721f4629d3cedb7a0c905d88d22cf5c31ded5aa808021e7780d9bdf3b78d4b73` |
| `docs/hill_ai_security_resynthesis_v1.md` | 19095 | `57849a0f93b99f9c0aa1d5067f1618eb559e64de99bcb4b857161402def0fdf8` |
| `examples/lawful_learning/lawful_learning_example_trace.json` | 3096 | `05cee7887d5d84d025f20b5137423eaf288597b8949149633a7aae7a02523892` |
| `examples/lawful_learning/proof_artifact_lawful_learning_example.json` | 1820 | `5966ff865cfe5fa4a2abc4f13f315fd85fb059da55bd24d07ba761b56e7c7f2a` |
| `examples/primes/calibration_bundle_example.json` | 1387 | `c1d453f87ec4c85b8136a72fa2ed015aa150ed794f95dd97c936b3033c44d083` |
| `examples/primes/calibration_bundle_example.yaml` | 701 | `11b68581d4f3997d912e966b8efd83c243b46b5e88d5de9d2840bf1823708741` |
| `examples/primes/primes_phase_example_trace.json` | 6410 | `c510ef3d0db65647017f2cee9776f265c8234e79002a81bf9c907c6e7d8a9773` |
| `examples/primes/proof_artifact_primes_example.json` | 1738 | `01e008ce39254c72f04752bffa534e96e4f0ecd9bc94df7a0241026eda69f318` |
| `examples/security/hsm_leak_trace.json` | 1912 | `ab66d3280ef68528b17eb4b8605fde5b7e57a2040a7ef82f11d0ff5e2a3602f3` |
| `examples/security/hsm_safe_trace.json` | 1467 | `25226df8be6001ed4586cf9010e7b350f848da3d6cd92398f0bf3c96a6549ec2` |
| `examples/security/proof_artifact_hsm_leak.json` | 2308 | `b009dc143fd2bc45ba100818da9231c5518e7d1cb8603ed13e1a1aa33134e3e1` |
| `examples/security/proof_artifact_hsm_safe.json` | 1877 | `830af965aadeda32db23acb7a4ac8419f770d6552972b96a85baf4ca662b4cf9` |
| `schemas/calibration_bundle.schema.json` | 2115 | `c92d50eaf11b3988da399ff14e9852dfd4b9c9568ef089887b951b02e7a849db` |
| `schemas/claim_ledger_row.schema.json` | 1444 | `aaa46f093050b5f8f5f5fa2a6f2cae32aabb4d83539484f4a0babd68185c532c` |
| `schemas/event_ir.schema.json` | 31671 | `829a758cd75f2199911aba7f09d7c55437a87380eb310074b8bd76840778a3ca` |
| `schemas/proof_artifact.schema.json` | 8351 | `12b55c5d12267e77d0d465a0f00c617412c7607052d0a441d2c0f9355fcdd0db` |
| `tools/hash_manifest.py` | 1008 | `62a18c152b419dc904551f9d17054e4f8b465ca20b7f2edf2edf362054a82ab4` |
| `tools/validate_event_ir.py` | 1693 | `57c7d0d51ba8df0808c0e1337b14cfcf2b73e507628d089ea8b9ea5f52306326` |
| `tools/validate_proof_artifact.py` | 1121 | `360628fa9f4f90852f45a0104e9d1a0644a92d42840ac94f5784557d66e2c90c` |

## Local validation performed

The archive was inspected as supplied, without rewriting source files.

Validation results:

```text
JSON parse: OK for all `.json` schema and example files.
Event-IR validator: OK for primes, security safe/leak, and lawful-learning traces.
ProofArtifact validator: OK for primes, security safe/leak, and lawful-learning proof artifacts.
Calibration bundle schema validation: OK for `examples/primes/calibration_bundle_example.json`.
```

Commands executed locally:

```bash
python3 tools/validate_event_ir.py --schema schemas/event_ir.schema.json --trace examples/primes/primes_phase_example_trace.json
python3 tools/validate_event_ir.py --schema schemas/event_ir.schema.json --trace examples/security/hsm_safe_trace.json
python3 tools/validate_event_ir.py --schema schemas/event_ir.schema.json --trace examples/security/hsm_leak_trace.json
python3 tools/validate_event_ir.py --schema schemas/event_ir.schema.json --trace examples/lawful_learning/lawful_learning_example_trace.json
python3 tools/validate_proof_artifact.py --schema schemas/proof_artifact.schema.json --artifact examples/primes/proof_artifact_primes_example.json
python3 tools/validate_proof_artifact.py --schema schemas/proof_artifact.schema.json --artifact examples/security/proof_artifact_hsm_safe.json
python3 tools/validate_proof_artifact.py --schema schemas/proof_artifact.schema.json --artifact examples/security/proof_artifact_hsm_leak.json
python3 tools/validate_proof_artifact.py --schema schemas/proof_artifact.schema.json --artifact examples/lawful_learning/proof_artifact_lawful_learning_example.json
python3 - <<'PY'
import json, jsonschema, pathlib
root = pathlib.Path(".")
schema = json.loads((root / "schemas/calibration_bundle.schema.json").read_text())
data = json.loads((root / "examples/primes/calibration_bundle_example.json").read_text())
jsonschema.validate(data, schema)
PY
```

## Extraction status

This manifest establishes source-supplied extraction mode. It supersedes any reconstruction-only plan for the files listed above.

The binary archive itself is not committed here. The target repository should receive the extracted `proof_fabric_kernel/` tree byte-for-byte, preserving the file hashes recorded above.

## Non-claim boundary

This manifest does not promote PFK schemas to mathematical theorem status. It records source provenance and local validation only.
