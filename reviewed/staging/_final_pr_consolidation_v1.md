# Final PR Consolidation Report (v1)

**Date:** 2026-05-14
**Context:** PR #8 and PR #9 have been merged into `main`. All 7 MVP packages
(Qiu Ying, Shen Zhou, Wang Yangming, Wu Kuan, Augustus, Pompey, Mark Antony)
are present and passing `validate_package.py` on `main`. ZERO package edits
are needed — inventory is complete.

---

## PR Inventory

| PR | Title | State | Type | Superseded By | In Main? | Action |
|----|-------|-------|------|---------------|----------|--------|
| #1 | Shen Zhou v1 | CLOSED | data | #8 | Yes (via #8) | No action |
| #4 | Wang Yangming + Pompey | CLOSED | data | #8 | Yes (via #8) | No action |
| #5 | Qiu Ying + Augustus v2.5 | CLOSED | data | #8 | Yes (via #8) | No action |
| #7 | Wu Kuan + Mark Antony | CLOSED | data | #9 | Yes (via #9) | No action |
| #10 | Backfill source refs v2 | MERGED | data | — | Yes | No action |
| #11 | Cleanup person_id + rels | MERGED | data | — | Yes | No action |
| #12 | Wang Yangming page-ref fix | MERGED | data | — | Yes | No action |
| #13 | MVP inventory + 7 reviews | OPEN | reports | — | No | **Merge now** |
| #14 | Post-PR9 cleanup status | OPEN | reports | — | No | **Merge now** |

---

## Per-PR Analysis

### PR #1 — Shen Zhou v1 (CLOSED)
- **Still needed?** No. Superseded by PR #8.
- **Reports-only or data-changing?** Data-changing. 12 files, 22 claims, 6 sources, 13 relationships.
- **Safe to merge?** Already closed. No action needed.
- **In main?** Yes. Package at `incoming/chinese/shen-zhou/` matches post-#8 state.
- **Recommendation:** Permanently closed. No further action.

### PR #4 — Wang Yangming + Pompey (CLOSED)
- **Still needed?** No. Superseded by PR #8.
- **Reports-only or data-changing?** Data-changing. 33 files across 2 packages.
- **Safe to merge?** Already closed. No action needed.
- **In main?** Yes. Both packages at `incoming/chinese/wang-yangming/` and `incoming/western/gnaeus-pompeius-magnus/` match post-#8 state.
- **Recommendation:** Permanently closed. No further action.

### PR #5 — Qiu Ying + Augustus v2.5 (CLOSED)
- **Still needed?** No. Superseded by PR #8.
- **Reports-only or data-changing?** Data-changing. 22 files across 2 packages.
- **Safe to merge?** Already closed. No action needed.
- **In main?** Yes. Both packages at `incoming/chinese/qiu-ying/` and `incoming/western/augustus-octavian/` match post-#8 state.
- **Note:** PR #14 reviewed this as "ready_for_staging_merge" — data already in main via PR #8. The review remains valid documentation of package quality.
- **Recommendation:** Permanently closed. The PR #14 review serves as archived assessment.

### PR #7 — Wu Kuan + Mark Antony (CLOSED)
- **Still needed?** No. Superseded by PR #9.
- **Reports-only or data-changing?** Data-changing. 22 files across 2 packages.
- **Safe to merge?** Already closed. No action needed.
- **In main?** Yes. Both packages at `incoming/chinese/wu-kuan/` and `incoming/western/mark-antony/` match post-#9 state.
- **Recommendation:** Permanently closed. No further action.

### PR #10 — Backfill source refs v2 (MERGED)
- **Still needed?** Already merged. Content is in main.
- **Reports-only or data-changing?** Data-changing. Updated sources.jsonl in 4 packages (Pompey, Wang Yangming, Qiu Ying, Augustus) with exact page/edition/Loeb references.
- **Safe to merge?** Already merged.
- **In main?** Yes.
- **Recommendation:** No action.

### PR #11 — Cleanup person_id + relationship type (MERGED)
- **Still needed?** Already merged. Content is in main.
- **Reports-only or data-changing?** Data-changing. Standardized Wu Kuan person_id (P_CHN_MING_002_WU_KUAN → P_CHN_MING_WU_KUAN) across 8 files; fixed Mark Antony relationship type; softened Wu Kuan description.
- **Safe to merge?** Already merged.
- **In main?** Yes.
- **Recommendation:** No action.

### PR #12 — Wang Yangming page-ref corrections (MERGED)
- **Still needed?** Already merged. Content is in main.
- **Reports-only or data-changing?** Data-changing. Corrected SRC017 page range (33-72 → 233-263, verified via Crossref) and SRC018 caveat (Google Books verification).
- **Safe to merge?** Already merged.
- **In main?** Yes.
- **Recommendation:** No action.

### PR #13 — MVP inventory + 7 central reviews (OPEN)
- **Still needed?** Yes. Adds structured review documents not present in main.
- **Reports-only or data-changing?** Reports-only. 8 new `.md` files under `reviewed/staging/`. Zero package changes.
- **Safe to merge?** **Yes.** No file conflicts with main or PR #14 (disjoint file sets).
- **In main?** No. None of these 8 review files exist on main yet.
- **Content:** `_current_mvp_inventory.md` (cross-package metrics) + 7 `central_review.md` files (13-section review per person).
- **Recommendation:** Merge now. Reports-only, no risk.

### PR #14 — Post-PR9 cleanup status (OPEN)
- **Still needed?** Yes. Adds status documentation and PR #5 review.
- **Reports-only or data-changing?** Reports-only. 3 new `.md` files under `reviewed/staging/`. Zero package changes.
- **Safe to merge?** **Yes.** No file conflicts with main or PR #13 (disjoint file sets).
- **In main?** No. None of these 3 status files exist on main yet.
- **Content:** `_post_pr9_repo_status_v1.md` (13-PR inventory), `_pr5_qiu-ying_augustus_initial_review.md` (PR #5 quality assessment), `_next_actions_post_pr9_v1.md` (roadmap).
- **Recommendation:** Merge now. Reports-only, no risk.

---

## Merge Order

PR #13 and #14 are both reports-only with disjoint file sets. They can be merged
in either order, or together:

1. Merge PR #13 → adds inventory + 7 central reviews
2. Merge PR #14 → adds status docs + PR #5 review

**No conflicts expected.** Both branches branch from `main`.

---

## Current Main State

```
incoming/
├── chinese/
│   ├── qiu-ying/          (11 files, VALIDATION PASSED)
│   ├── shen-zhou/         (11 files, VALIDATION PASSED)
│   ├── wang-yangming/     (11 files, VALIDATION PASSED)
│   └── wu-kuan/           (11 files, VALIDATION PASSED)
└── western/
    ├── augustus-octavian/      (11 files, VALIDATION PASSED)
    ├── gnaeus-pompeius-magnus/ (11 files, VALIDATION PASSED)
    └── mark-antony/            (11 files, VALIDATION PASSED)

reviewed/staging/
├── _mvp_hardening_report_v1.md
├── _pr7_hardening_plan_v1.md
├── _repo_state_review_v1.md
└── source_verification/
    ├── augustus_source_verification.md
    ├── pompey_source_verification.md
    ├── qiu-ying_source_verification.md
    └── wang-yangming_source_verification.md
```

After merging #13 and #14, `reviewed/staging/` will also contain the inventory,
7 central reviews, 3 status docs, and the PR #5 review.

---

## Summary

- **7 closed PRs** (#1, #4, #5, #7): All superseded. Zero action needed.
- **4 merged PRs** (#10, #11, #12): All in main. Zero action needed.
- **2 open PRs** (#13, #14): Both **reports-only**, disjoint files, **safe to merge now**.

**Next step:** Merge PR #13 then merge PR #14. After that, the repository
has a complete staging documentation layer alongside all 7 validated packages.
