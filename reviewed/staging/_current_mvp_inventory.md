# Current MVP Inventory v1.1
**Branch:** `step1.2a/staging-consolidation-v1`
**Date:** 2026-05-14
**Reviewer:** MorphMind AI (consolidation sprint)

---

## Overview

This inventory covers all 7 person packages in `incoming/` on the main branch. All packages are `ai_collected_unreviewed` — none promoted to master-quality. The 5 initial MVP packages (Shen Zhou, Wang Yangming, Pompey, Qiu Ying, Augustus) were normalized from v2.3 to v2.5 schema in the MVP hardening sprint (PR #8). Wu Kuan and Mark Antony were normalized in the PR #7 hardening pass (PRs #9, #11). Source verification sprint (PR #10) added Loeb refs for Pompey/Augustus, Wang Yangming monograph, and Qiu Ying sources. Wang Yangming page-ref corrections and SRC018 caveat applied in PR #12.

---

## 1. 沈周 (Shen Zhou)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/shen-zhou/` |
| **Person ID** | `P_CHN_MING_SHEN_ZHOU` |
| **Dates** | 1427–1509 |
| **Canonical branch** | `collect/shen-zhou-v1` (PR#1) |
| **Status** | `ai_collected_unreviewed` |
| **Required files** | 11/11 present |
| **Claims** | 22 |
| **Sources** | 6 (2 A_candidate, 1 B, 2 C, 1 D) |
| **Relationships** | 13 |
| **Visual media** | 3 entries (all staging) |
| **Works** | 8 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 native |

**Source sufficiency:** Weak. Only 6 sources for 22 claims (0.27 sources per claim). No confirmed `A`-level source. Primary claims rely on A_candidate (secondary literature) and one D-level general web source. 明史·隐逸传 biography not represented as a discrete source.

**Key source limitations:**
- Birth year discrepancy (1427 vs 1472) unresolved
- D-level source (SRC006, general web) present
- Only 6 sources for 22 claims — source density below 0.3
- Several "probable/medium" confidence claims on relationship interpretations from secondary sources

**Relationship limitations:**
- Relationship types correctly remapped to v2.5 (family, documented_teacher_student, documented_association, same_cultural_circle, later_grouping_only)
- Teacher-student relationships rely on secondary sources, not primary documents

**Visual media limitations:**
- All 3 entries staging with `needs_verification` for source holder and object IDs

**Suitable for Obsidian demo:** YES. Well-structured README and open_questions.md. Claims split into individual JSONL rows. person_id consistent across all files.

**Recommended next action:** Source verification — confirm passage refs in 明史·隐逸传 and/or 沈周年谱. Promote C/D sources to academic sources. Resolve birth year discrepancy.

---

## 2. 王阳明 (Wang Yangming)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/wang-yangming/` |
| **Person ID** | `P_CHN_MING_WANG_YANGMING` |
| **Dates** | 1472–1529 |
| **Canonical branch** | `collect/wang-yangming-and-pompey-v1` (PR#4) |
| **Status** | `ai_collected_unreviewed` |
| **Required files** | 11/11 present |
| **Claims** | 37 |
| **Sources** | 18 (includes source verification additions from PRs #10, #12) |
| **Relationships** | 8 |
| **Visual media** | 3 entries (all staging) |
| **Works** | 3 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 native |

**Source sufficiency:** Moderate. 18 sources for 37 claims (0.49 sources per claim). Several A_candidate primary texts (传习录, 大学问, 王文成公全书, 明史) lack specific edition/passage refs. SRC017 (Steben 1998) page range corrected in PR #12. SRC018 (Najita 1980) caveat added — only p.54 mentions Wang Yangming; Saigo Takamori ZERO mentions.

**Key source limitations:**
- SRC014 (Ching 1976) Japan pages still `needs_verification` — physical book or institutional library access required
- A_candidate sources lack specific edition/passage/volume references
- SRC018 (Najita 1980) does NOT substantiate C026 (Yangming influence on Saigo/Takasugi) — C026 confidence downgraded to low
- 5 C-level sources remain

**Relationship limitations:**
- Only 8 relationships — thin for a major Ming philosophical figure
- R002 (Lu Jiuyuan) correctly as reception_label

**Visual media limitations:**
- All staging; no verified contemporary portrait

**Suitable for Obsidian demo:** YES. Rich biographical narrative. Well-structured claims with Chinese and English text. Pre-split compound claims.

**Recommended next action:** Replace SRC014 with verified Japan Yangmingism monograph. Promote 传习录 and 明史·王守仁传 to A with specific passage citations.

---

## 3. 仇英 (Qiu Ying)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/qiu-ying/` |
| **Person ID** | `P_CHN_MING_001_QIU_YING` |
| **Dates** | ca. 1494–ca. 1552 (disputed range) |
| **Canonical branch** | `collect/qiu-ying-and-augustus-v2-5` (PR#5) |
| **Status** | `ai_collected_unreviewed` |
| **Required files** | 11/11 present |
| **Claims** | 34 |
| **Sources** | 23 |
| **Relationships** | 12 |
| **Visual media** | 4 entries (all staging) |
| **Works** | 13 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized from v2.3) |

**Source sufficiency:** Good. 23 sources for 34 claims (0.68 sources per claim). Strong modern scholarship (Laing 1999, Cahill, Ngan 2016) plus Chinese primary sources. Source verification sprint (PR #10, #12) added 明清画史笔记 source entries (无声诗史, 明画录, 图绘宝鉴续编).

**Key source limitations:**
- Birth/death dates uncertain (range 1482–1505 birth; 1552 death most likely)
- No self-written texts — all biographical data from external sources
- Cleveland Art Museum work (赵孟頫写经换茶图) unverified in online catalogue
- Systematic real/forgery distinction for attributed works incomplete
- Most Ming dynasty text passages need exact edition/page verification

**Relationship limitations:**
- REL_QY_004 (Shen Zhou influence): correctly `later_grouping_only`
- Patron relationships reasonably documented (Xiang Yuanbian, Zhou Fenglai)

**Visual media limitations:**
- Most museum object IDs remain `needs_verification`
- NPM, Palace Museum Beijing, Shanghai Museum accession numbers not independently confirmed

**Suitable for Obsidian demo:** YES. Best-documented Chinese package. Strong source density. Works list with 13 entries. Open questions file is thorough.

**Recommended next action:** Verify museum object IDs from official catalogues. Confirm Cleveland Art Museum catalogue entry. Add specific edition references for all Ming dynasty primary texts.

---

## 4. 吴宽 (Wu Kuan)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/wu-kuan/` |
| **Person ID** | `P_CHN_MING_WU_KUAN` |
| **Dates** | 1435–1504 |
| **Canonical branch** | `collect/wu-kuan-and-mark-antony-v1` (PR#7) |
| **Status** | `ai_collected_unreviewed` |
| **Required files** | 11/11 present |
| **Claims** | 22 (with sub-claims a/b/c suffixes post-split) |
| **Sources** | 7 (5 A_candidate, 0 B, 1 D, 1 unverified) |
| **Relationships** | 4 |
| **Visual media** | 2 entries (all staging) |
| **Works** | 4 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized in PR #9, cleanup in PR #11) |

**Source sufficiency:** Weak. 7 sources for 22 claims. Primary official source (明史·吴宽传) present at A_candidate. Baidu Baike correctly marked D/clue_only. Several claims have empty source_ids — these need source assignment or status downgrade.

**Key source limitations:**
- Claims with empty source_ids need source assignment or downgrade to needs_verification
- Only 4 relationships — very thin relational data for a Ming literatus
- No B-level academic monograph sources
- Baidu (SRC_WK_005, D-level) correctly flagged as clue_only

**Relationship limitations:**
- Only 4 recorded relationships (Shen Zhou, Wen Zhengming, Wang Ao, +1 other)
- Relationship strength unverified from primary correspondence

**Visual media limitations:**
- 2 entries, both staging with no verified object IDs

**Suitable for Obsidian demo:** Marginal. Schema v2.5 present but source base thin and relationship data minimal. Better suited as a secondary entry after source enrichment.

**Recommended next action:** Assign source_ids to all empty claims. Promote 明史·吴宽传 from A_candidate to A with verified juan/passage refs. Add academic monograph sources for Wu Kuan's literary and calligraphic legacy.

---

## 5. Gnaeus Pompeius Magnus (Pompey)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/western/gnaeus-pompeius-magnus/` |
| **Person ID** | `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` |
| **Dates** | 106–48 BCE |
| **Canonical branch** | `collect/wang-yangming-and-pompey-v1` (PR#4) |
| **Status** | `ai_collected_unreviewed` |
| **Required files** | 11/11 present |
| **Claims** | 42 |
| **Sources** | 17 (10 ancient + 7 modern) |
| **Relationships** | 12 |
| **Visual media** | 5 entries (all staging) |
| **Works** | 2 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized in hardening sprint) |

**Source sufficiency:** Good. 17 sources for 42 claims. Classical sources (Plutarch, Appian, Cassius Dio, Caesar, Cicero) form the core with modern scholarship backing. Source verification sprint provided extensive Loeb references: Plutarch Pompey chapters 1, 14, 25-28, 30-45, 46-47, 68-80 confirmed; Appian BC Book 1.80, Book 3.82-104 confirmed; Cassius Dio Books 36-37, 42 confirmed; Pliny NH 37.13 confirmed for birth date.

**Key source limitations:**
- Cicero Pro Lege Manilia sections 27-35 still approximate
- Valerius Maximus 6.2.8 ("adulescentulus carnifex") still `needs_verification`
- Florus 2.13 does NOT contain "most magnificent" superlative
- "Three legions" claim: Plutarch says "a legion" — number discrepancy unresolved
- RRC coinage catalogue numbers not yet provided
- 4 C-level sources present

**Relationship limitations:**
- Relationship types correctly remapped to v2.5 in hardening sprint
- Spouse relationships (3x) correctly typed

**Visual media limitations:**
- Ny Carlsberg Glyptotek bust inventory number unverified
- All visual media staging

**Suitable for Obsidian demo:** YES. Most extensive Western package (42 claims). Strong classical source coverage with Loeb references. Pre-split compound claims.

**Recommended next action:** Complete remaining needs_verification citations. Add RRC numbers. Resolve Florus/Valerius Maximus discrepancies. Verify Ny Carlsberg Glyptotek inventory number.

---

## 6. Augustus (Octavian)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/western/augustus-octavian/` |
| **Person ID** | `P_WEST_ROMAN_001_AUGUSTUS` |
| **Dates** | 63 BCE–14 CE |
| **Canonical branch** | `collect/qiu-ying-and-augustus-v2-5` (PR#5) |
| **Status** | `ai_collected_unreviewed` |
| **Required files** | 11/11 present |
| **Claims** | 35 |
| **Sources** | 18 (11 ancient/primary + 7 modern) |
| **Relationships** | 9 |
| **Visual media** | 3 entries (all staging) |
| **Works** | 2 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized from v2.3) |

**Source sufficiency:** Strong. 18 sources for 35 claims (0.51 sources per claim). Excellent ancient coverage: Suetonius Divus Augustus (chapters 7.1, 79, 99 confirmed); Cassius Dio Books 45-56 confirmed; Res Gestae chapter 34 confirmed; Appian BC 2.143 confirmed (Caesar's will); Tacitus Annals 1.2-10 and 1.5-6 confirmed; Cicero Ad Atticum 14.10.3 confirmed. Modern scholarship (Syme 1939, Goldsworthy 2014).

**Key source limitations:**
- Testamentary adoption legal ambiguity — marked probable/medium, appropriate
- "First emperor" framing correctly marked reception — modern category, not ancient title
- Velleius Paterculus and Nicolaus of Damascus exact passages `needs_verification`
- RIC coinage catalogue numbers `needs_verification`
- Via Labicana Augustus inventory number `needs_verification`

**Relationship limitations:**
- Relationships correctly remapped in hardening sprint
- Ally relationships → same_political_context or documented_association

**Visual media limitations:**
- Augustus of Prima Porta confirmed (Vatican Museums, Braccio Nuovo, inv. 2290)
- Via Labicana Augustus and coinage need full inventory/catalogue numbers

**Suitable for Obsidian demo:** YES. Best-sourced Western package. Strong biographical narrative. Claims have both Chinese and English text. Res Gestae bias caveats correctly included.

**Recommended next action:** Complete Velleius/Nicolaus passage refs. Add RIC numbers. Resolve birth date discrepancy (22 vs 23 September).

---

## 7. Mark Antony (Marcus Antonius)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/western/mark-antony/` |
| **Person ID** | `P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS` |
| **Dates** | 83–30 BCE |
| **Canonical branch** | `collect/wu-kuan-and-mark-antony-v1` (PR#7) |
| **Status** | `ai_collected_unreviewed` |
| **Required files** | 11/11 present |
| **Claims** | 35 |
| **Sources** | 11 (7 ancient + 4 modern) |
| **Relationships** | 13 |
| **Visual media** | 4 entries (all staging) |
| **Works** | 4 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized in PR #9, cleanup in PR #11) |

**Source sufficiency:** Moderate. 11 sources for 35 claims (0.31 sources per claim). Ancient sources correctly leveled: Plutarch/Appian/Cassius Dio at B_high (secondary narratives with bias), Cicero Philippics/Caesar Civil War/Res Gestae at A_candidate (primary documents). No D or C sources. Modern scholarship: Pelling 1988, Goldsworthy 2010, Syme 1939.

**Key source limitations:**
- Birth year disputed (83 BCE from Cicero Phil.; Plutarch records age 53/56 at death)
- All ancient source citations marked `needs_verification` — no verified Loeb chapter/passage refs
- Only 4 modern scholarly sources for 35 claims — moderately dependent on ancient sources
- No Cicero Philippics or Caesar Civil War passage-level references

**Relationship limitations:**
- Relationships schema v2.5 compliant (opponent, documented_association, spouse, sibling, same_political_context)
- 13 relationships — strongest relational data of all 7 packages
- Cleopatra VII package not yet collected — relationship claims one-sided

**Visual media limitations:**
- 4 entries all staging; coin portraits and later sculpture need museum verification

**Suitable for Obsidian demo:** YES. Well-structured. Relationships v2.5 compliant. Both English and Chinese claim text. Ancient bias caveats included.

**Recommended next action:** Add verified Loeb chapter/passage references for Plutarch Antony, Appian BC, Cassius Dio. Cross-reference birth year across all sources. Link to future Cleopatra VII package.

---

## Cross-Package Metrics

| Metric | Shen Zhou | Wang Yangming | Qiu Ying | Wu Kuan | Pompey | Augustus | Mark Antony |
|--------|-----------|---------------|----------|---------|--------|----------|-------------|
| Required files | 11/11 | 11/11 | 11/11 | 11/11 | 11/11 | 11/11 | 11/11 |
| Claims | 22 | 37 | 34 | 22 | 42 | 35 | 35 |
| Sources | 6 | 18 | 23 | 7 | 17 | 18 | 11 |
| Relationships | 13 | 8 | 12 | 4 | 12 | 9 | 13 |
| Sources per claim | 0.27 | 0.49 | 0.68 | 0.32 | 0.40 | 0.51 | 0.31 |
| A/A_candidate % | ~33% | ~50% | ~65% | ~71% | ~59% | ~61% | ~64% |
| D-level sources | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| C-level sources | 2 | 5 | ~3 | 0 | 4 | 1 | 0 |
| Validation | PASSED | PASSED | PASSED | PASSED | PASSED | PASSED | PASSED |
| Schema | v2.5 | v2.5 | v2.5 | v2.5 | v2.5 | v2.5 | v2.5 |

---

## Priority Triage

### Tier 1 — Ready for Central Review (no blocking issues)
- **Augustus** — strongest source base; minor needs_verification clean-up only
- **Qiu Ying** — strong scholarship; museum IDs still needs_verification but structure solid
- **Pompey** — extensive; source verification well under way with Loeb refs

### Tier 2 — Needs Light Fixes Before Review
- **Wang Yangming** — SRC014 Japan pages still `needs_verification`; otherwise solid
- **Mark Antony** — needs Loeb chapter refs; schema v2.5 compliant

### Tier 3 — Needs Substantial Work
- **Shen Zhou** — only 6 sources; needs source enrichment before master promotion
- **Wu Kuan** — thin source base, minimal relationships; needs source assignment

---

## Obsidian Demo Suitability

**Recommended 2 Chinese + 2 Western for initial demo:**
- Chinese: **Wang Yangming** (rich philosophy/career), **Qiu Ying** (best-sourced, works list strong)
- Western: **Augustus** (strongest source base), **Pompey** (most extensive claims)
