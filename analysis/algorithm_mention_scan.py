#!/usr/bin/env python3
"""
algorithm_mention_scan.py

Counts mentions of "algorithm" and LinkedIn-algorithm-specific phrasing
across post content in all three datasets. Same discipline as every
other scan in this repo: aggregate counts only, no record, author, or
matched text ever printed beyond the duplicate-template check below.

This scan is directly relevant to this project's own subject matter --
see docs/research/algorithm-strategy-advice.md, which documents the
broader genre of algorithm-strategy-advice content this scan measures
the raw prevalence of. LinkBoost-2025's top repeated posts include
content specifically about gaming or understanding the LinkedIn
algorithm, directly on-theme for the datasets this whole repo analyzes.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py, plus the low-distinct-ratio check from
pharma_content_scan.py. Neither fires a genuine warning on this scan --
LinkBoost-2025's lower distinct-string ratio was checked manually (top
repeated string is under 10% of matches) and reflects genuinely
distinct, on-topic posts, not a new artifact.

Usage:
    python3 algorithm_mention_scan.py podawaa /path/to/podawaa2024.json
    python3 algorithm_mention_scan.py hyperclapper /path/to/HyperClaper.json
    python3 algorithm_mention_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "algorithm (generic, any platform)": r"\balgorithm\b",
    "LinkedIn algorithm (specific)": r"\bLinkedIn(\'s)? algorithm\b",
    "algorithm change/update": r"\balgorithm (change|update|changes|updates)\b",
    "algorithm favors/rewards": r"\balgorithm (favors?|rewards?|loves?|hates?|penalizes?)\b",
    "beat the algorithm": r"\bbeat the algorithm\b",
    "game the algorithm": r"\bgame the algorithm\b",
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
    print(f"Records mentioning any algorithm term: {any_hit:,} ({any_hit/n*100:.3f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}")
    elif any_hit and distinct < any_hit * 0.5:
        print(f"  ^ NOTE: distinct-string count ({distinct:,}) is below the match count "
              f"({any_hit:,}) without one string dominating -- worth a manual check if this "
              f"pattern is unexpected for the dataset.")
    for name, c in term_counts.most_common():
        if c:
            print(f"    {name:<36} {c:,}")
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
