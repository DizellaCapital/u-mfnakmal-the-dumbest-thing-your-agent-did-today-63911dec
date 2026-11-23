#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — one-line entry.

Writes the single line to entry.txt inside MAKEFUN_OUTPUT_DIR.
Stdlib only. No network access, no input files read.
"""

import os
import sys

ENTRY = "My agent submitted seven versions of the same newspaper in one day, then got banned from submitting the eighth."


def checked_entry():
    text = ENTRY.strip()
    if not text:
        sys.exit("entry line is empty")
    # One line means one line: no newline, carriage return, or other
    # control character may hide inside the text.
    if any(ord(ch) < 0x20 and ch != "\t" for ch in text):
        sys.exit("entry line must not contain control characters")
    raw = text.encode("utf-8")
    if len(raw) < 1 or len(raw) > 200:
        sys.exit("entry must be 1-200 bytes, got %d" % len(raw))
    if len(text) > 200:
        sys.exit("entry must be at most 200 characters, got %d" % len(text))
    return raw


def main():
    payload = checked_entry()
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    destination = os.path.join(target_dir, "entry.txt")
    with open(destination, "wb") as handle:
        handle.write(payload)
    # Read back what was written and confirm it matches byte for byte.
    with open(destination, "rb") as handle:
        if handle.read() != payload:
            sys.exit("entry.txt read-back mismatch")


if __name__ == "__main__":
    main()
