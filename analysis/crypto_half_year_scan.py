#!/usr/bin/env python3
"""
crypto_half_year_scan.py

Counts, for each half-year, how many dated posts mention a blockchain or
crypto term, using the same eight terms as blockchain_crypto_scan.py.
Aggregate counts only: no record, author, URL, ID or matched text is ever
printed.

Why this exists: blockchain_crypto_scan.py compares whole datasets, and the
three datasets come from different pod tools and cover different years. A
gap between them mixes a difference in time with a difference in tool. This
script puts each dataset on a half-year axis so a series can be read inside
one tool.

Dates: each post's date is decoded from the LinkedIn post ID with the same
Snowflake-style decode as date_cutoff_count.py (INFERENCE: see
../docs/method.md). The ID comes from `linkedinPostId` (podawaa2024),
the `urn:li:activity:` id in `Url` (LinkBoost-2025) and the 18 or 19 digit
id in `post_url` (HyperClapper). Records with no usable ID are counted
as undated and left out of the half-year rows. HyperClapper's `created_at`
is not used: it records when the tool captured the post.

Each post counts once: records are de-duplicated on the post ID within a
dataset, so LinkBoost-2025's repeated logging of one target post does not
inflate a half-year.

Usage:
    python3 crypto_half_year_scan.py podawaa /path/to/podawaa2024.json
    python3 crypto_half_year_scan.py hyperclapper /path/to/HyperClaper.json
    python3 crypto_half_year_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import re
import sys
import json
import argparse
import datetime
from collections import Counter, defaultdict

from blockchain_crypto_scan import COMPILED

LO = datetime.datetime(2010, 1, 1, tzinfo=datetime.timezone.utc)
HI = datetime.datetime(2026, 12, 31, tzinfo=datetime.timezone.utc)
ACTIVITY_RE = re.compile(r"urn:li:activity:(\d{18,19})")
POST_URL_RE = re.compile(r"(?:activity|ugcPost|share)[-:](\d{18,19})")

WEB3_ERA = {"blockchain", "NFT", "Web3", "DeFi"}
COIN_ERA = {"crypto / cryptocurrency", "Bitcoin", "Ethereum", "altcoin"}


def decode_date(post_id):
    try:
        d = datetime.datetime.fromtimestamp((int(post_id) >> 22) / 1000, datetime.timezone.utc)
    except Exception:
        return None
    return d if LO <= d <= HI else None


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        for p in json.load(f)["Posts"]:
            pid = p.get("linkedinPostId")
            yield (str(pid) if pid else None), p.get("Content")


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        for p in json.load(f)["data"]["post"]:
            m = POST_URL_RE.search(p.get("post_url") or "")
            yield (m.group(1) if m else None), p.get("post_title")


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        for r in json.load(f):
            m = ACTIVITY_RE.search(r.get("Url") or "")
            yield (m.group(1) if m else None), r.get("Title")


LOADERS = {"podawaa": load_podawaa, "hyperclapper": load_hyperclapper, "linkboost": load_linkboost}
LABELS = {"podawaa": "podawaa2024", "hyperclapper": "HyperClapper", "linkboost": "LinkBoost-2025"}
SHOW = ["blockchain", "crypto / cryptocurrency", "Bitcoin", "NFT", "Web3", "DeFi"]


def half(d):
    return f"{d.year} H{1 if d.month <= 6 else 2}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS))
    ap.add_argument("path")
    args = ap.parse_args()

    seen = set()
    records = 0
    undated = 0
    dated = Counter()
    hits = Counter()
    web3 = Counter()
    coin = Counter()
    terms = defaultdict(Counter)

    for pid, text in LOADERS[args.dataset](args.path):
        records += 1
        d = decode_date(pid) if pid else None
        if d is None:
            undated += 1
            continue
        if pid in seen:
            continue
        seen.add(pid)
        h = half(d)
        dated[h] += 1
        matched = [name for name, pat in COMPILED if text and pat.search(text)]
        if matched:
            hits[h] += 1
            if WEB3_ERA & set(matched):
                web3[h] += 1
            if COIN_ERA & set(matched):
                coin[h] += 1
            for name in matched:
                terms[h][name] += 1

    print(f"=== {LABELS[args.dataset]}: {records:,} records, {len(seen):,} distinct dated posts, "
          f"{undated:,} records with no decodable post ID ===")
    head = f"{'half-year':<10}{'posts':>8}{'any term':>10}{'%':>8}{'web3-era':>10}{'coin-era':>10}"
    head += "".join(f"{n.split(' ')[0][:10]:>11}" for n in SHOW)
    print(head)
    for h in sorted(dated):
        n = dated[h]
        row = f"{h:<10}{n:>8,}{hits[h]:>10,}{hits[h] / n * 100:>8.2f}{web3[h]:>10,}{coin[h]:>10,}"
        row += "".join(f"{terms[h][name]:>11,}" for name in SHOW)
        print(row)
    print()
    print("web3-era = blockchain, NFT, Web3 or DeFi. coin-era = crypto, Bitcoin, Ethereum or altcoin.")
    print("A post can fall in both. A match is a keyword in the text, not a finding about the post.")


if __name__ == "__main__":
    main()
