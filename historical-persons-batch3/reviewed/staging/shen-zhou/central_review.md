# Central Review: 沈周 (Shen Zhou)

**Reviewer:** MorphMind AI
**Date:** 2026-05-13
**Package:** `incoming/chinese/shen-zhou/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_SHEN_ZHOU` |
| **Name (ZH)** | 沈周 |
| **Name (EN)** | Shen Zhou |
| **Birth** | 1427 (宣德二年十一月二十一日) |
| **Death** | 1509 (正德四年) |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#1 (`collect/shen-zhou-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 native |

---

## 2. Source Inventory & Quality

| Source ID | Level | Type | Notes |
|-----------|-------|------|-------|
| SRC001 | A_candidate | Secondary monograph | Needs edition verification |
| SRC002 | A_candidate | Secondary literature | Needs passage refs |
| SRC003 | B | Academic article | Published, needs page refs |
| SRC004 | C | General web | Clue only; not sole support |
| SRC005 | C | Wikipedia | Clue only |
| SRC006 | D | General web | Flagged; should be removed or kept as clue_only |

**Assessment:** Weak source density (6 sources for 22 claims = 0.27 per claim). No `A`-level source. Two C and one D-level sources present. The primary 明史·隐逸传 biography is not represented as a discrete source — several claims likely trace to it but through secondary references.

---

## 3. Claim Quality Review

| Category | Count | Assessment |
|----------|-------|-----------|
| Identity | 4 | Standard biographical claims. Birth year discrepancy (1427 vs 1472) unresolved. |
| Career | 3 | Civil service claims well-sourced. |
| Works | 5 | Paintings and poetry correct. |
| Relationships | 4 | Remapped from "friend"/"close friend" to documented_association in hardening sprint. |
| Reception labels | 6 | "Wu School founder" correctly marked reception. "明四家" grouping correct. |

**Key issues:**
- C009 ("founder of Wu School"): correctly `status=reception` — no change needed.
- C014/C018: overstrong "close friends" wording replaced with `documented_association` in hardening sprint.
- C019: "close relationship" wording removed; teacher-student fact retained.
- Several `probable/medium` claims correctly represent uncertain relationship interpretations.

---

## 4. Relationship Audit

All 13 relationships remapped to v2.5 allowed types in hardening sprint:
- Family relationships (`grandfather`, `uncle`, `father`): correct.
- Teacher-student (`documented_teacher_student`): correct for Wen Zhengming, 陈宽 marked `probable_teacher_student`.
- `same_cultural_circle`: correctly used for Tang Yin, Qiu Ying (no direct evidence of personal relationship).
- `later_grouping_only`: correctly used for 明四家 grouping.

**No blocking issues.**

---

## 5. Events Timeline

Timeline entries present. Key dates: 1427 (birth), 1509 (death), civil service milestones, major painting dates. Birth year discrepancy noted as open question.

---

## 6. Works & Visual Media

| Category | Count | Status |
|----------|-------|--------|
| Works | 8 | Paintings with attributions |
| Visual media | 3 | All `staging` — museum object IDs unverified |

**Visual media status:** All entries need source holder + object ID verification before promotion from staging.

---

## 7. Compound Claim Check

Claims already pre-split in the canonical package. No compound claims detected in current validated state.

---

## 8. Schema & JSON Validity

| Check | Result |
|-------|--------|
| JSON/JSONL parse | PASS |
| `person_id` empty | PASS (consistent across all files) |
| All required files present | PASS (11/11) |
| `source_ids` all resolve | PASS |
| No confirmed/high on C/D only | PASS |
| Summary ≤ claim status | PASS (post-hardening) |

---

## 9. Source Level Calibration

| Issue | Status |
|-------|--------|
| SRC004 (C) used for confirmed claims | Needs review — downgrade claims or promote source |
| SRC006 (D) present | Remove or mark clue_only |
| No A-level source | Weakness — needs promotion from A_candidate |

---

## 10. Confidence Calibration

| Status | Count | Notes |
|--------|-------|-------|
| confirmed/high | ~8 | Reasonable for dates, career milestones |
| probable/medium | ~10 | Appropriate for relationship interpretations |
| reception | ~4 | Correctly used for later groupings |

**Assessment:** Confidence calibration is appropriate. No over-confident claims detected.

---

## 11. Cross-Package Dependencies

| Related Person | Relationship | Package Status |
|----------------|-------------|----------------|
| Wen Zhengming | documented_teacher_student | Not yet collected |
| Tang Yin | same_cultural_circle | Not yet collected |
| Qiu Ying | later_grouping_only (明四家) | Collected (incoming) |
| 陈宽 | probable_teacher_student | Not yet collected |

**Note:** 3 of 4 relationships link to persons not yet in the database. Central review of Shen Zhou can proceed, but cross-package validation will need those persons collected.

---

## 12. Visual Media Audit

All 3 entries at staging status. Before master promotion:
- Verify museum object IDs for portrait paintings
- Confirm rights/public domain status
- Cross-reference with owning institution catalogues

---

## 13. Recommended Action

**Action:** `merge_after_source_enrichment`

**Required before merge:**
1. Add 明史·隐逸传 as discrete A-level source with juan number
2. Promote at least one source from A_candidate to A with verified passage refs
3. Resolve birth year (1427 vs 1472) discrepancy with open question update
4. Remove or downgrade SRC006 (D-level) to clue_only

**Optional / deferred:**
- Collect Wen Zhengming, Tang Yin to cross-validate relationships
- Verify museum object IDs for visual media
