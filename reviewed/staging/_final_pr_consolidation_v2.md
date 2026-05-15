# Final PR Consolidation Report (v2)

**Date:** 2026-05-15
**Context:** All 17 historical PRs have been audited. PR #8 through #15 have all merged into `main`. 7 MVP packages (Qiu Ying, Shen Zhou, Wang Yangming, Wu Kuan, Augustus, Pompey, Mark Antony) are present and validated on `main`. The only remaining open PR is #16 (batch1-core-network-v3: 8 new persons).

This report supersedes `_final_pr_consolidation_v1.md` (PR #15, 2026-05-14), which was correct at the time but predated the merge of PR #13 and #14 and the appearance of PR #17.

---

## Complete PR Inventory (#1-#17)

| PR | Title | State | Type | Superseded By | In Main? | Action |
|----|-------|-------|------|---------------|----------|--------|
| #1 | Shen Zhou v1 | CLOSED | data | #8 | Yes (via #8) | No action |
| #2 | Pompey solo v1 | CLOSED | data | #4, #8 | Yes (via #8) | No action |
| #3 | Qiu Ying + Augustus v1 | CLOSED | data | #5, #8 | Yes (via #8) | No action |
| #4 | Wang Yangming + Pompey | CLOSED | data | #8 | Yes (via #8) | No action |
| #5 | Qiu Ying + Augustus v2.5 | CLOSED | data | #8 | Yes (via #8) | No action |
| #6 | Source verification v1 | MERGED | reports | -- | Yes | No action |
| #7 | Wu Kuan + Mark Antony | CLOSED | data | #9 | Yes (via #9) | No action |
| #8 | Hardening sprint v1 | MERGED | data | -- | Yes | No action |
| #9 | Wu Kuan + Mark Antony norm | MERGED | data | -- | Yes | No action |
| #10 | Backfill source refs v2 | MERGED | data | -- | Yes | No action |
| #11 | Cleanup person_id + rels | MERGED | data | -- | Yes | No action |
| #12 | Wang Yangming page-ref fix | MERGED | data | -- | Yes | No action |
| #13 | MVP inventory + 7 reviews | MERGED | reports | -- | Yes | No action |
| #14 | Post-PR9 cleanup status | MERGED | reports | -- | Yes | No action |
| #15 | Final PR consolidation v1 | MERGED | reports | -- | Yes | No action |
| #16 | Batch 1 core network (8 ppl) | OPEN | data | -- | No | **Review** |
| #17 | Duplicate of #9 normalization | MERGED | data | #9 | Yes (via #9) | No action |

---

## Per-PR Analysis

### PR #1 -- Shen Zhou v1 (CLOSED)
- **Still needed?** No. Superseded by PR #8, which included Shen Zhou with full v2.5 normalization (relationship type remap, overstrong wording removal).
- **Recommendation:** Permanently closed. No further action.

### PR #2 -- Pompey solo v1 (CLOSED)
- **Still needed?** No. Partial package (2 files only). Pompey canonical is from PR #4, normalized in PR #8, source-verified in PR #10/#12.
- **Recommendation:** Permanently closed. No further action.

### PR #3 -- Qiu Ying + Augustus v1 (CLOSED)
- **Still needed?** No. v2.3 schema. Superseded by PR #5 (v2.5) then PR #8 (hardening).
- **Recommendation:** Permanently closed. No further action.

### PR #4 -- Wang Yangming + Pompey (CLOSED)
- **Still needed?** No. Both packages normalized in PR #8 (JSON fix, relationship remap, person_id fix). Source verification applied in PR #10 and #12.
- **Recommendation:** Permanently closed. No further action.

### PR #5 -- Qiu Ying + Augustus v2.5 (CLOSED)
- **Still needed?** No. Superseded by PR #8 (full normalization: v2.3 to v2.5 schema, person_id fix, bibliographic_hint removal). PR #14's review confirms both packages as "ready_for_staging_merge" -- the review remains valid archived documentation.
- **Recommendation:** Permanently closed. No further action.

### PR #6 -- Source verification v1 (MERGED)
- **Still needed?** Already merged. Source verification reports for Pompey, Wang Yangming, Qiu Ying, Augustus at `reviewed/staging/source_verification/`.
- **Recommendation:** No action.

### PR #7 -- Wu Kuan + Mark Antony (CLOSED)
- **Still needed?** No. Superseded by PR #9, which applied full v2.5 normalization (schema conversion, source calibration, claims splitting). Then PR #11 cleaned up person_ids and relationship types.
- **Recommendation:** Permanently closed. No further action.

### PR #8 -- Hardening sprint v1 (MERGED)
- **Still needed?** Already merged. Core hardening for 5 packages: Shen Zhou, Wang Yangming, Pompey, Qiu Ying, Augustus. All pass validation on main.
- **Recommendation:** No action.

### PR #9 -- Wu Kuan + Mark Antony normalization (MERGED)
- **Still needed?** Already merged. Normalized both packages to v2.5 schema. All pass validation on main.
- **Note:** PR #17 was a subsequent commit that re-applied these same changes (same branch, same files). Now merged. No conflict.
- **Recommendation:** No action.

### PR #10 -- Source refs backfill v2 (MERGED)
- **Still needed?** Already merged. Data-changing: added page/edition/Loeb references to 4 packages (Pompey, Wang Yangming, Qiu Ying, Augustus). Stripped bibliographic_hint legacy field.
- **In main?** Yes. All source updates present.
- **Recommendation:** No action.

### PR #11 -- Cleanup person_id + relationship type (MERGED)
- **Still needed?** Already merged. Data-changing: standardized Wu Kuan person_id (P_CHN_MING_002_WU_KUAN to P_CHN_MING_WU_KUAN) across 8 files; Mark Antony person_id standardized; relationship type fixed (sibling to family); Wu Kuan description softened.
- **In main?** Yes. All changes present on main.
- **Recommendation:** No action.

### PR #12 -- Wang Yangming page-ref corrections (MERGED)
- **Still needed?** Already merged. Data-changing: SRC017 page range corrected (33-72 to 233-263, verified via Crossref). SRC018 caveat added (book does NOT substantiate Saigo/Takasugi Yangmingist claim). C026 confidence downgraded to low.
- **In main?** Yes. All changes present on main.
- **Recommendation:** No action.

### PR #13 -- MVP inventory + 7 central reviews (MERGED)
- **Still needed?** Already merged. Reports-only. Added `_current_mvp_inventory.md` + 7 per-person `central_review.md` files (13-section structured reviews).
- **In main?** Yes. All 8 review files present at `reviewed/staging/`.
- **Recommendation:** No action.

### PR #14 -- Post-PR9 cleanup status (MERGED)
- **Still needed?** Already merged. Reports-only: `_post_pr9_repo_status_v1.md` (13-PR inventory), `_pr5_qiu-ying_augustus_initial_review.md` (PR #5 quality assessment), `_next_actions_post_pr9_v1.md` (roadmap).
- **In main?** Yes. All 3 status files present.
- **Recommendation:** No action.

### PR #15 -- Final PR consolidation v1 (MERGED)
- **Still needed?** Already merged. Reports-only. Correct at the time (2026-05-14): identified PR #13 and #14 as merge-ready, all other PRs resolved.
- **In main?** Yes.
- **Recommendation:** No action. This v2 report supersedes it.

### PR #16 -- Batch 1 core network: 8 persons (OPEN)
- **Still needed?** Yes. Adds 8 new persons (115 claims, 56 sources) to the network.
- **Data-changing.** 88 new package files across 8 person folders. All pass `validate_package.py`.
- **Persons:** Tang Yin, Wen Zhengming, Zhu Yunming, Xu Zhenqing (Chinese); Julius Caesar, Cicero, Cleopatra VII, Marcus Agrippa (Western).
- **Review status:** Initial review (`_batch1_pr16_initial_review.md`) exists on branch. Recommendation is CONDITIONAL APPROVAL -- Zhu Yunming needs 1-2 additional non-D sources.
- **Safety:** 7/8 packages are ready. Only Zhu Yunming is thin on sources (5 total, only 3 non-D).
- **Merge conflict risk:** Branch is based on main. No conflicts with current main.
- **Recommendation:** Address Zhu Yunming source gap (1-2 additional sources), re-validate, then merge. Do NOT close.

### PR #17 -- Duplicate of PR #9 normalization (MERGED)
- **Still needed?** Already merged. Same changes as PR #9 (Wu Kuan + Mark Antony normalization). Identical branch.
- **In main?** Yes. Content already present via PR #9.
- **Recommendation:** No action. This was effectively a re-push of PR #9 changes.

---

## Current Main State (7 packages, all validated)

```
incoming/
├── chinese/
│   ├── qiu-ying/              (11 files, VALIDATION PASSED)
│   ├── shen-zhou/             (11 files, VALIDATION PASSED)
│   ├── wang-yangming/         (11 files, VALIDATION PASSED)
│   └── wu-kuan/               (11 files, VALIDATION PASSED)
└── western/
    ├── augustus-octavian/      (11 files, VALIDATION PASSED)
    ├── gnaeus-pompeius-magnus/ (11 files, VALIDATION PASSED)
    └── mark-antony/            (11 files, VALIDATION PASSED)

reviewed/staging/
├── _current_mvp_inventory.md
├── _final_pr_consolidation_v1.md
├── _mvp_hardening_report_v1.md
├── _next_actions_post_pr9_v1.md
├── _post_pr9_repo_status_v1.md
├── _pr5_qiu-ying_augustus_initial_review.md
├── _pr7_hardening_plan_v1.md
├── _repo_state_review_v1.md
├── augustus-octavian/central_review.md
├── gnaeus-pompeius-magnus/central_review.md
├── mark-antony/central_review.md
├── qiu-ying/central_review.md
├── shen-zhou/central_review.md
├── wang-yangming/central_review.md
├── wu-kuan/central_review.md
└── source_verification/
    ├── augustus_source_verification.md
    ├── pompey_source_verification.md
    ├── qiu-ying_source_verification.md
    └── wang-yangming_source_verification.md
```

---

## Branch Cleanup Candidates

The following remote branches belong to closed/merged PRs and are candidates for deletion:

| Branch | PR | Status | Safe to Delete? |
|--------|-----|--------|------------------|
| `collect/shen-zhou-v1` | #1 | CLOSED | Yes |
| `collect/gnaeus-pompeius-magnus-v1` | #2 | CLOSED | Yes |
| `collect/qiu-ying-and-augustus-v1` | #3 | CLOSED | Yes |
| `collect/wang-yangming-and-pompey-v1` | #4 | CLOSED | Yes |
| `collect/qiu-ying-and-augustus-v2-5` | #5 | CLOSED | Yes |
| `verification/source-reports-v1` | #6 | MERGED | Yes |
| `collect/wu-kuan-and-mark-antony-v1` | #7 | CLOSED | Yes |
| `hardening/mvp-current-prs-v1` | #8 | MERGED | Yes |
| `hardening/pr7-wu-kuan-mark-antony-v1` | #9 + #17 | MERGED | Yes |
| `verification/source-reports-v2` | #10 | MERGED | Yes |
| `maintenance/cleanup-wu-kuan-mark-antony-v1` | #11 | MERGED | Yes |
| `verification/wang-yangming-page-refs-v3` | #12 | MERGED | Yes |
| `step1.2/staging-consolidation-small-expansion-v1` | #13 | MERGED | Yes |
| `maintenance/post-pr9-cleanup-v1` | #14 | MERGED | Yes |
| `consolidation/final-pr-consolidation-v1` | #15 | MERGED | Yes |
| `maintenance/pr-triage-after-hardening-v1` | (none) | -- | Yes |
| `collect/batch1-core-network-v1` | (superseded) | CLOSED | Yes |

**Do not delete:** `collect/batch1-core-network-v3` (PR #16, open).

---

## Summary

- **12 closed PRs** (#1, #2, #3, #4, #5, #7): All superseded by PR #8 or #9. Zero action needed.
- **9 merged PRs** (#6, #8, #9, #10, #11, #12, #13, #14, #15, #17): All in main. Zero action needed.
- **1 open PR** (#16): Batch 1 core network (8 persons). Data-changing, CONDITIONAL APPROVAL pending Zhu Yunming source supplement.
- **Zero merge conflicts** on any branch.
- **17 stale branches** are candidates for cleanup.

**Next action:** Address PR #16 Zhu Yunming source gap, then merge. After that, the staging branch contains all 15 persons needed for the MVP core network.
