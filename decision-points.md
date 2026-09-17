# Decision points by category

This page maps each `topic_taxonomy.py` category to the real-world
decision it's plausibly trying to influence, grounded in the actual
recurring content patterns `analysis/category_title_patterns.py` finds in
each category — not a generic description of the category name.

**Evidence tier: INFERENCE.** This page describes what a recurring
template is plausibly nudging a reader toward, based on its actual
content. It is not a measured claim that any specific reader made any
specific decision because of it — see [limitations.md](../limitations.md)
for why this repo doesn't make that kind of claim from engagement data
alone.

## Method: why only recurring phrases, never one-off posts

`category_title_patterns.py` reports a phrase only if it recurs at least
three times (configurable) within a category. A post used once is far
more traceable to its specific author than a template reused hundreds of
times across many accounts — the same reasoning already applied to the
"Agree?" × 3,918 finding in [baseline-profile.md](baseline-profile.md).
No quote on this page exceeds 15 words verbatim; longer patterns are
paraphrased.

## The table

| Category | Recurring pattern found | Decision point it's aimed at |
|---|---|---|
| `career_job_search` | A viral rejection-to-success narrative - months of silence, then an AI resume rewrite - recurs 533 times | Whether to abandon traditional job-search advice for an "AI resume rewrite" shortcut |
| `technology_ai` | Weekly "everything that happened in AI" roundups meant to be saved/bookmarked (199×); "ChatGPT can get you hired faster than any recruiter" with a copy-paste prompt list (129×) | Which AI tool or prompt to adopt, and which accounts to treat as a trustworthy AI news source |
| `education_certification` | "Google is offering free AI training" / curated "20 top websites" resource-list posts (93–114×) | Whether to enroll in a specific "free" credential or trust a curated list over independent research |
| `leadership_coaching_motivation` | Generic inspirational metaphors - "life is like a piano," "choose to rise above" - recur 109–130× each | Whether to treat vague motivational content as substantive leadership guidance |
| `finance_investing` | "Hard work beats talent" and "everyone blames the economy" narratives (97–123×) | Whether to internalize a simplified financial/economic narrative when making real financial decisions |
| `marketing_sales_branding` | Youth-credibility branding flexes ("I turned 25 and I'm advising CEOs twice my age") and services-hook posts (78–88×) | Whether to hire or trust a branding consultant based on confidence-signaling rather than track record |
| `business_entrepreneurship` | A repeated political campaign-endorsement post (97×, candidate not identified here) and "simplify your content calendar" templates (65×) | Whether to trust political endorsement content appearing in a professional feed; whether to adopt templated content-strategy advice |
| `health_wellness_fitness` | Personal recovery narratives - psychedelic-assisted healing, therapy destigmatization (52–60× each) | Whether to model a personal health decision on someone else's viral recovery story |
| `book_writing_publishing` | Repeated "my new book is now available" launch-announcement templates | Whether to buy or read the specific book being promoted |
| `uncategorized_other` | No single dominant pattern | Not mapped - this bucket is a catch-all by construction (see [topic-taxonomy.md](topic-taxonomy.md)); forcing a decision point onto it would fabricate specificity the category doesn't have |

## Two things worth flagging plainly

1. **The `business_entrepreneurship` political-endorsement finding is a
   genuine artifact of the keyword-matching method**, not a claim about
   political content strategy generally. A campaign-endorsement post
   likely matched on incidental overlap with the category's keywords
   (e.g. "business," "leadership")
   rather than being business content in any meaningful sense. The
   candidate is deliberately not identified on this page, consistent
   with [privacy.md](../privacy.md) and [limitations.md](../limitations.md).
2. **This is still content-category interpretation, not behavioral
   measurement.** None of the three datasets record who read a post, what
   they did afterward, or whether it changed a decision. The "decision
   point" column is this repo's read of what each recurring template is
   *for*, not evidence of what it *did*.

See also [career-advice-comparison.md](career-advice-comparison.md) and
[algorithm-strategy-advice.md](algorithm-strategy-advice.md) for the
related, more general mechanism (inflated engagement lending false
credibility to whatever claim sits underneath it) this page applies at
the category level.
