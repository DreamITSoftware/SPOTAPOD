#!/usr/bin/env python3
"""
being_human_scan.py

Counts mentions of "being human" / humanity-related terms (being
human, human touch, human connection, humanity, human element, human
side, humanness) across post content in all three datasets. Same
discipline as every other scan in this repo: aggregate counts only, no
record, author, or matched text ever printed beyond the
duplicate-template check below.

Bare "human" is deliberately excluded from this scan's term list --
it collides too broadly with unrelated usage ("human resources,"
"human capital," AI-vs-human comparisons) to be a reliable signal for
the specific "being human" theme this scan targets. Only the more
specific phrases above are checked.

Usage:
    python3 being_human_scan.py podawaa /path/to/podawaa2024.json
    python3 being_human_scan.py hyperclapper /path/to/HyperClaper.json
    python3 being_human_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "being human": r"\bbeing human\b",
    "human touch": r"\bhuman touch\b",
    "human connection": r"\bhuman connections?\b",
    "humanity": r"\bhumanity\b",
    "human element": r"\bhuman element\b",
    "human side": r"\bhuman side\b",
    "humanness": r"\bhumanness\b",
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
    print(f"Records mentioning any 'being human' term: {any_hit:,} ({any_hit/n*100:.4f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}")
    elif any_hit and distinct < any_hit * 0.5:
        print(f"  ^ NOTE: distinct-string count ({distinct:,}) is below the match count "
              f"({any_hit:,}) without one string dominating -- worth a manual check.")
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
