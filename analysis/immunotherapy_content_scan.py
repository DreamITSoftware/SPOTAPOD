#!/usr/bin/env python3
"""
immunotherapy_content_scan.py

Counts mentions of immunotherapy-related terms across post content in
all three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check below.

IMPORTANT LESSON THIS SCRIPT ENCODES: an earlier draft of this scan
used the pattern r"\bCAR-?T\b" for "CAR-T" (a real cell-therapy term),
with the hyphen made optional to also catch "CAR T" as two words. That
pattern, case-insensitive, also matches the common word "cart" --
shopping cart, price comparisons, abandoned-cart marketing content --
and completely dominated the raw counts with pure noise: 107, 60, and
58 false-positive matches in podawaa2024, HyperClaper, and
LinkBoost-2025 respectively, none of which were about cell therapy.
Sampling the matches directly (posts about online shopping, Shopify,
subscriptions, grocery habits) made this obvious immediately. The
pattern below requires "CAR-T" to appear with "cell" or "therapy"
nearby, which eliminates the false positives at the cost of missing a
bare "CAR-T" mention with no qualifying word next to it -- an
acceptable trade given how much noise the unqualified pattern produced.
This is the same class of lesson as the "TIME" magazine pattern
documented in entity-mentions.md, but caught before it ever reached a
committed script rather than after.

Usage:
    python3 immunotherapy_content_scan.py podawaa /path/to/podawaa2024.json
    python3 immunotherapy_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 immunotherapy_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "immunotherapy": r"\bimmunotherap(y|ies)\b",
    "immuno-oncology": r"\bimmuno-?oncology\b",
    "checkpoint inhibitor": r"\bcheckpoint inhibitors?\b",
    "CAR-T (cell therapy, strict)": r"\bCAR-T\s?(cell|therapy)\b",
    "monoclonal antibody/antibodies": r"\bmonoclonal antibod(y|ies)\b",
    "cancer immunotherapy": r"\bcancer immunotherapy\b",
}
COMPILED = [(name, re.compile(pat, re.IGNORECASE)) for name, pat in TERMS.items()]


def scan(texts, label, n):
    term_counts = Counter()
    matching_strings = Counter()
    any_hit = 0
    for t in texts:
        if not t:
            continue
        hit = False
        for name, pat in COMPILED:
            if pat.search(t):
                term_counts[name] += 1
                hit = True
        if hit:
            any_hit += 1
            matching_strings[t.strip()] += 1

    distinct = len(matching_strings)
    top_count = matching_strings.most_common(1)[0][1] if matching_strings else 0
    dominant_share = (top_count / any_hit * 100) if any_hit else 0

    print(f"=== {label} ({n:,} records) ===")
    print(f"Records mentioning any immunotherapy-related term: {any_hit:,} ({any_hit/n*100:.5f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation or an off-topic post using the term in passing. "
              f"Check the underlying content before trusting this number; see "
              f"docs/research/immunotherapy-content.md for an example where this exact pattern "
              f"turned out to be a single unrelated business post, not medical content.")
    for name, c in term_counts.most_common():
        if c:
            print(f"    {name:<34} {c:,}")
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
LABELS = {"podawaa": "podawaa2024", "hyperclapper": "HyperClaper", "linkboost": "LinkBoost-2025"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    args = ap.parse_args()
    texts = LOADERS[args.dataset](args.path)
    scan(texts, LABELS[args.dataset], len(texts))


if __name__ == "__main__":
    main()
