#!/usr/bin/env python3
"""
career_advice_reciprocal_crosstab.py

Row-level cross-tab, HyperClapper only: does career-advice-matching content
show a different reciprocal-engagement rate (like AND comment both true on
the same record) than the rest of the same file.

This exists because the dataset-wide comparison in
docs/research/career-advice-comparison.md (highest career-advice content
rate, highest reciprocal-engagement rate, and highest leadership-coaching
occupation skew all landing on the same file) only establishes that those
three numbers move together ACROSS the file as a whole. It does not, on
its own, establish that the specific posts matching career-advice language
are the same posts driving the reciprocal-engagement rate. This script
answers that narrower, harder question directly, within a single file,
so the two rates being compared come from the same population under the
same collection conditions.

Same discipline as career_advice_scan.py: aggregate counts and percentages
only. No record, author, or matched text is ever printed or stored.

The like/comment/impression fields profiled here are "indicators of
social media influence" as defined at 16 CFR Section 465.1(j), governed by
16 CFR Section 465.8 (see ../docs/regulatory-context.md). This script makes
no legal determination about any record.

Multiple exports of HyperClapper-style data exist with different file
hashes (see checksums/CHECKSUMS.txt for the canonical one, filed there
as "HyperClaper.json"). Always confirm the input file's SHA-256 against
that entry before treating this script's output as the project's
published figure; a mismatched file has, in practice, produced identical
counts on this specific check, but that should never be assumed without
checking the hash first.

Usage:
    python3 career_advice_reciprocal_crosstab.py /path/to/HyperClapper.json
"""
import sys
import json
import argparse
import hashlib
import re

CAREER_PATTERNS = [
    r"\bresume\b", r"\bcv\b", r"\bjob search\b", r"\binterview (tips|advice|prep)\b",
    r"\bcareer (advice|change|switch|growth|move)\b", r"\bpromotion\b", r"\bnetworking\b",
    r"\bjob offer\b", r"\bhiring\b", r"\bget hired\b", r"\bland (a|your) (job|role)\b",
    r"\bsalary negotiat", r"\blayoff", r"\blaid off\b", r"\bcover letter\b",
    r"\bpersonal brand(ing)?\b", r"\bLinkedIn (profile|tips)\b",
]
CAREER_RE = [re.compile(p, re.IGNORECASE) for p in CAREER_PATTERNS]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path", help="Path to a HyperClapper-style export")
    args = ap.parse_args()

    print(f"Input file SHA-256: {sha256_of(args.path)}")
    print("Compare against checksums/CHECKSUMS.txt before citing this output.")
    print()

    with open(args.path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]

    n = len(posts)
    career_total = career_reciprocal = 0
    other_total = other_reciprocal = 0

    for p in posts:
        title = p.get("post_title") or ""
        is_career = bool(title) and any(pat.search(title) for pat in CAREER_RE)
        reciprocal = bool(p.get("like")) and bool(p.get("comment"))
        if is_career:
            career_total += 1
            career_reciprocal += int(reciprocal)
        else:
            other_total += 1
            other_reciprocal += int(reciprocal)

    print("=" * 70)
    print("HYPERCLAPPER: CAREER-ADVICE vs NON-CAREER RECIPROCAL-ENGAGEMENT RATE")
    print("=" * 70)
    print(f"Total records: {n:,}")
    print()
    career_pct = career_reciprocal / career_total * 100 if career_total else 0.0
    other_pct = other_reciprocal / other_total * 100 if other_total else 0.0
    print(f"Career-advice-matching records: {career_total:,} ({career_total/n*100:.2f}%)")
    print(f"  reciprocal (like AND comment): {career_reciprocal:,} ({career_pct:.2f}% of career-matching)")
    print()
    print(f"Non-career records: {other_total:,} ({other_total/n*100:.2f}%)")
    print(f"  reciprocal (like AND comment): {other_reciprocal:,} ({other_pct:.2f}% of non-career)")
    print()
    print(f"Difference in reciprocal-engagement rate (career minus non-career): "
          f"{career_pct - other_pct:+.2f} percentage points")
    print()
    print("Reminder: keyword-pattern SIGNAL, not verified topic classification.")
    print("No record, author, or matched text is identified by this script.")


if __name__ == "__main__":
    main()
