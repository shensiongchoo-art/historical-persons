# Central Review — Wen Zhengming (文徵明)

**Reviewer:** MorphMind AI
**Date:** 2026-05-15
**Branch:** `review/batch1-central-review-source-audit-v1`

---

## 1. Person Name and ID

- **Name:** 文徵明 / Wen Zhengming (formerly Wen Bi; art name: 衡山居士 Hengshan Jushi)
- **Person ID:** `P_CHN_MING_WEN_ZHENGMING`
- **Dates:** 1470-11 – 1559

## 2. Source Package Path

`incoming/chinese/wen-zhengming/`

## 3. Current Status

`ai_collected_unreviewed`

## 4. Validation Result

**PASSED** — all 11 required files present, JSONL valid, person_id consistent.

## 5. Master-Candidate Facts

- Birth: November 1470, Changzhou County, Suzhou Prefecture
- Death: 1559, age 90 sui
- Names: originally Wen Bi, courtesy Zhengming, later used Zhengming as primary name, art name Hengshan Jushi
- Repeatedly failed provincial and metropolitan examinations
- 1523: appointed Hanlin Academy Drafter (Daizhao) through suigong route
- Resigned shortly after, devoted himself to painting and calligraphy
- Excelled in landscape painting, small regular script (xiaokai), running script (xingshu)
- Authored 甫田集 (Futian Collection)

## 6. Staging-Only Facts

- Wen Zhengming studied painting under Shen Zhou — single source (SRC_WZM_007, needs_verification). Probable but needs primary evidence.
- Wen Zhengming had associations with Qiu Ying — single source. Collaborative interactions mentioned but specifics unclear.
- Wen Zhengming received mentorship from Wu Kuan — single source, specifics unverified.

## 7. Rejected or Unsafe Claims

None rejected. The following need caveats:

- **CLM_WZM_004** (Shen Zhou teacher relationship): Single B_high source that needs verification. Keep at `probable`.
- **CLM_WZM_012** (central Suzhou network position): Sweeping claim about relationships with 6 other persons. Some are documented (Wu Kuan), others are later-grouping-based (Xu Zhenqing).
- **CLM_WZM_013** (late style trend): Art-historical interpretation, not a confirmed fact.

## 8. Source Issues

| Source | Issue | Severity |
|--------|-------|----------|
| SRC_WZM_001 (明史·文苑传) | Exact juan/page in Zhonghua Shuju edition not verified | Low |
| SRC_WZM_004 (Palace Museum) | Museum object/accession IDs not confirmed | Medium |
| SRC_WZM_007 (academic paper) | Journal name, author, DOI need verification | Medium |
| SRC_WZM_005, SRC_WZM_006 | D-level — correctly marked clue_only | Info only |

**Source sufficiency:** 7 sources, 5 non-D. 0.36 non-D sources per claim — above the 0.30 threshold. Acceptable.

## 9. Relationship Issues

- **REL_WZM_001** (Shen Zhou): `probable_teacher_student` — correct type but needs primary evidence.
- **REL_WZM_002** (Tang Yin): `probable_association` — correct. Same birth year, both Suzhou.
- **REL_WZM_003** (Zhu Yunming): `probable_association` — correct but thin. 吴中四才子 is the primary grouping evidence.
- **REL_WZM_004** (Xu Zhenqing): `later_grouping_only` — **correct.** Important: Xu died at 32/33 when Wen was 41. Direct interaction evidence is limited.
- **REL_WZM_005** (Qiu Ying): `probable_association` — acceptable. Qiu Ying inscribed Wen's works.
- **REL_WZM_006** (Wu Kuan): `probable_association` — correct. Wu Kuan's mentorship is documented but specifics need verification.

**Note:** Wen Zhengming→Zhu Yunming is typed `probable_association` while Tang Yin→Zhu Yunming also uses `probable_association`. This is fine — Wen and Zhu were closer in age (11 years apart) than Xu Zhenqing was to anyone.

## 10. Event Issues

events.jsonl present. Not reviewed in detail in this pass.

## 11. Works/Artwork Issues

- 8+ works entries including 甫田集
- Palace Museum object IDs needed for painting verification
- Calligraphy works need collection location verification

## 12. Visual Media Issues

3 visual_media entries, all staging status. No blocking issues.

## 13. Reception/Legend/Fiction Separation

**Good.** The package correctly separates:
- 明四家 (CLM_WZM_010) — `reception_label`
- 吴中四才子 (CLM_WZM_011) — `reception_label`
- No fictional/legendary claims present (unlike Tang Yin, Wen Zhengming has no popular folklore overlay)

## 14. Recommended Cleanup Actions

1. Verify SRC_WZM_001: exact juan/page for Wen Zhengming biography in 明史·文苑传.
2. Verify SRC_WZM_007: journal name, author, DOI. Consider replacing with 文徵明年谱 (Zhou Daozhen, 2020, already present as SRC_WZM_003).
3. Verify SRC_WZM_004: Palace Museum object IDs.
4. Cross-reference Shen Zhou teacher relationship across multiple sources (Wen's own 甫田集 may contain evidence).

## 15. Staging Readiness

**Staging-acceptable with minor verification notes.** The package has correct schema, appropriate reception labeling, and cautious relationship typing. Source density (0.36 non-D per claim) is adequate. SRC_WZM_007 is the main verification gap. The Shen Zhou teacher relationship should ideally be cross-referenced but is widely accepted in art-historical literature.
