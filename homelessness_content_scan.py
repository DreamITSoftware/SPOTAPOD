#!/usr/bin/env python3
"""
homelessness_content_scan.py

Counts mentions of homelessness-related terms across post content in
all three datasets, at two levels of breadth (narrow vs. broad, same
approach as law_content_scan.py), plus the duplicate-template safeguard
introduced in nonprofit_content_scan.py. Same discipline as every other
scan in this repo: aggregate counts only, no record, author, or matched
text ever printed beyond the duplicate-template check.

NARROW: homeless/homelessness, unhoused, homeless shelter, housing
insecurity, homeless services/agency.

BROAD: narrow + affordable housing + the bare word "shelter". Bare
"shelter" is included only in the broad tally because checking actual
matches showed it catches real noise -- a disaster-protection product
post ("a spherical shelter designed to protect against natural
disasters"), unrelated leadership content, and other clearly
off-topic uses. The narrow tally is the more trustworthy number for
most purposes.

Usage:
    python3 homelessness_content_scan.py podawaa /path/to/podawaa2024.json
    python3 homelessness_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 homelessness_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

NARROW = re.compile(
    r"\bhomeless(ness)?\b|\bunhoused\b|\bhomeless shelter\b|\bhousing insecurity\b|"
    r"\bhomeless services\b|\bhomeless agenc(y|ies)\b",
    re.IGNORECASE,
)
BROAD_ADD = re.compile(r"\baffordable housing\b|\bshelter\b", re.IGNORECASE)


def scan(texts, label, n):
    narrow_matches = Counter()
    narrow_any = 0
    broad_any = 0
    for t in texts:
        if not t:
            continue
        if NARROW.search(t):
            narrow_any += 1
            narrow_matches[t.strip()] += 1
        if NARROW.search(t) or BROAD_ADD.search(t):
            broad_any += 1

    distinct = len(narrow_matches)
    top_count = narrow_matches.most_common(1)[0][1] if narrow_matches else 0
    dominant_share = (top_count / narrow_any * 100) if narrow_any else 0

    print(f"=== {label} ({n:,} records) ===")
    print(f"NARROW (homeless/homelessness, unhoused, housing insecurity, homeless services): "
          f"{narrow_any:,} ({narrow_any/n*100:.4f}%)")
    print(f"  Distinct underlying text values: {distinct:,}")
    if narrow_any and dominant_share >= 20:
        corrected = narrow_any - top_count + 1
        print(f"  ^ NOTE: top repeated string = {top_count:,} records ({dominant_share:.1f}%). "
              f"Corrected estimate: {corrected:,}. (This does not necessarily mean noise -- "
              f"check the underlying text; see docs/research/homelessness-content.md for an "
              f"example where the repeated string was genuine on-topic content.)")
    print(f"BROAD (narrow + affordable housing + bare \"shelter\", noisier): "
          f"{broad_any:,} ({broad_any/n*100:.4f}%)")
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
