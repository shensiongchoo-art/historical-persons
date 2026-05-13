# Prompt: Next Step — PR Triage After MVP Hardening v1

Use this prompt with Claude Code / Codex after PR #8 hardening sprint has been merged.

Repository:

`https://github.com/shensiongchoo-art/historical-persons`

## Objective

Move the repository forward after the merged MVP hardening sprint.

Do NOT collect new people in this task.
Do NOT build visual/dashboard features.
Do NOT promote anything to master.
Do NOT rewrite project rules unless explicitly asked.

Focus on:

1. Closing or marking superseded PRs.
2. Verifying PR #6 source reports are clean and reports-only.
3. Reviewing PR #7 Wu Kuan + Mark Antony for next cleanup needs.
4. Creating a clear next-action report.

## Required reading

Before making changes, read:

1. `prompts/00_CLAUDE_CODE_FULL_PROJECT_CONTEXT_PROMPT_V1.md`
2. `project-rules/MVP_COLLECTION_RULES_V2_5.md`
3. `reviewed/staging/_repo_state_review_v1.md`
4. `reviewed/staging/_mvp_hardening_report_v1.md`
5. PR #6 and PR #7 metadata and changed files

## Branch

Create a branch:

`maintenance/pr-triage-after-hardening-v1`

Use this branch only for repo-status notes or triage reports.

## Tasks

### Task 1 — Confirm current PR inventory

Inspect open PRs:

- PR #1 Shen Zhou
- PR #2 old/partial Pompey
- PR #3 old Qiu Ying + Augustus v2.3
- PR #4 Wang Yangming + Pompey
- PR #5 Qiu Ying + Augustus v2.5
- PR #6 source verification reports
- PR #7 Wu Kuan + Mark Antony

Create/update:

`reviewed/staging/_open_pr_triage_after_hardening_v1.md`

Include:

- PR number
- title
- branch
- status
- whether superseded
- recommended action
- reason

### Task 2 — Close superseded PRs if safe

If GitHub permissions allow, add a short explanatory comment and close:

#### PR #2
Reason:
- Superseded by hardened canonical Pompey package from PR #4 / merged hardening state.
- Old/partial package should not be merged.

Suggested comment:

`Closing as superseded by the MVP hardening sprint. Pompey canonical staging package is now represented in the hardened v2.5 package state; this older partial PR should not be merged.`

#### PR #3
Reason:
- Superseded by PR #5 Qiu Ying + Augustus v2.5.
- PR #3 was generated under older v2.3 rules.

Suggested comment:

`Closing as superseded by PR #5 and the merged MVP hardening sprint. This v2.3 package is retained only as historical context and should not be merged.`

If you cannot close PRs, note this in the triage report.

### Task 3 — Check PR #6 source verification reports

Verify PR #6 is reports-only.

It should only change files under:

`reviewed/staging/source_verification/`

Expected reports:

- `pompey_source_verification.md`
- `wang-yangming_source_verification.md`
- `qiu-ying_source_verification.md`
- `augustus_source_verification.md`

If PR #6 includes any `incoming/` package changes, report it as not ready to merge.

If PR #6 is clean reports-only, mark it:

`recommended_action: merge_after_central_reviewer_approval`

Do not merge PR #6 yourself unless explicitly instructed.

### Task 4 — Check PR #7 Wu Kuan + Mark Antony

Inspect PR #7 package structure and changed files.

Do not fully rewrite the packages in this task.

Create a short review note:

`reviewed/staging/_pr7_wu-kuan_mark-antony_initial_review.md`

Include:

#### Wu Kuan / 吴宽
Check for:
- source levels too high
- Baidu or weak source overuse
- compound claims
- overstrong relationship words such as “挚友”
- claims needing downgrade to probable / needs_verification

#### Mark Antony / Marcus Antonius
Check for:
- source levels too high for Plutarch/Appian/Cassius Dio/Suetonius
- compound claims
- person_id naming consistency
- claims shaped by Augustan propaganda
- Cleopatra/Antony reception separated from history

Do not edit PR #7 files unless the fix is trivial and clearly safe.

### Task 5 — Produce next-step recommendation

Create/update:

`reviewed/staging/_next_actions_after_hardening_v1.md`

Recommended structure:

1. Immediate actions
2. PRs to close
3. PRs ready for central review
4. PRs needing cleanup
5. Packages ready for staging review
6. Packages needing source verification
7. Whether to resume collecting new people

Expected recommendation:

- Close PR #2 and PR #3 if possible.
- Keep PR #6 as source verification track; merge only if reports-only.
- Review/cleanup PR #7 next.
- Do not collect new people until PR #7 is reviewed.
- After PR #7 review, next new-person batch can be Li Dongyang, Wang Ao, Cleopatra VII, Marcus Agrippa.

## Validation

If you edit any person package, run:

`python tools/validate_package.py <person-folder>`

If you only create review notes and triage reports, validation is not required.

## Hard restrictions

- Do not merge PRs.
- Do not delete branches.
- Do not collect new people.
- Do not change project rules.
- Do not create dashboard/visual files.
- Do not promote anything to master.

## Final response format

At the end, report only:

1. Branch name
2. PRs inspected
3. PRs closed, if any
4. Files created/updated
5. PR #6 reports-only status
6. PR #7 initial review result
7. Next recommended action
8. PR link or branch link

Do not ask “should I continue?”.
