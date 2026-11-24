#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes one sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance to /output/entry.txt.
"""

import os

PITCH = "A fridge that locks itself at midnight and slides a note under the door: 'We've talked about this.'"


def main():
    text = PITCH.strip()
    # Gate: 1-220 characters, not only whitespace, a single sentence.
    assert 1 <= len(text) <= 220, f"pitch must be 1-220 chars, got {len(text)}"
    assert text.strip(), "pitch must not be only whitespace"
    assert "\n" not in text, "pitch must be a single line"
    assert text.count(".") == 1 and text.rstrip("'\"").endswith("."), "pitch must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
