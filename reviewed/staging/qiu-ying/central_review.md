# Central Review: 仇英 (Qiu Ying)

**Reviewer:** MorphMind AI
**Date:** 2026-05-14
**Package:** `incoming/chinese/qiu-ying/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_001_QIU_YING` |
| **Name (ZH)** | 仇英 |
| **Name (EN)** | Qiu Ying |
| **Birth** | ca. 1494 (disputed; range 1482–1505) |
| **Death** | ca. 1552 |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#5 (`collect/qiu-ying-and-augustus-v2-5`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized from v2.3) |

---

## 2. Current Package Status

Package is complete (11/11 required files) and passes validation. Normalized from v2.3 to v2.5 in hardening sprint (PR #8). Source verification sprint (PR #10) added 明清画史笔记 source entries (无声诗史, 明画录, 图绘宝鉴续编). Relationship types corrected (REL_QY_004 influence → later_grouping_only). Best-documented Chinese package with 23 sources for 34 claims.

---

## 3. Overall Central Review Verdict

**STAGING ONLY — NOT READY FOR MASTER PROMOTION.** Package is structurally excellent — strongest source density (0.68 sources per claim) among Chinese packages and comprehensive works list. Primary blocker is unverified museum object IDs and unverified Ming dynasty text passages. Birth/death dates appropriately marked as approximate. Once museum catalogue verification and Ming text passage verification are complete, this package will be closest to master-ready.

---

## 4. Master-Candidate Facts

- Ming dynasty professional painter active in Suzhou, ca. 1494–1552
- Trained as a lacquer artisan; learned painting possibly under Zhou Chen (周臣)
- Collaborated with Wen Zhengming on at least one known work (《湘君湘夫人图》)
- Major patron: Xiang Yuanbian (项元汴); also Zhou Fenglai (周凤来)
- Known for precision color work (青绿山水) and figure painting
- Classified as one of the 明四家 (Four Masters of the Ming) in later art history
- Left no writings of his own — biographical data from external sources only

---

## 5. Staging-Only Claims

- Birth/death date claims — correctly approximate with disputed range noted
- Claims about specific work dates — rely on stylistic analysis rather than dated inscriptions
- Patron relationships — documented but specific dates of patronage need verification
- Dong Qichang's assessment of Qiu Ying's color mastery — work exists, exact passage needs verification

---

## 6. Reception / Legendary / Disputed Material

- "明四家" classification — correctly reception (Dong Qichang consolidated this grouping)
- "Wu School" association — correctly later_grouping_only
- Qiu Ying as "representative of Ming professional painting" — reception framing
- Real vs. forgery distinction for attributed works — systematic analysis incomplete

---

## 7. Source Issues

| Issue | Severity |
|-------|----------|
| Museum object IDs unverified across all institutions | High |
| 明清画史笔记 passages need exact edition/page verification | Medium |
| Cleveland Art Museum work (赵孟頫写经换茶图) not confirmed | Medium |
| Ming dynasty text exact passages (Dong Qichang, Wang Shizhen, Yu Yunwen) needs_verification | Medium |
| D-level source present | Low |
| Wen Zhengming inscription exact text not transcribed | Low |

---

## 8. Relationship Issues

| Issue | Detail |
|-------|--------|
| REL_QY_004 (Shen Zhou influence) | Correctly later_grouping_only — no direct evidence |
| Teacher-student relationship with Zhou Chen | Probable — widely accepted in scholarship but not documented in Qiu Ying's own words |
| Patron relationships | Reasonably documented through work attributions and colophons |

---

## 9. Visual Media Issues

- All 4 entries staging
- National Palace Museum, Taipei: inventory numbers for 《汉宫春晓图》, 《仙山楼阁图》 needs_verification
- Palace Museum, Beijing: accession numbers not independently confirmed
- Shanghai Museum: accession numbers for 《梧竹书堂图》, 《倪瓒像》 needs_verification
- Cleveland, Tianjin, Liaoning museum works need official catalogue verification

---

## 10. Recommended Cleanup Actions

1. Verify NPM Taipei online collection database for Qiu Ying works and add accession numbers
2. Verify Palace Museum Beijing catalogue entries with accession numbers
3. Confirm Cleveland Museum of Art catalogue entry for 《赵孟頫写经换茶图》
4. Add specific edition references for 无声诗史, 明画录, 图绘宝鉴续编
5. Verify Dong Qichang's 《画禅室随笔》 passage on Qiu Ying's color use
6. Complete systematic real/forgery annotation for attributed works

---

## 11. Obsidian Demo Suitability

**YES — recommended as primary Chinese demo person.** Best-documented Chinese package. Strong source density. Works list with 13 entries including museum locations. Open questions file is thorough. Both English and Chinese claim text. Person_id consistent. The unverified museum IDs do not prevent demo — they can be displayed as "verified pending" or with notes.

---

## 12. Do-Not-Promote-Yet Notes

- **Do not promote to master_candidates** until museum object IDs are verified from at least two major institutions (NPM Taipei + Palace Museum Beijing)
- **Do not promote work-dating claims** as confirmed until specific dated inscriptions or reliable catalogue entries are cited
- Visual media must remain staging pending museum verification
