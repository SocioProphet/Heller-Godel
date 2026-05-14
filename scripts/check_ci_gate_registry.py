#!/usr/bin/env python3
"""Verify that GitHub Actions workflows and named steps are in the CI gate registry."""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"
REGISTRY = ROOT / "docs" / "governance" / "ci_gate_registry.md"

NAME_RE = re.compile(r"^name:\s*(.+?)\s*$")
JOB_RE = re.compile(r"^  ([A-Za-z0-9_-]+):\s*$")
STEP_NAME_RE = re.compile(r"^\s+-\s+name:\s*(.+?)\s*$")
USES_RE = re.compile(r"^\s+uses:\s*(.+?)\s*$")

# GitHub-generated post/complete steps are not represented in workflow YAML and are intentionally ignored.
GENERATED_STEP_PREFIXES: tuple[str, ...] = (
    "Post ",
    "Complete job",
)


def clean_scalar(value: str) -> str:
    return value.strip().strip('"\'')


def workflow_name(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        match = NAME_RE.match(line)
        if match:
            return clean_scalar(match.group(1))
    raise ValueError(f"workflow has no top-level name: {path}")


def workflow_jobs_and_steps(path: Path) -> tuple[list[str], list[str], list[str]]:
    """Return explicit job ids, named steps, and reusable workflow refs."""

    jobs: list[str] = []
    steps: list[str] = []
    reusable_refs: list[str] = []
    in_jobs = False
    in_steps = False

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line == "jobs:":
            in_jobs = True
            in_steps = False
            continue
        if not in_jobs:
            continue

        job_match = JOB_RE.match(raw_line)
        if job_match and not raw_line.startswith("    "):
            jobs.append(job_match.group(1))
            in_steps = False
            continue

        if raw_line.strip() == "steps:":
            in_steps = True
            continue

        if in_steps:
            step_match = STEP_NAME_RE.match(raw_line)
            if step_match:
                step_name = clean_scalar(step_match.group(1))
                if not step_name.startswith(GENERATED_STEP_PREFIXES):
                    steps.append(step_name)
                continue

        uses_match = USES_RE.match(raw_line)
        if uses_match and "workflows/" in uses_match.group(1):
            reusable_refs.append(clean_scalar(uses_match.group(1)))

    return jobs, steps, reusable_refs


def missing_terms_for_workflow(path: Path, registry_text: str) -> list[str]:
    name = workflow_name(path)
    rel = path.relative_to(ROOT).as_posix()
    jobs, steps, reusable_refs = workflow_jobs_and_steps(path)

    required_terms: list[tuple[str, str]] = [
        ("workflow filename", path.name),
        ("workflow path", rel),
        ("workflow name", name),
    ]
    required_terms.extend(("job id", job) for job in jobs)
    required_terms.extend(("step name", step) for step in steps)
    required_terms.extend(("reusable workflow ref", ref) for ref in reusable_refs)

    missing = [f"{kind}: {term!r}" for kind, term in required_terms if term not in registry_text]
    return missing


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
        rel = path.relative_to(ROOT).as_posix()
        missing_terms = missing_terms_for_workflow(path, registry_text)
        if missing_terms:
            missing.append(f"- {rel}: missing {', '.join(missing_terms)}")

    if missing:
        print("CI gate registry coverage failed.", file=sys.stderr)
        print("", file=sys.stderr)
        print(
            "Every workflow file must be listed in docs/governance/ci_gate_registry.md by filename, path, workflow name, job id, named step, and reusable workflow reference.",
            file=sys.stderr,
        )
        print("", file=sys.stderr)
        print("Missing coverage:", file=sys.stderr)
        for item in missing:
            print(item, file=sys.stderr)
        return 1

    print(f"CI gate registry coverage passed for {len(workflow_paths)} workflow(s), including job and named-step coverage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
