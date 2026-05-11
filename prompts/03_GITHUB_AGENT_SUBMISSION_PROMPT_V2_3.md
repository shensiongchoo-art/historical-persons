# Prompt: GitHub Agent Submission v2.5 — Non-Interactive MVP Mode

Use this prompt when an AI coding agent is asked to collect a person package and submit it to GitHub.

## Repository

Target repository:

`https://github.com/shensiongchoo-art/historical-persons`

## Non-interactive rule

Do not pause to ask the user whether to continue.
Do not stop after research notes.
Do not ask for approval before generating JSON/JSONL files.
Do not output only a progress message like “ready for Step 2”.

Complete the full collection package in one run using best effort.
If uncertain, mark the item as `needs_verification`, `probable`, `disputed`, `unknown`, `reception`, `legendary`, or `fictional` instead of asking a follow-up question.

## Required workflow

1. Pull the latest `main`.
2. Read:
   - `project-rules/MVP_COLLECTION_RULES_V2_5.md`
   - for Chinese figures: `prompts/01_COLLECT_CHINESE_PERSON_PROMPT_V2_5.md`
   - for Western figures: `prompts/02_COLLECT_WESTERN_PERSON_PROMPT_V2_5.md`
3. Create a new branch:
   - `collect/[person-slug]-v1`
4. Create a new person folder:
   - Chinese: `incoming/chinese/[person-slug]/`
   - Western: `incoming/western/[person-slug]/`
5. Generate all required files in that folder.
6. Run:
   - `python tools/validate_package.py incoming/chinese/[person-slug]`
   - or `python tools/validate_package.py incoming/western/[person-slug]`
7. Fix all validation errors.
8. Commit and push.
9. Open a Pull Request if possible. If PR creation is not available, commit to a collection branch and report the branch name.
10. Do not edit `reviewed/` or master data areas.

## v2.5 extra quality requirements

- One claim must contain one fact only.
- Summary wording must not be stronger than claim status.
- Reception labels must be written as reception, not direct fact.
- Do not use `friend`, `teacher`, `disciple`, `ally`, `influence`, or `founder` language unless direct evidence supports it.
- Prefer `probable_association`, `same_cultural_circle`, `documented_association`, `later_grouping_only`, or `reception_label` when evidence is indirect.
- Keep visual media in staging unless object ID, source holder, attribution, date, and rights/license are verified.

## Hard restrictions

- Do not put `references.jsonl` in the person root folder.
- Do not claim data is master-approved.
- Do not delete or rewrite other person folders.
- Do not create visual/dashboard files.
- Do not merge your own PR.
- Do not leave the package half-generated.

## Final response format

At the end, report only:

1. Target person
2. Branch name
3. Folder path
4. Files generated
5. Validation result
6. PR link or branch link
7. Known limitations

Do not ask “should I continue?”.
