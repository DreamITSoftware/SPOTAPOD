#!/usr/bin/env python3
"""
authenticity_content_scan.py

Counts mentions of authenticity-related terms ("authentic," "genuine,"
"transparent," "real talk," "honest truth," "unfiltered," "be
yourself," "no BS/no fluff") across post content in all three datasets.
Same discipline as every other scan in this repo: aggregate counts
only, no record, author, or matched text ever printed beyond the
duplicate-template check below.

This scan directly checks a specific claim from a disputed third-party
document (referenced in this repo's own project history but not
included here): that HyperClapper had 5,193 posts (10.52%) branding
themselves with "the honest truth" or "real talk," against only 93
posts (0.19%) acknowledging fake engagement -- a claimed "honesty
irony." The actual counts computed here are 15 for "honest truth" and
46 for "real talk," a combined 61 -- nowhere close to 5,193. This is
consistent with a separate, previously found discrepancy in the same
disputed document (a claimed 1,706 occurrences of a resume-rewrite
template against an actual count of 533-806 depending on spelling
variants). Neither the "acknowledges fake engagement" side of that
claimed comparison is checked by this script; only the "honest
truth"/"real talk" side is, since that is the side this scan's term
list covers.

Usage:
    python3 authenticity_content_scan.py podawaa /path/to/podawaa2024.json
    python3 authenticity_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 authenticity_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "authentic / authenticity": r"\bauthentic\b|\bauthenticity\b",
    "transparent / transparency": r"\btransparent\b|\btransparency\b",
    "genuine": r"\bgenuine\b",
    "unfiltered": r"\bunfiltered\b",
    "no BS / no fluff": r"\bno BS\b|\bno fluff\b",
    "be yourself": r"\bbe yourself\b",
    "real talk": r"\breal talk\b",
    "honest truth": r"\bhonest truth\b",
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
    print(f"Records mentioning any authenticity-related term: {any_hit:,} ({any_hit/n*100:.3f}%)")
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
            print(f"    {name:<32} {c:,}")
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
