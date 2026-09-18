#!/usr/bin/env python3
"""
political_content_scan.py

Counts mentions of political-party terms and Trump/Biden across post
content in all three datasets. Same discipline as every other scan in
this repo: aggregate counts only, no record, author, or matched text
ever printed beyond the duplicate-template check below.

Includes the duplicate-template safeguard from nonprofit_content_scan.py.
It fired on LinkBoost-2025: 97 of that dataset's "Democrat/Democratic
Party" matches trace to a single repeated post. That post is not new --
it is the same political campaign-endorsement template already
documented in docs/research/decision-points.md (also 97 occurrences,
under the business_entrepreneurship topic category there). Consistent
with this repo's rule against identifying real individuals from the
data, the candidate named in that post is not identified here either.

Usage:
    python3 political_content_scan.py podawaa /path/to/podawaa2024.json
    python3 political_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 political_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "Trump (Donald/President)": r"\bTrump\b",
    "Biden (Joe/President)": r"\bBiden\b",
    "Democrat(s) / Democratic Party": r"\bDemocrats?\b|\bDemocratic Party\b",
    "Republican(s) / GOP": r"\bRepublicans?\b|\bGOP\b",
    "political party (generic)": r"\bpolitical part(y|ies)\b",
    "libertarian": r"\blibertarian\b",
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
    print(f"Any political-term mention: {any_hit:,} ({any_hit/n*100:.4f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}. Candidate/individual "
              f"named in the repeated post is not identified by this script, consistent with this "
              f"repo's privacy rules -- see docs/research/political-content.md.")
    elif any_hit and distinct < any_hit * 0.5:
        print(f"  ^ NOTE: distinct-string count ({distinct:,}) well below match count ({any_hit:,}) "
              f"without one dominant string -- check underlying content before trusting the topic "
              f"label at face value.")
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
