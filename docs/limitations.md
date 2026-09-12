# Limitations

## Why this repo stops at aggregates, on purpose

Both source files identify real, non-consenting individuals — by handle in
`podawaa2024.json`, by full name, photo, and profile link in
`HyperClaper.json`, and by real name and LinkedIn URN in `LinkBoost-2025.json`.
The overwhelming majority of the combined unique identities across all three
files are private individuals, not public figures, and
appearing in either dataset is not, by itself, proof that a given person
knowingly used pod tooling:

- **Provenance is STATED, not VERIFIED.** Neither file's records carry
  independent, per-record confirmation that the account in question enrolled
  in an engagement pod. The classification comes from however each dataset
  was collected (see each file's own documentation, where available), not
  from anything derivable from the record fields themselves. This matters
  legally, not just methodologically: [16 CFR § 465.8](regulatory-context.md)
  only reaches conduct where someone "knew or should have known" an
  indicator was fake *and* it was used to misrepresent influence "for a
  commercial purpose." Neither element is a field in either dataset, and
  neither can be established from aggregate statistics — so nothing in this
  repo should be read as establishing that any account meets that legal
  standard.
- **Zero-views and low-denominator artifacts are common and mundane.** 44.3%
  of `podawaa2024` records show `Views = 0`; 98.0% of `HyperClaper` records
  show zero impressions. Some of this may reflect real pod-driven anomalies,
  but a large share is almost certainly a tracking/collection gap — LinkedIn's
  own view-count rollout was inconsistent over the 2018–2024 window this data
  spans. Treating a zero as "suspicious" without that context would
  misclassify a lot of ordinary accounts.
- **Reciprocal `like`/`comment` flags describe the tool's action, not the
  author's intent.** A post's *own author* did not necessarily request or
  even know about a reciprocal interaction; pod platforms can attach accounts
  to a queue in ways the account holder didn't fully understand or control.
- **Being a "target" in LinkBoost-2025 doesn't establish the target
  requested the engagement, either.** A high `SuccessfullLikes`/
  `SuccessfullComments` count on a given `ObjectUrn` tells you the pod
  service successfully acted on that post — it says nothing about whether
  the post's author paid for it, knew about it, or had anything to do with
  arranging it. Someone else could have targeted their post without their
  involvement.
- **Duplicate content has mundane causes.** Repeated boilerplate ("Agree?",
  "This post has no content", localized placeholder strings) mostly reflects
  the data pipeline's own fallback behavior, or copy-paste engagement-bait
  templates that circulate widely and organically — not necessarily a
  coordinated pod.
- **Small sample per author.** Most authors in `podawaa2024` have very few
  posts (1,409 authors have exactly 1). A single anomalous record is weak
  evidence about a person's overall behavior.

Because of all of the above, this repo deliberately does not build, and will
not build, a per-author lookup, browsable table, or "who's in this dataset"
tool. Doing so would present STATED and INCONCLUSIVE signals as if they were
individual verdicts, attached to a real person's name and photo, with no
correction mechanism and no due process. That's a different (and much
heavier) kind of claim than "here is the aggregate shape of this data,"
and this repo only makes the latter claim.

## What the aggregate numbers do and don't tell you

- They tell you the **shape** of two datasets: how skewed authorship is, how
  much content repeats, how sparse certain fields are, how activity is
  distributed over time.
- They do **not** tell you that any specific account, or even most accounts
  in either file, engaged in deceptive behavior. Population-level skew
  (a small number of accounts producing a large share of volume) is a normal
  feature of almost any social-platform dataset, pods or no pods.
- An absence of anomaly in these aggregate figures is not evidence that a
  dataset is "clean" of pod activity, and a high number in some bucket is not
  evidence that a specific account is "dirty." Both files may substantially
  undercount or overcount actual pod participation depending on how they were
  originally collected.

## Scope

This analysis covers exactly the two files checksummed in
[checksums/CHECKSUMS.txt](../checksums/CHECKSUMS.txt). No other data source,
merge, or join was used to produce any figure in this repo. See
[regulatory-context.md](regulatory-context.md) for the specific rule
(16 CFR § 465.8) this whole analysis is oriented around, and what it does
and doesn't require to prove a violation, and [provenance.md](provenance.md)
for the reported (STATED, not verified) origin of each file.
