#!/usr/bin/env python3
"""
children_content_scan.py

Counts mentions of children-related terms (child/children, kid/kids,
daughter, toddler, baby/babies, parenting, and a corrected "son" check)
across post content in all three datasets. Same discipline as every
other scan in this repo: aggregate counts only, no record, author, or
matched text ever printed beyond the duplicate-template check below.

IMPORTANT LESSON THIS SCRIPT ENCODES: an earlier draft matched bare
"son"/"sons" case-insensitively, like every other term in this scan.
That pattern also matches "son," the French possessive pronoun meaning
"his/her" (e.g., "elle a pris le controle de son compte" -- "she took
control of her account"), and podawaa2024 contains a meaningful amount
of French-language content (the same underlying fact already documented
in university-content.md's "MIT"/German "mit" collision and this
project's earlier France/Paris finding). The case-insensitive count for
podawaa2024 was 17,573 -- a manual check showed only 1.5% of those
matches (269 records) show a clear English usage pattern referring to
an actual child ("my son," "her son," "son of," "son is," etc.). The
other 98.5% is the French possessive pronoun or otherwise ambiguous.

The fix here is to require "son"/"sons" to appear with a clear English
usage marker (a possessive pronoun or article immediately before it, or
"of/is/was/are/were/who" immediately after) rather than matching the
bare word. This trades some recall (an English sentence structured
unusually would be missed) for a large reduction in false positives.
Every other term in this scan (child, kid, daughter, toddler, baby,
parenting) does not have this problem and is matched case-insensitively
as usual.

Usage:
    python3 children_content_scan.py podawaa /path/to/podawaa2024.json
    python3 children_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 children_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "child / children": r"\bchild(ren)?\b",
    "kid / kids": r"\bkids?\b",
    "daughter": r"\bdaughters?\b",
    "toddler": r"\btoddlers?\b",
    "baby / babies": r"\bbab(y|ies)\b",
    "parenting": r"\bparenting\b",
}
COMPILED = [(name, re.compile(pat, re.IGNORECASE)) for name, pat in TERMS.items()]

# "son" is handled separately and more strictly -- see docstring.
SON_PATTERN = re.compile(
    r"\b(my|his|her|their|our|your|a|the|one)\s+sons?\b|\bsons? (of|is|was|are|were|who)\b",
    re.IGNORECASE,
)


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
        if SON_PATTERN.search(t):
            term_counts["son (clear English usage only)"] += 1
            hit = True
        if hit:
            any_hit += 1
            matching_strings[t.strip()] += 1

    distinct = len(matching_strings)
    top_count = matching_strings.most_common(1)[0][1] if matching_strings else 0
    dominant_share = (top_count / any_hit * 100) if any_hit else 0

    print(f"=== {label} ({n:,} records) ===")
    print(f"Records mentioning any children-related term: {any_hit:,} ({any_hit/n*100:.3f}%)")
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
