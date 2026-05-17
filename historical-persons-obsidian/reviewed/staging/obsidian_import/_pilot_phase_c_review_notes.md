# Pilot Phase C Review Notes

**Date:** 2026-05-17
**Branch:** `pilot/obsidian-phase-c-source-notes-v1`
**Previous:** PR #33 (merged 2026-05-17) contained initial Phase A+B+C pilot
**This branch:** Updates source notes with verified citations from 22-person source audit sprint

---

## 1. Source Notes Created

### Tang Yin (7 notes)

| Source ID | Type | Reliability | Claims Linked | Status |
|-----------|------|-------------|---------------|--------|
| [[SRC_TY_001]] | official_history (明史·文苑传) | A_candidate | 8 claims | verified |
| [[SRC_TY_002]] | collected_works (六如居士集) | A_candidate | 4 claims | verified |
| [[SRC_TY_003]] | academic_monograph (唐寅研究, Deng 2012) | B_high | 1 claim | verified |
| [[SRC_TY_004]] | museum_record (故宫藏品) | A_candidate | 2 claims | **updated** — citation with dimensions, donor, DPM ref |
| [[SRC_TY_007]] | academic_monograph (Clapp 1991) | B_high | 7 claims | **updated** — placeholder → verified monograph |
| [[SRC_TY_008]] | local_gazetteer (姑苏志) | A_candidate | 0 claims | verified |
| [[SRC_TY_009]] | academic_paper (研究述评) | B_high | 2 claims | verified |

### Julius Caesar (7 notes)

| Source ID | Type | Reliability | Claims Linked | Status |
|-----------|------|-------------|---------------|--------|
| [[SRC_JC_001]] | primary_text (De Bello Gallico) | A_candidate | 2 claims | verified |
| [[SRC_JC_002]] | primary_text (De Bello Civili) | A_candidate | 3 claims | verified |
| [[SRC_JC_003]] | ancient_biography (Plutarch, Loeb) | B_high | 9 claims | verified |
| [[SRC_JC_004]] | ancient_biography (Suetonius, Loeb) | B_high | 9 claims | verified |
| [[SRC_JC_005]] | ancient_history (Cassius Dio, Loeb) | B_high | 5 claims | verified |
| [[SRC_JC_006]] | ancient_text (Cicero Letters, Loeb) | A_candidate | 1 claim | verified |
| [[SRC_JC_007]] | academic_monograph (Goldsworthy 2006) | B_high | 5 claims | verified |

**Total: 14 source notes** (7 Chinese + 7 Western)

---

## 2. Key Updates (2026-05-17 Sprint)

### SRC_TY_007: Placeholder → Verified Monograph
- **Before:** "Tang Yin: Life and Art" / "唐寅生平与艺术" — fabricated title, no author/journal/year
- **After:** Clapp, Anne de Coursey. *The Painting of T'ang Yin*. University of Chicago Press, 1991. ISBN 9780226106755. 320 pp.
- **Verification:** Google Scholar search confirmed this as the standard English monograph
- **Impact:** 7 claims now backed by verifiable academic source; co-sourcing reduced sole dependence

### SRC_TY_004: Museum Record Enriched
- **Before:** `needs_verification` with no citation details
- **After:** Full citation: painting title, medium (绢本设色), dimensions (124.7×63.6cm), donor (Zhang Boju 1956), DPM/中国古代书画图目 reference

### Person Note Refreshed
- tang-yin.md Review Status section updated with source audit sprint results
- Source sufficiency improved — SRC_TY_007 placeholder eliminated

---

## 3. D-Sources Not Created

Per policy, D/clue_only sources are not given standalone notes:

| Source | Person | Type |
|--------|--------|------|
| SRC_TY_005 | Tang Yin | Baidu Baike (D) — clue only |
| SRC_TY_006 | Tang Yin | Wikipedia (D) — clue only |
| SRC_JC_008 | Julius Caesar | Wikipedia (D) — clue only |
| SRC_JC_009 | Julius Caesar | Britannica (D) — clue only |

---

## 4. Obsidian Wikilink Structure

All source notes use bidirectional wikilinks:
- `[[tang-yin#Confirmed Historical Claims|CLM_TY_007]]` — source → person claim
- `[[SRC_TY_001]]` — person claims table → source note
- Co-source annotations show source relationships

---

## 5. Remaining Verification Gaps

| Source | Issue | Resolution Path |
|--------|-------|-----------------|
| SRC_TY_003 | Exact page references | Physical book or detailed TOC |
| SRC_TY_004 | Museum accession number | DPM catalog or 中国古代书画图目 |
| SRC_TY_007 | Page-level passages | Physical book access |
| SRC_JC_003–006 | Loeb chapter precision | Passage-level verification |
| SRC_JC_007 | Goldsworthy page references | Physical book access |

---

## 6. Phase C Verdict

**Pilot Phase C: COMPLETE for Tang Yin + Julius Caesar.**

- 14 source notes with frontmatter, metadata, claim wikilinks, review warnings
- SRC_TY_007 placeholder eliminated — replaced with verified Clapp 1991 monograph
- Bidirectional wikilinks working between person notes and source notes
- 0 claims now depend on unverifiable placeholder sources

**Recommended next:** Proceed to Phase D (relationships + events) for the 2 pilot persons, OR scale Phase A+B+C to remaining 20 persons.
