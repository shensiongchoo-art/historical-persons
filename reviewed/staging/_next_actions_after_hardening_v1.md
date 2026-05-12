# Next Actions After Hardening v1
**Branch:** `maintenance/pr-triage-after-hardening-v1`
**Date:** 2026-05-12

---

## 1. Immediate Actions (This Sprint)

- [x] Triage open PRs after hardening (#1, #4, #5, #6, #7)
- [x] Confirm PR #2 and #3 already closed (superseded)
- [x] Verify PR #6 is reports-only (confirmed — safe to merge)
- [x] Create PR #7 initial review notes
- [x] Document current state in triage report

## 2. PRs to Close

| PR | Status | Action Needed |
|----|--------|---------------|
| #2 | Already CLOSED | None |
| #3 | Already CLOSED | None |

## 3. PRs Ready for Central Review

| PR | Persons | After |
|-----|---------|-------|
| #1 | 沈周 Shen Zhou | Central reviewer approval |
| #4 | 王阳明 Wang Yangming + Pompey | Central reviewer approval |
| #5 | 仇英 Qiu Ying + Augustus | Central reviewer approval |
| #6 | Source verification reports | Merge (reports-only, no package changes) |

All four PRs have packages that pass validation on `main` after hardening sprint merge (PR #8).

## 4. PRs Needing Cleanup

| PR | Persons | Issues |
|----|---------|--------|
| #7 | 吴宽 Wu Kuan | v2.3 schema → v2.5, Baidu Baike overuse |
| #7 | Mark Antony | Schema norms, relationship type remapping |

**Recommended:** Open `hardening/pr7-wu-kuan-mark-antony-v1` for the next hardening pass.

## 5. Packages Ready for Staging Review

| Person | Status | Key Remaining Items |
|--------|--------|---------------------|
| 沈周 Shen Zhou | Staging ✓ | Source passage verification, birth year |
| 王阳明 Wang Yangming | Staging ✓ | SRC001/008/009/010 verified in v3 sprint |
| Pompey | Staging ✓ | Loeb refs added, RRC numbers pending |
| 仇英 Qiu Ying | Staging ✓ | 明清画史笔记 entries added, passage verification pending |
| Augustus | Staging ✓ | Loeb refs added, Wiseman year pending |

## 6. Packages Needing Source Verification

| Person | Item |
|--------|------|
| 沈周 Shen Zhou | 明史·隐逸传 passage refs, 沈周年谱 page refs |
| Wang Yangming | Cambridge History of China vol. 7 page refs |
| Pompey | Leach 1978 page refs, CAH vol. IX page refs, Crawford RRC numbers |
| Qiu Ying | 明清画史笔记 passage-level verification, Cleveland museum catalogue |
| Augustus | Syme page refs, Goldsworthy page refs, Wiseman date check |

## 7. Whether to Resume Collecting New People

**Not yet.** Do not collect new people until:

1. PR #7 (Wu Kuan + Mark Antony) is hardened to v2.5
2. Central reviewer approves the current 5-package staging state
3. Source verification gaps in the "Packages Needing Source Verification" list are addressed

**After PR #7 hardening, next new-person batch candidates:**
- 李东阳 (Li Dongyang) — Chinese, Ming dynasty, connected to Wu Kuan
- 王鏊 (Wang Ao) — Chinese, Ming dynasty, connected to Wu Kuan + Shen Zhou
- Cleopatra VII — Western, needed for Mark Antony relationship
- Marcus Agrippa — Western, needed for Augustus + Mark Antony context

## 8. Recommended Execution Order

1. **Merge PR #6** (source verification reports) — reports-only, safe
2. **Central reviewer approves PRs #1, #4, #5** for merge
3. **Open hardening PR for #7** — normalize Wu Kuan and Mark Antony to v2.5
4. **After PR #7 hardened** — resume collecting next person batch
5. **Ongoing** — passage-level source verification for all 5 current packages
