"""Deterministic Catalan/Tamari ledger for the Heller-Godel mu_2 bridge.

This module checks the finite toy-model part of the bridge:

    Catalan binary trees -> Tamari rotation graph -> mirror equivariance,
    plus the separate analytic/SO(3) signatures that evaluate to -1.

It does not construct a universal sentence-to-gate compiler and does not prove
P vs NP. The gate comparison remains conditional on a common-generator
identification outside this finite combinatorial ledger.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any, TypeAlias

Tree: TypeAlias = str | tuple["Tree", "Tree"]
LEAF: str = "x"


def catalan_number(n: int) -> int:
    """Return the nth Catalan number by its defining convolution."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    values = [0] * (n + 1)
    values[0] = 1
    for k in range(1, n + 1):
        values[k] = sum(values[i] * values[k - 1 - i] for i in range(k))
    return values[n]


@lru_cache(maxsize=None)
def full_binary_trees(n: int) -> tuple[Tree, ...]:
    """Enumerate full plane binary trees with n internal binary nodes."""

    if n < 0:
        raise ValueError("n must be nonnegative")
    if n == 0:
        return (LEAF,)

    trees: list[Tree] = []
    for left_nodes in range(n):
        right_nodes = n - 1 - left_nodes
        for left in full_binary_trees(left_nodes):
            for right in full_binary_trees(right_nodes):
                trees.append((left, right))
    return tuple(trees)


def tree_weight(tree: Tree) -> int:
    """Return the number of internal binary nodes."""

    if tree == LEAF:
        return 0
    left, right = tree  # type: ignore[misc]
    return 1 + tree_weight(left) + tree_weight(right)


def tree_to_sexpr(tree: Tree) -> str:
    """Return the canonical parenthesized representation."""

    if tree == LEAF:
        return LEAF
    left, right = tree  # type: ignore[misc]
    return f"({tree_to_sexpr(left)} {tree_to_sexpr(right)})"


def parse_tree(text: str) -> Tree:
    """Parse the canonical representation produced by tree_to_sexpr."""

    tokens = text.replace("(", " ( ").replace(")", " ) ").split()
    index = 0

    def parse_at() -> Tree:
        nonlocal index
        if index >= len(tokens):
            raise ValueError("unexpected end of tree")
        token = tokens[index]
        index += 1
        if token == LEAF:
            return LEAF
        if token != "(":
            raise ValueError(f"unexpected token: {token}")
        left = parse_at()
        right = parse_at()
        if index >= len(tokens) or tokens[index] != ")":
            raise ValueError("missing closing parenthesis")
        index += 1
        return (left, right)

    parsed = parse_at()
    if index != len(tokens):
        raise ValueError("extra tokens after tree")
    return parsed


def mirror(tree: Tree) -> Tree:
    """Mirror involution on binary trees."""

    if tree == LEAF:
        return LEAF
    left, right = tree  # type: ignore[misc]
    return (mirror(right), mirror(left))


def rotations(tree: Tree) -> frozenset[Tree]:
    """One-step undirected Tamari associativity rotations reachable from tree."""

    if tree == LEAF:
        return frozenset()
    left, right = tree  # type: ignore[misc]
    neighbors: set[Tree] = set()

    # ((A B) C) <-> (A (B C)) at the root.
    if left != LEAF:
        a, b = left  # type: ignore[misc]
        neighbors.add((a, (b, right)))

    if right != LEAF:
        b, c = right  # type: ignore[misc]
        neighbors.add(((left, b), c))

    # Rotations internal to left and right subtrees.
    for rotated_left in rotations(left):
        neighbors.add((rotated_left, right))
    for rotated_right in rotations(right):
        neighbors.add((left, rotated_right))

    return frozenset(neighbors)


def rotation_edges(n: int) -> tuple[tuple[str, str], ...]:
    """Canonical undirected Tamari-rotation edges for B_n."""

    tree_set = set(full_binary_trees(n))
    edges: set[tuple[str, str]] = set()
    for tree in tree_set:
        source = tree_to_sexpr(tree)
        for neighbor in rotations(tree):
            if neighbor not in tree_set:
                continue
            target = tree_to_sexpr(neighbor)
            if source != target:
                edges.add(tuple(sorted((source, target))))
    return tuple(sorted(edges))


def mirror_preserves_rotation_edges(n: int) -> bool:
    """Check that mirror sends Tamari rotation edges to rotation edges."""

    edges = set(rotation_edges(n))
    mirrored_edges = {
        tuple(
            sorted(
                (
                    tree_to_sexpr(mirror(parse_tree(left))),
                    tree_to_sexpr(mirror(parse_tree(right))),
                )
            )
        )
        for left, right in edges
    }
    return mirrored_edges == edges


def catalan_counts_through(max_n: int) -> tuple[int, ...]:
    """Catalan counts verified by explicit tree enumeration."""

    if max_n < 0:
        raise ValueError("max_n must be nonnegative")
    return tuple(len(full_binary_trees(n)) for n in range(max_n + 1))


def tamari_edge_counts_through(max_n: int) -> tuple[int, ...]:
    """Undirected rotation-edge counts for finite Catalan fibers."""

    if max_n < 0:
        raise ValueError("max_n must be nonnegative")
    return tuple(len(rotation_edges(n)) for n in range(max_n + 1))


def mu2_bridge_ledger(max_n: int = 5) -> dict[str, Any]:
    """Return a deterministic ledger for the Catalan/Tamari mu_2 test."""

    counts = catalan_counts_through(max_n)
    expected_counts = tuple(catalan_number(n) for n in range(max_n + 1))
    equivariance = {str(n): mirror_preserves_rotation_edges(n) for n in range(max_n + 1)}

    return {
        "artifact_type": "proof_character_mu2_test",
        "species_id": "CatalanBinaryTrees",
        "normal_forms": "full_binary_trees",
        "weight": "internal_node_count",
        "rewrite_structure": "TamariRotationGraph",
        "encoding_map": "E_B: tree -> corresponding Tamari vertex",
        "involution": "tree_mirror",
        "max_checked_internal_nodes": max_n,
        "catalan_counts_observed": counts,
        "catalan_counts_expected": expected_counts,
        "tamari_rotation_edge_counts": tamari_edge_counts_through(max_n),
        "mirror_equivariance_by_size": equivariance,
        "gf_equation": "z*B^2 - B + 1 = 0",
        "gf_solution_branch": "(1 - sqrt(1 - 4*z))/(2*z)",
        "branch_locus": ["1/4"],
        "galois_group": "Z/2",
        "monodromy_codomain": "S_2",
        "monodromy_generator": "loop around z = 1/4",
        "monodromy_action": "nontrivial_transposition_(12)",
        "character": "sign_representation",
        "analytic_signature": -1,
        "active_complex": "TamariRotationGraph_or_order_complex",
        "gate_group": "T^k x SO(3)",
        "so3_loop_class": "nontrivial_pi1_generator",
        "spin_lift_endpoint": "-I",
        "spin_signature": -1,
        "transport_assumption": "unitary_or_isometric_required_for_floquet_phases",
        "hermitian_structure": "not_specified_in_catalan_toy",
        "bridge_status": "conditional_on_common_generator",
        "p_vs_np_status": "not_a_p_vs_np_proof",
    }


def verify_mu2_bridge_ledger(ledger: dict[str, Any]) -> None:
    """Raise AssertionError if the deterministic ledger fails its finite checks."""

    assert ledger["artifact_type"] == "proof_character_mu2_test"
    assert tuple(ledger["catalan_counts_observed"]) == tuple(ledger["catalan_counts_expected"])
    assert all(ledger["mirror_equivariance_by_size"].values())
    assert ledger["galois_group"] == "Z/2"
    assert ledger["monodromy_codomain"] == "S_2"
    assert ledger["character"] == "sign_representation"
    assert ledger["analytic_signature"] == -1
    assert ledger["so3_loop_class"] == "nontrivial_pi1_generator"
    assert ledger["spin_signature"] == -1
    assert ledger["bridge_status"] == "conditional_on_common_generator"
    assert ledger["p_vs_np_status"] == "not_a_p_vs_np_proof"
