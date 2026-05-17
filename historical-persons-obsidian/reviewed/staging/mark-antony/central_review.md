# Central Review: Mark Antony (Marcus Antonius)

**Reviewer:** MorphMind AI
**Date:** 2026-05-13
**Package:** `incoming/western/mark-antony/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_WEST_ROMAN_002_MARK_ANTONY` |
| **Name (EN)** | Marcus Antonius |
| **Name (ZH)** | 马库斯·安东尼乌斯 / 马克·安东尼 |
| **Birth** | 14 January 83 BCE (disputed — derived from Cicero Phil. 2.24) |
| **Death** | 1 August 30 BCE (suicide in Alexandria) |
| **Culture** | Roman / Late Republic |
| **Canonical Source** | PR#7 (`collect/wu-kuan-and-mark-antony-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized in PR#7 hardening pass) |

---

## 2. Source Inventory & Quality

| Source ID | Level | Author | Type | Verified? |
|-----------|-------|--------|------|-----------|
| SRC_MA_PLUTARCH_ANTONY | B_high | Plutarch | Life of Antony (c. 100–110 CE) | needs_verification — Loeb chapter refs pending |
| SRC_MA_APPIAN_CIVIL_WARS | B_high | Appian | Civil Wars Bk 2–5 (c. 150–160 CE) | needs_verification |
| SRC_MA_CASSIUS_DIO | B_high | Cassius Dio | Roman History Bk 41–51 (c. 210–230 CE) | needs_verification |
| SRC_MA_SUETONIUS_AUGUSTUS | B_high | Suetonius | Life of Augustus (c. 119–121 CE) | needs_verification |
| SRC_MA_CICERO_PHILIPPICS | A_candidate | Cicero | Philippics (44–43 BCE) | Contemporary primary source — correctly A_candidate |
| SRC_MA_CAESAR_CIVIL_WAR | A_candidate | Caesar | Civil War (c. 48–47 BCE) | Contemporary primary — correctly A_candidate |
| SRC_MA_RES_GESTAE | A_candidate | Augustus | Res Gestae (c. 14 CE) | Pro-Augustan first-person — correctly A_candidate |
| SRC_MA_EPIGRAPHIC | A_candidate | Crawford RRC | Roman Republican Coinage | RRC 489–545 for 43–30 BCE |
| SRC_MA_PELLING_1988 | B_high | C.B.R. Pelling | Cambridge commentary on Plutarch Antony | Modern scholarship |
| SRC_MA_GOLDSWORTHY_2010 | B_high | A. Goldsworthy | Antony and Cleopatra | Modern monograph |
| SRC_MA_SYME_1939 | B_high | R. Syme | The Roman Revolution | Foundational scholarship |

**Assessment:** 11 sources for 35 claims (0.31/claim). All sources at B_high or above — no C or D-level sources, a notable strength. Ancient sources correctly leveled: narrative sources (Plutarch, Appian, Dio, Suetonius) at B_high (secondary, with known bias), contemporary documents (Cicero, Caesar, Res Gestae) at A_candidate. Modern scholarship present but thin (only 4 works).

---

## 3. Claim Quality Review

| Category | Count | Assessment |
|----------|-------|-----------|
| Identity | 3 | Birth year disputed; derived from Cicero — appropriately probable/medium |
| Military (under Caesar) | 6 | Gallic campaigns, Pharsalus — well-sourced |
| Political (44 BCE) | 8 | Consulship, Lupercalia, funeral oration — detailed |
| Second Triumvirate | 7 | Formation, proscriptions, Philippi — well-sourced |
| Antony in the East | 6 | Cleopatra alliance, Parthian campaign, Donations of Alexandria |
| Actium & death | 4 | Naval battle, flight, suicide — well-documented |
| Reception | 1 | CLM_MA_035: posthumous reputation — correctly reception/high |

**Key strengths:**
- All 35 claims have source_ids — no empty source_ids (contrast with Wu Kuan).
- Both Chinese and English claim text present for every claim.
- Ancient bias noted in review_note fields (e.g., Plutarch's Augustan-influenced narrative).
- Cleopatra relationship not romanticized — correctly presented as political/military alliance.

**Minor issues:**
- CLM_MA_001 (birth date): `probable/medium` correct — the 83 BCE date is derived inferentially.
- Several confirmed/high claims rely on single ancient source (Plutarch only) — ideally need two-source confirmation.

---

## 4. Relationship Audit

All 13 relationships v2.5 compliant:

| Rel ID | Type | Related Person | Notes |
|--------|------|---------------|-------|
| REL_MA_001 | documented_association | Julius Caesar | Under Caesar in Gaul, Pharsalus, Magister Equitum |
| REL_MA_002 | opponent | Octavian/Augustus | Evolution: hostility→triumvir→enemy correctly captured |
| REL_MA_003 | spouse | Fulvia | First wife |
| REL_MA_004 | spouse | Octavia Minor | Political marriage to Octavian's sister |
| REL_MA_005 | spouse | Cleopatra VII | Political + personal alliance |
| REL_MA_006 | documented_association | Aulus Gabinius | Early military commander |
| REL_MA_007–013 | various | Various | Lepidus, Cicero, Brutus, etc. |

**Assessment:** Relationship types correctly calibrated. The Antony-Octavian evolution (ally→opponent) is particularly well-handled through evidence_note rather than ambiguous type labels. Spouse relationships correctly typed. All 13 have both evidence_note and relationship_summary.

---

## 5. Events Timeline

Well-structured. Key dates: 83 BCE (birth), 57–55 BCE (Gabinius campaign), 54–50 BCE (Gaul), 49 BCE (tribune, flight to Caesar), 48 BCE (Pharsalus), 44 BCE (consul, funeral oration), 43 BCE (Second Triumvirate, Lex Titia), 42 BCE (Philippi), 41 BCE (Perusine War), 37 BCE (Tarentum pact), 36 BCE (Parthian campaign), 34 BCE (Donations of Alexandria), 32 BCE (declaration of war), 31 BCE (Actium), 30 BCE (death).

---

## 6. Works & Visual Media

| Category | Count | Status |
|----------|-------|--------|
| Works | 4 | Military campaigns, political offices |
| Visual media | 4 | All staging — coin portraits, busts |

---

## 7. Compound Claim Check

Claims appear pre-split. No detected compound claims in validated state. CLM_MA_035 (reception_label) correctly isolated as separate claim.

---

## 8. Schema & JSON Validity

| Check | Result |
|-------|--------|
| JSON/JSONL parse | PASS |
| `person_id` consistent | PASS |
| All required files | PASS (11/11) |
| `source_ids` resolve to sources.jsonl | PASS |
| v2.5 schema compliance | PASS |
| Relationships: relationship_id + person_id + related_person_name | PASS |
| Sources: reliability_level + citation_detail | PASS |

---

## 9. Source Level Calibration

| Issue | Status |
|-------|--------|
| Plutarch/Appian/Dio at B_high | Correct — secondary narratives with known bias |
| Cicero/Caesar/Res Gestae at A_candidate | Correct — primary but biased |
| No D or C sources | **Strength** — cleanest source list among all packages |
| Modern scholarship only 4 works | Thin but adequate (Pelling is the expert commentary) |

---

## 10. Confidence Calibration

| Status | Count | Notes |
|--------|-------|-------|
| confirmed/high | ~28 | Military and political events well-documented by multiple sources |
| probable/medium | ~5 | Interpretive and inferential claims |
| reception/high | 1 | CLM_MA_035 posthumous reputation |

**Assessment:** Slightly heavy on confirmed/high for claims dependent on single ancient sources with known bias. Consider downgrading some Plutarch-only claims to probable/medium. The bias annotation in review_note is present but could be more consistently applied.

---

## 11. Cross-Package Dependencies

| Related Person | Relationship | Package Status |
|----------------|-------------|----------------|
| Julius Caesar | documented_association | Not yet collected |
| Octavian/Augustus | opponent | Collected (incoming) |
| Cleopatra VII | spouse | Not yet collected |
| Cicero | opponent | Not yet collected |
| Lepidus | same_political_context | Not yet collected |
| Fulvia | spouse | Not yet collected |
| Octavia Minor | spouse | Not yet collected |

**Key gap:** Cleopatra VII not yet collected — one of the most important relationships in the package is one-sided. Antony's narrative depends heavily on Cleopatra; her absence makes verification asymmetric.

---

## 12. Visual Media Audit

4 entries, all staging. Coin portraits (RRC 489–545 range) and busts (Vatican, etc.). RRC numbers partially present but not consistently linked to specific visual media entries. Before promotion: verify museum IDs, provide full RRC references, confirm CC/public domain.

---

## 13. Recommended Action

**Action:** `merge_after_loeb_verification`

**Required before merge:**
1. Add Loeb chapter/passage references for Plutarch Antony, Appian BC, Cassius Dio — all currently `needs_verification`
2. Cross-reference Antony's age at death (53 vs 56 per Plutarch) against Cicero Phil. 2.24
3. Re-calibrate confidence for claims relying on single ancient source with known bias (downgrade some confirmed→probable)

**Recommended (not blocking):**
- Collect Cleopatra VII for cross-validation (highest priority cross-package dependency)
- Add 1–2 more modern scholarly sources to reduce dependence on ancient narratives
- Link RRC numbers to specific visual media entries

**Notes:** Mark Antony is a well-structured package with clean source discipline (no C/D sources). The primary gap is passage-level verification of ancient sources — all Loeb refs are needs_verification. Once those are provided, this package is merge-ready. The Cleopatra VII dependency is the main cross-package concern — Antony cannot be fully validated until she is collected.
