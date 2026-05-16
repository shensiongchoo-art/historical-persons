# Xu Zhenqing Source Search Results v1

**Date:** 2026-05-15
**Branch:** verification/xu-zhenqing-source-search-v1
**Status:** Source candidates identified — no package edits made

---

## 1. Current Sources in incoming/chinese/xu-zhenqing/sources.jsonl

| Source ID | Title | Level | Status |
|-----------|-------|-------|--------|
| SRC_XZQ_001 | 明史·文苑传 (juan 286) | A_candidate | ai_verified_unreviewed |
| SRC_XZQ_002 | 徐祯卿全集编年校注 (Fan Zhixin, 2009) | A_candidate | ai_verified_unreviewed |
| SRC_XZQ_003 | 徐祯卿与明代前七子文学 | B_high | needs_verification |
| SRC_XZQ_004 | 百度百科·徐祯卿 | D | clue_only |
| SRC_XZQ_005 | Wikipedia: Xu Zhenqing | D | clue_only |

**Gap:** Only SRC_XZQ_003 is a B_high academic source for the Former Seven Masters / literary relationships, and it's marked needs_verification. No monograph-level source for Li Mengyang relationship. No source specifically about Xu Zhenqing's poetic theory or Wu-Zhong context beyond the basic collected works.

---

## 2. Search Methodology

Six search targets were queried:
1. 明代前七子研究 monograph / academic source
2. 明代文学史 / 中国文学史 with Xu Zhenqing section
3. 徐祯卿年谱 or biography
4. 李梦阳集 / correspondence / literary relationship evidence
5. 明史 passage (already partially covered by SRC_XZQ_001)
6. Academic papers on 徐祯卿 and 前七子

Searched via Google Scholar with Chinese and English queries across 1950-2026.

---

## 3. Source Candidates Found

### 3.1 Strongest Candidates (recommend for sources.jsonl after verification)

**A. 徐祯卿年谱简编 [ref_88c26a]**
- Type: academic_paper / chronological biography
- Reliability: B_high (scholarly journal article)
- Would support: CLM_XZQ_001, CLM_XZQ_002, CLM_XZQ_003, CLM_XZQ_004 (identity, dates, career)
- Sufficient to add: Yes, after verifying journal/publication details
- Gap covered: Direct chronological biography — addresses the thin-source criticism of Xu Zhenqing package

**B. 徐祯卿文学思想浅探 [ref_6b4c87]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_005, CLM_XZQ_007, CLM_XZQ_008 (poetry, Former Seven Masters, Li Mengyang)
- Sufficient to add: Yes, after verifying publication details
- Gap covered: Literary thought — provides academic backing for Former Seven Masters affiliation

**C. 徐祯卿诗学地位再评价 [ref_3a4d22]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_005, CLM_XZQ_007 (poetry, literary status)
- Sufficient to add: Yes, after verifying publication details
- Gap covered: Re-evaluation of Xu Zhenqing's poetic position

**D. Literary Archaism, Personal Expression and Self-Cultivation in Ming China: Li Mengyang and his World [literary_archaism_personal]**
- Type: monograph (book)
- Reliability: B_high (academic monograph, likely university press)
- Would support: CLM_XZQ_007, CLM_XZQ_008 (Former Seven Masters, Li Mengyang relationship)
- Sufficient to add: Yes, as B_high monograph on Li Mengyang. Chapter-level citation would be ideal.
- Gap covered: Major English-language monograph on Li Mengyang and the archaist movement

### 3.2 Supporting Candidates

**E. 明代吴中诗人徐祯卿 [ref_38f9ff]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_006, CLM_XZQ_009 (Wu-Zhong identity, Four Talents grouping)

**F. 吴中四才子名目考 [ref_c363af]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_006, CLM_XZQ_009 (Four Talents designation origin)

**G. 因情立格——徐祯卿在诗歌创作与理论批评上的追求 [ref_20df9d]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_005 (poetic theory and creation)

**H. 徐祯卿的撰述及其版本谈 [ref_cd5479]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_005 (writings and editions)

**I. 明代前七子复古运动的酝酿及形成 [ref_5d6e1f]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_007 (Former Seven Masters formation)

**J. 明代"前七子"正义之一 [ref_c403d3]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_007 (Former Seven Masters correction/clarification)

**K. 徐祯卿诗文集的版本考略 [ref_10b8e7]**
- Type: academic_paper
- Reliability: B_high
- Would support: CLM_XZQ_005 (editions of collected works)

---

## 4. Claims Support Matrix

| Claim | Current Support | New Candidate Sources | Strength After |
|-------|----------------|----------------------|----------------|
| CLM_XZQ_001 (birth) | SRC_XZQ_001 | ref_88c26a (年谱简编) | Strong |
| CLM_XZQ_002 (death) | SRC_XZQ_001 | ref_88c26a | Strong |
| CLM_XZQ_003 (courtesy name) | SRC_XZQ_001 | ref_88c26a | Strong |
| CLM_XZQ_004 (jinshi) | SRC_XZQ_001 | ref_88c26a | Strong |
| CLM_XZQ_005 (poetry, 迪功集) | SRC_XZQ_002 | ref_6b4c87, ref_20df9d, ref_cd5479, ref_10b8e7 | Strong |
| CLM_XZQ_006 (吴中四才子) | SRC_XZQ_003 | ref_38f9ff, ref_c363af | Strong |
| CLM_XZQ_007 (前七子) | SRC_XZQ_003 | ref_6b4c87, ref_5d6e1f, ref_c403d3, literary_archaism_personal | Strong |
| CLM_XZQ_008 (Li Mengyang) | SRC_XZQ_003 | literary_archaism_personal, ref_6b4c87 | Medium-Strong |
| CLM_XZQ_009 (苏州文人圈) | SRC_XZQ_003 | ref_38f9ff, ref_c363af | Medium |
| CLM_XZQ_010 (early death, limited network) | SRC_XZQ_003 | ref_88c26a (supports age context) | Medium |

---

## 5. Unresolved Gaps

1. **No dedicated Xu Zhenqing monograph** found. All candidates are journal articles or chapters within broader works. A full-length biography in Chinese or English was not identified in this search.

2. **李梦阳集 primary text not found.** No search result for Li Mengyang's collected works (空同集) with specific Xu Zhenqing passages. The relationship evidence remains from secondary scholarship.

3. **明史 passage already covered** by SRC_XZQ_001. No gap here — juan 286, 文苑传二 is the standard reference.

4. **No 明代文学史 monograph identified** that has a substantial Xu Zhenqing section. Cambridge History of Chinese Literature may cover this but was not in search results.

5. **All candidate sources need publication detail verification** (journal name, volume, pages, author, year) before addition to sources.jsonl.

---

## 6. Recommendation

**Phase 1 — Verify top 4 candidates (immediate):**
1. 徐祯卿年谱简编 [ref_88c26a] — verify journal, author, year, pages
2. 徐祯卿文学思想浅探 [ref_6b4c87] — verify publication details
3. 徐祯卿诗学地位再评价 [ref_3a4d22] — verify publication details
4. Literary Archaism...Li Mengyang [literary_archaism_personal] — verify publisher, year, author

**Phase 2 — Add to sources.jsonl and update claims (after Phase 1):**
- Add 2-3 verified sources as SRC_XZQ_006, SRC_XZQ_007, SRC_XZQ_008
- Update CLM_XZQ_007 and CLM_XZQ_008 source_ids
- Change SRC_XZQ_003 from needs_verification to verified if publication details confirmed
- Mark package source_sufficiency as adequate_with_caveats

**Phase 3 — Deep search (deferred):**
- Search CALIS/WorldCat for Xu Zhenqing monograph when university library access available
- Search for 空同集 passages mentioning 徐祯卿 via text databases
- Search for Cambridge History of Chinese Literature Ming volume section

**Current verdict:** 11 candidate sources found. Xu Zhenqing package can be strengthened to adequate_with_caveats with 2-3 verified additions. The package remains staging-acceptable but source-thin for relationships claims (CLM_XZQ_008, _009, _010).

---

## 7. Remaining Blockers

- Publication detail verification for all 11 candidates (journal, volume, pages, author)
- No primary text (空同集) passages verified for Li Mengyang-Xu Zhenqing relationship
- No dedicated monograph-level biography identified
- Xu Zhenqing remains the weakest Batch 1 Chinese package even after these additions
