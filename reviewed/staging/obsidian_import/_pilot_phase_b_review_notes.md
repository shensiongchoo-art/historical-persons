# Pilot Phase B Review Notes

**Date:** 2026-05-16
**Branch:** `pilot/obsidian-phase-a-tang-yin-caesar-v1` (continuing on PR #33)
**Scope:** Claims tables added to 2 pilot notes from claims.jsonl

---

## 1. Files Updated

| File | Change |
|------|--------|
| `obsidian-vault-pilot/01_Persons/Chinese/tang-yin.md` | +3 claim tables: 10 confirmed, 5 probable/disputed, 3 reception/legendary |
| `obsidian-vault-pilot/01_Persons/Western/julius-caesar.md` | +2 claim tables: 16 confirmed, 2 reception/legendary |

Both notes retain: YAML frontmatter, AI-COLLECTED banner, Summary, Identity, Timeline, Fact/Legend Separation, Source Package, Review Status, Open Questions.

---

## 2. Claim Counts

### Tang Yin / 唐寅

| Status | Count | Claim IDs |
|--------|-------|-----------|
| Confirmed | 10 | CLM_TY_001–005, 007–009, 013–014 |
| Probable | 4 | CLM_TY_012, 016–018 |
| Disputed | 1 | CLM_TY_006 (examination scandal culpability) |
| Reception | 2 | CLM_TY_010 (明四家), CLM_TY_011 (吴中四才子) |
| Legendary | 1 | CLM_TY_015 (唐伯虎点秋香) |
| **Total** | **18** | |

### Julius Caesar

| Status | Count | Claim IDs |
|--------|-------|-----------|
| Confirmed | 16 | CLM_JC_001–004, 006–015, 017–018 |
| Probable | 0 | — |
| Disputed | 0 | — |
| Reception | 1 | CLM_JC_005 (First Triumvirate as later label) |
| Legendary | 1 | CLM_JC_016 (Et tu, Brute?) |
| **Total** | **18** | |

---

## 3. Readability Assessment

### What works
- **Grouping by status** keeps confirmed biography separate from legend/reception — Obsidian reader can quickly scan confirmed facts
- **Tang Yin 10 confirmed claims** fits comfortably in one table (no horizontal scroll at 80-char width)
- **Julius Caesar 16 confirmed claims** is large but still scrollable in Obsidian; splitting by category (career / military / relationships / death) could improve readability but is low priority
- **Source IDs only** keeps rows short — full source notes are deferred to Phase C
- **Chinese-first display for Tang Yin** with English implicit in claim_text_zh field
- **Probable/disputed table** uses bold **disputed** status tag for quick identification

### Minor concerns
- Caesar's 16-row confirmed table may require vertical scrolling in Obsidian on small screens — acceptable for pilot
- Tang Yin's probable/disputed section mixes 4 probable + 1 disputed — the **disputed** tag is bolded for visibility
- No source descriptions yet — Phase C will add one-sentence inline source labels

### Verdict
Both tables are readable and scannable. No blocking issues for pilot review.

---

## 4. Phase C Recommendation

**Proceed with Phase C (source notes) for the 2 pilot persons.**

Phase C would:
1. Create `obsidian-vault-pilot/03_Sources/` directory
2. Create one markdown note per non-D source (e.g., `SRC_TY_001.md`, `SRC_JC_003.md`)
3. Add source YAML frontmatter: source_id, source_type, reliability_level, verification_status
4. Cross-link source notes from claim tables (replace bare source_id with `[[SRC_TY_001]]` wikilinks)

Estimated source notes:
- Tang Yin: 7 non-D sources (SRC_TY_001–004, 007, 009 + 1 more) → ~7 source notes
- Julius Caesar: 7 non-D sources (SRC_JC_001–007) → ~7 source notes

---

## 5. Full 22-Person Import Readiness

| Criterion | Status |
|-----------|--------|
| Phase A format approved | ✓ (PR #33 Phase A notes structurally sound) |
| Phase B claims tables tested | ✓ (this PR: Tang Yin 18 claims, Caesar 18 claims) |
| Phase C source notes tested | ✗ — needed before scaling |
| Phase D relationships/events tested | ✗ — lower priority |
| Schema inconsistency handled | ✗ — Chinese Batch 2 uses simpler schema; normalization recommended |
| All 22 validated | ✓ (all PASSED) |

**Recommendation:** Do not import all 22 until Phase C source notes are tested on the 2 pilot persons. Phase D (relationships/events) can be deferred to post-22-import.

---

## 6. Next Actions

1. Review Phase B claims tables in Obsidian (or visually inspect markdown)
2. If approved → Phase C: create source notes for Tang Yin + Caesar non-D sources
3. If Phase C approved → Phase A+B+C for all 22 persons
4. Then Phase D (relationships, events, works)
5. Phase E (manual review in Obsidian)
