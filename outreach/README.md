# Outreach materials

Derived, aggregate-only educational resources built from this repo's
research — distinct from `docs/`, `analysis/`, and `figures/` because
these are finished deliverables meant to be printed and handed to someone
(a teacher, in this case), not repo documentation.

## What's here

**`classroom-case-study.pdf`** — a two-page, ready-to-teach media
literacy lesson plan ("Spotting Manufactured Popularity Online") for
grades 9–12 (adaptable to 6–8). Built from the same aggregate findings as
[docs/research/](../docs/research/) — the author-concentration statistic
and the 533×-repeated "AI resume rewrite" template — reframed as a
45–50 minute classroom activity with learning objectives, a data
interpretation exercise, discussion questions, and a standards-alignment
table (mapped to NAMLE's Access/Analyze/Evaluate/Act competencies).

`classroom-case-study.html` is the source it was generated from —
includes all icons pre-embedded as base64 data URIs, so it's fully
self-contained and reproducible without any build step beyond HTML-to-PDF
conversion:

```bash
wkhtmltopdf --enable-local-file-access classroom-case-study.html classroom-case-study.pdf
```

## Why this is safe to include as a finished PDF, unlike the raw data

Every fact in this document is aggregate (a concentration statistic, a
repeated-template count) or already-established methodology from
`docs/research/`. It contains no names, handles, photos, profile links,
or unique/one-off post content — see
[docs/research/decision-points.md](../docs/research/decision-points.md)
for why only phrases repeated many times, never a single post, are ever
referenced. That's the same test that governs everything in this repo
(see [CONTRIBUTING.md](../CONTRIBUTING.md)): this PDF passes it, which is
why it's committed directly rather than left as a build artifact.

## Scope note (same as everywhere else in this repo)

This lesson explicitly teaches a *general* media-literacy skill using
LinkedIn/career-advice content as its example — on purpose, since LinkedIn
requires users to be 16+ and isn't a platform most students in the target
grade range use daily. The module states this directly to the teacher and
is **not** framed as being about, or evidence for, any teen-focused
platform, any pending state or federal legislation (including KOSA), or
any state's social-media-minors laws. See
[docs/research/decision-points.md](../docs/research/decision-points.md)
and [docs/limitations.md](../docs/limitations.md) for the reasoning this
follows.
