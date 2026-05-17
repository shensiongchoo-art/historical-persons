# Central Review — Tang Yin (唐寅)

**Reviewer:** MorphMind AI
**Date:** 2026-05-15
**Branch:** `review/batch1-central-review-source-audit-v1`

---

## 1. Person Name and ID

- **Name:** 唐寅 / Tang Yin (courtesy: 伯虎 Bohu, 子畏 Ziwei; art names: 六如居士 Liuru Jushi, 桃花庵主 Taohua Anzhu)
- **Person ID:** `P_CHN_MING_TANG_YIN`
- **Dates:** 1470 – 1524-01-07

## 2. Source Package Path

`incoming/chinese/tang-yin/`

## 3. Current Status

`ai_collected_unreviewed`

## 4. Validation Result

**PASSED** — all 11 required files present, JSONL valid, person_id consistent.

## 5. Master-Candidate Facts

- Birth: 1470, Wu County, Suzhou Prefecture (明史·文苑传 — needs exact juan/page)
- Death: 1524-01-07 (second day of 12th month, Jiajing 2)
- Name: Tang Yin, courtesy Bohu and Ziwei; art names Liuru Jushi and Taohua Anzhu
- 1498 Yingtian provincial examination: first place (jieyuan)
- 1499 metropolitan exam scandal: imprisoned, demoted to clerk, refused, returned to Suzhou
- Supported himself through painting sales
- Landscape, figure, and bird-and-flower painter
- Left collected works: 六如居士集

## 6. Staging-Only Facts

- Tang Yin studied painting under Zhou Chen — only one source (SRC_TY_007, needs_verification). Probable but unconfirmed.
- Tang Yin's painting style blended Southern Song academy traditions with literati conventions — interpretive claim, needs art-historical verification.
- Tang Yin had close associations with all other "Four Talents" — mostly probable, specifics unverified.

## 7. Rejected or Unsafe Claims

None rejected. All claims are within acceptable bounds. The following need caveats:

- **CLM_TY_012** (teacher-student with Zhou Chen): Source is SRC_TY_007 which needs_verification. Confidence should remain `probable`.
- **CLM_TY_016** (Suzhou literati network position): Mix of confirmed and probable elements. The claim text's "重要地位" is interpretive.

## 8. Source Issues

| Source | Issue | Severity |
|--------|-------|----------|
| SRC_TY_001 (明史·文苑传) | Exact juan/page in Zhonghua Shuju edition not verified | Low |
| SRC_TY_004 (Palace Museum) | Museum object/accession IDs not confirmed | Medium |
| SRC_TY_007 (academic paper) | Journal name, author, DOI all need verification | Medium |
| SRC_TY_005, SRC_TY_006 | D-level (Baidu/Wikipedia) — correctly marked clue_only | Info only |

**Source sufficiency:** 8 sources, 5 non-D. 0.28 non-D sources per claim — below the 0.30 threshold. Acceptable but thin.

## 9. Relationship Issues

- **REL_TY_001** (Shen Zhou): `probable_association` — correct. 明四家 is an art-historical grouping.
- **REL_TY_002** (Wen Zhengming): `probable_association` — correct. Both same year, both Suzhou, literary exchanges documented.
- **REL_TY_003** (Zhu Yunming): `probable_association` — correct. Early association documented in 明史.
- **REL_TY_004** (Xu Zhenqing): `later_grouping_only` — correct. Xu died young (33) at age 32 when Tang was 41. Limited interaction window.
- **REL_TY_005** (Zhou Chen): Empty related_person_id. `probable_teacher_student` — needs primary source verification.
- **REL_TY_006** (Qiu Ying): `later_grouping_only` — correct. 明四家 is an art-historical classification.

**Assessment:** Relationship types are well-chosen. 吴中四才子 is correctly handled as later grouping, not real organization.

## 10. Event Issues

events.jsonl present. Not reviewed in detail in this pass.

## 11. Works/Artwork Issues

- 8 works entries including 王蜀宫妓图 (Court Ladies of the Former Shu) at Palace Museum
- Museum object IDs needed for verification
- Not all attributed works are universally accepted as authentic

## 12. Visual Media Issues

3 visual_media entries, all staging status. No blocking issues.

## 13. Reception/Legend/Fiction Separation

**Excellent.** The package correctly separates:
- Art-historical Tang Yin (明四家, CLM_TY_010) — `reception_label`
- Literary Tang Yin (吴中四才子, CLM_TY_011) — `reception_label`
- Popular Tang Yin (唐伯虎点秋香, CLM_TY_015) — `legendary`

The legend claim (CLM_TY_015) explicitly states the Qiuxiang story is fictional with no historical basis. The exam scandal dispute (CLM_TY_006) is correctly marked `disputed`.

## 14. Recommended Cleanup Actions

1. Verify SRC_TY_001 passage: 明史·文苑传二, juan 286, Tang Yin biography page numbers.
2. Verify SRC_TY_004: Palace Museum object/accession IDs for 王蜀宫妓图 and other Tang Yin paintings.
3. Verify SRC_TY_007: journal name, author, and DOI for the academic paper.
4. Promote Zhou Chen teacher relationship from SRC_TY_007-only to multi-source if possible.

## 15. Staging Readiness

**Staging-acceptable with minor verification notes.** The package has correct schema, proper reception separation, and cautious relationship typing. Source density is slightly below threshold (0.28 non-D sources per claim) but claims are well-formulated and appropriately caveated. The Zhou Chen relationship and SRC_TY_007 are the main verification gaps. Can be used for staging with the understanding that 3 sources need verification follow-up.
