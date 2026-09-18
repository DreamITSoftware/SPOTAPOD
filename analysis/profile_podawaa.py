#!/usr/bin/env python3
"""
profile_podawaa.py

Aggregate, de-identified profiling of a podawaa2024-style LinkedIn export.

The Likes/Views fields profiled here are "indicators of social media
influence" as defined at 16 CFR § 465.1(j) — see ../docs/regulatory-context.md
for the full text of 16 CFR § 465.8, which governs their misuse. This script
reports only aggregate distributions and makes no claim about whether any
specific record's metrics were fake or used to violate that rule.

Deliberately does NOT print, store, or export any AuthorPublicIdentifier,
Content string tied to an individual record, or any other field that could
re-identify a specific author. Author identifiers are only ever used
in-memory, hashed into a running counter, and discarded.

Input schema expected (top level):
{
  "Posts": [
    {"linkedinPostId": int, "Content": str, "AuthorPublicIdentifier": str,
     "Likes": int, "Views": int},
    ...
  ]
}

Usage:
    python3 profile_podawaa.py /path/to/podawaa2024.json
"""
import sys
import json
import hashlib
from collections import Counter, defaultdict

# LinkedIn share/activity URN IDs are Snowflake-style: shifting right 22 bits
# yields milliseconds since the Unix epoch directly (no additional custom
# epoch offset, unlike Twitter's original scheme).
def decode_year(post_id: int):
    try:
        ms = post_id >> 22
        import datetime
        return datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc).year
    except Exception:
        return None


def anon_id(identifier: str) -> str:
    """One-way hash, salted per-run only for de-duplication within this run.
    Never written out; used only to count unique authors / concentration."""
    return hashlib.sha256(identifier.encode("utf-8")).hexdigest()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 profile_podawaa.py /path/to/podawaa2024.json")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    posts = data["Posts"]
    n = len(posts)

    author_counts = Counter()      # hash -> post count (no identity retained)
    year_counts = Counter()
    zero_views = 0
    likes_gt_views = 0
    content_counts = Counter()     # exact content string -> count (content, not identity)
    field_present = defaultdict(int)
    fields = ["linkedinPostId", "Content", "AuthorPublicIdentifier", "Likes", "Views"]

    for p in posts:
        for field in fields:
            v = p.get(field)
            if v is not None and v != "":
                field_present[field] += 1

        aid = p.get("AuthorPublicIdentifier")
        if aid:
            author_counts[anon_id(aid)] += 1

        pid = p.get("linkedinPostId")
        if isinstance(pid, int):
            yr = decode_year(pid)
            if yr:
                year_counts[yr] += 1

        views = p.get("Views") or 0
        likes = p.get("Likes") or 0
        if views == 0:
            zero_views += 1
        if likes > views:
            likes_gt_views += 1

        content = (p.get("Content") or "").strip()
        if content:
            content_counts[content] += 1

    unique_authors = len(author_counts)

    # Author concentration buckets (no identities, just distribution)
    counts_sorted = sorted(author_counts.values(), reverse=True)
    total_posts_by_authors = sum(counts_sorted)

    def top_share(pct):
        k = max(1, int(len(counts_sorted) * pct))
        return sum(counts_sorted[:k]) / total_posts_by_authors * 100

    bucket_defs = [(1, 1), (2, 5), (6, 20), (21, 50), (51, None)]
    bucket_labels = ["1", "2-5", "6-20", "21-50", "50+"]
    buckets = Counter()
    for c in counts_sorted:
        for (lo, hi), label in zip(bucket_defs, bucket_labels):
            if hi is None:
                if c >= lo:
                    buckets[label] += 1
                    break
            elif lo <= c <= hi:
                buckets[label] += 1
                break

    duplicated_content_records = sum(c for c in content_counts.values() if c > 1)
    duplicate_groups = sum(1 for c in content_counts.values() if c > 1)
    top_duplicates = content_counts.most_common(10)

    print("=" * 60)
    print("PODAWAA2024 — AGGREGATE PROFILE (de-identified)")
    print("=" * 60)
    print(f"Total records:                  {n:,}")
    print(f"Unique authors (hashed count):  {unique_authors:,}")
    print(f"Records with zero Views:        {zero_views:,} ({zero_views/n*100:.1f}%)")
    print(f"Records with Likes > Views:     {likes_gt_views:,} ({likes_gt_views/n*100:.2f}%)")
    print()
    print("Field completeness:")
    for field in fields:
        pct = field_present[field] / n * 100
        print(f"  {field:<24} {field_present[field]:,} ({pct:.1f}%)")
    print()
    print("Decoded post year distribution (from post ID, Snowflake-style):")
    for yr in sorted(year_counts):
        print(f"  {yr}: {year_counts[yr]:,}")
    print()
    print("Author concentration (posts-per-author buckets):")
    for label in bucket_labels:
        print(f"  {label:<8} authors: {buckets[label]:,}")
    print(f"  Top 1% of authors account for {top_share(0.01):.1f}% of posts")
    print(f"  Top 5% of authors account for {top_share(0.05):.1f}% of posts")
    print(f"  Top 10% of authors account for {top_share(0.10):.1f}% of posts")
    print()
    print("Duplicate content (exact-match Content strings, cross-author):")
    print(f"  Records sharing content with >=1 other record: {duplicated_content_records:,}")
    print(f"  Distinct duplicate-content groups:              {duplicate_groups:,}")
    print(f"  Top repeated strings (text only, no author linkage):")
    for text, cnt in top_duplicates:
        snippet = text if len(text) <= 60 else text[:57] + "..."
        print(f"    {cnt:>6}x  {snippet!r}")


if __name__ == "__main__":
    main()
