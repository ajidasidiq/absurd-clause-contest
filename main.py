#!/usr/bin/env python3
"""Write one absurd terms-of-service clause to /output/entry.txt.

The entry is a single original English sentence of at most 200
characters, phrased as a clause buried deep inside a terms-of-service
agreement: deadpan legal boilerplate that quietly turns absurd. It is
written for the judge's brief: it must read like a real clause until
the absurdity hits, land its joke on one reading with no outside
setup, and carry a concrete absurd image rather than a vague shrug
at the genre.

The joke: the user grants the Company a perpetual, royalty-free
licence to their dreams - and the Company may sublicense the recurring
nightmares to third parties, without further notice. The register
stays pure boilerplate the whole way ("Section 12.4", "hereby grant",
"perpetual, royalty-free licence", "without further notice"), so the
absurdity ambushes the reader instead of announcing itself.
"""

import os
import sys

CLAUSE = (
    "Section 12.4: you hereby grant the Company a perpetual, "
    "royalty-free licence to your dreams, including the right to "
    "sublicense any recurring nightmares to third parties without "
    "further notice."
)

MAX_CHARS = 200


def main() -> int:
    text = CLAUSE.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} limit",
              file=sys.stderr)
        return 1
    if any(ord(ch) < 32 for ch in text):
        print("entry must not contain control characters", file=sys.stderr)
        return 1
    if len(text.splitlines()) != 1:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if CLAUSE != CLAUSE.strip():
        print("entry must not have leading or trailing whitespace",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
