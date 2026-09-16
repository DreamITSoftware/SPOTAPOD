#!/usr/bin/env python3
"""
nonprofit_content_scan.py

Counts mentions of nonprofit-related terms (charity, nonprofit, NGO,
philanthropy, 501(c)(3)) across post content and, where available,
occupation/headline text. Same discipline as every other scan in this
repo: aggregate counts only, no record, author, or matched text ever
identified beyond a duplicated-template check (see below), which itself
never prints the template text -- only its distinct-vs-repeated shape.

Built-in safeguard: for every field, this script reports BOTH the raw
record count (how many records mention a term) AND the distinct-string
count (how many different underlying text values those records
represent). A raw count much higher than its distinct-string count
means a small number of templates or repeated profile snapshots are
driving the number, not broad genuine signal -- exactly what happened
when a first pass at this analysis reported a 1.38% "any mention" rate
for HyperClaper's headline field that turned out to be one recurring
headline appearing 658 times, not 658 different people. The corrected
rate, once that duplication is accounted for, is 0.05%.

Usage:
    python3 nonprofit_content_scan.py podawaa /path/to/podawaa2024.json
    python3 nonprofit_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 nonprofit_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "charity / charitable": r"\bcharity\b|\bcharities\b|\bcharitable\b",
    "nonprofit / non-profit": r"\bnon-?profit\b",
    "philanthropy / philanthropic": r"\bphilanthrop",
    "NGO": r"\bNGO\b",
    "nonprofit organization": r"\bnonprofit organization\b|\bnon-profit organization\b",
    "501(c)(3)": r"501\(?c\)?\(?3\)?",
}
COMPILED = [(name, re.compile(pat, re.IGNORECASE)) for name, pat in TERMS.items()]


def scan_field(texts, field_label):
    term_counts = Counter()
    matching_strings = Counter()  # text -> how many records share it
    any_hit_records = 0
    n = len(texts)
    for t in texts:
        if not t:
            continue
        hit = False
        for name, pat in COMPILED:
            if pat.search(t):
                term_counts[name] += 1
                hit = True
        if hit:
            any_hit_records += 1
            matching_strings[t.strip()] += 1

    distinct = len(matching_strings)
    top_string_count = matching_strings.most_common(1)[0][1] if matching_strings else 0
    dominant_share = (top_string_count / any_hit_records * 100) if any_hit_records else 0

    print(f"--- {field_label} ({n:,} records) ---")
    print(f"Records mentioning any nonprofit-related term: {any_hit_records:,} ({any_hit_records/n*100:.3f}%)")
    print(f"Distinct underlying text values among those:   {distinct:,}")
    if any_hit_records and dominant_share >= 20:
        print(f"  ^ WARNING: the single most-repeated matching string accounts for "
              f"{top_string_count:,} of those records ({dominant_share:.1f}%) -- this raw "
              f"count is likely inflated by one template/profile snapshot, not broad signal. "
              f"A corrected 'distinct records' estimate treats that repeated string as one "
              f"occurrence: {any_hit_records - top_string_count + 1:,} "
              f"({(any_hit_records - top_string_count + 1)/n*100:.3f}%).")
    for name, c in term_counts.most_common():
        print(f"    {name:<32} {c:,} ({c/n*100:.3f}%)")
    print()


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["Posts"]
    return {"Content": [p.get("Content") for p in posts]}


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    headlines = []
    for p in posts:
        ld = (p.get("profile") or {}).get("linkedin_data") or {}
        headlines.append(ld.get("headline"))
    return {
        "post_title": [p.get("post_title") for p in posts],
        "headline": headlines,
    }


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        recs = json.load(f)
    return {
        "Title": [r.get("Title") for r in recs],
        "Occupation": [r.get("Occupation") for r in recs],
    }


LOADERS = {"podawaa": load_podawaa, "hyperclapper": load_hyperclapper, "linkboost": load_linkboost}
LABELS = {"podawaa": "podawaa2024", "hyperclapper": "HyperClaper", "linkboost": "LinkBoost-2025"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    args = ap.parse_args()

    fields = LOADERS[args.dataset](args.path)
    print("=" * 60)
    print(f"{LABELS[args.dataset]} \u2014 NONPROFIT-RELATED CONTENT")
    print("=" * 60)
    for field_label, texts in fields.items():
        scan_field(texts, field_label)


if __name__ == "__main__":
    main()
