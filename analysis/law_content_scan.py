#!/usr/bin/env python3
"""
law_content_scan.py

Counts how many records touch legal/law-related language, reported at
two levels of breadth: NARROW (legal-profession-specific: lawyer,
attorney, law firm, litigation, paralegal, etc.) and BROADER (adds
legislation, compliance, intellectual property, lawsuit, court case,
and the bare adjective "legal"). Same discipline as every other scan in
this repo: aggregate counts only, no record or author ever identified.

"Compliance" and bare "legal" are, by design, reported as their own line
items within the broader tally rather than folded in silently, because
both terms are heavily used in general business/HR contexts (data
compliance, workplace compliance) that are not really "about law" the
way a lawyer or law-firm post is -- see docs/research/law-content.md for
why the narrow tally is the more meaningful one for most questions this
scan is likely to be asked to answer.

Usage:
    python3 law_content_scan.py podawaa /path/to/podawaa2024.json
    python3 law_content_scan.py hyperclapper /path/to/HyperClaper.json
    python3 law_content_scan.py linkboost /path/to/LinkBoost-2025.json
"""
import sys
import json
import argparse
import re
import time
from collections import Counter

NARROW = {
    "law firm": r"\blaw firm\b",
    "attorney": r"\battorneys?\b",
    "lawyer": r"\blawyers?\b",
    "litigation": r"\blitigation\b",
    "paralegal": r"\bparalegals?\b",
    "bar exam": r"\bbar exam\b",
    "JD (Juris Doctor)": r"\bJ\.?D\.? (degree|graduate)\b|\bJuris Doctor\b",
    "legal counsel": r"\blegal counsel\b",
    "general counsel": r"\bgeneral counsel\b",
}
BROADER_ADD = {
    "legislation": r"\blegislation\b",
    "compliance": r"\bcompliance\b",
    "intellectual property": r"\bintellectual property\b",
    "contract law": r"\bcontract law\b",
    "employment law": r"\bemployment law\b",
    "lawsuit": r"\blawsuits?\b",
    "court case": r"\bcourt case\b|\bcourtroom\b",
    "legal (adjective, general)": r"\blegal\b",
}


def compile_set(d):
    return [(name, re.compile(pat, re.IGNORECASE)) for name, pat in d.items()]


NARROW_C = compile_set(NARROW)
BROAD_C = NARROW_C + compile_set(BROADER_ADD)


def scan(texts, label, n):
    t0 = time.time()
    narrow_counts = Counter()
    broad_counts = Counter()
    narrow_any = 0
    broad_any = 0
    for t in texts:
        if not t:
            continue
        nhit = False
        for name, pat in NARROW_C:
            if pat.search(t):
                narrow_counts[name] += 1
                nhit = True
        if nhit:
            narrow_any += 1
        bhit = False
        for name, pat in BROAD_C:
            if pat.search(t):
                broad_counts[name] += 1
                bhit = True
        if bhit:
            broad_any += 1
    print(f"=== {label} ({n:,} records, {time.time()-t0:.1f}s) ===")
    print(f"NARROW (legal profession specific): {narrow_any:,} ({narrow_any/n*100:.3f}%)")
    for name, c in narrow_counts.most_common(15):
        print(f"    {name:<28} {c:,} ({c/n*100:.3f}%)")
    print(f"BROADER (incl. legislation/compliance/IP/etc.): {broad_any:,} ({broad_any/n*100:.3f}%)")
    for name, c in broad_counts.most_common(20):
        print(f"    {name:<28} {c:,} ({c/n*100:.3f}%)")
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
