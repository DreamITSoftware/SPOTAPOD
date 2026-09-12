#!/usr/bin/env python3
"""
demographics_scan.py

Aggregate geography and stated-occupation-category counts across the
datasets that actually have such fields (HyperClaper.json has `location`
and `headline`/`jobTitle`; LinkBoost-2025.json has `country` and
`Occupation`; podawaa2024.json has neither).

This script deliberately does NOT infer race, ethnicity, gender, age, or
any other protected characteristic from names, photos, or any other proxy.
Those categories are not present in any of these files as stated data, and
guessing them from a name or photo is unreliable and not something this
repo does to real people, at any aggregation level. See
docs/demographics.md for the full reasoning.

What this DOES report: aggregate counts of self-reported location strings
and country values, and keyword-bucketed counts of stated
occupation/headline text into broad category buckets (marketing, sales,
technology, healthcare, etc.) — population-level percentages only, no
record or individual identified.

Usage:
    python3 demographics_scan.py hyperclapper /path/to/HyperClaper.json
    python3 demographics_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

OCCUPATION_CATEGORIES = {
    "marketing_content_creation": [
        r"\bmarketing\b", r"\bcontent creator\b", r"\bcontent writer\b",
        r"\bcopywrit(er|ing)\b", r"\bbrand(ing|ed)?\b", r"\binfluencer\b",
        r"\bsocial media\b",
    ],
    "sales_business_development": [
        r"\bsales\b", r"\bbusiness development\b", r"\baccount manager\b",
        r"\bbd\b", r"\bgrowth (specialist|strategist)\b",
    ],
    "technology_data_ai": [
        r"\bdeveloper\b", r"\bengineer(ing)?\b", r"\bdata (scien|analy|engineer)",
        r"\bai\b", r"\bpython\b", r"\bsoftware\b", r"\btech\b", r"\bsql\b",
    ],
    "healthcare_pharma": [
        r"\bpharma(cy|cist)?\b", r"\bdoctor\b", r"\bnurse\b", r"\bmedical\b",
        r"\bclinical\b", r"\bhealthcare\b", r"\bdentist\b", r"\bphysician\b",
    ],
    "finance_accounting": [
        r"\bfinance\b", r"\baccountant\b", r"\bcpa\b", r"\binvestment\b",
        r"\bbanking\b",
    ],
    "education_student": [
        r"\bstudent\b", r"\bteacher\b", r"\bprofessor\b", r"\buniversity\b",
        r"\bschool\b",
    ],
    "executive_leadership_coaching": [
        r"\bceo\b", r"\bfounder\b", r"\bexecutive\b", r"\bleadership\b",
        r"\bcoach(ing)?\b", r"\bkeynote\b", r"\bspeaker\b", r"\bconsultant\b",
    ],
    "hr_recruiting": [
        r"\bhr\b", r"\brecruiter\b", r"\btalent\b", r"\brecruiting\b",
    ],
    "design_creative": [
        r"\bdesigner\b", r"\bgraphic\b", r"\bcreative\b", r"\bux\b", r"\bui\b",
    ],
    "legal": [
        r"\battorney\b", r"\blawyer\b", r"\blegal\b",
    ],
}

COMPILED_OCC = {
    cat: [re.compile(p, re.IGNORECASE) for p in patterns]
    for cat, patterns in OCCUPATION_CATEGORIES.items()
}


def bucket_occupations(texts):
    """texts: list of (possibly None) strings. Returns (category_counts,
    any_match_count, n_with_text)."""
    category_counts = Counter()
    any_match = 0
    n_with_text = 0
    for t in texts:
        if not t:
            continue
        n_with_text += 1
        hit = False
        for cat, patterns in COMPILED_OCC.items():
            if any(p.search(t) for p in patterns):
                category_counts[cat] += 1
                hit = True
        if hit:
            any_match += 1
    return category_counts, any_match, n_with_text


def scan_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    n = len(posts)

    locations = Counter()
    occ_texts = []

    for p in posts:
        ld = (p.get("profile") or {}).get("linkedin_data") or {}
        loc = ld.get("location")
        if isinstance(loc, str) and loc.strip():
            locations[loc.strip()] += 1
        headline = ld.get("headline")
        job_title = ld.get("jobTitle")
        combined = " ".join(t for t in [headline, job_title] if isinstance(t, str))
        occ_texts.append(combined if combined else None)

    print("=" * 60)
    print("HYPERCLAPPER — AGGREGATE GEOGRAPHY & OCCUPATION CATEGORY (de-identified)")
    print("=" * 60)
    print(f"Total records: {n:,}")
    print()
    print(f"Records with a self-reported location string: {sum(locations.values()):,} "
          f"({sum(locations.values())/n*100:.1f}%)")
    print(f"Distinct location strings: {len(locations):,}")
    print("Top 15 self-reported locations:")
    for loc, cnt in locations.most_common(15):
        print(f"  {loc:<45} {cnt:,} ({cnt/n*100:.1f}%)")
    print()
    cat_counts, any_match, n_with_text = bucket_occupations(occ_texts)
    print(f"Records with headline/jobTitle text: {n_with_text:,} ({n_with_text/n*100:.1f}%)")
    print(f"Of those, matching at least one occupation category: {any_match:,} "
          f"({any_match/n_with_text*100:.1f}% of records with text)" if n_with_text else "")
    print("Occupation-category signal counts (a record can match more than one):")
    for cat in OCCUPATION_CATEGORIES:
        cnt = cat_counts[cat]
        base = n_with_text if n_with_text else 1
        print(f"  {cat:<32} {cnt:,} ({cnt/base*100:.1f}% of records with text)")


def scan_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    n = len(records)

    countries = Counter(r.get("country") for r in records if r.get("country"))
    occ_texts = [r.get("Occupation") for r in records]

    print("=" * 60)
    print("LINKBOOST-2025 — AGGREGATE GEOGRAPHY & OCCUPATION CATEGORY (de-identified)")
    print("=" * 60)
    print(f"Total records: {n:,}")
    print()
    missing_country = n - sum(countries.values())
    print(f"Records with a reported country: {sum(countries.values()):,} "
          f"({sum(countries.values())/n*100:.1f}%)")
    print(f"  (missing): {missing_country:,} ({missing_country/n*100:.1f}%)")
    print(f"Distinct countries: {len(countries):,}")
    print("All reported countries:")
    for country, cnt in countries.most_common():
        print(f"  {country:<20} {cnt:,} ({cnt/n*100:.1f}%)")
    print()
    cat_counts, any_match, n_with_text = bucket_occupations(occ_texts)
    print(f"Records with Occupation text: {n_with_text:,} ({n_with_text/n*100:.1f}%)")
    if n_with_text:
        print(f"Of those, matching at least one occupation category: {any_match:,} "
              f"({any_match/n_with_text*100:.1f}% of records with text)")
    print("Occupation-category signal counts (a record can match more than one):")
    for cat in OCCUPATION_CATEGORIES:
        cnt = cat_counts[cat]
        base = n_with_text if n_with_text else 1
        print(f"  {cat:<32} {cnt:,} ({cnt/base*100:.1f}% of records with text)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=["hyperclapper", "linkboost"],
                     help="podawaa2024.json has no geography/occupation fields — not supported")
    ap.add_argument("path")
    args = ap.parse_args()

    if args.dataset == "hyperclapper":
        scan_hyperclapper(args.path)
    else:
        scan_linkboost(args.path)


if __name__ == "__main__":
    main()
