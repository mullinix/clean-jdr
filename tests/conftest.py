"""Resuable testing fixtures for clean-jdr."""

import os
import random

WORDS = "the quick brown fox jumped over the lazy dog".split(" ")
OTHER = "+ - * = ? : . , ".split(" ")
NUMERALS = "0 1 2 3 4 5 6 7 8 9".split(" ")


def random_paragraph() -> bytes:
    """Generates a paragraph with random bytes entertwined."""
    lines = b""
    # make 10 lines
    for _ in range(10):
        words = b""
        # make 10 "words" per line
        for _ in range(10):
            num_words = random.choice(range(len(WORDS)))
            text = random.choices(WORDS, k=num_words)
            others = random.choices(OTHER, k=num_words)
            numbers = random.choices(NUMERALS, k=num_words)
            bytes_ = os.urandom(num_words)
            byte_arry = (
                [t.encode("latin-1") for t in text]
                + [o.encode("latin-1") for o in others]
                + [n.encode("latin-1") for n in numbers]
                + [bytes([b]) for b in bytes_]
            )
            random.shuffle(byte_arry)
            words += b"".join(byte_arry)
        lines += words + "\n".encode("latin-1")
    return lines


if __name__ == "__main__":
    print(random_paragraph())
