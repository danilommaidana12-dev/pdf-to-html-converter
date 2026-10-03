from __future__ import annotations

import argparse
from pathlib import Path

from book_converter.cli import build_parser, run_command


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return run_command(args)


if __name__ == "__main__":
    raise SystemExit(main())
