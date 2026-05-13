# Open Questions — Pompey (Gnaeus Pompeius Magnus)

## High Priority

1. **Exact page/chapter references for classical sources**: Plutarch, Appian, and Cassius Dio are cited but without specific passage references (e.g., "Plutarch, Life of Pompey ch. 46"). All three marked `needs_verification` for citation details. Needs standard edition references (e.g., Loeb Classical Library).

2. **Caesar's Civil War edition**: SRC004 (Caesar, *Commentarii de Bello Civili*) cited as primary text without edition reference. Needs Loeb or Oxford Classical Text specification.

3. **Crawford coin catalogue numbers**: SRC012 (Crawford, *Roman Republican Coinage*, 1974) verified but specific RRC catalogue numbers for Pompey's coins (the 71 BCE aureus and 56 BCE denarius) are not provided.

## Medium Priority

4. **Pompey portrait identification — Ny Carlsberg Glyptotek bust**: Multiple competing identifications exist for the "Pompey" portrait type. Needs museum inventory number and scholarly consensus reference.

5. **Villa Arconati statue provenance**: Described as "reputed" Pompey statue. Needs art-historical verification of the identification and provenance from 1627 Rome transfer.

6. **Leach (1978) page references**: Standard modern biography (SRC005) cited extensively but without specific page/chapter references.

7. **Cambridge Ancient History page references**: Authoritative reference (SRC006) needs specific volume/chapter/page citations.

8. **Ptolemy XIII's advisors**: Pothinus, Theodotus, Achillas are consistently named in classical sources (Plutarch) for the decision to kill Pompey, but not verified in the current source set. Needs cross-reference with Plutarch, *Life of Pompey*.

## Low Priority

9. **Exact date of death — 28 vs 29 September**: English Wikipedia gives 28 September 48 BCE; some Chinese sources give 29 September. The 28th is more widely cited and makes him die one day before his 58th birthday, which may have literary appeal. Needs verification against primary sources.

10. **Sulla's ironic use of "Magnus"**: Mommsen's claim that Sulla first used the cognomen with bitter irony is cited in Wikipedia but unverified in the sources consulted. Needs checking against Mommsen's *Römische Geschichte* or modern scholarship.

11. **Shakespeare references to Pompey**: Listed in legendary_notes as reception. Mentioned in *Julius Caesar* and *Antony and Cleopatra* but specific act/scene references not provided.

12. **Modern historical fiction list**: Colleen McCullough, Steven Saylor, Robert Harris listed as reception. These are well-known but specific novel titles and publication dates not verified.

## Hardening Sprint Notes (v1, 2026-05-12)

- person_id standardized from `P_WEST_ROMAN_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` → `P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS` across all package files (88 occurrences replaced).
- Package source base: PR#4 (collect/wang-yangming-and-pompey-v1) used as the complete Pompey staging package. PR#2 (collect/gnaeus-pompeius-magnus-v1) contains only claims.jsonl and open_questions.md — not a full package.
- Compound claims already split (Julia's death, Luca renewal, Crassus death, Pharsalus details). Retained.
- `Magnus` title origin: retained as `disputed/medium` — multiple competing origin stories in classical sources.
- `adulescentulus carnifex` nickname: retained as `reception/medium`.
- Cicero (R006) and Cato (R007): conservative wording retained from PR#4.
- Source passage references (Plutarch, Appian, Cassius Dio): all marked `needs_verification`. See items 1–2 above. Source verification deferred to dedicated verification sprint (PR#6).

## Recommended Review Actions

1. Provide Loeb Classical Library references for all classical source citations
2. Add RRC catalogue numbers for Pompey's coinage (Crawford 1974)
3. Verify Pompey bust identification with museum catalogues (Copenhagen Ny Carlsberg Glyptotek, Venice Museo Archeologico)
4. Cross-reference Ptolemy XIII's advisors with Plutarch (*Life of Pompey*)
5. Add specific page references for Leach (1978) and Cambridge Ancient History
6. Verify Mommsen's claim about Sulla's ironic use of "Magnus"

## Source Verification Sprint Notes (v2, 2026-05-12)

### Classical sources — Loeb refs added (SRC001–SRC004, SRC013–SRC014)
- SRC001 (Plutarch, Life of Pompey): LCL 87, Perrin 1917. Promoted A_candidate → **A**. Key chapters: 1–13 (birth/Sulla/cognomen), 17–22 (Sertorian War), 30–33 (lex Manilia), 46–48 (Triumvirate), 68–73 (Pharsalus), 77–80 (death in Egypt).
- SRC002 (Appian, Civil Wars): LCL 543–544, McGing 2020 (preferred over older White 1913 LCL 3–5). Promoted **A**. Books 2–5.
- SRC003 (Cassius Dio): LCL 53 (Books 36–40, Cary 1914) + LCL 66 (Books 41–45, Cary 1916). Promoted **A**.
- SRC004 (Caesar, Bello Civili): LCL 39, Damon 2016 (preferred over Peskett 1914). Promoted **A**. Books 1–3.
- SRC013 (Plutarch, Life of Crassus): LCL 65, Perrin 1916. Promoted **A**. Key chapters: 11–13 (Spartacus), 14–15 (joint consulship), 36–38 (Luca).
- SRC014 (Cicero, Pro Lege Manilia): LCL 198, Hodge 1927. Promoted **A**. §27–50 key for Pompey's qualities.

### Still needs_verification
- SRC005 (Leach 1978): page references not yet added — defer to bibliography sprint.
- SRC006 (Cambridge Ancient History vol. IX): page references not yet added.
- SRC007 (Oxford Classical Dictionary): entry pages not yet added.
- SRC012 (Crawford, Roman Republican Coinage): RRC catalogue numbers for Pompey coins not yet added.
