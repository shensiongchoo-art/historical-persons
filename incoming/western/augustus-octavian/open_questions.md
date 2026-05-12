# Augustus (Gaius Octavius / Octavian / Augustus) — Open Questions

## Biographical
1. Was Augustus born on 22 or 23 September 63 BCE? Suetonius and Velleius Paterculus give 23 September; Cassius Dio gives 22 September. Scholarly consensus favors 23 September, but the discrepancy remains unresolved.
2. What was the exact date of his father Gaius Octavius's death — 59 or 58 BCE? Sources differ.

## Legal and Constitutional
3. What was the legally precise nature of Caesar's testamentary adoption? The will created a *condicio nominis ferendi* (condition of assuming the name), which was not equivalent to full *adrogatio*. Modern scholarship (Tatum 2024, Lindsay 2009) debates how contemporaries understood the legal position between May 44 BCE and the passage of the *lex curiata* in August 43 BCE.
4. Did Augustus receive *imperium consulare maius* in 23 BCE or only in 19 BCE? The exact scope and timing of his proconsular imperium under the Second Settlement requires careful reading of fragmentary evidence.

## Military
5. What exactly was Augustus's role at the Battle of Philippi (42 BCE)? He was reportedly ill during the first engagement. Antony's accusations of cowardice need to be evaluated against other evidence.
6. Was the Teutoburg Forest disaster (9 CE) the result of strategic overreach or operational failure? The *Res Gestae* omits this event entirely, making objective assessment dependent on scattered references in other sources.

## Family and Succession
7. Did Livia poison Augustus, as Tacitus (*Annals* 1.5-6) and Cassius Dio suggest? Most modern historians reject this as hostile historical tradition, but the rumor itself reveals tensions in the transition to Tiberius.
8. What was the precise dynastic plan after the deaths of Marcellus (23 BCE) and Agrippa (12 BCE)? The succession path to Tiberius was circuitous and may not have been Augustus's first choice.

## Visual and Material Culture
9. How many contemporary portrait types of Augustus were produced, and how were they distributed across the empire? The Prima Porta type is the most famous, but other types (Actium type, Forbes type) need systematic cataloging.
10. The bronze Meroë Head (British Museum) was taken as a war trophy by Kushite forces during their invasion of Roman Egypt (24 BCE). Does this head represent a specific portrait type, and what does its context reveal about Augustan image distribution in the provinces?

## Reception and Historiography
11. To what extent did Augustus himself author the *Res Gestae*, and to what extent was it edited or supplemented after his death? The text as we have it was read in the Senate by Tiberius and Drusus after Augustus's death.
12. How should the "restoration of the Republic" narrative in Augustan propaganda be reconciled with the concentration of military, financial, and legislative power that characterized the regime after 27 BCE? This remains the central interpretive question.

## Hardening Sprint Notes (v1, 2026-05-12)

- claims.jsonl: normalized from v2.3 schema (text_en/text_zh, category) to v2.5 schema (claim_text_en/claim_text_zh, claim_type, person_id added).
- sources.jsonl: normalized from v2.3 schema (level, bibliographic_hint) to v2.5 schema (reliability_level, title, author; bibliographic_hint preserved as reference field).
- relationships.jsonl: normalized from v2.3 schema (rel_id, person_a/person_b, description_en) to v2.5 schema (relationship_id, person_id, related_person_name, evidence_note).
- Ancient sources (Suetonius, Cassius Dio, Appian, Res Gestae, Tacitus, Plutarch, Nicolaus of Damascus, Velleius, Cicero) correctly retained at level A or A_candidate; notes flag source bias.
- Res Gestae: self-presentation caveat in claims CLM_AU_018 and CLM_AU_027. Retained.
- "First Roman emperor" framing: downgraded to reception/medium in CLM_AU_022. Retained.
- Compound claims (name stages, marriages, titles, settlements, Actium) were split in v2.5 package. Retained.
- Source passage references (Suetonius Aug. chapter refs, Cassius Dio book/chapter refs): specific chapter numbers present in some citations (Aug. 5, Aug. 7.1, Aug. 79, Aug. 99). Remaining passage refs marked needs_verification — defer to source verification sprint.

## Source Verification Sprint Notes (v2, 2026-05-12)

### Ancient sources — Loeb refs added (SRC_AU_001–SRC_AU_009); all promoted A_candidate → **A**
- SRC_AU_001 (Suetonius, Divus Augustus): LCL 31, Rolfe 1914 (rev. 1998). Chapters: 5 (birth), 7–8 (adoption/names), 79 (appearance), 99–100 (death).
- SRC_AU_002 (Cassius Dio, Books 45–56): LCL 66, 82, 83, 175 (Cary 1916–1924). Book 53 key for constitutional settlements.
- SRC_AU_003 (Appian, Civil Wars 3–5): LCL 543–544, McGing 2020 (preferred). Books 3–4 (Triumvirate/proscriptions/Philippi), Book 5 (Sextus Pompeius).
- SRC_AU_004 (Res Gestae): No Loeb edition. Standard editions: Cooley 2009 (Cambridge; preferred) and Brunt & Moore 1967 (Oxford).
- SRC_AU_005 (Tacitus, Annales 1): LCL 249, Jackson 1931. Ann. 1.1–15 (retrospective on Augustus); Ann. 1.5–6 (Livia rumour — hostile tradition).
- SRC_AU_006 (Plutarch, Life of Antony): LCL 101, Perrin 1920. Key chapters: 16–22 (Triumvirate), 75–77 (Actium).
- SRC_AU_007 (Nicolaus of Damascus): No Loeb. Standard edition: Toher 2017, Cambridge Classical Texts & Commentaries 53.
- SRC_AU_008 (Velleius Paterculus): LCL 152, Shipley 1924 (rev. Woodman 2025). Book 2, chs. 59–130.
- SRC_AU_009 (Cicero, Philippics & Atticus): Philippics: LCL 189 + 507, Bailey 2010. Letters: LCL 7, 8, 200, 201, Bailey 1999.

### Author fields fixed
- All 18 SRC_AU_ records: author field replaced from "see bibliographic_hint" to named author.

### Still needs_verification
- SRC_AU_010 (Syme, Roman Revolution): page refs not added.
- SRC_AU_011 (Goldsworthy 2014): page refs not added.
- SRC_AU_013–014 (museum records): inventory verification with museum catalogue URLs added; formal citation_detail added.
- SRC_AU_017 (Wiseman JRA date "2025" in source record): year needs checking against actual publication — may be 2005.
- SRC_AU_018 (coinage): RIC I² references added; full numismatic citation deferred.
