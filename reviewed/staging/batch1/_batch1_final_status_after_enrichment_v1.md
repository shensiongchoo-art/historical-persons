# Batch 1 Final Status After Enrichment v1

**Branch:** `review/batch1-final-status-after-enrichment-v1`
**Date:** 2026-05-16
**Author:** MorphMind AI
**Status:** Complete — all 8 packages staging-ready

---

## 1. PR Merges Summary

| PR | Title | Status |
|----|-------|--------|
| #24 | Batch 1 claims accuracy audit — 13 fixes across 7 packages | **MERGED** (squash) |
| #25 | Xu Zhenqing source enrichment — replace SRC_XZQ_003, add 2 B_high | **MERGED** (squash) |

---

## 2. Final Package State

| # | Package | Claims | Sources (non-D) | Density | Validation | Staging |
|---|---------|--------|-----------------|---------|------------|---------|
| 1 | Tang Yin (唐寅) | 18 | 9 (7) | 0.39 | PASSED | ready |
| 2 | Wen Zhengming (文徵明) | 14 | 8 (6) | 0.43 | PASSED | ready |
| 3 | Zhu Yunming (祝允明) | 10 | 8 (6) | 0.60 | PASSED | ready |
| 4 | **Xu Zhenqing (徐祯卿)** | 10 | **10 (8)** | **0.80** | PASSED | **ready** |
| 5 | Julius Caesar | 18 | 9 (7) | 0.39 | PASSED | ready |
| 6 | Cicero | 16 | 8 (6) | 0.38 | PASSED | ready |
| 7 | Cleopatra VII | 15 | 7 (5) | 0.33 | PASSED | ready |
| 8 | Marcus Agrippa | 14 | 8 (6) | 0.43 | PASSED | ready |

**Total: 115 claims | 67 sources (51 non-D) | all PASSED**

---

## 3. Xu Zhenqing — Before/After

| Metric | Before (v1) | After (v2) |
|--------|-------------|------------|
| Non-D sources | 5 | **8** |
| Source density | 0.30 | **0.80** |
| Unverified sources | 1 (SRC_XZQ_003) | **0** |
| Claims with sole unverified source | 5 | **0** |
| Status | needs_source_enrichment | **adequate_with_caveats** |

**Key changes:**
- SRC_XZQ_003: Replaced placeholder → 崔秀霞 2008 《徐祯卿诗歌转变与其在前七子中的地位》(语文知识)
- SRC_XZQ_009: Added 史小军/刘茜 2022 (昆明学院学报) — Wu-Zhong reception
- SRC_XZQ_010: Added 陈书录 1993 (南京师大学报) — yin qing li ge poetic theory
- CLM_XZQ_006-009: source_ids reassigned with new verified sources

---

## 4. Remaining Source Gaps

| Package | Gap | Severity |
|---------|-----|----------|
| Cleopatra VII | Lowest non-D count (5); source density 0.33 | Low |
| Julius Caesar | Heavy reliance on ancient sources (Plutarch, Suetonius) marked A_candidate; no page refs verified | Low |
| Tang Yin | SRC_TY_003 (academic monograph) exact pages unverified | Info |
| Wen Zhengming | SRC_WZM_003 (年谱) page ranges unverified | Info |
| All Chinese | Exact Zhonghua Shuju/juan/page refs for 明史 passages unverified | Info |
| All Western | Exact Loeb/page refs for Plutarch/Appian/Dio unverified | Info |

**None of these gaps block staging.** They are low-priority improvements for future verification sprints.

---

## 5. PR #24 Claims Accuracy Fixes Verified

All 13 fixes from PR #24 are present in main:

| Package | Fixes | Status |
|---------|-------|--------|
| Tang Yin | +backup sources (3 claims), Chinese quote encoding | ✅ |
| Wen Zhengming | +SRC_WZM_003/008 (4 claims), soften "central position" | ✅ |
| Zhu Yunming | +SRC_ZYM_006 to family background | ✅ |
| Xu Zhenqing | +SRC_XZQ_006 (2 claims), Chinese quote encoding | ✅ |
| Julius Caesar | Calendar reform timeline 46→45 BCE | ✅ |
| Cleopatra VII | +Roller 2010 to Tarsus meeting | ✅ |
| Marcus Agrippa | Clarify "met as young men" not "from childhood" | ✅ |
| Cicero | 0 issues — unchanged | ✅ |

---

## 6. Readiness for Next Batch

**All 8 Batch 1 persons are staging-ready.** No package has critically thin sources, unverified placeholder sources, or fabricated claims.

**Recommendation: Batch 2 can proceed.** The repository now has 15 staging packages (7 pre-Batch-1 + 8 Batch 1) with consistent v2.5 schema, validated JSONL, and adequate source coverage.

### Recommended Batch 2 candidates

**Chinese (Wu-Men network closure):**
- Li Dongyang (李东阳) — closes Ming court-literati network node
- Wang Ao (王鏊) — Suzhou official, Five Commonalities Society

**Western (Late Republic closure):**
- Marcus Aemilius Lepidus — completes Second Triumvirate
- Octavia Minor — links Antony/Augustus families
- Sextus Pompey — Republican resistance, Sicily

**Chinese (Former Seven Masters closure):**
- Li Mengyang (李梦阳) — leader of Former Seven Masters
- He Jingming (何景明) — co-leader

**Total recommended: 6-7 new persons** — controlled expansion, closes key network nodes.

---

## 7. Remaining Open PRs

| PR | Title | Status |
|----|-------|--------|
| #18 | Final PR consolidation v2 | Reports-only, superseded by #24/#25 |
| #19 | Batch 1 central review + source audit | Reports-only |
| #20 | Xu Zhenqing enrichment plan | Superseded by #25 |
| #22 | Batch 1 claims accuracy review | Superseded by #24 |

---

## 8. Recommended Next Actions

1. Close superseded PRs #18, #20, #22
2. Review and merge reports-only PR #19 (Batch 1 central review reports)
3. Open Batch 2 collection PR with 6-7 new persons
