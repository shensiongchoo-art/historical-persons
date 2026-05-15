# Final PR Consolidation Report (v2)

**Date:** 2026-05-15
**Context:** All 18 historical PRs have been audited. PR #16 (Batch 1 core network: 8 persons) has been merged into `main`. All 15 packages — 7 original MVP + 8 Batch 1 core network — are present and validated on `main`. The only remaining open PR is #18 (this report, reports-only).

This report supersedes `_final_pr_consolidation_v1.md` (PR #15, 2026-05-14), which was correct at the time but predated the merge of PR #13, #14, #16, and #17.

---

## Complete PR Inventory (#1-#18)

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
| #16 | Batch 1 core network (8 ppl) | MERGED | data | -- | Yes | No action |
| #17 | Duplicate of #9 normalization | MERGED | data | #9 | Yes (via #9) | No action |
| #18 | Final PR consolidation v2 | OPEN | reports | -- | No | **Merge now** |

---

## Per-PR Analysis

### PR #1 -- Shen Zhou v1 (CLOSED)
- **Still needed?** No. Superseded by PR #8.
- **Recommendation:** Permanently closed. No further action.

### PR #2 -- Pompey solo v1 (CLOSED)
- **Still needed?** No. Partial package. Pompey canonical is from PR #4, normalized in PR #8, source-verified in PR #10/#12.
- **Recommendation:** Permanently closed. No further action.

### PR #3 -- Qiu Ying + Augustus v1 (CLOSED)
- **Still needed?** No. v2.3 schema. Superseded by PR #5 (v2.5) then PR #8 (hardening).
- **Recommendation:** Permanently closed. No further action.

### PR #4 -- Wang Yangming + Pompey (CLOSED)
- **Still needed?** No. Both packages normalized in PR #8.
- **Recommendation:** Permanently closed. No further action.

### PR #5 -- Qiu Ying + Augustus v2.5 (CLOSED)
- **Still needed?** No. Superseded by PR #8. PR #14's review remains valid archived documentation.
- **Recommendation:** Permanently closed. No further action.

### PR #6 -- Source verification v1 (MERGED)
- **Still needed?** Already merged. Source verification reports at `reviewed/staging/source_verification/`.
- **Recommendation:** No action.

### PR #7 -- Wu Kuan + Mark Antony (CLOSED)
- **Still needed?** No. Superseded by PR #9 (v2.5 normalization).
- **Recommendation:** Permanently closed. No further action.

### PR #8 -- Hardening sprint v1 (MERGED)
- **Still needed?** Already merged. Core hardening for 5 packages. All pass validation.
- **Recommendation:** No action.

### PR #9 -- Wu Kuan + Mark Antony normalization (MERGED)
- **Still needed?** Already merged. Both packages v2.5 schema compliant. All pass validation.
- **Recommendation:** No action.

### PR #10 -- Source refs backfill v2 (MERGED)
- **Still needed?** Already merged. Added page/edition/Loeb references to 4 packages.
- **Recommendation:** No action.

### PR #11 -- Cleanup person_id + relationship type (MERGED)
- **Still needed?** Already merged. Standardized person_ids, fixed relationship types.
- **Recommendation:** No action.

### PR #12 -- Wang Yangming page-ref corrections (MERGED)
- **Still needed?** Already merged. SRC017 page range corrected, SRC018 caveat added.
- **Recommendation:** No action.

### PR #13 -- MVP inventory + 7 central reviews (MERGED)
- **Still needed?** Already merged. Reports-only. Central reviews for all 7 MVP persons.
- **Recommendation:** No action.

### PR #14 -- Post-PR9 cleanup status (MERGED)
- **Still needed?** Already merged. Reports-only: repo status, PR #5 review, next actions roadmap.
- **Recommendation:** No action.

### PR #15 -- Final PR consolidation v1 (MERGED)
- **Still needed?** Already merged. Correct at the time. This v2 supersedes it.
- **Recommendation:** No action.

### PR #16 -- Batch 1 core network: 8 persons (MERGED)
- **Still needed?** Already merged. Adds 8 new persons (115 claims, 56 sources, 40 relationships). All 8 packages pass `validate_package.py`.
- **Data-changing.** 88 new package files across 8 person folders.
- **Persons:** Tang Yin, Wen Zhengming, Zhu Yunming, Xu Zhenqing (Chinese Ming network); Julius Caesar, Cicero, Cleopatra VII, Marcus Agrippa (Western Late Republic/Early Principate network).
- **Status:** All 8 packages marked `ai_collected_unreviewed`.
- **In main?** Yes. All 8 packages present and validated on `main`.
- **Known limitation:** Zhu Yunming has only 5 sources — the thinnest source base among all 15 packages. Review noted this as a known gap; did not block merge. Source enrichment is a post-merge task.
- **Review files:** `_batch1_core_network_collection_summary.md`, `_batch1_pr16_initial_review.md`, `_batch1_pr16_recommendation.md` are present in `reviewed/staging/`.
- **Recommendation:** No action. Merge is complete.

### PR #17 -- Duplicate of PR #9 normalization (MERGED)
- **Still needed?** Already merged. Same changes as PR #9. No conflict.
- **Recommendation:** No action.

### PR #18 -- Final PR consolidation v2 (OPEN)
- **Still needed?** Yes. This report. Supersedes v1 with the post-PR #16 merge reality.
- **Reports-only.** One file: `_final_pr_consolidation_v2.md`. Zero package changes.
- **Safe to merge?** **Yes.** No file conflicts with `main`. Reports-only with no data risk.
- **In main?** No. This file is not yet on `main`.
- **Recommendation:** Merge now. This is the final administrative report closing out the PR audit cycle.

---

## Current Main State (15 packages, all validated)

```
incoming/
├── chinese/
│   ├── qiu-ying/              (11 files, VALIDATION PASSED)
│   ├── shen-zhou/             (11 files, VALIDATION PASSED)
│   ├── tang-yin/              (11 files, VALIDATION PASSED)
│   ├── wang-yangming/         (11 files, VALIDATION PASSED)
│   ├── wen-zhengming/         (11 files, VALIDATION PASSED)
│   ├── wu-kuan/               (11 files, VALIDATION PASSED)
│   ├── xu-zhenqing/           (11 files, VALIDATION PASSED)
│   └── zhu-yunming/           (11 files, VALIDATION PASSED)
└── western/
    ├── augustus-octavian/      (11 files, VALIDATION PASSED)
    ├── cicero/                 (11 files, VALIDATION PASSED)
    ├── cleopatra-vii/          (11 files, VALIDATION PASSED)
    ├── gnaeus-pompeius-magnus/ (11 files, VALIDATION PASSED)
    ├── julius-caesar/          (11 files, VALIDATION PASSED)
    ├── marcus-agrippa/         (11 files, VALIDATION PASSED)
    └── mark-antony/            (11 files, VALIDATION PASSED)

reviewed/staging/
├── _batch1_core_network_collection_summary.md
├── _batch1_pr16_initial_review.md
├── _batch1_pr16_recommendation.md
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

All remote branches for closed/merged PRs are candidates for deletion:

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
| `hardening/pr7-wu-kuan-mark-antony-v1` | #9, #17 | MERGED | Yes |
| `verification/source-reports-v2` | #10 | MERGED | Yes |
| `maintenance/cleanup-wu-kuan-mark-antony-v1` | #11 | MERGED | Yes |
| `verification/wang-yangming-page-refs-v3` | #12 | MERGED | Yes |
| `step1.2/staging-consolidation-small-expansion-v1` | #13 | MERGED | Yes |
| `maintenance/post-pr9-cleanup-v1` | #14 | MERGED | Yes |
| `consolidation/final-pr-consolidation-v1` | #15 | MERGED | Yes |
| `collect/batch1-core-network-v3` | #16 | MERGED | Yes |
| `maintenance/pr-triage-after-hardening-v1` | (none) | -- | Yes |
| `collect/batch1-core-network-v1` | (superseded) | CLOSED | Yes |
| `collect/batch1-core-network-v2` | (superseded) | CLOSED | Yes |

**Do not delete:** `consolidation/final-pr-consolidation-v2` (PR #18, open).

---

## Next Actions After PR #18

PR #18 is the last administrative report. After merging, all 15 packages are in `main` and all 18 PRs are audited. The next phase should be **central review and source audit** of the 8 Batch 1 persons, NOT more collection.

### Priority: Central Review / Source Audit (Batch 1)

Each of the 8 Batch 1 persons needs a structured central review matching the 13-section format used for the 7 MVP persons (see `reviewed/staging/*/central_review.md`). Priority order:

**Tier 1 — Strongest packages, review first:**
1. **Julius Caesar** — 9 sources, 18 claims. Strong ancient source coverage. Verify Loeb chapter references.
2. **Cicero** — 8 sources including primary texts. Verify speech/letter references.
3. **Cleopatra VII** — Well-caveated. Verify legendary material separation from documented history.

**Tier 2 — Needs source verification before full review:**
4. **Tang Yin** — Verify 明史·文苑传 passage refs. Zhou Chen teacher relationship needs primary evidence.
5. **Wen Zhengming** — Shen Zhou teacher relationship needs primary evidence. Age calculation verification.
6. **Marcus Agrippa** — Birth year uncertain. Independent achievements subsumed into Augustan narrative.

**Tier 3 — Thin source base, needs enrichment first:**
7. **Zhu Yunming** — Only 5 sources. Needs 1-2 additional academic references before meaningful review.
8. **Xu Zhenqing** — Thin source base. Needs primary text verification.

### Do Not Collect
- Do not collect new persons until central reviews for all 8 Batch 1 persons are complete.
- The repository already has 15 packages covering both the Ming Wu cultural network and the Late Roman Republic/Early Principate network.

---

## Summary

- **10 closed PRs** (#1, #2, #3, #4, #5, #7): All superseded. Zero action needed.
- **7 merged PRs** (#6, #8, #9, #10, #11, #12, #13, #14, #15, #16, #17): All in `main`. Zero action needed.
- **1 open PR** (#18): Reports-only. **Merge now.**
- **15 packages** on `main`: 7 MVP + 8 Batch 1. All `ai_collected_unreviewed`. All pass validation.
- **19 stale branches** are candidates for cleanup.
- **Next phase:** Central review + source audit of 8 Batch 1 persons. No new collection.
