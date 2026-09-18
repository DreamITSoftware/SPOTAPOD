#!/usr/bin/env python3
"""
diabetes_content_scan.py

Counts mentions of diabetes-related terms (diabetes, diabetic, type 1/2
diabetes, insulin, blood sugar, glucose monitoring, prediabetes) across
post content in all three datasets. Same discipline as every other
scan in this repo: aggregate counts only, no record, author, or matched
text ever printed beyond the duplicate-template check below.

This is one of the smallest genuine content categories found in this
project, comparable in scale to national-security and immunotherapy
content (both documented elsewhere in this repo), all under 0.25% of
any dataset.

Includes the same duplicate-template safeguard introduced in
nonprofit_content_scan.py. It fires on LinkBoost-2025: 40 of 172
matches trace to a single post about sugar consumption and blood sugar
impact, boosted by the platform's structure. Checked directly, this is
genuine health/nutrition content, not a false positive -- similar in
kind to the genuine-but-duplicated findings in
homelessness-content.md and veteran-content.md, unlike the outright
false positives documented in immunotherapy-content.md and
university-content.md.

Usage:
    python3 diabetes_content_scan.py podawaa /path/to/podawaa2024.json
    python3 diabetes_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 diabetes_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "diabetes": r"\bdiabetes\b",
    "diabetic": r"\bdiabetics?\b",
    "type 1 diabetes": r"\btype\s?1 diabetes\b|\bT1D\b",
    "type 2 diabetes": r"\btype\s?2 diabetes\b|\bT2D\b",
    "insulin": r"\binsulin\b",
    "blood sugar": r"\bblood sugar\b",
    "glucose monitoring": r"\bglucose monitor(ing)?\b|\bcontinuous glucose\b",
    "prediabetes": r"\bprediabetes\b|\bpre-diabetes\b",
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
    print(f"Records mentioning any diabetes-related term: {any_hit:,} ({any_hit/n*100:.4f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ NOTE: top repeated string = {top_count:,} records ({dominant_share:.1f}%). "
              f"Corrected estimate: {corrected:,}. Checking the underlying text is recommended "
              f"before assuming this is noise -- it may be genuine content boosted by the "
              f"platform's structure rather than a false positive; see "
              f"docs/research/diabetes-content.md for this scan's specific finding.")
    for name, c in term_counts.most_common():
        if c:
            print(f"    {name:<24} {c:,}")
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
