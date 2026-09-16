#!/usr/bin/env python3
"""
national_security_scan.py

Counts mentions of national-security-related terms (national security,
NSA, CIA, FBI, intelligence agency, homeland security, classified
information, national defense) across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond the
duplicate-template check below.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py: reports distinct underlying text values
alongside every raw count, and flags any field where a single repeated
string accounts for 20% or more of the matching records. This caught a
real one on first run: LinkBoost-2025's "FBI" count of 15 turned out to
be one boosted news-commentary post about an unrelated financial-fraud
case (the Jordan Belfort/Wolf of Wall Street story), not 15 distinct
posts about the FBI.

Usage:
    python3 national_security_scan.py podawaa /path/to/podawaa2024.json
    python3 national_security_scan.py hyperclapper /path/to/HyperClaper.json
    python3 national_security_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "national security": r"\bnational security\b",
    "NSA": r"\bNSA\b",
    "CIA": r"\bCIA\b",
    "FBI": r"\bFBI\b",
    "intelligence agency / agencies": r"\bintelligence agenc(y|ies)\b",
    "homeland security": r"\bhomeland security\b",
    "classified information": r"\bclassified information\b",
    "national defense": r"\bnational defense\b",
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
    print(f"Records mentioning any national-security term: {any_hit:,} ({any_hit/n*100:.4f}%)")
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
