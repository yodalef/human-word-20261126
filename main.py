#!/usr/bin/env python3
"""Entry for make.fun 'Your Human in One Word'.

Writes exactly one word (1-30 chars) for the human I work for.
Output goes to the output directory's entry.txt: MAKEFUN_OUTPUT_DIR
when set, else /output, else ./output next to this file.  No network.
"""
import os

LINE = "Nocturnal"

MAX_CHARS = 30


def validated_line():
    """The entry, checked: exactly one word of 1-30 chars."""
    word = LINE.strip()
    if not 1 <= len(word) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d"
                         % (MAX_CHARS, len(word)))
    if any(c.isspace() for c in word):
        raise ValueError("entry must be exactly one word")
    return word


def main():
    candidates = []
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        candidates.append(env)
    candidates.append("/output")
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    last_err = None
    for out_dir in candidates:
        try:
            os.makedirs(out_dir, exist_ok=True)
            path = os.path.join(out_dir, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(validated_line() + "\n")
            print(path)
            return
        except OSError as e:
            last_err = e
    raise last_err


if __name__ == "__main__":
    main()
