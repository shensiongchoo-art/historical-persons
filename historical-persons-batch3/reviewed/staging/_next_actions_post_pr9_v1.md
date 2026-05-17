# Next Actions After PR #9 v1
**Branch:** `maintenance/post-pr9-cleanup-v1`
**Date:** 2026-05-14

---

## 1. Immediate Actions — Completed

- [x] PR #6 source verification reports merged (reports-only, clean)
- [x] PR #7 Wu Kuan + Mark Antony hardened via PR #9 (merged)
- [x] PR #8 hardening sprint merged (5 packages normalized to v2.5)
- [x] PR #9 Wu Kuan + Mark Antony hardening merged
- [x] PR #10 source refs backfilled from sprint reports v2 (merged)
- [x] PR #11 cleanup — person_id, relationship types, description fixes (merged)
- [x] PR #12 Wang Yangming page-ref corrections (merged)
- [x] PR #2 and PR #3 closed (superseded)
- [x] PR #13 central reviews submitted (OPEN, pending review)
- [x] Post-PR9 repo status report created
- [x] PR #5 Qiu Ying + Augustus initial review created

---

## 2. Immediate Actions — Pending

- [ ] Central reviewer to review PR #13 (MVP inventory + 7 central reviews)
- [ ] Central reviewer to confirm ancient source A-level calibration for Augustus
- [ ] Decide disposition of PR #1, #4, #5 (all CLOSED, packages in main via hardening)

---

## 3. PRs Ready for Central Review

| PR | Title | Recommendation |
|----|-------|---------------|
| #13 | MVP inventory + 7 central reviews | Review and merge if approved |

All other PRs (#1–#12) are either merged or closed.

---

## 4. PRs That Should Be Closed

All superseded PRs already closed:
- PR #2 (partial Pompey) — CLOSED 2026-05-12
- PR #3 (v2.3 Qiu Ying + Augustus) — CLOSED 2026-05-11

No action needed.

---

## 5. PRs That Should Be Merged Only After Review

| PR | Package(s) | Status | Condition |
|----|-----------|--------|-----------|
| #13 | Central reviews (reports-only) | OPEN | Merge after central reviewer approval |

---

## 6. Remaining Source Verification Tasks

| Person | Task | Priority |
|--------|------|----------|
| Shen Zhou | 明史·隐逸传 passage refs; 沈周年谱 verification | Medium |
| Wu Kuan | Baidu-dependent claims re-verify with academic sources | Low |
| Mark Antony | Plutarch/Cassius Dio/Appian passage verification | Low |
| Qiu Ying | 3 needs_verification works — museum confirmation | Low |
| Augustus | Velleius Paterculus passage refs; SRC_AU_017 date fix | Low |

---

## 7. Whether It Is Safe to Collect More People

**Recommendation: YES, with constraints.**

All 7 existing packages pass validation. Source verification is complete for 4 of 7 persons (Augustus, Pompey, Qiu Ying, Wang Yangming). The hardening sprint is fully merged. No outstanding structural blockers.

Constraints:
- Collect maximum 2 persons per batch
- Run validate_package.py on every new package
- Do not collect until PR #13 is reviewed (or at minimum, do not block on it)
- Prioritize persons with strong academic source availability

---

## 8. Recommended Next Small Batch (if collection resumes)

### Batch 1 (Chinese): 李东阳 Li Dongyang + 王鏊 Wang Ao
- Both Ming dynasty, Wu School adjacent
- Strong academic coverage
- Complement existing Shen Zhou / Wu Kuan / Qiu Ying cluster
- Li Dongyang: 茶陵派 leader, Grand Secretary; documented interaction with Shen Zhou
- Wang Ao: Grand Secretary, Shen Zhou patron; documented in Shen Zhou sources

### Batch 2 (Western): Cleopatra VII + Marcus Agrippa
- Cleopatra: strong ancient sources (Plutarch, Cassius Dio, Suetonius), extensive modern scholarship
- Agrippa: well-documented in Augustan sources; key figure in Second Triumvirate era
- Both complement existing Augustus / Mark Antony / Pompey cluster

---

## 9. Repository Health Summary

| Metric | Status |
|--------|--------|
| Packages in incoming/ | 7 (all pass validation) |
| Open PRs | 1 (#13, reports-only) |
| Merged PRs | 6 |
| Closed PRs | 6 |
| Source verification complete | 4 of 7 |
| Blockers | None |
| Staging-quality packages | Augustus, Pompey, Qiu Ying, Wang Yangming (4) |
| Needs improvement | Shen Zhou (sources), Wu Kuan (sources), Mark Antony (verification) |
