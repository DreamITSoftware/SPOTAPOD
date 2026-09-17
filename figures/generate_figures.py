#!/usr/bin/env python3
"""
generate_figures.py

Regenerates every figure in this repo directly from the raw source files.
Only aggregate/statistical values are ever plotted — no names, handles,
photos, or per-record content make it into any chart.

Usage:
    python3 generate_figures.py /path/to/podawaa2024.json /path/to/HyperClaper.json --outdir figures
"""
import sys
import json
import math
import hashlib
import datetime
import argparse
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BHIL_BLUE = "#2b5876"
BHIL_ORANGE = "#e07b39"
BHIL_GRAY = "#8a8f98"


def anon(x):
    return hashlib.sha256(x.encode("utf-8")).hexdigest()


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["Posts"]


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)["data"]["post"]


def decode_year(post_id):
    try:
        ms = post_id >> 22
        return datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc).year
    except Exception:
        return None


def fig_likes_distribution(posts, outdir):
    likes = [p.get("Likes", 0) for p in posts if p.get("Likes", 0) > 0]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(likes, bins=60, color=BHIL_BLUE, log=True)
    ax.set_xscale("log")
    ax.set_xlabel("Likes (log scale)")
    ax.set_ylabel("Record count (log scale)")
    ax.set_title("podawaa2024 — Likes distribution")
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig1-likes-distribution.png", dpi=150)
    plt.close(fig)


def fig_author_concentration(posts, outdir):
    counts = Counter()
    for p in posts:
        aid = p.get("AuthorPublicIdentifier")
        if aid:
            counts[anon(aid)] += 1
    sorted_counts = sorted(counts.values(), reverse=True)
    total = sum(sorted_counts)
    cum = []
    running = 0
    for c in sorted_counts:
        running += c
        cum.append(running / total * 100)
    x = [i / len(cum) * 100 for i in range(1, len(cum) + 1)]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x, cum, color=BHIL_ORANGE, linewidth=2)
    ax.set_xlabel("Authors, ranked by post count (percentile)")
    ax.set_ylabel("Cumulative share of posts (%)")
    ax.set_title("podawaa2024 — Author concentration (Lorenz-style curve)")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig2-author-concentration.png", dpi=150)
    plt.close(fig)


def fig_posts_by_year(posts, outdir):
    years = Counter()
    for p in posts:
        pid = p.get("linkedinPostId")
        if isinstance(pid, int):
            yr = decode_year(pid)
            if yr and 2015 <= yr <= 2027:
                years[yr] += 1
    xs = sorted(years)
    ys = [years[y] for y in xs]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar([str(y) for y in xs], ys, color=BHIL_BLUE)
    ax.set_xlabel("Decoded post year")
    ax.set_ylabel("Record count")
    ax.set_title("podawaa2024 — Posts by decoded year")
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig3-posts-by-year.png", dpi=150)
    plt.close(fig)


def fig_ratio_distribution(posts, outdir):
    ratios = []
    for p in posts:
        views = p.get("Views") or 0
        likes = p.get("Likes") or 0
        if views > 0:
            ratios.append(likes / views)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(ratios, bins=60, range=(0, 2), color=BHIL_ORANGE)
    ax.axvline(1.0, color="red", linestyle="--", linewidth=1, label="Likes = Views")
    ax.set_xlabel("Likes / Views ratio")
    ax.set_ylabel("Record count")
    ax.set_title("podawaa2024 — Like-to-view ratio distribution")
    ax.legend()
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig4-ratio-distribution.png", dpi=150)
    plt.close(fig)


def fig_field_completeness(posts, outdir):
    fields = ["linkedinPostId", "Content", "AuthorPublicIdentifier", "Likes", "Views"]
    n = len(posts)
    pct = []
    for field in fields:
        present = sum(1 for p in posts if p.get(field) not in (None, ""))
        pct.append(present / n * 100)
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.barh(fields, pct, color=BHIL_GRAY)
    ax.set_xlim(0, 100)
    ax.set_xlabel("% of records with field present")
    ax.set_title("podawaa2024 — Field completeness")
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig5-field-completeness.png", dpi=150)
    plt.close(fig)


def fig_hyperclapper_timeline(posts, outdir):
    months = Counter()
    for p in posts:
        ca = p.get("created_at")
        if ca:
            try:
                dt = datetime.datetime.fromisoformat(ca.replace("Z", "+00:00"))
                months[f"{dt.year}-{dt.month:02d}"] += 1
            except Exception:
                pass
    xs = sorted(months)
    ys = [months[m] for m in xs]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(xs, ys, color=BHIL_BLUE, marker="o", markersize=3)
    ax.set_xlabel("Month")
    ax.set_ylabel("Record count")
    ax.set_title("HyperClapper — Records by month")
    ax.tick_params(axis="x", rotation=90, labelsize=6)
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig6-hyperclapper-timeline.png", dpi=150)
    plt.close(fig)


def fig_hyperclapper_reciprocal(posts, outdir):
    flags = Counter()
    for p in posts:
        flags[(bool(p.get("like")), bool(p.get("comment")))] += 1
    labels = [f"like={l} comment={c}" for (l, c) in flags]
    values = list(flags.values())
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(labels, values, color=BHIL_ORANGE)
    ax.set_ylabel("Record count")
    ax.set_title("HyperClapper — Reciprocal engagement flags")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig7-hyperclapper-reciprocal-flags.png", dpi=150)
    plt.close(fig)


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def fig_linkboost_target_concentration(records, outdir):
    counts = Counter()
    for r in records:
        obj_urn = r.get("ObjectUrn")
        if obj_urn:
            counts[anon(obj_urn)] += 1
    sorted_counts = sorted(counts.values(), reverse=True)
    total = sum(sorted_counts)
    cum = []
    running = 0
    for c in sorted_counts:
        running += c
        cum.append(running / total * 100)
    x = [i / len(cum) * 100 for i in range(1, len(cum) + 1)]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(x, cum, color=BHIL_ORANGE, linewidth=2)
    ax.set_xlabel("Target posts, ranked by record count (percentile)")
    ax.set_ylabel("Cumulative share of records (%)")
    ax.set_title("LinkBoost-2025 — Target-post concentration")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig8-linkboost-target-concentration.png", dpi=150)
    plt.close(fig)


def fig_linkboost_country(records, outdir):
    counts = Counter(r.get("country") for r in records if r.get("country"))
    top = counts.most_common(10)
    labels = [c for c, _ in top]
    values = [v for _, v in top]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.barh(labels[::-1], values[::-1], color=BHIL_BLUE)
    ax.set_xlabel("Record count")
    ax.set_title("LinkBoost-2025 — Records by reported country (top 10)")
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig9-linkboost-country.png", dpi=150)
    plt.close(fig)


def fig_linkboost_likes_comments(records, outdir):
    likes = [r.get("SuccessfullLikes") or 0 for r in records]
    comments = [r.get("SuccessfullComments") or 0 for r in records]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.hist(likes, bins=40, alpha=0.6, label="SuccessfullLikes", color=BHIL_BLUE)
    ax.hist(comments, bins=40, alpha=0.6, label="SuccessfullComments", color=BHIL_ORANGE)
    ax.set_xlabel("Count per record")
    ax.set_ylabel("Number of records")
    ax.set_title("LinkBoost-2025 — Successful likes/comments distribution")
    ax.legend()
    fig.tight_layout()
    fig.savefig(f"{outdir}/fig10-linkboost-likes-comments.png", dpi=150)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("podawaa_path")
    ap.add_argument("hyperclapper_path")
    ap.add_argument("--linkboost-path", default=None)
    ap.add_argument("--outdir", default="figures")
    args = ap.parse_args()

    podawaa = load_podawaa(args.podawaa_path)
    hyperclapper = load_hyperclapper(args.hyperclapper_path)

    fig_likes_distribution(podawaa, args.outdir)
    fig_author_concentration(podawaa, args.outdir)
    fig_posts_by_year(podawaa, args.outdir)
    fig_ratio_distribution(podawaa, args.outdir)
    fig_field_completeness(podawaa, args.outdir)
    fig_hyperclapper_timeline(hyperclapper, args.outdir)
    fig_hyperclapper_reciprocal(hyperclapper, args.outdir)

    if args.linkboost_path:
        linkboost = load_linkboost(args.linkboost_path)
        fig_linkboost_target_concentration(linkboost, args.outdir)
        fig_linkboost_country(linkboost, args.outdir)
        fig_linkboost_likes_comments(linkboost, args.outdir)

    print("All figures written to", args.outdir)


if __name__ == "__main__":
    main()
