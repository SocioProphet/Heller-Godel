.PHONY: test governance-check

test:
	python -m pytest

governance-check:
	@echo "=== Claim boundary guard ==="
	python scripts/check_claim_boundaries.py
	@echo "=== Legacy topology audit ==="
	python scripts/audit_legacy_topology_terms.py \
		--diff-against-frozen \
		--fail-on-core \
		--fail-on-scope-drift
	@echo "=== CI gate registry coverage ==="
	python scripts/check_ci_gate_registry.py
	@echo "=== governance-check PASS ==="
