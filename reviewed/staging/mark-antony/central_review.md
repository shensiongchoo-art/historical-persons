# Central Review: Mark Antony (Marcus Antonius)

**Reviewer:** MorphMind AI
**Date:** 2026-05-14
**Package:** `incoming/western/mark-antony/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS` |
| **Name (EN)** | Mark Antony / Marcus Antonius |
| **Name (ZH)** | 马克·安东尼 / 马库斯·安东尼乌斯 |
| **Birth** | 83 BCE (disputed; 14 January) |
| **Death** | 30 BCE (1 August, suicide in Alexandria) |
| **Culture** | Roman / Late Republic |
| **Canonical Source** | PR#7 (`collect/wu-kuan-and-mark-antony-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized PR #9, cleanup PR #11) |

---

## 2. Current Package Status

Package is complete (11/11 required files) and passes validation. Normalized to v2.5 schema in PR #9 hardening pass. Cleanup applied in PR #11 (person_id standardized, relationship types aligned to v2.5). Ancient sources correctly leveled: Plutarch/Appian/Cassius Dio at B_high (secondary narratives with bias), Cicero Philippics/Caesar Civil War/Res Gestae at A_candidate (primary documents). No D or C sources — clean source base.

---

## 3. Overall Central Review Verdict

**STAGING ONLY — NOT READY FOR MASTER PROMOTION.** Package has clean architecture — no D/C-level sources, all v2.5 schema compliant, relationships schema correct. Primary blocker is the complete absence of verified Loeb chapter/passage references for all ancient sources. All ancient citations remain `needs_verification`. Once source verification sprint covers Mark Antony (equivalent to what was done for Pompey and Augustus), this package will move from Tier 2 to Tier 1.

---

## 4. Master-Candidate Facts

- Born 83 BCE (Cicero Phil. evidence; Plutarch records age at death as 53 or 56)
- Tribune of the Plebs (49 BCE); Master of Horse under Caesar; Consul (44 BCE)
- Caesar's funeral oration turned Rome against the Liberators
- Second Triumvirate with Octavian and Lepidus (43 BCE); renewed 37 BCE
- Allied with Cleopatra VII of Egypt; received eastern provinces
- Defeated at Battle of Actium (31 BCE); died by suicide (30 BCE)
- Antony's children with Cleopatra (Alexander Helios, Cleopatra Selene, Ptolemy Philadelphus)

---

## 5. Staging-Only Claims

- All ancient source-dependent claims marked `needs_verification` for passage refs
- Birth year dispute — 83 BCE from Cicero Phil.; Plutarch gives contradictory age at death
- Antony's "Hellenistic" or "Orientalizing" political style — modern scholarly framing, partially reception

---

## 6. Reception / Legendary / Disputed Material

- "Antony as Caesar's loyal lieutenant" — embedded in ancient sources with pro-Augustan bias
- Octavian's propaganda: Antony as "enslaved by Cleopatra" — hostile tradition
- Assessment of Antony's generalship — mixed in modern scholarship; Parthian campaign a failure, Philippi/Acrum judged differently
- Shakespeare's *Antony and Cleopatra* — literary/fictional reception, not historical source

---

## 7. Source Issues

| Issue | Severity |
|-------|----------|
| No verified Loeb chapter/passage refs for any ancient source | High |
| Plutarch *Antony* chapters not specified | High |
| Appian *Civil Wars* books not specified for Antony-specific claims | High |
| Cassius Dio books not specified for Antony-specific claims | High |
| Cicero Philippics passage refs not provided | Medium |
| Caesar *Civil War* passage refs not provided | Medium |
| Only 4 modern scholarly sources for 35 claims | Medium |

---

## 8. Relationship Issues

| Issue | Detail |
|-------|--------|
| Relationship types v2.5 compliant | opponent, documented_association, spouse, sibling, same_political_context |
| 13 relationships | Strongest relational data of all 7 packages |
| Cleopatra VII | Package not yet collected — relationship claims one-sided |

---

## 9. Visual Media Issues

- 4 entries, all staging
- Coin portraits need RRC/RIC catalogue numbers
- Sculpture identifications need museum inventory verification

---

## 10. Recommended Cleanup Actions

1. **CRITICAL**: Source verification sprint — add Plutarch *Antony* Loeb chapter refs for all claims
2. Add Appian *Civil Wars* book/section refs for Triumvirate, Philippi, Actium
3. Add Cassius Dio book/section refs for Antony-related passages
4. Add Cicero Philippics specific section refs for Antony's actions 44-43 BCE
5. Cross-reference birth year (83 vs 86 BCE) across Cicero Phil., Plutarch, and Appian
6. Add at least 2 additional modern scholarly sources (e.g., Southern 1998, Huzar 1978)

---

## 11. Obsidian Demo Suitability

**YES — conditional on source verification.** Well-structured package with clean source base. Relationships v2.5 compliant. Both English and Chinese claim text. Ancient bias caveats included. The lack of verified chapter refs is the primary issue — but the package is usable for demo showing structure, relationships, and claim architecture.

---

## 12. Do-Not-Promote-Yet Notes

- **Do not promote to master_candidates** until at least Plutarch *Antony* Loeb chapter refs are verified
- **Do not promote birth date claim** as confirmed until cross-referencing Cicero, Plutarch, and Appian
- Future Cleopatra VII package should be collected before promoting cross-person relationship claims
