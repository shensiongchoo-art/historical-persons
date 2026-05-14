# Current MVP Inventory v1
**Branch:** `step1.2/staging-consolidation-small-expansion-v1`
**Date:** 2026-05-13
**Reviewer:** MorphMind AI

---

## Overview

This inventory covers all 7 person packages in `incoming/` on the master branch. All packages are `ai_collected_unreviewed` — none promoted to master-quality. The 5 hardened packages (沈周, 王阳明, Pompey, 仇英, Augustus) were normalized from v2.3 to v2.5 schema in the MVP hardening sprint. Wu Kuan and Mark Antony were partially normalized in the PR#7 hardening pass.

---

## 1. 沈周 (Shen Zhou)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/shen-zhou/` |
| **Person ID** | `P_CHN_MING_SHEN_ZHOU` |
| **Dates** | 1427–1509 |
| **Canonical branch** | `collect/shen-zhou-v1` (PR#1) |
| **Status** | `ai_collected_unreviewed` |
| **Claims** | 22 (identity, career, works, relationships) |
| **Sources** | 6 (2 A_candidate, 1 B, 2 C, 1 D) |
| **Relationships** | 13 |
| **Visual media** | 3 entries (all staging) |
| **Works** | 8 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (native) |

**Source sufficiency:** Weak. Only 6 sources total, none confirmed `A`. Primary claims rely on `A_candidate` (secondary literature) and one D-level general web source. No single passage-level verified source from 明史·隐逸传 or 沈周年谱.

**Weaknesses:**
- Birth year discrepancy (1427 vs 1472) unresolved
- D-level source (general web) present
- Only 6 sources for 22 claims — source density below 0.3 sources per claim
- Several "probable/medium" confidence claims on relationship interpretations

**Obsidian suitability:** YES. Well-structured README and open_questions.md. Claims are split into individual JSONL rows. person_id is consistent across all files. Package is self-contained with no external dependencies.

**Verification needs:**
- Confirm passage refs in 明史·隐逸传 and/or 沈周年谱
- Resolve birth year discrepancy
- Promote C/D sources to A/A_candidate with specific edition/passage details

**Recommended next action:** Source verification sprint — provide specific passage references from 明史 or academic monographs. Promote key sources from A_candidate to A.

---

## 2. 王阳明 (Wang Yangming)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/wang-yangming/` |
| **Person ID** | `P_CHN_MING_WANG_YANGMING` |
| **Dates** | 1472–1529 |
| **Canonical branch** | `collect/wang-yangming-and-pompey-v1` (PR#4) |
| **Status** | `ai_collected_unreviewed` |
| **Claims** | 37 (pre-split compound claims) |
| **Sources** | 15 (8 A_candidate, 1 B, 5 C, 1 placeholder) |
| **Relationships** | 8 |
| **Visual media** | 3 entries (all staging) |
| **Works** | 3 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (native) |

**Source sufficiency:** Moderate. 15 sources for 37 claims (0.41 sources per claim). Several A_candidate primary texts (传习录, 大学问, 王文成公全书, 明史) lack specific edition/passage refs. SRC014 (Japanese Yangmingism) is a placeholder — no real monograph cited.

**Weaknesses:**
- SRC014 is a placeholder source; claims C025–C026 depend on it
- 5 C-level (general web) sources present
- A_candidate sources lack specific edition/passage/volume references
- One `needs_verification` claim (C027)

**Obsidian suitability:** YES. Rich biographical narrative in person_profile.md. Claims are well-structured with both Chinese and English text. Pre-split compound claims with proper claim_id suffixes (a/b/c pattern). philosophical terms correctly marked as reception_label.

**Recommended next action:** Replace SRC014 placeholder with Julia Ching monograph (or equivalent) with page references. Promote 传习录, 大学问, 明史·王守仁传 to A with specific passage citations.

---

## 3. 仇英 (Qiu Ying)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/qiu-ying/` |
| **Person ID** | `P_CHN_MING_001_QIU_YING` |
| **Dates** | ca. 1494–ca. 1552 (disputed range) |
| **Canonical branch** | `collect/qiu-ying-and-augustus-v2-5` (PR#5) |
| **Status** | `ai_collected_unreviewed` |
| **Claims** | 34 |
| **Sources** | 23 (modern + ancient) |
| **Relationships** | 12 |
| **Visual media** | 4 entries (all staging) |
| **Works** | 13 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized from v2.3) |

**Source sufficiency:** Good. 23 sources for 34 claims (0.68 sources per claim). Strong modern scholarship (Laing 1999, Cahill, Ngan 2016) plus Chinese primary sources. Key gap: 明清画史笔记 sources (无声诗史, 明画录, 图绘宝鉴续编) missing as discrete entries despite being cited in several claims.

**Weaknesses:**
- Birth/death dates uncertain (range 1482–1505 birth; 1552 death most likely)
- 无声诗史, 明画录, 图绘宝鉴续编 not represented as discrete source entries
- No self-written texts — all biographical data from external sources
- Cleveland Art Museum work unverified in online catalogue
- Systematic real/forgery distinction for attributed works incomplete

**Obsidian suitability:** YES. Best-documented Chinese package. Strong source density. Works list with 13 entries includes museum object IDs where available. Open questions file is thorough. D-level source present but flagged.

**Recommended next action:** Add discrete source entries for 无声诗史, 明画录, 图绘宝鉴续编 with edition details. Verify Cleveland Art Museum catalogue entry. Continue filling museum object IDs.

---

## 4. 吴宽 (Wu Kuan)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/chinese/wu-kuan/` |
| **Person ID** | `P_CHN_MING_002_WU_KUAN` |
| **Dates** | 1435–1504 |
| **Canonical branch** | `collect/wu-kuan-and-mark-antony-v1` (PR#7) |
| **Status** | `ai_collected_unreviewed` |
| **Claims** | 18 (with sub-claims a/b/c suffixes post-split) |
| **Sources** | 7 (5 A_candidate, 0 B, 1 D, 1 unverified) |
| **Relationships** | 4 |
| **Visual media** | 2 entries (all staging) |
| **Works** | 4 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (partially normalized — PR#7 hardening incomplete) |

**Source sufficiency:** Weak. Only 7 sources for 18 claims. Primary official source (明史·吴宽传) present at A_candidate. Baidu Baike correctly marked D/clue_only. 8 claims have empty source_ids — these need source assignment or status downgrade to needs_verification.

**Weaknesses:**
- 8 claims (CLM_WK_008–011, CLM_WK_012a–013b, CLM_WK_016–018) have empty source_ids
- Only 4 relationships — Shen Zhou, Wen Zhengming, Wang Ao, and one other; thin relational data
- Compound claims split but some split sub-claims lack source assignments
- SRC_WK_005 (Baidu) is D-level; correctly not used as primary support

**Obsidian suitability:** YES (with reservations). Schema v2.5 basic structure is present. Empty source_ids on 8 claims is the main issue — these claims are essentially unsupported. Should be fixed before Obsidian ingestion.

**Recommended next action:** Assign source_ids to all empty claims. If no source available, downgrade claim status to needs_verification/low. Promote 明史·吴宽传 from A_candidate to A with verified juan/passage refs.

---

## 5. Gnaeus Pompeius Magnus (Pompey)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/western/gnaeus-pompeius-magnus/` |
| **Person ID** | `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` |
| **Dates** | 106–48 BCE |
| **Canonical branch** | `collect/wang-yangming-and-pompey-v1` (PR#4) |
| **Status** | `ai_collected_unreviewed` |
| **Claims** | 42 (pre-split compound claims) |
| **Sources** | 15 (8 ancient + 7 modern) |
| **Relationships** | 12 |
| **Visual media** | 5 entries (all staging) |
| **Works** | 2 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized this sprint) |

**Source sufficiency:** Good. 15 sources for 42 claims. Classical sources (Plutarch, Appian, Cassius Dio, Caesar, Cicero) form the core with modern scholarship backing. Source verification sprint provided extensive Loeb references for Plutarch Pompey, Appian BC, and Cassius Dio.

**Weaknesses:**
- All classical source passage references marked `needs_verification` — verification sprint started but not all resolved
- Florus 2.13 passage does NOT match claimed "one of the most magnificent" superlative
- "Adulescentulus carnifex" attribution (Valerius Maximus 6.2.8) still needs_verification
- "Three legions" claim: Plutarch says "a legion" — number discrepancy unresolved
- 4 C-level sources present
- RRC coinage catalogue numbers not yet provided

**Obsidian suitability:** YES. Most extensive Western package (42 claims). Relationship types correctly remapped to v2.5. person_id standardized across all files. Compound claims pre-split.

**Recommended next action:** Complete source verification for remaining needs_verification classical passages. Add RRC numbers for coinage. Resolve Florus and Valerius Maximus discrepancies. Verify Ny Carlsberg Glyptotek bust inventory number.

---

## 6. Augustus (Octavian)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/western/augustus-octavian/` |
| **Person ID** | `P_WEST_ROMAN_001_AUGUSTUS` |
| **Dates** | 63 BCE–14 CE |
| **Canonical branch** | `collect/qiu-ying-and-augustus-v2-5` (PR#5) |
| **Status** | `ai_collected_unreviewed` |
| **Claims** | 35 |
| **Sources** | 18 (11 ancient/primary + 7 modern) |
| **Relationships** | 9 |
| **Visual media** | 3 entries (all staging) |
| **Works** | 2 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized from v2.3) |

**Source sufficiency:** Strong. 18 sources for 35 claims (0.51 sources per claim). Excellent ancient source coverage: Suetonius, Cassius Dio, Appian, Res Gestae, Tacitus, Plutarch, Nicolaus of Damascus, Velleius Paterculus, Cicero. Strong modern scholarship (Syme, Goldsworthy).

**Weaknesses:**
- Some Suetonius/Cassius Dio passage references still `needs_verification`
- Birth date discrepancy (22 vs 23 September) unresolved
- Livia/poison question correctly flagged as disputed; no resolution
- 1 C-level source present
- "First Roman emperor" framing correctly marked as reception — but may need caveat

**Obsidian suitability:** YES. Best-sourced Western package. Strong biographical narrative. Claims have both Chinese and English text. Caveats for Res Gestae self-presentation bias correctly included. Name stages covered in detail.

**Recommended next action:** Complete Suetonius/Cassius Dio Loeb chapter refs for remaining needs_verification claims. Resolve birth date discrepancy with cross-referencing to multiple ancient sources.

---

## 7. Mark Antony (Marcus Antonius)

| Field | Value |
|-------|-------|
| **Folder** | `incoming/western/mark-antony/` |
| **Person ID** | `P_WEST_ROMAN_002_MARK_ANTONY` |
| **Dates** | 83–30 BCE |
| **Canonical branch** | `collect/wu-kuan-and-mark-antony-v1` (PR#7) |
| **Status** | `ai_collected_unreviewed` |
| **Claims** | 35 |
| **Sources** | 11 (7 ancient + 4 modern) |
| **Relationships** | 13 |
| **Visual media** | 4 entries (all staging) |
| **Works** | 4 entries |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized in PR#7 hardening) |

**Source sufficiency:** Moderate. 11 sources for 35 claims (0.31 sources per claim). Ancient sources correctly leveled: Plutarch/Appian/Cassius Dio at B_high (secondary narratives with bias), Cicero/Caesar/Res Gestae at A_candidate (primary documents). No D or C sources. Strong modern scholarship (Pelling 1988, Goldsworthy 2010, Syme 1939).

**Weaknesses:**
- Birth year disputed (83 BCE derived from Cicero Phil.; Plutarch records age 53/56 at death)
- All ancient source citations marked `needs_verification` — no verified chapter/passage refs
- No Cleopatra VII package yet — relationship claims one-sided
- Only 4 modern scholarly sources for 35 claims — moderately dependent on ancient sources

**Obsidian suitability:** YES. Well-structured. Relationships schema v2.5 compliant (opponent, documented_association, spouse, etc.). Both English and Chinese claim text. Ancient bias caveats included.

**Recommended next action:** Add verified Loeb chapter/passage references for Plutarch Antony, Appian BC, Cassius Dio. Cross-reference Antony's age at death across all sources. Link to future Cleopatra VII package.

---

## Cross-Package Metrics

| Metric | Shen Zhou | Wang Yangming | Qiu Ying | Wu Kuan | Pompey | Augustus | Mark Antony |
|--------|-----------|---------------|----------|---------|--------|----------|-------------|
| Claims per source | 3.67 | 2.47 | 1.48 | 2.57 | 2.80 | 1.94 | 3.18 |
| Sources per claim | 0.27 | 0.41 | 0.68 | 0.39 | 0.36 | 0.51 | 0.31 |
| A/A_candidate % | 33% | 53% | ~65% | 71% | ~73% | ~78% | 100% |
| D-level sources | 1 | 0 | 1 | 1 | 0 | 0 | 0 |
| C-level sources | 2 | 5 | ~3 | 0 | 4 | 1 | 0 |
| Empty source_ids | 0 | 0 | 0 | 8 | 0 | 0 | 0 |
| Passes validation | YES | YES | YES | YES | YES | YES | YES |

---

## Priority Triage

### Tier 1 — Ready for Central Review (no blocking issues)
- **Augustus** — strongest source base; minor needs_verification clean-up only
- **Pompey** — extensive; source verification well under way
- **Qiu Ying** — strong scholarship; needs 明清画史笔记 source entries

### Tier 2 — Needs Light Fixes Before Review
- **Wang Yangming** — SRC014 placeholder replacement; otherwise solid
- **Mark Antony** — needs Loeb chapter refs; schema is v2.5 compliant

### Tier 3 — Needs Substantial Work
- **Shen Zhou** — only 6 sources; needs source enrichment
- **Wu Kuan** — 8 empty source_ids; needs source assignment
