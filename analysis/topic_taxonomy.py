#!/usr/bin/env python3
"""
topic_taxonomy.py

Assigns every record across all three datasets to exactly ONE of nine
mutually exclusive content categories (priority-ordered pattern match:
first matching category wins), then reports aggregate counts per
category, per dataset. Same discipline as every other analysis script in
this repo: outputs counts and percentages only. No record, author, or
matched text is printed or returned.

Usage:
    python3 topic_taxonomy.py /path/to/podawaa2024.json /path/to/HyperClaper.json /path/to/LinkBoost-2025.json
    python3 topic_taxonomy.py ... --json   # machine-readable output
"""
import sys
import json
import argparse
import re
from collections import Counter, defaultdict

# Priority-ordered: a record is tested against categories in this order
# and assigned to the FIRST one that matches, so categories are mutually
# exclusive by construction (no record is double-counted).
CATEGORIES = [
    ("career_job_search", [
        r"\bresume\b", r"\bcv\b", r"\bjob search\b", r"\binterview (tips|advice|prep)\b",
        r"\bhiring\b", r"\bget hired\b", r"\bjob offer\b", r"\blaid off\b", r"\blayoff",
        r"\bcover letter\b", r"\bland (a|your) (job|role)\b",
    ]),
    ("book_writing_publishing", [
        r"\bmy (new )?book\b", r"\bpre-?order\b", r"\bbook launch\b", r"\bbestseller\b",
        r"\bwrote a book\b", r"\bpublish(ed|ing)? my book\b", r"\bmanuscript\b", r"\bco-author",
    ]),
    ("education_certification", [
        r"\bcertificat(e|ion)\b", r"\bfree course\b", r"\benroll(ed|ment)?\b", r"\breskill\b",
        r"\bupskill\b", r"\blearning path\b",
    ]),
    ("technology_ai", [
        r"\btechnology\b", r"\bartificial intelligence\b", r"\bchatgpt\b", r"\bopenai\b",
        r"\banthropic\b", r"\bclaude\b", r"\bsoftware\b", r"\bmachine learning\b", r"\bAI\b",
    ]),
    ("finance_investing", [
        r"\bfinanc", r"\binvest", r"\bwealth\b", r"\bretirement\b", r"\bmoney\b",
    ]),
    ("health_wellness_fitness", [
        r"\bhealth\b", r"\bwellness\b", r"\bfitness\b", r"\bnutrition\b", r"\bmental health\b",
    ]),
    ("leadership_coaching_motivation", [
        r"\bleadership\b", r"\bcoach(ing)?\b", r"\bmindset\b", r"\bmotivat", r"\bkeynote\b",
        r"\bspeaker\b",
    ]),
    ("marketing_sales_branding", [
        r"\bmarketing\b", r"\bsales\b", r"\bpersonal brand", r"\bsocial media\b",
        r"\bcontent creator\b", r"\bcopywrit",
    ]),
    ("business_entrepreneurship", [
        r"\bbusiness\b", r"\bentrepreneur", r"\bstartup\b", r"\bfounder\b",
    ]),
]
# Anything matching none of the above falls into this catch-all, so every
# record is assigned to exactly one category and coverage is complete.
FALLBACK = "uncategorized_other"

COMPILED = [(name, [re.compile(p, re.IGNORECASE) for p in patterns]) for name, patterns in CATEGORIES]


def classify(text):
    if not text:
        return FALLBACK
    for name, patterns in COMPILED:
        if any(p.search(text) for p in patterns):
            return name
    return FALLBACK


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["Posts"]
    return [p.get("Content") for p in posts]


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    return [p.get("post_title") for p in posts]


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    return [r.get("Title") for r in records]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("podawaa_path")
    ap.add_argument("hyperclapper_path")
    ap.add_argument("linkboost_path")
    ap.add_argument("--json", action="store_true", help="print machine-readable JSON instead of a text report")
    args = ap.parse_args()

    datasets = {
        "podawaa2024": load_podawaa(args.podawaa_path),
        "HyperClaper": load_hyperclapper(args.hyperclapper_path),
        "LinkBoost-2025": load_linkboost(args.linkboost_path),
    }

    all_category_names = [name for name, _ in CATEGORIES] + [FALLBACK]
    totals = Counter()
    by_dataset = {name: Counter() for name in all_category_names}
    dataset_sizes = {}

    for ds_name, texts in datasets.items():
        dataset_sizes[ds_name] = len(texts)
        for t in texts:
            cat = classify(t)
            totals[cat] += 1
            by_dataset[cat][ds_name] += 1

    grand_total = sum(dataset_sizes.values())

    if args.json:
        result = {}
        for cat in all_category_names:
            result[cat] = {
                "total_count": totals[cat],
                "total_pct": round(totals[cat] / grand_total * 100, 2),
                "by_dataset": {
                    ds: {
                        "count": by_dataset[cat][ds],
                        "pct_of_dataset": round(by_dataset[cat][ds] / dataset_sizes[ds] * 100, 2),
                    }
                    for ds in datasets
                },
            }
        meta = {
            "dataset_sizes": dataset_sizes,
            "grand_total_records": grand_total,
            "method": "priority-ordered keyword pattern match; each record assigned to exactly one category (first match wins); no record, author, or matched text is included in this output",
            "categories_in_priority_order": all_category_names,
        }
        print(json.dumps({"meta": meta, "categories": result}, indent=2))
        return

    print("=" * 70)
    print("TOPIC TAXONOMY - mutually exclusive categorization (aggregate only)")
    print("=" * 70)
    print(f"Dataset sizes: " + ", ".join(f"{k}={v:,}" for k, v in dataset_sizes.items()))
    print(f"Grand total records: {grand_total:,}")
    print()
    for cat in all_category_names:
        pct = totals[cat] / grand_total * 100
        print(f"{cat:<32} {totals[cat]:>7,}  ({pct:5.2f}% of all records)")
        for ds in datasets:
            c = by_dataset[cat][ds]
            p = c / dataset_sizes[ds] * 100
            print(f"    {ds:<20} {c:>7,}  ({p:5.2f}% of {ds})")
    print()
    print("Reminder: keyword-pattern SIGNALS, not verified topic labels. No")
    print("record, author, or matched text is identified by this script.")


if __name__ == "__main__":
    main()
