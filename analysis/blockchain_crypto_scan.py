#!/usr/bin/env python3
"""
blockchain_crypto_scan.py

Counts mentions of blockchain/crypto-related terms across post content
in all three datasets. Same discipline as every other scan in this
repo: aggregate counts only, no record, author, or matched text ever
printed beyond the duplicate-template check below.

podawaa2024 shows by far the highest rate (2.93%, roughly 4x
HyperClaper and 2.5x LinkBoost-2025) and is the only dataset where
"blockchain" itself, rather than "crypto/cryptocurrency" generally,
is the single largest term. Since podawaa2024 is 2024 data and
HyperClaper/LinkBoost-2025 are 2025-2026 data, this is consistent with
-- but does not on its own prove -- a shift in this content ecosystem's
attention from blockchain/Web3 toward AI over that period, which lines
up with the sharp technology_ai increase already documented in
topic-taxonomy.md (16.39% in podawaa2024 to 27.97% in HyperClaper).
Treat this as INFERENCE-tier reasoning from two adjacent data points,
not a confirmed time-series trend.

Usage:
    python3 blockchain_crypto_scan.py podawaa /path/to/podawaa2024.json
    python3 blockchain_crypto_scan.py hyperclapper /path/to/HyperClaper.json
    python3 blockchain_crypto_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
from collections import Counter

TERMS = {
    "blockchain": r"\bblockchain\b",
    "crypto / cryptocurrency": r"\bcrypto\b|\bcryptocurrenc(y|ies)\b",
    "Bitcoin": r"\bBitcoin\b|\bBTC\b",
    "Ethereum": r"\bEthereum\b|\bETH\b",
    "NFT": r"\bNFTs?\b",
    "Web3": r"\bWeb3\b|\bWeb 3\.0\b",
    "DeFi": r"\bDeFi\b",
    "altcoin": r"\baltcoins?\b",
}
COMPILED = [(name, re.compile(pat, re.IGNORECASE)) for name, pat in TERMS.items()]


def scan(texts, label, n):
    term_counts = Counter()
    matching_strings = Counter()
    any_hit = 0
    for t in texts:
        if not t:
            continue
        hit = False
        for name, pat in COMPILED:
            if pat.search(t):
                term_counts[name] += 1
                hit = True
        if hit:
            any_hit += 1
            matching_strings[t.strip()] += 1

    distinct = len(matching_strings)
    top_count = matching_strings.most_common(1)[0][1] if matching_strings else 0
    dominant_share = (top_count / any_hit * 100) if any_hit else 0

    print(f"=== {label} ({n:,} records) ===")
    print(f"Records mentioning any blockchain/crypto term: {any_hit:,} ({any_hit/n*100:.3f}%)")
    print(f"Distinct underlying text values: {distinct:,}")
    if any_hit and dominant_share >= 20:
        corrected = any_hit - top_count + 1
        print(f"  ^ WARNING: top repeated string = {top_count:,} records ({dominant_share:.1f}%) -- "
              f"likely template inflation. Corrected estimate: {corrected:,}")
    elif any_hit and distinct < any_hit * 0.5:
        print(f"  ^ NOTE: distinct-string count ({distinct:,}) is below the match count "
              f"({any_hit:,}) without one string dominating -- consistent with LinkBoost-2025's "
              f"known structure if this is that dataset; worth a manual check otherwise.")
    for name, c in term_counts.most_common():
        if c:
            print(f"    {name:<28} {c:,}")
    print()


def load_podawaa(path):
    with open(path, "r", encoding="utf-8") as f:
        return [p.get("Content") for p in json.load(f)["Posts"]]


def load_hyperclapper(path):
    with open(path, "r", encoding="utf-8") as f:
        return [p.get("post_title") for p in json.load(f)["data"]["post"]]


def load_linkboost(path):
    with open(path, "r", encoding="utf-8") as f:
        return [r.get("Title") for r in json.load(f)]


LOADERS = {"podawaa": load_podawaa, "hyperclapper": load_hyperclapper, "linkboost": load_linkboost}
LABELS = {"podawaa": "podawaa2024", "hyperclapper": "HyperClaper", "linkboost": "LinkBoost-2025"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    args = ap.parse_args()
    texts = LOADERS[args.dataset](args.path)
    scan(texts, LABELS[args.dataset], len(texts))


if __name__ == "__main__":
    main()
