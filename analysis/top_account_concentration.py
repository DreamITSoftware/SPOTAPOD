#!/usr/bin/env python3
"""
top_account_concentration.py

Computes what share of a dataset's posts come from its most active
authors -- the top 20 and top 100 accounts by post count -- using the
same "percent of posts with an identified author" denominator this
repo's own baseline-profile.md uses for its top 1%/5%/10% figures.

This script directly checks a specific claim from a disputed third-party
document (referenced in this repo's own project history but not
included here): that HyperClapper's "top 20 accounts produce 50.6%...
top 100 produce 87.3%" of all posts. Run against this repo's own copy
of HyperClapper, the actual figures are 36.2% (top 20) and 83.5% (top
100) of posts with an identified author -- both lower than claimed.
This is consistent with two other, previously documented discrepancies
in the same disputed document (see docs/research/authenticity-content.md
and docs/research/decision-points.md): the document's specific
statistics do not hold up against direct verification against the
source files.

Deliberately does NOT print, store, or export any author name, profile
identifier, URL, or post content. Author identifiers are hashed
in-memory, used only to count posts-per-author, and discarded; no
per-author value is ever printed, only the aggregate top-20/top-100
totals.

Input schema expected (top level): {"data": {"post": [{"profile":
{"linkedin_data": {"public_identifier": ...}}}, ...]}}

Usage:
    python3 top_account_concentration.py /path/to/HyperClaper.json
"""
import sys
import json
import hashlib
from collections import Counter


def anon_id(identifier: str) -> str:
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 top_account_concentration.py /path/to/HyperClaper.json")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        posts = json.load(f)["data"]["post"]

    n_total = len(posts)
    author_counts = Counter()
    missing = 0
    for p in posts:
        prof = p.get("profile") or {}
        ld = prof.get("linkedin_data") or {}
        pid = ld.get("public_identifier")
        if pid:
            author_counts[anon_id(pid)] += 1
        else:
            missing += 1

    n_authors = len(author_counts)
    n_attributed = n_total - missing
    ranked = [c for _, c in author_counts.most_common()]

    top20 = sum(ranked[:20])
    top100 = sum(ranked[:100])

    print("=" * 70)
    print("TOP-ACCOUNT CONCENTRATION")
    print("=" * 70)
    print(f"Total posts: {n_total:,}")
    print(f"Posts with no author identifier: {missing:,}")
    print(f"Unique authors with an identifier: {n_authors:,}")
    print()
    print(f"Top 20 authors:  {top20:,} posts "
          f"({top20/n_attributed*100:.1f}% of attributed posts, "
          f"{top20/n_total*100:.1f}% of all posts)")
    print(f"Top 100 authors: {top100:,} posts "
          f"({top100/n_attributed*100:.1f}% of attributed posts, "
          f"{top100/n_total*100:.1f}% of all posts)")
    print()
    print("Reminder: no author identifier, name, or post content is")
    print("identified by this script. Percentages use posts with an")
    print("identified author as the denominator, matching this repo's")
    print("baseline-profile.md top 1%/5%/10% methodology.")


if __name__ == "__main__":
    main()
