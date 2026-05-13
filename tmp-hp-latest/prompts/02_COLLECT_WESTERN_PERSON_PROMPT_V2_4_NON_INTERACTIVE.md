# Prompt: Collect Western Historical Person v2.4 — Non-Interactive MVP Mode

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

Collect ONE Western historical person only. The user will provide the target person name.

Recommended MVP targets include:
- Gnaeus Pompeius Magnus / Pompey
- Augustus / Octavian
- Mark Antony

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

Do NOT create `references.jsonl` in the person root folder.
Raw search notes, if absolutely needed, must go under `_raw/`, but avoid raw files unless necessary.

## Execution steps — complete all without pausing

### Step 1 — Collect sources
Gather a compact set of reliable sources. Prefer:
- primary ancient texts where applicable
- critical editions or reputable translations
- academic books or university press sources
- museum or archive records
- established reference works

Wikipedia / Britannica may be used as clues, not final authority for confirmed/high claims.

### Step 2 — Build structured data
Create the required JSON and JSONL files.
Every major claim must have one or more `source_ids`.
If exact passage, volume, page, edition, DOI, ISBN, or URL is not verified, write `needs_verification`.
Do not invent bibliographic details.

### Step 3 — Write human-readable profile
Write `person_profile.md` based only on the structured claims.
Do not introduce uncited facts in the narrative.

### Step 4 — Validate before submission
All JSON and JSONL must parse.
Run or mentally simulate:

`python tools/validate_package.py incoming/western/[person-slug]`

Fix errors before final submission.

## BCE/CE date rule

Do not store BCE dates only as negative integers.
Use explicit BCE/CE fields:

```json
{
  "year_display": "106 BCE",
  "era": "BCE",
  "year_number": 106,
  "astronomical_year": -105,
  "precision": "year"
}
```

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

## Core collection rules

- Focus on verified historical facts first.
- Every important claim must have one or more `source_ids`.
- Use source IDs consistently, e.g. `SRC001`.
- Separate historical fact from later literature, folklore, Shakespearean/dramatic depictions, national myths, and popular culture.
- Do not infer friendship, conspiracy, direct influence, or factional membership unless supported by evidence.
- Visual media is optional and must be cautious.
- A bust, coin, statue, painting, or dramatic scene is not automatically a verified likeness.
- If uncertain, mark uncertainty instead of asking the user.

## Final response format

At the end, provide only:

1. Target person
2. Folder created
3. Files generated
4. Validation result
5. Known limitations
6. Next recommended review action

Do not ask “should I continue?”.
