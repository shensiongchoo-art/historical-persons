# Central Review: 仇英 (Qiu Ying)

**Reviewer:** MorphMind AI
**Date:** 2026-05-13
**Package:** `incoming/chinese/qiu-ying/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_001_QIU_YING` |
| **Name (ZH)** | 仇英 |
| **Name (EN)** | Qiu Ying |
| **Birth** | ca. 1494 (disputed: 1482–1505 range) |
| **Death** | ca. 1552 |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#5 (`collect/qiu-ying-and-augustus-v2-5`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized from v2.3 in hardening sprint) |

---

## 2. Source Inventory & Quality

| Category | Count | Notes |
|----------|-------|-------|
| Modern academic | ~8 | Laing (1999), Ngan (2016), Cahill, etc. — strong |
| Chinese primary | ~6 | Dong Qichang, Wang Shizhen, Wen Zhengming inscriptions |
| Museum catalogues | ~4 | Palace Museum, National Palace Museum, Cleveland |
| 明清画史笔记 | 0 (gap) | **无声诗史, 明画录, 图绘宝鉴续编 missing as discrete entries** |
| Encyclopedic | 2 | Wikipedia, Baidu — clue only |
| D-level | 1 | General web — flag |

**Assessment:** 23 sources for 34 claims (0.68/claim) — best source density among Chinese packages. Strong modern art-historical scholarship. Critical gap: the three 明清画史笔记 texts are cited in scholarship for Qiu Ying but not represented as discrete source entries in the package.

---

## 3. Claim Quality Review

| Category | Count | Assessment |
|----------|-------|-----------|
| Identity | 5 | Birth/death dates carefully flagged as disputed |
| Artistic training | 4 | 周臣 teacher-student solid; Wen Zhengming collaboration documented |
| Career/patronage | 6 | Cahill's "no self-written texts" thesis correctly applied |
| Works/attributions | 12 | Major works listed with museum locations |
| Reception labels | 4 | "明四家" correctly reception; no overclaiming |
| Relationships | 3 | Shen Zhou correctly later_grouping_only |

**Key issues:**
- No claims overstate — Qiu Ying's low social status and lack of self-written texts are correctly represented.
- "明四家" correctly as reception_label — he is the only professional painter in that grouping.
- Works list needs systematic real/forgery distinction.

---

## 4. Relationship Audit

| Rel ID | Type | Related Person | Status |
|--------|------|---------------|--------|
| REL_QY_001 | documented_teacher_student | 周臣 (Zhou Chen) | Correct |
| REL_QY_002 | documented_association | 文徵明 (Wen Zhengming) | Correct — documented collaboration, not formal teacher-student |
| REL_QY_003 | same_cultural_circle | 唐寅 (Tang Yin) | Correct — both Zhou Chen students, no direct evidence of friendship |
| REL_QY_004 | later_grouping_only | 沈周 (Shen Zhou) | Correct — Shen Zhou died when Qiu Ying was ~15; only indirect influence |

**Assessment:** All relationships correctly typed. REL_QY_004 particularly important: the hardening sprint changed `influence` → `later_grouping_only` because Shen Zhou and Qiu Ying never met.

---

## 5. Events Timeline

Timeline correctly reflects sparse biographical data. Key events: approximate birth (ca. 1494), apprenticeship to Zhou Chen, major works dated by inscription, death (ca. 1552). Birth/death uncertainty correctly represented.

---

## 6. Works & Visual Media

| Category | Count | Status |
|----------|-------|--------|
| Works | 13 | Strong — includes museum object IDs for major works |
| Visual media | 4 | All staging — museum verification incomplete |

**Works highlights:** 赵孟頫写经换茶图 (Cleveland), 汉宫春晓图 (Palace Museum, Taipei), 清明上河图 copy (Liaoning Provincial Museum). Cleveland Art Museum object ID unverified — needs online catalogue check.

---

## 7. Compound Claim Check

All compound claims pre-split. No combined facts detected.

---

## 8. Schema & JSON Validity

| Check | Result |
|-------|--------|
| JSON/JSONL parse | PASS |
| `person_id` consistent | PASS |
| All required files | PASS (11/11) |
| `source_ids` resolve | PASS |
| v2.3→v2.5 normalization | PASS |
| Claims: text_zh/en + category → claim_text_zh/en + claim_type | PASS |
| Sources: level → reliability_level | PASS |
| Relationships: rel_id → relationship_id | PASS |

---

## 9. Source Level Calibration

| Issue | Status |
|-------|--------|
| 明清画史笔记 missing | **GAP** — add as discrete A/A_candidate sources |
| D-level source present | Flag; remove or mark clue_only |
| Modern scholarship levels correct | Laing, Ngan, Cahill at B_high — appropriate |

---

## 10. Confidence Calibration

| Status | Count | Notes |
|--------|-------|-------|
| confirmed/high | ~10 | Museum-documented works, verified inscriptions |
| probable/medium | ~15 | Attribution claims, date ranges — appropriately cautious |
| reception | ~4 | "明四家" and later labels |
| needs_verification | ~5 | Undocumented attributions, uncertain dates |

**Assessment:** Appropriate caution for a figure with no self-written texts. The "probable/medium" on many art-historical claims is correct scholarly practice.

---

## 11. Cross-Package Dependencies

| Related Person | Relationship | Package Status |
|----------------|-------------|----------------|
| 周臣 (Zhou Chen) | documented_teacher_student | Not yet collected |
| 文徵明 (Wen Zhengming) | documented_association | Not yet collected |
| 唐寅 (Tang Yin) | same_cultural_circle | Not yet collected |
| 沈周 (Shen Zhou) | later_grouping_only | Collected (incoming) |

---

## 12. Visual Media Audit

4 entries, all staging. Cleveland 写经换茶图, Palace Museum 汉宫春晓图, and two others. Before promotion: verify museum object IDs, confirm public domain/publication rights.

---

## 13. Recommended Action

**Action:** `merge_after_source_fix`

**Required before merge:**
1. Add 无声诗史 (Jiang Shaoshu), 明画录 (Xu Qin), 图绘宝鉴续编 as discrete A_candidate source entries with edition details
2. Verify Cleveland Art Museum object ID for 赵孟頫写经换茶图 in online catalogue
3. Remove or flag D-level source as clue_only

**Recommended (not blocking):**
- Fill remaining museum object IDs for major works
- Cross-reference works with systematic forgery literature
- Collect 周臣 and 文徵明 for cross-validation

**Notes:** Qiu Ying is the best-structured Chinese package. Source enrichment (明清画史笔记) is the only substantial gap. No blocking issues.
