# Central Review — Cleopatra VII (Cleopatra VII Philopator)

**Reviewer:** MorphMind AI
**Date:** 2026-05-15
**Branch:** `review/batch1-central-review-source-audit-v1`

---

## 1. Person Name and ID

- **Name:** Cleopatra VII Philopator / 克娄巴特拉七世·菲洛帕托尔
- **Person ID:** `P_WEST_PTOLEMAIC_CLEOPATRA_VII`
- **Dates:** Early 69 BCE – 10 or 12 August 30 BCE

## 2. Source Package Path

`incoming/western/cleopatra-vii/`

## 3. Current Status

`ai_collected_unreviewed`

## 4. Validation Result

**PASSED** — all 11 required files present, JSONL valid, person_id consistent.

## 5. Master-Candidate Facts

- Birth: early 69 BCE, Alexandria
- Death: 10 or 12 August 30 BCE, Alexandria
- Macedonian Greek Ptolemaic dynasty, descended from Ptolemy I
- One of few Ptolemaic rulers who spoke Egyptian
- Co-ruled with brother Ptolemy XIII from 51 BCE; driven from Alexandria in power struggle
- 48 BCE: allied with Caesar, restored to throne
- Son with Caesar: Caesarion (Ptolemy XV Caesar)
- 41 BCE: met and allied with Mark Antony at Tarsus
- Three children with Antony: Alexander Helios, Cleopatra Selene II, Ptolemy Philadelphus
- 31 BCE: defeated with Antony by Octavian at Actium
- After her death, Ptolemaic dynasty ended; Egypt became Roman province

## 6. Staging-Only Facts

- Cleopatra spoke Egyptian (CLM_CL_004) — `probable`, single modern scholarly source. Widely accepted but based on Plutarch's statement, not direct documentation.
- Cleopatra's manner of death (CLM_CL_011, CLM_CL_012) — asp/snake bite is the ancient tradition. Multiple accounts exist. Correctly handled as uncertain.

## 7. Rejected or Unsafe Claims

None rejected. The following need caveats:

- **CLM_CL_011** (asp suicide): Correctly marked `probable`, not `confirmed`. States it "should not be treated as a certain medical fact."
- **CLM_CL_012** (death manner disputed): Correctly marked `disputed`.
- **CLM_CL_013** (Roman propaganda): Correctly marked `confirmed`. The claim that Roman/pro-Augustan propaganda is biased is itself a confirmed historiographical fact.

**Important:** No claims about Cleopatra's beauty, seductiveness, or ethnicity appear in the claims. This is correct — the package avoids the Roman propaganda tropes.

## 8. Source Issues

| Source | Issue | Severity |
|--------|-------|----------|
| SRC_CL_001 (Plutarch Antony) | Most detailed ancient source but pro-Augustan. B_high rating correct. | Low — bias noted |
| SRC_CL_002 (Cassius Dio) | Written 200+ years after events. B_high rating correct. | Low |
| SRC_CL_004 (coinage) | RRC or museum accession numbers needed. Marked needs_verification. | Medium |
| SRC_CL_006, SRC_CL_007 | D-level — correctly marked clue_only | Info only |

**Source sufficiency:** 7 sources, 5 non-D. 0.33 non-D sources per claim — above threshold. Acceptable.

**Source quality note:** Plutarch's Life of Antony is rated B_high. For Cleopatra specifically, Plutarch is the single most detailed ancient narrative source. His bias is properly flagged but the dependency is high — most Cleopatra biographical claims trace back to Plutarch or Cassius Dio.

## 9. Relationship Issues

- **REL_CL_001** (Julius Caesar): `documented_association` — correct. Cross-reference confirmed.
- **REL_CL_002** (Mark Antony): `documented_association` — correct. Cross-reference with mark-antony package.
- **REL_CL_003** (Octavian/Augustus): `opponent` — correct.
- **REL_CL_004** (Ptolemy XIII): Listed. Brother-husband, co-ruler turned enemy.
- **REL_CL_005** (Caesarion): Listed. Mother-son.

**Assessment:** Relationship types are well-chosen. Cross-package person_ids consistent. Mark Antony person_id uses `P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS` — consistent with other packages.

## 10. Event Issues

events.jsonl present. Not reviewed in detail in this pass.

## 11. Works/Artwork Issues

- No literary works attributed to Cleopatra (correct — no surviving writings)
- Coinage is listed as a source type, not a work
- Potential for adding: Cleopatra's alleged medical/cosmetic writings (attributed by later sources, likely spurious)

## 12. Visual Media Issues

3 visual_media entries, all staging status. Coin portraits and sculptural representations. Need museum/collection verification.

## 13. Reception/Legend/Fiction Separation

**Excellent — best in batch.** The package correctly separates:
- Roman propaganda image of "Oriental seductress" (CLM_CC_013) — correctly identified as propaganda, not objective assessment
- Later literary/film portrayals (CLM_CL_015) — correctly `reception_label`, explicitly mentions Shakespeare
- Asp death (CLM_CL_011, CLM_CL_012) — correctly uncertain and disputed
- No claims about beauty, seduction, ethnicity, or romanticized motives

This package is a model for how to handle a historically contested figure.

## 14. Recommended Cleanup Actions

1. Verify SRC_CL_004: RRC numbers or museum accession numbers for Cleopatra's coinage.
2. Add specific Plutarch Antony chapter references for key Cleopatra passages (chapter ranges provided in source notes — need precision).
3. Consider adding a claim about Cleopatra's education and intellectual reputation (well-documented in Roller 2010).
4. Verify museum inventory numbers for sculptural portraits.

## 15. Staging Readiness

**Staging-ready.** The package correctly handles the most historically contested figure in the batch. Roman propaganda bias is thoroughly documented, asp death is properly uncertain, Shakespearean/film reception is separated, and no romanticized claims are present. Source base (5 non-D) is adequate. The coinage source verification and Plutarch chapter precision are minor follow-up tasks. Can be used for staging immediately.
