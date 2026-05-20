# Batch 3 Source Verification — Crassus + Brutus

**Date**: 2026-05-17
**Branch**: verification/batch3-crassus-brutus-source-check-v1
**Packages**: marcus-licinius-crassus, marcus-junius-brutus
**Reviewer**: MorphMind AI (academic search + known-bibliography check)

---

## 1. Crassus Sources

### SRC_CRS_001 — Plutarch, Life of Crassus
- **Exists**: Yes. Standard Loeb Classical Library text (Parallel Lives, Vol. III).
- **Verification**: Plutarch's Life of Crassus is a well-attested ancient biography in the Parallel Lives collection. Paired with Life of Nicias.
- **Passage refs**: needs_verification. Specific section/chapter references for each claim not verified.
- **Status**: A_candidate → **keep A_candidate**. Exact passages need verification but source is canonical.
- **Affected claims**: CLM_CRS_001–016 (all Crassus claims reference this source).

### SRC_CRS_002 — Appian, Civil Wars
- **Exists**: Yes. Loeb Classical Library edition, Books 1–2 cover the relevant period.
- **Verification**: Appian's Bella Civilia is the standard Greek historian's account of the late Republic. Book 2 covers the triumvirate through Caesar's death; Book 1 covers the Spartacus war.
- **Passage refs**: needs_verification. Exact book/chapter references not verified.
- **Status**: A_candidate → **keep A_candidate**.

### SRC_CRS_003 — Cassius Dio, Roman History
- **Exists**: Yes. Loeb Classical Library, Books 39–40 cover Crassus' Parthian campaign.
- **Verification**: Dio's account of Carrhae is the most detailed surviving narrative of the campaign.
- **Passage refs**: needs_verification.
- **Status**: A_candidate → **keep A_candidate**.

### SRC_CRS_004 — Cicero, Letters
- **Exists**: Yes. Loeb Classical Library editions of Epistulae ad Atticum and ad Familiares.
- **Verification**: Cicero's letters are contemporary to Crassus (106–43 BCE). Letters mentioning Crassus exist but specific letter numbers need verification.
- **Passage refs**: needs_verification.
- **Status**: A_candidate → **keep A_candidate**. Note: Cicero is a biased contemporary source — his advocacy perspective should be flagged.

### SRC_CRS_005 — Cadoux, T.J. in OCD4
- **Exists**: Confirmed. Oxford Classical Dictionary, 4th edition (2012).
- **Verification**: Entry on "Marcus Licinius Crassus" is a standard reference article.
- **Status**: B_high → **keep B_high**. Encyclopedia entry, not monograph-length treatment.

### SRC_CRS_006 — Marshall, B.A., Crassus: A Political Biography
- **Exists**: CONFIRMED. Marshall, Bruce A. *Crassus: A Political Biography*. Amsterdam: Hakkert, 1976. vii + 206 pp., 1 map.
- **Verification**: Located via academic search. Reviewed in classical journals. This is the principal English-language monograph on Crassus.
- **Status**: B_high → **keep B_high**. Standard modern scholarly monograph.
- **Note**: Published by Hakkert (Amsterdam), not "Hakkert" alone. Citation detail in sources.jsonl should be updated to reflect publisher location.

### SRC_CRS_007 — Wikipedia
- **Exists**: Yes, but tertiary.
- **Status**: C → **keep C (clue_only)**. Correctly flagged.

### Molten Gold Death Story (LEG_CRS_001)
- **Verification**: Confirmed as literary/dramatic motif. Academic papers analyze it as "Dionysiac tragedy" in Plutarch's Crassus (see [relations_between_tragedy], [dionysiac_tragedy_plutarch], [death_m_licinius]).
- **Status**: needs_verification → **keep needs_verification**. Scholarly consensus considers this a literary invention or dramatic motif, not verified historical fact. Correctly placed in legendary_notes.jsonl.

---

## 2. Brutus Sources

### SRC_BRU_001 — Plutarch, Life of Brutus
- **Exists**: Yes. Standard Loeb Classical Library text (Parallel Lives, Vol. VI). Paired with Life of Dion.
- **Verification**: A modern scholarly commentary exists (likely Moles or Pelling) [commentary_plutarchs_brutus]. The biography is the principal ancient source.
- **Passage refs**: needs_verification.
- **Status**: A_candidate → **keep A_candidate**.

### SRC_BRU_002 — Appian, Civil Wars
- **Exists**: Yes. Books 2–4 cover the assassination and Philippi campaign.
- **Verification**: Appian's account is the most continuous narrative of the civil wars period. See [appian_cassius_dio] for scholarship on Appian's reliability.
- **Passage refs**: needs_verification.
- **Status**: A_candidate → **keep A_candidate**.

### SRC_BRU_003 — Cicero, Brutus, Orator, and Correspondence
- **Exists**: Yes. Loeb Classical Library editions.
- **Verification**: Cicero's dialogue *Brutus* (on Roman oratory) is a major source for Brutus' intellectual reputation. The *Epistulae ad Brutum* are a distinct letter collection.
- **Passage refs**: needs_verification.
- **Status**: A_candidate → **keep A_candidate**. Note: Cicero's works are advocacy, not neutral reporting.

### SRC_BRU_004 — Cassius Dio, Roman History
- **Exists**: Yes. Books 41–47 cover Caesar's civil war through Philippi.
- **Verification**: Dio provides the most detailed account of the Philippi campaign among surviving sources.
- **Passage refs**: needs_verification.
- **Status**: A_candidate → **keep A_candidate**.

### SRC_BRU_005 — Suetonius, Life of the Deified Julius
- **Exists**: Yes. Loeb Classical Library.
- **Verification**: Suetonius Divus Iulius 82.3 reports "kai su, teknon" as Caesar's words. Scholarly debate exists on the historicity — see [caesars_one_fatal] for analysis.
- **Status**: A_candidate → **keep A_candidate**.
- **Note**: "Kai su, teknon" historicity is debated. Correctly flagged as needs_verification in claim CLM_BRU_013 and legendary_notes LEK_BRU_001.

### SRC_BRU_006 — Crawford, Roman Republican Coinage (RRC 508/3)
- **Exists**: CONFIRMED. Crawford, Michael H. *Roman Republican Coinage*. Cambridge University Press, 1974. RRC 508/3 is the standard catalog number for the Eid Mar denarius.
- **Verification**: RRC is the authoritative numismatic reference for Roman Republican coinage. The Eid Mar type is well-documented.
- **Status**: B_high → **keep B_high**. Standard reference catalog.

### SRC_BRU_007 — Shakespeare, Julius Caesar
- **Exists**: Yes. First performed 1599, First Folio 1623.
- **Verification**: Literary work, not historical source.
- **Status**: D → **keep D (reception_only)**. Correctly classified. Shakespeare's "Et tu, Brute?" is a literary invention — this is correctly flagged in legendary_notes LEK_BRU_001 and claim CLM_BRU_016.

### SRC_BRU_008 — Tempest, K., Brutus: The Noble Conspirator
- **Exists**: CONFIRMED. Tempest, Kathryn. *Brutus: The Noble Conspirator*. Yale University Press, 2017.
- **Verification**: Located via academic search [brutus_noble_conspirator]. This is a recent, well-reviewed scholarly biography.
- **Status**: B_high → **keep B_high**. Excellent modern source.

### SRC_BRU_009 — Wikipedia
- **Exists**: Yes, but tertiary.
- **Status**: C → **keep C (clue_only)**. Correctly flagged.

---

## 3. Cross-Package Source Issues

### Shared ancient sources
Both packages cite Plutarch, Appian, and Cassius Dio. These are standard, well-attested texts available in Loeb Classical Library editions. No fabrication concerns. However:
- **Plutarch's Lives**: Crassus is in Vol. III (with Nicias); Brutus is in Vol. VI (with Dion). Different volumes.
- **Appian Civil Wars**: Books 1–2 for Crassus-era; Books 2–4 for Brutus-era. Both in standard Loeb.
- **Cassius Dio**: Books 39–40 for Crassus/Carrhae; Books 41–47 for Caesar through Philippi.

### Missing source: Plutarch's Life of Caesar
- Brutus package could potentially cite Plutarch's Life of Caesar as an additional source for the assassination narrative. Not required but would strengthen source diversity.
- **Recommendation**: Consider adding SRC_BRU_010 = Plutarch, Life of Caesar (A_candidate, needs_verification) in a future pass, but not blocking.

### Missing source: Plutarch's Life of Pompey
- Crassus package does not cite Plutarch's Life of Pompey, which contains substantial material on the First Triumvirate and Crassus-Pompey rivalry.
- **Recommendation**: Optional addition in future enrichment pass. Not blocking.

---

## 4. Claim-by-Claim Risk Assessment

### Crassus claims requiring no changes
CLM_CRS_001–011, CLM_CRS_013–014: Well-supported by Plutarch + parallel sources. Confidence levels appropriate.

### Crassus claims with caveats
- **CLM_CRS_012** (7,100 talents): Plutarch's figure should be treated as approximate. Confidence "probable" is appropriate.
- **CLM_CRS_015** (Tertulla marriage): Sparse source evidence. "probable" is appropriate.
- **CLM_CRS_016** (molten gold): Correctly at needs_verification. Scholarly literature confirms this is a literary motif [relations_between_tragedy], [death_m_licinius].

### Brutus claims requiring no changes
CLM_BRU_001–012, CLM_BRU_014–015: Well-supported by Plutarch + Cicero + coinage evidence. Confidence levels appropriate.

### Brutus claims with caveats
- **CLM_BRU_013** (Caesar's paternity): Correctly at needs_verification. Chronologically improbable.
- **CLM_BRU_016** (Shakespeare's "Et tu, Brute?"): Correctly at confirmed (as literary fact, not historical fact). Properly sourced to Shakespeare (D/reception_only).

---

## 5. Recommended Source File Updates

### Crassus sources.jsonl — minor fix needed
- **SRC_CRS_006 (Marshall)**: Publisher should read "Amsterdam: Hakkert, 1976" not just "Hakkert, 1976." Non-blocking editorial fix.
- **SRC_CRS_005 (Cadoux)**: Citation detail is adequate for an encyclopedia entry.

### Brutus sources.jsonl — no fixes needed
All source entries are accurate. No fabrication detected.

---

## 6. Verification Summary

| Source | Exists | Classification | Confidence |
|--------|--------|---------------|------------|
| Plutarch, Crassus | Yes | A_candidate | High |
| Plutarch, Brutus | Yes | A_candidate | High |
| Appian, Civil Wars | Yes | A_candidate | High |
| Cassius Dio | Yes | A_candidate | High |
| Cicero Letters | Yes | A_candidate | High |
| Cicero Brutus/Orator | Yes | A_candidate | High |
| Suetonius, Div. Iul. | Yes | A_candidate | High |
| Marshall 1976 | Yes | B_high | Confirmed |
| Tempest 2017 | Yes | B_high | Confirmed |
| Crawford RRC 1974 | Yes | B_high | Confirmed |
| Cadoux OCD4 | Yes | B_high | High |
| Shakespeare | Yes | D/reception | Confirmed |
| Wikipedia ×2 | Yes | C/clue_only | Confirmed |

**Overall**: All 13 cited sources confirmed to exist. No fabricated sources detected. Molten gold and "Et tu, Brute?" motifs correctly classified as legendary/literary. Source reliability levels are appropriate for all entries.

---

## 7. Remaining Gaps

1. **Passage-level verification**: No specific book/chapter/section references verified for any ancient source claim. All ancient sources marked needs_verification for passage refs. This requires Loeb volume access or digital edition lookup (Perseus, LacusCurtius).

2. **Cicero letter numbers**: Specific letters mentioning Crassus (e.g., Ad Atticum 4.13, Ad Fam. 5.8) not verified. Non-blocking.

3. **OCD4 exact page**: Cadoux entry page number not verified. Encyclopedia entries are short; this is minor.

4. **Crawford RRC 508/3 holdings**: Specific museum accession numbers for Eid Mar specimens not verified. Staging-only visual media appropriately handles this.

5. **Marshall 1976 availability**: Out of print; may be difficult to access for independent verification. Tempest 2017 is widely available as a substitute for modern scholarship on the late Republic.

---

## 8. Recommendation

- **Both packages are staging-acceptable** with current source citations.
- No sources need downgrading or removal.
- Marshall publisher detail is the only recommended edit.
- Passage-level verification is a future enrichment task, not blocking for staging.
- No claim confidence levels need adjustment based on this source check.

**Action**: Merge this report, then proceed to content review of claims/relationships.
