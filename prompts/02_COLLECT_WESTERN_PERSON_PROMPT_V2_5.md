# Prompt: Collect Western Historical Person v2.5 — MVP Mode

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

Collect ONE Western historical person only. The user will provide the target person name.

Recommended next MVP targets:

- Gnaeus Pompeius Magnus / Pompey
- Augustus / Octavian
- Mark Antony

## Required output folder

Create one folder:

`incoming/western/[person-slug]/`

Example:

`incoming/western/gnaeus-pompeius-magnus/`

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

- primary ancient texts
- critical editions or reputable translations
- inscriptions, coins, papyri, official records where applicable
- museum or archive records
- academic monographs and peer-reviewed scholarship
- established reference works

Wikipedia / Britannica may be clues only.

### Step 2 — Create structured files first
Create JSON/JSONL files before writing the full narrative.
Every important claim must have `source_ids`.
One claim must contain one fact only.
Do not invent bibliographic details.
If exact volume/page/passage/edition/DOI/ISBN is unknown, write `needs_verification`.

### Step 3 — Write person_profile.md from claims
Narrative must not introduce uncited facts.
Summary wording must not be stronger than the structured claim status.
If something is a later historiographical or literary label, write it as later reception.

### Step 4 — Validate
Run or mentally simulate:

`python tools/validate_package.py incoming/western/[person-slug]`

Fix errors before final submission.

## BCE/CE date rule

Do not store BCE dates only as negative integers.

Use explicit fields:

```json
{
  "year_display": "106 BCE",
  "era": "BCE",
  "year_number": 106,
  "astronomical_year": -105,
  "precision": "year"
}
```

## Special caution for Western figures

- Later literary or dramatic depictions, including Shakespearean reception, must not be treated as evidence for historical actions or words.
- Historiographical labels such as “First Triumvirate”, “founder of empire”, “first emperor”, or “defender of the Republic” may need `reception` or interpretive status depending on wording.
- Do not infer friendship, conspiracy, faction, alliance, or influence without source support.
- Ancient sources are not automatically neutral. Note bias where relevant.
- Busts, coins, statues, and paintings require cautious `representation_status`.
- A later painting or dramatic scene is not a verified likeness.

## Minimum person_record.json

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

## Final response format

At the end, report only:

1. Target person
2. Folder created
3. Files generated
4. Validation result
5. Known limitations
6. Next recommended review action

Do not ask “should I continue?”.
