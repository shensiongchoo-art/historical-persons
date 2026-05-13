# Prompt: Collect Chinese Historical Person v2.3

You are collecting data for a historical-person database MVP. The output will be reviewed by a central reviewer before entering the master database.

## Target

Collect ONE Chinese historical person only.

The user will provide the target person name.

## Required output folder

Create one folder:

`incoming/chinese/[person-slug]/`

Example:

`incoming/chinese/shen-zhou/`

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
- Use Chinese primary/academic sources where possible.
- Wikipedia / Baidu / Britannica can be clues, not final authority.
- Distinguish fact from folklore, novels, opera, popular culture, and later reception.
- Later group labels such as “吴中四才子”, “江南四大才子”, “明四家”, “吴门画派代表” must be marked as `reception_label` or `later_grouping_only`.
- Do not infer close friendship, teacher-student relationship, or direct influence unless supported by direct evidence such as letters, poems, prefaces, epitaphs, records, or reliable scholarship.
- Visual media is optional. Do not call any ancient/early-modern portrait a real likeness unless strongly supported.
- If the media is the person’s own work, use `media_type: artwork_by_person` and `representation_status: not_a_likeness`.

## Required JSON rule

All `.json` and `.jsonl` files must be valid JSON. Avoid unescaped English double quotes inside Chinese text. Prefer Chinese quotation marks: “ ”.

## `person_record.json` minimum fields

```json
{
  "person_id": "P_CHN_[PERIOD]_[CANONICAL_NAME]",
  "canonical_key": "person_slug",
  "primary_display_name_zh": "",
  "primary_display_name_en": "",
  "historical_status": "confirmed_historical_person",
  "primary_culture": "Chinese",
  "primary_language": "zh-Hans",
  "period": "",
  "birth": {
    "year_display": "",
    "era": "CE",
    "precision": "",
    "original_date_text": "",
    "conversion_note": ""
  },
  "death": {
    "year_display": "",
    "era": "CE",
    "precision": "",
    "original_date_text": "",
    "conversion_note": ""
  },
  "review_status": "ai_collected_unreviewed",
  "inclusion_category": "core_historical_candidate",
  "source_sufficiency": "to_be_reviewed",
  "short_description_zh": "",
  "short_description_en": ""
}
```

## Final self-check

Before submitting, verify:

1. `person_id` is not empty.
2. Every JSON/JSONL file parses.
3. No `references.jsonl` exists in the person root folder.
4. Every `source_id` used in claims/events/relationships/works exists in `sources.jsonl`.
5. No confirmed/high claim relies only on Wikipedia/Baidu/Britannica.
6. Later grouping is not treated as friendship.
7. Visual media separates likeness from artwork by the person.
8. Uncertain claims are marked `probable`, `needs_verification`, `disputed`, `legendary`, or `reception`.
