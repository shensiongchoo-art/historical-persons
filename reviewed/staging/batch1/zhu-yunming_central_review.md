# Central Review — Zhu Yunming (祝允明)

**Reviewer:** MorphMind AI
**Date:** 2026-05-15
**Branch:** `review/batch1-central-review-source-audit-v1`

---

## 1. Person Name and ID

- **Name:** 祝允明 / Zhu Yunming (courtesy: 希哲 Xizhe; art names: 枝山 Zhishan, 枝指生 Zhizhi Sheng)
- **Person ID:** `P_CHN_MING_ZHU_YUNMING`
- **Dates:** 1461 – 1527

## 2. Source Package Path

`incoming/chinese/zhu-yunming/`

## 3. Current Status

`ai_collected_unreviewed`

## 4. Validation Result

**PASSED** — all 11 required files present, JSONL valid, person_id consistent.

## 5. Master-Candidate Facts

- Birth: 1461, Changzhou County, Suzhou Prefecture
- Death: 1527
- Names: courtesy Xizhe, art names Zhishan and Zhizhi Sheng
- Passed provincial examination (juren)
- Served as magistrate of Xingning, Guangdong, and Vice-Prefect of Yingtian Prefecture
- Famous for cursive script (caoshu) calligraphy
- Authored 怀星堂集 (Huaixingtang Collection)
- Distinguished scholarly family: grandfather Zhu Hao (jinshi), maternal grandfather Xu Youzhen (Tianshun official)

## 6. Staging-Only Facts

- Zhu Yunming is counted among the great mid-Ming calligraphers with Wen Zhengming and Wang Chong — art-historical assessment from modern scholarship (SRC_ZYM_003, SRC_ZYM_006, SRC_ZYM_007).
- Zhu Yunming had personal associations with Tang Yin, Wen Zhengming, and Xu Zhenqing — specifics of these personal relationships are not fully documented; 吴中四才子 is a later literary classification.

## 7. Rejected or Unsafe Claims

None rejected. The following need caveats:

- **CLM_ZYM_008** (family background): Strong claim about Xu Youzhen as maternal grandfather. 明史 should confirm this but exact passage not verified. Currently `probable` — appropriate.
- **CLM_ZYM_009** (Suzhou associations): Vague claim about "交往" with three other persons. Source is SRC_ZYM_003 (needs_verification). Appropriate confidence level (`probable`).

## 8. Source Issues

| Source | Issue | Severity |
|--------|-------|----------|
| SRC_ZYM_001 (明史·文苑传) | Exact juan/page in Zhonghua Shuju edition not verified. Zhu Yunming's biography is appended to Xu Zhenqing's — passage reference needed. | Low |
| SRC_ZYM_003 (academic paper) | Journal name, author, DOI need verification | Medium |
| SRC_ZYM_004, SRC_ZYM_005 | D-level — correctly marked clue_only | Info only |

**Important correction:** Zhu Yunming was previously reported as having "only 5 sources." The actual source count is **7**, with **5 non-D sources**. This is moderate, not critically thin.

**Source sufficiency:** 7 sources, 5 non-D. 0.50 non-D sources per claim — well above the 0.30 threshold. Acceptable.

## 9. Relationship Issues

- **REL_ZYM_001** (Tang Yin): `probable_association` — correct. Early association documented in 明史.
- **REL_ZYM_002** (Wen Zhengming): `probable_association` — correct.
- **REL_ZYM_003** (Xu Zhenqing): `later_grouping_only` — **correct.** 吴中四才子 is the primary grouping.

Relationships are thin (only 3 entries). Missing: Zhu Yunming→Wang Chong (calligraphy peer, mentioned in SRC_ZYM_007) and possibly Zhu Hao/Xu Youzhen family relationships. These can be added later when family relationship types are standardized.

## 10. Event Issues

events.jsonl present. Not reviewed in detail in this pass.

## 11. Works/Artwork Issues

- 怀星堂集 is the primary work
- Calligraphy works listed but no museum/collection IDs verified
- Major calligraphy pieces (e.g., 草书赤壁赋, 草书杜甫诗卷) need collection location verification

## 12. Visual Media Issues

2 visual_media entries, all staging status. No blocking issues.

## 13. Reception/Legend/Fiction Separation

**Good.** The package correctly separates:
- Literary-historical Zhu Yunming (吴中四才子, CLM_ZYM_007) — `reception_label`
- Popular "Zhu Zhishan" (CLM_ZYM_010) — `reception_label`, explicitly stating the comedic character is "distinct from the historical Zhu Yunming"

The folk Zhu Zhishan claim (CLM_ZYM_010) has no source_ids — this is correct since the claim itself is about the existence of a non-historical image. However, a source documenting this folk tradition would strengthen the claim.

## 14. Recommended Cleanup Actions

1. Verify SRC_ZYM_001: exact juan/page for Zhu Yunming's biography (appended to Xu Zhenqing's in 明史·文苑传二, juan 286).
2. Verify SRC_ZYM_003: journal name, author, DOI for the calligraphy studies paper.
3. Add collection IDs for major Zhu Yunming calligraphic works.
4. Consider adding a relationship to Wang Chong (王宠) — mentioned in SRC_ZYM_007 as a peer calligrapher.
5. Source the folk "Zhu Zhishan" claim with at least one reference documenting the tradition.

## 15. Staging Readiness

**Staging-acceptable with minor verification notes.** Previously flagged as the weakest package due to source count, but the actual source base (7 sources, 5 non-D) is moderate. Source density (0.50 per claim) is above average for this batch. The academic paper verification (SRC_ZYM_003) and calligraphy collection IDs are the main gaps. Reception/fiction separation is well-handled. Can be used for staging.
