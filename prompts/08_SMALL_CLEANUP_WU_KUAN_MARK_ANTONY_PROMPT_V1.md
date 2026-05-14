# Prompt: Small Cleanup — Wu Kuan + Mark Antony after PR #9 v1

Use this prompt with Claude Code / Codex after PR #9 has been merged.

Repository:

`https://github.com/shensiongchoo-art/historical-persons`

## Objective

Perform a small, targeted cleanup only.

Do NOT collect new people.
Do NOT merge PRs yourself.
Do NOT change project scope.
Do NOT build visual/dashboard features.
Do NOT move anything to master.

This cleanup addresses small issues found after PR #9 was merged:

1. Wu Kuan person_id still uses numeric suffix.
2. Mark Antony person_id still uses numeric suffix.
3. Mark Antony relationship type `sibling` should be normalized or rules updated.
4. Wu Kuan short description is stronger than its claim statuses.

## Read first

Read:

1. `project-rules/MVP_COLLECTION_RULES_V2_5.md`
2. `reviewed/staging/_mvp_hardening_report_v1.md`
3. `incoming/chinese/wu-kuan/person_record.json`
4. `incoming/chinese/wu-kuan/claims.jsonl`
5. `incoming/chinese/wu-kuan/relationships.jsonl`
6. `incoming/western/mark-antony/person_record.json`
7. `incoming/western/mark-antony/relationships.jsonl`
8. `tools/validate_package.py`

## Branch

Create a new branch:

`maintenance/cleanup-wu-kuan-mark-antony-v1`

## Task A — Standardize Wu Kuan person_id

Current likely ID:

`P_CHN_MING_002_WU_KUAN`

Replace everywhere in `incoming/chinese/wu-kuan/` with:

`P_CHN_MING_WU_KUAN`

Files to check:

- `person_record.json`
- `claims.jsonl`
- `events.jsonl`
- `relationships.jsonl`
- `works.jsonl`
- `visual_media.jsonl`
- `legendary_notes.jsonl`
- `person_profile.md`
- `README.md`
- `open_questions.md`

If the old ID is not present in a file, do not force changes.

## Task B — Standardize Mark Antony person_id

Current likely ID:

`P_WEST_ROMAN_002_MARK_ANTONY`

Replace everywhere in `incoming/western/mark-antony/` with:

`P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS`

Files to check:

- `person_record.json`
- `claims.jsonl`
- `events.jsonl`
- `relationships.jsonl`
- `works.jsonl`
- `visual_media.jsonl`
- `legendary_notes.jsonl`
- `person_profile.md`
- `README.md`
- `open_questions.md`

If the old ID is not present in a file, do not force changes.

## Task C — Normalize Mark Antony relationship type

In:

`incoming/western/mark-antony/relationships.jsonl`

If any relationship uses:

`relationship_type: sibling`

Change it to:

`relationship_type: family`

Do not change the evidence note unless needed for grammar.

## Task D — Soften Wu Kuan short description

In:

`incoming/chinese/wu-kuan/person_record.json`

The short description currently may say things like:

- 与沈周为挚友
- 文徵明之师
- close friend of Shen Zhou
- teacher of Wen Zhengming

These are stronger than the current claim statuses because several relevant claims were downgraded to `probable` or `needs_verification`.

Rewrite the short descriptions more cautiously.

Suggested Chinese wording:

`明代成化八年状元，官至礼部尚书。诗文与书法在苏州文人圈中有重要地位，后世常将其置于吴门文学与书法传统中讨论。与沈周、文徵明等苏州文人存在关联，但具体关系强度仍需更多原始材料核实。著有《匏翁家藏集》。`

Suggested English wording:

`Ming dynasty zhuangyuan of 1472 who rose to Minister of Rites. Wu Kuan held an important place in the Suzhou literati world and is later discussed in relation to Wu School literary and calligraphic traditions. His associations with Shen Zhou, Wen Zhengming, and other Suzhou figures require further source verification for relationship strength. Author of Collected Works of Paoweng.`

Make sure the summary does not state uncertain relationships as confirmed fact.

## Task E — Validate packages

Run:

```bash
python tools/validate_package.py incoming/chinese/wu-kuan
python tools/validate_package.py incoming/western/mark-antony
```

Fix any validation errors.

## Task F — Create cleanup note

Create:

`reviewed/staging/_small_cleanup_wu-kuan_mark-antony_v1.md`

Include:

1. Branch name
2. Files changed
3. Person ID changes applied
4. Relationship type changes applied
5. Wu Kuan summary wording changes
6. Validation results
7. Remaining known issues

Remaining known issues should mention:

- Wu Kuan still needs stronger sources for relationship strength and calligraphy claims.
- Mark Antony still needs exact passage references for several ancient claims.
- Visual media remains staging.

## Hard restrictions

Do not:

- collect new people
- merge PRs
- delete branches
- edit unrelated packages
- change project rules
- create dashboard/visual files
- promote anything to master

## Final response format

At the end, report only:

1. Branch name
2. Files changed
3. Validation result for Wu Kuan
4. Validation result for Mark Antony
5. PR link or branch link
6. Remaining known issues

Do not ask “should I continue?”.
