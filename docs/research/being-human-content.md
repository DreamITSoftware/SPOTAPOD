# "Being human" content

`analysis/being_human_scan.py` counts mentions of "being human" /
humanity-related terms (being human, human touch, human connection,
humanity, human element, human side, humanness) across post content in
all three datasets. Same discipline as every other scan in this repo:
aggregate counts only, no record, author, or matched text ever printed
beyond the duplicate-template check described below.

Bare "human" is deliberately excluded from this scan's term list - it
collides too broadly with unrelated usage ("human resources," "human
capital," AI-vs-human comparisons) to be a reliable signal for the
specific "being human" theme this scan targets. Only the more specific
phrases above are checked.

## LinkBoost-2025's low-distinct-ratio note, checked

The low-distinct-ratio note fires on LinkBoost-2025 (83 distinct
strings for 1,614 matches), but the duplicate-template warning does
not - no single string dominates (the top is 83 of 1,614, about 5%).
Checked manually: the top repeated strings span many distinct,
on-theme motivational/leadership posts (a light-and-dark duality post
about humanity and love, a "spend your life truly living" post, "employee
loyalty is dead" commentary, a post about letting go in relationships).
This is genuine signal, not an artifact.

## Results (VERIFIED - reproducible via the script)

| Term | podawaa2024 | HyperClapper | LinkBoost-2025 |
|---|---|---|---|
| Humanity | 478 | 238 | 711 |
| Human connection | 136 | 62 | 319 |
| Human touch | 154 | 27 | 207 |
| Human side | 29 | 19 | 239 |
| Being human | 27 | 33 | 228 |
| Human element | 78 | 11 | 55 |
| Humanness | 2 | 1 | - |
| **Any mention** | **857 (0.4014%)** | **374 (0.7576%)** | **1,614 (2.0701%)** |

## Reading these numbers

"Humanity" leads every dataset by a wide margin, consistently the most
common of the seven terms checked, ahead of more specific phrasings
like "being human" or "human touch."

LinkBoost-2025 has by far the highest rate - over 5x podawaa2024's rate
and nearly 3x HyperClapper's. This fits the pattern already established
across multiple scans in this repo: LinkBoost-2025 consistently skews
hardest toward emotional/motivational/inspirational content, the same
lean already documented in
[authenticity-content.md](authenticity-content.md),
[honesty-language-content.md](honesty-language-content.md), and
[confidence-content.md](confidence-content.md).

**A specific thematic connection worth naming**: several of
LinkBoost-2025's top repeated "being human" posts explicitly juxtapose
human qualities (humanity, connection, the human side) against a
backdrop of AI-driven career advice - one of the same top repeated
strings in this scan is a "ChatGPT prompts for resume creation" post.
This suggests "being human" framing in this dataset may function partly
as counter-programming to the same dataset's own heavy AI-productivity
content, rather than as an unrelated, independent theme.

## Caveats

Same as every keyword scan in this repo: a match means the phrase
appears in the text, not that the post contains substantive philosophical
or emotional content about humanity.
