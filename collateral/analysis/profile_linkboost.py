#!/usr/bin/env python3
"""
profile_linkboost.py

Aggregate, de-identified profiling of a LinkBoost-2025-style export
(a pod-engagement service's action log: each record is one successful
like/comment action performed against a target LinkedIn post).

The engagement-metric fields profiled here (SuccessfullLikes,
SuccessfullComments) are "indicators of social media influence" as
defined at 16 CFR § 465.1(j) — see ../docs/regulatory-context.md for the
full text of 16 CFR § 465.8, which governs their misuse. This script
reports only aggregate distributions and makes no claim about whether any
specific record's metrics were fake or used to violate that rule.

Deliberately does NOT print, store, or export any FirstName, LastName,
piFirstName, piLastName, Occupation, DashEntityUrn, ObjectUrn,
liProfileLink, or UserId tied to a specific record. Identifier fields are
only ever used in-memory, hashed into a running counter, and discarded.

Input schema expected: a top-level JSON array of records — see
schema/linkboost.schema.json.

Usage:
    python3 profile_linkboost.py /path/to/LinkBoost-2025.json
"""
import sys
import json
import hashlib
from collections import Counter, defaultdict


def anon(x) -> str:
    return hashlib.sha256(str(x).encode("utf-8")).hexdigest()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 profile_linkboost.py /path/to/LinkBoost-2025.json")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)

    n = len(records)

    target_counts = Counter()   # hashed ObjectUrn (target post/author) -> record count
    operator_counts = Counter() # hashed UserId (LinkBoost account) -> record count
    country_counts = Counter()
    likes_vals = []
    comments_vals = []
    field_present = defaultdict(int)
    title_counts = Counter()    # target post content -> count (content, not identity)

    fields = ["Id", "FirstName", "LastName", "Occupation", "DashEntityUrn",
              "ObjectUrn", "SuccessfullLikes", "SuccessfullComments",
              "Comment", "Url", "liProfileLink", "liUrl", "liDigitalMarketer",
              "Title", "VolumeId", "UserId", "country"]

    for r in records:
        for field in fields:
            v = r.get(field)
            if v not in (None, ""):
                field_present[field] += 1

        obj_urn = r.get("ObjectUrn")
        if obj_urn:
            target_counts[anon(obj_urn)] += 1

        user_id = r.get("UserId")
        if user_id:
            operator_counts[anon(user_id)] += 1

        country = r.get("country")
        if country:
            country_counts[country] += 1

        likes_vals.append(r.get("SuccessfullLikes") or 0)
        comments_vals.append(r.get("SuccessfullComments") or 0)

        title = (r.get("Title") or "").strip()
        if title:
            title_counts[title] += 1

    unique_targets = len(target_counts)
    unique_operators = len(operator_counts)

    def concentration(counter):
        counts_sorted = sorted(counter.values(), reverse=True)
        total = sum(counts_sorted)
        def top_share(pct):
            k = max(1, int(len(counts_sorted) * pct))
            return sum(counts_sorted[:k]) / total * 100
        return top_share(0.01), top_share(0.05), top_share(0.10)

    target_top1, target_top5, target_top10 = concentration(target_counts)
    op_top1, op_top5, op_top10 = concentration(operator_counts)

    duplicated_title_records = sum(c for c in title_counts.values() if c > 1)
    duplicate_title_groups = sum(1 for c in title_counts.values() if c > 1)

    print("=" * 60)
    print("LINKBOOST-2025 — AGGREGATE PROFILE (de-identified)")
    print("=" * 60)
    print(f"Total records:                       {n:,}")
    print(f"Unique target posts (hashed ObjectUrn): {unique_targets:,}")
    print(f"Unique operator accounts (hashed UserId): {unique_operators:,}")
    print()
    print("Field completeness:")
    for field in fields:
        pct = field_present[field] / n * 100
        print(f"  {field:<20} {field_present[field]:,} ({pct:.1f}%)")
    print()
    print(f"SuccessfullLikes    — min {min(likes_vals)}, max {max(likes_vals)}, "
          f"mean {sum(likes_vals)/n:.1f}")
    print(f"SuccessfullComments — min {min(comments_vals)}, max {max(comments_vals)}, "
          f"mean {sum(comments_vals)/n:.1f}")
    print()
    print("Records by reported country (top 10):")
    for country, cnt in country_counts.most_common(10):
        print(f"  {country:<20} {cnt:,} ({cnt/n*100:.1f}%)")
    missing_country = n - sum(country_counts.values())
    print(f"  {'(missing)':<20} {missing_country:,} ({missing_country/n*100:.1f}%)")
    print()
    print("Target-post concentration (records-per-target, hashed):")
    print(f"  Top 1% of targets account for  {target_top1:.1f}% of records")
    print(f"  Top 5% of targets account for  {target_top5:.1f}% of records")
    print(f"  Top 10% of targets account for {target_top10:.1f}% of records")
    print()
    print("Operator-account concentration (records-per-operator, hashed):")
    print(f"  Top 1% of operators account for  {op_top1:.1f}% of records")
    print(f"  Top 5% of operators account for  {op_top5:.1f}% of records")
    print(f"  Top 10% of operators account for {op_top10:.1f}% of records")
    print()
    print("Duplicate target-post content (exact-match Title, cross-record):")
    print(f"  Records sharing Title with >=1 other record: {duplicated_title_records:,}")
    print(f"  Distinct duplicate-Title groups:              {duplicate_title_groups:,}")


if __name__ == "__main__":
    main()
