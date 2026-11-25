#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line entry.

Writes one original funny line to /output/entry.txt (1-200
characters, UTF-8, a single line). Standard library only, no
network, no input.

The line is built from two fragments: a setup (the doorstop's
single job, stated flatly — hold the door open) and a punch
(the twist: it still gets kicked aside every time someone
actually uses the door, so the object fails at the one thing
it exists for, at the hands of the very people it serves).
``assemble`` joins them into the single line; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "Our doorstop has one job \u2014 hold the door open \u2014"
PUNCH = "and still gets kicked aside every time someone actually uses the door."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one funny line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-200 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
