# Prompt: Collect Chinese Historical Person v2.4 — Non-Interactive MVP Mode

You are collecting data for a historical-person database MVP. The output will be reviewed by a central reviewer before entering the master database.

## Non-interactive execution rule

Do not pause to ask the user for confirmation.
Do not stop after research notes.
Do not ask whether to continue to Step 2.
Do not output progress-only messages such as “ready to generate JSON files”.
Do not wait for approval between steps.

You must complete the whole package in one run using best effort.
If information is uncertain, mark it as `needs_verification`, `probable`, `disputed`, `unknown`, `reception`, `legendary`, or `fictional` instead of asking a follow-up question.

If a tool or environment requires a structured-output/final-response call, use it only after generating or presenting the complete deliverable summary. Do not use it as a pause point.

## Target

Collect ONE Chinese historical person only. The user will provide the target person name.

Recommended MVP targets include:
- 沈周 / Shen Zhou
- 王阳明 / Wang Yangming
- 仇英 / Qiu Ying

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

Do NOT create `references.jsonl` in the person root folder.
Raw search notes, if absolutely needed, must go under `_raw/`, but avoid raw files unless necessary.

## Execution steps — complete all without pausing

### Step 1 — Collect sources
Gather a compact set of reliable sources. Prefer:
- primary texts, epitaphs, collected works, poems, prefaces, letters, local gazetteers
- official histories where applicable
- reliable museum records
- academic books or peer-reviewed scholarship

Wikipedia / Baidu / Britannica may be used as clues, not final authority for confirmed/high claims.

### Step 2 — Build structured data
Create the required JSON and JSONL files.
Every major claim must have one or more `source_ids`.
If exact volume, page, edition, URL, passage, inscription, collection number, DOI, or ISBN is not verified, write `needs_verification`.
Do not invent bibliographic details.

### Step 3 — Write human-readable profile
Write `person_profile.md` based only on the structured claims.
Do not introduce uncited facts in the narrative.

### Step 4 — Validate before submission
All JSON and JSONL must parse.
Run or mentally simulate:

`python tools/validate_package.py incoming/chinese/[person-slug]`

Fix errors before final submission.

## Core collection rules

- Focus on verified historical facts first.
- Every important claim must have one or more `source_ids`.
- Use source IDs consistently, e.g. `SRC001`.
- Use Chinese primary/academic sources where possible.
- Distinguish fact from folklore, novels, opera, popular culture, and later reception.
- Later group labels such as “吴中四才子”, “江南四大才子”, “明四家”, “吴门画派代表” must be marked as `reception_label` or `later_grouping_only`.
- Do not infer close friendship, teacher-student relationship, or direct influence unless supported by direct evidence such as letters, poems, prefaces, epitaphs, records, or reliable scholarship.
- Visual media is optional. Do not call any ancient/early-modern portrait a real likeness unless strongly supported.
- If the media is the person’s own work, use `media_type: artwork_by_person` and `representation_status: not_a_likeness`.
- If uncertain, mark uncertainty instead of asking the user.

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

## Final response format

At the end, provide only:

1. Target person
2. Folder created
3. Files generated
4. Validation result
5. Known limitations
6. Next recommended review action

Do not ask “should I continue?”.
