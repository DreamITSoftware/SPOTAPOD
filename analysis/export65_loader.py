#!/usr/bin/env python3
"""
export65_loader.py

Shared reader that lets the scan scripts in this folder run on the 65
export files ("podUsers_<id>_<stamp>.json"). See
../docs/provenance.md#the-65-export-files for where the files came from
and export65_profile.py for the file-level profile.

Usage from a scan script (the dataset name is "export65"):

    from export65_loader import load_export65
    LOADERS["export65"] = load_export65
    LABELS["export65"] = "65 export files"

and then, on the command line, pass either the folder that holds the
files or a single file:

    python3 algorithm_mention_scan.py export65 /path/to/folder_with_the_files

What the loader returns: the post text of each DISTINCT record, in a list.
Records are de-duplicated on `_id` across all the files, and the copy with
the highest `engagedUsersCount` is kept (ties: the earlier file by export
stamp), which is the rule export65_profile.py uses, so the record counts
agree. The text field is `title`.

The files carry no occupation, headline, location, country, likes or
views, so scans that need those fields are not run on this dataset.

The loader never prints anything. Names and ids are not read.
"""
import glob
import hashlib
import os
import re

from export65_profile import num, parse_records


def _read_groups(path):
    """Return a list of (stamp, sha256, records) for each distinct file."""
    if os.path.isdir(path):
        paths = sorted(glob.glob(os.path.join(path, "*podUsers_*.json")))
    else:
        paths = [path]
    seen = {}
    for p in paths:
        raw = open(p, "rb").read()
        h = hashlib.sha256(raw).hexdigest()
        if h in seen:
            continue
        recs = parse_records(raw)
        if recs is None:
            continue
        m = re.search(r"_(\d{4}-\d{2}-\d{2}--\d{2}-\d{2}-\d{2})\.json$", p)
        seen[h] = (m.group(1) if m else "", h, recs)
    return sorted(seen.values(), key=lambda g: (g[0], g[1]))


def load_records(path):
    """Distinct records (one per `_id`), as a list of dicts. Callers must not print them."""
    kept = {}
    for _stamp, _h, recs in _read_groups(path):
        for r in recs:
            k = r.get("_id")
            if k is None:
                continue
            if k not in kept or num(r.get("engagedUsersCount")) > num(kept[k].get("engagedUsersCount")):
                kept[k] = r
    return list(kept.values())


def load_export65(path):
    """Post text of each distinct record. Use for scans whose loaders return a list of texts."""
    return [r.get("title") for r in load_records(path)]


def load_export65_counted(path):
    """Same, as (texts, n). Use for scans whose loaders return a tuple."""
    texts = load_export65(path)
    return texts, len(texts)


def load_export65_fields(path):
    """Same, as {field name: texts}. Use for scans that report one block per field."""
    return {"title": load_export65(path)}


def load_export65_records(path):
    """Same, as a list of {"text_fields": [text]}. Use for scans that expect records."""
    return [{"text_fields": [t]} for t in load_export65(path)]
