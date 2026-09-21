#!/usr/bin/env python3
"""
university_content_scan.py

Counts mentions of university-related terms across post content in all
three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check below.

IMPORTANT LESSON THIS SCRIPT ENCODES: an earlier draft matched "MIT"
case-insensitively, which also caught the German preposition "mit"
(meaning "with") -- podawaa2024 contains a meaningful amount of
German-language content, and this single collision inflated that
dataset's "MIT" count from a genuine 148 to a false 2,601, a roughly
94% false-positive rate that briefly made "MIT" look like the single
largest university-related term in that dataset, ahead of the generic
word "university" itself. That inconsistency (one dataset's top term
not matching the other two) is what prompted a manual check. The fix:
"MIT" is matched case-sensitively here (no re.IGNORECASE), since the
German word is always written lowercase and the university acronym is
always written in caps. This is the same class of lesson as the "cart"/
CAR-T collision documented in immunotherapy-content.md and the "TIME"
magazine pattern documented in entity-mentions.md -- a short,
common-looking token needs either a qualifying phrase or a case
constraint, not just a word boundary, before it can be trusted.

Usage:
    python3 university_content_scan.py podawaa /path/to/podawaa2024.json
    python3 university_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 university_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

MIT_STRICT = re.compile(r"\bMIT\b")  # deliberately case-sensitive; see docstring
OTHER_TERMS = {
    "university/universities": re.compile(r"\buniversit(y|ies)\b", re.IGNORECASE),
    "college(s)": re.compile(r"\bcolleges?\b", re.IGNORECASE),
    "Harvard": re.compile(r"\bHarvard\b", re.IGNORECASE),
    "Stanford": re.compile(r"\bStanford\b", re.IGNORECASE),
    "Oxford": re.compile(r"\bOxford\b", re.IGNORECASE),
    "Cambridge": re.compile(r"\bCambridge\b", re.IGNORECASE),
    "Yale": re.compile(r"\bYale\b", re.IGNORECASE),
    "Princeton": re.compile(r"\bPrinceton\b", re.IGNORECASE),
    "Berkeley": re.compile(r"\bBerkeley\b", re.IGNORECASE),
    "Ivy League": re.compile(r"\bIvy League\b", re.IGNORECASE),
}


def scan(texts, label, n):
    term_counts = Counter()
    matching_strings = Counter()
    any_hit = 0
    for t in texts:
        if not t:
            continue
        hit = False
        if MIT_STRICT.search(t):
            term_counts["MIT (strict, case-sensitive)"] += 1
            hit = True
        for name, pat in OTHER_TERMS.items():
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
    print(f"Records mentioning any university-related term: {any_hit:,} ({any_hit/n*100:.3f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}")
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
