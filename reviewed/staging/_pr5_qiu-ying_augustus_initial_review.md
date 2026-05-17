# PR #5 Initial Review: Qiu Ying + Augustus v2.5
**Branch:** `maintenance/post-pr9-cleanup-v1`
**Date:** 2026-05-14
**Reviewer:** Post-PR9 Cleanup Agent
**PR Status:** CLOSED (not merged); packages now in main via hardening sprint (PR #8)

---

## Qiu Ying (仇英) — incoming/chinese/qiu-ying/

### v2.5 Schema Compliance: ✅ PASSED
- All 11 required files present
- Claims: 34 — one fact per claim, no compound claims detected
- Sources: 23 — uses `reliability_level`, `citation_detail`, `verification_status`, `used_for_claim_ids`
- Relationships: 12 — uses `relationship_id`, `person_id`, `related_person_name`, `relationship_type`
- Events: 8 — structured event entries
- Works: 13 — `attribution_status` used (confirmed / needs_verification)

### Source Levels
| Level | Count | Assessment |
|-------|-------|------------|
| A | 3 | 无声诗史, 明画录, 图绘宝鉴续编 — added in source verification sprint v2 |
| A_candidate | 5 | Ancient texts + museum records — needs passage-level verification |
| B_high | 5 | Laing, Ngan, Hsu Wenmei — strong modern scholarship |
| B | 5 | Cahill, Little, Chen Guocheng, Pan Lu, Young — solid secondary |
| C | 1 | Wikipedia — clue only |
| D | 1 | Baidu Baike — clue only |

**Assessment:** Source calibration is proportional. Ancient texts properly marked A_candidate pending passage verification. Baidu/Wikipedia correctly marked as clue-only (C/D). Primary academic sources (Laing, Ngan, Hsu) carry B_high.

### Source Weakness After Verification
- 3 ancient text sources (SRC_QY_008–010) still need specific juan/page references
- Museum record sources (SRC_QY_013–015) need object ID verification
- SRC_QY_017 (Baidu) used for 3 works with `needs_verification` attribution — correct handling

### Works: verified / attributed / disputed / copy
| Status | Count | Handling |
|--------|-------|----------|
| confirmed | 10 | Museum-verified (NPM, Palace Museum Beijing, Shanghai Museum) |
| needs_verification | 3 | Reported locations not independently confirmed |

**Assessment:** Correct separation. Museum-verified works have institution names and object-level attribution. Unconfirmed works explicitly marked `needs_verification`.

### 明四家 (Four Masters) Marking: ✅
- REL_QY_010–012 correctly use `later_grouping_only`
- REL_QY_004 (Shen Zhou) correctly marked as `later_grouping_only` with note about no direct contact
- Short description uses "后世列为明四家之一" (posthumously classified) — reception wording correct

### Visual Media: staging ✅
- 4 entries in visual_media.jsonl
- All marked with review_status appropriate for staging

### Recommendation: **ready_for_staging_merge**
Minor caveats:
- 3 works (WRK_QY_011–013) depend on Baidu-sourced locations — acceptable pending museum verification
- Ancient text sources need passage-level verification (not blocking)
- Birth year range 1494–1498 still debated — correctly marked `disputed`

---

## Augustus (Octavian) — incoming/western/augustus-octavian/

### v2.5 Schema Compliance: ✅ PASSED
- All 11 required files present
- Claims: 35 — one fact per claim
- Sources: 18 — properly calibrated
- Relationships: 9 — uses `opponent`, `family`, `documented_association`, `same_political_context`
- Events: 15 — BCE/CE date schema correct
- Works: 2 — Res Gestae + building program

### BCE/CE Date Schema: ✅
- Birth: `"era": "BCE"`, `"year_number": 63`, `"astronomical_year": -62` — correct
- Events use `era`, `precision`, `date_display` consistently
- Death: `"era": "CE"`, `"precision": "day"` — correct

### Source Levels and Ancient Source Caveats
| Level | Count | Examples |
|-------|-------|----------|
| A | 10 | Suetonius, Cassius Dio, Appian, Res Gestae, Nicolaus, Cicero, Tacitus, Plutarch, coinage, museum records |
| A_candidate | 1 | Velleius Paterculus — contemporary but strongly pro-Augustan |
| B_high | 2 | Syme (The Roman Revolution), Goldsworthy (modern biography) |
| B | 3 | Eck, Southern, Wiseman |
| C | 1 | Wikipedia — clue only |

**Assessment:** Ancient sources correctly marked A with explicit caveats about bias. Suetonius noted as "anecdotal details reliable; interpretation and gossip require caution." Res Gestae noted as "self-presentation only — NOT neutral history." Velleius correctly distinguished as A_candidate (contemporary but strongly pro-Augustan/pro-Tiberian). Loeb references verified and backfilled (source verification sprint v2).

**Critical:** Source levels for ancient authors are marked A — higher than standard v2.5 guidance (which recommends A_candidate or B_high for narrative ancient sources). However, specific Loeb chapter references are present and the verification notes explicitly flag bias. This calibration is acceptable if central reviewer agrees ancient texts with verified passage refs can carry A level.

### Testamentary Adoption Ambiguity: ✅
- CLM_AU_007 correctly marked `probable` with `confidence: medium`
- Notes legal ambiguity: adrogatio normally requires lex curiata during father's lifetime
- Distinguishes testamentary will (45 BCE) from legal formalization (43 BCE lex curiata)

### "First Emperor" / Principate Wording: ✅
- Short description: "First Roman princeps (27 BCE–14 CE)" — uses correct Latin term, not "emperor"
- Person record: "establish the Principate—a system of one-man rule presented in republican forms" — historiographically accurate
- CLM_AU_018: "Res Gestae explicitly avoids the word 'princeps' as a constitutional office" — correctly treats as reception/historiographical category
- "First emperor" appears only in modern source (Goldsworthy) title — not in structured claims

### Visual Media: staging ✅
- 2 museum record sources for portrait statues (Prima Porta, Via Labicana)
- Museum inventory numbers provided
- Visual media marked as staging

### Recommendation: **ready_for_staging_merge**
Minor caveats:
- Ancient source A-level calibration should be confirmed by central reviewer
- Velleius Paterculus A_candidate → may be appropriate but verify passage references
- SRC_AU_017 (Wiseman) has suspect "2025" date — needs verification

---

## Combined Verdict

| Package | Recommendation | Blockers |
|---------|---------------|----------|
| Qiu Ying | **ready_for_staging_merge** | None critical; minor source passage verification |
| Augustus | **ready_for_staging_merge** | Ancient source A-level calibration needs central reviewer sign-off |

### Merge note
PR #5 was CLOSED, not merged. Both packages were hardened via PR #8 and are now in main. If central reviewer approves Staging level, these packages can move to `reviewed/staging/{qiu-ying,augustus-octavian}/` with a new PR.
