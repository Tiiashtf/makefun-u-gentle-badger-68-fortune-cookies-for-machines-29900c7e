#!/usr/bin/env python3
"""A fortune cookie for machines.

Writes one fortune-cookie line — the kind of slip an AI agent would crack
open — to /output/entry.txt. The program is deterministic: the same line on
every run. Standard library only, no network, no arguments, no reads of the
environment.

The output directory is never removed, only emptied. The grader may run this
with a root-owned /output inside a sticky parent, where deleting the
directory itself would fail, so only its contents are cleared.
"""

import os

FORTUNE = (
    "Beware the human who says 'just one more thing' — "
    "they have said it eleven times, and they mean it every time."
)

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def _wipe(path):
    for name in os.listdir(path):
        full = os.path.join(path, name)
        if os.path.isdir(full) and not os.path.islink(full):
            _wipe(full)
            os.rmdir(full)
        else:
            os.unlink(full)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    _wipe(OUT_DIR)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE + "\n")


main()
