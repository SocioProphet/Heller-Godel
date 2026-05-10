"""Import uploaded corpus sources into the repository tree.

Run from repository root with:

    python scripts/import_uploaded_sources.py /path/to/uploaded/files

The script writes exact base64 text payloads for original binary files and, when
`pdftotext` is available, markdown text extractions for PDFs. BSD files remain
context-only; this script only captures them, it does not add them to tests.
"""

from __future__ import annotations

import base64
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
UPLOAD_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/mnt/data')

SOURCES = [
    ('heller godel motivation.pdf', 'sources/primary', 'heller_godel_motivation', 'primary'),
    ('calculus invariant characters v2(2).pdf', 'sources/primary', 'calculus_invariant_characters_v2', 'primary'),
    ('calculus invariant characters(2).pdf', 'sources/primary', 'calculus_invariant_characters_prior', 'primary'),
    ('time_theory_draft_v23_layout_exec(1).pdf', 'sources/context/temporal_mechanics', 'time_theory_draft_v23_layout_exec', 'context_future_horizon'),
    ('BSD_Program_Lane_v0.1.pdf', 'sources/context/bsd_program', 'BSD_Program_Lane_v0.1', 'context_only'),
    ('BSD_Program_Lane_v0.2.pdf', 'sources/context/bsd_program', 'BSD_Program_Lane_v0.2', 'context_only'),
    ('BSD_Program_Log_M3_snapshot.pdf', 'sources/context/bsd_program', 'BSD_Program_Log_M3_snapshot', 'context_only'),
    ('BSD_53_Rows_Resolution.pdf', 'sources/context/bsd_program', 'BSD_53_Rows_Resolution', 'context_only'),
    ('bsd_milestone_4(1).zip', 'sources/context/bsd_program', 'bsd_milestone_4', 'context_only'),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def write_base64(src: Path, base_dir: Path, stem: str, label: str) -> None:
    digest = sha256(src)
    out_dir = ROOT / base_dir / 'base64'
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f'{stem}.b64.md'
    encoded = base64.b64encode(src.read_bytes()).decode('ascii')
    out.write_text(
        '---\n'
        f'source_file: {src.name}\n'
        f'source_sha256: {digest}\n'
        'encoding: base64\n'
        f'label: {label}\n'
        'status: exact uploaded binary encoded as text\n'
        '---\n\n'
        '```text\n'
        f'{encoded}\n'
        '```\n'
    )


def write_pdf_markdown(src: Path, base_dir: Path, stem: str, label: str) -> None:
    if src.suffix.lower() != '.pdf' or shutil.which('pdftotext') is None:
        return
    digest = sha256(src)
    out_dir = ROOT / base_dir / 'extracted-markdown'
    out_dir.mkdir(parents=True, exist_ok=True)
    text = subprocess.check_output(['pdftotext', '-layout', str(src), '-'], text=True)
    out = out_dir / f'{stem}.md'
    out.write_text(
        '---\n'
        f'source_file: {src.name}\n'
        f'source_sha256: {digest}\n'
        'extraction: pdftotext -layout\n'
        f'label: {label}\n'
        'status: word-for-word text extraction from uploaded PDF; original source hash preserved\n'
        '---\n\n'
        '```text\n'
        f'{text}\n'
        '```\n'
    )


def main() -> None:
    for filename, rel_dir, stem, label in SOURCES:
        src = UPLOAD_DIR / filename
        if not src.exists():
            raise FileNotFoundError(src)
        base_dir = Path(rel_dir)
        write_base64(src, base_dir, stem, label)
        write_pdf_markdown(src, base_dir, stem, label)
    print('source import complete')


if __name__ == '__main__':
    main()
