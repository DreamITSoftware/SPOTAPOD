#!/usr/bin/env python3
"""
duplicate_content.py

Finds exact-match Content strings shared across multiple distinct authors
in a podawaa2024-style file, and reports it as a size distribution only.
Never prints which authors are in a cluster.

Usage:
    python3 duplicate_content.py /path/to/podawaa2024.json --min-authors 2
"""
import sys
import json
import argparse
import hashlib
from collections import defaultdict


def anon(x):
    return hashlib.sha256(x.encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--min-authors", type=int, default=2)
    args = ap.parse_args()

    with open(args.path, "r", encoding="utf-8") as f:
        posts = json.load(f)["Posts"]

    content_to_authors = defaultdict(set)
    for p in posts:
        content = (p.get("Content") or "").strip()
        aid = p.get("AuthorPublicIdentifier")
        if content and aid:
            content_to_authors[content].add(anon(aid))

    cluster_sizes = []
    for content, authors in content_to_authors.items():
        if len(authors) >= args.min_authors:
            cluster_sizes.append(len(authors))

    cluster_sizes.sort(reverse=True)
    print(f"Clusters with >= {args.min_authors} distinct authors sharing identical content: {len(cluster_sizes)}")
    if cluster_sizes:
        print(f"Largest cluster spans {cluster_sizes[0]} distinct authors")
        print(f"Median cluster spans {cluster_sizes[len(cluster_sizes)//2]} distinct authors")
    print()
    print("size,cluster_count")
    from collections import Counter
    hist = Counter(cluster_sizes)
    for size in sorted(hist):
        print(f"{size},{hist[size]}")


if __name__ == "__main__":
    main()
