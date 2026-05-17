# Xu Zhenqing Source Enrichment Plan (v1)

**Branch:** `review/xu-zhenqing-source-enrichment-v1`
**Date:** 2026-05-15
**Author:** MorphMind AI
**Status:** Planning — no package edits yet

---

## 1. Current Source Inventory

| Source ID | Title | Type | Level | Status |
|-----------|-------|------|-------|--------|
| SRC_XZQ_001 | 明史·文苑传 | official_history | A_candidate | ai_verified_unreviewed |
| SRC_XZQ_002 | 徐祯卿全集编年校注 (Fan Zhixin, 2009) | collected_works | A_candidate | ai_verified_unreviewed |
| SRC_XZQ_003 | 徐祯卿与明代前七子文学 | academic_paper | B_high | **needs_verification** |
| SRC_XZQ_004 | 百度百科·徐祯卿 | encyclopedia | D | clue_only |
| SRC_XZQ_005 | Wikipedia: Xu Zhenqing | encyclopedia | D | clue_only |

**Non-D sources: 3** (SRC_XZQ_001, SRC_XZQ_002, SRC_XZQ_003)
**D/clue_only: 2** (SRC_XZQ_004, SRC_XZQ_005)

---

## 2. Weak Sources

| Source | Weakness |
|--------|----------|
| SRC_XZQ_003 | **No journal name, author, DOI, or page range.** Title is a descriptive placeholder. This source supports 6 of 10 claims (CLM_XZQ_006 through CLM_XZQ_010). Its `needs_verification` status cascades to over half the claims. |
| SRC_XZQ_004, SRC_XZQ_005 | Correctly marked D/clue_only. Not used as primary support for any claim. Low risk. |

---

## 3. Claim-to-Source Dependency

| Claim | Sources | Risk if SRC_XZQ_003 is removed |
|-------|---------|-------------------------------|
| CLM_XZQ_001-004 (identity, jinshi) | SRC_XZQ_001 only | None — 明史 is sufficient |
| CLM_XZQ_005 (poetry, 迪功集) | SRC_XZQ_002 only | None — collected works are sufficient |
| CLM_XZQ_006 (吴中四才子) | SRC_XZQ_003 | **High** — but 明史 itself documents the grouping |
| CLM_XZQ_007 (前七子) | SRC_XZQ_003 | **High** — only source for this claim |
| CLM_XZQ_008 (Li Mengyang) | SRC_XZQ_003 | **High** — only source |
| CLM_XZQ_009 (Suzhou network) | SRC_XZQ_003 | **High** — only source |
| CLM_XZQ_010 (limited network) | SRC_XZQ_003 | **High** — only source |

**Critical finding:** SRC_XZQ_003 is the sole source for 5 of 10 claims. If it cannot be verified, those 5 claims must either be downgraded to `needs_verification` or sourced elsewhere.

---

## 4. Missing Source Types

| Gap | Priority | Rationale |
|-----|----------|-----------|
| Academic monograph on Xu Zhenqing | High | No book-length study cited. Tang Yin has Deng Xiaodong (2012); Wen Zhengming has Zhou Daozhen (2020). Xu Zhenqing needs equivalent. |
| Literary history reference work | High | A standard Ming literary history (e.g., 明代文学史, 中国文学史 series) would cover 前七子 and Xu Zhenqing's place in it. |
| 明史 passage verification | Medium | SRC_XZQ_001 already has the key 吴中四才子 passage quoted in notes. Exact juan/page in Zhonghua Shuju edition needed. |
| Contemporary Ming sources | Medium | Letters or poems exchanged between Xu Zhenqing and Li Mengyang or other Suzhou literati, if surviving. May be included in SRC_XZQ_002 already. |

---

## 5. Candidate Sources to Search

### Tier 1 — Replace SRC_XZQ_003 (highest priority)

1. **明代前七子研究** or equivalent monograph on the Former Seven Masters
   - Likely published by a Chinese university press (e.g., 人民出版社, 中华书局, 北京大学出版社)
   - Would cover Xu Zhenqing's literary affiliation with Li Mengyang, He Jingming, et al.
   - Search target: CNKI / academic databases for "前七子" + "徐祯卿"

2. **明代文学史** (standard Ming literary history)
   - Would place Xu Zhenqing in literary-historical context
   - Multiple editions exist (e.g., 袁行霈 中国文学史, 章培恒 中国文学史新著, or dedicated Ming volumes)
   - Search target: standard reference works in Chinese literary history

3. **徐祯卿年谱** or biographical study
   - May exist as a journal article or monograph chapter
   - Would document his official career after jinshi (1505-1511)
   - Search target: CNKI for "徐祯卿" + "年谱" or "生平" or "考"

### Tier 2 — Strengthen specific claims

4. **李梦阳集** or collected works of Li Mengyang
   - Would document literary exchanges with Xu Zhenqing directly
   - A_candidate if used with specific passage references
   - Search target: modern annotated edition of Li Mengyang's works

5. **何景明集** or other Former Seven Masters members' works
   - Supplementary — would strengthen the 前七子 claim
   - Lower priority than Li Mengyang

### Tier 3 — Cross-reference existing sources

6. **明史·文苑传** passage in 徐祯卿全集编年校注
   - SRC_XZQ_002 (Fan Zhixin 2009) likely includes the 明史 biography as an appendix
   - This could provide exact juan/page references
   - Check the appendix/附录 section of the 2009 edition

---

## 6. Recommended Strategy

### Phase 1: Search for academic sources (NO package edits)

1. Search CNKI / academic databases for:
   - "徐祯卿" + "前七子" → find academic papers replacing SRC_XZQ_003
   - "徐祯卿" + "年谱" or "生平" → find biographical study
   - "吴中四才子" + "明代" → find literary history coverage

2. Search for standard Ming literary histories:
   - 明代文学史 (multiple editions)
   - 中国文学史 (Yuan Xingpei, Zhang Peiheng series)

3. Check SRC_XZQ_002 appendix for 明史 biography reprint.

**Do not edit the package during this phase. Record findings.**

### Phase 2: After findings confirmed, apply edits

If 1-2 verified academic sources are found:
- Add them as new source entries in sources.jsonl
- Reassign source_ids on claims CLM_XZQ_006 through CLM_XZQ_010
- Replace or verify SRC_XZQ_003
- Re-run `validate_package.py`

If 明史 passage is verified in SRC_XZQ_002 appendix:
- Update SRC_XZQ_001 citation_detail with exact page number
- CLM_XZQ_006 (吴中四才子 grouping) can then use SRC_XZQ_001 as source — the 明史 passage itself documents the grouping
- Change CLM_XZQ_006 confidence from `reception_label` (which it currently is) — the 明史 passage makes the grouping itself a confirmed historical fact, though the grouping label remains reception

### Fallback

If no additional sources are found:
- Downgrade CLM_XZQ_007 through CLM_XZQ_010 to `needs_verification` low confidence
- Add explicit `needs_verification` caveat to package README
- Xu Zhenqing would be marked as a thin-but-honest package — usable for network topology only, not for biographical detail

---

## 7. Should Xu Zhenqing Package Be Edited Now?

**No.** The package should not be edited until Phase 1 search results are in. The current state is:

- Schema: v2.5 compliant
- Validation: PASSED
- Claims: All appropriately caveated at `probable` confidence where sources are thin
- No JSON errors, no fabricated data

The package is honest about its limitations. Editing before source verification risks introducing errors or fabricating source details.

**Only purely mechanical fix:** CLM_XZQ_006 could have SRC_XZQ_001 added as a source alongside SRC_XZQ_003 — the 明史 passage explicitly groups Xu Zhenqing with the other three. This is a mechanical correction based on data already in the source notes. But even this should wait until Phase 2 to batch all edits together.

---

## 8. Success Criteria

Xu Zhenqing is considered "source-enriched" when:
1. SRC_XZQ_003 is verified or replaced with a real academic paper/monograph (author, journal, year, pages confirmed)
2. At least 1 additional B_high academic source is added
3. Total non-D sources ≥ 5 (up from 3)
4. No claim depends solely on an unverified source
5. Package still passes `validate_package.py`
