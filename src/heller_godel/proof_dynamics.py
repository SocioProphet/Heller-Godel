"""Fixture-level proof-dynamics verifier for Catalan mu_2 monodromy.

This module is deliberately narrow. It verifies the finite Catalan p=2
fixture only: a branched Catalan proof species, active complex
Assoc_n x mu_2, and an SO(3) spin-gate assignment whose sign is computed by
branch-flip parity.

It does not prove P vs NP, universal proof-system dynamics, closed Lyapunov
cycle existence, empirical Lawful Learning validation, or odd-prime
generalization.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from typing import Any, Iterable

CATALAN_FIXTURE_ID = "catalan_mu2_v0_1"


class ProofDynamicsValidationError(ValueError):
    """Raised when a proof-dynamics artifact fails deterministic validation."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code
        self.message = message


Tree = str | tuple["Tree", "Tree"]


@dataclass(frozen=True)
class ValidationResult:
    accepted: bool
    fixture_id: str
    branch_parity: int
    analytic_signature: int
    gate_signature: int
    commutes: bool
    claim_status: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "accepted": self.accepted,
            "fixture_id": self.fixture_id,
            "branch_parity": self.branch_parity,
            "analytic_signature": self.analytic_signature,
            "gate_signature": self.gate_signature,
            "commutes": self.commutes,
            "claim_status": self.claim_status,
        }


def catalan_number(n: int) -> int:
    """Return the nth Catalan number by the exact binomial formula."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    from math import comb

    return comb(2 * n, n) // (n + 1)


def catalan_generating_equation() -> str:
    return "C(z) = 1 + z C(z)^2"


def catalan_closed_form() -> str:
    return "C(z) = (1 - sqrt(1 - 4z)) / (2z)"


def dominant_singularity() -> str:
    return "1/4"


def branch_coordinate() -> str:
    return "tau^2 = 1 - 4z"


def _fail(code: str, message: str) -> None:
    raise ProofDynamicsValidationError(code, message)


def validate_sheet(sheet: int) -> None:
    if sheet not in (-1, 1):
        _fail("PDV_GRAPH_031", "sheet must be +1 or -1")


def flip_sheet(sheet: int) -> int:
    validate_sheet(sheet)
    return -sheet


def _strip_tree(tree: str) -> str:
    return re.sub(r"\s+", "", tree)


def parse_tree(tree: str) -> Tree:
    """Parse a compact full-binary-tree expression.

    Leaves are single alphanumeric symbols. Juxtaposition denotes binary
    composition and is grouped left-associatively when the outermost pair of
    parentheses is omitted. Thus ``((ab)c)d`` and ``(((ab)c)d)`` parse to the
    same tree.
    """

    text = _strip_tree(tree)
    if not text:
        _fail("PDV_GRAPH_031", "empty tree expression")

    def parse_atom(index: int) -> tuple[Tree, int]:
        if index >= len(text):
            _fail("PDV_GRAPH_031", "unexpected end of tree expression")
        char = text[index]
        if char == "(":
            node, next_index = parse_sequence(index + 1, stop=")")
            if next_index >= len(text) or text[next_index] != ")":
                _fail("PDV_GRAPH_031", "unclosed parenthesis in tree expression")
            return node, next_index + 1
        if char.isalnum():
            return char, index + 1
        _fail("PDV_GRAPH_031", f"invalid tree character {char!r}")
        raise AssertionError("unreachable")

    def parse_sequence(index: int, stop: str | None = None) -> tuple[Tree, int]:
        terms: list[Tree] = []
        while index < len(text) and (stop is None or text[index] != stop):
            term, index = parse_atom(index)
            terms.append(term)
        if not terms:
            _fail("PDV_GRAPH_031", "empty tree subexpression")
        node = terms[0]
        for term in terms[1:]:
            node = (node, term)
        return node, index

    node, end = parse_sequence(0)
    if end != len(text):
        _fail("PDV_GRAPH_031", "trailing tree expression content")
    return node


def normalize_tree(tree: str) -> str:
    return serialize_tree(parse_tree(tree))


def serialize_tree(tree: Tree) -> str:
    if isinstance(tree, str):
        return tree
    left, right = tree
    return f"({serialize_tree(left)}{serialize_tree(right)})"


def is_full_binary_tree(tree: str) -> bool:
    try:
        parse_tree(tree)
    except ProofDynamicsValidationError:
        return False
    return True


def leaf_count(tree: str | Tree) -> int:
    parsed = parse_tree(tree) if isinstance(tree, str) else tree
    if isinstance(parsed, str):
        return 1
    return leaf_count(parsed[0]) + leaf_count(parsed[1])


def internal_node_count(tree: str | Tree) -> int:
    parsed = parse_tree(tree) if isinstance(tree, str) else tree
    if isinstance(parsed, str):
        return 0
    return 1 + internal_node_count(parsed[0]) + internal_node_count(parsed[1])


def _rotation_neighbors_tree(tree: Tree) -> set[Tree]:
    if isinstance(tree, str):
        return set()

    left, right = tree
    neighbors: set[Tree] = set()

    # ((A B) C) -> (A (B C))
    if isinstance(left, tuple):
        a, b = left
        neighbors.add((a, (b, right)))

    # (A (B C)) -> ((A B) C)
    if isinstance(right, tuple):
        b, c = right
        neighbors.add(((left, b), c))

    for new_left in _rotation_neighbors_tree(left):
        neighbors.add((new_left, right))
    for new_right in _rotation_neighbors_tree(right):
        neighbors.add((left, new_right))

    return neighbors


def list_rotation_neighbors(tree: str) -> list[str]:
    parsed = parse_tree(tree)
    return sorted(serialize_tree(neighbor) for neighbor in _rotation_neighbors_tree(parsed))


def is_rotation_edge(src: str, dst: str) -> bool:
    normalized_dst = normalize_tree(dst)
    return normalized_dst in list_rotation_neighbors(src)


def _state(step: dict[str, Any], key: str) -> tuple[str, int]:
    raw = step.get(key)
    if not isinstance(raw, list | tuple) or len(raw) != 2:
        _fail("PDV_GRAPH_031", f"{key} state must be [tree, sheet]")
    tree, sheet = raw
    if not isinstance(tree, str):
        _fail("PDV_GRAPH_031", f"{key} tree must be a string")
    if not isinstance(sheet, int):
        _fail("PDV_GRAPH_031", f"{key} sheet must be an integer +1 or -1")
    validate_sheet(sheet)
    return normalize_tree(tree), sheet


def validate_rotation_step(step: dict[str, Any]) -> None:
    src_tree, src_sheet = _state(step, "from")
    dst_tree, dst_sheet = _state(step, "to")
    if src_sheet != dst_sheet:
        _fail("PDV_GRAPH_032", "rotation edges must preserve sheet")
    if not is_rotation_edge(src_tree, dst_tree):
        _fail("PDV_GRAPH_032", "invalid associahedral rotation")


def validate_branch_flip_step(step: dict[str, Any]) -> None:
    src_tree, src_sheet = _state(step, "from")
    dst_tree, dst_sheet = _state(step, "to")
    if src_tree != dst_tree:
        _fail("PDV_GRAPH_033", "branch flip must preserve tree")
    if dst_sheet != -src_sheet:
        _fail("PDV_GRAPH_033", "branch flip must change sheet")


def branch_parity(path: Iterable[dict[str, Any]]) -> int:
    parity = 0
    for step in path:
        if step.get("type") == "branch_flip":
            parity ^= 1
    return parity


def analytic_signature_from_parity(parity: int) -> int:
    return -1 if parity else 1


def gate_loop_for_step(step_type: str) -> str:
    if step_type == "rotation":
        return "trivial"
    if step_type == "branch_flip":
        return "2pi_rotation_SO3"
    _fail("PDV_GRAPH_033", f"unknown step type {step_type!r}")
    raise AssertionError("unreachable")


def spin_sign_for_step(step_type: str) -> int:
    if step_type == "rotation":
        return 1
    if step_type == "branch_flip":
        return -1
    _fail("PDV_GRAPH_033", f"unknown step type {step_type!r}")
    raise AssertionError("unreachable")


def gate_signature(path: Iterable[dict[str, Any]]) -> int:
    signature = 1
    for step in path:
        signature *= spin_sign_for_step(step.get("type"))
    return signature


def canonical_json(payload: dict[str, Any]) -> str:
    """Return stable canonical JSON for replay hashing."""

    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_canonical(payload: dict[str, Any]) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


FORBIDDEN_CLAIM_PATTERNS: tuple[str, ...] = (
    "p != np",
    "p≠np",
    "proves p vs np",
    "proof of p vs np",
    "p vs np result",
    "universal proof-system theorem",
    "closed lyapunov cycle existence",
    "empirical lawful learning validation",
    "odd-prime generalization",
)


def _iter_claim_strings(value: Any, *, skip: bool = False) -> Iterable[str]:
    if isinstance(value, dict):
        for key, child in value.items():
            child_skip = skip or key in {"not_claims", "exclusions", "dependencies"}
            yield from _iter_claim_strings(child, skip=child_skip)
    elif isinstance(value, list | tuple):
        for child in value:
            yield from _iter_claim_strings(child, skip=skip)
    elif isinstance(value, str) and not skip:
        yield value


def reject_overclaims(claims: Any) -> None:
    text = "\n".join(_iter_claim_strings(claims)).lower()
    for pattern in FORBIDDEN_CLAIM_PATTERNS:
        if pattern in text:
            _fail("PDV_CLAIM_070", f"forbidden overclaim detected: {pattern}")


def validate_species(species: dict[str, Any]) -> None:
    if species.get("name") != "CatalanFullBinaryTrees":
        _fail("PDV_SPECIES_010", "declared species is not Catalan full binary trees")
    if species.get("generating_function") != catalan_closed_form():
        _fail("PDV_SPECIES_011", "generating function does not match Catalan closed form")
    if species.get("equation") != catalan_generating_equation():
        _fail("PDV_SPECIES_011", "generating equation does not match Catalan equation")


def validate_branch_system(branch_system: dict[str, Any]) -> None:
    if branch_system.get("coordinate") != branch_coordinate():
        _fail("PDV_BRANCH_020", "branch coordinate is not tau^2 = 1 - 4z")
    if branch_system.get("fiber") != "mu_2":
        _fail("PDV_BRANCH_021", "branch fiber is not mu_2")
    if branch_system.get("generator") != "tau -> -tau":
        _fail("PDV_BRANCH_022", "monodromy generator is not tau -> -tau")


def validate_active_complex(active_complex: dict[str, Any]) -> None:
    if active_complex.get("name") != "Assoc_n x mu_2":
        _fail("PDV_GRAPH_030", "active complex is not Assoc_n x mu_2")
    if active_complex.get("frozen") is not True:
        _fail("PDV_PHASE_041", "active complex must be frozen before transport")


def validate_phase_separation(descent_phase: dict[str, Any], transport_phase: dict[str, Any]) -> None:
    if descent_phase.get("monodromy_claims_made") is not False:
        _fail("PDV_PHASE_040", "descent phase asserts monodromy")
    if transport_phase.get("mutates_active_complex") is not False:
        _fail("PDV_PHASE_041", "transport phase mutates frozen active complex")
    if transport_phase.get("role") != "neutral_probe":
        _fail("PDV_PHASE_042", "transport phase must be a neutral probe")


def validate_gate_assignment(gate_assignment: dict[str, Any]) -> None:
    rotation = gate_assignment.get("rotation", {})
    branch = gate_assignment.get("branch_flip", {})
    if rotation.get("so3_loop") != "trivial" or rotation.get("spin_sign") != 1:
        _fail("PDV_GATE_050", "rotation edge must be assigned trivial SO(3) loop")
    if branch.get("so3_loop") != "2pi_rotation_SO3":
        _fail("PDV_GATE_051", "branch edge must be assigned SO(3) 2pi loop")
    if branch.get("spin_lift_endpoint") != "-I" or branch.get("spin_sign") != -1:
        _fail("PDV_GATE_052", "branch edge spin lift endpoint must be -I with sign -1")


def validate_transport_path(path: list[dict[str, Any]]) -> None:
    for step in path:
        step_type = step.get("type")
        if step_type == "rotation":
            validate_rotation_step(step)
        elif step_type == "branch_flip":
            validate_branch_flip_step(step)
        else:
            _fail("PDV_GRAPH_033", f"unrecognized transport step type {step_type!r}")


def validate_artifact(artifact: dict[str, Any]) -> dict[str, Any]:
    """Validate a Catalan mu_2 proof-dynamics artifact."""

    for field in (
        "fixture_id",
        "species",
        "branch_system",
        "active_complex",
        "descent_phase",
        "transport_phase",
        "gate_assignment",
        "claims",
    ):
        if field not in artifact:
            _fail("PDV_SCHEMA_001", f"missing required field {field}")

    if artifact["fixture_id"] != CATALAN_FIXTURE_ID:
        _fail("PDV_SCHEMA_002", "unrecognized fixture version")

    validate_species(artifact["species"])
    validate_branch_system(artifact["branch_system"])
    validate_active_complex(artifact["active_complex"])
    validate_phase_separation(artifact["descent_phase"], artifact["transport_phase"])
    validate_gate_assignment(artifact["gate_assignment"])
    reject_overclaims(artifact["claims"])

    path = artifact["transport_phase"].get("path")
    if not isinstance(path, list):
        _fail("PDV_SCHEMA_001", "transport path must be a list")

    validate_transport_path(path)

    parity = branch_parity(path)
    analytic_signature = analytic_signature_from_parity(parity)
    computed_gate_signature = gate_signature(path)

    if artifact["transport_phase"].get("declared_branch_parity") != parity:
        _fail("PDV_MONO_060", "declared branch parity does not match recomputation")
    if artifact["transport_phase"].get("analytic_signature") != analytic_signature:
        _fail("PDV_MONO_061", "declared analytic signature does not match recomputation")
    if artifact["transport_phase"].get("gate_signature") != computed_gate_signature:
        _fail("PDV_MONO_062", "declared gate signature does not match recomputation")

    return ValidationResult(
        accepted=True,
        fixture_id=artifact["fixture_id"],
        branch_parity=parity,
        analytic_signature=analytic_signature,
        gate_signature=computed_gate_signature,
        commutes=analytic_signature == computed_gate_signature,
        claim_status="fixture_verified",
    ).as_dict()
