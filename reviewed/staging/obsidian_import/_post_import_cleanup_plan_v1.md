# Post-Import Cleanup Plan v1

**Date:** 2026-05-18
**Branch:** `cleanup/obsidian-post-import-v1` (off `main` after merge of PR #34 = `b00b1f8`)
**Predecessors:** `_22_person_import_plan_v1.md`, `_22_person_dryrun_generation_report_v1.md`, `_22_person_dryrun_spotcheck_report_v1.md`, `_22_person_live_mirror_report_v1.md`
**Scope:** Non-blocking cleanup items identified after the 22-person live-vault mirror. No new data collection. No standalone notes. No dashboard work. No `incoming/` edits.

This plan documents 5 remaining cleanup areas, marks which fixes are trivial-and-safe-enough to apply inline (with proof), and which require an explicit follow-on iteration with user authorisation.

---

## 1. Person wikilink slug drift

### Findings (before this PR's inline fixes)

| Location | Distinct unresolved person wikilinks | Where they appeared |
|----------|---------------------------------------|----------------------|
| **Repo dry-run** (`obsidian-vault-pilot/_dryrun_22_v1/`) | 3 | `[[gaius-julius-caesar]]` (cicero.md, cleopatra-vii.md); `[[marcus-antonius-mark-antony]]` (julius-caesar.md, dry-run version); `[[marcus-tullius-cicero]]` (julius-caesar.md, dry-run version) |
| **Live vault** (`H:\…\Historical-Persons-Wiki\`) | 2 | `[[gaius-julius-caesar]]` (cicero.md, cleopatra-vii.md); `[[marcus-antonius]]` (julius-caesar.md, **the reviewed pilot file**) |

Root cause: the generator derives forward person wikilinks from `related_person_name` via a simple slug-guess (lower + spaces→hyphens). The actual canonical filenames are the folder slugs under `incoming/` (e.g. `mark-antony`, `julius-caesar`, `cicero`), which don't match name-derived slugs like `marcus-antonius-mark-antony` or `gaius-julius-caesar`.

### Canonical link mapping

The minimum needed correction table for the current 22-person batch:

| Generated slug-guess | Canonical filename | Trivial-safe to apply? |
|----------------------|---------------------|--------------------------|
| `gaius-julius-caesar` | `julius-caesar` | ✅ Yes (no file rename, dry-run + non-pilot vault only) |
| `marcus-antonius-mark-antony` | `mark-antony` | ✅ Yes (dry-run only — pilot version is different) |
| `marcus-tullius-cicero` | `cicero` | ✅ Yes (dry-run only — pilot version is different) |
| `marcus-antonius` (pilot wording) | `mark-antony` | ⚠️ Requires user authorisation — modifies the reviewed pilot file |
| (no other unresolved links found) | | — |

### Inline fixes applied in this PR (trivial-safe)

- ✅ Repo dry-run `_dryrun_22_v1/01_Persons/Western/cicero.md`: `[[gaius-julius-caesar]]` → `[[julius-caesar]]` (2 occurrences).
- ✅ Repo dry-run `_dryrun_22_v1/01_Persons/Western/cleopatra-vii.md`: `[[gaius-julius-caesar]]` → `[[julius-caesar]]` (2 occurrences).
- ✅ Live vault `01_Persons/Western/cicero.md`: same fix.
- ✅ Live vault `01_Persons/Western/cleopatra-vii.md`: same fix.
- ✅ Repo dry-run `_dryrun_22_v1/01_Persons/Western/julius-caesar.md`: `[[marcus-antonius-mark-antony]]` → `[[mark-antony]]` and `[[marcus-tullius-cicero]]` → `[[cicero]]`.

**Post-fix unresolved count: repo dry-run = 0, live vault = 1.**

The remaining 1 link (`[[marcus-antonius]]` in the live vault's pilot `julius-caesar.md`) is **not** modified in this PR. The pilot file's MD5 remains `4f6d324c50701ae8da29a6b0899324f3`, byte-identical to its reviewed state.

### Fixes deferred (require explicit user approval)

- ⏸ **Pilot `01_Persons/Western/julius-caesar.md` in the live vault** has `[[marcus-antonius]]` in `related_people` (line 24) and the Relationships table (line 160). Changing it would alter the MD5 of a reviewed pilot file. Recommendation: ask user once, apply if approved, document with new MD5.
- ⏸ **Generator hardening** (`tools/obsidian_dryrun_generator.py`): add a `RELATED_PERSON_NAME_TO_SLUG` lookup map keyed off the 22 canonical slugs so regenerations don't reintroduce the bug. Recommended for the next generator iteration; out of scope for this cleanup PR.

---

## 2. Duplicate pilot source notes

### Findings

The live vault contains **two parallel sets** of source notes for Tang Yin and Julius Caesar:

| Pilot (preserved, originally reviewed) | Dry-run namespaced (mirrored from `_dryrun_22_v1/`) |
|----------------------------------------|-----------------------------------------------------|
| `SRC_TY_001.md` … `SRC_TY_009.md` (9 files) | `tang-yin__SRC_TY_001.md` … `tang-yin__SRC_TY_009.md` (9 files) |
| `SRC_JC_001.md` … `SRC_JC_009.md` (9 files) | `julius-caesar__SRC_JC_001.md` … `julius-caesar__SRC_JC_009.md` (9 files) |

**Total duplicate pairs: 18.**

### Cross-reference graph (which version do live notes link to?)

- Live vault `01_Persons/Chinese/tang-yin.md` (the reviewed pilot) uses **pilot-style** `[[SRC_TY_001]]` wikilinks → resolve to the pilot source notes.
- Live vault `01_Persons/Western/julius-caesar.md` (the reviewed pilot) uses **pilot-style** `[[SRC_JC_001]]` wikilinks → resolve to the pilot source notes.
- **No file in the live vault references the 18 dry-run namespaced TY/JC source notes** (verified by `grep -rn tang-yin__SRC_TY_\|julius-caesar__SRC_JC_` → 0 results across `01_Persons/`).

So the 18 namespaced duplicates are present but **unreferenced** in the vault. They appear in Obsidian's file list and graph, but no link traverses to them.

### Options and recommendation

| Option | Pros | Cons |
|--------|------|------|
| **A. Keep both** (current state) | Zero file operations needed. The namespaced versions stay as an internal-consistency artifact of the uniform `{slug}__{source_id}.md` convention. | Visual clutter in the vault file tree and graph. Two reviewers might accidentally pick the wrong version when comparing. |
| **B. Remove the 18 namespaced duplicates from the live vault** | Single set of TY/JC source notes — less confusion. Vault file count drops 221 → 203. | Breaks naming uniformity (TY/JC sources keep pilot prefix while the other 20 use namespacing). Vault behaviour differs from the repo dry-run sandbox. |
| **C. Remove the 18 pilot-style notes; the dry-run namespaced versions become canonical for TY/JC too** | Full naming uniformity in the vault. | The pilot has hand-curated wording the dry-run lacks (timing rows, alternate-name details). Would require also updating the pilot person notes' `[[SRC_TY_001]]` links to `[[tang-yin__SRC_TY_001]]`, which alters the pilot files. |
| **D. Redirect with Obsidian aliases** | Both names resolve to one file via Obsidian's `aliases:` frontmatter; no file deletion. | Adds 18 frontmatter edits + 1 alias per file. Aliases are an Obsidian convention, not a Markdown one — fragile across other tools. |

**Recommendation: B — Remove the 18 namespaced TY/JC duplicates from the live vault.** Rationale: the pilot's hand-curated wording is the better reading copy, the pilot wikilinks resolve cleanly, and the namespaced duplicates have zero inbound references. Naming uniformity is broken for TY/JC alone, which is acceptable because TY/JC are the pilot exemplars whose pilot status is documented in `_22_person_live_mirror_report_v1.md`.

**Do not delete yet.** Apply Option B in a follow-on PR after explicit user approval. The deletion is reversible from the repo sandbox at any time.

---

## 3. Cosmetic table issues

### Em-dash `—` Status column

**Findings:** 364 em-dash table cells distributed across 21 of 22 person notes. Top 5 by count:

| File | Em-dash cells |
|------|---------------|
| `mark-antony.md` | 61 |
| `augustus-octavian.md` | 48 |
| `qiu-ying.md` | 37 |
| `wu-kuan.md` | 27 |
| `cicero.md` | 23 |

Root cause: the source JSONL for these packages omits `status` / `confidence` fields on events and works rows; the generator emits `—` for missing data rather than blanking the column or hiding it.

### Options

| Option | Pros | Cons |
|--------|------|------|
| **A. Keep `—`** (current) | Honest representation — reader sees the data is absent. Generator stays simple. | Visually noisy; 364 em-dashes draw the eye. |
| **B. Replace `—` with empty cell** | Cleaner visual. | Reader can't distinguish "no data" from "data: empty string". |
| **C. Hide Status column when all rows in a table are `—`** | Best of both: clean tables, status shows when meaningful. | Generator complexity — needs a two-pass per-table check. |
| **D. Backfill the source JSONL** with explicit status values | Resolves the issue at the source data layer. | Edits `incoming/` — **out of scope per project rules**. |

**Recommendation: defer to a generator v3 iteration with Option C (auto-hide all-em-dash columns).** Non-blocking; readers can already filter or ignore the column.

Do not apply changes in this PR.

### Other minor cosmetic items not requiring action now

- Long Open Questions sections (already demoted to H3 in generator v2). No further action.
- Generic forward wikilinks (e.g., `[[周臣]]`, `[[zhou-chen]]`) for people not in the 22-person batch — expected and unresolved by design.

---

## 4. Relationship / event / work standalone notes

**Status: not generated.** The vault folders `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/` exist as empty scaffolds (placeholders only).

### Why defer

1. **Link-normalization must come first.** Standalone event/work notes would create more cross-link references that depend on consistent slugs. Generating them before §1 (link drift) is fully resolved would lock in additional drift.
2. **Cross-person value not yet realised.** Standalone notes pay off most when multiple persons share the same event (e.g., Battle of Actium, First Triumvirate) or work. The current source data doesn't have a global `event_id` schema — events are person-scoped. A reconciliation pass is required to merge cross-person events (defer to a separate task, post-link-normalization).
3. **No reviewer ask yet.** The current vault already has events embedded in person notes' Life Timeline tables, works in the Works tables, and relationships in the Relationships tables. Standalone notes are an enhancement, not a fix.

### Recommendation

- **Do not generate** any files in `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/` in this cleanup pass.
- Open a separate planning task **after** issues #1 (link drift), #2 (duplicates), and #3 (cosmetic) are resolved and the user has reviewed the cleaned-up state.

---

## 5. Obsidian vault sync safety

### Scan results

| Check | Result |
|-------|--------|
| OneDrive `*Sync-Conflict*` files anywhere under `01-Projects/Historical-Persons-Wiki/` | ✅ **0** found |
| Syncthing `*.sync-conflict-*` files under the project folder | ✅ **0** found |
| `.obsidian/`, `.stfolder/`, `.stignore` inside the project folder | ✅ **0** (correctly absent — they live at the vault root only) |
| Vault-root `.obsidian/`, `.stfolder`, `.stignore` (must be PRESENT and untouched) | ✅ All 3 present at `/mnt/h/OneDrive/obsidian-vault/` (vault root); not modified |
| Tang Yin pilot file MD5 (must match pre-mirror) | ✅ `688cc12e0baacf706e51d1b6deb582d5` unchanged |
| Julius Caesar pilot file MD5 (must match pre-mirror) | ✅ `4f6d324c50701ae8da29a6b0899324f3` unchanged |
| `incoming/` directory modified | ✅ `git status incoming/` empty |
| PARA folders outside the project (`00-Inbox/`, `02-Areas/`, etc.) | ✅ untouched (mirror scope was limited to `01-Projects/Historical-Persons-Wiki/`) |

**No sync-safety issues found.** The mirror operation was correctly scoped and the partial-promote exclusions worked as intended.

### Recommendation

- No action needed in this PR.
- Optional ongoing monitoring: re-run the `*Sync-Conflict*` / `*.sync-conflict-*` scan after any future vault sync cycle, especially before further generator runs. A one-liner check fits in any future automation step.

---

## 6. Summary of fixes applied in this PR (cleanup v1)

| # | Item | Fix scope | File / location | Reversible? |
|---|------|-----------|------------------|--------------|
| 1 | Link drift `[[gaius-julius-caesar]]` → `[[julius-caesar]]` | Repo dry-run | `_dryrun_22_v1/01_Persons/Western/cicero.md` | Yes — `sed` reverse |
| 2 | Same fix | Repo dry-run | `_dryrun_22_v1/01_Persons/Western/cleopatra-vii.md` | Yes |
| 3 | Same fix | Live vault | `01_Persons/Western/cicero.md` | Yes |
| 4 | Same fix | Live vault | `01_Persons/Western/cleopatra-vii.md` | Yes |
| 5 | Link drift `[[marcus-antonius-mark-antony]]` → `[[mark-antony]]` | Repo dry-run | `_dryrun_22_v1/01_Persons/Western/julius-caesar.md` (dry-run version, NOT pilot) | Yes |
| 6 | Link drift `[[marcus-tullius-cicero]]` → `[[cicero]]` | Repo dry-run | same file as #5 | Yes |

All 6 fixes are trivial-safe regex replacements with no semantic change beyond resolving the wikilink target. The pilot file in the vault (`julius-caesar.md`) is NOT modified — its `[[marcus-antonius]]` link remains unresolved by intent.

---

## 7. Fixes proposed for follow-on PRs (not applied here)

| Item | Why deferred | Suggested PR title |
|------|--------------|---------------------|
| Modify pilot vault `julius-caesar.md`: `[[marcus-antonius]]` → `[[mark-antony]]` | Modifies a reviewed pilot file; requires explicit user authorisation | `pilot: update marcus-antonius wikilink → mark-antony` |
| Delete 18 namespaced TY/JC duplicate source notes from live vault | Visual-clutter cleanup; recommendation §2 Option B | `vault: deduplicate TY/JC namespaced source notes` |
| Generator v3 — add `RELATED_PERSON_NAME → CANONICAL_SLUG` lookup map | Prevents regression of link drift on future regenerations | `generator: add name→slug lookup table` |
| Generator v3 — auto-hide Status column when all rows are `—` | Cosmetic; reduces visual noise across 364 cells | (same PR as above) |
| Phase D — generate standalone event/work/relationship notes | Wait until link normalization is done | `phase-d: generate standalone notes` |

---

## 8. Acceptance gates before any of §7 proceeds

1. ☐ User opens the live vault in Obsidian and confirms the trivial fixes applied here have not visually disrupted anything.
2. ☐ User decides yes/no on modifying the pilot vault `julius-caesar.md` wikilink (recommendation: yes — accept the trivial pilot edit so vault is link-clean).
3. ☐ User decides yes/no on Option B (delete namespaced TY/JC duplicates).
4. ☐ User confirms generator v3 work is in scope before any regeneration / re-mirror.

This cleanup plan is non-blocking. The vault is functionally usable now.

---

## 9. What this PR does NOT do

- Does not generate any new person, source, event, work, relationship, or visual-media notes.
- Does not modify `incoming/` source data.
- Does not promote anything to master.
- Does not build dashboards or UI features.
- Does not modify the pilot `julius-caesar.md` or `tang-yin.md` files (MD5-verified unchanged).
- Does not delete any vault files.
- Does not patch the generator script.
- Does not touch `.obsidian/`, `.stfolder`, `.stignore`, or any sync-conflict file.
- Does not write outside `obsidian-vault-pilot/_dryrun_22_v1/` and `reviewed/staging/obsidian_import/` on the repo side, or `01-Projects/Historical-Persons-Wiki/01_Persons/Western/cicero.md` and `cleopatra-vii.md` on the vault side.
