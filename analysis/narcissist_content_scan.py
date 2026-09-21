#!/usr/bin/env python3
"""
narcissist_content_scan.py

Counts mentions of narcissist/narcissistic/narcissism across post
content in all three datasets. Same discipline as every other scan in
this repo: aggregate counts only, no record, author, or matched text
ever printed beyond the duplicate-template check below.

This is the smallest content category documented in this repo so far.
Only 156 total records across all 340,829 combined records mention
narcissism in any form, before the LinkBoost-2025 correction below is
even applied.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py. It fires on LinkBoost-2025: 52 of 116
matches trace to a single personal recovery/psychedelic-journey post
("free from the NARCISSISTS spider web"), boosted by the platform's
structure. Checked directly, this is genuine content, not a false
positive -- the same pattern as the genuine-but-duplicated findings in
homelessness-content.md and diabetes-content.md, unlike the outright
false positives in immunotherapy-content.md, university-content.md, and
children-content.md.

Usage:
    python3 narcissist_content_scan.py podawaa /path/to/podawaa2024.json
    python3 narcissist_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 narcissist_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "narcissist(s)": r"\bnarcissists?\b",
    "narcissistic": r"\bnarcissistic\b",
    "narcissism": r"\bnarcissism\b",
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
    print(f"Records mentioning any narcissist-related term: {any_hit:,} ({any_hit/n*100:.4f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ NOTE: top repeated string = {top_count:,} records ({dominant_share:.1f}%). "
              f"Corrected estimate: {corrected:,}. Checking the underlying text is recommended "
              f"before assuming this is noise -- it may be genuine content boosted by the "
              f"platform's structure rather than a false positive; see "
              f"docs/research/narcissist-content.md for this scan's specific finding.")
    for name, c in term_counts.most_common():
        if c:
            print(f"    {name:<20} {c:,}")
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
