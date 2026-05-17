# Pilot Phase A Review Notes

**Date:** 2026-05-16
**Branch:** `pilot/obsidian-phase-a-tang-yin-caesar-v1`
**Pilot Persons:** Tang Yin / 唐寅 + Julius Caesar

---

## 1. What Was Generated

| File | Size | Sections |
|------|------|----------|
| `obsidian-vault-pilot/01_Persons/Chinese/tang-yin.md` | ~155 lines | Frontmatter, Summary, Identity, Timeline, Fact/Legend Separation, Source Package, Review Status, Open Questions |
| `obsidian-vault-pilot/01_Persons/Western/julius-caesar.md` | ~140 lines | Frontmatter, Summary, Identity, Timeline, Fact/Reception/Fiction Separation, Source Package, Review Status, Open Questions |

Data sources used:
- `person_record.json` — person_id, names, dates, short_description, review_status
- `person_profile.md` — identity, early life, career, legend separation, source caveats

---

## 2. What Was Intentionally Excluded (deferred to Phase B/C/D)

| Excluded | Reason |
|----------|--------|
| Full claims tables from claims.jsonl | Phase B — would double file size; needs claim grouping by confidence/type |
| Source notes from sources.jsonl | Phase C — need canonical source notes before inline referencing |
| Relationship tables from relationships.jsonl | Phase D — need bidirectional links between person notes |
| Works lists from works.jsonl | Phase D — lower priority for initial pilot |
| Events from events.jsonl | Phase D — need event notes to link from timeline |
| Visual media metadata | Deferred — metadata only policy; no images until verified |
| Legendary notes detail | Phase B — full legendary_notes.jsonl content not yet added |

---

## 3. What Worked

1. **Frontmatter parses correctly** — all fields populated from person_record.json
2. **Fact/legend/reception separation is clear** — Tang Yin 唐伯虎点秋香 / 明四家 / 吴中四才子 are clearly categorized
3. **Caesar reception layers are well-separated** — "Et tu, Brute?", Caesar salad, Caesarean etymology explicitly flagged as literary/fictional/folk
4. **Source caveats are honest** — Caesar's Commentarii noted as self-interested; Plutarch as later synthesis; Cicero as political rival
5. **Review status is transparent** — every note starts with ⚠️ banner and includes review_status, source_sufficiency
6. **Timeline provides scannable overview** — each event marked confirmed/probable/disputed
7. **Open questions guide reviewer attention** — key uncertainties surfaced rather than buried

---

## 4. Risks Observed

| Risk | Severity | Notes |
|------|----------|-------|
| Timeline may drift from events.jsonl | Low | Phase D will reconcile; current timeline manually curated from profile |
| Related people links may break | Low | Wikilinks reference canonical_keys; all 22 persons share same naming convention |
| Missing claims granularity | Medium | Phase B is essential — timeline is coarse-grained; 18 claims each need row-level display |
| Source repetition across notes | Low | Phase C will create canonical source notes; current notes only reference source package |
| Frontmatter tags inconsistent across packages | Low | Standardize during Phase A batch generation for all 22 |

---

## 5. Phase B Recommendation

**Proceed with Phase B (claims tables) for the 2 pilot persons.**

Rationale:
- Phase A notes are structurally sound and reviewable
- Claims tables are the most information-dense addition — testing format with 2 persons before 22 is prudent
- Expected output: each note gains a "Claims" section with tables grouped by confidence/type
- Claims.jsonl fields to include: claim_id, statement, confidence, claim_type, source_ids, date_range

---

## 6. Vault Structure Assessment

The proposed structure works:
```
obsidian-vault-pilot/
└── 01_Persons/
    ├── Chinese/
    │   └── tang-yin.md          ✓ generated
    └── Western/
        └── julius-caesar.md     ✓ generated
```

Missing sections (by design — Phase C/D):
- `00_Project/` — not needed for 2-person pilot
- `02_Events/` — Phase D
- `03_Sources/` — Phase C
- `99_Templates/` — create when generating full batch

---

## 7. Next Actions

1. Review these 2 pilot notes in Obsidian (or visually inspect markdown)
2. If format approved → Phase B: add claims tables for Tang Yin + Julius Caesar
3. If Phase B approved → Phase A for all 22 persons
4. Then Phase C (source notes) and Phase D (relationships, events)
5. Do not start Batch 3 until all 22 are imported and reviewed
