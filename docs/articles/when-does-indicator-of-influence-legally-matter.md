# When Does "Indicator of Social Media Influence" Legally Matter?

### The FTC wrote a specific legal definition for exactly the numbers this project measures

Buried in the FTC's 2024 rule on fake reviews and testimonials is a definition worth knowing by heart if you're studying engagement manipulation. **16 CFR § 465.1(j)** defines an "indicator of social media influence" as any metric the public uses to assess an individual's or entity's influence, and names followers, friends, connections, subscribers, views, plays, likes, saves, shares, reposts, and comments explicitly.

## Why this definition does real work

Every metric field across three LinkedIn engagement-pod datasets, `Likes`, `Views`, `like_count`, `impression_count`, `followers`, `SuccessfullLikes`, `SuccessfullComments`, falls squarely within that definition. That's not a coincidence. It's the reason 16 CFR § 465.8's misuse rule is the single most directly applicable law to this kind of data, more than any general fraud or unfair-competition theory.

## What "legally matters" actually requires

Naming a metric doesn't make its manipulation automatically unlawful. The rule attaches liability only when a fake indicator "can be used... to materially misrepresent influence or importance for a commercial purpose," and only when the seller or buyer "knew or should have known" it was fake. A like count existing, even an anomalous one, is a schema fact. Whether that specific number was used to misrepresent something to a specific person, in a way that mattered to a commercial decision, is a separate question the definition itself doesn't answer.

## Why this distinction is worth an entire article

It's tempting to treat "this metric is legally defined as an indicator of influence" as equivalent to "this metric's manipulation is illegal." They aren't the same claim. The first is a matter of reading a regulation's text, straightforward, and true of every metric field in this project's datasets. The second requires facts about intent and actual commercial effect that no exported dataset, however large, can supply on its own.

## What this is, and isn't

**CORROBORATED**: every relevant metric field in all three datasets falls within § 465.1(j)'s definition, a plain textual match.

**Not established**: that any specific instance of an anomalous metric meets the rule's actual liability elements.

Full regulatory text and analysis: **github.com/DreamITSoftware/SPOTAPOD**.

---

*Self-published. Not peer-reviewed. This is not legal advice.*
