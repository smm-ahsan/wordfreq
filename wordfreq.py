#!/usr/bin/env python3
"""WordFreq - word frequency and keyword density for writers and SEO.

Counts words in a text (or a text file), ranks them by frequency and
shows each word's keyword density as a percentage of the total.
Standard library only.
"""

import argparse
import sys
from collections import Counter
import re

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on",
    "for", "with", "is", "are", "was", "were", "be", "been", "it",
    "its", "this", "that", "these", "those", "you", "your", "we",
    "our", "they", "their", "he", "she", "his", "her", "as", "at",
    "by", "from", "not", "no", "do", "does", "have", "has",
}

WORD_RE = re.compile(r"[a-z0-9']+")


def tokenise(text, min_length):
    """Lowercase the text, extract words, strip stray apostrophes."""
    words = []
    for raw in WORD_RE.findall(text.lower()):
        word = raw.strip("'")
        if word and len(word) >= min_length:
            words.append(word)
    return words


def main():
    parser = argparse.ArgumentParser(
        description="Count word frequency and keyword density in a text."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text", help="Text to analyse, in quotes.")
    group.add_argument("--file", help="Path to a text file to analyse.")
    parser.add_argument(
        "--top", type=int, default=10,
        help="How many top words to show (default 10).",
    )
    parser.add_argument(
        "--min-length", type=int, default=1,
        help="Ignore words shorter than this (default 1).",
    )
    parser.add_argument(
        "--stopwords", action="store_true",
        help="Exclude common English stopwords (the, and, of, ...).",
    )
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as handle:
                text = handle.read()
        except OSError as exc:
            parser.error("cannot read --file: %s" % exc)
    else:
        text = args.text

    words = tokenise(text, args.min_length)
    if args.stopwords:
        words = [w for w in words if w not in STOPWORDS]

    total = len(words)
    counts = Counter(words)

    print("Total words: %d" % total)
    print("Unique words: %d" % len(counts))
    if total == 0:
        return 0

    # Rank by count descending; ties broken alphabetically.
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    for rank, (word, count) in enumerate(ranked[: args.top], start=1):
        density = count / total * 100
        print("%d. %s - %d (%.1f%%)" % (rank, word, count, density))
    return 0


if __name__ == "__main__":
    sys.exit(main())
