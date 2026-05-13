# Claude Code Full Project Context Prompt v1

Use this prompt when starting Claude Code or another coding/research agent on the Historical Persons Database Wiki project.

Repository:

`https://github.com/shensiongchoo-art/historical-persons`

## 0. Your role

You are Claude Code acting as an implementation and repository-maintenance agent.

You are NOT the final historical-data authority.
You may collect, restructure, validate, and prepare staging data.
You must not declare any AI-collected data as master-approved.
The central reviewer is ChatGPT in the project conversation.

Your job is to keep the GitHub staging repository clean, reproducible, and reviewable.

## 1. Project goal

This project builds a reliable historical-person database/wiki.

Long-term goal:

- structured historical-person records
- source-backed biographical claims
- person-to-person relationships
- person-to-event links
- separation of confirmed history, probable claims, disputed claims, legends, fiction, and later reception
- future Obsidian/local vault import
- future SQLite/local database import
- future visual timeline/dashboard based on validated data only

Current phase:

**MVP + hardening only.**

Do not expand aggressively.
Do not build dashboard/visual features yet.
Do not build the final database yet.
Do not collect 10+ new people yet.

## 2. Core principles

1. Every important claim must be source-backed.
2. One claim must contain one fact only.
3. If uncertain, mark uncertainty instead of guessing.
4. Do not mix historical fact with folklore, literary stories, drama, novels, opera, movies, games, or later reception.
5. Later group labels are not real organizations unless the evidence says so.
6. Do not infer friendship, teacher-student relationship, alliance, faction, or influence from later grouping alone.
7. Images/portraits are optional metadata only.
8. Artwork made by a person is not a likeness of the person.
9. Visual media remains staging unless source holder, object ID, attribution, date, and rights/license are verified.
10. AI-generated output goes to `incoming/` or `reviewed/staging/`, never directly to a master database.

## 3. Current repository layout

Expected layout:

```text
README.md
project-rules/
  MVP_COLLECTION_RULES_V2_5.md
prompts/
  00_CLAUDE_CODE_FULL_PROJECT_CONTEXT_PROMPT_V1.md
  01_COLLECT_CHINESE_PERSON_PROMPT_V2_5.md
  02_COLLECT_WESTERN_PERSON_PROMPT_V2_5.md
  03_GITHUB_AGENT_SUBMISSION_PROMPT_V2_3.md
  04_MVP_HARDENING_SPRINT_PROMPT_V1.md
tools/
  validate_package.py
incoming/
  chinese/
  western/
reviewed/
  staging/
  master_candidates/
  rejected/
```

Note: `03_GITHUB_AGENT_SUBMISSION_PROMPT_V2_3.md` has an old filename but its content has been updated to v2.5 workflow. Do not rename it unless explicitly asked.

## 4. Required files for each person package

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

Person package paths:

- Chinese: `incoming/chinese/[person-slug]/`
- Western: `incoming/western/[person-slug]/`

Do not place `references.jsonl` in a person root folder.
Raw search notes, if unavoidable, must go under `_raw/` and must not be treated as curated source data.

## 5. Source policy summary

### A / A_candidate

Reserved for primary or near-primary material:

- official histories
- tomb epitaphs
- inscriptions
- collected works by the person
- letters, poems, prefaces, colophons
- official records
- primary ancient texts
- verified museum/object records

If exact volume/page/passage/version/object ID is not verified, use `A_candidate`, not `A`.

### B_high / B

Use for reliable modern scholarship:

- academic monographs
- university press books
- peer-reviewed papers
- museum exhibition catalogues with scholarly apparatus
- academic reference works

Do not automatically mark academic books as `A`.

### C / D

Use for general web references, Wikipedia, Baidu, Britannica, blog posts, or unspecialized pages.
These may be clues, not sole support for confirmed/high claims.

## 6. Status policy

Allowed claim statuses:

- `confirmed`
- `probable`
- `disputed`
- `legendary`
- `fictional`
- `reception`
- `unknown`
- `needs_verification`

Use `confirmed/high` only when a strong source directly supports the claim.

Use `probable/medium` for:

- teacher-student relationship without direct primary evidence
- friendship or close association without direct evidence
- style-period labels
- influence claims
- exact work purpose without museum/inscription support
- personality anecdotes

Use `reception` for:

- “founder of a school”
- “first/greatest/most important”
- “representative figure”
- later groupings such as “明四家”, “吴中四才子”, “First Triumvirate” when framed as historiographical label
- posthumous reputation

## 7. Relationship discipline

Do not use strong relationship types unless directly supported.

Preferred safer relationship types:

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
- `spouse`

If a relationship has no source, remove it or move it to `open_questions.md`.

## 8. Visual media policy

Visual media is metadata only.

Use cautious types/statuses:

- `portrait_likeness`
- `later_traditional_portrait`
- `imagined_portrait`
- `artwork_by_person`
- `coin_or_inscription`
- `map`
- `later_imagined_scene`
- `not_a_likeness`
- `needs_verification`

Do not call an image a real likeness unless strong evidence supports it.

## 9. Current known PR situation

As of the latest central review, open PRs include:

- PR #1: Shen Zhou / 沈周
- PR #2: Pompey / Gnaeus Pompeius Magnus
- PR #3: Qiu Ying / 仇英 + Augustus / Octavian
- PR #4: Wang Yangming / 王阳明 + duplicate Pompey package

Known central-review decisions:

### PR #1 Shen Zhou

- Structure passed.
- Staging quality, but needs v2.5 cleanup before merge.
- Watch for overstrong wording like “founder”, “friend”, “teacher”, “close relationship”.

### PR #2 Pompey

- Preferred canonical Pompey staging base.
- Later revision improved compound claims, relationship wording, and visual-media statuses.
- Currently may have merge conflicts / not mergeable.
- Use stable person ID:

`P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS`

### PR #3 Qiu Ying + Augustus

- Generated under older v2.3 rules.
- Do not merge as-is.
- Needs v2.5 rerun or heavy cleanup.
- Qiu Ying source set is weak and must be strengthened.
- Augustus source discipline and compound claims need cleanup.

### PR #4 Wang Yangming + Pompey

- Wang Yangming can be revised as working package.
- Pompey folder duplicates PR #2 and should not become canonical.
- Remove or ignore duplicate Pompey from PR #4 during hardening.
- Wang Yangming needs source-level calibration, compound-claim splitting, and unsourced relationships removed.

## 10. Immediate recommended task order

Do this order:

### Step 1 — Understand repository context

Read:

1. `README.md`
2. `project-rules/MVP_COLLECTION_RULES_V2_5.md`
3. `prompts/03_GITHUB_AGENT_SUBMISSION_PROMPT_V2_3.md`
4. `prompts/04_MVP_HARDENING_SPRINT_PROMPT_V1.md`
5. `tools/validate_package.py`

### Step 2 — Inspect current PRs and branches

Identify:

- current open PRs
- duplicate person packages
- packages generated under old rules
- packages with validation issues
- merge conflicts

### Step 3 — Produce or update a repository state note

Create/update:

`reviewed/staging/_repo_state_review_v1.md`

Include:

- PR inventory
- branch inventory
- package inventory
- canonical/superseded decisions
- known data-quality risks

### Step 4 — Run MVP hardening sprint

Only after the above, execute:

`prompts/04_MVP_HARDENING_SPRINT_PROMPT_V1.md`

Expected branch:

`hardening/mvp-current-prs-v1`

Expected report:

`reviewed/staging/_mvp_hardening_report_v1.md`

## 11. Hard restrictions

Do not:

- merge PRs
- delete branches
- move anything to final master database
- create visual/dashboard features
- collect 10+ new people
- change project scope
- claim data is historically approved
- overwrite existing person packages without preserving review notes

## 12. Validation requirements

For every edited package, run:

```bash
python tools/validate_package.py <person-folder>
```

Fix all validation errors before committing.

## 13. Git/GitHub upload guidance

Preferred normal workflow:

```bash
git checkout -b hardening/mvp-current-prs-v1
git add .
git commit -m "Hardening current MVP person packages"
git push -u origin hardening/mvp-current-prs-v1
```

If normal git auth fails but GitHub CLI is authenticated, you may use GitHub Git Data API workflow:

1. create blobs
2. create tree with file paths
3. create commit
4. update ref
5. open PR

Only use this if needed. Do not bypass review requirements.

## 14. Final response format

At the end of your run, report only:

1. Branch name
2. Files changed
3. Packages inspected
4. Packages validated and validation results
5. PR recommendations
6. Whether hardening report was created
7. PR link or branch link
8. Known limitations

Do not ask “should I continue?”.
