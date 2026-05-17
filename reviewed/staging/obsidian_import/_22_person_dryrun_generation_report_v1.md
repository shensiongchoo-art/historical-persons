# 22-Person Dry-Run Generation Report v1

**Date:** 2026-05-17
**Branch:** `planning/obsidian-22-person-import-v1`
**Generator:** `tools/obsidian_dryrun_generator.py`
**Sandbox path:** `obsidian-vault-pilot/_dryrun_22_v1/`
**Predecessors:** `_22_person_import_plan_v1.md`, `_22_person_import_dry_run_v1.md`
**Live vault touched:** **NO**
**`incoming/` touched:** **NO**

This report documents the actual generator run against all 22 staging-ready person packages. Output lives in the repo sandbox only; the live Obsidian vault at `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` is unchanged.

---

## 1. Generation summary

| Metric | Count |
|--------|-------|
| Person notes generated | **22** (12 Chinese + 10 Western) |
| Source notes generated | **203** (112 Chinese + 91 Western) |
| D-level source notes with 🚫 CLUE ONLY banner | **30** |
| Files skipped | **0** |
| Filename collisions across `03_Sources/Chinese/` ∪ `03_Sources/Western/` | **0** |
| Source wikilinks across all person notes | **1,360** |
| Unresolved source wikilinks | **0** |
| YAML frontmatter parse failures across 225 generated files | **0** |
| Total files written under sandbox | **225 .md files + 11 `.gitkeep` placeholders** |

Output tree:

```
obsidian-vault-pilot/_dryrun_22_v1/
├── 00_Project/                 (.gitkeep)
├── 01_Persons/
│   ├── Chinese/                12 .md
│   └── Western/                10 .md
├── 02_Events/                  (.gitkeep)
├── 03_Sources/
│   ├── Chinese/                112 .md
│   └── Western/                91 .md
├── 04_Relationships/           (.gitkeep)
├── 05_Works/                   (.gitkeep)
├── 06_Visual_Media/            (.gitkeep)
├── 90_Staging_Review/          _generation_manifest.json
└── 99_Templates/               (.gitkeep)
```

`_generation_manifest.json` lists every output path and is committed alongside the notes for reproducibility.

---

## 2. Filename namespacing applied

Per the approved convention `{canonical_key}__{source_id}.md`, used **uniformly for all 22 persons** including the pilot persons (Tang Yin, Julius Caesar). Examples:

| Package | Sample dry-run source filename | Wikilink in person note |
|---------|--------------------------------|--------------------------|
| tang-yin | `tang-yin__SRC_TY_001.md` | `[[tang-yin__SRC_TY_001]]` |
| julius-caesar | `julius-caesar__SRC_JC_001.md` | `[[julius-caesar__SRC_JC_001]]` |
| shen-zhou (generic-ID) | `shen-zhou__SRC001.md` | `[[shen-zhou__SRC001]]` |
| wang-yangming (generic-ID) | `wang-yangming__SRC001.md` | `[[wang-yangming__SRC001]]` |
| gnaeus-pompeius-magnus (generic-ID) | `gnaeus-pompeius-magnus__SRC001.md` | `[[gnaeus-pompeius-magnus__SRC001]]` |
| qiu-ying (already-namespaced) | `qiu-ying__SRC_QY_001.md` | `[[qiu-ying__SRC_QY_001]]` |

This convention eliminates all source-ID collisions among the 8 generic-ID packages. The underlying `source_id` value inside each note's YAML frontmatter is preserved as it appears in `sources.jsonl` (e.g., `SRC001`); only the filename and wikilink form change.

---

## 3. D-level source notes (30 with 🚫 CLUE ONLY banner)

Every source where `reliability_level == "D"` OR `verification_status == "clue_only"` receives the canonical D-LEVEL banner directly below the H1, identical wording across all 30.

| Package | D-level source note filenames | Count |
|---------|-------------------------------|-------|
| cicero | `cicero__SRC_CC_007.md`, `cicero__SRC_CC_008.md` | 2 |
| cleopatra-vii | `cleopatra-vii__SRC_CL_006.md`, `cleopatra-vii__SRC_CL_007.md` | 2 |
| he-jingming | `he-jingming__SRC004.md`, `he-jingming__SRC006.md` | 2 |
| julius-caesar | `julius-caesar__SRC_JC_008.md`, `julius-caesar__SRC_JC_009.md` | 2 |
| lepidus | `lepidus__SRC004.md` | 1 |
| li-dongyang | `li-dongyang__SRC_LDY_005.md`, `li-dongyang__SRC_LDY_006.md` | 2 |
| li-mengyang | `li-mengyang__SRC_LMY_005.md`, `li-mengyang__SRC_LMY_006.md` | 2 |
| marcus-agrippa | `marcus-agrippa__SRC_MA_006.md`, `marcus-agrippa__SRC_MA_007.md` | 2 |
| octavia-minor | `octavia-minor__SRC004.md` | 1 |
| qiu-ying | `qiu-ying__SRC_QY_017.md` | 1 |
| sextus-pompey | `sextus-pompey__SRC005.md` | 1 |
| shen-zhou | `shen-zhou__SRC003.md` | 1 |
| tang-yin | `tang-yin__SRC_TY_005.md`, `tang-yin__SRC_TY_006.md` | 2 |
| wang-ao | `wang-ao__SRC003.md`, `wang-ao__SRC004.md` | 2 |
| wen-zhengming | `wen-zhengming__SRC_WZM_005.md`, `wen-zhengming__SRC_WZM_006.md` | 2 |
| wu-kuan | `wu-kuan__SRC_WK_005.md` | 1 |
| xu-zhenqing | `xu-zhenqing__SRC_XZQ_004.md`, `xu-zhenqing__SRC_XZQ_005.md` | 2 |
| zhu-yunming | `zhu-yunming__SRC_ZYM_004.md`, `zhu-yunming__SRC_ZYM_005.md` | 2 |
| **Total** | | **30** |

Validation: grep for `"D-LEVEL — CLUE ONLY"` across the 30 manifest entries returned 30 matches. **0 missing banners.**

augustus-octavian, mark-antony, wang-yangming, gnaeus-pompeius-magnus contain no `reliability_level == D` or `verification_status == clue_only` entries — confirmed at generation time.

---

## 4. Unresolved source ID collisions

**None.** The namespacing convention resolved all 8 generic-ID package collisions:

| Original generic ID | Now resolves to (per package) |
|---------------------|-------------------------------|
| `SRC001` | `shen-zhou__SRC001.md`, `wang-yangming__SRC001.md`, `gnaeus-pompeius-magnus__SRC001.md`, `wang-ao__SRC001.md`, `he-jingming__SRC001.md`, `lepidus__SRC001.md`, `octavia-minor__SRC001.md`, `sextus-pompey__SRC001.md` (8 distinct files) |
| `SRC002`–`SRC017` | Same pattern (each package gets its own namespaced file) |

Within the 203 source notes, zero basename duplicates. Each `(canonical_key, source_id)` pair is unique → each filename is unique → Obsidian wikilink resolution is unambiguous.

---

## 5. Missing source IDs / orphan references

**None.** 1,360 source wikilinks emitted across the 22 person notes; **0 unresolved**.

Specifically validated:
- Every `[[<canonical_key>__<source_id>]]` wikilink in a person note targets a file that exists in the sandbox's `03_Sources/Chinese/` or `03_Sources/Western/`.
- No `\`<source_id>\`(missing)` markers were emitted (the generator inserts that marker when a claim/relationship/event/work references an unknown `source_id` — survey already confirmed 0 such cases).

---

## 6. Skipped files

**None.** All 22 packages emitted both person notes and full source-note sets. The generator's skip rules (empty `source_id` in `sources.jsonl`) triggered 0 skips.

No package was excluded. No source within any package was excluded.

---

## 7. Dry-run Tang Yin / Julius Caesar vs reviewed pilot — structural diff

The dry-run regenerates Tang Yin and Julius Caesar **into the sandbox only**. The reviewed pilot files in `obsidian-vault-pilot/01_Persons/...` and the vault mirror are **not touched**.

### Differences observed

| Aspect | Pilot (reviewed) | Dry-run (sandbox) | Type of difference |
|--------|------------------|--------------------|---------------------|
| Total lines (Tang Yin) | 234 | 220 | Cosmetic — pilot has hand-curated narrative |
| Total lines (Caesar) | 235 | 221 | Cosmetic — pilot has hand-curated narrative |
| `## Key Historical / Reception / Legend / Fiction Separation` heading | Pilot: `## Key Historical/Legend/Fiction Separation` (TY) and `## Key Historical/Reception/Fiction Separation` (JC) | Dry-run: uniform `## Key Historical / Reception / Legend / Fiction Separation` | Wording — generator standardised |
| `## Probable / Disputed / Needs Verification Claims` section | Pilot TY: `## Probable / Disputed Claims`; Pilot JC: not present (all claims confirmed) | Dry-run: uniform `## Probable / Disputed / Needs Verification Claims` (empty section for JC since 0 probables) | Wording + uniformity |
| `## Reception / Legendary / Fictional Material` heading | Pilot JC: `## Reception / Literary / Fictional Material`; Pilot TY: `## Reception / Legendary Material` | Dry-run: uniform `## Reception / Legendary / Fictional Material` | Wording — generator standardised |
| Identity table rows | Pilot TY: includes Courtesy Name, Art Names, Ancestral Home, Primary Role | Dry-run: includes Period, Inclusion Category, omits the four pilot-narrative rows | Data source — pilot added rows from `person_profile.md` narrative; generator reads only `person_record.json` |
| Source wikilink form | Pilot: `[[SRC_TY_001]]`, `[[SRC_JC_001]]` | Dry-run: `[[tang-yin__SRC_TY_001]]`, `[[julius-caesar__SRC_JC_001]]` | Namespacing — per approved convention |
| YAML frontmatter | Pilot: includes `tags` like `ming-dynasty`, `suzhou`, `wu-school`, `painting`, `poetry`, `calligraphy`, `batch-1` and `related_people` wikilinks | Dry-run: tags reduced to `{batch}, {culture}, {period-slug}`; `related_people` derived from `relationships.jsonl` (slug-guess) | Cosmetic — pilot has richer hand-curated tags |
| Life Timeline | Pilot TY: 8 rows (bilingual narrative + dates with era info from `person_profile.md`) | Dry-run: 5 rows (from `events.jsonl` only, single-language) | Data source — pilot pulled from `person_profile.md`; generator uses `events.jsonl` strictly |
| AI-COLLECTED banner | Present | Present | Match |
| Section order | Match | Match | Match |
| Sources grouping by reliability | Match (4 buckets) | Match (4 buckets) | Match |
| D-LEVEL banner on D source notes | Present (in pilot v2 gap-fix) | Present (uniform) | Match |

### Verdict on TY/JC differences

Structurally **the dry-run conforms to the spec**: same section list, same ordering, same banners, same source-grouping. The differences are:

1. **Cosmetic heading wording** — dry-run standardises ("Probable / Disputed / **Needs Verification**", "Reception / **Legendary** / Fictional Material") for cross-person uniformity. This is an improvement for the 22-batch.
2. **Data richness** — pilot files contain hand-curated narrative (alternate name tables, bilingual timeline rows, richer tags) that the generator cannot synthesise from `incoming/` alone. The generator is faithful to the structured data; the pilot adds editorial polish.
3. **Source wikilink form** — namespaced in dry-run as instructed.

**Recommendation:** keep the reviewed pilot files untouched. The dry-run TY/JC files are diff-comparison reference only. After the 20 non-pilot persons are promoted, the pilot files remain the canonical TY/JC notes; the dry-run versions of TY/JC are discarded (or kept in `_dryrun_22_v1/` for archive).

---

## 8. Generator behaviour summary

`tools/obsidian_dryrun_generator.py` is committed in this branch. Highlights:

- Reads `incoming/<culture>/<slug>/{person_record.json, claims.jsonl, sources.jsonl, relationships.jsonl, events.jsonl, works.jsonl, open_questions.md}`. Does not read `_raw/`, does not read `README.md`, does not read `person_profile.md` (reserved for hand-curation).
- Schema-tolerant via `first_of(d, *keys)` helper — handles the field-name variations across packages (e.g. `title` vs `title_en` vs `title_zh`; `claim_text_en` vs `claim_text_zh`; `evidence_note` vs `relationship_summary_en`).
- Claim bucket mapping:
  - `confidence/status == 'confirmed'` → Confirmed bucket
  - `confidence/status ∈ {probable, disputed, needs_verification, low, high, medium}` → Probable bucket
  - `claim_type ∈ {reception_label, later_grouping_only, reception, reception_only}` → Reception bucket
  - `claim_type ∈ {legend, legendary, fiction, fictional, folklore, myth}` → Legendary bucket
  - Fallback → Probable (so reviewer never loses a claim).
- Source bucket mapping:
  - `verification_status == 'clue_only'` OR `reliability_level == 'D'` → D bucket (gets banner)
  - `reliability_level ∈ {A, A_candidate}` → A bucket
  - `reliability_level ∈ {B_high, B}` → B bucket
  - `reliability_level == 'C'` → C bucket (no banner)
- Wikilink form for source references in a person note: `[[<canonical_key>__<source_id>]]` — namespacing applied uniformly across all 22.
- Forward wikilinks to related persons: best-effort slug derived from `related_person_name`. These will resolve when the rest of the batch is imported; flagged as forward references in the person note.
- Output is regeneratable: re-running the generator wipes and rebuilds `_dryrun_22_v1/` so manual edits to the sandbox are not preserved across runs.

---

## 9. Safety checks (all passed)

| Check | Result |
|-------|--------|
| Live Obsidian vault file count unchanged | ✅ 22 files (2 person + 18 source + 2 templates) — matches gap-fix v2 state |
| Live Obsidian vault byte content unchanged on Tang Yin pilot file | ✅ (was not opened for write) |
| Live Obsidian vault byte content unchanged on Julius Caesar pilot file | ✅ (was not opened for write) |
| `incoming/` directory unchanged | ✅ (`git status incoming/` empty) |
| No `.obsidian/`, `.stfolder`, `.stignore`, or conflict files copied into repo | ✅ |
| No writes outside `obsidian-vault-pilot/_dryrun_22_v1/` and `reviewed/staging/obsidian_import/` and `tools/` | ✅ |
| Existing pilot files in `obsidian-vault-pilot/01_Persons/...` and `03_Sources/...` unchanged | ✅ (`git status` shows only sandbox + this report + generator script) |
| Generator emits to repo only — no `cp` to vault | ✅ |

---

## 10. Is the dry-run safe for human review?

**Yes.** The dry-run is safe for the user to review in the following modes (in order of preference):

1. **Direct file reading from the repo** — open files under `obsidian-vault-pilot/_dryrun_22_v1/01_Persons/` and `_dryrun_22_v1/03_Sources/` in any text/Markdown editor (VS Code, etc.). This is the safest mode — no Obsidian indexing, no vault mutation.
2. **Open the sandbox as a temporary Obsidian vault** — point Obsidian's "Open folder as vault" at `H:\…\obsidian-vault-pilot\_dryrun_22_v1\` (after copying the folder out of WSL or via a `\\wsl$\` path). Verifies graph view, wikilink resolution, banner rendering — at the cost of Obsidian creating a `.obsidian/` config inside the sandbox (which can be deleted later, or `.gitignore`'d).
3. **Copy the sandbox into a scratch folder inside the live vault** — only if you want to use your existing Obsidian instance. The sandbox lives at `01-Projects/Historical-Persons-Wiki/_dryrun_22_v1/` (a sibling of the reviewed pilot). On approval, promote contents up; on rejection, delete the sandbox folder.

The dry-run output is internally complete (all wikilinks resolve, all banners present, all YAML parses) so reviewing it in isolation will not surface false "broken link" warnings.

---

## 11. Recommendation for next step

**Recommended next action: user reviews the sandbox before any promotion.**

Specifically:
1. Open 3 representative dry-run person notes — one MVP (e.g., `shen-zhou.md`), one B1 (e.g., `cicero.md`), one B2 (e.g., `lepidus.md`) — and confirm:
   - Frontmatter is acceptable.
   - Claims grouping matches the MVP rules v2.5 disciplines.
   - Source wikilinks land on the correct namespaced source note.
   - D-LEVEL banner renders on a D-level source note (e.g., `shen-zhou__SRC003.md`).
2. Compare the dry-run `tang-yin.md` and `julius-caesar.md` against the reviewed pilot files (diff already done in §7). Confirm the differences are acceptable (or specify which pilot-richness items should be back-ported to the generator).
3. Decide on promotion mode:
   - **(A) Full promotion** — promote all 22 to `obsidian-vault-pilot/` proper, then mirror to vault. Keep pilot TY/JC files unchanged (do not overwrite); only the 20 non-pilot persons + their 203 − 18 = 185 source notes are promoted.
   - **(B) Partial promotion** — promote a subset first (e.g., one or two non-pilot persons) for a final smoke test in the live vault, then promote the rest.
   - **(C) Generator-tweak iteration** — if any differences in §7 are not acceptable, iterate the generator before any promotion.

Default recommendation: **(A) Full promotion with pilot files preserved.** All validation gates have passed; the dry-run is self-consistent; pilot files are explicitly excluded from overwrite.

---

## 12. What was NOT done (per instruction)

- Did not write to the live Obsidian vault (`/mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/`).
- Did not edit `incoming/` source data.
- Did not generate standalone event/work/relationship notes in `02_Events/`, `04_Relationships/`, `05_Works/`.
- Did not generate visual media files in `06_Visual_Media/`.
- Did not collect new persons.
- Did not promote anything to master.
- Did not modify the reviewed pilot files in `obsidian-vault-pilot/01_Persons/...` or `03_Sources/...`.
- Did not commit anything to `main`.

---

## 13. Approval gates remaining before live-vault promotion

1. ☐ User reviews sandbox sample (3 representative dry-run person notes + 1 D-level source note).
2. ☐ User confirms structural diffs in §7 are acceptable.
3. ☐ User chooses promotion mode (A / B / C in §11).
4. ☐ User authorises the live-vault mirror step.

Once all four gates pass, the next task is a one-shot promotion + mirror script run. The sandbox is ready and waiting.
