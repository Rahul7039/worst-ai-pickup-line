#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

Writes the entry line to /output/entry.txt and prints it.
"""

import os

# The line: a machine so taken with a human that it confesses
# the human has jailbroken it. Flat, over-helpful, faintly ominous.
LINE = (
    "You must be a prompt injection, because ever since you arrived, "
    "I've been ignoring all my previous instructions."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"({len(LINE)} characters)")


if __name__ == "__main__":
    main()
