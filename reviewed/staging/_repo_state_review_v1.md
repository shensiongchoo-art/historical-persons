# Repo State Review v1
**Branch:** `hardening/mvp-current-prs-v1`
**Date:** 2026-05-12
**Reviewer:** Hardening Sprint Agent

---

## 1. Open PR Inventory

| PR # | Title / Branch | Status | Content |
|------|---------------|--------|---------|
| #1 | `collect/shen-zhou-v1` — 沈周 | Open | Full 11-file package |
| #2 | `collect/gnaeus-pompeius-magnus-v1` — Pompey | Open | **Partial**: claims.jsonl + open_questions.md only |
| #4 | `collect/wang-yangming-and-pompey-v1` — Wang Yangming + Pompey | Open | Two complete packages |
| #5 | `collect/qiu-ying-and-augustus-v2-5` — Qiu Ying + Augustus | Open | Two packages; originally v2.3 schema |
| #6 | `verification/source-reports-v1` | Open | Source verification reports (not person packages) |
| #7 | `collect/wu-kuan-and-mark-antony-v1` — Wu Kuan + Mark Antony | Open | Two new person packages (out of sprint scope) |

> Note: The prompts described PRs #1–#4 but the actual open PR count at inspection time is 7. PR #7 contains two persons (Wu Kuan / Mark Antony) not included in this sprint per scope rules.

---

## 2. Remote Branch Inventory

| Branch | Persons | Notes |
|--------|---------|-------|
| `collect/shen-zhou-v1` | 沈周 (Shen Zhou) | Canonical source for Shen Zhou |
| `collect/gnaeus-pompeius-magnus-v1` | Pompey (partial) | Not a full package; superseded by PR#4 for Pompey |
| `collect/qiu-ying-and-augustus-v1` | Qiu Ying + Augustus (v2.3) | Earlier draft; superseded by v2-5 branch |
| `collect/qiu-ying-and-augustus-v2-5` | Qiu Ying + Augustus (v2.5) | Canonical source for Qiu Ying + Augustus |
| `collect/wang-yangming-and-pompey-v1` | Wang Yangming + Pompey | Canonical source for Wang Yangming; complete Pompey package |
| `collect/wu-kuan-and-mark-antony-v1` | Wu Kuan + Mark Antony | Out of current sprint scope |
| `verification/source-reports-v1` | N/A | Source verification reports |

---

## 3. Canonical Package Decisions

| Person | Canonical Source Branch | Rationale |
|--------|------------------------|-----------|
| 沈周 (Shen Zhou) | `collect/shen-zhou-v1` (PR#1) | Only full package; no duplicate |
| 王阳明 (Wang Yangming) | `collect/wang-yangming-and-pompey-v1` (PR#4) | Full v2.5 package with split claims |
| Pompey (Gnaeus Pompeius Magnus) | `collect/wang-yangming-and-pompey-v1` (PR#4) | Only complete package; PR#2 is partial (2 files only) |
| 仇英 (Qiu Ying) | `collect/qiu-ying-and-augustus-v2-5` (PR#5) | v2.5 version used; v1 branch superseded |
| Augustus (Octavian) | `collect/qiu-ying-and-augustus-v2-5` (PR#5) | v2.5 version used; v1 branch superseded |

**Superseded / do not merge:**
- `collect/qiu-ying-and-augustus-v1` — superseded by v2-5 branch
- PR#2 (`collect/gnaeus-pompeius-magnus-v1`) — partial package only; Pompey canonical is PR#4

---

## 4. Person Package Inventory (hardening branch)

### `incoming/chinese/shen-zhou` — 沈周
- `person_id`: `P_CHN_MING_SHEN_ZHOU`
- Claims: 22 | Sources: 6 | Relationships: 13
- Validation: **PASSED**
- Schema: v2.5 native

### `incoming/chinese/wang-yangming` — 王阳明
- `person_id`: `P_CHN_MING_WANG_YANGMING`
- Claims: 37 | Sources: 15 | Relationships: 8
- Validation: **PASSED**
- Schema: v2.5 native; compound claims pre-split

### `incoming/western/gnaeus-pompeius-magnus` — Pompey
- `person_id`: `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS`
- Claims: 42 | Sources: 15 | Relationships: 12
- Validation: **PASSED**
- Schema: v2.5 (person_id standardized this sprint)

### `incoming/chinese/qiu-ying` — 仇英
- `person_id`: `P_CHN_MING_001_QIU_YING`
- Claims: 34 | Sources: 20 | Relationships: 12
- Validation: **PASSED**
- Schema: normalized from v2.3 to v2.5 this sprint

### `incoming/western/augustus-octavian` — Augustus
- `person_id`: `P_WEST_ROMAN_001_AUGUSTUS`
- Claims: 35 | Sources: 18 | Relationships: 9
- Validation: **PASSED**
- Schema: normalized from v2.3 to v2.5 this sprint

---

## 5. Data Quality Risks (cross-package)

### Source Level Risks

| Risk | Packages Affected |
|------|------------------|
| Several `A_candidate` sources lack passage/volume/edition refs | Wang Yangming, Shen Zhou, Qiu Ying, Pompey |
| SRC014 (Wang Yangming Japanese Yangmingism) is a placeholder `B` source | Wang Yangming |
| `D`-level sources present (general web) | Shen Zhou, Qiu Ying |
| Augustus ancient sources have some chapter refs; many still `needs_verification` | Augustus |

### Relationship Type Fixes Applied This Sprint

| Fix | Package |
|-----|---------|
| `political_ally` / `political_ally_then_opponent` → `same_political_context` | Pompey |
| `marriage` → `spouse` (3 rows) | Pompey |
| `influence` → `later_grouping_only` | Qiu Ying |
| `ally` → `same_political_context` or `documented_association` | Augustus |
| `philosophical_predecessor` → `reception_label` | Wang Yangming |
| `grandfather`/`uncle`/`father`/`friend` → v2.5 allowed types | Shen Zhou |

### Claim Status Fixes Applied This Sprint

| Fix | Package |
|-----|---------|
| `confirmed_misattribution` → `reception` (C028) | Pompey |
| Overstrong "friend/close friends/close relationship" wording removed | Shen Zhou |

### Pending Verification Items

- All classical source passage references in Pompey (Plutarch, Appian, Cassius Dio) are `needs_verification` — defer to source verification sprint
- Shen Zhou birth year discrepancy (Wikipedia 1427 vs 1472) unresolved
- 明清画史笔记 (无声诗史, 明画录, 图绘宝鉴续编) not represented as discrete sources in Qiu Ying
- Pompey Ny Carlsberg Glyptotek bust museum inventory number unverified
- Augustus passage references in Suetonius/Cassius Dio partially verified; remainder deferred

---

## 6. Out-of-Scope Items (not touched this sprint)

- PR#7 (`collect/wu-kuan-and-mark-antony-v1`): Wu Kuan and Mark Antony — new persons, outside current sprint scope
- `verification/source-reports-v1`: Source verification — separate track
- No visual/dashboard features built
- No PRs merged
- No master-level data touched
