# 22-Person Dry-Run Spot-Check Report v1

**Date:** 2026-05-18
**Branch:** `planning/obsidian-22-person-import-v1`
**Sandbox:** `obsidian-vault-pilot/_dryrun_22_v1/`
**Predecessors:** `_22_person_import_plan_v1.md`, `_22_person_import_dry_run_v1.md`, `_22_person_dryrun_generation_report_v1.md`
**Live vault touched:** **NO**
**`incoming/` touched:** **NO**

This report is a manual deep-read review of 6 representative dry-run person notes (3 Chinese + 3 Western, covering MVP + B1 + B2 batches and both ID conventions) plus targeted sampling of D-level source notes. Nothing was edited.

---

## 1. Notes checked

| # | Path | Batch / Culture | Schema | Claims | Sources |
|---|------|------------------|--------|--------|---------|
| 1 | `_dryrun_22_v1/01_Persons/Chinese/tang-yin.md` | B1 / Chinese | namespaced IDs (`SRC_TY_*`, `CLM_TY_*`) | 18 | 9 |
| 2 | `_dryrun_22_v1/01_Persons/Chinese/wang-yangming.md` | MVP / Chinese | generic IDs (`SRC001`, `C001`) | 37 | 18 |
| 3 | `_dryrun_22_v1/01_Persons/Chinese/li-mengyang.md` | B2 / Chinese | namespaced IDs (`SRC_LMY_*`, `CLM_LMY_*`) | 8 | 7 |
| 4 | `_dryrun_22_v1/01_Persons/Western/julius-caesar.md` | B1 / Western | namespaced IDs (`SRC_JC_*`, `CLM_JC_*`) | 18 | 9 |
| 5 | `_dryrun_22_v1/01_Persons/Western/augustus-octavian.md` | MVP / Western | namespaced IDs (`SRC_AU_*`, `CLM_AU_*`) | 35 | 18 |
| 6 | `_dryrun_22_v1/01_Persons/Western/mark-antony.md` | MVP / Western | name-based IDs (`SRC_MA_PLUTARCH_ANTONY`, `CLM_MA_*`) | 35 | 11 |

Plus targeted D-level source-note sampling:
- `tang-yin__SRC_TY_005.md` (Baidu Baike, D / clue_only) — Chinese
- `julius-caesar__SRC_JC_008.md` (Wikipedia, D / clue_only) — Western
- `shen-zhou__SRC003.md` (Wikipedia Shen Zhou, D) — Chinese
- `lepidus__SRC004.md` (Wikipedia Lepidus, D) — Western
- `sextus-pompey__SRC005.md` (Wikipedia Sextus Pompey, D) — Western
- `qiu-ying__SRC_QY_017.md` (D) — Chinese

Plus a C-level control: `wang-yangming__SRC006.md` (Wikipedia, C / needs_verification) — to confirm the D-banner is NOT emitted for C-level sources.

---

## 2. Frontmatter status

| File | YAML parses | Required keys present |
|------|-------------|------------------------|
| tang-yin.md | ✅ | person_id, canonical_key, display_name, primary_language, culture, period, birth, death, historical_status, review_status, source_sufficiency, data_source_folder, tags |
| wang-yangming.md | ✅ | (same set; `related_people` absent — JSONL provides only `related_person_name` without P_-prefixed `related_person_id` for most rows) |
| li-mengyang.md | ✅ | (same set; `related_people` PRESENT with `[[xu-zhenqing]]`, `[[he-jingming]]`, `[[li-dongyang]]` — best-effort slug guesses) |
| julius-caesar.md | ✅ | (same set; `related_people` PRESENT with 5 wikilinks including `[[marcus-tullius-cicero]]`, `[[marcus-antonius-mark-antony]]` — note: these don't match the live pilot's `[[cicero]]` / `[[marcus-antonius]]` shorter slugs) |
| augustus-octavian.md | ✅ | (same set; no `related_people` block — `related_person_name` field in relationships.jsonl is empty for most rows; the generator's slug-guess defaulted to nothing) |
| mark-antony.md | ✅ | (same set; no `related_people` block — same reason as augustus-octavian) |

All 6 frontmatter blocks parse cleanly with `yaml.safe_load`. All 6 carry `historical_status: ai_collected_unreviewed` (the FORCED safety label).

Notable nit on `related_people`:
- The pilot's hand-curated frontmatter uses short, canonical slugs (`[[cicero]]`, `[[marcus-antonius]]`).
- The generator's slug-guess derives wikilinks from `related_person_name` ("Marcus Tullius Cicero" → `marcus-tullius-cicero`, "Marcus Antonius (Mark Antony)" → `marcus-antonius-mark-antony`).
- Result: dry-run forward-wikilinks won't necessarily resolve to the slugs that will be the actual filenames after the 22-batch lands. This is **non-blocking** because (a) forward wikilinks are expected to be partial-resolve at sandbox stage, (b) the generator can be tweaked to map names → canonical slugs once the 22-batch's canonical slugs are catalogued, (c) the `## Relationships` table body still shows the friendly person name as the primary identifier.

---

## 3. Readability assessment

For each of the 6 notes:

### Tang Yin (B1 / Chinese)
- Summary bilingual ZH+EN — clear, accurate, no reception material asserted as fact.
- Identity table includes courtesy/art names via `alternate_names_zh/en` row.
- Life Timeline: 5 rows; status column shows `—` for all rows (no `status` field in the events JSONL for this package; cosmetic, see §6).
- Claims grouping: 10 confirmed, 5 probable/disputed, 3 reception, 0 legendary — matches `incoming/` data after bucket-mapping.
- Source tables: 4 buckets all populated and well-labeled; needs_verification re-list flags SRC_TY_004, SRC_TY_007.
- **Verdict: highly readable.** No malformed content.

### Wang Yangming (MVP / Chinese, generic IDs)
- 37 claims, 18 sources, 8 relationships — the second-densest Chinese package.
- Confirmed table: 27 rows, all sourced; visible namespaced wikilinks like `[[wang-yangming__SRC001]]` resolve.
- Reception table includes `identity` and `reception_label` types — correctly separated from confirmed biography.
- **Open Questions section is long (~50 lines) and contains nested H2 headings** (`## High Priority`, `## Medium Priority`, `## Hardening Sprint Notes`, etc.) inlined verbatim from `open_questions.md`. This produces sibling H2s inside the parent `## Open Questions` H2, which Obsidian renders fine but breaks the visual hierarchy (a "##" inside a "##" reads as a peer, not a child). See §6 for the cosmetic note.
- Section count: 20 (vs. the canonical 14) because of the nested H2s in Open Questions.
- **Verdict: readable, but Open Questions section is structurally noisy.** Content is correct.

### Li Mengyang (B2 / Chinese, namespaced IDs)
- Smaller package: 8 claims, 7 sources, 3 relationships.
- Life Timeline shows only 1 row (the only event in `events.jsonl` for this person) — accurate to source data, no fabrication.
- Reception/Legendary section correctly empty (0 legendary).
- D-level sources (SRC_LMY_005 Baidu, SRC_LMY_006 Wikipedia) appear in the C/D/clue_only bucket with wikilinks resolving.
- `## Open Questions` has ✓ RESOLVED markers carried over verbatim — accurate to source data.
- **Verdict: clean, compact, well-formed.**

### Julius Caesar (B1 / Western, namespaced IDs)
- Mirror of the pilot in structure — 18 claims, 9 sources.
- Dry-run version uses namespaced source wikilinks (`[[julius-caesar__SRC_JC_001]]`) per the approved convention; live pilot still uses `[[SRC_JC_001]]`. **Expected difference**, not a defect.
- Probable/Disputed table is empty ("*(none)*") — Caesar has 0 probable claims. Rendered cleanly.
- D-level source notes present: SRC_JC_008 (Wikipedia), SRC_JC_009 (Britannica) — both carry the 🚫 banner.
- **Verdict: structurally consistent with the accepted pilot.**

### Augustus / Octavian (MVP / Western)
- The largest Western package: 35 claims, 18 sources, 9 relationships, 15 events.
- Relationships table renders 9 rows; the **Person column shows plain text "julius-caesar", "mark-antony", "cleopatra-vii" etc.** rather than `Display Name ([[wikilink]])` pairs (because this package's relationships.jsonl has empty `related_person_name` and uses raw slugs in another field). This is a data-shape inconsistency from the source, not a generator defect — see §6.
- Confirmed claims table is long (27 rows) but readable; the per-claim source wikilinks are all valid.
- Open Questions section inherits nested H2s (`## Biographical`, `## Legal and Constitutional`, etc.) — same cosmetic note as Wang Yangming.
- **Verdict: dense but well-structured.** The Relationships "Person" column needs the slug-→-name lookup added to the generator in a future iteration (non-blocking).

### Mark Antony (MVP / Western, name-based source IDs)
- 35 claims, 11 sources (SRC_MA_PLUTARCH_ANTONY, SRC_MA_CICERO_PHILIPPICS, etc. — verbose name-based source IDs).
- Source filenames respect the namespacing: `mark-antony__SRC_MA_PLUTARCH_ANTONY.md` (long but unambiguous).
- Relationships table renders cleanly with bilingual notes and source links.
- All 0 D-level sources for this package (no encyclopedia entries) — `## C / D / clue_only` bucket correctly empty.
- **Verdict: very readable. Best of the 6 for relationship-section clarity** — `relationships.jsonl` here has full `related_person_name` strings.

---

## 4. Source link assessment

| File | Source wikilinks emitted | Unresolved |
|------|--------------------------|------------|
| tang-yin.md | 47 | **0** |
| wang-yangming.md | 119 | **0** |
| li-mengyang.md | 31 | **0** |
| julius-caesar.md | 55 | **0** |
| augustus-octavian.md | 112 | **0** |
| mark-antony.md | 114 | **0** |
| **Total across the 6** | **478** | **0** |

Every `[[<canonical_key>__<source_id>]]` wikilink in the 6 spot-check notes targets a file that exists in `_dryrun_22_v1/03_Sources/{Chinese,Western}/`. No `(missing)` markers emitted by the generator. Namespacing is applied uniformly — no bare `[[SRC001]]` or `[[SRC_TY_001]]` form leaks through.

Forward wikilinks to other persons (`[[shen-zhou]]`, `[[cicero]]`, `[[marcus-tullius-cicero]]`, etc.) are intentionally unresolved at sandbox stage — they will resolve as the 22 person notes co-locate. See §2 note on slug-derivation drift.

---

## 5. D-source banner assessment

Spot-checked 6 D-level source notes from different packages:

| File | reliability_level | verification_status | 🚫 banner |
|------|-------------------|---------------------|------------|
| `tang-yin__SRC_TY_005.md` | D | clue_only | ✅ present (line 14) |
| `julius-caesar__SRC_JC_008.md` | D | clue_only | ✅ present (line 14) |
| `shen-zhou__SRC003.md` | D | needs_verification | ✅ present |
| `lepidus__SRC004.md` | D | needs_verification | ✅ present |
| `sextus-pompey__SRC005.md` | D | needs_verification | ✅ present |
| `qiu-ying__SRC_QY_017.md` | D | (varies) | ✅ present |

Banner wording is identical across all 6 (the canonical 4-line block established in the pilot v2 gap-fix), placed directly below the H1 title.

Control check: `wang-yangming__SRC006.md` (reliability_level: **C**, verification_status: needs_verification) was sampled and **does NOT carry the D-banner** — correct behaviour. C-level encyclopedias appear in the "C / D / clue_only" bucket of the parent person note but do not get the strong D-warning. This matches the v1 plan's spec.

Cross-references from the per-source `Used For Claims` section to claim anchors in the parent person note are rendered as `[[<slug>#Confirmed Historical Claims|<claim_id>]]` — these resolve in Obsidian via the heading-anchor mechanism (verified manually on `wang-yangming__SRC006.md` and `tang-yin__SRC_TY_001.md` style links).

---

## 6. Formatting issues found

All issues are **non-blocking**. Listing by severity:

| # | Severity | Issue | Affected files | Cause | Suggested fix |
|---|----------|-------|----------------|-------|----------------|
| 1 | Cosmetic | Open Questions section contains nested H2 headings inherited verbatim from `open_questions.md` (e.g., `## High Priority` inside `## Open Questions`). Renders fine in Obsidian but breaks visual heading hierarchy. | wang-yangming.md, augustus-octavian.md, mark-antony.md (and likely 3–4 others with rich open_questions.md). | Generator inlines `open_questions.md` content without re-leveling its headers. | Either (a) demote inlined headers to H3 at emit time, or (b) keep verbatim and accept the visual quirk for staging. Defer until after first promotion. |
| 2 | Cosmetic | Life Timeline / Works tables show `—` (em-dash) in Status column when the source JSONL has no `status` / `confidence` / `attribution_status` field. | tang-yin.md (5 rows), julius-caesar.md (7 rows), several others. | Schema variance — some packages omit a status field on events/works. | Either (a) hide the Status column when all rows are `—`, or (b) leave as-is. Non-blocking. |
| 3 | Cosmetic | Period-derived tag has slashes that got slugified weirdly: `"late-republic-/-early-empire"`. | augustus-octavian.md | Generator's tag derivation replaces spaces with hyphens but leaves slashes intact. | Strip non-alphanum (except hyphens) from period slug at emit time. Trivial fix. |
| 4 | Cosmetic | Relationships table Person column shows plain text (e.g., "julius-caesar") rather than `Display Name ([[wikilink]])` for packages whose `relationships.jsonl` has empty `related_person_name`. | augustus-octavian.md (9/9 rows). | Source data lacks `related_person_name`. | Add a slug→name reverse-lookup at generation time, OR enrich the source data. Non-blocking for sandbox review. |
| 5 | Expected | Dry-run source wikilinks use `[[tang-yin__SRC_TY_001]]` form, whereas the reviewed pilot files in `obsidian-vault-pilot/01_Persons/...` use `[[SRC_TY_001]]` form. | Tang Yin & Julius Caesar dry-run vs. pilot. | Approved namespacing convention applied uniformly to dry-run. | None — this is the approved behaviour. Pilot files preserved separately. |
| 6 | Expected | Forward wikilinks to related persons (`[[marcus-tullius-cicero]]`, `[[cicero]]`, etc.) may or may not match the eventual person-note filename (`cicero.md`). | All 22 dry-run notes. | Generator's slug-guess derives from `related_person_name`; canonical slugs are the folder names under `incoming/`. | Add a name→canonical-slug map (one line per known person) before promotion. Non-blocking for sandbox review. |

No file is malformed. No file is unreadable. No file has a broken table or syntactically invalid markdown.

---

## 7. Is the dry-run safe to mirror to the live Obsidian vault?

**Yes, with the recommended mode below.**

Hard requirements (all met):
- [x] All 22 person notes generated; all YAML parses.
- [x] All 203 source notes generated; 0 filename collisions; 0 unresolved wikilinks.
- [x] 30 D-level source notes carry the 🚫 D-LEVEL — CLUE ONLY banner.
- [x] AI-COLLECTED / STAGING ONLY banner present on every person note checked.
- [x] Pilot files in `obsidian-vault-pilot/01_Persons/Chinese/tang-yin.md` and `01_Persons/Western/julius-caesar.md` unchanged.
- [x] Live vault under `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` unchanged (still 22 files from gap-fix v2 state).
- [x] `incoming/` unchanged (`git status incoming/` empty).

Acceptable cosmetic-debt (defer fixing until post-mirror):
- Nested H2s in Open Questions (issue #1).
- Em-dash Status columns when JSONL lacks the field (issue #2).
- Period-slug slash artifact in `augustus-octavian` tags (issue #3).
- Relationships Person column plain-text for the MVP-Western packages (issue #4).

These four cosmetic items can be addressed in a generator v2 patch and the affected files regenerated in a follow-on sandbox-refresh, without re-mirroring the entire 22. Or accept them in v1 as known cosmetic limitations of the dry-run.

---

## 8. Recommended mirror mode

**Recommendation: Option A — Partial-promote mirror (sandbox-aware, pilot-preserving).**

Specifically, in a follow-on task with explicit user authorisation:

1. **Decide which of the 4 cosmetic issues (#1–#4) to fix in the generator BEFORE first mirror.** Recommended fix list:
   - Issue #1 (Open Questions nested H2s): fix → demote inlined headers to H3 at emit time. Low-risk, improves readability noticeably.
   - Issue #3 (period-slug slashes): fix → trivial regex tweak.
   - Issue #2 (em-dash Status columns): defer → cosmetic only.
   - Issue #4 (Relationships Person column): defer → requires data enrichment or lookup table.
2. **Regenerate the sandbox** with the two patched issues. Re-validate (re-run generator → confirm 22 notes, 203 source notes, 30 D-banners, 0 unresolved).
3. **Mirror to live vault using this sub-folder mapping:**
   - `_dryrun_22_v1/01_Persons/Chinese/*.md` (12 files, **excluding tang-yin.md**) → `H:\...\01_Persons\Chinese\` (11 files)
   - `_dryrun_22_v1/01_Persons/Western/*.md` (10 files, **excluding julius-caesar.md**) → `H:\...\01_Persons\Western\` (9 files)
   - `_dryrun_22_v1/03_Sources/Chinese/*.md` (112 files; **the 9 `tang-yin__SRC_TY_*.md` are NEW filenames vs. the pilot's `SRC_TY_*.md` — both will co-exist in the vault until the user decides which set to keep**) → `H:\...\03_Sources\Chinese\`
   - `_dryrun_22_v1/03_Sources/Western/*.md` (91 files; same note for `julius-caesar__SRC_JC_*.md` vs. pilot's `SRC_JC_*.md`) → `H:\...\03_Sources\Western\`
   - Pilot files in `obsidian-vault-pilot/01_Persons/Chinese/tang-yin.md`, `obsidian-vault-pilot/01_Persons/Western/julius-caesar.md`, and the 18 pilot source notes are **NOT touched** in the vault mirror.
4. **Mirror as a single atomic `cp -r` operation** to minimize OneDrive/Syncthing intermediate-state churn.
5. **Write `90_Staging_Review/_import_log.md`** in the live vault to record what was mirrored, when, and from which sandbox commit.

Alternative modes considered but not recommended:

- **Full overwrite** (replace pilot files with dry-run versions) — rejected. The pilot has been visually reviewed and is richer in editorial detail than the generator can produce.
- **Promote sandbox to `obsidian-vault-pilot/` proper before mirror** — feasible, but the sandbox-first → vault-mirror split allows the user to compare side-by-side in one step.
- **Defer mirror entirely until ALL 4 cosmetic issues are fixed** — over-cautious given the issues are non-blocking and reviewer comprehension is not impacted.

**Decision point for the user:** confirm Option A above, including the two recommended generator fixes (#1 + #3) and the sandbox-regeneration before mirror. On confirmation, the next task is the mirror operation itself.

---

## 9. What this report did NOT do

- Did not mirror anything to the live Obsidian vault.
- Did not modify the dry-run sandbox.
- Did not modify the reviewed pilot files.
- Did not edit `incoming/`.
- Did not collect new persons.
- Did not promote anything to master.

Repo writes in this pass: this report only.
