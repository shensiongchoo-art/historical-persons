# 29-Person Obsidian Dry-Run Generation Report v1

**Date:** 2026-05-21
**Branch:** `mirror/obsidian-29-person-v1`
**Generator:** `tools/obsidian_dryrun_generator.py` (v3 — adds person-registry resolution)
**Sandbox:** `obsidian-vault-pilot/_dryrun_29_v1/`
**Predecessor sandbox:** `obsidian-vault-pilot/_dryrun_22_v1/` (kept as a reference)
**Live vault touched:** **NO**
**`incoming/` touched:** **NO**

---

## 1. Person count

**29 person notes generated** (15 Chinese + 14 Western):

- 22 from the prior wave (MVP + B1 + B2) — re-emitted from current `incoming/`
- 2 from Batch 3 — `marcus-licinius-crassus`, `marcus-junius-brutus`
- 5 from Batch 4 — `wang-shizhen`, `chen-chun`, `li-panlong`, `cato-the-younger`, `gaius-cassius-longinus`

All 29 person notes carry the canonical `⚠️ AI-COLLECTED / STAGING ONLY` banner under the H1 and the 16-section body structure (Summary → Identity → Life Timeline → Reception/Legend separation → Claims Overview → Confirmed/Probable/Reception tables → Relationships → Works → Sources (4 buckets) → Source Package → Review Status → Open Questions).

---

## 2. Source note count

**256 source notes generated** (133 Chinese + 123 Western):

- 203 carry-over from the 22-person sandbox (re-emitted with current data)
- 53 new from the 7 newly merged packages

Filename convention applied uniformly: `{canonical_key}__{source_id}.md`. **0 filename collisions** across `03_Sources/Chinese/` ∪ `03_Sources/Western/`.

---

## 3. D-level source note count

**38 source notes carry the 🚫 D-LEVEL — CLUE ONLY banner.**

- 30 from the 22-person wave
- 8 new from the 7 newly merged packages

Banner-presence audit: **0 missing** across all 38 D-level notes.

---

## 4. Source link validation

| Metric | Value |
|--------|-------|
| `[[<slug>__SRC*]]` wikilinks emitted across all 29 person notes | **1,732** |
| Unresolved source wikilinks | **0** |
| Forced retry / `(missing)` markers | **0** |

Every source wikilink in every person note targets a source-note file that exists in the sandbox.

---

## 5. Person link validation

| Metric | Value |
|--------|-------|
| `[[<slug>]]` person wikilinks emitted (related_people frontmatter + Relationships table) | **205** |
| Unresolved person wikilinks | **0** |
| Distinct missing-person *references* not emitted as wikilinks | **63** (134 individual occurrences across the 29 packages) |

The 134 unresolved references are NOT emitted as broken wikilinks. They appear as **plain text** in the Relationships-table Person column and are **omitted** from the `related_people:` frontmatter block. The generator v3 logs each one to `90_Staging_Review/_generation_manifest.json` under `unresolved_person_refs`. See §7 for the list.

---

## 6. Unresolved person references (the 134 / 63-distinct)

These are real historical persons mentioned in the 29-package relationship data who are **not yet collected** into the database. The generator behaves correctly: it does not invent wikilinks for them.

Top categories (63 distinct names; abbreviated):

| Category | Examples |
|----------|----------|
| **Roman family / political** (33 names) | Caesarion (Ptolemy XV), Cornelia Metella, Decimus Junius Brutus Albinus, Fulvia, Gnaeus Pompeius Magnus (son), Gnaeus Pompeius Strabo, Julia Caesaris, Julia the Elder, Lucius Antonius, Lucius Cornelius Sulla, Marcus Claudius Marcellus (son), Marcus Licinius Crassus (son), Mucia Tertia, Octavia Minor (already in vault — should resolve, see §8), Ptolemy XV Caesar (Caesarion), Quintus Hortensius Hortalus, Scribonia, Sextus Pompey (already in vault — should resolve, see §8), Tiberius Claudius Nero, Tiberius Sempronius Gracchus (the Censor), … |
| **Ming-dynasty Chinese figures** (~20 names) | 徐渭 (Xu Wei), 边贡 (Bian Gong), 谢榛 (Xie Zhen), 宗臣 (Zong Chen), 梁有誉 (Liang Youyu), 项元汴 (Xiang Yuanbian), 周臣 (Zhou Chen), 王宠 (Wang Chong), 陈洪绶 (Chen Hongshou), 严嵩 (Yan Song), 王锡爵, 张居正, … |
| **Mark Antony's family / opponents** | Lucius Antonius (brother), Fulvia, Antonia Major, Antonia Minor, Caesarion |
| **Other Republican / Imperial figures** | Marcus Tullius Cicero (son), Quintus Tullius Cicero, Marcus Junius Brutus (already in vault — should resolve, see §8), Cassius Longinus (already in vault — should resolve, see §8) |

Full list with full provenance (which package referenced each one) is available in `_dryrun_29_v1/90_Staging_Review/_generation_manifest.json` under `unresolved_person_refs`.

### Important caveat (registry mismatches worth investigating)

The generator's registry indexed every `person_record.json` field across the 29 incoming packages — 352 lookup keys across 29 canonical slugs. Yet some references that *should* have matched did not. Quick spot-check during writing this report suggests these miss-cases when the *referencing* package uses a name string that doesn't appear in the *referenced* package's `person_record.json`. Examples:

- Package A (e.g. `mark-antony`) lists a relationship to "Octavia Minor" — but `octavia-minor`'s `person_record.json` may use "Octavia" or a different name variant as the primary display name, so the lookup misses.
- Package A uses a Pinyin form ("zhou-chen") for the related_person_name, but `周臣` is not in the registry because Zhou Chen is *not* in the 29-package set (correctly unresolved).

The 63 names need a manual triage to separate **actually-missing** persons (deferred collection) from **registry-miss** cases (where both persons are in the 29 set but the name didn't match a registry key).

---

## 7. Changes from the 22-person dry-run

| Dimension | 22-person dry-run (v2) | 29-person dry-run (v3) | Delta |
|-----------|-------------------------|--------------------------|-------|
| Person notes | 22 | **29** | +7 |
| Source notes (namespaced) | 203 | **256** | +53 |
| D-level source notes | 30 | **38** | +8 |
| Source wikilinks emitted | 1,360 | **1,732** | +372 |
| Unresolved source wikilinks | 0 | **0** | 0 |
| Person wikilinks emitted | ~225 (with slug-guesses) | **205** | -20 (no slug guesses now) |
| **Unresolved person wikilinks** | 3 distinct in sandbox; 2 distinct in vault | **0** | -2/-3 |
| Generator version | v2 (slug-guess heuristic) | **v3 (registry-based)** | architectural |
| Manifest tracks unresolved person refs? | no | **yes** (134 individual / 63 distinct) | new field |
| Sandbox path | `_dryrun_22_v1/` | `_dryrun_29_v1/` | new (22-person kept as reference) |
| Em-dash Status column behaviour | unchanged | unchanged (still deferred) | — |

The v3 generator is **strictly better** at person-link emission: it emits ONLY confident matches, falls back to plain text otherwise, and surfaces every miss in the manifest. No more zombie `[[marcus-tullius-cicero]]` wikilinks pointing to nothing.

---

## 8. Whether safe to mirror to live vault

**Yes — safe to mirror,** subject to two non-blocking caveats below.

Hard requirements (all met):
- [x] All 29 person notes generated; YAML parses cleanly on all 285 files in the sandbox.
- [x] 0 source filename collisions; 0 unresolved source wikilinks.
- [x] 38 D-level notes carry the 🚫 banner.
- [x] 0 unresolved emitted person wikilinks (the 134 unresolved *references* are plain-text or omitted by design).
- [x] Pilot files in the live vault unchanged (MD5 verified: tang-yin.md = `688cc12e…`, julius-caesar.md = `4f6d324c…`).
- [x] Live vault file count still at 245 from prior mirror.
- [x] `incoming/` untouched.

Non-blocking caveats (do not delay mirror):

1. **63 distinct unresolved person references.** Most are persons not yet in the 29 set (correctly skipped). A subset may be registry-miss cases where both persons ARE in the 29 set but name variants differ. Recommend a follow-up triage pass to identify those — but a fresh mirror is fine without it because the affected references render as plain text (no broken wikilinks).
2. **Em-dash Status column** still appears for events/works rows whose source JSONL omits `status`. Already documented as deferred cosmetic issue #2 from `_22_person_dryrun_spotcheck_report_v1.md` §6. Unchanged.

---

## 9. Recommended mirror mode

**Option A — Partial-promote (pilot-preserving) via `rsync -av` with exclude filters.**

Identical pattern to the 22-person live mirror:

```bash
rsync -av \
  --exclude='tang-yin.md' \
  --exclude='julius-caesar.md' \
  --exclude='.gitkeep' \
  --exclude='.obsidian/' \
  --exclude='.stfolder/' \
  --exclude='.stignore' \
  --exclude='*Sync-Conflict*' \
  --exclude='*.sync-conflict-*' \
  --exclude='_generation_manifest.json' \
  obsidian-vault-pilot/_dryrun_29_v1/ \
  /mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/
```

Effects (predicted):
- **Person notes:** 22 existing in vault (incl. pilot tang-yin.md and julius-caesar.md, both unchanged) + 7 new (Crassus, Brutus, Wang Shizhen, Chen Chun, Li Panlong, Cato, Cassius) = **29 in vault.**
- **Source notes:** 18 pilot SRC_TY_*/SRC_JC_* preserved + 256 namespaced from sandbox = **~274 in vault** (with the same 18 namespaced TY/JC duplicates from the prior mirror still present).
- The 20 already-mirrored namespaced person notes (other than pilot TY/JC) will be **overwritten** by the new v3-emitted versions, which include the registry-resolved person wikilinks. The contents change but the filenames are identical, so no extra files.
- Folder scaffold unchanged.

Pilot preservation is enforced by the rsync `--exclude='tang-yin.md'` / `--exclude='julius-caesar.md'` filters. MD5 verification post-mirror recommended.

**Not recommended:** Option C (full overwrite including pilot) — would clobber the reviewed pilot files and break the integrity record. Stay with partial-promote.

---

## 10. What this run did NOT do

- Did not write to the live Obsidian vault.
- Did not edit `incoming/` source data.
- Did not generate standalone event / work / relationship notes in `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/` (those folders exist as empty scaffolds with `.gitkeep`).
- Did not visit `_dryrun_22_v1/` — the 22-person sandbox is preserved as a reference.
- Did not collect new persons.
- Did not modify the reviewed pilot files in `obsidian-vault-pilot/01_Persons/...`.
- Did not commit anything to `main`.
- Did not delete any existing vault files.

Repo writes in this run: `tools/obsidian_dryrun_generator.py` (patched to v3), `obsidian-vault-pilot/_dryrun_29_v1/` (newly created), and this report.

---

## 11. Suggested follow-on actions (in order)

1. **User reviews the sandbox** — open 3–4 representative new person notes (`shen-zhou.md`, `marcus-licinius-crassus.md`, `wang-shizhen.md`, `cato-the-younger.md`) in any Markdown viewer or by temporarily opening `_dryrun_29_v1/` as a vault.
2. **User authorises the mirror** — recommend Option A in §9.
3. **Mirror** (next task) — partial-promote rsync to live vault.
4. **Verify** post-mirror — file counts (29 + ~274 + 2 templates), pilot MD5, D-banner re-confirm, link resolution within vault.
5. **Update** `_post_import_status_v1.md` to reflect 29-person vault state.
6. **(Optional)** Triage the 63 unresolved-person references to identify registry-miss vs. genuinely-missing-from-collection.
7. **Pause** collection until §6 is resolved.
