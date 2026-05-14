# Central Review: 沈周 (Shen Zhou)

**Reviewer:** MorphMind AI
**Date:** 2026-05-14
**Package:** `incoming/chinese/shen-zhou/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_SHEN_ZHOU` |
| **Name (ZH)** | 沈周 |
| **Name (EN)** | Shen Zhou |
| **Birth** | 1427 (宣德二年十一月二十一日) |
| **Death** | 1509 (正德四年) |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#1 (`collect/shen-zhou-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 native |

---

## 2. Current Package Status

Package is complete (11/11 required files) and passes validation. All relationship types remapped to v2.5 during hardening sprint (PR #8). Birth year discrepancy (1427 vs 1472 in some references) remains unresolved.

---

## 3. Overall Central Review Verdict

**STAGING ONLY — NOT READY FOR MASTER PROMOTION.** Source base is critically thin (6 sources for 22 claims). No `A`-level verified source. Primary biography (明史·隐逸传) not represented as a discrete source entry. D-level general web source present. Needs source enrichment and passage verification before any claim can be promoted to master.

---

## 4. Master-Candidate Facts

- Shen Zhou lived 1427–1509 in Suzhou, Ming Dynasty
- Major Ming dynasty painter, calligrapher, poet
- Descended from a wealthy scholar-official family; never held civil service office
- Associated with the Wu School (吴门画派) in later art-historical classification

---

## 5. Staging-Only Claims

- Most relationship claims at `probable/medium` — rely on secondary sources, not primary correspondence or colophons
- "Founder of Wu School" (C009) correctly marked `reception`
- Several identity claims depend on A_candidate sources with unverified passage refs

---

## 6. Reception / Legendary / Disputed Material

- "明四家" (Four Masters of the Ming) — correctly flagged as reception_label and later_grouping_only
- "吴门画派 founder" — correctly reception
- Birth year 1427 vs references giving 1472 — unresolved discrepancy

---

## 7. Source Issues

| Issue | Severity |
|-------|----------|
| Only 6 sources for 22 claims | High |
| No `A`-level source (all A_candidate or lower) | High |
| D-level source (SRC006) present | Medium |
| 明史·隐逸传 biography not a discrete source | High |
| No passage-level verified source from primary biographical text | High |
| 2 C-level sources (general web) | Medium |

---

## 8. Relationship Issues

| Issue | Detail |
|-------|--------|
| Teacher-student evidence | Relies on secondary sources, not primary colophons or inscriptions |
| "Close friends" wording | Removed in hardening; replaced with documented_association |
| Relationship count (13) | Includes several later_grouping_only entries |

---

## 9. Visual Media Issues

- All 3 visual media entries are `staging`
- No verified contemporary portrait
- Source holder and object IDs not verified

---

## 10. Recommended Cleanup Actions

1. Add 明史·隐逸传 (卷298) as discrete A_candidate source with juan ref
2. Add 沈周年谱 (Chen Zhenlian or equivalent) as B_high scholarly source
3. Remove or demote D-level source SRC006
4. Promote C-level sources to B with passage refs where possible
5. Resolve birth year discrepancy with cross-referenced academic sources
6. Add Qing dynasty art-historical sources (e.g., 《无声诗史》, 《明画录》) as discrete sources

---

## 11. Obsidian Demo Suitability

**YES — suitable for demo with caveats.** Well-structured package with 11 complete files. Claims are split into individual JSONL rows. person_id is consistent. The thin source base is the main limitation — the demo would show structure but not depth of sourcing.

---

## 12. Do-Not-Promote-Yet Notes

- **Do not promote to master_candidates** until source density improves to at least 10 sources and 明史·隐逸传 is represented as a discrete source with verified passage refs
- **Do not use for relational claims** about teacher-student relationships until primary evidence (letters, colophons) is cited
