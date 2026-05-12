# Open PR Triage After Hardening v1
**Branch:** `maintenance/pr-triage-after-hardening-v1`
**Date:** 2026-05-12
**Reviewer:** Triage Agent

---

## 1. Current Open PR Inventory

| PR # | Title | Branch | Status | Superseded? | Recommended Action |
|------|-------|--------|--------|-------------|-------------------|
| #1 | Shen Zhou (沈周) v1 | `collect/shen-zhou-v1` | Open | No | Keep; merge after central review |
| #4 | Wang Yangming + Pompey | `collect/wang-yangming-and-pompey-v1` | Open | No | Keep; merge after central review |
| #5 | Qiu Ying + Augustus v2.5 | `collect/qiu-ying-and-augustus-v2-5` | Open | No | Keep; merge after central review |
| #6 | Source verification reports | `verification/source-reports-v1` | Open | No | Merge; reports-only, no package changes |
| #7 | Wu Kuan + Mark Antony | `collect/wu-kuan-and-mark-antony-v1` | Open | No | Defer; needs v2.5 hardening before review |

## 2. Superseded PRs (Already Closed)

| PR # | Title | Status | Reason |
|------|-------|--------|--------|
| #2 | Pompey (partial) | **CLOSED** | Only 2 files (claims.jsonl, open_questions.md). Superseded by PR #4 complete Pompey package. |
| #3 | Qiu Ying + Augustus v1 | **CLOSED** | Generated under v2.3 rules. Superseded by PR #5 v2.5 packages. |

> No action needed — PR #2 and #3 were already closed before this triage.

## 3. PR #6 — Source Verification Reports

**Status:** Reports-only. Clean.

Files changed (4):
- `reviewed/staging/source_verification/pompey_source_verification.md`
- `reviewed/staging/source_verification/wang-yangming_source_verification.md`
- `reviewed/staging/source_verification/qiu-ying_source_verification.md`
- `reviewed/staging/source_verification/augustus_source_verification.md`

**No `incoming/` package files touched.** Zero package data changes.

**Recommended action:** `merge_after_central_reviewer_approval`. Safe to merge — verifies existing packages without modifying them. Does not invent page numbers or editions. Marks unverified items as `needs_verification`.

## 4. PR #7 — Wu Kuan + Mark Antony Initial Review

### Wu Kuan (吴宽) — `P_CHN_MING_002_WU_KUAN`

| Criterion | Finding | Severity |
|-----------|---------|----------|
| Schema version | **v2.3** — uses `category` not `claim_type`, `text_zh/text_en` not `claim_text_zh/claim_text_en`, no `person_id` on claims | **CRITICAL** |
| Source schema | `level` not `reliability_level`, `bibliographic_hint` not `citation_detail`, no `author` field | **CRITICAL** |
| Relationship schema | `rel_id`, `person_a/person_b`, `description_zh/en` — v2.3 format | **CRITICAL** |
| Source discipline | Baidu Baike (SRC_WK_005, C-level) used for 13 of 18 claims | **HIGH** |
| Overstrong wording | "close friends" with Shen Zhou (CLM_WK_012, REL_WK_001) | **MEDIUM** |
| Source count | 7 sources (4 A, 1 B_high, 1 C, 1 A-dubious) — thin | **MEDIUM** |
| Claims | 18 claims, well-split, no compound claims detected | OK |
| Validation | PASSED (under v2.3 rules) | OK |

### Mark Antony — `P_WEST_ROMAN_002_MARK_ANTONY`

| Criterion | Finding | Severity |
|-----------|---------|----------|
| Schema version | Mixed v2.5-ish — has `person_id`, `claim_text`, `category` (not `claim_type`), uses `status_note` | **HIGH** |
| Source schema | `level` not `reliability_level`, `type` not `source_type`, no `citation_detail` | **HIGH** |
| Source discipline | All 7 ancient sources at A with bias caveats — excellent | GOOD |
| Relationship types | `commander_and_subordinate`, `political_opponent`, `political_ally_then_rival`, `marriage`, `romantic_partner_and_political_ally`, `military_opponent`, `stepchild_and_political_ally` — **not in v2.5 allowed set** | **CRITICAL** |
| Compound claims | None detected — 35 claims, well-split | GOOD |
| Augustus propaganda | Correctly flagged (CLM_MA_035: reception) | GOOD |
| Claims | 35 claims, detailed `status_note`, good source cross-referencing | GOOD |
| Validation | PASSED | OK |

### PR #7 Overall Assessment

**Not ready for merge.** Both packages need v2.5 hardening before central review.

1. Wu Kuan: Full v2.3→v2.5 normalization required (claims, sources, relationships)
2. Wu Kuan: Baidu Baike overuse — need Ming History or other academic sources
3. Mark Antony: Schema normalization (claims, sources fields)
4. Mark Antony: Relationship type remapping to v2.5 allowed set
5. Both: `person_id` naming consistency check

---

## 5. Package Status Summary

### Ready for Central Review (post-hardening)
| Person | PR | Status After Hardening |
|--------|-----|----------------------|
| 沈周 Shen Zhou | #1 | Staging-quality, PASSED |
| 王阳明 Wang Yangming | #4 | Staging-quality, PASSED (SRC001/008/009/010 verified v3) |
| Pompey | #4 | Staging-quality, PASSED |
| 仇英 Qiu Ying | #5 | Staging-quality, PASSED |
| Augustus | #5 | Staging-quality, PASSED |

### Needs Work Before Review
| Person | PR | Key Issues |
|--------|-----|------------|
| 吴宽 Wu Kuan | #7 | v2.3 schema, source discipline |
| Mark Antony | #7 | Schema norms, relationship types |

### Reports-Only (Ready)
| Item | PR | Status |
|------|-----|--------|
| Source verification reports | #6 | Clean, reports-only |
| PR triage report | This file | Current branch |
| PR #7 initial review | `_pr7_wu-kuan_mark-antony_initial_review.md` | Current branch |

---
