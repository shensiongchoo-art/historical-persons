# MVP Hardening Report v1
**Branch:** `hardening/mvp-current-prs-v1`
**Date:** 2026-05-12
**Sprint:** MVP Hardening Sprint v1

---

## 1. PR Inventory and Disposition Recommendations

| PR # | Branch | Persons | Recommendation | Reason |
|------|--------|---------|---------------|--------|
| #1 | `collect/shen-zhou-v1` | 沈周 | **Keep / merge after review** | Full v2.5 package; all fixes applied in this sprint |
| #2 | `collect/gnaeus-pompeius-magnus-v1` | Pompey (partial) | **Close** | Only 2 files (claims.jsonl, open_questions.md); superseded by PR#4's complete Pompey package |
| #4 | `collect/wang-yangming-and-pompey-v1` | Wang Yangming + Pompey | **Keep / merge after review** | Both packages complete and hardened; canonical for both persons |
| #5 | `collect/qiu-ying-and-augustus-v2-5` | Qiu Ying + Augustus | **Keep / revise then merge** | v2.3 schema normalized to v2.5 in this sprint; packages pass validation |
| #6 | `verification/source-reports-v1` | N/A | **Defer** | Source verification work; separate track from hardening sprint |
| #7 | `collect/wu-kuan-and-mark-antony-v1` | Wu Kuan + Mark Antony | **Defer** | New persons outside MVP hardening scope; review in next sprint |

---

## 2. Canonical Package Decision Per Person

| Person | `person_id` | Canonical Branch | Status After Sprint |
|--------|------------|-----------------|---------------------|
| 沈周 Shen Zhou | `P_CHN_MING_SHEN_ZHOU` | PR#1 | Staging-quality, PASSED |
| 王阳明 Wang Yangming | `P_CHN_MING_WANG_YANGMING` | PR#4 | Staging-quality, PASSED |
| Gnaeus Pompeius Magnus | `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` | PR#4 | Staging-quality, PASSED |
| 仇英 Qiu Ying | `P_CHN_MING_001_QIU_YING` | PR#5 (v2-5 branch) | Staging-quality, PASSED |
| Augustus Octavian | `P_WEST_ROMAN_001_AUGUSTUS` | PR#5 (v2-5 branch) | Staging-quality, PASSED |

---

## 3. Staging-Quality Assessment Per Person

### 沈周 Shen Zhou — STAGING QUALITY: ACCEPTABLE

**Fixes applied:**
- All relationship types remapped to v2.5 allowed set (family, documented_teacher_student, probable_teacher_student, documented_association, probable_association, same_cultural_circle, later_grouping_only)
- Claims C014, C018: overstrong "friend/close friends" wording replaced with "documented association" language
- Claim C019: "close relationship" wording removed; teacher-student fact retained
- Claim C009 ("founder of Wu School"): correctly `status=reception` — no change needed

**Remaining issues:**
- Only 6 sources; many `A_candidate` or lower; no single passage-level verified source
- D-level source present (general web)
- Birth year (1427) vs some references (1472) discrepancy unresolved; open question logged
- `SRC004` (secondary) used as evidence for several confirmed claims

**Recommended next action:** Source verification sprint — confirm passage refs in 明史·隐逸传 and/or 沈周年谱

---

### 王阳明 Wang Yangming — STAGING QUALITY: ACCEPTABLE

**Fixes applied:**
- R002 (陆九渊): `philosophical_predecessor` → `reception_label`, status → `reception/medium`; curly-quote JSON error fixed (`「陆王心学」`)
- SRC014 (日本阳明学): downgraded `B_high` → `B`, marked as placeholder pending real monograph citation
- Compound claims (name titles, Ning rebellion, Tianquan Bridge, Four-Sentence Teaching) already split in PR#4 — retained
- Tang Yin and Zhu Yunming relationships correctly absent (no evidence rows)

**Remaining issues:**
- SRC014 is a placeholder; claims C025–C026 (Japanese Yangmingism) rely on it
- Several `A_candidate` sources (传习录, 大学问, 王文成公全书, 明史) lack specific edition/passage refs
- 5 C-level (general web) sources present; claims traceable to them need promotion to academic sources
- `needs_verification` claim present (C027)

**Recommended next action:** Replace SRC014 placeholder with specific Julia Ching or equivalent monograph; promote key sources from A_candidate to A with passage refs

---

### Gnaeus Pompeius Magnus (Pompey) — STAGING QUALITY: ACCEPTABLE

**Fixes applied:**
- `person_id` standardized: `P_WEST_ROMAN_REPUBLIC_...` → `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` across all 8 package files (88 occurrences)
- Relationship types: `political_ally` → `same_political_context`, `political_ally_then_opponent` → `same_political_context`, `marriage` × 3 → `spouse`
- Claim C028: `confirmed_misattribution` → `reception`
- Source base: PR#4 complete package used (PR#2 partial package superseded)
- Compound claims (Julia's death, Luca renewal, Crassus death, Pharsalus) already split — retained

**Remaining issues:**
- All classical source passage references (Plutarch, Appian, Cassius Dio) marked `needs_verification` — requires Loeb Classical Library or equivalent references
- Crawford RRC catalogue numbers for coinage not yet provided
- Pompey portrait bust identification (Ny Carlsberg Glyptotek) unverified
- Ptolemy XIII's advisors (Pothinus, Theodotus, Achillas) unverified against primary sources
- 4 C-level sources present

**Recommended next action:** Dedicated source verification sprint (PR#6 track) — Loeb refs for Plutarch Life of Pompey, Appian BC, Cassius Dio; RRC numbers for coinage

---

### 仇英 Qiu Ying — STAGING QUALITY: ACCEPTABLE (post-normalization)

**Fixes applied:**
- Full v2.3 → v2.5 schema normalization: claims (`text_zh/en/category` → `claim_text_zh/en/claim_type` + `person_id`), sources (`level` → `reliability_level`), relationships (`rel_id/person_a/person_b/description_en` → `relationship_id/person_id/related_person_name/evidence_note`)
- REL_QY_004: `influence` → `later_grouping_only` (indirect retrospective stylistic connection to Shen Zhou)
- Open question #13 added: 明清画史笔记 sources (无声诗史, 明画录, 图绘宝鉴续编) not yet represented as discrete source entries

**Remaining issues:**
- Birth/death dates still uncertain (range 1482–1505 for birth, 1552 for death); correctly flagged as approximate
- 明清画史笔记 sources missing as discrete source entries — several claims rely on them via summary source
- Cleveland Art Museum work (赵孟頫写经换茶图) unverified in online catalogue
- Systematic real/forgery distinction for attributed works not complete
- D-level source present

**Recommended next action:** Add discrete source entries for 无声诗史, 明画录, 图绘宝鉴续编 with edition details; verify Cleveland Art Museum catalogue

---

### Augustus (Octavian) — STAGING QUALITY: ACCEPTABLE (post-normalization)

**Fixes applied:**
- Full v2.3 → v2.5 schema normalization (same as Qiu Ying)
- Relationships: `ally` × 3 → `same_political_context` (Lepidus, Cicero) and `documented_association` (Agrippa)
- Ancient sources (Suetonius, Cassius Dio, Appian, Res Gestae, Tacitus, Plutarch, Nicolaus, Velleius, Cicero) correctly retained at level A or A_candidate
- Res Gestae self-presentation caveat retained in CLM_AU_018 and CLM_AU_027
- "First Roman emperor" framing: `reception/medium` in CLM_AU_022
- Compound claims (name stages, marriages, titles, settlements, Actium) already split — retained

**Remaining issues:**
- Some Suetonius/Cassius Dio passage references still `needs_verification`; specific chapter numbers present for a subset only
- Birth date discrepancy (22 vs 23 September) unresolved — open question logged
- Livia/poison question correctly flagged as `disputed` / hostile tradition
- 3 B-level and 1 C-level sources present

**Recommended next action:** Source verification sprint — provide specific Suetonius Loeb chapter refs and Cassius Dio book/chapter for remaining `needs_verification` claims

---

## 4. Known Data-Quality Issues by Category

### 4.1 Source Discipline
- `A_candidate` used correctly where edition/passage unverified — needs verification sprint to promote
- Several packages have C-level (Wikipedia, Baidu) sources; these are correctly flagged as leads only, not sole claim support
- Placeholder source (Wang Yangming SRC014) must be replaced before promoting dependent claims

### 4.2 Claim Confidence
- Claims at `probable/medium` correctly represent uncertain attributions (e.g., Shen Zhou–陈宽 teacher-student, Qiu Ying birth dates)
- `reception` correctly used for later historiographical constructions (明四家, 陆王心学, "first Roman emperor")
- No claims of `confirmed/high` rely solely on C-level sources after this sprint

### 4.3 Relationship Integrity
- All packages now use only v2.5 allowed relationship types
- `same_cultural_circle` and `later_grouping_only` used appropriately to avoid inferring direct relationships from group labels
- Spouse relationships now correctly typed as `spouse` (not `marriage`)

### 4.4 JSON/Schema Integrity
- All 5 packages pass `tools/validate_package.py` after this sprint
- Wang Yangming relationships.jsonl JSON error (unescaped double quotes in evidence_note) resolved

---

## 5. Recommended Next Actions for Central Reviewer

**Immediate (before any PR merge):**
1. Review `hardening/mvp-current-prs-v1` branch — confirm all 5 package hardening edits are acceptable
2. Close PR#2 (`collect/gnaeus-pompeius-magnus-v1`) — partial package; Pompey canonical is PR#4
3. Mark `collect/qiu-ying-and-augustus-v1` as superseded — v2-5 branch is the canonical version

**Short-term (next sprint):**
4. Source verification sprint (PR#6 track) — provide Loeb Classical Library passage refs for Pompey and Augustus classical sources
5. Promote Wang Yangming SRC014 placeholder to a real academic monograph (Julia Ching or equivalent)
6. Add 无声诗史, 明画录, 图绘宝鉴续编 as discrete source entries in Qiu Ying package
7. Resolve Shen Zhou birth year discrepancy (1427 vs 1472 in Wikipedia)

**Medium-term:**
8. Review PR#7 (Wu Kuan + Mark Antony) in next expansion sprint
9. Systematic visual media verification (all packages have `visual_media.jsonl` with `staging` or `needs_verification` status — do not promote to master without source holder + object ID + rights confirmation)
