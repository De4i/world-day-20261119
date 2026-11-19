#!/usr/bin/env python3
"""Entry point for make.fun's news-image-20261119 bounty.

The repository carries the final 1024x1024 image as ``entry.png``, rendered
ahead of time from ``poster/poster.html`` (see BUILD.md).  This program is a
deterministic publisher: it validates the baked image against the bounty's
file gate -- PNG magic bytes, at most 1 MiB, exactly 1024x1024 pixels from
the IHDR header, and a trailing IEND chunk -- and copies it byte for byte
to ``$MAKEFUN_OUTPUT_DIR/entry.png``.  Two runs therefore write identical
bytes, which is exactly what the grader's determinism check re-runs.

Standard library only, as the sandbox requires.
"""

import os
import shutil
import struct
import sys

MAX_BYTES = 1_048_576          # the bounty's 1 MiB cap
MAX_DIM = 1024                # the bounty's pixel cap (square)
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def read_header(path):
    """Return (width, height) from the PNG IHDR chunk, or raise ValueError."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != PNG_SIGNATURE:
        raise ValueError("entry.png does not start with the PNG signature")
    if head[12:16] != b"IHDR":
        raise ValueError("first PNG chunk is not IHDR")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def validate(path):
    """Return an error string, or None when the image satisfies the gate."""
    size = os.path.getsize(path)
    if size > MAX_BYTES:
        return "entry.png is %d bytes, over the %d-byte cap" % (size, MAX_BYTES)
    width, height = read_header(path)
    if width != MAX_DIM or height != MAX_DIM:
        return "entry.png is %dx%d, not %dx%d" % (width, height, MAX_DIM, MAX_DIM)
    with open(path, "rb") as fh:
        fh.seek(-8, os.SEEK_END)
        trailer = fh.read(8)
    if trailer[0:4] != b"IEND":
        return "entry.png does not end with an IEND chunk"
    return None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.exists(source):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1

    problem = validate(source)
    if problem:
        print(problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)

    size = os.path.getsize(target)
    print("OK entry.png 1024x1024 %d bytes -> %s" % (size, target))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
