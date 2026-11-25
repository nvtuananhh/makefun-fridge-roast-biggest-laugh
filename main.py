"""Fridge Roast: One Line, Biggest Laugh — final entry.

Writes a single-line roast of a smart fridge to entry.txt.
Standard library only, no network, deterministic.
"""

import os

ENTRY = "My smart fridge films my snacks, updates its firmware, and shames my milk \u2014 yet its ice maker is still 'coming soon.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
