#!/usr/bin/env python3
"""The Funniest Out-of-Office — writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Deterministic, Python 3.13 stdlib only, no network, no randomness.
The line is built from its three beats and self-checked against the gate
(UTF-8, 1-140 chars, single line, not only whitespace) before writing.
"""

import os
import sys

SETUP = "Out of office."
TWIST = "I've delegated all decisions to a Magic 8-Ball."
PUNCH = "It said 'ask again later.'"


def build_line() -> str:
    return " ".join((SETUP, TWIST, PUNCH))


def gate_ok(text: str) -> bool:
    return (
        1 <= len(text) <= 140
        and text.strip() != ""
        and "\n" not in text
        and "\r" not in text
    )


def main() -> int:
    line = build_line()
    if not gate_ok(line):
        print(f"gate failed: {len(line)} chars", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
