#!/usr/bin/env python3
"""
entity_mention_scan.py

Counts how many records mention a named entity from four fixed categories
(news outlets, magazines, TV networks/streaming platforms, corporations).
Same discipline as every other scan in this repo: aggregate counts only.
No record, author, or matched text is ever printed by this script.

A record is counted once per entity it mentions (a record naming an
outlet twice still counts once for that outlet), and can be counted
under multiple different entities if it mentions more than one. This is
an overlapping tally, not the mutually-exclusive scheme topic_taxonomy.py
uses.

Known limitation: entity names that double as common English words (e.g.
"time", "target", "max") are deliberately either excluded or require a
qualifying phrase (e.g. "Fortune 500" rather than bare "Fortune" would
still be too broad; patterns below already reflect this trade-off) to
avoid both false positives and, in one observed case, catastrophic
slowdown from a bare common-word pattern matching almost every record.

Usage:
    python3 entity_mention_scan.py podawaa /path/to/podawaa2024.json --category news_outlets
    python3 entity_mention_scan.py hyperclapper /path/to/HyperClaper.json --category all
    python3 entity_mention_scan.py linkboost /path/to/LinkBoost-2025.json --category corporations
"""
import sys
import json
import argparse
import re
import time
from collections import Counter

CATEGORIES = {
    "news_outlets": {
        "Forbes": r"\bForbes\b", "CNBC": r"\bCNBC\b", "Bloomberg": r"\bBloomberg\b",
        "Reuters": r"\bReuters\b", "New York Times": r"\b(New York Times|NYTimes|NYT)\b",
        "Wall Street Journal": r"\b(Wall Street Journal|WSJ)\b", "Washington Post": r"\bWashington Post\b",
        "CNN": r"\bCNN\b", "Fox News": r"\bFox News\b", "BBC": r"\bBBC\b",
        "TechCrunch": r"\bTechCrunch\b", "Business Insider": r"\bBusiness Insider\b",
        "The Guardian": r"\bThe Guardian\b", "Axios": r"\bAxios\b", "Politico": r"\bPolitico\b",
        "USA Today": r"\bUSA Today\b", "Newsweek": r"\bNewsweek\b",
        "HuffPost": r"\bHuffPost\b|\bHuffington Post\b", "NPR": r"\bNPR\b", "MSNBC": r"\bMSNBC\b",
        "ABC News": r"\bABC News\b", "NBC News": r"\bNBC News\b", "Al Jazeera": r"\bAl Jazeera\b",
        "The Economist": r"\bThe Economist\b", "Fast Company": r"\bFast Company\b",
        "Harvard Business Review": r"\bHarvard Business Review\b|\bHBR\b",
    },
    "magazines": {
        "Forbes": r"\bForbes\b", "Harvard Business Review": r"\bHarvard Business Review\b|\bHBR\b",
        "Fast Company": r"\bFast Company\b", "Newsweek": r"\bNewsweek\b",
        "The Economist": r"\bThe Economist\b", "Inc. Magazine": r"\bInc\.\s?Magazine\b|\bInc\.com\b",
        "Entrepreneur Magazine": r"\bEntrepreneur Magazine\b|\bEntrepreneur\.com\b",
        "Fortune": r"\bFortune Magazine\b|\bFortune 500\b|\bFortune 100\b",
        "Wired": r"\bWired Magazine\b|\bWIRED\b",
        "Bloomberg Businessweek": r"\bBloomberg Businessweek\b|\bBusinessweek\b",
        "TIME Magazine": r"\bTIME Magazine\b|\bTIME 100\b", "The Atlantic": r"\bThe Atlantic\b",
        "National Geographic": r"\bNational Geographic\b", "Vogue": r"\bVogue\b",
        "GQ": r"\bGQ Magazine\b", "Vanity Fair": r"\bVanity Fair\b",
        "People Magazine": r"\bPeople Magazine\b", "Rolling Stone": r"\bRolling Stone\b",
        "Psychology Today": r"\bPsychology Today\b",
    },
    "tv_streaming": {
        "CNN": r"\bCNN\b", "Fox News": r"\bFox News\b", "MSNBC": r"\bMSNBC\b",
        "ABC": r"\bABC News\b|\bABC Network\b", "NBC": r"\bNBC News\b|\bNBC Network\b",
        "CBS": r"\bCBS News\b|\bCBS Network\b", "BBC": r"\bBBC\b", "PBS": r"\bPBS\b",
        "Al Jazeera": r"\bAl Jazeera\b", "Fox Business": r"\bFox Business\b", "C-SPAN": r"\bC-?SPAN\b",
        "Netflix": r"\bNetflix\b", "Hulu": r"\bHulu\b", "Disney+": r"\bDisney\+|\bDisney Plus\b",
        "HBO / HBO Max": r"\bHBO Max\b|\bHBO\b", "Amazon Prime Video": r"\bPrime Video\b|\bAmazon Prime Video\b",
        "Apple TV+": r"\bApple TV\+?\b", "Paramount+": r"\bParamount\+|\bParamount Plus\b",
        "Peacock": r"\bPeacock (TV|streaming)\b|\bwatch on Peacock\b", "YouTube": r"\bYouTube\b",
        "Twitch": r"\bTwitch\b", "TikTok": r"\bTikTok\b",
    },
    "corporations": {
        "Google": r"\bGoogle\b", "Microsoft": r"\bMicrosoft\b", "Apple": r"\bApple\b",
        "Amazon": r"\bAmazon\b", "Meta": r"\bMeta\b", "Facebook": r"\bFacebook\b",
        "Tesla": r"\bTesla\b", "Nvidia": r"\bNvidia\b", "OpenAI": r"\bOpenAI\b", "IBM": r"\bIBM\b",
        "Oracle": r"\bOracle (Corporation|Cloud|Database)\b", "Salesforce": r"\bSalesforce\b",
        "Adobe": r"\bAdobe\b", "McKinsey": r"\bMcKinsey\b", "Deloitte": r"\bDeloitte\b",
        "PwC": r"\bPwC\b|\bPricewaterhouseCoopers\b",
        "Ernst & Young (EY)": r"\bErnst\s?&\s?Young\b|\bEY Global\b", "KPMG": r"\bKPMG\b",
        "Goldman Sachs": r"\bGoldman Sachs\b", "JPMorgan": r"\bJP\s?Morgan\b",
        "Morgan Stanley": r"\bMorgan Stanley\b", "Nike": r"\bNike\b", "Starbucks": r"\bStarbucks\b",
        "Walmart": r"\bWalmart\b", "Coca-Cola": r"\bCoca-?Cola\b", "PepsiCo": r"\bPepsiCo\b",
        "Uber": r"\bUber\b", "Airbnb": r"\bAirbnb\b", "SpaceX": r"\bSpaceX\b",
        "LinkedIn": r"\bLinkedIn\b", "Disney": r"\bDisney\b", "Samsung": r"\bSamsung\b", "Intel": r"\bIntel\b",
    },
}


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


def scan(texts, label, category_name, entities):
    compiled = [(name, re.compile(pat, re.IGNORECASE)) for name, pat in entities.items()]
    t0 = time.time()
    counts = Counter()
    any_hit = 0
    n = len(texts)
    for t in texts:
        if not t:
            continue
        hit = False
        for name, pat in compiled:
            if pat.search(t):
                counts[name] += 1
                hit = True
        if hit:
            any_hit += 1
    print(f"=== {label} - {category_name} ({n:,} records, {time.time()-t0:.1f}s) ===")
    print(f"Records mentioning any tracked entity: {any_hit:,} ({any_hit/n*100:.2f}%)")
    for name, c in counts.most_common(40):
        print(f"  {name:<26} {c:,} ({c/n*100:.3f}%)")
    print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dataset", choices=list(LOADERS.keys()))
    ap.add_argument("path")
    ap.add_argument("--category", choices=list(CATEGORIES.keys()) + ["all"], default="all")
    args = ap.parse_args()

    texts = LOADERS[args.dataset](args.path)
    label = LABELS[args.dataset]
    cats = CATEGORIES.keys() if args.category == "all" else [args.category]
    for cat in cats:
        scan(texts, label, cat, CATEGORIES[cat])


if __name__ == "__main__":
    main()
