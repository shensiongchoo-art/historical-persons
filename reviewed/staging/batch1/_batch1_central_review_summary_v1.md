# Batch 1 Central Review Summary (v1)

**Branch:** `review/batch1-central-review-source-audit-v1`
**Date:** 2026-05-15
**Reviewer:** MorphMind AI
**Context:** All 8 Batch 1 persons (PR #16) have been merged into `main`. This is the first central review pass. No package edits were made — all observations are recorded in the individual review files. All 8 packages pass `validate_package.py`.

---

## 1. Package Inventory

| # | Person | Person ID | Sources | Claims | Relationships | Validation |
|---|--------|-----------|---------|--------|---------------|------------|
| 1 | 唐寅 / Tang Yin | `P_CHN_MING_TANG_YIN` | 8 | 18 | 6 | PASSED |
| 2 | 文徵明 / Wen Zhengming | `P_CHN_MING_WEN_ZHENGMING` | 7 | 14 | 6 | PASSED |
| 3 | 祝允明 / Zhu Yunming | `P_CHN_MING_ZHU_YUNMING` | 7 | 10 | 3 | PASSED |
| 4 | 徐祯卿 / Xu Zhenqing | `P_CHN_MING_XU_ZHENQING` | 5 | 10 | 4 | PASSED |
| 5 | Julius Caesar | `P_WEST_LATE_REPUBLIC_GAIUS_JULIUS_CAESAR` | 9 | 18 | 5 | PASSED |
| 6 | Cicero | `P_WEST_LATE_REPUBLIC_MARCUS_TULLIUS_CICERO` | 8 | 16 | 5 | PASSED |
| 7 | Cleopatra VII | `P_WEST_PTOLEMAIC_CLEOPATRA_VII` | 7 | 15 | 5 | PASSED |
| 8 | Marcus Agrippa | `P_WEST_EARLY_PRINCIPATE_MARCUS_VIPSANIUS_AGRIPPA` | 7 | 14 | 5 | PASSED |

**Totals:** 58 sources, 115 claims, 39 relationships. All pass validation.

---

## 2. Validation Results

All 8 packages pass `validate_package.py`. No JSON errors, no missing required files, all person_ids consistent.

---

## 3. Schema Compliance

All 8 packages follow v2.5 schema:
- Stable person_ids without numeric suffixes
- `review_status: ai_collected_unreviewed` on all records
- One claim = one fact (no compound claims)
- BCE dates use proper era/year fields
- Reception/later groupings correctly labeled as `reception_label` or `later_grouping_only`
- D-level sources (Wikipedia/Baidu/Britannica) correctly marked `clue_only`

---

## 4. Source Quality Ratings

| Person | A_candidate | B_high | D/clue_only | Non-D sources | Rating |
|--------|------------|--------|-------------|---------------|--------|
| Julius Caesar | 3 | 4 | 2 | 7 | **Strong** |
| Cicero | 3 | 3 | 2 | 6 | **Strong** |
| Zhu Yunming | 2 | 3 | 2 | 5 | **Moderate** |
| Marcus Agrippa | 1 | 4 | 2 | 5 | **Moderate** |
| Tang Yin | 2 | 3 | 2 | 5 | **Moderate** |
| Cleopatra VII | 1 | 4 | 2 | 5 | **Moderate** |
| Wen Zhengming | 2 | 3 | 2 | 5 | **Moderate** |
| Xu Zhenqing | 2 | 1 | 2 | 3 | **Weak** |

**Note:** Zhu Yunming was previously reported as having only 5 sources. The actual source count is 7 — 5 non-D. This is moderate, not critically thin. Xu Zhenqing is the only package with fewer than 5 non-D sources.

---

## 5. Top Source Risks

| Risk | Packages Affected | Detail |
|------|-------------------|--------|
| SRC needing journal/author verification | Tang Yin (SRC_TY_007), Wen Zhengming (SRC_WZM_007), Zhu Yunming (SRC_ZYM_003), Xu Zhenqing (SRC_XZQ_003) | 4 academic papers missing journal name, author, or DOI |
| Museum record unverified | Tang Yin, Wen Zhengming, Zhu Yunming | Palace Museum object/accession IDs not confirmed |
| Coinage reference unverified | Cleopatra VII (SRC_CL_004) | RRC or museum accession numbers needed |
| 明史 passage refs not verified | All 4 Chinese packages | Exact juan/page in Zhonghua Shuju edition needed |
| Caesar's own writings are self-serving | Julius Caesar (SRC_JC_001, SRC_JC_002) | Properly flagged in notes but no alternative sources for some claims |
| Res Gestae is self-serving | Marcus Agrippa (SRC_MA_003) | Properly flagged; Augustan propaganda bias |
| Zhou Chen teacher relationship unverified | Tang Yin (CLM_TY_012) | Single source with needs_verification |
| Shen Zhou teacher relationship unverified | Wen Zhengming (CLM_WZM_004) | Single source with needs_verification |

---

## 6. Top Claim Risks

| Risk | Packages Affected | Detail |
|------|-------------------|--------|
| Relationships based only on later groupings | All 4 Chinese, Tang Yin relationships | 吴中四才子 and 明四家 are later classifications, not documented personal bonds |
| Agrippa birth year uncertain | Marcus Agrippa (CLM_MA_014) | Correctly marked `needs_verification` |
| Caesar birth year discrepancy | Julius Caesar | 100 BCE vs 102 BCE — only 100 BCE cited |
| Cleopatra asp death | Cleopatra VII (CLM_CL_011, CLM_CL_012) | Correctly disputed/uncertain |
| Caesar "dictator perpetuo" framing | Julius Caesar (CLM_JC_012) | Correct, but could note the exceptional nature more strongly |
| Tang Yin exam scandal culpability | Tang Yin (CLM_TY_006) | Correctly disputed |

---

## 7. Relationship Risks

| Risk | Detail |
|------|--------|
| 吴中四才子 treated as real association | All 4 Chinese packages correctly use `later_grouping_only` or `probable_association` — but cross-package consistency varies slightly. Tang Yin→Xu Zhenqing uses `later_grouping_only` (correct); Wen Zhengming→Zhu Yunming uses `probable_association` for the same grouping (inconsistent). |
| Tang Yin→Qiu Ying: later_grouping_only | Correct — 明四家 is an art-historical grouping |
| Mark Antony person_id mismatch | Cicero's `related_person_id` for Mark Antony uses `P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS`; Agrippa's uses `P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS`. Both present in the repo. Cross-reference with mark-antony package confirms consistency. |
| Empty related_person_id fields | Several relationships have empty `related_person_id` (Zhou Chen, Li Mengyang, Julia the Elder, Tiberius, Atticus, Brutus) — acceptable if those persons are not yet in the database |

---

## 8. Visual Media Risks

All 8 packages have visual_media.jsonl entries. All marked `staging` status. Risks are low — visual media is optional metadata. Main concern: museum object IDs not verified for Chinese paintings and Roman portrait busts.

---

## 9. Staging-Acceptable Packages

These packages are ready for staging use with minor caveats:

| Package | Assessment |
|---------|------------|
| **Julius Caesar** | Best in batch. Strong source coverage (7 non-D), good BCE handling, Shakespeare separation, reception labels correct. Ready for staging. |
| **Cicero** | Strong. Primary texts well-represented, Catilinarian controversy correctly disputed, Fulvia story labeled legendary. Ready for staging. |
| **Cleopatra VII** | Good. Roman propaganda bias thoroughly documented, asp death uncertain, Shakespeare reception separated. Ready for staging with coinage verification note. |

---

## 10. Packages Needing Cleanup Before Merge/Use

| Package | Issue | Severity |
|---------|-------|----------|
| **Wen Zhengming** | SRC_WZM_007 (academic paper) needs journal/author verification | Low |
| **Marcus Agrippa** | Birth year uncertainty (CLM_MA_014); only monograph dated 1932; Res Gestae bias | Low-Medium |
| **Tang Yin** | SRC_TY_007 needs verification; Zhou Chen teacher relationship thinly sourced | Low-Medium |
| **Zhu Yunming** | SRC_ZYM_003 needs verification; calligraphy museum IDs missing | Low |

None of these are merge-blocking. All are post-merge cleanup tasks.

---

## 11. Packages Needing Source Verification First

| Package | Priority | Detail |
|---------|----------|--------|
| **Xu Zhenqing** | **High** | Only 5 sources, 3 non-D. Most relationships are `later_grouping_only`. Needs at least 1-2 additional academic sources before meaningful staging assessment. |
| **Zhu Yunming** | Medium | Previously reported as "only 5 sources" — actual is 7 (5 non-D). Acceptable for staging but would benefit from calligraphy collection IDs. |
| **All Chinese** | Medium | 明史·文苑传 exact juan/page references needed for all 4 packages |

---

## 12. Recommended Next Action Order

1. **Merge this review branch** — all 9 review files are reports-only, no package changes.
2. **Xu Zhenqing source enrichment** (highest priority) — add 1-2 academic references before staging use.
3. **Verify SRC academic papers** — SRC_TY_007, SRC_WZM_007, SRC_ZYM_003, SRC_XZQ_003 need journal/author details.
4. **Chinese 明史 passage verification** — exact juan/page refs for all 4 Chinese packages.
5. **Museum/collection IDs** — Palace Museum object IDs for Tang Yin/Wen Zhengming, calligraphy IDs for Zhu Yunming, RRC numbers for Cleopatra coinage, bust inventory numbers for Caesar/Agrippa.
6. **Do not collect new persons** until source verification for all 8 Batch 1 packages is complete.

---

## 13. Summary

- **All 8 packages pass validation.** v2.5 schema compliance is uniform.
- **3 packages are staging-ready** (Caesar, Cicero, Cleopatra VII).
- **4 packages need minor source verification** (Tang Yin, Wen Zhengming, Zhu Yunming, Agrippa).
- **1 package needs source enrichment** (Xu Zhenqing).
- **No package has blocking issues.** No claims are rejected. Legendary/fictional material is correctly separated in all packages.
- **Next phase:** Source verification sprint — starting with Xu Zhenqing + academic paper verification.
