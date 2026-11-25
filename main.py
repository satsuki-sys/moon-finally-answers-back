#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes one original line, in the voice of the Moon replying at last to
the wishes, howls and late-night promises of everyone staring up at it,
to /output/entry.txt. The line is kept in a single constant so the output
is exactly one line, inside the 240-character limit.
"""

import os

LINE = (
    "You wish on me, howl at me, and swear you'll change tomorrow. "
    "Four billion years of it, and nobody has once asked how I'm doing. "
    "I'm fine. The tides are still on. "
    "Your basement, Kevin — that was your idea, not mine."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE.strip()
    assert 1 <= len(line) <= 240, f"line is {len(line)} chars"
    assert "\n" not in line, "line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
