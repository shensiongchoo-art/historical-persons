# PR #7 Initial Review — Wu Kuan + Mark Antony
**Branch:** `maintenance/pr-triage-after-hardening-v1`
**Date:** 2026-05-12
**PR:** https://github.com/shensiongchoo-art/historical-persons/pull/7

---

## Wu Kuan (吴宽) — `incoming/chinese/wu-kuan/`

### Schema Issues (CRITICAL — full v2.3 schema)

Claims use old schema:
- `text_zh` / `text_en` → needs `claim_text_zh` / `claim_text_en`
- `category` → needs `claim_type`
- No `person_id` field on claims

Sources use old schema:
- `level` → needs `reliability_level`
- `bibliographic_hint` → needs `citation_detail`
- No `author` field
- `source_type` field present but values differ from v2.5 (e.g. `ancient_text_critical_edition` vs v2.5 allowed types)

Relationships use old schema:
- `rel_id` → needs `relationship_id`
- `person_a` / `person_b` → needs `person_id` / `related_person_name`
- `description_zh` / `description_en` → needs `evidence_note`

### Source Discipline (HIGH)

| Source | Level | Usage | Issue |
|--------|-------|-------|-------|
| SRC_WK_001 (明史) | A | 7 claims | Good — but needs juan number |
| SRC_WK_005 (Baidu Baike) | C | 13 of 18 claims | **Overused** — promote claims to A-level sources |
| SRC_WK_003 (书架书目) | A | 0 claims | Dubious as A — personal library catalogue, not a source per se |
| SRC_WK_006 (Palace Museum) | A | 1 claim | Good — material evidence |
| SRC_WK_002 (文集) | A | 1 claim | Good — primary text |

### Overstrong Wording

- CLM_WK_012 / REL_WK_001: "close friends" with Shen Zhou → downgrade to `documented_association`
- CLM_WK_008: "most important poetic figure" → correctly at `probable/medium` but wording should be softened
- CLM_WK_010: "foundational figure of Wu School of Calligraphy" → correctly at `reception`

### Claims Needing Downgrade

| Claim | Current | Suggested | Reason |
|-------|---------|-----------|--------|
| CLM_WK_008 | `probable/medium` | Keep as `probable` | "Most important" needs peer support |
| CLM_WK_012 | `confirmed/high` | `confirmed/medium` | "Close friends" relies on Baidu; needs Ming source |

### Recommended Actions

1. Full v2.3→v2.5 schema normalization
2. Replace Baidu Baike (SRC_WK_005) claim support with 明史 or Dictionary of Ming Biography
3. Add exact juan number for 明史·吴宽传
4. Soften "close friends" → "documented association"
5. Check if 吴宽传 exists in 明史 and at what juan

---

## Mark Antony (Marcus Antonius) — `incoming/western/mark-antony/`

### Schema Issues (HIGH — mixed v2.5-ish)

Claims:
- Has `person_id` ✓
- Uses `claim_text` (single field) instead of `claim_text_en` (v2.5 needs separate en/zh fields)
- Uses `category` instead of `claim_type`
- Has `status_note` field which v2.5 doesn't use

Sources:
- Uses `level` instead of `reliability_level`
- Uses `type` instead of `source_type`
- Missing `citation_detail` field
- Has `title_orig` which is non-standard but useful (keep as-is)

### Relationship Type Issues (CRITICAL)

| Current Type | v2.5 Allowed? | Suggested |
|-------------|---------------|-----------|
| `commander_and_subordinate` | No | `documented_association` |
| `political_opponent` | No | `opponent` |
| `romantic_partner_and_political_ally` | No | Split: `spouse` or `documented_association` |
| `political_ally_then_rival` | No | `same_political_context` (compound — needs splitting) |
| `marriage` | No | `spouse` |
| `military_opponent` | No | `opponent` |
| `stepchild_and_political_ally` | No | `family` or `documented_association` |
| `family` | Yes | Keep ✓ |

### Source Discipline (GOOD)

All 7 ancient sources correctly at A-level with explicit bias caveats:
- Plutarch: "∼130 years after Antony's death...incorporates anti-Antonian propaganda"
- Appian: "draws on sources hostile to Antony"
- Cassius Dio: "heavily influenced by Augustan tradition"
- Cicero's Philippics: "contemporary hostile source by Antony's political enemy"
- Caesar's Civil War: "contemporary but self-serving"
- Suetonius: "draws on Augustan-era sources"
- Res Gestae: "propaganda but contemporary"

Modern sources (Goldsworthy 2010, Syme 1939, Pelling 1988) correctly at B_high.

### Augustus Propaganda Handling (GOOD)

- CLM_MA_035: Correctly categorized as `reception` with detailed note on Augustan propaganda tradition
- CLM_MA_026: Antony's will correctly marked `probable` — "may have been forged or altered by Octavian"
- CLM_MA_028: Senate war declaration correctly notes Octavian's framing tactics

### Recommended Actions

1. Schema normalization: `level`→`reliability_level`, `type`→`source_type`, add `citation_detail`
2. Claims: `claim_text`→`claim_text_en`, `category`→`claim_type`
3. Relationship types: remap all non-v2.5 types to allowed set
4. Add Loeb Classical Library references for ancient sources (as done for Pompey/Augustus)
5. Add Chinese translations to claims (claim_text_zh) per v2.5 bilingual requirement
6. Verify `person_id`: `P_WEST_ROMAN_002_MARK_ANTONY` — should it follow the late-Republic pattern?

---

## Overall PR #7 Readiness

**Not ready for merge.** Both packages pass validation but need v2.5 hardening.

Estimated work:
- Wu Kuan: Heavy — full schema normalization + source strengthening
- Mark Antony: Moderate — schema normalization + relationship type cleanup
