# Outreach materials

These are derived, aggregate-only educational resources built from this
repo's research.

They sit apart from `docs/`, `analysis/`, and `figures/` because they
are finished deliverables meant to be printed and handed to someone (a
teacher, in this case), not repo documentation.

## What's here

**`classroom-case-study.pdf`**, a two-page, ready-to-teach media
literacy lesson plan ("Spotting Manufactured Popularity Online") for
grades 9 to 12 (adaptable to 6 to 8). Built from the same aggregate findings as
[docs/research/](../docs/research/), the author-concentration statistic
and the 533×-repeated "AI resume rewrite" template, reframed as a
45 to 50 minute classroom activity with learning objectives, a data
interpretation exercise, discussion questions, and a standards-alignment
table (mapped to NAMLE's Access/Analyze/Evaluate/Act competencies).

`classroom-case-study.html` is the source the PDF was generated from. It
includes all icons pre-embedded as base64 data URIs, so it is
self-contained and needs no build step beyond HTML-to-PDF conversion:

```bash
wkhtmltopdf --enable-local-file-access classroom-case-study.html classroom-case-study.pdf
```

## Why this is safe to include as a finished PDF, unlike the raw data

Every fact in this document is aggregate (a concentration statistic, a
repeated-template count) or established methodology from
`docs/research/`. It contains no names, handles, photos, profile links,
or unique/one-off post content.

See
[docs/research/decision-points.md](../docs/research/decision-points.md)
for why only phrases repeated many times, never a single post, are ever
referenced. The same test governs everything in this repo (see
[CONTRIBUTING.md](../CONTRIBUTING.md)).

The PDF passes it, so it is committed directly instead of being left as
a build artifact.

## Scope note (same as everywhere else in this repo)

This lesson teaches a *general* media-literacy skill and uses
LinkedIn/career-advice content as its example on purpose: LinkedIn
requires users to be 16+ and most students in the target grade range do
not use it daily. The module tells the teacher this directly. It is
**not** framed as being about, or evidence for, any teen-focused
platform, any pending state or federal legislation (including KOSA), or
any state's social-media-minors laws. See
[docs/research/decision-points.md](../docs/research/decision-points.md)
and [docs/limitations.md](../docs/limitations.md) for the reasoning this
follows.
