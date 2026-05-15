# Central Review — Xu Zhenqing (徐祯卿)

**Reviewer:** MorphMind AI
**Date:** 2026-05-15
**Branch:** `review/batch1-central-review-source-audit-v1`

---

## 1. Person Name and ID

- **Name:** 徐祯卿 / Xu Zhenqing (courtesy: 昌谷 Changgu / 昌国 Changguo)
- **Person ID:** `P_CHN_MING_XU_ZHENQING`
- **Dates:** 1479 – 1511 (age 33)

## 2. Source Package Path

`incoming/chinese/xu-zhenqing/`

## 3. Current Status

`ai_collected_unreviewed`

## 4. Validation Result

**PASSED** — all 11 required files present, JSONL valid, person_id consistent.

## 5. Master-Candidate Facts

- Birth: 1479, Wu County, Suzhou Prefecture
- Death: 1511, age 33
- Names: courtesy Changgu/Changguo
- 1505: earned jinshi degree
- Known for poetry, authored 迪功集 (Digong Collection)
- Listed among 吴中四才子 in 明史·文苑传 (the passage: 祯卿少与祝允明、唐寅、文徵明齐名，号吴中四才子)
- Classified among Ming Former Seven Masters (前七子) in literary history

## 6. Staging-Only Facts

- Xu Zhenqing had personal interactions with Tang Yin, Wen Zhengming, Zhu Yunming — all relationships are `later_grouping_only`. The 明史 passage confirms the grouping but does not document personal interactions.
- Xu Zhenqing had literary exchanges with Li Mengyang — single source (SRC_XZQ_003, needs_verification).
- Xu Zhenqing's network depth and breadth — CLM_XZQ_010 explicitly cautions against overstating it. This is a strength of the package.

## 7. Rejected or Unsafe Claims

None rejected. The following need caveats:

- **CLM_XZQ_008** (Li Mengyang relationship): Single source (SRC_XZQ_003, needs_verification). Confidence marked `probable` — appropriate.
- **CLM_XZQ_009** (Suzhou network): Correctly states that 吴中四才子 is a "后世归类." Cross-check: 明史 explicitly groups Xu with the other three, making the grouping itself a confirmed historical fact. The uncertainty is about the nature of personal relationships, not the grouping.

## 8. Source Issues

| Source | Issue | Severity |
|--------|-------|----------|
| SRC_XZQ_001 (明史·文苑传) | Exact juan/page in Zhonghua Shuju edition not verified. The specific passage about 吴中四才子 is cited in notes but page number is unconfirmed. | Low |
| SRC_XZQ_003 (academic paper) | Journal name, author, DOI need verification | High |
| SRC_XZQ_004, SRC_XZQ_005 | D-level — correctly marked clue_only | Info only |

**Source sufficiency:** **CRITICAL.** Only 5 sources total, 3 non-D. 0.30 non-D sources per claim — exactly at the minimum threshold. This is the thinnest source base in the entire 15-package repository.

## 9. Relationship Issues

- **REL_XZQ_001** (Tang Yin): `later_grouping_only` — correct. Tang was 9 years older. Limited interaction window (Xu was 20-32 during Tang's prime).
- **REL_XZQ_002** (Wen Zhengming): `later_grouping_only` — correct. Wen was also 9 years older.
- **REL_XZQ_003** (Zhu Yunming): `later_grouping_only` — correct. Zhu was 18 years older.
- **REL_XZQ_004** (Li Mengyang): `probable_association` — incorrect type. Li Mengyang is a literary peer in 前七子, not just a "probable" association. However, the specifics of their interaction are indeed uncertain, so `probable_association` is defensible.

**Assessment:** All three 吴中四才子 relationships are correctly typed as `later_grouping_only`. This is appropriate given Xu's early death (age 33) and the age gap with the other three.

## 10. Event Issues

events.jsonl present. Not reviewed in detail in this pass.

## 11. Works/Artwork Issues

- 迪功集 is the primary work
- Modern annotated edition (范志新编年校注, 2009) is cited — this is strong
- Additional works may include 谈艺录 (mentioned in SRC_XZQ_002 notes)

## 12. Visual Media Issues

2 visual_media entries, all staging status. No blocking issues. Xu Zhenqing is less visually documented than Tang Yin or Wen Zhengming.

## 13. Reception/Legend/Fiction Separation

**Good.** The package correctly labels:
- 吴中四才子 (CLM_XZQ_006) — `reception_label`
- Former Seven Masters (CLM_XZQ_007) — `reception_label`

No legendary material exists for Xu Zhenqing (unlike Tang Yin or Zhu Yunming). The package does not invent any. The explicit caveat about limited interaction window (CLM_XZQ_010) is a strength.

## 14. Recommended Cleanup Actions

1. **Add 1-2 academic sources (HIGHEST PRIORITY).** The 3 non-D source base is critically thin. At minimum:
   - One additional academic paper or monograph on Xu Zhenqing's poetry
   - Or: a Chinese literary history reference work that provides more detail on 前七子
2. Verify SRC_XZQ_003: journal name, author, DOI.
3. Verify SRC_XZQ_001: exact juan/page for Xu Zhenqing's biography in 明史·文苑传. The specific passage about 吴中四才子 is already cited in the source notes — this is a good lead.
4. Consider whether 明史's grouping passage itself can serve as direct evidence for the 吴中四才子 grouping (it can — the passage is contemporary/near-contemporary to the persons).

## 15. Staging Readiness

**Needs source enrichment before staging.** This is the only package in the batch that falls below acceptable source density. The 3 non-D sources are all well-chosen (明史, 徐祯卿全集编年校注, and one academic paper), but the total is too thin for 10 claims. The package is otherwise well-structured: claims are cautious, relationships correctly typed, reception labels appropriate, and the limited-interaction-window caveat is a model of good practice. **Recommendation:** Add 1-2 additional academic sources, re-validate, then promote to staging-acceptable.
