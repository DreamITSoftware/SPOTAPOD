#!/usr/bin/env python3
"""
export65_profile.py

Aggregate-only profile of the 65 export files ("podUsers_<id>_<stamp>.json"),
a separate set of files from podawaa2024.json, HyperClaper.json and
LinkBoost-2025.json. See ../docs/provenance.md#the-65-export-files for
where they came from and ../docs/research/export-65-profile.md for the
results this script produced.

What it reports: how many files and distinct files there are, how many
records, how the records de-duplicate, the record states, the engagement
types and timing settings, the creation dates, and how many records fall
before or after a cutoff date. It can also write or check a manifest of
file hashes.

What it never does: print or write a name, a profile or post URL, a post
text, a record id or any other identifier. First and last names are used
only to count distinct accounts, as one-way SHA-256 hashes held in memory.

Every file is one server response: a text frame that begins with the
letter "a" followed by a JSON array of message strings, one of which is a
"result" message holding the list of records. The script also accepts a
plain JSON list of records.

Dates:
  - `createdAt` is the creation time stored on each record, in milliseconds.
    It is read as stored. All dates are UTC.
  - The post id inside each record's `url` is read with the same
    Snowflake-style decode that ../docs/method.md describes (id >> 22 is a
    millisecond timestamp). That decode is an INFERENCE about the id
    format, not confirmed by LinkedIn. It is used here only to compare the
    time a record was created with the time the target post was published.

Usage:
    python3 export65_profile.py /path/to/folder_with_the_files
    python3 export65_profile.py /path/to/folder --cutoff 2024-10-21
    python3 export65_profile.py /path/to/folder --write-manifest out.csv
    python3 export65_profile.py /path/to/folder --check-manifest ../checksums/EXPORT65_MANIFEST.csv
"""
import argparse
import collections
import csv
import datetime as dt
import glob
import hashlib
import json
import os
import re
import sys


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def parse_records(raw):
    """Return the list of records held by one export file, or None if there is none."""
    txt = raw.decode("utf-8")
    if txt[:1] == "a":
        frames = json.loads(txt[1:])
        results = []
        for m in frames:
            msg = json.loads(m) if isinstance(m, str) else m
            if isinstance(msg, dict) and msg.get("msg") == "result" and "error" not in msg:
                results.append(msg.get("result"))
        if len(results) == 1 and isinstance(results[0], list):
            return results[0]
        return None
    data = json.loads(txt)
    return data if isinstance(data, list) else None


def created_ms(rec):
    c = rec.get("createdAt")
    if isinstance(c, dict):
        c = c.get("$date")
    return c if isinstance(c, (int, float)) else None


def iso(ms):
    return dt.datetime.fromtimestamp(ms / 1000, dt.timezone.utc).strftime("%Y-%m-%d")


def post_ms(rec):
    m = re.search(r"urn:li:(?:activity|ugcPost|share):(\d+)", rec.get("url") or "")
    if not m:
        return None
    ts = int(m.group(1)) >> 22
    return ts if 1.4e12 < ts < 2.0e12 else None


def num(v):
    return v if isinstance(v, (int, float)) else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--cutoff", default="2024-10-21", help="UTC date, YYYY-MM-DD (default 2024-10-21)")
    ap.add_argument("--stats", action="store_true",
                    help="also print counts for the statsLikes, statsComments and statsViews fields and for post text")
    ap.add_argument("--write-manifest")
    ap.add_argument("--check-manifest")
    a = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(a.folder, "*podUsers_*.json")))
    if not paths:
        sys.exit("no podUsers_*.json files found in " + a.folder)

    # group uploads by content
    groups = collections.OrderedDict()
    for p in paths:
        raw = open(p, "rb").read()
        h = sha256_bytes(raw)
        g = groups.setdefault(h, {"count": 0, "raw": raw, "stamp": None})
        g["count"] += 1
        m = re.search(r"_(\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2})\.json$", p)
        if m and g["stamp"] is None:
            g["stamp"] = m.group(1)

    files = []
    bad = 0
    for h, g in groups.items():
        recs = parse_records(g["raw"])
        if recs is None:
            bad += 1
            continue
        cts = [c for c in map(created_ms, recs) if c]
        files.append({"sha256": h, "uploads": g["count"], "stamp": g["stamp"] or "", "recs": recs,
                      "created_min": iso(min(cts)) if cts else "", "created_max": iso(max(cts)) if cts else ""})
    files.sort(key=lambda f: (f["stamp"], f["sha256"]))

    print("Files uploaded:                      %d" % len(paths))
    print("Distinct files (by content):         %d" % len(groups))
    print("Byte-identical extra copies:         %d" % (len(paths) - len(groups)))
    if bad:
        print("Files with no readable result:       %d" % bad)
    stamps = [f["stamp"] for f in files if f["stamp"]]
    if stamps:
        print("Export stamps in file names:         %s to %s (yyyy-dd-mm--HH-MM-SS)" % (min(stamps), max(stamps)))
    sizes = [len(f["recs"]) for f in files]
    total = sum(sizes)
    print("Records in the distinct files:       %d" % total)
    print("Files holding exactly 5,000 records: %d (largest file: %d)" % (sum(1 for s in sizes if s == 5000), max(sizes)))

    # de-duplicate on _id: keep the copy with the highest engagedUsersCount (ties: first seen)
    kept, copies = {}, collections.Counter()
    states_seen = collections.defaultdict(set)
    for f in files:
        for r in f["recs"]:
            k = r.get("_id")
            if k is None:
                continue
            copies[k] += 1
            states_seen[k].add(r.get("state"))
            if k not in kept or num(r.get("engagedUsersCount")) > num(kept[k].get("engagedUsersCount")):
                kept[k] = r
    n = len(kept)
    # files at the 5,000-record limit versus the rest: how far back do their records reach?
    def span_days(f):
        c = [x for x in map(created_ms, f["recs"]) if x]
        return (max(c) - min(c)) / 86400000.0 if c else 0.0
    cap = sorted(span_days(f) for f in files if len(f["recs"]) == 5000)
    rest = sorted(span_days(f) for f in files if len(f["recs"]) != 5000)
    if cap and rest:
        print("Days between earliest and latest record, median per file: %.0f for the %d files at 5,000 records, %.0f for the other %d" % (
            cap[len(cap) // 2], len(cap), rest[len(rest) // 2], len(rest)))
    print("Distinct records (_id):              %d" % n)
    print("Records present in more than 1 file: %d" % sum(1 for c in copies.values() if c > 1))
    print("Records whose state differs by file: %d" % sum(1 for v in states_seen.values() if len(v) > 1))

    def block(title, counter, total_n, limit=None):
        print("\n" + title)
        for k, v in counter.most_common(limit):
            print("  %-22s %8d  %5.1f%%" % (k, v, 100.0 * v / total_n))

    block("State (kept copy of each record)", collections.Counter(str(r.get("state")) for r in kept.values()), n)
    block("engagementType", collections.Counter(str(r.get("engagementType")) for r in kept.values()), n)
    timing = collections.Counter(str(r.get("engageTiming")) for r in kept.values())
    block("engageTiming as stored (top 12)", timing, n, 12)

    eu = sorted(num(r.get("engagedUsersCount")) for r in kept.values())
    print("\nengagedUsersCount: median %s, mean %.1f, max %s" % (eu[len(eu) // 2], sum(eu) / len(eu), eu[-1]))
    for fld in ("statsLikes", "statsComments", "statsViews"):
        print("  %s present on %d records" % (fld, sum(1 for r in kept.values() if r.get(fld) is not None)))

    # accounts, counted from one-way hashes of case-normalised first + last name
    accts = set()
    for r in kept.values():
        key = (str(r.get("firstName")).strip().lower() + "|" + str(r.get("lastName")).strip().lower()).encode("utf-8")
        accts.add(hashlib.sha256(key).hexdigest())
    print("\nDistinct accounts (first + last name, case-normalised): %d" % len(accts))

    # dates
    cm = [created_ms(r) for r in kept.values()]
    dated = [c for c in cm if c]
    print("\nRecords with createdAt: %d of %d; earliest %s, latest %s (UTC)" % (len(dated), n, iso(min(dated)), iso(max(dated))))
    cutoff = int(dt.datetime.strptime(a.cutoff, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc).timestamp() * 1000)
    before = sum(1 for c in dated if c < cutoff)
    print("Created before %s: %d (%.2f%%); on or after: %d (%.2f%%)" % (
        a.cutoff, before, 100.0 * before / len(dated), len(dated) - before, 100.0 * (len(dated) - before) / len(dated)))
    months = collections.Counter(dt.datetime.fromtimestamp(c / 1000, dt.timezone.utc).strftime("%Y-%m") for c in dated)
    print("\nRecords created per month (UTC)")
    for k in sorted(months):
        print("  %s %7d" % (k, months[k]))

    lags, pdates = [], []
    for r in kept.values():
        p, c = post_ms(r), created_ms(r)
        if p and c:
            lags.append((c - p) / 3600000.0)
            pdates.append(p)
    if lags:
        lags.sort()
        q = lambda x: lags[int(x * (len(lags) - 1))]
        print("\nHours from the target post's decoded publish time to record creation (INFERENCE: id decode), n=%d" % len(lags))
        print("  min %.2f, 25%% %.2f, median %.2f, 75%% %.2f, 95%% %.2f, max %.1f" % (
            q(0), q(0.25), q(0.5), q(0.75), q(0.95), q(1)))
        print("  negative: %d; within 1 hour: %.1f%%; within 24 hours: %.1f%%; over 7 days: %.1f%%" % (
            sum(1 for x in lags if x < 0),
            100.0 * sum(1 for x in lags if x <= 1) / len(lags),
            100.0 * sum(1 for x in lags if x <= 24) / len(lags),
            100.0 * sum(1 for x in lags if x > 168) / len(lags)))
        print("  decoded post dates run from %s to %s; before %s: %d" % (
            iso(min(pdates)), iso(max(pdates)), a.cutoff, sum(1 for p in pdates if p < cutoff)))

    if a.stats:
        def val(r, k):
            v = r.get(k)
            return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None
        def med(xs):
            xs = sorted(xs)
            return xs[len(xs) // 2] if xs else None
        likes = [val(r, "statsLikes") for r in kept.values()]
        comments = [val(r, "statsComments") for r in kept.values()]
        views = [val(r, "statsViews") for r in kept.values()]
        both = [(l, v) for l, v in zip(likes, views) if l is not None and v is not None]
        print("\nEngagement statistics fields as stored (the site does not document what they measure)")
        print("  Records with post text (title):      %d of %d" % (sum(1 for r in kept.values() if r.get("title")), n))
        print("  statsLikes present:                  %d (median %s)" % (sum(1 for x in likes if x is not None), med([x for x in likes if x is not None])))
        print("  statsComments present:               %d (median %s)" % (sum(1 for x in comments if x is not None), med([x for x in comments if x is not None])))
        print("  statsViews present:                  %d (median %s)" % (sum(1 for x in views if x is not None), med([x for x in views if x is not None])))
        print("  Records with both likes and views:   %d" % len(both))
        print("    statsViews of 0 with statsLikes above 0: %d" % sum(1 for l, v in both if v == 0 and l > 0))
        print("    statsLikes above statsViews:             %d (%.1f%%)" % (
            sum(1 for l, v in both if l > v), 100.0 * sum(1 for l, v in both if l > v) / len(both) if both else 0.0))
        ratios = [l / v for l, v in both if v > 0]
        if ratios:
            ratios.sort()
            print("    Records with exactly 1 view:             %d" % sum(1 for l, v in both if v == 1))
            print("    Highest statsLikes per statsViews:       %.1f to 1 (median %.2f)" % (ratios[-1], ratios[len(ratios) // 2]))
            print("    Records with 2 or more likes per view:   %d; 10 or more: %d; 100 or more: %d" % (
                sum(1 for x in ratios if x >= 2), sum(1 for x in ratios if x >= 10), sum(1 for x in ratios if x >= 100)))
        liked = sorted((x for x in likes if x is not None), reverse=True)
        if len(liked) >= 10:
            cut = liked[9]
            top = [(l, v) for l, v in zip(likes, views) if l is not None and l >= cut]
            print("  Records with the 10 highest statsLikes (ties at the tenth value kept): %d" % len(top))
            print("    with statsViews of 0:                    %d" % sum(1 for l, v in top if v == 0))
            print("    with no statsViews field:                %d" % sum(1 for l, v in top if v is None))
            print("    with statsViews above 0:                 %d" % sum(1 for l, v in top if v is not None and v > 0))

        # concentration by account and repetition of post text; one-way hashes in memory, counts only
        def acct(r):
            k = (str(r.get("firstName")).strip().lower() + "|" + str(r.get("lastName")).strip().lower()).encode("utf-8")
            return hashlib.sha256(k).hexdigest()
        per_acct = collections.Counter(acct(r) for r in kept.values())
        ranked = sorted(per_acct.values(), reverse=True)
        print("\nRecords by account (first + last name, case-normalised; counts only)")
        print("  Distinct accounts:                   %d" % len(ranked))
        for k in (20, 100):
            print("  Share of records from the top %-3d accounts: %.1f%%" % (k, 100.0 * sum(ranked[:k]) / n))
        print("  Accounts with 1 record: %d; with 100 or more: %d (%.1f%% of records)" % (
            sum(1 for c in ranked if c == 1), sum(1 for c in ranked if c >= 100),
            100.0 * sum(c for c in ranked if c >= 100) / n))
        text_recs = collections.Counter()
        text_accts = collections.defaultdict(set)
        for r in kept.values():
            t = r.get("title")
            if t:
                th = hashlib.sha256(t.encode("utf-8")).hexdigest()
                text_recs[th] += 1
                text_accts[th].add(acct(r))
        withtext = sum(text_recs.values())
        rep = [c for c in text_recs.values() if c > 1]
        print("\nRepetition of post text (exact match; counts only)")
        print("  Distinct post texts:                 %d of %d records with text" % (len(text_recs), withtext))
        print("  Texts that occur in more than 1 record: %d (covering %d records)" % (len(rep), sum(rep)))
        print("  Most records sharing one text:       %d" % (max(text_recs.values()) if text_recs else 0))
        multi = [len(v) for v in text_accts.values() if len(v) > 1]
        print("  Texts submitted under more than 1 account name: %d; most account names for one text: %d" % (
            len(multi), max(multi) if multi else 1))

    if a.write_manifest:
        with open(a.write_manifest, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh)
            w.writerow(["file_no", "sha256", "records", "uploads_with_this_content", "export_stamp_yyyy-dd-mm--HH-MM-SS",
                        "created_min_utc", "created_max_utc"])
            for i, f in enumerate(files, 1):
                w.writerow([i, f["sha256"], len(f["recs"]), f["uploads"], f["stamp"], f["created_min"], f["created_max"]])
        print("\nmanifest written: %s (%d rows)" % (a.write_manifest, len(files)))

    if a.check_manifest:
        want = {}
        with open(a.check_manifest, newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                want[row["sha256"]] = int(row["records"])
        have = {f["sha256"]: len(f["recs"]) for f in files}
        ok = sum(1 for h, c in have.items() if want.get(h) == c)
        print("\nmanifest check: %d of %d listed files found with matching hash and record count; %d of your files not listed"
              % (ok, len(want), sum(1 for h in have if h not in want)))


if __name__ == "__main__":
    main()
