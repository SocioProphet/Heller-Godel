#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--schema', required=True)
    parser.add_argument('--trace', required=True)
    args = parser.parse_args()
    schema = json.loads(Path(args.schema).read_text(encoding='utf-8'))
    data = json.loads(Path(args.trace).read_text(encoding='utf-8'))
    validator = jsonschema.Draft202012Validator(schema)
    events = data if isinstance(data, list) else [data]
    for event in events:
        validator.validate(event)
    print(f'validated {len(events)} event(s): {args.trace}')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
