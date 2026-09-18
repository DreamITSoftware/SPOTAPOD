#!/usr/bin/env python3
"""
pharma_content_scan.py

Counts mentions of pharma/biotech-related terms across post content in
all three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check below.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py. On this scan it did NOT fire (no single
string crossed the 20% threshold in any dataset) but a manual check was
still needed for LinkBoost-2025, where a low distinct-string-to-match
ratio (28 distinct strings behind 482 matches) turned out to reflect
roughly 8 distinct posts each boosted 29-38 times, not one dominant
template. Checking those posts directly showed they're FDA
import-compliance / customs-regulatory content (Import Alerts, product
refusals and seizures at the border, FOIA requests to the FDA), not
pharmaceutical-industry content -- the FDA mentions there are about
trade compliance, not drug regulation. See
docs/research/pharma-content.md for the full explanation.

Usage:
    python3 pharma_content_scan.py podawaa /path/to/podawaa2024.json
    python3 pharma_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 pharma_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "pharma / pharmaceutical(s)": r"\bpharma\b|\bpharmaceuticals?\b",
    "big pharma": r"\bbig pharma\b",
    "pharma company/companies": r"\bpharma compan(y|ies)\b|\bpharmaceutical compan(y|ies)\b",
    "drug company/companies": r"\bdrug compan(y|ies)\b",
    "pharmaceutical industry": r"\bpharmaceutical industry\b",
    "biotech": r"\bbiotech\b|\bbiotechnology\b",
    "clinical trial(s)": r"\bclinical trials?\b",
    "FDA": r"\bFDA\b",
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
    print(f"Records mentioning any pharma/biotech term: {any_hit:,} ({any_hit/n*100:.4f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}")
    elif any_hit and distinct < any_hit * 0.5:
        print(f"  ^ NOTE: distinct-string count ({distinct:,}) is well below the match count "
              f"({any_hit:,}) without any single string dominating -- likely a small cluster of "
              f"posts each boosted multiple times, not one repeated template. Worth checking the "
              f"actual content before trusting the topic label at face value; see "
              f"docs/research/pharma-content.md for an example where this pattern turned out to be "
              f"FDA import-compliance content, not pharmaceutical-industry content.")
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
