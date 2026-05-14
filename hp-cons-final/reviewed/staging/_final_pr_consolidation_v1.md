# Final PR Consolidation Report v1

**Date**: 2026-05-14
**Repository**: shensiongchoo-art/historical-persons
**Context**: Post-PR8/PR9 hardening — PR consolidation and closure sweep
**Branch**: maintenance/final-pr-consolidation-v1

---

## 1. Current Open PR Inventory

Two PRs remain open as of 2026-05-14:

| PR | Title | Branch | Status |
|----|-------|--------|--------|
| #13 | step1.2: MVP inventory + 7 central reviews | step1.2/staging-consolidation-central-reviews-v1-fresh | OPEN, MERGEABLE |
| #14 | post-PR9 cleanup: repo status, PR #5 review, next actions | maintenance/post-pr9-cleanup-v1 | OPEN, MERGEABLE |

All other PRs (#1–#12) are in terminal state (CLOSED or MERGED).

---

## 2. Complete PR Inventory and Disposition

### 2.1 Collect/Draft PRs — All CLOSED

| PR | Title | Superseded By | Status |
|----|-------|---------------|--------|
| #1 | Add Shen Zhou (沈周) v1 | #8 (hardening, included Shen Zhou) | CLOSED |
| #2 | Pompey MVP collection v1 | #4 then #8 | CLOSED |
| #3 | Qiu Ying + Augustus v1 | #5 (v2.5) then #8 | CLOSED |
| #4 | Wang Yangming + Pompey v1 | #8 | CLOSED |
| #5 | Qiu Ying + Augustus v2.5 | #8 | CLOSED |
| #7 | Wu Kuan + Mark Antony v2.5 | #9 (normalized to v2.5) | CLOSED |

All six collect/drafts are superseded by hardening PRs #8 and #9. Already in terminal state.

### 2.2 Merged PRs — Source Verifications and Cleanups

| PR | Title | Scope | Status |
|----|-------|-------|--------|
| #6 | Source verification reports v1 (4 persons) | Reports-only, reviewed/staging/ | MERGED |
| #8 | Hardening sprint v1: normalize 5 packages to v2.5 | Package hardening + staging reports | MERGED |
| #9 | Hardening: normalize PR #7 Wu Kuan + Mark Antony to v2.5 | Package hardening + staging report | MERGED |
| #10 | Backfill source refs from sprint reports v2 | sources.jsonl only (Pompey, Wang Yangming, Qiu Ying, Augustus) | MERGED |
| #11 | Cleanup: standardize person_id, fix relationship type, soften Wu Kuan | Every JSONL/JSON in wu-kuan + mark-antony (17 files) | MERGED |
| #12 | Wang Yangming page-ref corrections and SRC018 caveat | wang-yangming claims.jsonl + sources.jsonl | MERGED |

### 2.3 Open PRs — Reports-Only

| PR | Title | Files | Scope | Status |
|----|-------|-------|-------|--------|
| #13 | MVP inventory + 7 central reviews | 8 files under reviewed/staging/ | Reports-only, no incoming/ changes | OPEN, MERGEABLE |
| #14 | Post-PR9 cleanup: repo status, PR #5 review, next actions | 3 files under reviewed/staging/ | Reports-only, no incoming/ changes | OPEN, MERGEABLE |

---

## 3. PR Supersession Analysis

### 3.1 PR #1, #4, #5, #7 — Already Superseded and Closed

All four collect/draft PRs are superseded and already CLOSED. No further action needed.

- **PR #1** (Shen Zhou v1): Superseded by PR #8, which normalized Shen Zhou to v2.5 alongside four other packages.
- **PR #4** (Wang Yangming + Pompey v1): Superseded by PR #8, which hardened both packages to v2.5.
- **PR #5** (Qiu Ying + Augustus v2.5): Superseded by PR #8, which included both packages in the hardening sprint.
- **PR #7** (Wu Kuan + Mark Antony v2.5): Superseded by PR #9, which normalized both packages to v2.5.

All four are already CLOSED. No need to close them again — they are in terminal state.

### 3.2 PR #11 vs PR #9 — NOT Superseded

**PR #11 is not superseded by PR #9.** The timeline is:

1. PR #9 merged (2026-05-13 13:55 UTC): Created Wu Kuan + Mark Antony packages — 23 files ADDED (all net-new in incoming/).
2. PR #11 merged (2026-05-13 14:33 UTC): Modified 17 files across both packages — standardizing person_id format, fixing relationship type classification, softening Wu Kuan biographical description text.

PR #11 is a **post-hardening cleanup** building on PR #9's output. Every file PR #9 ADDED, PR #11 MODIFIED. The changes are additive (normalization, not replacement). Both are safely merged to main.

### 3.3 PR #2, #3 — Already Closed

Both are superseded collection drafts. Already CLOSED. No action needed.

---

## 4. Reports-Only PRs — Safe to Merge

Both open PRs are **reports-only** with zero modifications to `incoming/`:

### PR #14 — Merge First
- **3 files**: `_post_pr9_repo_status_v1.md`, `_pr5_qiu-ying_augustus_initial_review.md`, `_next_actions_post_pr9_v1.md`
- **Additions**: 348 lines, all under `reviewed/staging/`
- **Content**: Validates that PR #8 and #9 hardening is complete, all 7 packages pass v2.5 validation, confirms PR #5's Qiu Ying and Augustus packages are ready_for_staging_merge, and recommends next batch (Li Dongyang + Wang Ao / Cleopatra VII + Marcus Agrippa).
- **Risk**: None. Zero package changes.

### PR #13 — Merge Second
- **8 files**: `_current_mvp_inventory.md` + 7 `{person}/central_review.md`
- **Additions**: 1,461 lines, all under `reviewed/staging/`
- **Content**: Cross-package inventory with metrics for all 7 MVP persons. Each central review covers 13 sections: identity, sources, claims, relationships, events, works, compound claims, schema compliance, source calibration, confidence assessment, cross-package dependencies, visual media, recommended actions.
- **Risk**: None. Zero package changes.

---

## 5. Source-Fix PRs — Review Status

| PR | Type | Files Touched | Central Review Needed? |
|----|------|---------------|----------------------|
| #10 | Source backfill | sources.jsonl only (4 persons) | Already merged; changes were ref-level swaps |
| #11 | Post-hardening cleanup | All JSONL files in wu-kuan + mark-antony | Already merged; person_id standardization, relationship type fix |
| #12 | Page-ref correction | wang-yangming claims.jsonl + sources.jsonl | Already merged; SRC018 caveat + 2 claim corrections |

All three source-fix PRs are MERGED. Central review occurred during or before merge. No further review needed.

---

## 6. Recommended Exact Sequence

### Phase 1 — Merge Reports-Only (Now)

| Step | Action | Rationale |
|------|--------|-----------|
| 1 | **Merge PR #14** | Validates repo state post-PR9. Confirms all 7 packages pass validation, PR #5 content rated ready_for_staging_merge. Establishes baseline for PR #13 review context. |
| 2 | **Merge PR #13** | Adds 7 central reviews + cross-package inventory. All reports-only, no package changes. |

### Phase 2 — Verify (After Merges)

| Step | Action | Rationale |
|------|--------|-----------|
| 3 | Confirm main branch has all 7 v2.5 packages | PR #8 (5 persons) + PR #9 (2 persons) + PR #11 (cleanup) + PR #10/#12 (verification) |
| 4 | Verify reviewed/staging/ directory completeness | Should have: inventory, 7 central reviews, PR5 review, post-PR9 status, next actions, PR7 hardening plan |

### Phase 3 — No Further Action

| Step | Action | Rationale |
|------|--------|-----------|
| 5 | **Do NOT close any PRs** | #1–#5, #7 already CLOSED. #6, #8–#12 already MERGED. No PRs to close. |
| 6 | **Do NOT promote to master** | Branch is `main`. No `master` exists. Current main is the canonical branch. |

---

## 7. Summary

| Category | Count | Status |
|----------|-------|--------|
| Closed (superseded collects) | 6 | #1, #2, #3, #4, #5, #7 — terminal |
| Merged (hardening) | 2 | #8, #9 — terminal |
| Merged (verification) | 2 | #10, #12 — terminal |
| Merged (cleanup) | 1 | #11 — terminal, NOT superseded by #9 |
| Merged (reports-only) | 1 | #6 — terminal |
| Open (reports-only, safe to merge) | 2 | #13, #14 — MERGEABLE |

**Bottom line**: The PR landscape is clean. All collect/draft PRs are closed. All hardening, verification, and cleanup PRs are merged. The only remaining work is to merge the two reports-only PRs (#14 then #13) to complete the staging documentation.

**No edits to historical data needed. No new person collection. No branch promotion to master.**
