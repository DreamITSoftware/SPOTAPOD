#!/usr/bin/env python3
"""
simple_title_aggregate.py

Aggregates how many records' stated occupation/headline text contains a
SIMPLE, generic professional title keyword (e.g. "CEO", "Founder",
"Coach", "Consultant") \u2014 never the verbatim headline/occupation
sentence itself, and never a name or handle. Mutually exclusive
(priority-ordered): each record is assigned to the first matching title
keyword, or "unspecified_other" if none match.

Only podawaa2024.json has no occupation/headline-equivalent field at all,
so it isn't included here. HyperClaper.json's own `jobTitle` field is
almost always empty (1 of 49,369 records) \u2014 the actual signal lives in
`headline`, which is what this script reads instead.

Usage:
    python3 simple_title_aggregate.py hyperclapper /path/to/HyperClaper.json
    python3 simple_title_aggregate.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

# Priority-ordered: a record is tested against these in order and
# assigned to the FIRST matching simple title. Broad seniority titles are
# checked before narrower functional ones so "Founder & Marketing Coach"
# lands under Founder, not Coach \u2014 an arbitrary but fixed rule, stated
# here so results are reproducible.
SIMPLE_TITLES = [
    ("Founder / Co-Founder", [r"\bco-?founder\b", r"\bfounder\b"]),
    ("CEO", [r"\bceo\b", r"\bchief executive\b"]),
    ("President", [r"\bpresident\b"]),
    ("Director", [r"\bdirector\b"]),
    ("VP / Vice President", [r"\bvp\b", r"\bvice president\b"]),
    ("Manager", [r"\bmanager\b"]),
    ("Coach", [r"\bcoach\b"]),
    ("Consultant / Advisor", [r"\bconsultant\b", r"\badvisor\b", r"\badviser\b"]),
    ("Speaker / Trainer", [r"\bspeaker\b", r"\btrainer\b", r"\bkeynote\b"]),
    ("Recruiter", [r"\brecruiter\b", r"\btalent acquisition\b"]),
    ("Engineer / Developer", [r"\bengineer\b", r"\bdeveloper\b"]),
    ("Designer", [r"\bdesigner\b"]),
    ("Analyst", [r"\banalyst\b"]),
    ("Marketer", [r"\bmarketer\b", r"\bmarketing\b"]),
    ("Author / Writer", [r"\bauthor\b", r"\bwriter\b"]),
    ("Owner / Entrepreneur", [r"\bowner\b", r"\bentrepreneur\b"]),
    ("Specialist", [r"\bspecialist\b"]),
]
FALLBACK = "unspecified_other"
COMPILED = [(name, [re.compile(p, re.IGNORECASE) for p in patterns]) for name, patterns in SIMPLE_TITLES]


def classify(text):
    if not text:
        return None  # no occupation text at all -- tracked separately from "unspecified"
    for name, patterns in COMPILED:
        if any(p.search(text) for p in patterns):
            return name
    return FALLBACK


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]
    out = []
    for p in posts:
        ld = (p.get("profile") or {}).get("linkedin_data") or {}
        out.append(ld.get("headline"))
    return out


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)
    return [r.get("Occupation") for r in records]


LOADERS = {"hyperclapper": load_hyperclapper, "linkboost": load_linkboost}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()),
                     help="podawaa2024.json has no occupation/headline field -- not supported")
    ap.add_argument("path")
    args = ap.parse_args()

    texts = LOADERS[args.dataset](args.path)
    n = len(texts)

    counts = Counter()
    no_text = 0
    for t in texts:
        cat = classify(t)
        if cat is None:
            no_text += 1
        else:
            counts[cat] += 1

    print("=" * 60)
    print(f"{args.dataset.upper()} \u2014 SIMPLE TITLE AGGREGATE (no names, no full bios)")
    print("=" * 60)
    print(f"Total records: {n:,}")
    print(f"No occupation/headline text at all: {no_text:,} ({no_text/n*100:.1f}%)")
    print()
    print("Mutually exclusive simple-title counts (a record is assigned to")
    print("the first matching title in priority order):")
    for name, _ in SIMPLE_TITLES:
        c = counts[name]
        print(f"  {name:<26} {c:,} ({c/n*100:.1f}%)")
    c = counts[FALLBACK]
    print(f"  {FALLBACK:<26} {c:,} ({c/n*100:.1f}%)")
    print()
    print("Reminder: this reports title-keyword counts only. No name,")
    print("handle, or verbatim occupation/headline text is printed by")
    print("this script.")


if __name__ == "__main__":
    main()
