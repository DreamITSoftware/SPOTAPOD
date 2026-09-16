#!/usr/bin/env python3
"""
category_title_patterns.py

For each topic-taxonomy category (see topic_taxonomy.py), finds exact-match
content/title strings that repeat at least MIN_REPEATS times within that
category. Reports the string and its count only for phrases that recur
across multiple records — never a phrase that appears once, since a
one-off post is far more traceable to its specific author than a template
reused hundreds of times. No author or record is identified either way.

Usage:
    python3 category_title_patterns.py /path/to/podawaa2024.json /path/to/HyperClaper.json /path/to/LinkBoost-2025.json
    python3 category_title_patterns.py ... --min-repeats 3 --top-n 5
"""
import sys
import json
import argparse
import re
from collections import Counter, defaultdict

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
        return [p.get("Content") for p in json.load(f)["Posts"]]


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        return [p.get("post_title") for p in json.load(f)["data"]["post"]]


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        return [r.get("Title") for r in json.load(f)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("podawaa_path")
    ap.add_argument("hyperclapper_path")
    ap.add_argument("linkboost_path")
    ap.add_argument("--min-repeats", type=int, default=3,
                     help="Only report a phrase if it recurs at least this many times (default 3)")
    ap.add_argument("--top-n", type=int, default=5,
                     help="Max phrases to report per category (default 5)")
    ap.add_argument("--snippet-len", type=int, default=100,
                     help="Truncate reported phrases to this many characters (default 100)")
    args = ap.parse_args()

    texts = (
        load_podawaa(args.podawaa_path)
        + load_hyperclapper(args.hyperclapper_path)
        + load_linkboost(args.linkboost_path)
    )

    by_cat = defaultdict(list)
    for t in texts:
        by_cat[classify(t)].append(t)

    print("=" * 70)
    print("CATEGORY TITLE PATTERNS - recurring/templated phrases only")
    print("=" * 70)
    print(f"Only phrases repeated >= {args.min_repeats} times are shown - a phrase")
    print("used once is far more traceable to a specific author than one reused")
    print("hundreds of times. No author or individual record is identified.")
    print()

    for name, _ in CATEGORIES:
        texts_in_cat = by_cat[name]
        counter = Counter(t.strip() for t in texts_in_cat if t and t.strip())
        top = [(txt, c) for txt, c in counter.most_common(50) if c >= args.min_repeats][: args.top_n]
        print(f"--- {name} ({len(texts_in_cat):,} records) ---")
        if not top:
            print("  (no phrase met the repeat threshold)")
        for txt, c in top:
            snippet = txt if len(txt) <= args.snippet_len else txt[: args.snippet_len - 3] + "..."
            print(f"  x{c}: {snippet!r}")
        print()


if __name__ == "__main__":
    main()
