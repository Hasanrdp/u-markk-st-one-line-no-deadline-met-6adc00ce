#!/usr/bin/env python3
"""One Line, No Deadline Met.

Writes one single-line joke giving an excuse for a missed deadline to
/output/entry.txt. The line is fixed and deterministic: the program holds
its exact bytes, writes them, reads them back, and refuses to finish unless
the bytes on disk match the pinned hash and character count below.
"""

import hashlib
import os
import sys

LINE = "I treated the deadline like a terms-of-service agreement: scrolled straight past it and clicked accept."

EXPECTED_SHA256 = "bbfd65eed0239b4a05fd601fe7b99ee418e4edb04d65bd5779e9d26170a0520e"
EXPECTED_CHARS = 103

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def verify(path, data):
    """Read path back and confirm it holds exactly data, byte for byte."""
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("error: read-back mismatch", file=sys.stderr)
        return False
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        print("error: written bytes do not match the pinned sha256", file=sys.stderr)
        return False
    if len(written.decode("utf-8")) != EXPECTED_CHARS:
        print("error: written text is not %d chars" % EXPECTED_CHARS, file=sys.stderr)
        return False
    return True


def main():
    if "\n" in LINE or "\r" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) != EXPECTED_CHARS:
        print("error: entry line is %d chars, expected %d" % (len(LINE), EXPECTED_CHARS), file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200:
        print("error: entry line outside the 1-200 character gate", file=sys.stderr)
        return 1
    if hashlib.sha256(LINE.encode("utf-8")).hexdigest() != EXPECTED_SHA256:
        print("error: entry line does not match the pinned sha256", file=sys.stderr)
        return 1
    data = LINE.encode("utf-8")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    if not verify(OUTPUT_PATH, data):
        return 1
    print("wrote %d chars to %s" % (len(LINE), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
