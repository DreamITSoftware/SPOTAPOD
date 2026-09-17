#!/usr/bin/env python3
"""
career_advice_scan.py

Aggregate, keyword-based scan for career-advice content (resume/CV, job
search, interview prep, promotion, networking, layoffs, personal
branding, etc.) across all three datasets.

Same discipline as regulatory_category_scan.py and book_genre_scan.py:
reports counts and percentages only. No matched text, author, or record
is printed.

Usage:
    python3 career_advice_scan.py podawaa /path/to/podawaa2024.json
    python3 career_advice_scan.py hyperclapper /path/to/HyperClaper.json
    python3 career_advice_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re

CAREER_PATTERNS = [
    r"\bresume\b", r"\bcv\b", r"\bjob search\b", r"\binterview (tips|advice|prep)\b",
    r"\bcareer (advice|change|switch|growth|move)\b", r"\bpromotion\b", r"\bnetworking\b",
    r"\bjob offer\b", r"\bhiring\b", r"\bget hired\b", r"\bland (a|your) (job|role)\b",
    r"\bsalary negotiat", r"\blayoff", r"\blaid off\b", r"\bcover letter\b",
    r"\bpersonal brand(ing)?\b", r"\bLinkedIn (profile|tips)\b",
]
CAREER_RE = [re.compile(p, re.IGNORECASE) for p in CAREER_PATTERNS]


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
    matched = sum(1 for t in texts if t and any(p.search(t) for p in CAREER_RE))

    print("=" * 60)
    print(f"{args.dataset.upper()} — CAREER-ADVICE CONTENT SCAN (aggregate, de-identified)")
    print("=" * 60)
    print(f"Total records scanned: {n:,}")
    print(f"Records matching career-advice language: {matched:,} "
          f"({matched/n*100:.2f}%)")
    print()
    print("Reminder: keyword-pattern SIGNAL, not verified topic classification.")
    print("No record, author, or matched text is identified by this script.")
    if args.dataset == "linkboost":
        print()
        print("Note: LinkBoost-2025.json has 469 unique target posts across")
        print("77,969 records — this percentage measures engagement-pod")
        print("activity VOLUME on career-advice-adjacent posts, not the")
        print("number of distinct career-advice pieces of content.")


if __name__ == "__main__":
    main()
