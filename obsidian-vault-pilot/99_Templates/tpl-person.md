---
person_id: "{{PERSON_ID}}"                # e.g. P_CHN_MING_TANG_YIN  or  P_WEST_LATE_REPUBLIC_GAIUS_JULIUS_CAESAR
canonical_key: "{{canonical-key}}"        # url-safe slug; matches incoming/ folder name; used as filename
display_name: "{{Display Name / 中文名}}"  # bilingual ZH/EN
primary_language: "{{zh-Hans|zh|en}}"     # zh-Hans / zh / en
culture: "{{Chinese|Roman|Ptolemaic|...}}"
period: "{{Period (Dynasty or Era with date range)}}"
birth: "{{YYYY or YYYY BCE}}"
death: "{{YYYY or YYYY BCE}}"
historical_status: ai_collected_unreviewed       # FIXED for staging
review_status: "{{staging_ready|needs_source_enrichment}}"
source_sufficiency: "{{adequate_with_caveats|to_be_reviewed|high|medium|low}}"
data_source_folder: "{{incoming/chinese/<slug>/  or  incoming/western/<slug>/}}"
tags:
  - "{{culture-or-period-tag}}"
  - "{{role-tag}}"
  - "{{batch-tag}}"
related_people:
  - "[[{{canonical-key-of-related-person}}]]"
---

> ⚠️ **AI-COLLECTED / STAGING ONLY** — Not yet reviewed by a subject-matter expert. Do not cite as master-approved.

# {{Display Name / 中文名}}

## Summary

<!-- 2–4 sentences from person_record.json short_description. Bilingual: ZH paragraph first, then EN paragraph (or vice versa for Western figures). The summary must NOT use stronger language than the structured claims — see MVP rules v2.5 "Description cannot be stronger than claims". -->

---

## Identity

| Field | Value |
|-------|-------|
| **Person ID** | `{{PERSON_ID}}` |
| **Display Name** | {{Display Name}} |
| **Courtesy / Art Names** | {{optional}} |
| **Birth** | {{date + era}} |
| **Death** | {{date + era}} |
| **Place of Origin / Death** | {{optional}} |
| **Primary Role** | {{painter, general, statesman, etc.}} |
| **Culture** | {{Chinese, Ming Dynasty / Roman, Late Republic / etc.}} |

---

## Life Timeline

| Year | Event | Status |
|------|-------|--------|
| {{YYYY}} | {{event description}} | confirmed / probable / disputed / reception |

<!-- Sourced from events.jsonl plus key dates from person_profile.md. Use ONLY the status labels allowed by MVP rules v2.5: confirmed / probable / disputed / legendary / fictional / reception / unknown / needs_verification. -->

---

## Key Historical / Reception / Legend / Fiction Separation

### Confirmed Historical Facts
- {{fact 1}}
- {{fact 2}}

### Disputed / Uncertain
- {{disputed item}}

### Source Caveats
- {{e.g. primary source is self-serving / later compilation / etc.}}

### Reception / Later Groupings (not formal organizations)
- **{{label}}** — {{explanation that this is a later historiographical grouping, NOT a contemporary institution}}

### Legendary / Fictional
- **{{legend title}}** — {{state explicitly this is fiction/legend, not historical biography}}

---

## Claims Overview

| Status | Count |
|--------|-------|
| Confirmed | {{n}} |
| Probable | {{n}} |
| Disputed | {{n}} |
| Reception | {{n}} |
| Legendary | {{n}} |
| **Total** | **{{n}}** |

---

## Confirmed Historical Claims

| Claim ID | Date | Claim | Sources |
|----------|------|-------|---------|
| {{CLM_XX_001}} | {{date or —}} | {{statement}} | [[{{SRC_XX_001}}]] |

<!-- One row per claim where confidence == confirmed AND claim_type == biography. -->

---

## Probable / Disputed Claims

| Claim ID | Date | Claim | Status | Sources |
|----------|------|-------|--------|---------|
| {{CLM_XX_006}} | {{date}} | {{statement}} | probable / disputed / needs_verification | [[{{SRC_XX_001}}]] |

<!-- Group probable + disputed + needs_verification together. Mark each row's specific status in the Status column. -->

---

## Reception / Legendary Material

| Claim ID | Type | Claim | Sources |
|----------|------|-------|---------|
| {{CLM_XX_010}} | reception | {{statement using "后世美术史中常被视为..." / "later regarded as..."}} | [[{{SRC_XX_007}}]] |
| {{CLM_XX_015}} | legendary | {{state explicitly: this is later legend, not historical biography}} | (no sources - classified as legendary) |

<!-- Never mix reception/legendary claims into the confirmed biography sections above. Reception language must NOT be stronger than "later regarded as..." per MVP rules v2.5. -->

---

## Relationships

| Person | Relationship Type | Status | Sources | Notes |
|--------|-------------------|--------|---------|-------|
| {{Related person name}} ([[{{canonical-key}}]]) | {{relationship_type}} | ai_collected_unreviewed | [[{{SRC_XX_001}}]] | {{summary}} |

<!--
Rules:
- Use ONLY the relationship_type values present in relationships.jsonl.
- Do NOT invent friendship/influence/teacher-student beyond source evidence.
- Allowed types from MVP rules v2.5 relationship discipline:
    family, documented_teacher_student, probable_teacher_student,
    documented_association, probable_association,
    same_cultural_circle, same_political_context,
    patronage_or_commission, correspondence_or_textual_exchange,
    later_grouping_only, reception_label, opponent, rival, ally
- Plain text (no [[...]]) for related persons with empty related_person_id.
- Do NOT create new person notes from relationship rows.
-->

---

## Works

| Work | Type | Status | Sources | Notes |
|------|------|--------|---------|-------|
| {{title_zh (title_en)}} | {{work_type}} | ai_collected_unreviewed | [[{{SRC_XX_001}}]] | {{description}} |

> ⚠️ Artworks by this person are `artwork_by_person`, not portrait likenesses of them. Per MVP rules v2.5 visual-media discipline, these are creative output and not evidence of physical appearance.

<!-- Do NOT create standalone work notes during initial import. -->

---

## Sources

### A / A_candidate (primary or near-primary)

| Source ID | Title | Type | Reliability | Verification Status |
|-----------|-------|------|-------------|---------------------|
| [[{{SRC_XX_001}}]] | {{title}} | {{official_history / collected_works / primary_text / etc.}} | A_candidate | ai_verified_unreviewed |

### B_high / B (modern scholarship & ancient biography)

| Source ID | Title | Type | Reliability | Verification Status |
|-----------|-------|------|-------------|---------------------|
| [[{{SRC_XX_003}}]] | {{title}} | academic_monograph / ancient_biography / academic_paper | B_high | ai_verified_unreviewed |

### C / D / clue_only (encyclopedia & general reference)

| Source ID | Title | Type | Reliability | Verification Status |
|-----------|-------|------|-------------|---------------------|
| [[{{SRC_XX_005}}]] | {{Baidu / Wikipedia / Britannica}} | encyclopedia | D | clue_only |

*Note: D-level sources are kept for research traceability only — never as sole support for a claim. See each note's `🚫 D-LEVEL — CLUE ONLY` banner.*

### ⚠️ Flagged: needs_verification

| Source ID | Title | Reliability | Status |
|-----------|-------|-------------|--------|
| [[{{SRC_XX_004}}]] | {{title}} | {{A_candidate / B_high}} | needs_verification |

<!-- If no sources are flagged needs_verification, write: "*None — all sources are currently ai_verified_unreviewed or clue_only.*" -->

---

## Source Package

Path: `{{incoming/chinese/<slug>/  or  incoming/western/<slug>/}}`
Files: 11 (person_record.json, person_profile.md, claims.jsonl, sources.jsonl, relationships.jsonl, events.jsonl, works.jsonl, visual_media.jsonl, legendary_notes.jsonl, open_questions.md, README.md)
Validation: {{PASSED / FAILED — note}}

---

## Review Status

- **Current:** `ai_collected_unreviewed` — staging-ready, not master-approved
- **Source sufficiency:** {{adequate_with_caveats / to_be_reviewed / high / medium / low}} — {{n}} sources ({{m}} non-D), source density {{x.xx}}
- **Next review actions:**
  - {{specific verification action 1}}
  - {{specific verification action 2}}

---

## Open Questions

- {{question 1, from open_questions.md}}
- {{question 2}}

---

<!--
TEMPLATE NOTES (delete before publishing):
- Filename = `{{canonical_key}}.md` placed under 01_Persons/Chinese/ or 01_Persons/Western/.
- Frontmatter keys are case-sensitive; do not reorder.
- The AI-COLLECTED banner immediately after the H1 is REQUIRED on every person note.
- Status labels allowed: confirmed / probable / disputed / legendary / fictional / reception / unknown / needs_verification.
- Reception language: "后世美术史中常被视为..." / "later regarded as..." — never assert reception as fact.
- One claim = one fact. Compound claims must be split before they reach this template.
- Wikilinks to related people are forward references — DO NOT create those notes during single-person import.
-->
