# Data dictionary

Every "indicator of social media influence" field below (`Likes`, `Views`,
`like_count`, `impression_count`, `comment_count`, `followers`) falls within
the definition at 16 CFR § 465.1(j), which [16 CFR § 465.8](regulatory-context.md)
covers. See that doc for the full rule text and what it requires beyond a
raw metric value.

## podawaa2024.json

Top level: `{"Posts": [ ... ]}`

| Field | Type | Completeness | Notes |
|---|---|---|---|
| `linkedinPostId` | int | 98.4% | Snowflake-style ID; encodes an approximate post timestamp (see [method](method.md)) |
| `Content` | string | 99.7% | Raw post text. Placeholder strings such as `"This post has no content"` / `"postNoContent"` indicate the pipeline that produced this dataset couldn't retrieve real content, not that the post was actually empty |
| `AuthorPublicIdentifier` | string | 88.8% | LinkedIn's public profile slug. **Never printed by any script in this repo** — hashed in memory only |
| `Likes` | int | 100.0% | As recorded at collection time |
| `Views` | int | 100.0% | As recorded at collection time; 44.3% of records show 0, which is a data-completeness gap, not necessarily zero actual views (see [limitations](limitations.md)) |

## HyperClaper.json

Top level: `{"data": {"post": [ ... ]}}`

| Field | Type | Completeness | Notes |
|---|---|---|---|
| `profile.name` | string | — | Author display name. **Never printed by any script in this repo** |
| `profile.linkedin_data.public_identifier` | string | — | LinkedIn slug. Hashed in memory only |
| `profile.linkedin_data.followers` | string (e.g. `"5,381 followers"`) | — | Parsed to int for aggregate stats only |
| `profile.linkedin_data.isPremium` / `isTopVoice` | bool | — | Account status flags |
| `profile.linkedin_data.linkedin_profile_link` / `linkedin_profile_id` | string / string | — | **Never read by any script in this repo except for hashing `public_identifier`** |
| `profile.profile_picture` | URL | — | **Never read by any script in this repo** |
| `comment` | bool | 100.0% | Whether a reciprocal comment action was recorded for this post via the pod tool |
| `like` | bool | 100.0% | Whether a reciprocal like action was recorded for this post via the pod tool |
| `post_url` | URL | 100.0% | Link to the LinkedIn post itself |
| `created_at` | ISO 8601 timestamp | 100.0% | When this record was captured, not necessarily the post's original publish date |
| `post_title` | string | 98.8% | Post text/caption |
| `like_count` / `impression_count` / `comment_count` | int | 15.3% / 2.0% / 15.1% | Sparse — only populated for a minority of records |

## LinkBoost-2025.json

Top level: `[ ... ]` (flat array, no wrapper object)

| Field | Type | Completeness | Notes |
|---|---|---|---|
| `Id` | string | 100.0% | Internal record ID |
| `FirstName` / `LastName` | string | 96.0–96.1% | Real name. **Never printed by any script in this repo** |
| `piFirstName` / `piLastName` | string | 100.0% | Duplicate of FirstName/LastName, always present. **Never printed by any script in this repo** |
| `Occupation` | string | 96.1% | LinkedIn-style headline/bio — a quasi-identifier on its own |
| `DashEntityUrn` | string | 96.1% | LinkedIn internal profile URN. **Never read by any script in this repo** |
| `ObjectUrn` | string | 100.0% | LinkedIn member URN identifying the target post/author (469 unique). Hashed in memory only, used to measure target-post concentration |
| `SuccessfullLikes` / `SuccessfullComments` | int | 100.0% | Count of successful pod actions recorded for this record (min 2 / min 1, max 261 / max 133) |
| `Comment` | string | 99.9% | Comment text posted as part of the pod action |
| `Url` | string | 100.0% | Link to the target LinkedIn post |
| `liProfileLink` | string (HTML) | 96.1% | Anchor tag embedding a profile URN and a "Digital Marketer: Lastname, Firstname" label. **Never read by any script in this repo** |
| `liUrl` / `liDigitalMarketer` | string | 100.0% | Related HTML/label fields. **Never read by any script in this repo** |
| `Title` | string | 99.6% | Target post's content |
| `VolumeId` | int | 100.0% | Batch identifier — only 1 unique value across the whole file |
| `UserId` | string | 100.0% | LinkBoost operator/account ID (238 unique — not a LinkedIn ID). Hashed in memory only |
| `country` | string | 60.5% | Reported country (22 unique) — a quasi-identifier in combination with other fields |

Fields not covered by scripts beyond hashing/counting as noted above are
internal/structural and carry no additional identity risk beyond what's
already flagged — this includes `id` and `__typename` in HyperClaper.json.

