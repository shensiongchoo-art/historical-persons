# Central Review: 王阳明 (Wang Yangming / Wang Shouren)

**Reviewer:** MorphMind AI
**Date:** 2026-05-13
**Package:** `incoming/chinese/wang-yangming/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_WANG_YANGMING` |
| **Name (ZH)** | 王阳明 / 王守仁 |
| **Name (EN)** | Wang Yangming / Wang Shouren |
| **Birth** | 1472 (成化八年九月三十日) |
| **Death** | 1529 (嘉靖七年十一月二十九日) |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#4 (`collect/wang-yangming-and-pompey-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 native |

---

## 2. Source Inventory & Quality

| Source ID | Level | Type | Notes |
|-----------|-------|------|-------|
| SRC001 | A_candidate | 明史·王守仁传 | Official biography; needs juan/passage refs |
| SRC002 | A_candidate | 传习录 | Primary text; needs edition/section refs |
| SRC003 | A_candidate | 大学问 | Primary text; needs edition refs |
| SRC004 | A_candidate | 王文成公全书/王阳明全集 | Collected works; needs volume/page refs |
| SRC005 | A_candidate | 明儒学案 | Ming-Qing scholarly work; needs edition |
| SRC006–010 | C | Wikipedia, Baidu, general web | 5 C-level sources — clue only |
| SRC011–013 | B | Modern scholarship | Academic sources |
| SRC014 | B (placeholder) | Japanese Yangmingism | **Placeholder — no real monograph cited** |
| SRC015 | A_candidate | Dictionary of Ming Biography | Needs exact page refs |

**Assessment:** 15 sources for 37 claims (0.41/claim). SRC014 is the critical gap — a placeholder source for Japanese Yangmingism with no real monograph behind it. 5 C-level sources excessive; claims traceable to them need academic source support. A_candidate sources need specific edition/passage refs promoted to A.

---

## 3. Claim Quality Review

| Category | Count | Assessment |
|----------|-------|-----------|
| Identity | 5 | Dates, family, birthplace — solid |
| Career/philosophy | 12 | Core achievements well-documented |
| Military | 6 | Ning rebellion, southern campaigns — well-sourced |
| Reception labels | 8 | "陆王心学", "龙场悟道" correctly reception |
| Relationships | 3 | Teacher-student, family — correct |
| Unsourced/weak | 3 | C025–C026 depend on SRC014 placeholder |

**Key issues:**
- C025–C026 (Japanese Yangmingism): depend on SRC014 placeholder — should be downgraded to needs_verification until real source cited.
- C027: `needs_verification` — correctly flagged.
- "龙场悟道" correctly marked as reception (the event happened; the framing label is later).
- "陆王心学" correctly as reception_label (R002 had philosophical_predecessor → reception_label fix).

---

## 4. Relationship Audit

| Rel ID | Type | Related Person | Status |
|--------|------|---------------|--------|
| R001 | family | 王华 (father) | Correct |
| R002 | reception_label | 陆九渊 | Correct (was philosophical_predecessor, fixed to reception_label) |
| R003–005 | documented_teacher_student | Various disciples | Correct |
| R006 | documented_association | Tang Yin | Correct — no close friendship evidence |
| R007–008 | family/other | Various | Correct |

**Assessment:** Relationship types compliant with v2.5. R002 especially notable: the 陆九渊→王阳明 transmission is a later scholarly construct, not a direct relationship — correctly reception_label. Tang Yin correctly absent from close-friendship claims.

---

## 5. Events Timeline

Well-structured timeline. Key events: 1472 (birth), 1499 (jinshi), 1506 (廷杖 + exile), 1508 (龙场), 1516–1519 (南赣 + Ning rebellion), 1527–1528 (Guangxi), 1529 (death). Dates generally accurate.

---

## 6. Works & Visual Media

| Category | Count | Status |
|----------|-------|--------|
| Works | 3 | 传习录, 大学问, 王文成公全书 |
| Visual media | 3 | All staging — needs museum/source verification |

---

## 7. Compound Claim Check

Compound claims pre-split in PR#4: name titles, Ning rebellion, Tianquan Bridge (天泉桥), Four-Sentence Teaching (四句教). All properly suffixed (a/b/c pattern).

---

## 8. Schema & JSON Validity

| Check | Result |
|-------|--------|
| JSON/JSONL parse | PASS (curly-quote fix applied in hardening) |
| `person_id` consistent | PASS |
| All required files | PASS (11/11) |
| `source_ids` resolve | PASS |
| No confirmed/high on C-only | PASS |
| Summary ≤ claim status | PASS |

---

## 9. Source Level Calibration

| Issue | Status |
|-------|--------|
| SRC014 is placeholder | **BLOCKING** — replace with real monograph |
| 5 C-level sources | Reduce; promote claims to A/A_candidate sources |
| A_candidate without passage refs | Promote to A with verified citations |

---

## 10. Confidence Calibration

| Status | Count | Notes |
|--------|-------|-------|
| confirmed/high | ~19 | Core biographical and philosophical claims well-supported |
| probable/medium | ~10 | Appropriate for interpretive and attribution claims |
| reception | ~7 | Correctly used for later historiographical labels |
| needs_verification | 1 (C027) | Correctly flagged |

**Assessment:** Confidence calibration is appropriate. C025–C026 should be downgraded from their current status if SRC014 placeholder is not replaced.

---

## 11. Cross-Package Dependencies

| Related Person | Relationship | Package Status |
|----------------|-------------|----------------|
| 王华 (father) | family | Not yet collected |
| 徐爱 (disciple) | documented_teacher_student | Not yet collected |
| Tang Yin | documented_association | Not yet collected |
| Zhu Yunming | (correctly absent) | Not yet collected |

---

## 12. Visual Media Audit

All 3 entries staging. Needs museum/source holder verification. The standard portrait of Wang Yangming is widespread but its provenance needs confirmation.

---

## 13. Recommended Action

**Action:** `merge_after_source_fix` (SRC014 replacement is blocking)

**Required before merge:**
1. Replace SRC014 placeholder with Julia Ching, *To Acquire Wisdom: The Way of Wang Yangming* (Columbia UP, 1976) or equivalent monograph with specific page refs
2. Promote at least 明史·王守仁传 (SRC001) from A_candidate to A with verified 卷195 passage refs
3. Promote 传习录 (SRC002) from A_candidate to A with edition details (上海古籍出版社, 1992)
4. Downgrade C025–C026 if SRC014 is not promptly replaced

**Optional / deferred:**
- Cross-reference specific 传习录 sections (上/中/下) for key claims
- Reduce C-level sources by promoting claims to academic sources
- Collect core disciples (徐爱, 钱德洪) for cross-validation
