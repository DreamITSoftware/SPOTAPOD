# Speaker / thought leader

`analysis/speaker_thought_leader_scan.py` reports how many records'
stated occupation/headline text contains "speaker" and/or "thought
leader." Same discipline as [simple-titles.md](simple-titles.md): only
aggregate counts are reported, never a name, handle, or verbatim
occupation/headline sentence.

## Scope

Only **HyperClaper.json** and **LinkBoost-2025.json** are covered.
`podawaa2024.json` has no occupation/headline-equivalent field, so
there's nothing to scan there - same limitation documented in
[simple-titles.md](simple-titles.md).

## Results (VERIFIED - reproducible via the script)

| | HyperClaper | LinkBoost-2025 |
|---|---|---|
| Total records | 49,369 | 77,969 |
| Records with occupation/headline text | 37,500 | 74,898 |
| "Speaker" | 1,889 (3.83% of all records) | 14,261 (18.29% of all records) |
| "Thought leader" | 500 (1.01% of all records) | 4,292 (5.50% of all records) |
| Both terms in the same record | 500 | 4,175 |

## Reading the overlap

The overlap is the actual finding here, not the raw counts on their
own. In HyperClaper, **100% of "thought leader" records also contain
"speaker"** (500 of 500). In LinkBoost-2025 it's **97.3%** (4,175 of
4,292). That's not two independently common self-descriptions
co-occurring by chance - it's much more consistent with a single
recurring bio template (something like "Speaker | Thought Leader") than
with two separate, unrelated credibility claims. Read the "thought
leader" numbers above as largely a subset of the "speaker" numbers,
not as an independent signal.

LinkBoost-2025 skews dramatically higher on both terms than HyperClaper
- roughly 1 in 5 records mentions "speaker" there, versus roughly 1 in
26 in HyperClaper. This is consistent with LinkBoost-2025's broader lean
toward leadership/coaching content already documented in
[topic-taxonomy.md](topic-taxonomy.md) (`leadership_coaching_motivation`
at 18.91%, roughly 3\u00d7 the other two datasets) and
[simple-titles.md](simple-titles.md) (Founder/Coach account for 34.7%
combined in LinkBoost-2025).

## Caveats

Same as every keyword scan in this repo: a match means the term appears
in the occupation/headline text, not that the account is a verified or
active public speaker. As with [simple-titles.md](simple-titles.md),
this is self-reported text, not a credential.
