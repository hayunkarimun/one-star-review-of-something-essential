#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes one deadpan one-star review, at most 160 characters, of an
everyday essential everyone relies on, to /output/entry.txt.

The review: sleep. The sharpest true grievance is not that sleep takes
eight hours a night -- it is that it keeps office hours it never agreed
to: it shows up late, and it walks out at 3 a.m. without saying goodbye.
Deadpan throughout, one line, and the turn lands in the last few words.
"""

import os

REVIEW = (
    "One star. Sleep takes eight hours a night, shows up late, "
    "and leaves at 3 a.m. without saying goodbye."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> None:
    text = REVIEW.strip()
    if not text:
        raise SystemExit("refusing to write an empty review")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"review is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if any(ch in text for ch in ("\n", "\r")):
        raise SystemExit("review must be a single line")
    if not any(ch.isalnum() for ch in text):
        raise SystemExit("review must contain more than punctuation")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and confirm the file on disk is exactly the review.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back mismatch: file differs from the review")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
