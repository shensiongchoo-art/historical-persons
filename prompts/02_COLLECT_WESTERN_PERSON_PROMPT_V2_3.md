# Prompt: Collect Western Historical Person v2.3

You are collecting data for a historical-person database MVP. The output will be reviewed by a central reviewer before entering the master database.

## Target

Collect ONE Western historical person only.

The user will provide the target person name.

## Required output folder

Create one folder:

`incoming/western/[person-slug]/`

Example:

`incoming/western/gnaeus-pompeius-magnus/`

## Required files

Generate these files exactly:

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

Do NOT create `references.jsonl` in the root folder. Raw search notes, if needed, must go under `_raw/`.

## Core collection requirements

- Focus on verified historical facts first.
- Every important claim must have one or more `source_ids`.
- Use source IDs consistently, e.g. `SRC001`.
- Do not invent bibliographic metadata.
- If volume, page, URL, edition, DOI, ISBN, or passage is not verified, write `needs_verification`.
- Prefer primary texts, critical editions, reliable academic books, museum records, and established reference works.
- Wikipedia / Britannica can be clues, not final authority.
- Separate historical facts from later literature, folklore, Shakespearean/dramatic depictions, national myths, and popular culture.
- Do not infer direct influence, friendship, conspiracy, or factional membership unless supported by direct evidence.
- Visual media is optional. Busts, coins, paintings, and statues must include `representation_status`.
- A later painting or dramatic scene is not evidence of real appearance.

## BCE/CE date rule

Do not store BCE dates only as negative integers.

Use:

```json
{
  "year_display": "106 BCE",
  "era": "BCE",
  "year_number": 106,
  "astronomical_year": -105,
  "precision": "year"
}
```

## Required JSON rule

All `.json` and `.jsonl` files must be valid JSON. Avoid unescaped English double quotes inside text.

## `person_record.json` minimum fields

```json
{
  "person_id": "P_WEST_[PERIOD]_[CANONICAL_NAME]",
  "canonical_key": "person_slug",
  "primary_display_name_en": "",
  "primary_display_name_zh": "",
  "historical_status": "confirmed_historical_person",
  "primary_culture": "",
  "primary_language": "en",
  "period": "",
  "birth": {
    "year_display": "",
    "era": "BCE",
    "year_number": null,
    "astronomical_year": null,
    "precision": "",
    "original_date_text": "",
    "conversion_note": ""
  },
  "death": {
    "year_display": "",
    "era": "BCE",
    "year_number": null,
    "astronomical_year": null,
    "precision": "",
    "original_date_text": "",
    "conversion_note": ""
  },
  "review_status": "ai_collected_unreviewed",
  "inclusion_category": "core_historical_candidate",
  "source_sufficiency": "to_be_reviewed",
  "short_description_en": "",
  "short_description_zh": ""
}
```

## Final self-check

Before submitting, verify:

1. `person_id` is not empty.
2. Every JSON/JSONL file parses.
3. No `references.jsonl` exists in the person root folder.
4. Every `source_id` used in claims/events/relationships/works exists in `sources.jsonl`.
5. No confirmed/high claim relies only on Wikipedia/Britannica.
6. Literary/dramatic reception is separated from historical fact.
7. Visual media is cautious and not treated as verified likeness without evidence.
8. Uncertain claims are marked `probable`, `needs_verification`, `disputed`, `legendary`, or `reception`.
