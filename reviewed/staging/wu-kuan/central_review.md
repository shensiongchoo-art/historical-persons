# Central Review: 吴宽 (Wu Kuan)

**Reviewer:** MorphMind AI
**Date:** 2026-05-13
**Package:** `incoming/chinese/wu-kuan/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_002_WU_KUAN` |
| **Name (ZH)** | 吴宽 |
| **Name (EN)** | Wu Kuan |
| **Birth** | 1435 (宣德十年) |
| **Death** | 1504 (弘治十七年七月十日) |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#7 (`collect/wu-kuan-and-mark-antony-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (partially normalized — PR#7 hardening applied) |

---

## 2. Source Inventory & Quality

| Source ID | Level | Type | Citation | Notes |
|-----------|-------|------|----------|-------|
| SRC_WK_001 | A_candidate | 明史·吴宽传 | 卷184, 列传第七十二 | Primary official biography — strongest source |
| SRC_WK_002 | A_candidate | 匏翁家藏集 | 四库全书, 77卷 | Wu Kuan's collected works |
| SRC_WK_003 | A_candidate | 丛书堂书目 | Wu Kuan's library catalogue | Limited utility for biographical claims |
| SRC_WK_004 | A_candidate | 震泽集, 卷22 | 王鏊撰神道碑 | Contemporary tomb inscription — strong |
| SRC_WK_005 | D | Baidu Baike | 吴宽 | Correctly marked D/clue_only |
| SRC_WK_006 | A_candidate | Palace Museum | 五同会图 scroll | Museum collection record |
| SRC_WK_007 | A_candidate | 国家图书馆 | 吴文定公诗稿 manuscript | NLC manuscript record |

**Assessment:** 7 sources for 18 claims (0.39/claim). 5 A_candidate, 0 B, 1 D. The D-level Baidu source is correctly flagged and not used as primary support. Source base is thin but has good primary materials — 明史 biography, collected works, contemporary tomb inscription, museum records. No modern academic monograph.

---

## 3. Claim Quality Review

| Claim ID | Status/Confidence | Type | Sources | Issue |
|----------|-------------------|------|---------|-------|
| CLM_WK_001 | probable/medium | identity | SRC_WK_001 | Name, origin — solid |
| CLM_WK_002 | confirmed/high | identity | SRC_WK_001 | Birth/death dates — correct |
| CLM_WK_003 | probable/medium | career | SRC_WK_001 | 1472 zhuangyuan — solid |
| CLM_WK_004–006b | probable/medium–confirmed/high | career | SRC_WK_001 | Official career — solid |
| CLM_WK_007 | confirmed/high | work | SRC_WK_002 | 匏翁家藏集 — solid |
| CLM_WK_008 | needs_verification/low | work | **(empty)** | **No source assigned** |
| CLM_WK_009 | needs_verification/low | work | **(empty)** | **No source assigned** |
| CLM_WK_010 | needs_verification/low | reception_label | **(empty)** | **No source assigned** |
| CLM_WK_011 | needs_verification/low | work | **(empty)** | **No source assigned** |
| CLM_WK_012a | probable/medium | relationship | **(empty)** | **No source assigned** — Shen Zhou association |
| CLM_WK_012b | probable/medium | work | **(empty)** | **No source assigned** — Dongzhuang Album |
| CLM_WK_012c | probable/medium | reception_label | **(empty)** | **No source assigned** — Suzhou saying |
| CLM_WK_013a | probable/medium | relationship | **(empty)** | **No source assigned** — Wen Zhengming student |
| CLM_WK_013b | probable/medium | reception_label | **(empty)** | **No source assigned** — Jingxian Shrine |
| CLM_WK_014 | confirmed/high | relationship | SRC_WK_004 | Wang Ao — solid (tomb inscription) |
| CLM_WK_015 | confirmed/high | relationship | SRC_WK_004, SRC_WK_006 | 五同会 — solid |
| CLM_WK_016 | needs_verification/low | career | **(empty)** | **No source assigned** |
| CLM_WK_017 | needs_verification/low | career | **(empty)** | **No source assigned** |
| CLM_WK_018 | needs_verification/low | identity | **(empty)** | **No source assigned** |

**Critical issue:** 8 of 18 claims have empty `source_ids`. While these are correctly marked `needs_verification/low`, they need either source assignment or remained flagged as unsupported. The pre-split compound claims (012a/b/c, 013a/b) were separated in hardening but lost their source assignments.

---

## 4. Relationship Audit

| Rel ID | Type | Related Person | Source | Status |
|--------|------|---------------|--------|--------|
| REL_WK_001 | documented_association | Shen Zhou | SRC_WK_005 (Baidu) | **Problem — D-level source for relationship claim** |
| REL_WK_002 | documented_teacher_student | Wen Zhengming | SRC_WK_005 (Baidu) | **Problem — D-level source** |
| REL_WK_003 | documented_association | Wang Ao | SRC_WK_004 | Correct — tomb inscription |
| REL_WK_004 | documented_association | (other) | — | Needs review |

**Assessment:** REL_WK_001 and REL_WK_002 rely on Baidu Baike (D-level). These relationships are historically correct (Shen Zhou painted Dongzhuang Album for Wu Kuan's father; Wen Zhengming studied under Wu Kuan) but need academic source support. Replace SRC_WK_005 with 明史, Dictionary of Ming Biography, or 沈周年谱.

---

## 5. Events Timeline

Basic timeline present. Key events: 1435 (birth), 1472 (zhuangyuan), career milestones, 1504 (death). Limited detail compared to richer packages (Wang Yangming, Pompey).

---

## 6. Works & Visual Media

| Category | Count | Status |
|----------|-------|--------|
| Works | 4 | 匏翁家藏集, 丛书堂书目, 吴文定公诗稿, writings |
| Visual media | 2 | All staging |

---

## 7. Compound Claim Check

Claims 012 and 013 were split into a/b/c sub-claims in hardening. Split is correct structurally, but sub-claims lost source assignments. Need to assign sources to each sub-claim.

---

## 8. Schema & JSON Validity

| Check | Result |
|-------|--------|
| JSON/JSONL parse | PASS |
| `person_id` consistent | PASS |
| All required files | PASS (11/11) |
| `source_ids` refer to existing sources | PASS (where present) |
| v2.3→v2.5 normalization | PASS (claims: text→claim_text; sources: level→reliability_level; relationships: rel_id→relationship_id) |

---

## 9. Source Level Calibration

| Issue | Status |
|-------|--------|
| SRC_WK_005 (Baidu) at D | Correct — but used as source for 2 relationships |
| No modern academic monograph (B_high) | Gap — needs Dictionary of Ming Biography or similar |
| 明史 at A_candidate | Correct — juan number 184 present; promote to A with passage refs |

---

## 10. Confidence Calibration

| Status | Count | Notes |
|--------|-------|-------|
| confirmed/high | 5 | Dates and well-sourced career/relationship claims |
| probable/medium | 5 | Relationship interpretations and sub-claims |
| needs_verification/low | 8 | Empty source_ids — correctly flagged low confidence |

**Assessment:** Confidence calibration is honest. The 8 low-confidence claims correctly reflect missing source support.

---

## 11. Cross-Package Dependencies

| Related Person | Relationship | Package Status |
|----------------|-------------|----------------|
| Shen Zhou | documented_association | Collected (incoming) |
| Wen Zhengming | documented_teacher_student | Not yet collected |
| Wang Ao (王鏊) | documented_association | Not yet collected |

---

## 12. Visual Media Audit

2 entries, all staging. Before promotion: verify object IDs and rights.

---

## 13. Recommended Action

**Action:** `needs_substantial_source_work_before_merge`

**Required before merge:**
1. Assign source_ids to all 8 empty-source claims — if no source available, keep as needs_verification/low with review note
2. Replace Baidu (SRC_WK_005) as source for REL_WK_001 and REL_WK_002 with 明史 or Dictionary of Ming Biography
3. Promote 明史·吴宽传 (SRC_WK_001) from A_candidate to A with verified passage references
4. Add source_ids to split sub-claims (CLM_WK_012a/b/c, CLM_WK_013a/b)

**Recommended (not blocking):**
- Add a modern academic monograph on Ming Suzhou literary culture as B_high source
- Collect Wen Zhengming and Wang Ao for cross-validation
- Enrich events timeline with more detail

**Notes:** Wu Kuan is the weakest Chinese package. The 8 empty source_ids and Baidu-dependent relationships are significant gaps. This package should not merge until these are addressed.
