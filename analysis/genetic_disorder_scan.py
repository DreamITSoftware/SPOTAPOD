#!/usr/bin/env python3
"""
genetic_disorder_scan.py

Counts mentions of genetic-disorder-related terms (genetic disorder(s),
genetic condition(s), genetic disease(s), genetic mutation(s),
hereditary disease/condition, inherited disorder(s), Down syndrome,
cystic fibrosis, sickle cell) across post content in all three
datasets. Same discipline as every other scan in this repo: aggregate
counts only, no record, author, or matched text ever printed beyond the
duplicate-template check below.

This is a health-adjacent, sensitive topic. Every match reported here
is purely a keyword hit in public post text. No claim is made or
implied about any specific individual's actual health status, genetic
makeup, or diagnosis -- this script measures how often terms appear in
text, nothing more.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py. It fires on LinkBoost-2025: all 46 "genetic
condition(s)" matches trace to a single post (excerpting a Cathie Wood
interview discussing AI and genomics in healthcare, naming "rare
genetic conditions" alongside cancer and chronic illness), boosted by
the platform's structure. This is genuine, substantive content, not a
false positive -- but it is one post, not 46 distinct mentions.

Usage:
    python3 genetic_disorder_scan.py podawaa /path/to/podawaa2024.json
    python3 genetic_disorder_scan.py hyperclapper /path/to/HyperClaper.json
    python3 genetic_disorder_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "genetic disorder(s)": r"\bgenetic disorders?\b",
    "genetic condition(s)": r"\bgenetic conditions?\b",
    "genetic disease(s)": r"\bgenetic diseases?\b",
    "genetic mutation(s)": r"\bgenetic mutations?\b",
    "hereditary disease/condition": r"\bhereditary (disease|condition)s?\b",
    "inherited disorder(s)": r"\binherited disorders?\b",
    "Down syndrome": r"\bDown syndrome\b",
    "cystic fibrosis": r"\bcystic fibrosis\b",
    "sickle cell": r"\bsickle cell\b",
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
    print(f"Records mentioning any genetic-disorder term: {any_hit:,} ({any_hit/n*100:.5f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20 and any_hit > 1:
        corrected = any_hit - top_count + 1
        print(f"  ^ NOTE: top repeated string = {top_count:,} records ({dominant_share:.1f}%). "
              f"Corrected estimate: {corrected:,}. Checking the underlying text is recommended "
              f"before assuming this is noise or genuine broad signal; see "
              f"docs/research/genetic-disorder-content.md for this scan's specific finding.")
    for name, c in term_counts.most_common():
        if c:
            print(f"    {name:<30} {c:,}")
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
