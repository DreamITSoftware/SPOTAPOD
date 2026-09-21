#!/usr/bin/env python3
"""
rare_earth_metals_scan.py

Counts mentions of rare earth metals/elements and adjacent critical-
minerals terms (lithium, cobalt, critical minerals, neodymium) across
post content in all three datasets. Same discipline as every other
scan in this repo: aggregate counts only, no record, author, or
matched text ever printed beyond the duplicate-template check below.

Note on scope: lithium and cobalt are not technically rare earth
elements (they are battery/EV-supply-chain minerals commonly discussed
alongside rare earths in the same policy/industry conversations), but
are included here because they account for the overwhelming majority
of matches -- the specific phrase "rare earth metals/elements" appears
only 7 times total across all three datasets combined.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py. It fires on LinkBoost-2025: 53 of 71 matches
trace to a single e-waste/battery-recycling industry post (about an
Indian recycling company), boosted by the platform's structure. Checked
directly, this is genuine content, not a false positive.

Usage:
    python3 rare_earth_metals_scan.py podawaa /path/to/podawaa2024.json
    python3 rare_earth_metals_scan.py hyperclapper /path/to/HyperClaper.json
    python3 rare_earth_metals_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "rare earth metals/elements/earths": r"\brare earth (metals?|elements?|earths?)\b|\brare earths\b",
    "neodymium": r"\bneodymium\b",
    "lithium": r"\blithium\b",
    "cobalt": r"\bcobalt\b",
    "critical minerals": r"\bcritical minerals?\b",
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
    print(f"Records mentioning any rare-earth/critical-minerals term: {any_hit:,} ({any_hit/n*100:.5f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ NOTE: top repeated string = {top_count:,} records ({dominant_share:.1f}%). "
              f"Corrected estimate: {corrected:,}. Check the underlying text before assuming "
              f"noise -- see docs/research/rare-earth-metals-content.md for this scan's finding.")
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
