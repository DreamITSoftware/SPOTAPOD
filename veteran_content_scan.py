#!/usr/bin/env python3
"""
veteran_content_scan.py

Counts mentions of veteran- and military-related terms across post
content in all three datasets. Same discipline as every other scan in
this repo: aggregate counts only, no record, author, or matched text
ever printed beyond the duplicate-template check below. No individual
is identified by name in this script's output or its documentation.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py. It fires on LinkBoost-2025: 97 of 476
matches trace to the same repeated political campaign-endorsement post
already documented (without naming the candidate) in
docs/research/decision-points.md and docs/research/political-content.md
-- that post describes the candidate as a "decorated 20-year veteran
and combat aviator," which is why it surfaces here too. The remaining
LinkBoost-2025 matches are genuine, distinct content: real tributes to
Indian Armed Forces personnel, not an artifact.

Bare "VA" is deliberately excluded from this scan (unlike some other
terms in this repo) because it collides too readily with the state
abbreviation for Virginia and other unrelated two-letter uses; only
"Veterans Affairs," "VA benefits," "VA loan," and "VA disability" are
checked, which all require enough surrounding context to be reliable.

Usage:
    python3 veteran_content_scan.py podawaa /path/to/podawaa2024.json
    python3 veteran_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 veteran_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "veteran(s)": r"\bveterans?\b",
    "military veteran": r"\bmilitary veterans?\b",
    "veteran-owned": r"\bveteran-owned\b",
    "disabled veteran": r"\bdisabled veterans?\b",
    "combat veteran": r"\bcombat veterans?\b",
    "armed forces": r"\barmed forces\b",
    "service member(s)": r"\bservice members?\b|\bservicemembers?\b",
    "Veterans Affairs / VA benefits": r"\bVeterans Affairs\b|\bVA benefits\b|\bVA loan\b|\bVA disability\b",
    "ex-military": r"\bex-military\b",
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
    print(f"Records mentioning any veteran/military term: {any_hit:,} ({any_hit/n*100:.3f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}. This is the same "
              f"repeated political-endorsement post documented (without naming the candidate) in "
              f"docs/research/decision-points.md and docs/research/political-content.md.")
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
