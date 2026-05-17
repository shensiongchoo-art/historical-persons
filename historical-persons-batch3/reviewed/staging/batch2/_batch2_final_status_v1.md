# Batch 2 Final Status v1

**Branch:** `review/batch2-final-status-v1`
**Date:** 2026-05-16
**Author:** MorphMind AI

## 1. Batch 2 Package Inventory

| # | Person | Person ID | Validation | Source Quality | Staging-Ready |
|---|--------|-----------|------------|----------------|---------------|
| 1 | Li Dongyang | P_CHN_MING_LI_DONGYANG | PASSED | 4 non-D (2 A_candidate) | Yes |
| 2 | Wang Ao | P_CHN_MING_WANG_AO | PASSED | 2 non-D (thin but honest) | Yes |
| 3 | Li Mengyang | P_CHN_MING_LI_MENGYANG | PASSED | 4 non-D (1 verified in main; 5 verified in PR #30) | Yes (after PR #30 merge) |
| 4 | He Jingming | P_CHN_MING_HE_JINGMING | PASSED | 4 non-D (strong) | Yes |
| 5 | Lepidus | P_WEST_LATE_REPUBLIC_LEPIDUS | PASSED | 3 non-D (all verified) | Yes |
| 6 | Octavia Minor | P_WEST_LATE_REPUBLIC_OCTAVIA_MINOR | PASSED | 3 non-D (all verified) | Yes |
| 7 | Sextus Pompey | P_WEST_LATE_REPUBLIC_SEXTUS_POMPEY | PASSED | 4 non-D (all verified) | Yes |

**Total: 7 packages | all PASSED | 6 of 7 staging-ready without enrichment**

## 2. PR Status Summary

| PR | Title | State | Notes |
|----|-------|-------|-------|
| #28 | Batch 2 core network collection | **MERGED** (squash, e7ddb44) | 7 packages, 78 files |
| #29 | Batch 2 initial review | **OPEN** | All 7 packages staging-acceptable; flagged two source issues |
| #30 | Li Mengyang source enrichment | **OPEN** (mergeable) | 3 needs_verification replaced, +1 English monograph |

## 3. Pre-Merge Issues Resolution

### Issue 1: Li Mengyang SRC_LMY_002 (A_candidate -> B_high)
- **Status:** RESOLVED
- SRC_LMY_002 was A_candidate with citation_detail: needs_verification
- Fixed in commit 6aa4de7 (pushed to PR #28 before merge)
- PR #30 further enriches Li Mengyang: upgrades SRC_LMY_002 back to A_candidate with verified Zhonghua Book Company 2019 edition, replaces two invented titles with real monographs

### Issue 2: Li Dongyang SRC_LDY_003 (possible A_candidate overclaim)
- **Status:** CONDITIONAL WARNING - NO ACTION NEEDED
- SRC_LDY_003 is B_high, not A_candidate
- citation_detail: needs_verification, verification_status: needs_verification
- Per v2.5 rules: B_high + needs_verification is acceptable for staging, not master-ready
- No edit required

## 4. Source Quality Assessment

| Package | Verified Non-D | Needs Verification | D/Clue Only | Density |
|---------|---------------|-------------------|-------------|---------|
| Li Dongyang | 3 (SRC_LDY_001, 002, 004) | 1 (SRC_LDY_003) | 2 | 75% |
| Wang Ao | 2 (SRC001, 002) | 0 | 2 | 100% of non-D |
| Li Mengyang (main) | 1 (SRC_LMY_001) | 3 (SRC_LMY_002-004) | 2 | 25% |
| Li Mengyang (PR #30) | 5 (SRC_LMY_001-004, 007) | 0 | 2 | 100% |
| He Jingming | 3 (SRC001, 002, 005) | 1 (SRC003) | 2 | 75% |
| Lepidus | 3 (SRC001-003) | 0 | 1 | 100% |
| Octavia Minor | 3 (SRC001-003) | 0 | 1 | 100% |
| Sextus Pompey | 4 (SRC001-004) | 0 | 1 | 100% |

## 5. Packages Requiring Source Verification Before Master

| Package | Item | Priority |
|---------|------|----------|
| Li Dongyang | SRC_LDY_003: monograph on Li Dongyang and Chaling school - author/publisher/year | MEDIUM |
| Wang Ao | SRC001 Ming History juan/page verification; SRC002 DMB page verification | LOW |
| Li Mengyang | SRC_LMY_001 Ming History exact page range; SRC002-004,007 exact passage/page | LOW (after PR #30) |
| He Jingming | SRC001 Ming History juan/page; SRC003 Dafu ji Siku quanshu juan | LOW |

## 6. Schema Inconsistency Note

Chinese packages (Li Dongyang, Li Mengyang) use simpler schema:
- claim_id: CLM_LDY_001 format
- source_id: SRC_LDY_001 format
- Date: birth.year_display only

Western + scout-generated Chinese packages (Wang Ao, He Jingming, all Western) use richer schema:
- claim_id: C001 format
- source_id: SRC001 format
- Date: date.year_display + era + place + precision
- Sources: additional author, language, used_for_claim_ids fields

Both pass validation. Richer schema is superior. Normalization recommended in future hardening pass.

## 7. Obsidian Demo Readiness

### Ready for import (staging-acceptable):
- All 7 Batch 2 packages are staging-acceptable
- Combined with Batch 1 (8 packages), total staging-ready: **15 packages**

### Before Obsidian demo:
- Li Mengyang should be enriched first (merge PR #30)
- Schema normalization would improve consistency but is not blocking
- Source verification for Li Dongyang SRC_LDY_003 is medium priority

## 8. Clear Statement

**Do not collect more people until the following are reviewed:**

1. Merge PR #30 (Li Mengyang source enrichment)
2. Review and merge PR #29 (Batch 2 initial review)
3. Plan Obsidian vault import for 15 staging-ready packages
4. Decide on schema normalization approach (simplify rich to simple, or enrich simple to rich)
5. Decide whether to start Batch 3 (mid-grade network: Bian Gong, Kang Hai, Livia, Fulvia, etc.)

**No further collection until Obsidian/import planning is reviewed.**
