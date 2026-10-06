# What 16 CFR § 465.8 Actually Says

### The FTC rule on fake social media indicators, and the two things it requires that no dataset can supply

A federal rule covers conduct like engagement pods. **16 CFR § 465.8**, "Misuse of fake indicators of social media influence," took effect October 21, 2024, as part of the FTC's Trade Regulation Rule on Consumer Reviews and Testimonials. It says:

> It is an unfair or deceptive act or practice... for anyone to sell or distribute fake indicators of social media influence that they knew or should have known to be fake... or to purchase or procure [them]... that materially misrepresent their influence or importance for a commercial purpose.

"Indicators of social media influence" is defined broadly enough to cover the metrics this kind of research measures: followers, views, likes, saves, shares, and comments, all named explicitly in the rule.

## The two elements that decide the question

The rule only reaches conduct satisfying both: scienter (the seller or buyer "knew or should have known" the indicator was fake) and materiality for a commercial purpose (the fake indicator actually misrepresents influence in a way that matters commercially).

Checking three LinkedIn engagement-pod datasets against this rule element by element splits the elements in two. Two have data behind them. The metrics the rule covers exist and are populated across all three files (a schema fact), and a coordinated, reciprocal exchange mechanism is documented (one dataset logs a paired like-and-comment flag together 68.6% of the time, and another logs every single record as a "successful" pod action by its own structure). The other two elements, materiality to a specific reader's decision, and scienter, don't exist in any form a dataset can supply. No file records what a specific buyer knew, or what a specific reader actually decided because of an inflated number.

## Why the gap matters

The rule shows what aggregate data can and cannot do. It can show a mechanism exists at scale. It cannot show intent or a specific instance of reliance. No dataset of exported records could close those gaps, because they are facts about a specific transaction between specific people.

## What this is, and isn't

**CORROBORATED**: the covered metrics exist and are populated in all three files.

**STATED/CORROBORATED**: the reciprocal-exchange mechanism and its frequency.

**Not addressed by any dataset**: scienter, in any of the three files. The rule depends on this element most.

Full element-by-element table and sourcing: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. This is not legal advice. The author is not a lawyer. Consult one for any actual legal determination.*
