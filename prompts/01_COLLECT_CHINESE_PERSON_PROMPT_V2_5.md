# Prompt: Collect Chinese Historical Person v2.5 — MVP Mode

You are collecting data for a historical-person database MVP. The output will be reviewed by a central reviewer before entering the master database.

## Read first

Read and obey:

`project-rules/MVP_COLLECTION_RULES_V2_5.md`

## Non-interactive execution rule

Do not pause to ask for confirmation.
Do not stop after research notes.
Do not ask whether to continue to Step 2.
Do not output progress-only messages.
Complete the whole package in one run using best effort.
If uncertain, mark uncertainty instead of asking a follow-up question.

## Target

Collect ONE Chinese historical person only. The user will provide the target person name.

Recommended next MVP targets:

- 王阳明 / Wang Yangming
- 仇英 / Qiu Ying
- 吴宽 / Wu Kuan

## Required output folder

Create one folder:

`incoming/chinese/[person-slug]/`

Example:

`incoming/chinese/wang-yangming/`

## Required files

Generate exactly:

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

Do not create `references.jsonl` in the person root folder.

## Execution steps — complete all without pausing

### Step 1 — Collect compact reliable sources
Prefer:

- 正史、墓志、碑刻、文集、年谱、地方志
- 诗文、书信、序跋、题跋
- 可靠博物馆藏品记录
- 学术专著、论文、展览图录

Wikipedia / 百度百科 / Britannica may be clues only.

### Step 2 — Create structured files first
Create JSON/JSONL files before writing the full narrative.
Every important claim must have `source_ids`.
One claim must contain one fact only.
Do not invent bibliographic details.
If exact volume/page/passage/version is unknown, write `needs_verification`.

### Step 3 — Write person_profile.md from claims
Narrative must not introduce uncited facts.
Summary wording must not be stronger than the structured claim status.
If something is a later art-historical or literary grouping, write it as later reception.

### Step 4 — Validate
Run or mentally simulate:

`python tools/validate_package.py incoming/chinese/[person-slug]`

Fix errors before final submission.

## Special caution for Chinese figures

- “吴中四才子”, “江南四大才子”, “明四家”, “吴门画派” are often later groupings. Mark as `reception_label` or `later_grouping_only` unless supported as contemporary evidence.
- Do not infer friendship from grouping.
- Do not infer teacher-student relationship from influence unless directly supported.
- Child prodigy stories, personality anecdotes, morality praise, and “first/greatest/founder” claims should default to staging/reception/probable.
- A person’s artwork is not a portrait likeness of that person.

## Minimum person_record.json

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

At the end, report only:

1. Target person
2. Folder created
3. Files generated
4. Validation result
5. Known limitations
6. Next recommended review action

Do not ask “should I continue?”.
