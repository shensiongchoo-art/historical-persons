# Step 1.2A — Staging Consolidation Summary

**Branch:** `step1.2a/staging-consolidation-v1`
**Date:** 2026-05-14
**Sprint:** GitHub Staging Consolidation
**Reviewer:** MorphMind AI

---

## 1. Branch Name

`step1.2a/staging-consolidation-v1`

---

## 2. Persons Inventoried

| # | Person | Folder | Person ID | Claims | Sources | Validation |
|---|--------|--------|-----------|--------|---------|------------|
| 1 | 沈周 (Shen Zhou) | `incoming/chinese/shen-zhou/` | `P_CHN_MING_SHEN_ZHOU` | 22 | 6 | PASSED |
| 2 | 王阳明 (Wang Yangming) | `incoming/chinese/wang-yangming/` | `P_CHN_MING_WANG_YANGMING` | 37 | 18 | PASSED |
| 3 | 仇英 (Qiu Ying) | `incoming/chinese/qiu-ying/` | `P_CHN_MING_001_QIU_YING` | 34 | 23 | PASSED |
| 4 | 吴宽 (Wu Kuan) | `incoming/chinese/wu-kuan/` | `P_CHN_MING_WU_KUAN` | 22 | 7 | PASSED |
| 5 | Pompey | `incoming/western/gnaeus-pompeius-magnus/` | `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` | 42 | 17 | PASSED |
| 6 | Augustus | `incoming/western/augustus-octavian/` | `P_WEST_ROMAN_001_AUGUSTUS` | 35 | 18 | PASSED |
| 7 | Mark Antony | `incoming/western/mark-antony/` | `P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS` | 35 | 11 | PASSED |

All 7 packages: 11/11 required files present, all v2.5 schema, all pass validation.

---

## 3. Central Review Files Created

| File | Person |
|------|--------|
| `reviewed/staging/shen-zhou/central_review.md` | 沈周 (Shen Zhou) |
| `reviewed/staging/wang-yangming/central_review.md` | 王阳明 (Wang Yangming) |
| `reviewed/staging/qiu-ying/central_review.md` | 仇英 (Qiu Ying) |
| `reviewed/staging/wu-kuan/central_review.md` | 吴宽 (Wu Kuan) |
| `reviewed/staging/gnaeus-pompeius-magnus/central_review.md` | Pompey |
| `reviewed/staging/augustus-octavian/central_review.md` | Augustus |
| `reviewed/staging/mark-antony/central_review.md` | Mark Antony |

Plus: `reviewed/staging/_current_mvp_inventory.md` (cross-package inventory with metrics table and triage).

---

## 4. Validation Results

| Person | Result |
|--------|--------|
| 沈周 (Shen Zhou) | PASSED |
| 王阳明 (Wang Yangming) | PASSED |
| 仇英 (Qiu Ying) | PASSED |
| 吴宽 (Wu Kuan) | PASSED |
| Pompey | PASSED |
| Augustus | PASSED |
| Mark Antony | PASSED |

**All 7 packages pass `tools/validate_package.py`. Zero failures.**

---

## 5. Packages Suitable for Later Obsidian Demo

### Recommended Primary Demo (2 Chinese + 2 Western)

| Position | Person | Rationale |
|----------|--------|-----------|
| Chinese #1 | **王阳明 (Wang Yangming)** | Rich philosophy + career narrative; 37 claims; pre-split compounds; both zh/en |
| Chinese #2 | **仇英 (Qiu Ying)** | Best-sourced Chinese package (0.68 sources/claim); 13 works with museum locations |
| Western #1 | **Augustus** | Strongest source base (0.51 sources/claim); verified Loeb refs; name stages coverage |
| Western #2 | **Pompey** | Most extensive (42 claims); Loeb refs verified for major sources; rich relationships |

### Secondary (include if demo expands to 6+ persons)
- **Mark Antony** — Clean source base, best relationships (13), needs Loeb refs
- **沈周 (Shen Zhou)** — Structure good, but 6 sources too thin for prominent demo

### Not Recommended for Initial Demo
- **吴宽 (Wu Kuan)** — Thin source base (7 sources), empty source_ids, minimal relationships

---

## 6. Packages Needing Further Source Verification

| Package | Primary Gap | Priority |
|---------|-------------|----------|
| Mark Antony | No Loeb chapter refs for any ancient source | High |
| 沈周 (Shen Zhou) | 明史·隐逸传 not a discrete source; birth year discrepancy | High |
| 吴宽 (Wu Kuan) | Empty source_ids on several claims; no B-level monographs | Critical |
| 王阳明 (Wang Yangming) | SRC014 Japan pages still needs_verification | Medium |
| 仇英 (Qiu Ying) | Museum object IDs and Ming text passages needs_verification | Medium |
| Pompey | Valerius Maximus, Florus, legion count discrepancies | Medium |
| Augustus | Velleius/Nicolaus passages, RIC numbers | Low |

---

## 7. Packages Needing Relationship Cleanup

| Package | Issue | Priority |
|---------|-------|----------|
| 吴宽 (Wu Kuan) | Only 4 relationships — critically thin | High |
| 王阳明 (Wang Yangming) | Only 8 relationships for major figure with many disciples | Medium |
| Mark Antony | Cleopatra VII package not yet collected — one-sided | Medium |

---

## 8. Project Ready for Small Obsidian Demo?

**YES — with caveats.** The project has 7 validated, v2.5-compliant person packages with consistent person_ids and pre-split compound claims. All packages have both English and Chinese claim text. Source verification is partial but sufficient for a demo that is honest about status.

**Recommended approach:**
1. Select 2 Chinese + 2 Western persons from the recommended primary demo list
2. Build a small Obsidian vault with just those 4 persons
3. Display claim statuses (confirmed/probable/reception/needs_verification) transparently
4. Include source cards showing verification status
5. Mark all packages as `ai_collected_unreviewed` — do not present as master-quality
6. The demo shows the architecture and data model, not pretend-completeness

---

## 9. Recommended Next Step

**Step 1.2B — Small Obsidian Demo Build**

1. Select: Wang Yangming + Qiu Ying + Augustus + Pompey
2. Build minimal Obsidian vault from these 4 packages only
3. Create person pages, claim notes, source notes, relationship graphs
4. Tag all items with review_status and verification_status
5. Do NOT import all 7 persons — keep demo small and clean
6. Do NOT build SQLite/database import yet
7. Do NOT collect new people
8. Do NOT change project rules

**Before Obsidian build, consider:**
- Completing Mark Antony source verification sprint (Loeb refs)
- Resolving Wu Kuan empty source_ids
- This would make a 6-person demo feasible, but 4-person is sufficient to validate the architecture
