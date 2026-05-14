#!/usr/bin/env python3
"""Audit legacy topology terminology in scoped Heller-Godel file classes.

This is an audit tool, not an automatic rewriter. It deliberately separates
current theorem-core files from context, historical/source-capture material,
and legacy manuscripts so remediation can be reviewed without destroying the
record of earlier framings.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
import re
import sys
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FROZEN_LEDGER = ROOT / "docs" / "review-ledgers" / "HG_LEGACY_TOPOLOGY_TERMS_AUDIT.md"
REPORT_START = "<!-- AUDIT_REPORT_START -->"
REPORT_END = "<!-- AUDIT_REPORT_END -->"


@dataclass(frozen=True)
class PatternSpec:
    name: str
    regex: re.Pattern[str]
    severity: str
    replacement_hint: str


PATTERNS: tuple[PatternSpec, ...] = (
    PatternSpec(
        "pi-one-base-symbol",
        re.compile(r"Π₁\(B\)|\\Pi_1\(B\)|\\Pi_1\{?\(?B\)?\}?"),
        "core-blocker",
        r"Use current finite-local-system pi_1 language, or use \\mathsf{Path}(B) only in path-category transport sections.",
    ),
    PatternSpec(
        "fundamental-path-groupoid",
        re.compile(r"fundamental path groupoid", re.IGNORECASE),
        "core-blocker",
        "Use geometric path category where path transport, not homotopy-class groupoid structure, is intended.",
    ),
    PatternSpec(
        "generic-groupoid-language",
        re.compile(r"\bgroupoid\b", re.IGNORECASE),
        "review-required",
        "Review in theorem-core. Groupoid language is allowed only when an actual groupoid object is being defined, not as stale path-space shorthand.",
    ),
    PatternSpec(
        "homotopy-class-language",
        re.compile(r"homotopy classes|homotopy class", re.IGNORECASE),
        "core-blocker",
        "Use piecewise-smooth paths modulo orientation-preserving reparametrization where that is the intended object.",
    ),
    PatternSpec(
        "old-fiber-product-path-object",
        re.compile(r"E\s*[×x]_{B,s}\s*(?:Π₁\(B\)|\\Pi_1\(B\))"),
        "core-blocker",
        r"Use E ×_{B,s} \\mathsf{Path}(B) only in horizontal-lift/path-category sections.",
    ),
    PatternSpec(
        "old-horizontal-lift-domain",
        re.compile(r"(?:γ|gamma)\s*(?:∈|in)\s*(?:Π₁\(B\)|\\Pi_1\(B\))"),
        "core-blocker",
        r"Use γ ∈ \\mathsf{Path}(B) and type Φ_γ : E_{s(γ)} → E_{t(γ)} only if horizontal lifts are active.",
    ),
    PatternSpec(
        "simply-connected-proof-rationale",
        re.compile(r"since\s+S\^?2\s+is\s+simply\s+connected|because\s+S\^?2\s+is\s+simply\s+connected", re.IGNORECASE),
        "review-required",
        "Allowed only as sanity-check topology; do not use it as a theorem-grade substitute for the current finite-local-system argument.",
    ),
    PatternSpec(
        "every-loop-contractible-rationale",
        re.compile(r"every loop is contractible", re.IGNORECASE),
        "review-required",
        "Allowed only in historical/context notes; theorem-core should use explicit pi_1/local-system triviality if applicable.",
    ),
)


@dataclass(frozen=True)
class FileClass:
    tag: str
    path_patterns: tuple[str, ...]
    fail_on_hit: bool
    note: str


FILE_CLASSES: tuple[FileClass, ...] = (
    FileClass(
        "theorem-core",
        (
            "docs/manuscripts/paper_i_*.md",
            "docs/appendices/appendix_a_*.md",
            "docs/gates/minimality.md",
            "src/heller_godel/*.py",
        ),
        True,
        "Active theorem/proof/computation surface. Hits require remediation or an inline exemption.",
    ),
    FileClass(
        "context-no-patch",
        (
            "docs/context/**/*",
            "sources/primary/**/*",
            "sources/context/**/*",
            "data/manifests/**/*",
        ),
        False,
        "Context and source evidence. Hits are reported but should not be rewritten as theorem-core remediation.",
    ),
    FileClass(
        "historical-no-patch",
        (
            "docs/source-captures/**/*",
            "**/*historical*",
            "**/*history*",
        ),
        False,
        "Historical/source-capture material. Preserve unless a separate archival normalization is approved.",
    ),
    FileClass(
        "legacy-manuscript-no-patch",
        (
            "docs/manuscripts/calculus_invariant_characters_*.md",
            "docs/manuscripts/*patch_plan*.md",
        ),
        False,
        "Superseded or legacy manuscript material. Report separately from active Paper I theorem core.",
    ),
)


@dataclass(frozen=True)
class Hit:
    file_class: str
    path: Path
    line_number: int
    pattern: PatternSpec
    line: str


def iter_classified_files(root: Path) -> Iterable[tuple[FileClass, Path]]:
    seen: set[Path] = set()
    for file_class in FILE_CLASSES:
        for pattern in file_class.path_patterns:
            for path in root.glob(pattern):
                if not path.is_file():
                    continue
                resolved = path.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                yield file_class, path


def scan_file(file_class: FileClass, path: Path) -> list[Hit]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    hits: list[Hit] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for pattern in PATTERNS:
            if pattern.regex.search(line):
                hits.append(Hit(file_class.tag, path, line_number, pattern, line.strip()))
    return hits


def render_markdown(hits: list[Hit], root: Path) -> str:
    lines: list[str] = []
    lines.append("# Legacy Topology Terminology Audit")
    lines.append("")
    lines.append("Generated by `scripts/audit_legacy_topology_terms.py`.")
    lines.append("")
    lines.append("## Scope classes")
    lines.append("")
    for file_class in FILE_CLASSES:
        fail_text = "yes" if file_class.fail_on_hit else "no"
        patterns = ", ".join(f"`{p}`" for p in file_class.path_patterns)
        lines.append(f"- **{file_class.tag}** — fail on hit: `{fail_text}` — {file_class.note} Patterns: {patterns}")
    lines.append("")
    lines.append("## Pattern coverage")
    lines.append("")
    for pattern in PATTERNS:
        lines.append(f"- **{pattern.name}** / `{pattern.severity}` — {pattern.replacement_hint}")
    lines.append("")
    lines.append("## Hits")
    lines.append("")
    if not hits:
        lines.append("No scoped hits found.")
        return "\n".join(lines) + "\n"

    current_key: tuple[str, Path] | None = None
    for hit in hits:
        rel = hit.path.relative_to(root)
        key = (hit.file_class, rel)
        if key != current_key:
            lines.append("")
            lines.append(f"### `{hit.file_class}` — `{rel}`")
            current_key = key
        escaped = hit.line.replace("`", "\\`")
        lines.append(f"- L{hit.line_number}: `{hit.pattern.name}` / `{hit.pattern.severity}` — `{escaped}`")
        lines.append(f"  - Hint: {hit.pattern.replacement_hint}")
    lines.append("")
    return "\n".join(lines)


def frozen_report_payload(frozen_text: str) -> str:
    """Return the authoritative report payload from a frozen ledger.

    Ledgers may preserve historical connector-backed context outside the exact
    scanner output. When AUDIT_REPORT_START / AUDIT_REPORT_END markers exist,
    only the marked payload is compared. Without markers, the whole file remains
    the comparison target for backward compatibility.
    """

    if REPORT_START not in frozen_text and REPORT_END not in frozen_text:
        return frozen_text
    if REPORT_START not in frozen_text or REPORT_END not in frozen_text:
        raise ValueError("frozen ledger has incomplete audit report markers")
    start = frozen_text.index(REPORT_START) + len(REPORT_START)
    end = frozen_text.index(REPORT_END, start)
    return frozen_text[start:end].strip("\n") + "\n"


def compare_against_frozen(current_report: str, frozen_path: Path) -> int:
    """Return 0 when current report matches the frozen authoritative payload."""

    if not frozen_path.exists():
        print(f"frozen report not found: {frozen_path}", file=sys.stderr)
        return 2
    frozen = frozen_path.read_text(encoding="utf-8")
    try:
        frozen_payload = frozen_report_payload(frozen)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    if frozen_payload == current_report:
        print(f"local audit matches frozen report payload: {frozen_path}")
        return 0
    print(f"local audit diverges from frozen report payload: {frozen_path}", file=sys.stderr)
    print("write the local report with --output and open a correction PR before remediation", file=sys.stderr)
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root to scan.")
    parser.add_argument("--fail-on-core", action="store_true", help="Exit 1 if theorem-core hits are found.")
    parser.add_argument("--output", type=Path, help="Write markdown report to this path.")
    parser.add_argument(
        "--diff-against-frozen",
        type=Path,
        nargs="?",
        const=DEFAULT_FROZEN_LEDGER,
        help="Compare generated report against the frozen ledger payload; optionally pass a custom ledger path.",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    hits: list[Hit] = []
    for file_class, path in iter_classified_files(root):
        hits.extend(scan_file(file_class, path))

    report = render_markdown(hits, root)
    exit_code = 0

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)

    if args.diff_against_frozen:
        exit_code = max(exit_code, compare_against_frozen(report, args.diff_against_frozen.resolve()))

    if args.fail_on_core:
        core_hits = [hit for hit in hits if hit.file_class == "theorem-core"]
        if core_hits:
            print(f"legacy topology audit failed: {len(core_hits)} theorem-core hit(s)", file=sys.stderr)
            exit_code = max(exit_code, 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
