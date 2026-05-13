# Prompt: MVP Hardening Sprint v1

You are an AI coding/research agent working on the Historical Persons Database Wiki MVP.

Repository:

`https://github.com/shensiongchoo-art/historical-persons`

## Objective

Do NOT collect many new people yet.
This sprint is for hardening the MVP pipeline and cleaning current staging packages so the project can safely scale later.

Main goals:

1. Resolve overlap/conflict between open PRs.
2. Keep only one canonical staging package per person.
3. Upgrade selected packages to MVP v2.5 quality.
4. Do not merge anything yourself.
5. Produce a clear hardening report for central review.

## Non-interactive execution rule

Do not pause to ask whether to continue.
Do not stop after planning notes.
Do not ask for approval before editing files.
Complete the sprint using best effort.
If uncertain, mark the item as `needs_verification`, `probable`, `disputed`, `unknown`, `reception`, `legendary`, or `fictional` instead of asking a follow-up question.

## Read first

Before editing, read:

1. `project-rules/MVP_COLLECTION_RULES_V2_5.md`
2. `prompts/01_COLLECT_CHINESE_PERSON_PROMPT_V2_5.md`
3. `prompts/02_COLLECT_WESTERN_PERSON_PROMPT_V2_5.md`
4. `prompts/03_GITHUB_AGENT_SUBMISSION_PROMPT_V2_3.md`
5. `tools/validate_package.py`

## Branch

Create a new branch:

`hardening/mvp-current-prs-v1`

Do not work directly on `main`.
Do not merge any PR.

## Current PR context to inspect

Inspect current open PRs:

- PR #1: Shen Zhou / 沈周
- PR #2: Pompey / Gnaeus Pompeius Magnus
- PR #3: Qiu Ying / 仇英 + Augustus / Octavian
- PR #4: Wang Yangming / 王阳明 + Pompey duplicate package

Use GitHub PR metadata and changed files if available.

## Canonical decision for this sprint

Use these decisions unless the repository state has changed substantially:

### Pompey

- Treat PR #2 as the preferred Pompey staging base because it has already incorporated central-review fixes.
- PR #4 also contains a Pompey folder, but it should NOT become the canonical Pompey package.
- Avoid duplicate Pompey packages in the same target branch.
- Standardize Pompey person ID to:

`P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS`

### Wang Yangming

- Keep Wang Yangming from PR #4 as the working package, but revise it to v2.5 quality.

### Qiu Ying and Augustus

- PR #3 was generated using older v2.3 rules.
- Do not merge it as-is.
- Either revise it to v2.5 quality or create a fresh v2.5 replacement branch/package for Qiu Ying and Augustus.

### Shen Zhou

- Keep PR #1 as staging reference, but do not merge unless it meets v2.5 cleanup expectations.

## Required output of this sprint

Create a hardening report:

`reviewed/staging/_mvp_hardening_report_v1.md`

The report must include:

1. Current PR inventory.
2. Canonical package decision per person.
3. Which PRs should be kept, revised, closed, or superseded.
4. Which person packages are staging-quality.
5. Which person packages need rerun.
6. Known data-quality issues by person.
7. Recommended next action for central reviewer.

## Package cleanup tasks

### A. Wang Yangming package cleanup

Target folder if present:

`incoming/chinese/wang-yangming/`

Required fixes:

1. Source level calibration:
   - `明史·王守仁传` should be `A_candidate` until exact volume/passage/version is verified.
   - `传习录`, `大学问`, `王文成公全书` may be `A_candidate` until exact edition/passage is verified.
   - Dictionary of Ming Biography, Cambridge History, Stanford Encyclopedia, IEP, Needham should generally be `B_high`, not `A`.

2. Split compound claims:
   - Name/title claim must be split into separate claims: birth name, courtesy name, art name/common name, posthumous title, noble title.
   - Ning Prince rebellion claim must be split into outbreak, mobilization, battle, capture, aftermath.
   - Folangji cannon and psychological warfare must be separate claims.
   - Tianquan Bridge event and Four-Sentence Teaching text must be separate claims.

3. Relationship cleanup:
   - Remove or source Tang Yin and Zhu Yunming relationships.
   - If there is no direct evidence, do not keep them as person relationships. Use broad same-period context only if explicitly sourced.

4. Philosophical/reception claims:
   - `陆王心学`, `真三不朽`, Japanese/Korean Yangmingism transmission, and later reception should be marked `reception`, `scholarly_interpretation`, `probable`, or `needs_verification` as appropriate.

### B. Pompey package cleanup

Target folder if using PR #2 material:

`incoming/western/gnaeus-pompeius-magnus/`

Required fixes:

1. Use stable person_id:

`P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS`

2. Keep or improve PR #2 revisions:
   - compound claims split
   - `Magnus` title origin marked probable/disputed where needed
   - hostile nickname marked reception/probable
   - relationship wording for Cicero and Cato kept conservative
   - visual media status corrected

3. Add exact passage references for high-impact ancient-source claims where possible.

4. If exact passage cannot be verified, keep `needs_verification` and note it in `open_questions.md`.

5. Do not keep duplicate Pompey package from PR #4 in the same final branch.

### C. Qiu Ying package cleanup or rerun

Target folder:

`incoming/chinese/qiu-ying/`

Required fixes if revising instead of rerunning:

1. Upgrade to v2.5 source discipline.
2. Avoid relying on Wikipedia as a source for confirmed claims.
3. Replace vague `仇英研究文献` style sources with real bibliographic sources.
4. Add or mark as needed:
   - 明清画史笔记 such as `无声诗史`, `明画录`, `图绘宝鉴续编` where verifiable.
   - museum collection records for major works.
   - Ellen Johnston Laing or equivalent scholarship with complete bibliographic fields.
5. Works must distinguish verified works, attributed works, disputed works, and later copies.
6. Keep birth/death approximate unless strong source supports exact dates.

### D. Augustus package cleanup or rerun

Target folder:

`incoming/western/augustus-octavian/`

Required fixes if revising instead of rerunning:

1. Upgrade to v2.5 source discipline.
2. Do not use Wikipedia as source_ids for all claims.
3. Split compound claims:
   - name stages
   - titles
   - marriages
   - adoption/succession arrangements
   - Actium / settlement / principate claims
4. Use source-specific caveats:
   - `Res Gestae` is Augustan self-presentation/propaganda.
   - Suetonius is anecdotal and later.
   - Cassius Dio is later and interpretive.
5. Treat “first Roman emperor” as reception/historiographical simplification with constitutional nuance.
6. Separate historical fact from Augustan propaganda and later imperial reception.

## Validation requirements

For every package edited or generated, run:

`python tools/validate_package.py <person-folder>`

Fix all validation errors.

No package may contain root-level `references.jsonl`.
No JSON/JSONL file may fail parsing.
No confirmed/high claim may rely only on Wikipedia/Baidu/Britannica.
No person relationship may have empty `source_ids` unless it is removed or moved to an open question.

## Do not do these

- Do not merge PRs.
- Do not create visual dashboards.
- Do not move data into a final master database.
- Do not expand to 10 new people.
- Do not rewrite project rules unless explicitly asked.
- Do not delete other branches.

## Final response format

At the end, report only:

1. Branch name.
2. Files changed.
3. Packages validated and validation results.
4. Which PRs should be kept/revised/closed/superseded.
5. Whether Wang Yangming, Pompey, Qiu Ying, Augustus are staging-ready.
6. Known limitations.
7. Pull request link or branch link.

Do not ask “should I continue?”.
