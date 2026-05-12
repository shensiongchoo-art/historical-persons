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
