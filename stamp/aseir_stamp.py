"""Settings stamps for ASEIR backtests and alerts.

Every chart, report and trade preview we deliver carries a 12-character stamp. The
stamp is the first 12 hex characters of the SHA-256 of the run's settings, serialised
as canonical JSON (keys sorted, no whitespace, UTF-8). Anyone holding the settings
file can recompute it; change a single parameter, or a single candle in the data
(captured by the ``data`` fingerprint), and the stamp changes.

    aseir-stamp compute settings.json
    aseir-stamp verify settings.json 2f8e8943959c
"""
from __future__ import annotations

import sys
import json
import hashlib
import argparse
from typing import Any, Mapping

STAMP_LEN = 12

__all__ = ["canonical", "stamp", "verify", "main"]


def canonical(settings: Mapping[str, Any]) -> bytes:
    """Canonical JSON: sorted keys, compact separators, non-ASCII kept as UTF-8."""
    return json.dumps(settings, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False).encode("utf-8")


def stamp(settings: Mapping[str, Any]) -> str:
    return hashlib.sha256(canonical(settings)).hexdigest()[:STAMP_LEN]


def verify(settings: Mapping[str, Any], expected: str) -> bool:
    return stamp(settings) == expected.strip().lower()


def _load(path: str) -> Mapping[str, Any]:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise SystemExit(f"{path}: settings must be a JSON object")
    return data


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="aseir-stamp", description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("compute", help="print the stamp of a settings file")
    c.add_argument("settings")
    v = sub.add_parser("verify", help="check a settings file against a stamp")
    v.add_argument("settings")
    v.add_argument("stamp")
    args = parser.parse_args(argv)

    settings = _load(args.settings)
    if args.cmd == "compute":
        print(stamp(settings))
        return 0
    actual = stamp(settings)
    if verify(settings, args.stamp):
        print(f"OK  {actual}  settings match the stamp")
        return 0
    print(f"MISMATCH  expected {args.stamp.strip().lower()}  got {actual}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
