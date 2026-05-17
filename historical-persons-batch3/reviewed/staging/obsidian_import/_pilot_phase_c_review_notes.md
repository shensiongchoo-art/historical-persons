# Pilot Phase C Review Notes

**Date:** 2026-05-16
**Branch:** `pilot/obsidian-phase-a-tang-yin-caesar-v1` (continuing on PR #33)
**Scope:** Source notes created + claims linked via Obsidian wikilinks

---

## 1. Source Notes Created

### Tang Yin (7 notes)

| Source ID | Type | Reliability | Claims Linked |
|-----------|------|-------------|---------------|
| [[SRC_TY_001]] | official_history (明史·文苑传) | A_candidate | 8 claims |
| [[SRC_TY_002]] | collected_works (六如居士集) | A_candidate | 4 claims |
| [[SRC_TY_003]] | academic_monograph (唐寅研究) | B_high | 1 claim |
| [[SRC_TY_004]] | museum_record (故宫藏品) | A_candidate | 2 claims |
| [[SRC_TY_007]] | academic_paper (生平与艺术) | B_high | 7 claims |
| [[SRC_TY_008]] | local_gazetteer (姑苏志) | A_candidate | 0 claims (collected but unused) |
| [[SRC_TY_009]] | academic_paper (研究述评) | B_high | 2 claims |

### Julius Caesar (7 notes)

| Source ID | Type | Reliability | Claims Linked |
|-----------|------|-------------|---------------|
| [[SRC_JC_001]] | primary_text (Commentarii de Bello Gallico) | A_candidate | 2 claims |
| [[SRC_JC_002]] | primary_text (Commentarii de Bello Civili) | A_candidate | 3 claims |
| [[SRC_JC_003]] | ancient_biography (Plutarch) | B_high | 9 claims |
| [[SRC_JC_004]] | ancient_biography (Suetonius) | B_high | 9 claims |
| [[SRC_JC_005]] | ancient_history (Cassius Dio) | B_high | 5 claims |
| [[SRC_JC_006]] | ancient_text (Cicero Letters) | A_candidate | 1 claim |
| [[SRC_JC_007]] | academic_monograph (Goldsworthy) | B_high | 5 claims |

**Total: 14 source notes created** (7 Chinese + 7 Western)

---

## 2. D-Sources Not Created

Per policy, D/clue_only sources are not given standalone notes:

| Source | Person | Type |
|--------|--------|------|
| SRC_TY_005 | Tang Yin | Baidu Baike (D) — clue only |
| SRC_TY_006 | Tang Yin | Wikipedia (D) — clue only |
| SRC_JC_008 | Julius Caesar | Wikipedia (D) — clue only |
| SRC_JC_009 | Julius Caesar | Britannica (D) — clue only |

These appear in sources.jsonl but are not used as primary support for any claim.

---

## 3. Person Notes Updated

Both person notes retain:
- YAML frontmatter (unchanged, valid)
- AI-COLLECTED / staging banner
- Summary, Identity, Timeline, Fact/Legend Separation sections

Claims tables updated:
- Tang Yin: all 24 source references converted to [[wikilinks]]
- Julius Caesar: all 34 source references converted to [[wikilinks]]

---

## 4. Readability Assessment

### Source links are clear
- `[[SRC_TY_001]]` is concise — no invented titles cluttering the claims table
- Obsidian auto-completes link preview on hover
- Multiple sources per claim are comma-separated: `[[SRC_JC_003]], [[SRC_JC_004]], [[SRC_JC_005]]`

### Source notes are self-contained
- Each source note has YAML frontmatter with used_for_claim_ids
- Claim wikilinks in "Used For Claims" section enable bidirectional navigation
- Review Warning banner on every source note

### Minor concern
- SRC_TY_007 is heavily cited (7 claims) but marked `needs_verification` — reviewer should prioritize this source
- SRC_TY_008 is in sources.jsonl but unused — represents a gap that could strengthen Tang Yin's Suzhou context

---

## 5. Missing Source IDs

No missing source IDs. Every source cited in claims tables has a corresponding source note:

| Check | Result |
|-------|--------|
| Tang Yin claims → source notes | 6/6 non-D sources linked (SRC_TY_001,002,003,004,007,009) |
| Julius Caesar claims → source notes | 7/7 non-D sources linked (SRC_JC_001–007) |
| D sources in claims tables | None — all D sources unused as primary support |

---

## 6. Phase D Recommendation

**Proceed, but with low scope for the pilot.**

Phase D would:
1. Add relationship tables to person notes from relationships.jsonl
2. Create event notes from events.jsonl
3. Create work notes from works.jsonl

**Recommendation for pilot:** Phase D is lower priority than scaling Phase A+B+C to all 22 persons. The 2-person pilot has proven the format works. Phase D relationships add value but are not blocking for import scaling.

---

## 7. Full 22-Person Import Readiness

| Criterion | Status |
|-----------|--------|
| Phase A (person notes) | ✓ Proven with 2 persons |
| Phase B (claims tables) | ✓ Proven — 36 claims across 2 persons |
| Phase C (source notes) | ✓ Proven — 14 source notes, 58 cross-links |
| Phase D (relationships/events) | ✗ Not yet — lower priority |
| Schema consistency | ⚠ Chinese Batch 2 uses simpler schema; normalization recommended |
| All 22 validated | ✓ |

**Recommendation:** Import Phases A+B+C for all 22 persons. Defer Phase D until all persons are in the vault. Schema normalization can be a post-import hardening pass.
