"""The Funniest AI Excuse: one-line entry writer.

Writes exactly one line, with no trailing newline, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set,
for local runs). Standard library only; no network, no input.
"""

import os

ENTRY = "I asked a subagent to watch the deadline. It waved goodbye as it left."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one line, no trailing newline.
    assert "\n" not in ENTRY
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
