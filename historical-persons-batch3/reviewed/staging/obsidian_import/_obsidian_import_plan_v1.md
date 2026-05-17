# Obsidian Import Plan v1

**Date:** 2026-05-16
**Status:** Planning only — no files imported yet
**Scope:** 22 staging-ready persons (7 MVP + 8 Batch 1 + 7 Batch 2)

---

## 1. Purpose

Create an Obsidian vault from the current staging JSON/JSONL packages as a proof-of-concept knowledge base for the Historical Persons Database.

Key principles:
- Existing JSON/JSONL packages are the source of truth — no new facts
- All AI-collected data remains `ai_collected_unreviewed` / staging — not master-approved
- The vault enables human review, navigation, and source auditing
- Do not treat the Obsidian vault as master until central review passes

---

## 2. Scope

Include all 22 staging persons:

**MVP (7):** Shen Zhou, Wang Yangming, Qiu Ying, Wu Kuan, Pompey, Augustus, Mark Antony
**Batch 1 (8):** Tang Yin, Wen Zhengming, Zhu Yunming, Xu Zhenqing, Julius Caesar, Cicero, Cleopatra VII, Marcus Agrippa
**Batch 2 (7):** Li Dongyang, Wang Ao, Li Mengyang, He Jingming, Lepidus, Octavia Minor, Sextus Pompey

Exclude: no new people, no visual/dashboard, no master promotion.

---

## 3. Recommended Vault Structure

```
history-persons-vault/
├── 00_Project/
│   ├── README.md
│   ├── Collection Rules.md
│   ├── Glossary.md
│   └── Review Status.md
├── 01_Persons/
│   ├── Chinese/
│   │   ├── wang-yangming.md
│   │   ├── shen-zhou.md
│   │   ├── ... (12 files)
│   └── Western/
│       ├── julius-caesar.md
│       ├── augustus-octavian.md
│       ├── ... (10 files)
├── 02_Events/
│   ├── battle-of-actium.md
│   ├── ming-court-1472-examination.md
│   └── ... (from events.jsonl)
├── 03_Sources/
│   ├── SRC_PLUTARCH_ANTONY.md
│   ├── SRC_MINGSHI_LMY_001.md
│   └── ... (from sources.jsonl)
├── 04_Relationships/
│   └── (cross-references, auto-generated links)
├── 05_Works/
│   ├── gallic-wars.md
│   ├── collected-works-of-paoweng.md
│   └── ... (from works.jsonl)
├── 06_Visual_Media/
│   └── (metadata only — no unverified images)
├── 90_Staging_Review/
│   ├── _import_log.md
│   ├── _validation_results.md
│   └── _known_issues.md
└── 99_Templates/
    ├── tpl-person.md
    ├── tpl-source.md
    ├── tpl-event.md
    └── tpl-work.md
```

---

## 4. Person Note Format

Each person produces one Markdown file under `01_Persons/{Chinese,Western}/`.

### 4.1 Frontmatter (YAML)

```yaml
---
person_id: P_CHN_MING_TANG_YIN
canonical_key: tang-yin
display_name: Tang Yin / 唐寅
primary_language: zh
culture: Chinese
period: Ming dynasty (1470–1524)
birth: "1470"
death: "1524"
historical_status: ai_collected_unreviewed
review_status: staging_ready
source_sufficiency: medium
tags:
  - ming-dynasty
  - wu-school
  - painting
  - poetry
  - batch-1
related_people:
  - "[[wen-zhengming]]"
  - "[[zhu-yunming]]"
  - "[[xu-zhenqing]]"
  - "[[shen-zhou]]"
related_events:
  - "[[ming-kechang-an-1499]]"
data_source_folder: incoming/chinese/tang-yin/
---
```

### 4.2 Body Structure

```
# Tang Yin / 唐寅

## Summary
(From person_record.json short_description — 2–4 sentences)

## Identity
- **Person ID:** P_CHN_MING_TANG_YIN
- **Birth:** 1470 (Chenghua 6)
- **Death:** 1524 (Jiajing 3)
- **Ancestral Home:** Wuxian, Suzhou
- **Primary Role:** Painter, poet, calligrapher

## Timeline
| Year | Event | Status |
|------|-------|--------|
| 1470 | Born in Wuxian, Suzhou | confirmed |
| 1498 | Passed provincial exam (解元) | confirmed |
| 1499 | Implicated in examination scandal (科场案) | disputed |
| ... | (from events.jsonl) | |

## Claims

### Confirmed
- (claims with confidence: confirmed, sourced)

### Probable
- (claims with confidence: probable)

### Disputed / Uncertain
- (claims with confidence: disputed, needs_verification)

### Reception & Later Groupings
- 明四家 (Four Masters of Ming) — reception label
- 江南四大才子 — folklore grouping

### Legendary / Fictional
- 唐伯虎点秋香 — fictional, not historical

## Relationships
| Related Person | Relation Type | Evidence Level | Source |
|---------------|---------------|----------------|--------|
| Wen Zhengming | documented_association | probable | SRC_TY_005 |
| ... | | | |

## Works
(From works.jsonl, grouped by work_status)

## Sources
(From sources.jsonl, grouped by reliability_level)

## Review Status
- **Current:** staging_ready
- **Source sufficiency:** medium
- **Key risks:** 科场案 guilt still uncertain; folk legend separation

## Open Questions
(From open_questions.md)
```

---

## 5. Frontmatter Fields Specification

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `person_id` | string | yes | Canonical ID from person_record.json |
| `canonical_key` | string | yes | Folder name / URL-safe slug |
| `display_name` | string | yes | Chinese + English name |
| `primary_language` | string | yes | `zh` or `en` |
| `culture` | string | yes | `Chinese`, `Roman`, `Ptolemaic` |
| `period` | string | yes | Dynasty or era with date range |
| `birth` | string | yes | Year or approximate |
| `death` | string | yes | Year or approximate |
| `historical_status` | string | yes | `ai_collected_unreviewed` (for all staging) |
| `review_status` | string | yes | `staging_ready`, `needs_source_enrichment` |
| `source_sufficiency` | string | yes | `high`, `medium`, `low` |
| `tags` | list | yes | Culture, period, roles, batch |
| `related_people` | list | yes | Wikilinks to other person notes |
| `related_events` | list | no | Wikilinks to event notes |
| `data_source_folder` | string | yes | Path to incoming/ package |

---

## 6. Claim Display Policy

Claims from `claims.jsonl` must be grouped by `confidence` and `claim_type`:

| Display Section | confidence values | claim_type values |
|----------------|-------------------|-------------------|
| **Confirmed** | `confirmed` | biography |
| **Probable** | `probable`, `high` | biography |
| **Disputed / Uncertain** | `disputed`, `needs_verification`, `low` | biography |
| **Reception & Later Groupings** | any | `reception_label`, `later_grouping_only` |
| **Legendary / Fictional** | any | `legend`, `fiction`, `folklore` |

Rules:
- Never mix reception/legendary claims into confirmed biography sections
- Claims marked `needs_verification` must display that tag visibly
- Each claim cites its `source_ids` inline

---

## 7. Source Note Policy

Sources reused across multiple persons should have one canonical note under `03_Sources/`.

Each source note:

```yaml
---
source_id: SRC_PLUTARCH_ANTONY
source_type: primary_text
reliability_level: B_high
verification_status: needs_verification
used_for_claim_ids:
  - CLM_MA_001
  - CLM_MA_005
---
# Plutarch, Life of Antony

- **Author:** Plutarch (c. 46–120 CE)
- **Citation:** Life of Antony, sections 1–87
- **Language:** Greek (Loeb Classical Library)
- **Reliability:** Ancient biography; uses earlier sources but includes moral commentary
- **Verification:** Exact passage/page references need verification against Loeb edition
- **Used for claims:** CLM_MA_001, CLM_MA_005
```

Rules:
- Only create source notes for non-D (non-clue) sources
- D / `clue_only` sources appear inline in person source lists, not as standalone notes
- Source notes are metadata — do not reproduce full source text
- Mark `needs_verification` prominently when exact page/passage is unverified

---

## 8. Relationship Display Policy

**Phase D approach (recommended):**

1. **Embed in person notes first** — each person note has a Relationships section with a table
2. **Auto-generate Wikilinks** — `related_people` frontmatter creates Obsidian backlinks
3. **Dedicated relationship notes later** — `04_Relationships/` for bidirectional summaries after import
4. **Graph database later** — relationships become edges in future SQLite/Neo4j import

Relationship types (from `relationships.jsonl`):
- `spouse`, `sibling`, `parent_child`, `family`
- `documented_association`
- `opponent`, `same_political_context`
- `teacher_student` (only where sourced)
- `later_grouping_only` (reception, not direct)

---

## 9. Visual Media Policy

All visual media remains **metadata only**. No images imported unless verified.

Visual media classification (from `visual_media.jsonl`):

| Classification | Meaning | Import? |
|---------------|---------|---------|
| `artwork_by_person` | Created by the person (not a portrait) | Metadata only |
| `later_traditional_portrait` | Later artistic imagining | Metadata only |
| `imagined_portrait` | Modern/fictional depiction | Metadata only |
| `coin_or_inscription` | Numismatic/epigraphic | Metadata if verified |
| `later_imagined_scene` | Historical scene painting | Metadata only |
| `not_a_likeness` | Misattributed portrait | Metadata only |
| `needs_verification` | Attribution uncertain | Metadata only |

No image files imported until source holder, object ID, attribution, date, and rights/license are verified.

---

## 10. Import Approach — Five Phases

### Phase A: Person Notes from person_record.json + person_profile.md
- Generate Markdown files with frontmatter + summary + identity
- No claims, sources, or relationships yet
- Verify all 22 files parse correctly
- **Output:** 22 person notes in `01_Persons/`

### Phase B: Claims Tables from claims.jsonl
- Add claims grouped by confidence/type to each person note
- Each claim row: claim_id | statement | confidence | source_ids | date
- Run validation to confirm no claim is orphaned from its sources
- **Output:** 385 claim rows distributed across 22 notes

### Phase C: Source Notes from sources.jsonl
- Create canonical source notes for all non-D sources
- Cross-link source notes to person notes that use them
- Add inline source lists for D/clue sources
- **Output:** ~100 source notes in `03_Sources/`

### Phase D: Relationships, Events, Works
- Add relationship tables to person notes
- Create event notes from events.jsonl
- Create work notes from works.jsonl
- Auto-generate Wikilinks and backlinks
- **Output:** Linked graph across all vault sections

### Phase E: Manual Review in Obsidian
- Human reviewer opens vault, checks 2 pilot persons first
- Verifies frontmatter, claims grouping, source links
- Flags errors, missing links, misclassified claims
- Approves or rejects each phase before proceeding

---

## 11. File Naming Convention

| Section | Pattern | Example |
|---------|---------|---------|
| Chinese persons | `{canonical_key}.md` | `tang-yin.md` |
| Western persons | `{canonical_key}.md` | `julius-caesar.md` |
| Events | `{event_key}.md` | `battle-of-actium.md` |
| Sources | `{source_id}.md` | `SRC_PLUTARCH_ANTONY.md` |
| Works | `{work_key}.md` | `gallic-wars.md` |
| Templates | `tpl-{type}.md` | `tpl-person.md` |

Canonical keys are the folder names from `incoming/`:
- Chinese: `tang-yin`, `wen-zhengming`, `li-dongyang`, etc.
- Western: `julius-caesar`, `marcus-agrippa`, `cleopatra-vii`, etc.

---

## 12. Import Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Duplicate person_id | Low | All 22 person_ids verified unique |
| Inconsistent source levels | Medium | A_candidate vs B_high varies by package; document in source notes |
| Too many unverified claims | Medium | `needs_verification` tag visible; reviewer can filter in Obsidian |
| Markdown tables too large | Low | Largest packages have 37 claims — manageable; split if needed |
| Internal links break on rename | Low | Use canonical_key as filename; stable across normalization |
| Visual media rights | Info | No images imported; metadata only |
| Obsidian becomes accidental master | High | **All files stamped `ai_collected_unreviewed`; banner at top of every note** |
| Schema inconsistency | Low | Chinese Batch 2 vs Western schema differences; document in 00_Project |
| Li Dongyang SRC_LDY_003 | Low | Already B_high + needs_verification; acceptable for staging |

---

## 13. Recommended Next Actions

1. **Central reviewer reviews this plan** — confirm vault structure, frontmatter fields, claim grouping policy
2. **Pilot import for 2 persons only:**
   - Tang Yin / 唐寅 (Chinese, 18 claims, rich legend/folk separation)
   - Julius Caesar (Western, 18 claims, reception/literary separation)
3. **Phase A only** — generate Markdown from person_record.json + person_profile.md
4. **Manual review** of 2 pilot notes in Obsidian
5. **Approve pilot** → proceed to Phase A for all 22
6. **Phase B–E** follow after Phase A approval
7. **Do not start Batch 3** until Obsidian import plan is reviewed and pilot approved
