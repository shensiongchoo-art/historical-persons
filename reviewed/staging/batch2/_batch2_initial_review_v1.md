# Batch 2 Initial Review v1

**Branch:** `review/batch2-initial-review-v1`
**Date:** 2026-05-16
**Author:** MorphMind AI
**Status:** Review complete — PR #28 is mergeable with caveats

---

## 1. PR Status Summary

| PR | Title | State |
|----|-------|-------|
| #24 | Batch 1 claims accuracy audit — 13 fixes | **MERGED** |
| #25 | Xu Zhenqing source enrichment | **MERGED** |
| #26 | Batch 1 final status report | **MERGED** |
| #28 | Batch 2 core network collection — 7 persons | **OPEN** (mergeable) |

---

## 2. Package Inventory

| # | Person | Person ID | Folder | Claims | Sources | Non-D | Validation |
|---|--------|-----------|--------|--------|---------|-------|------------|
| 1 | Li Dongyang | P_CHN_MING_LI_DONGYANG | chinese/li-dongyang/ | 10 | 6 | 4 | PASSED |
| 2 | Wang Ao | P_CHN_MING_WANG_AO | chinese/wang-ao/ | 8 | 4 | 2 | PASSED |
| 3 | Li Mengyang | P_CHN_MING_LI_MENGYANG | chinese/li-mengyang/ | 8 | 6 | 4 | PASSED |
| 4 | He Jingming | P_CHN_MING_HE_JINGMING | chinese/he-jingming/ | 10 | 6 | 4 | PASSED |
| 5 | Lepidus | P_WEST_LATE_REPUBLIC_LEPIDUS | western/lepidus/ | 9 | 4 | 3 | PASSED |
| 6 | Octavia Minor | P_WEST_LATE_REPUBLIC_OCTAVIA_MINOR | western/octavia-minor/ | 9 | 4 | 3 | PASSED |
| 7 | Sextus Pompey | P_WEST_LATE_REPUBLIC_SEXTUS_POMPEY | western/sextus-pompey/ | 9 | 5 | 4 | PASSED |

**Total: 63 claims | 35 sources (24 non-D) | all PASSED**

---

## 3. Source Quality Assessment

### Strong (ready for staging)
- **Lepidus:** Gruen (1974), CAH IX (1994), Syme (1939) — all real academic works. Augustan bias explicitly flagged on C009.
- **Octavia Minor:** Same quality as Lepidus. Moralized Roman portrayal correctly framed as reception_label (C009). Political role foregrounded over "wronged wife" narrative.
- **Sextus Pompey:** Powell & Welch (2002) cited. "Pirate" label deconstructed as Augustan propaganda (C008). "Commander/海军指挥官" used instead.

### Adequate with caveats
- **He Jingming:** 明史 + DMB + Cambridge History + 大复集 (四库全书). Stronger than Li Mengyang. DMB and Cambridge History are verified academic works. 明史 and 大复集 need exact juan/page/edition verification.
- **Wang Ao:** Only 2 non-D sources (明史 + DMB), but claims are all basic identity/career facts adequately supported by 明史. Thin but honest. DMB page numbers need verification.
- **Li Dongyang:** 明史 + 李东阳集 (周寅宾点校 2008) + 钱振民年谱 (1995). SRC_LDY_003 (Chaling school monograph) needs_verification. CLM_LDY_006, 008, 010 depend on it.

### Needs source enrichment
- **Li Mengyang:** **CRITICAL.** Only 1 verified source (SRC_LMY_001 明史). SRC_LMY_002 (collected works), SRC_LMY_003 (academic monograph), SRC_LMY_004 (年谱) all have `needs_verification`. CLM_LMY_005-008 depend on unverified sources. This mirrors the Xu Zhenqing situation in Batch 1.

---

## 4. Claim Risk Assessment

| Risk | Packages | Detail |
|------|----------|--------|
| **HIGH** | Li Mengyang | CLM_LMY_005 (archaist manifesto), 006 (前七子 leader), 007 (Li Dongyang challenge), 008 (Li-He debate) all depend on SRC_LMY_003 (needs_verification) |
| MEDIUM | Li Dongyang | CLM_LDY_006 (Chaling school), 008 (transitional figure), 010 (Former Seven Masters reaction) depend on SRC_LDY_003 (needs_verification) |
| LOW | Wang Ao | All claims are identity/career facts from 明史. No controversial claims. |
| LOW | He Jingming | CLM_C008-C010 are reception_label. Core identity claims from 明史 + DMB. |
| LOW | Lepidus | C009 is reception_label. Core claims from Gruen/CAH/Syme. |
| LOW | Octavia Minor | C009 is reception_label. Core claims from CAH/Syme. |
| LOW | Sextus Pompey | C008-C009 are reception_label. Core claims from Gruen/Powell/CAH. |

---

## 5. Relationship Assessment

| Package | Relationships | Risk |
|---------|--------------|------|
| Li Dongyang | Wu Kuan (jinshi cohort), Wang Ao (court), Li Mengyang (literary_context) | Low — all documented, no inferred friendship |
| Wang Ao | Wu Kuan (Five Commonalities), Li Dongyang (court), Liu Jin (opposition) | Low — documented associations |
| Li Mengyang | Xu Zhenqing (前七子), He Jingming (Li-He debate), Li Dongyang (literary_context) | Low — well-documented |
| He Jingming | Li Mengyang, Xu Zhenqing, Bian Gong (all 前七子) | Low — well-documented |
| Lepidus | Caesar, Antony, Augustus (all triumvir/political) | Low — documented political relationships |
| Octavia Minor | Augustus (sibling), Antony (spouse), Marcellus (spouse), Cleopatra (dynastic_rival) | Low — documented; "dynastic_rival" type is reception caveated |
| Sextus Pompey | Pompey the Great (parent_child), Augustus (opponent), Antony (opponent), Lepidus (opponent) | Low — documented |

**No fabricated or inferred relationships detected.**

---

## 6. Rule Compliance

| Rule | Status | Notes |
|------|--------|-------|
| Exactly 7 persons, no extras | ✅ | |
| 11 files per package | ✅ | |
| Wikipedia/Baidu D/clue_only | ✅ | No D source used as sole support for confirmed claims |
| Later groupings → reception_label | ✅ | 前七子, 李何之争 all correctly labeled |
| No inferred friendship/alliance | ✅ | documented_association, literary_context, opponent used |
| Visual media → staging_only | ✅ | All needs_verification, staging_only |
| BCE dates correct | ✅ | Western packages have precise era/place/precision fields |
| One claim = one fact | ✅ | No compound claims detected |
| All source_ids in claims exist in sources.jsonl | ✅ | Cross-checked for all 7 packages |

---

## 7. Schema Inconsistency Note

Western packages (generated by specialist scout) use a richer schema than Chinese packages (generated by agent directly):

| Field | Chinese packages | Western packages |
|-------|-----------------|------------------|
| claim_id | CLM_LDY_001 format | C001 format |
| source_id | SRC_LDY_001 format | SRC001 format |
| Date object | `birth.year_display` | `date.year_display + era + place + precision` |
| Confidence | `confidence: confirmed/probable/reception` | Same but with additional `claim_type` and `review_note` |
| Source fields | `source_type, reliability_level, citation_detail` | Additional `author, language, used_for_claim_ids` |

**Both pass validation.** The richer Western schema is actually superior — it provides more structured data for downstream use. Chinese packages should be normalized to match in a future hardening pass.

---

## 8. Overall Verdict

| Package | Recommendation |
|---------|---------------|
| Li Dongyang | **Accept.** Minor source gap (SRC_LDY_003). Address in source verification sprint. |
| Wang Ao | **Accept.** Thin but honest. 2 non-D sources adequate for basic claims. |
| Li Mengyang | **Accept with urgent follow-up.** Needs the same treatment Xu Zhenqing received. Source enrichment sprint ASAP. |
| He Jingming | **Accept.** Well-sourced. Verification needed for 明史/大复集 exact references. |
| Lepidus | **Accept.** Excellent quality. Model package for thin-sourced Western figures. |
| Octavia Minor | **Accept.** Excellent quality. Reception framing properly handled. |
| Sextus Pompey | **Accept.** Excellent quality. Augustan propaganda explicitly deconstructed. |

---

## 9. Merge Recommendation

**PR #28 should be merged.** All 7 packages are staging-acceptable. The Li Mengyang source gap is real but not blocking — the package correctly marks sources as needs_verification and is honest about its limitations. This approach (thin-but-honest) is preferable to overclaiming source strength.

### Before merge, fix or note:
1. **Li Mengyang SRC_LMY_002:** Marked as A_candidate but citation_detail is "needs_verification." Downgrade to B_high or change to `needs_verification` status. An A_candidate source must have verified citation details.
2. **Li Dongyang SRC_LDY_003:** Same issue — B_high with needs_verification. Acceptable for staging but flag for enrichment sprint.

### Post-merge action:
Source verification sprint for Li Mengyang — search CNKI for:
- 李梦阳集 modern annotated edition (editor, publisher, year)
- Academic monograph on Li Mengyang and Former Seven Masters
- 李梦阳年谱 author and publication details

---

## 10. Remaining Blockers

| Blocker | Status |
|---------|--------|
| PR #24 merged | ✅ |
| PR #25 merged | ✅ |
| PR #26 merged | ✅ |
| PR #28 review | ✅ This document |
| Li Mengyang source gap | ⚠️ Accept for staging, address in sprint |
