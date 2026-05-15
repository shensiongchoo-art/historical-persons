# Central Review — Marcus Agrippa (Marcus Vipsanius Agrippa)

**Reviewer:** MorphMind AI
**Date:** 2026-05-15
**Branch:** `review/batch1-central-review-source-audit-v1`

---

## 1. Person Name and ID

- **Name:** Marcus Vipsanius Agrippa / 马库斯·维普萨尼乌斯·阿格里帕
- **Person ID:** `P_WEST_EARLY_PRINCIPATE_MARCUS_VIPSANIUS_AGRIPPA`
- **Dates:** ca. 64-63 BCE – March 12 BCE

## 2. Source Package Path

`incoming/western/marcus-agrippa/`

## 3. Current Status

`ai_collected_unreviewed`

## 4. Validation Result

**PASSED** — all 11 required files present, JSONL valid, person_id consistent.

## 5. Master-Candidate Facts

- Birth: ca. 64-63 BCE, plebeian family
- Death: March 12 BCE, Campania
- Close associate (political/military) of Octavian/Augustus from youth
- 36 BCE: defeated Sextus Pompey at Battle of Naulochus
- 31 BCE: commanded Octavian's fleet at Actium, defeated Antony and Cleopatra
- Consul three times: 37, 28, 27 BCE
- Oversaw extensive public works in Rome: original Pantheon, aqueducts (Aqua Julia, Aqua Virgo), public baths
- Married Julia (Augustus' daughter) — political marriage
- Sons Gaius and Lucius adopted by Augustus as heirs
- After Agrippa's death, Tiberius was compelled to marry Julia

## 6. Staging-Only Facts

- Agrippa's exact birth year (CLM_MA_014) — correctly marked `needs_verification`. Ancient sources do not provide a clear date.
- Agrippa's relationship with Octavian described as "political/military association" not "close friendship" (CLM_MA_004) — correct, well-handled.
- Independent assessment claim (CLM_MA_013) — modern historiographical position, correctly flagged as interpretive.

## 7. Rejected or Unsafe Claims

None rejected. The following need caveats:

- **CLM_MA_003** (trusted commander/partner): While confirmed, "最信任" (most trusted) is slightly superlative. The ancient sources support his importance but "most trusted" is interpretive.
- **CLM_MA_008** (public works): "大规模" (large-scale) is interpretive but widely accepted. The specific works listed are documented.
- **CLM_MA_004** (relationship framing): This is a meta-claim about how to interpret the relationship. Valuable as a caveat but unusual as a standalone claim.

## 8. Source Issues

| Source | Issue | Severity |
|--------|-------|----------|
| SRC_MA_001 (Suetonius) | B_high. Pro-Augustan. Bias properly flagged. | Low |
| SRC_MA_003 (Res Gestae) | A_candidate but self-serving. Bias properly flagged. | Low |
| SRC_MA_005 (Reinhold 1932) | Only academic monograph on Agrippa. Dated (1932). Supplemented by Powell 2015 in notes. | Medium |
| SRC_MA_006, SRC_MA_007 | D-level — correctly marked clue_only | Info only |

**Source sufficiency:** 7 sources, 5 non-D. 0.36 non-D sources per claim — above threshold. Acceptable.

**Note:** The only academic monograph (Reinhold 1932) is nearly a century old. This reflects a real gap in the scholarship — Agrippa has no modern OUP/Cambridge university press biography. The notes correctly mention Powell 2015 as a supplement.

## 9. Relationship Issues

- **REL_MA_001** (Augustus/Octavian): `documented_association` — correct. The summary appropriately uses "political/military associate" rather than "friend."
- **REL_MA_002** (Mark Antony): `opponent` — correct. Actium documented.
- **REL_MA_003** (Cleopatra VII): `opponent` — correct. Actium documented.
- **REL_MA_004** (Julia the Elder): `family` — correct. Empty related_person_id (Julia not yet in database).
- **REL_MA_005** (Tiberius): `same_political_context` — correct. Empty related_person_id. The relationship is indirect (via Julia).

**Assessment:** Well-chosen types. The avoidance of "friend" for Augustus and the use of `same_political_context` for Tiberius show good judgment.

## 10. Event Issues

events.jsonl present. Not reviewed in detail in this pass.

## 11. Works/Artwork Issues

- Agrippa's works are architectural/public works, not literary
- Original Pantheon, Aqua Julia, Aqua Virgo, public baths listed
- Archaeological evidence of original Pantheon is limited (Hadrian's rebuild replaced it)
- Aqueduct routes and specifications could be documented more precisely

## 12. Visual Media Issues

3 visual_media entries, all staging status. Portrait busts (Louvre, Uffizi attributions) need museum inventory verification.

## 13. Reception/Legend/Fiction Separation

**Good.** The package correctly:
- Frames Agrippa's achievements as independently assessable (CLM_MA_013), pushing back against the tendency to subsume him into the Augustan narrative
- Labels his relationship with Octavian as political/military, not personal friendship (CLM_MA_004)
- Notes the political nature of his marriage to Julia
- No legendary or fictional material present (Agrippa has no major literary/film reception tradition)

## 14. Recommended Cleanup Actions

1. Verify exact Cassius Dio book/chapter references for Agrippa's campaigns and public works (book ranges provided — need chapter precision).
2. Verify Res Gestae sections referencing Agrippa.
3. Add museum inventory numbers for Agrippa portrait busts (Louvre, Uffizi).
4. Document aqueduct routes and specifications more precisely if sources allow.
5. Consider adding Powell 2015 (Pen & Sword) as a formal source entry to supplement the dated Reinhold monograph.
6. Verify the scholarly consensus on Agrippa's birth year (currently marked `needs_verification`).

## 15. Staging Readiness

**Staging-acceptable with minor verification notes.** The package is well-structured with correct relationship typing, appropriate framing of Agrippa's independent achievements, and proper caveats about ancient source bias. The main concern is the dated monograph (1932) — but this reflects a real gap in the scholarship, not a package error. Adding Powell 2015 as a formal source would strengthen the package. Loeb chapter verification and museum IDs are minor follow-up tasks. Can be used for staging.
