#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('root', nargs='?', default='proof_fabric_kernel')
    args = parser.parse_args()
    root = Path(args.root)
    rows = []
    for path in sorted(root.rglob('*')):
        if path.is_file():
            rows.append({'path': path.relative_to(root).as_posix(), 'bytes': path.stat().st_size, 'sha256': sha256(path)})
    print(json.dumps({'root': str(root), 'files': rows}, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
