# MVP Collection Rules v2.5

This version strengthens the v2.4 non-interactive workflow after central review of the Shen Zhou MVP package.

## Purpose

Third-party AI agents may collect and structure historical-person data, but their output is **not trusted master data**. Every package remains `ai_collected_unreviewed` until central review.

## Required package location

Use one folder per person:

- Chinese: `incoming/chinese/[person-slug]/`
- Western: `incoming/western/[person-slug]/`

## Required files

Each person folder must contain exactly these core files:

1. `README.md`
2. `person_profile.md`
3. `person_record.json`
4. `claims.jsonl`
5. `sources.jsonl`
6. `relationships.jsonl`
7. `events.jsonl`
8. `works.jsonl`
9. `visual_media.jsonl`
10. `legendary_notes.jsonl`
11. `open_questions.md`

Raw search files must not be placed in the person root folder. If raw notes are unavoidable, place them under `_raw/` and mark them explicitly as non-curated.

## Non-interactive rule

Do not pause after research notes. Do not ask whether to continue to Step 2. Complete the full package in one run. If uncertain, mark the item as uncertain instead of asking the user.

Allowed uncertainty/status labels:

- `confirmed`
- `probable`
- `disputed`
- `legendary`
- `fictional`
- `reception`
- `unknown`
- `needs_verification`

## Claim discipline

### One claim = one fact

Do not combine multiple facts into one claim.

Bad:

> Shen Zhou had a close relationship with Wen Zhengming, who studied painting under him.

Better:

1. Wen Zhengming studied painting under Shen Zhou.
2. Shen Zhou and Wen Zhengming had a close relationship. This second claim requires separate evidence.

### Description cannot be stronger than claims

`person_record.json.short_description_*` and `person_profile.md` must not use stronger language than the structured claims.

If a claim is marked `reception`, the summary must say:

- “后世美术史中常被视为…”
- “later regarded as…”
- “often classified by later scholarship as…”

Do not write a reception claim as direct fact.

Bad:

> 沈周是吴门画派创始人。

Better:

> 沈周在后世美术史中常被视为吴门画派的奠基人物之一。

## Source level calibration

### A / A_candidate

Reserved for primary or near-primary materials:

- tomb epitaphs
- inscriptions
- collected works by the person
- letters, poems, prefaces, colophons
- official records
- museum catalogue records for specific objects
- reliable editions of primary texts

If volume/page/passage/version is not verified, use `A_candidate`, not `A`.

### B_high / B

Use for reliable modern scholarship:

- academic monographs
- university press books
- peer-reviewed papers
- museum exhibition catalogues with scholarly apparatus

Do not automatically mark academic books as `A`.

### C / D

Use for general web references, encyclopedia pages, Wikipedia, Baidu, Britannica, news pages, blog posts, or unspecialized summaries. These may be used as clues, not sole support for confirmed/high claims.

## Confidence calibration

Use `confirmed/high` only when the claim is directly supported by a strong source.

Use `probable/medium` for:

- teacher-student relationships without direct primary evidence
- friendship or close association without letters/poems/prefaces/colophons
- style-period labels such as “early style”, “late style”, “Fine Shen”, “Coarse Shen”
- exact work purpose or commission details without museum catalogue or inscription
- influence claims
- personality or character anecdotes

Use `reception` for:

- “founder of a school”
- “one of the greatest”
- “pioneer of...”
- “representative figure of...”
- later groupings such as “明四家”, “吴中四才子”, “江南四大才子”, “First Triumvirate” as a historiographical label when appropriate

## Relationship discipline

Do not use `friend`, `close_friend`, `teacher`, `disciple`, `influence`, or `political_ally` unless the evidence supports that relationship directly.

Preferred relationship types:

- `family`
- `documented_teacher_student`
- `probable_teacher_student`
- `documented_association`
- `probable_association`
- `same_cultural_circle`
- `same_political_context`
- `patronage_or_commission`
- `correspondence_or_textual_exchange`
- `later_grouping_only`
- `reception_label`
- `opponent`
- `rival`
- `ally`

If the only evidence is a later grouping, use only `later_grouping_only` or `reception_label`.

## Visual media discipline

Visual media is optional metadata. It must not be treated as verified likeness unless strongly supported.

Use:

- `portrait_likeness`
- `later_traditional_portrait`
- `imagined_portrait`
- `artwork_by_person`
- `coin_or_inscription`
- `map`
- `later_imagined_scene`

If the media is the person’s own work, use:

- `media_type: artwork_by_person`
- `representation_status: not_a_likeness`

All visual media remains staging unless source holder, object ID, date, attribution, and rights/license are verified.

## JSON validity

All `.json` and `.jsonl` files must parse. Avoid unescaped English double quotes inside Chinese text. Prefer Chinese quotation marks: “ ”.

## Final self-check

Before submitting, verify:

1. `person_id` is not empty.
2. All required files exist.
3. All JSON/JSONL files parse.
4. No `references.jsonl` exists in the person root folder.
5. Every `source_id` used in claims/events/relationships/works exists in `sources.jsonl`.
6. No confirmed/high claim relies only on Wikipedia/Baidu/Britannica.
7. Every compound claim has been split.
8. Summary wording is no stronger than claim statuses.
9. Later groupings are not converted into friendship or organization membership.
10. Visual media separates likeness from artwork by the person.
