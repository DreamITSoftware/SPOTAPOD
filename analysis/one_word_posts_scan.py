#!/usr/bin/env python3
"""
one_word_posts_scan.py

Finds posts whose content consists of a single whitespace-delimited
token (e.g. "Agree?", a single emoji, a bare URL) across all three
datasets. Same discipline as every other scan in this repo: reports
counts only. Consistent with the rest of this repo's approach to
recurring content (see decision-points.md, category_title_patterns.py),
only one-word strings that repeat at least 3 times are ever printed --
a genuinely one-off single-word post is never surfaced, since a unique
short post is far more traceable to its specific author than one reused
across many records.

A post is counted as "one word" if, after stripping leading/trailing
whitespace, splitting on whitespace produces exactly one token. This
counts "Agree?" (punctuation attached, no internal space) as one word,
which matches the intuitive, colloquial sense of "one-word post" this
scan is answering.

Usage:
    python3 one_word_posts_scan.py podawaa /path/to/podawaa2024.json
    python3 one_word_posts_scan.py hyperclapper /path/to/HyperClaper.json
    python3 one_word_posts_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
from collections import Counter

MIN_REPEATS = 3


def scan(texts, label, n):
    counter = Counter()
    total_one_word = 0
    for t in texts:
        if not t:
            continue
        stripped = t.strip()
        if not stripped:
            continue
        tokens = stripped.split()
        if len(tokens) == 1:
            total_one_word += 1
            counter[stripped] += 1

    distinct = len(counter)
    print(f"=== {label} ({n:,} records) ===")
    print(f"One-word posts: {total_one_word:,} ({total_one_word/n*100:.3f}%)")
    print(f"Distinct one-word strings: {distinct:,}")
    print(f"Top repeated one-word posts (>= {MIN_REPEATS} occurrences):")
    shown = [(w, c) for w, c in counter.most_common(50) if c >= MIN_REPEATS]
    if not shown:
        print("  (none met the repeat threshold)")
    for word, c in shown:
        print(f"  x{c}: {word!r}")
    print()


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        return [p.get("Content") for p in json.load(f)["Posts"]]


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        return [p.get("post_title") for p in json.load(f)["data"]["post"]]


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        return [r.get("Title") for r in json.load(f)]


LOADERS = {"podawaa": load_podawaa, "hyperclapper": load_hyperclapper, "linkboost": load_linkboost}
LABELS = {"podawaa": "podawaa2024", "hyperclapper": "HyperClapper", "linkboost": "LinkBoost-2025"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    args = ap.parse_args()
    texts = LOADERS[args.dataset](args.path)
    scan(texts, LABELS[args.dataset], len(texts))


if __name__ == "__main__":
    main()
