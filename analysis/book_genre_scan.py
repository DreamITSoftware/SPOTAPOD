#!/usr/bin/env python3
"""
book_genre_scan.py

Aggregate, keyword-based scan for book-promotion content ("my new book,"
"pre-order," "bestseller," etc.) across all three datasets, with a
secondary genre breakdown (business, self-help, fiction, etc.) for records
that match.

Same discipline as regulatory_category_scan.py: this reports counts and
percentages only. No matched text, author, or record is printed. A record
can match more than one genre category, or none ("uncategorized").

Usage:
    python3 book_genre_scan.py podawaa /path/to/podawaa2024.json
    python3 book_genre_scan.py hyperclapper /path/to/HyperClaper.json
    python3 book_genre_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

BOOK_PATTERNS = [
    r"\bmy (new )?book\b", r"\bmy first book\b", r"\bpre-?order\b",
    r"\bbook launch\b", r"\bbestseller\b", r"\bgrab (your |a )?copy\b",
    r"\bavailable on amazon\b", r"\bkindle\b",
    r"\bpublish(ed|ing)? my book\b", r"\bwrote a book\b", r"\bco-author",
    r"\baudiobook\b", r"\bbook signing\b", r"\bISBN\b",
]
BOOK_RE = [re.compile(p, re.IGNORECASE) for p in BOOK_PATTERNS]

GENRE_PATTERNS = {
    "business_entrepreneurship": [r"\bbusiness\b", r"\bentrepreneur", r"\bstartup\b", r"\bleadership\b", r"\bfounder\b"],
    "self_help_personal_dev": [r"\bself.?help\b", r"\bmindset\b", r"\bmotivat", r"\bpersonal (growth|development)\b", r"\bhabits?\b"],
    "career_sales_marketing": [r"\bcareer\b", r"\bsales\b", r"\bmarketing\b", r"\bpersonal brand"],
    "finance_investing": [r"\bfinanc", r"\binvest", r"\bmoney\b", r"\bwealth\b", r"\bretirement\b"],
    "health_wellness_fitness": [r"\bhealth\b", r"\bwellness\b", r"\bfitness\b", r"\bnutrition\b", r"\bmental health\b"],
    "memoir_biography": [r"\bmemoir\b", r"\bautobiograph", r"\bbiograph", r"\bmy (journey|story)\b"],
    "fiction_novel": [r"\bnovel\b", r"\bfiction\b", r"\bthriller\b", r"\bromance\b", r"\bsci-?fi\b"],
    "childrens_book": [r"\bchildren'?s book\b", r"\bkids book\b", r"\bpicture book\b"],
    "poetry": [r"\bpoetry\b", r"\bpoems?\b"],
    "spiritual_religious": [r"\bspiritual", r"\bfaith\b", r"\bchristian\b", r"\bgod\b", r"\bmindfulness\b"],
    "technology_ai": [r"\btechnology\b", r"\bAI\b", r"\bartificial intelligence\b", r"\bsoftware\b"],
    "parenting_relationships": [r"\bparenting\b", r"\brelationship", r"\bmarriage\b", r"\bfamily\b"],
    "writing_craft": [r"\bwriting\b", r"\bauthor(ing)?\b", r"\bmanuscript\b", r"\bpublishing\b"],
}
GENRE_RE = {g: [re.compile(p, re.IGNORECASE) for p in pats] for g, pats in GENRE_PATTERNS.items()}


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["Posts"]
    return [p.get("Content") for p in posts], len(posts)


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    return [p.get("post_title") for p in posts], len(posts)


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    return [r.get("Title") for r in records], len(records)


LOADERS = {"podawaa": load_podawaa, "hyperclapper": load_hyperclapper, "linkboost": load_linkboost}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    args = ap.parse_args()

    texts, n = LOADERS[args.dataset](args.path)
    matched = [t for t in texts if t and any(p.search(t) for p in BOOK_RE)]

    print("=" * 60)
    print(f"{args.dataset.upper()} — BOOK-PROMOTION GENRE SCAN (aggregate, de-identified)")
    print("=" * 60)
    print(f"Total records scanned: {n:,}")
    print(f"Records matching book-promotion language: {len(matched):,} "
          f"({len(matched)/n*100:.2f}%)")
    print()

    if not matched:
        return

    genre_counts = Counter()
    uncategorized = 0
    for t in matched:
        hit = False
        for g, patterns in GENRE_RE.items():
            if any(p.search(t) for p in patterns):
                genre_counts[g] += 1
                hit = True
        if not hit:
            uncategorized += 1

    print("Genre breakdown (of book-promotion records; a record can match")
    print("more than one genre, so percentages don't sum to 100%):")
    for g in GENRE_PATTERNS:
        c = genre_counts[g]
        if c:
            print(f"  {g:<28} {c:,} ({c/len(matched)*100:.1f}%)")
    print(f"  {'uncategorized':<28} {uncategorized:,} ({uncategorized/len(matched)*100:.1f}%)")
    print()
    print("Reminder: keyword-pattern SIGNALS, not verified genre classification.")
    print("No record, author, or matched text is identified by this script.")


if __name__ == "__main__":
    main()
