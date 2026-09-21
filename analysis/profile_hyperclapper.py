#!/usr/bin/env python3
"""
profile_hyperclapper.py

Aggregate, de-identified profiling of a HyperClapper-style export
(pod-engagement app data: posts plus the reciprocal like/comment flag
that recorded whether the pod interaction happened).

The engagement-metric fields profiled here (like_count, impression_count,
comment_count, followers) are "indicators of social media influence" as
defined at 16 CFR § 465.1(j) — see ../docs/regulatory-context.md for the
full text of 16 CFR § 465.8, which governs their misuse. This script
reports only aggregate distributions and makes no claim about whether any
specific record's metrics were fake or used to violate that rule.

Deliberately does NOT print, store, or export any name, profile picture,
profile URL, internal profile ID, headline, company, or post_title text
tied to a specific record. Identifiers are only ever used in-memory,
hashed into a running counter, and discarded.

Input schema expected (top level):
{
  "data": {
    "post": [
      {
        "profile": {"name": ..., "linkedin_data": {"public_identifier": ..., "followers": ..., "isPremium": ..., "isTopVoice": ..., ...}, ...},
        "comment": bool, "like": bool,
        "created_at": iso8601 str,
        "post_title": str,
        "like_count": int, "impression_count": int, "comment_count": int,
        ...
      },
      ...
    ]
  }
}

Usage:
    python3 profile_hyperclapper.py /path/to/HyperClaper.json
"""
import sys
import json
import hashlib
import datetime
from collections import Counter, defaultdict


def anon_id(identifier: str) -> str:
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()


def parse_followers(s):
    if s is None or s == "":
        return None
    if isinstance(s, (int, float)):
        return int(s)
    digits = "".join(ch for ch in str(s) if ch.isdigit())
    return int(digits) if digits else None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 profile_hyperclapper.py /path/to/HyperClaper.json")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    posts = data["data"]["post"]
    n = len(posts)

    author_counts = Counter()
    reciprocal_flags = Counter()          # (like, comment) -> count
    premium_count = 0
    top_voice_count = 0
    followers_vals = []
    like_impr_ratios = []
    month_counts = Counter()
    title_counts = Counter()
    field_present = defaultdict(int)
    zero_impressions = 0

    top_fields = ["profile", "comment", "like", "post_url", "created_at",
                  "post_title", "like_count", "impression_count", "comment_count"]

    for p in posts:
        for field in top_fields:
            v = p.get(field)
            if v not in (None, ""):
                field_present[field] += 1

        prof = p.get("profile") or {}
        ld = prof.get("linkedin_data") or {}
        pub_id = ld.get("public_identifier")
        if pub_id:
            author_counts[anon_id(pub_id)] += 1

        if ld.get("isPremium"):
            premium_count += 1
        if ld.get("isTopVoice"):
            top_voice_count += 1
        f = parse_followers(ld.get("followers"))
        if f is not None:
            followers_vals.append(f)

        reciprocal_flags[(bool(p.get("like")), bool(p.get("comment")))] += 1

        like_count = p.get("like_count") or 0
        impr = p.get("impression_count") or 0
        if impr == 0:
            zero_impressions += 1
        else:
            like_impr_ratios.append(like_count / impr)

        ca = p.get("created_at")
        if ca:
            try:
                dt = datetime.datetime.fromisoformat(ca.replace("Z", "+00:00"))
                month_counts[f"{dt.year}-{dt.month:02d}"] += 1
            except Exception:
                pass

        title = (p.get("post_title") or "").strip()
        if title:
            title_counts[title] += 1

    unique_authors = len(author_counts)
    counts_sorted = sorted(author_counts.values(), reverse=True)

    duplicated_title_records = sum(c for c in title_counts.values() if c > 1)
    duplicate_groups = sum(1 for c in title_counts.values() if c > 1)

    print("=" * 60)
    print("HYPERCLAPPER — AGGREGATE PROFILE (de-identified)")
    print("=" * 60)
    print(f"Total records:                  {n:,}")
    print(f"Unique authors (hashed count):  {unique_authors:,}")
    print()
    print("Field completeness:")
    for field in top_fields:
        pct = field_present[field] / n * 100
        print(f"  {field:<20} {field_present[field]:,} ({pct:.1f}%)")
    print()
    print("Reciprocal engagement flags (like, comment) — pod-exchange signal:")
    for (like, comment), cnt in sorted(reciprocal_flags.items(), key=lambda x: -x[1]):
        pct = cnt / n * 100
        print(f"  like={like!s:<5} comment={comment!s:<5} -> {cnt:,} ({pct:.1f}%)")
    print()
    print(f"Records with zero impressions:  {zero_impressions:,} ({zero_impressions/n*100:.1f}%)")
    if like_impr_ratios:
        srt = sorted(like_impr_ratios)
        mid = srt[len(srt)//2]
        print(f"Median like/impression ratio (non-zero-impr records): {mid:.4f}")
    print()
    print(f"Author accounts flagged isPremium:  {premium_count:,} ({premium_count/n*100:.1f}% of records)")
    print(f"Author accounts flagged isTopVoice:  {top_voice_count:,} ({top_voice_count/n*100:.1f}% of records)")
    if followers_vals:
        srt = sorted(followers_vals)
        print(f"Followers — median: {srt[len(srt)//2]:,}, max: {srt[-1]:,}, records with data: {len(srt):,}")
    print()
    print("Records by month (created_at):")
    for month in sorted(month_counts):
        print(f"  {month}: {month_counts[month]:,}")
    print()
    print("Author concentration (posts-per-author):")
    if counts_sorted:
        total = sum(counts_sorted)
        def top_share(pct):
            k = max(1, int(len(counts_sorted) * pct))
            return sum(counts_sorted[:k]) / total * 100
        print(f"  Top 1% of authors account for {top_share(0.01):.1f}% of posts")
        print(f"  Top 5% of authors account for {top_share(0.05):.1f}% of posts")
        print(f"  Top 10% of authors account for {top_share(0.10):.1f}% of posts")
    print()
    print("Duplicate post_title content (cross-author exact match):")
    print(f"  Records sharing title with >=1 other record: {duplicated_title_records:,}")
    print(f"  Distinct duplicate-title groups:              {duplicate_groups:,}")


if __name__ == "__main__":
    main()
