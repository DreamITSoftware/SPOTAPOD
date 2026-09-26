# One-word posts

`analysis/one_word_posts_scan.py` finds posts whose content consists of
a single whitespace-delimited token (e.g. "Agree?", a single emoji, a
bare URL) across all three datasets. Same discipline as every other
scan in this repo: reports counts only. Consistent with this repo's
general approach to recurring content (see
[decision-points.md](decision-points.md) and
`category_title_patterns.py`), only one-word strings that repeat at
least 3 times are ever printed - a genuinely one-off single-word post
is never surfaced, since a unique short post is far more traceable to
its specific author than one reused across many records.

## Results (VERIFIED - reproducible via the script)

| Dataset | One-word posts | % of dataset | Distinct one-word strings |
|---|---|---|---|
| podawaa2024 | 4,608 | 2.158% | 364 |
| HyperClapper | 110 | 0.223% | 23 |
| LinkBoost-2025 | 1,021 | 1.309% | 5 |

**podawaa2024** (top repeated, >= 3 occurrences):

| Word | Count |
|---|---|
| "Agree?" | 3,918 |
| "postNoContent" | 160 |
| Emoji/short reactions (each) | 3-40 |
| "Thoughts?" | 26 |
| "test"/"Test" | 9 / 6 |
| "Concur?" | 8 |
| "Truth!" | 7 |
| "#haveitmagical" | 5 |
| "Surprised?" | 5 |
| "True?" | 4 |
| "Agree..?" | 4 |
| "Finally..." | 4 |
| "#beneficialownership" | 4 |

**HyperClapper:**

| Word | Count |
|---|---|
| "Agree" | 81 |
| "Insightful" | 5 |
| Heart emoji | 3 |

**LinkBoost-2025:**

| Word | Count |
|---|---|
| "Agree?" | 888 |
| "inc.com" | 58 |
| A bare Luma event URL | 57 |
| "Social" | 12 |
| "#selfaccountable" | 6 |

## Two things worth flagging

**"postNoContent" (160x in podawaa2024) is not a real post.** It reads
as a missing-data placeholder string from the source export tool, not
something anyone actually typed. It should be treated as a
data-quality artifact, not genuine one-word engagement content, and is
excluded from the "genuine one-word content" framing below.

**LinkBoost-2025's "inc.com" and a bare Luma event URL are a distinct
genre from the rest of the table** - bare-link posts with zero
accompanying text, different in kind from the one-word engagement-bait
pattern ("Agree?"/"Thoughts?") that otherwise dominates every dataset.

## Reading these numbers

"Agree?"/"Agree" is, by a wide margin, the single most common one-word
post in every dataset where it appears - not just a notable duplicate
string as reported in
[baseline-profile.md](baseline-profile.md), but the literal top
one-word post everywhere. podawaa2024 has both the highest rate (2.16%)
and by far the most variety (364 distinct one-word strings, versus 23
and 5 in the other two) - consistent with podawaa2024 being the
broadest and most diffuse of the three datasets across every other
scan in this repo.

## Caveats

This is a purely structural measure (token count) and says nothing
about a post's substance beyond its length - a one-word post could be
genuine engagement bait, a data artifact, a bare link, or an incomplete
export. As with every other repeated-content finding in this repo, only
strings that recur across multiple records are ever shown.
