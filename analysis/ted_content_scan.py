#!/usr/bin/env python3
"""
ted_content_scan.py

Counts mentions of TED/TEDx-related content across post content in all
three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check below.

IMPORTANT DESIGN NOTE: bare "TED" is a real collision risk, since it is
also a common first name (Ted, short for Theodore/Edward). This script
matches bare "TED" case-SENSITIVELY (all-caps only), unlike every other
term-based scan in this repo, which matches case-insensitively.
Personal names are essentially never written in all-caps prose, so this
substantially reduces (though does not perfectly eliminate) the
collision risk, at the cost of missing any all-caps sentence that
happens to contain someone's name "TED" -- an acceptable trade given
how much more common the personal name is than an emphasized personal
name. "TEDx" and "TED Talk(s)" are unambiguous phrases and are matched
case-insensitively as usual.

Usage:
    python3 ted_content_scan.py podawaa /path/to/podawaa2024.json
    python3 ted_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 ted_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TEDX_PAT = re.compile(r"\bTEDx\b", re.IGNORECASE)
TEDTALK_PAT = re.compile(r"\bTED [Tt]alks?\b", re.IGNORECASE)
TED_STRICT = re.compile(r"\bTED\b")  # deliberately case-sensitive, see docstring


def scan(texts, label, n):
    term_counts = Counter()
    matching_strings = Counter()
    any_hit = 0
    for t in texts:
        if not t:
            continue
        hit = False
        if TEDX_PAT.search(t):
            term_counts["TEDx"] += 1
            hit = True
        if TEDTALK_PAT.search(t):
            term_counts["TED Talk(s)"] += 1
            hit = True
        if TED_STRICT.search(t):
            term_counts["TED (strict, all-caps)"] += 1
            hit = True
        if hit:
            any_hit += 1
            matching_strings[t.strip()] += 1

    distinct = len(matching_strings)
    top_count = matching_strings.most_common(1)[0][1] if matching_strings else 0
    dominant_share = (top_count / any_hit * 100) if any_hit else 0

    print(f"=== {label} ({n:,} records) ===")
    print(f"Records mentioning any TED/TEDx term: {any_hit:,} ({any_hit/n*100:.4f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}")
    elif any_hit and distinct < any_hit * 0.5:
        print(f"  ^ NOTE: distinct-string count ({distinct:,}) is below the match count "
              f"({any_hit:,}) without one string dominating -- worth a manual check.")
    for name in ["TEDx", "TED Talk(s)", "TED (strict, all-caps)"]:
        print(f"    {name:<24} {term_counts.get(name, 0):,}")
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
