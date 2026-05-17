# Central Review: Gnaeus Pompeius Magnus (Pompey the Great)

**Reviewer:** MorphMind AI
**Date:** 2026-05-13
**Package:** `incoming/western/gnaeus-pompeius-magnus/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` |
| **Name (EN)** | Gnaeus Pompeius Magnus |
| **Name (ZH)** | 格奈乌斯·庞培·马格努斯 |
| **Birth** | 29 September 106 BCE |
| **Death** | 28 September 48 BCE |
| **Culture** | Roman / Late Republic |
| **Canonical Source** | PR#4 (`collect/wang-yangming-and-pompey-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (person_id standardized in hardening sprint) |

---

## 2. Source Inventory & Quality

| Source ID | Level | Author | Type | Verified? |
|-----------|-------|--------|------|-----------|
| SRC_POMPEY_PLUTARCH | A_candidate | Plutarch | Life of Pompey | Ch. 1,14,25–28,30–45,46–47,68–80 verified |
| SRC_POMPEY_APPIAN | A_candidate | Appian | Civil Wars | Book 1.80, 2.9, 3.82–99, 3.103–104 checked |
| SRC_POMPEY_CASSIUS_DIO | A_candidate | Cassius Dio | Roman History | Books 36–37, 42 checked |
| SRC_POMPEY_CAESAR | A_candidate | Caesar | Civil War | Book 3.82–99 checked |
| SRC_POMPEY_CICERO_MANILIA | A_candidate | Cicero | Pro Lege Manilia | Sections 27–35 needs_verification |
| SRC_POMPEY_CICERO letters | A_candidate | Cicero | Letters | Partially checked |
| SRC_POMPEY_PLINY | A_candidate | Pliny | Natural History | 37.13 (birth date) confirmed |
| SRC_POMPEY_FLORUS | A_candidate | Florus | Epitome | **2.13 does NOT match claimed superlative** |
| SRC_POMPEY_VALERIUS | A_candidate | Valerius Maximus | — | 6.2.8 (adulescentulus carnifex) needs_verification |
| SRC_POMPEY_CRASSUS | A_candidate | Plutarch | Life of Crassus | Ch. 14 needs_verification |
| 5 modern | B_high | Various | Academic works | — |

**Assessment:** 15 sources for 42 claims (0.36/claim). Strong ancient source coverage. Source verification sprint provided extensive Loeb references but several remain `needs_verification`. Florus discrepancy is significant — a claimed superlative not found in the actual text.

---

## 3. Claim Quality Review

| Category | Count | Assessment |
|----------|-------|-----------|
| Identity/family | 5 | Birth date from Pliny NH 37.13 confirmed |
| Early career | 6 | "Three legions" claim (Plutarch says "a legion") — discrepancy |
| Military campaigns | 14 | Sertorian War, Spartacus, pirates, Mithridates — well-sourced |
| First Triumvirate | 4 | Formation, Julia marriage solid |
| Civil War | 7 | Pharsalus well-documented |
| Death | 3 | Egypt assassination confirmed |
| Reception | 3 | "Magnus" cognomen, later assessments |

**Key issues:**
- C028: correctly changed from `confirmed_misattribution` → `reception` in hardening sprint.
- "Three legions" number: Plutarch's account has "a legion" — need cross-reference with Appian/Cassius Dio.
- Florus-dependent superlative claim: downgrade or remove.

---

## 4. Relationship Audit

All 12 relationships remapped to v2.5 types in hardening sprint:
- `political_ally` → `same_political_context` (Caesar, Crassus)
- `political_ally_then_opponent` → `same_political_context` + `opponent` (Caesar)
- `marriage` × 3 → `spouse` (Julia, Mucia, Cornelia)
- Family relationships correct

**Assessment:** All types v2.5 compliant. Relationship evolution (ally→opponent for Caesar) correctly represented.

---

## 5. Events Timeline

Extensive timeline with 42 events. Key dates: 106 BCE (birth), 83 BCE (raised legion), 81 BCE (first triumph), 71 BCE (second triumph), 67 BCE (Lex Gabinia), 66 BCE (Lex Manilia), 61 BCE (third triumph), 60 BCE (First Triumvirate), 59 BCE (marriage to Julia), 48 BCE (Pharsalus and death). Well-structured.

---

## 6. Works & Visual Media

| Category | Count | Status |
|----------|-------|--------|
| Works | 2 | Theatre of Pompey, coinage |
| Visual media | 5 | All staging — Ny Carlsberg Glyptotek bust, coin portraits |

---

## 7. Compound Claim Check

Compound claims pre-split: Julia's death, Luca renewal, Crassus death, Pharsalus. All properly split with a/b/c suffixes.

---

## 8. Schema & JSON Validity

| Check | Result |
|-------|--------|
| JSON/JSONL parse | PASS |
| `person_id` consistent | PASS (88 occurrences standardized from P_WEST_ROMAN_REPUBLIC_...) |
| All required files | PASS (11/11) |
| `source_ids` resolve | PASS |
| No confirmed/high on C-only | PASS |

---

## 9. Source Level Calibration

| Issue | Status |
|-------|--------|
| Florus 2.13 mismatch | **BLOCKING** — claim does not match source |
| "Adulescentulus carnifex" unverified | Needs cross-reference with Collins 1953/Leach 1978 |
| "Three legions" vs "a legion" | Needs resolution |
| Cicero Pro Lege Manilia sections | Needs exact section verification |
| 4 C-level sources | Reduce or promote to academic sources |

---

## 10. Confidence Calibration

| Status | Count | Notes |
|--------|-------|-------|
| confirmed/high | ~25 | Military and political milestones well-sourced |
| probable/medium | ~10 | Interpretive claims, exact numbers |
| reception | ~5 | "Magnus" adoption, later historiographical assessments |
| disputed | 2 | Appropriate for contested claims |

---

## 11. Cross-Package Dependencies

| Related Person | Relationship | Package Status |
|----------------|-------------|----------------|
| Julius Caesar | opponent / same_political_context | Not yet collected |
| Crassus | same_political_context | Not yet collected |
| Sulla | documented_association | Not yet collected |
| Julia (daughter) | family | Not yet collected |
| Cornelia Metella | spouse | Not yet collected |

---

## 12. Visual Media Audit

5 entries, all staging. Ny Carlsberg Glyptotek bust inventory number unverified. RRC coinage catalogue numbers not provided. Before promotion: verify museum IDs, provide RRC numbers, confirm public domain.

---

## 13. Recommended Action

**Action:** `merge_after_verification_fixes`

**Required before merge:**
1. Fix Florus 2.13 claim — remove or downgrade the unsupported superlative
2. Resolve "three legions" vs "a legion" discrepancy across Plutarch/Appian/Dio
3. Verify "adulescentulus carnifex" against Valerius Maximus 6.2.8 with critical edition
4. Verify Cicero Pro Lege Manilia section numbers against Loeb

**Recommended (not blocking):**
- Add RRC catalogue numbers for coinage
- Verify Ny Carlsberg Glyptotek bust inventory number
- Reduce C-level sources by promoting to academic citations
- Collect Julius Caesar, Crassus for cross-validation

**Notes:** Pompey is the most extensive package (42 claims). Source verification is well under way but two source-text mismatches (Florus, "three legions") need resolution before merge. Otherwise ready.
