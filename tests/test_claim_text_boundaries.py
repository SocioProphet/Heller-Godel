from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

# Only scan files that are allowed to make theorem-core claims. Review ledgers,
# future-horizon notes, and context notes may quote or discuss unsafe language.
SCAN_PATHS = [
    ROOT / "README.md",
    ROOT / "docs" / "manuscripts",
]

# These phrases are not banned absolutely. They are banned only when they appear
# as positive theorem-core claims rather than negated, quarantined, or future-horizon
# language. The manuscript may mention them as non-claims.
SENSITIVE_PHRASES = [
    "heisenberg-style",
    "nonabelian extension",
    "non-abelian extension",
    "non-split central extension",
    "cohomological obstruction",
    "chern-class lift",
    "holographic boundary",
    "ads/cft",
    "moufang",
    "octonionic",
]

SAFE_CONTEXT_MARKERS = [
    "not",
    "does not",
    "do not",
    "no ",
    "non-claim",
    "non-scope",
    "future horizon",
    "future-horizon",
    "quarantine",
    "blocked",
    "requires",
    "required",
    "not theorem-core",
    "not promoted",
    "not establish",
    "not established",
    "not constructed",
    "demote",
    "demoted",
]

# Direct assertive patterns that should never appear in theorem-core docs.
FORBIDDEN_ASSERTIVE_PATTERNS = [
    re.compile(r"zeta_p\s+(is|defines|classifies)\s+(a\s+)?nontrivial\s+.*cohomolog", re.I),
    re.compile(r"zeta_p\s+(is|defines|classifies)\s+(a\s+)?non[- ]?abelian", re.I),
    re.compile(r"zeta_p\s+(is|defines|classifies)\s+(a\s+)?non[- ]?split", re.I),
    re.compile(r"the\s+regulator\s+(constructs|gives|produces)\s+(the\s+)?chern", re.I),
    re.compile(r"chi_p\s+(is|defines)\s+(a\s+)?holographic\s+boundary", re.I),
]


def iter_scanned_files():
    for path in SCAN_PATHS:
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from path.rglob("*.md")


def window(text: str, start: int, end: int, radius: int = 220) -> str:
    return text[max(0, start - radius) : min(len(text), end + radius)].lower()


def test_no_forbidden_assertive_patterns_in_theorem_core_docs():
    failures = []
    for path in iter_scanned_files():
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_ASSERTIVE_PATTERNS:
            match = pattern.search(text)
            if match:
                failures.append(f"{path.relative_to(ROOT)}: {match.group(0)!r}")

    assert not failures, "Forbidden theorem-core overclaim(s):\n" + "\n".join(failures)


def test_sensitive_phrases_are_scoped_when_they_appear():
    failures = []
    for path in iter_scanned_files():
        text = path.read_text(encoding="utf-8")
        lower = text.lower()
        for phrase in SENSITIVE_PHRASES:
            start = 0
            while True:
                idx = lower.find(phrase, start)
                if idx == -1:
                    break
                context = window(text, idx, idx + len(phrase))
                if not any(marker in context for marker in SAFE_CONTEXT_MARKERS):
                    failures.append(
                        f"{path.relative_to(ROOT)}: phrase {phrase!r} lacks nearby boundary marker"
                    )
                start = idx + len(phrase)

    assert not failures, "Sensitive phrase(s) lack safe boundary context:\n" + "\n".join(failures)


def test_core_manuscript_explicitly_states_coboundary_boundary():
    manuscript = ROOT / "docs" / "manuscripts" / "calculus_invariant_characters_v2_1_3.md"
    text = manuscript.read_text(encoding="utf-8").lower()
    assert "coboundary" in text
    assert "section defect" in text
    assert "does not by itself establish" in text
