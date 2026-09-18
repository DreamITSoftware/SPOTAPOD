#!/usr/bin/env python3
"""
regulatory_category_scan.py

Aggregate, keyword-based signal counts for content categories that
intersect with laws OTHER than 16 CFR § 465.8 — run across the text
fields (post/comment content and stated occupation) of any of the three
datasets in this repo.

This is deliberately blunt: a keyword hit is a SIGNAL, not a finding. It
tells you "N records contain terms associated with category X," and
nothing more. It does not identify which records, which authors, or
whether any actual legal element (falsity, materiality, licensing status,
jurisdiction, intent) is present. See docs/research/other-regulatory-signals.md for
the evidence-tier discipline this script's output is meant to be read
under.

Deliberately does NOT print, store, or export any name, handle, URN,
profile link, or the matched text itself — only aggregate counts per
category, per file. No script in this repo can be used to find out which
specific record(s) tripped a category.

Usage:
    python3 regulatory_category_scan.py podawaa /path/to/podawaa2024.json
    python3 regulatory_category_scan.py hyperclapper /path/to/HyperClaper.json
    python3 regulatory_category_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

# Each category is a light keyword/phrase set, matched case-insensitively
# as whole-word/phrase substrings. These are intentionally broad and will
# over-match casual/figurative language (e.g. "guaranteed to make you
# smile") — that's why this is a SIGNAL count, not a violation count.
CATEGORIES = {
    "health_medical_claims": [
        r"\bcure[sd]?\b", r"\btreat(s|ment|ing)?\b", r"\bdiagnos(e|is|ed)\b",
        r"\bdetox\b", r"\breverse (your |the )?(disease|diabetes|aging)\b",
        r"\bguaranteed weight loss\b", r"\blose \d+\s*(lbs|pounds|kg)\b",
        r"\bmiracle (cure|pill|fix)\b", r"\bFDA[- ]approved\b",
        r"\bclinically proven\b",
    ],
    "financial_investment_claims": [
        r"\bguaranteed return[s]?\b", r"\brisk[- ]free investment\b",
        r"\bdouble your (money|income)\b", r"\bpassive income\b",
        r"\bcrypto(currency)? (opportunity|investment)\b",
        r"\bfinancial advisor\b", r"\bregistered investment\b",
        r"\bact now\b.{0,20}\blimited (time|spots)\b",
    ],
    "professional_licensing_language": [
        r"\bI(?:'m| am) a (licensed )?(doctor|physician|attorney|lawyer|cpa|accountant|therapist|psychologist)\b",
        r"\bmedical advice\b", r"\blegal advice\b", r"\btax advice\b",
        r"\bboard[- ]certified\b",
    ],
    "endorsement_disclosure_gap": [
        r"\bpartner(ed)? with\b", r"\bsponsored\b", r"\bad\b(?!\w)",
        r"\baffiliate link\b", r"\bcode\s+\w+\s+for\s+\d+%\s*off\b",
    ],
}

COMPILED = {
    cat: [re.compile(p, re.IGNORECASE) for p in patterns]
    for cat, patterns in CATEGORIES.items()
}


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["Posts"]
    return [{"text_fields": [p.get("Content")]} for p in posts]


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    out = []
    for p in posts:
        headline = ((p.get("profile") or {}).get("linkedin_data") or {}).get("headline")
        out.append({"text_fields": [p.get("post_title"), headline]})
    return out


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    return [{"text_fields": [r.get("Title"), r.get("Comment"), r.get("Occupation")]}
            for r in records]


LOADERS = {
    "podawaa": load_podawaa,
    "hyperclapper": load_hyperclapper,
    "linkboost": load_linkboost,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    args = ap.parse_args()

    records = LOADERS[args.dataset](args.path)
    n = len(records)

    category_counts = Counter()
    any_category_count = 0

    for rec in records:
        text = " ".join(t for t in rec["text_fields"] if t)
        if not text:
            continue
        hit_any = False
        for cat, patterns in COMPILED.items():
            if any(p.search(text) for p in patterns):
                category_counts[cat] += 1
                hit_any = True
        if hit_any:
            any_category_count += 1

    print("=" * 60)
    print(f"{args.dataset.upper()} — REGULATORY-CATEGORY SIGNAL SCAN (aggregate, de-identified)")
    print("=" * 60)
    print(f"Total records scanned: {n:,}")
    print(f"Records matching at least one category: {any_category_count:,} "
          f"({any_category_count/n*100:.2f}%)")
    print()
    print("Category signal counts (a record can match more than one):")
    for cat in CATEGORIES:
        cnt = category_counts[cat]
        print(f"  {cat:<32} {cnt:,} ({cnt/n*100:.2f}%)")
    print()
    print("Reminder: these are keyword-pattern SIGNALS, not findings. No")
    print("record, author, or occupation is identified by this script, and")
    print("no legal conclusion follows from a match. See")
    print("docs/research/other-regulatory-signals.md.")


if __name__ == "__main__":
    main()
