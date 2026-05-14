#!/usr/bin/env python3
"""Verify that every GitHub Actions workflow is registered in the CI gate registry."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"
REGISTRY = ROOT / "docs" / "governance" / "ci_gate_registry.md"

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")


def workflow_name(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        match = NAME_RE.match(line)
        if match:
            return match.group(1).strip().strip('"\'')
    raise ValueError(f"workflow has no top-level name: {path}")


def main() -> int:
    if not WORKFLOW_DIR.exists():
        print(f"workflow directory not found: {WORKFLOW_DIR}", file=sys.stderr)
        return 1
    if not REGISTRY.exists():
        print(f"CI gate registry not found: {REGISTRY}", file=sys.stderr)
        return 1

    registry_text = REGISTRY.read_text(encoding="utf-8")
    workflow_paths = sorted(
        list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml")),
        key=lambda path: path.name,
    )

    missing: list[str] = []
    for path in workflow_paths:
        name = workflow_name(path)
        rel = path.relative_to(ROOT).as_posix()
        missing_terms = [term for term in (path.name, rel, name) if term not in registry_text]
        if missing_terms:
            missing.append(
                f"- {rel} (name: {name!r}) missing registry term(s): {', '.join(repr(term) for term in missing_terms)}"
            )

    if missing:
        print("CI gate registry coverage failed.", file=sys.stderr)
        print("", file=sys.stderr)
        print("Every workflow file must be listed in docs/governance/ci_gate_registry.md by filename, path, and workflow name.", file=sys.stderr)
        print("", file=sys.stderr)
        print("Missing coverage:", file=sys.stderr)
        for item in missing:
            print(item, file=sys.stderr)
        return 1

    print(f"CI gate registry coverage passed for {len(workflow_paths)} workflow(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
