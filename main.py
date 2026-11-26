"""Write one lost-sock status update to /output/entry.txt.

Stdlib only. Deterministic: the same line, byte for byte, every run.
The kit gate requires 1-120 UTF-8 characters, not only whitespace.
"""

import os

LINE = (
    "Day 12 inside the dog's bed. He thinks I'm his. "
    "I've stopped correcting him \u2014 turns out the cuddles are elite."
)

MAX_CHARS = 120


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, limit {MAX_CHARS}"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be exactly one line"
    out = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    # Read back and re-check the gate on what was actually written.
    with open(out, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written output differs from LINE"
    assert 1 <= len(written.rstrip("\n")) <= MAX_CHARS


if __name__ == "__main__":
    main()
