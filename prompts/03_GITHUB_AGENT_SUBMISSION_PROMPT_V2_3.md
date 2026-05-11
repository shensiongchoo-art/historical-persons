# Prompt: GitHub Agent Submission v2.3

Use this prompt when an AI coding agent is asked to collect a person package and submit it to GitHub.

## Repository

Target repository:

`https://github.com/shensiongchoo-art/historical-persons`

## Required workflow

1. Pull the latest `main`.
2. Read:
   - `project-rules/MVP_COLLECTION_RULES_V2_3.md`
   - the correct prompt under `prompts/`
3. Create a new branch:
   - `collect/[person-slug]-v1`
4. Create a new person folder:
   - Chinese: `incoming/chinese/[person-slug]/`
   - Western: `incoming/western/[person-slug]/`
5. Generate required files.
6. Run `python tools/validate_package.py incoming/.../[person-slug]`.
7. Fix all validation errors.
8. Commit and push.
9. Open a Pull Request.
10. Do not edit `reviewed/` or master data areas.

## Hard restrictions

- Do not put `references.jsonl` in the person root folder.
- Do not claim data is master-approved.
- Do not delete or rewrite other person folders.
- Do not create visual/dashboard files.
- Do not merge your own PR.
