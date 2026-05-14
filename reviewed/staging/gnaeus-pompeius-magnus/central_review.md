# Central Review: Gnaeus Pompeius Magnus (Pompey the Great)

**Reviewer:** MorphMind AI
**Date:** 2026-05-14
**Package:** `incoming/western/gnaeus-pompeius-magnus/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` |
| **Name (EN)** | Gnaeus Pompeius Magnus |
| **Name (ZH)** | 格奈乌斯·庞培乌斯·马格努斯 / 庞培 |
| **Birth** | 106 BCE (29 September, per Pliny NH 37.13) |
| **Death** | 48 BCE (assassinated in Egypt) |
| **Culture** | Roman / Late Republic |
| **Canonical Source** | PR#4 (`collect/wang-yangming-and-pompey-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized in hardening sprint) |

---

## 2. Current Package Status

Package is complete (11/11 required files) and passes validation. person_id standardized across all files (88 occurrences) in hardening sprint. Relationship types correctly remapped (political_ally → same_political_context; marriage → spouse). Claim C028 (misattribution) → reception. Source verification sprint provided Loeb references for Plutarch Pompey (chapters 1, 14, 25-28, 30-45, 46-47, 68-80), Appian BC (1.80, 3.82-104), Cassius Dio (Books 36-37, 42), and Pliny NH 37.13.

---

## 3. Overall Central Review Verdict

**STAGING ONLY — NOT READY FOR MASTER PROMOTION.** Most extensive Western package (42 claims) with good classical source coverage. Source verification sprint significantly advanced the source base with verified Loeb chapter references. Remaining blockers: Cicero Pro Lege Manilia sections approximate, Valerius Maximus and Velleius Paterculus passages `needs_verification`, Florus 2.13 discrepancy (claimed superlative not found), legion count discrepancy (Plutarch says "a legion" not "three"). Once these remaining classical citations are verified, this package will approach master-readiness for core biographical claims.

---

## 4. Master-Candidate Facts

- Born 106 BCE in Picenum, Roman Italy; died 48 BCE in Egypt
- Raised three legions for Sulla at age 23 (83 BCE) — number disputed
- First triumph without holding formal magistracy (81/80 BCE) — unprecedented
- Lex Gabinia command (67 BCE): cleared Mediterranean of pirates in ~3 months
- Lex Manilia command (66 BCE): defeated Mithridates VI, reorganized Eastern provinces
- First Triumvirate with Caesar and Crassus (60 BCE); married Caesar's daughter Julia (59 BCE)
- Civil War against Caesar (49-48 BCE); defeated at Pharsalus; assassinated in Egypt

---

## 5. Staging-Only Claims

- "Three legions" claim — Plutarch says "a legion"; number needs cross-referencing
- Claims citing Florus for superlative praise — Florus 2.13 does NOT contain "most magnificent"
- "Adulescentulus carnifex" (teenage butcher) — Valerius Maximus 6.2.8 needs_verification
- Pro Lege Manilia sections 27-35 — approximate, not verified against critical edition
- Velleius Paterculus passage for birth — not independently verified

---

## 6. Reception / Legendary / Disputed Material

- "First Triumvirate" — modern historiographical label (18th-19th c.), not an ancient term
- "Pompey the Great" (Magnus) — title given by Sulla after African campaign, but ancient sources vary on the exact context
- Assessment of Pompey's generalship — modern scholarly debate; package correctly marks reception claims

---

## 7. Source Issues

| Issue | Severity |
|-------|----------|
| Cicero Pro Lege Manilia sections 27-35 approximate | Medium |
| Valerius Maximus 6.2.8 needs_verification | Medium |
| Florus 2.13 passage mismatch — claimed superlative absent | High |
| Legion count discrepancy (3 vs 1) | Medium |
| Velleius Paterculus passage unverified | Medium |
| RRC coinage catalogue numbers not provided | Low |
| 4 C-level sources present | Medium |

---

## 8. Relationship Issues

| Issue | Detail |
|-------|--------|
| Relationship types v2.5 compliant | All remapped in hardening sprint |
| Spouse relationships (3x) | Correctly typed as spouse |
| Caesar rivalry | Correctly same_political_context / opponent |

---

## 9. Visual Media Issues

- Ny Carlsberg Glyptotek bust inventory number unverified
- All 5 entries staging
- Coin portraits need RRC catalogue numbers

---

## 10. Recommended Cleanup Actions

1. Cross-reference Valerius Maximus 6.2.8 with Loeb critical edition
2. Add Florus 2.13 verified passage text and remove unsubstantiated superlative claim
3. Cross-reference legion count (1 vs 3) across Plutarch, Appian, Cassius Dio
4. Add specific RRC numbers for Pompeian coinage
5. Verify Ny Carlsberg Glyptotek bust inventory number from museum catalogue
6. Add critical edition (Loeb/Teubner/OCT) references for Pro Lege Manilia

---

## 11. Obsidian Demo Suitability

**YES — recommended as primary Western demo person.** Most extensive package (42 claims). Strong classical source coverage with verified Loeb references. Person_id consistent across all files. Compound claims pre-split. Relationship network rich with 12 entries.

---

## 12. Do-Not-Promote-Yet Notes

- **Do not promote claims dependent on Valerius Maximus or Florus** until passage verification is complete
- **Do not promote "three legions" claim** without cross-referencing all classical sources
- Visual media must remain staging pending museum verification
