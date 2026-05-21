# 29-Person Live Vault Mirror Report v1

**Date:** 2026-05-21
**Branch:** `mirror/obsidian-29-person-v1` (PR #42)
**Generator:** `tools/obsidian_dryrun_generator.py` (v3 — person-registry resolution)
**Sandbox source:** `obsidian-vault-pilot/_dryrun_29_v1/`
**Live vault destination:** `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` (WSL: `/mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/`)
**Mirror mode:** Partial-promote (pilot-preserving) via `rsync -av` with exclude filters.
**Status:** ✅ Mirror complete and validated. Live vault now reflects 29 persons.

---

## 1. Mirror mode used

**Option A — Partial-promote, pilot-preserving.** Identical pattern to the 22-person mirror (2026-05-18) for continuity.

Command actually executed:

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

`rsync` total: 782,201 bytes sent · 5,464 bytes received · 759,445 bytes total payload · single pass · no errors.

---

## 2. Files copied

| Category | Count | Notes |
|----------|-------|-------|
| Person notes copied or updated | **27** | 20 existing dry-run-style notes overwritten in-place with v3-emitted versions; 7 new (Crassus, Brutus, Wang Shizhen, Chen Chun, Li Panlong, Cato, Cassius). Excludes pilot tang-yin.md and julius-caesar.md. |
| Source notes copied or updated | **256** | All namespaced `{slug}__{source_id}.md`. 203 overwritten in-place, 53 new from the 7 new packages. |
| Folder scaffold | 9 dirs | All present idempotently. |

Total payload: ~283 file-level operations (mostly idempotent rewrites — same filename, refreshed content).

---

## 3. Files intentionally excluded

| File / pattern | Reason |
|----------------|--------|
| `01_Persons/Chinese/tang-yin.md` (sandbox) | Preserve reviewed pilot file (MD5 verified) |
| `01_Persons/Western/julius-caesar.md` (sandbox) | Preserve reviewed pilot file (MD5 verified) |
| `.gitkeep` placeholders | Vault is not git-tracked |
| `_generation_manifest.json` | Repo-only metadata |
| `.obsidian/`, `.stfolder/`, `.stignore` | Vault sync/config; must never be overwritten |
| `*Sync-Conflict*`, `*.sync-conflict-*` | Defensive — sync conflict files must not propagate |

The reviewed Tang Yin and Julius Caesar pilot **source notes** (`SRC_TY_001`–`009`, `SRC_JC_001`–`009`, 18 files) were NOT in the exclude list. They have different filenames from the namespaced dry-run versions, so both sets continue to co-exist as before. See §6.

---

## 4. Live vault destination

`H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\`
WSL path: `/mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/`

---

## 5. Final counts (post-mirror, verified)

| Metric | Pre-mirror | Post-mirror | Delta |
|--------|------------|--------------|-------|
| Total person notes | 22 | **29** | +7 |
| Person notes (Chinese) | 12 | **15** | +3 (Wang Shizhen, Chen Chun, Li Panlong) |
| Person notes (Western) | 10 | **14** | +4 (Crassus, Brutus, Cato, Cassius) |
| Total source notes | 221 | **274** | +53 |
| Source notes (Chinese) | 121 | **142** | +21 |
| Source notes (Western) | 100 | **132** | +32 |
| Template notes | 2 | 2 | 0 |
| Total `.md` files under project folder | 245 | **305** | +60 |

The vault file-tree is now in sync with the 29-person staging set.

---

## 6. Source note duplication update

The vault continues to hold **two parallel sets** of source notes for Tang Yin and Julius Caesar (carried over from the 22-person mirror):

| Pilot (preserved) | Dry-run namespaced (refreshed this run) |
|-------------------|------------------------------------------|
| `SRC_TY_001.md` … `SRC_TY_009.md` (9 files) | `tang-yin__SRC_TY_001.md` … `tang-yin__SRC_TY_009.md` (9 files) |
| `SRC_JC_001.md` … `SRC_JC_009.md` (9 files) | `julius-caesar__SRC_JC_001.md` … `julius-caesar__SRC_JC_009.md` (9 files) |

The preserved pilot person notes use bare `[[SRC_TY_001]]` wikilinks → these resolve to the pilot source notes. The 18 namespaced duplicates have **0 inbound references** in the vault. This is the same state as after the 22-person mirror — no change.

A future cleanup PR can delete the 18 namespaced duplicates if visual clutter becomes a problem (Option B from `_post_import_cleanup_plan_v1.md` §2). Not blocking.

---

## 7. D-level banner count

**42 source notes in the live vault carry the 🚫 D-LEVEL — CLUE ONLY banner.**

Composition:
- 38 newly mirrored / refreshed from the v3 sandbox (all 38 verified present and banner-confirmed)
- 4 pre-existing pilot (`SRC_TY_005`, `SRC_TY_006`, `SRC_JC_008`, `SRC_JC_009`) — still present, still banner-confirmed

0 missing banners across all 42.

---

## 8. Unresolved link counts

### Source wikilinks: **0 unresolved**

| Metric | Value |
|--------|-------|
| Total source wikilinks scanned in live vault person notes | 1,733 |
| Unresolved | **0** |

### Person wikilinks: **2 unresolved** — both in the preserved pilot

| Metric | Value |
|--------|-------|
| Total person wikilinks scanned in live vault | 207 |
| Unresolved | **2** |

The 2 unresolved person wikilinks are:

- `julius-caesar.md` line 24: `"[[marcus-antonius]]"` (in `related_people:` frontmatter)
- `julius-caesar.md` line 160: `[[marcus-antonius]]` (in Relationships table body)

These are **both in the preserved pilot `julius-caesar.md`** — the same documented item from `_post_import_cleanup_plan_v1.md` §1 that requires explicit user approval to modify. Modifying them would alter the pilot's MD5.

**0 unresolved person wikilinks in any of the 27 newly mirrored / refreshed person notes.** The v3 generator's registry-based resolution worked end-to-end: every `[[<slug>]]` link in the new content resolves to a real person note in the vault.

---

## 9. Pilot preservation verification

✅ **Both pilot person notes are byte-identical to their pre-mirror state.**

| File | Pre-mirror MD5 | Post-mirror MD5 | Preserved? |
|------|------------------|------------------|-------------|
| `01_Persons/Chinese/tang-yin.md` | `688cc12e0baacf706e51d1b6deb582d5` | `688cc12e0baacf706e51d1b6deb582d5` | ✅ |
| `01_Persons/Western/julius-caesar.md` | `4f6d324c50701ae8da29a6b0899324f3` | `4f6d324c50701ae8da29a6b0899324f3` | ✅ |

All 18 pilot source notes (`SRC_TY_001`–`009`, `SRC_JC_001`–`009`) are also still present and intact. The `rsync` exclude filters for the pilot files worked correctly.

---

## 10. Safety checks (all passed)

| Check | Result |
|-------|--------|
| `.obsidian/` copied into project folder | ✅ 0 |
| `.stfolder/` copied | ✅ 0 |
| `.stignore` copied | ✅ 0 |
| `.gitkeep` copied | ✅ 0 (excluded by rsync) |
| OneDrive `*Sync-Conflict*` files | ✅ 0 in project folder |
| Syncthing `*.sync-conflict-*` files | ✅ 0 in project folder |
| `_generation_manifest.json` leaked into vault | ✅ 0 (excluded) |
| `incoming/` directory modified | ✅ `git status incoming/` empty |
| Vault root `.obsidian/`, `.stfolder`, `.stignore` modified | ✅ Untouched (live at vault root only) |
| Other PARA folders in vault (`00-Inbox/`, `02-Areas/`, etc.) | ✅ Untouched (mirror scope was limited to `01-Projects/Historical-Persons-Wiki/`) |
| Pilot file MD5s | ✅ Both unchanged §9 |
| Pre-mirror vs. post-mirror total file count | 245 → 305 (delta = +60) |

---

## 11. Remaining warnings

| # | Severity | Description | Status |
|---|----------|-------------|---------|
| 1 | Documented | Preserved pilot `julius-caesar.md` still has `[[marcus-antonius]]` (2 occurrences) — modifying would alter pilot MD5 | Carried over from `_post_import_cleanup_plan_v1.md` §1; requires explicit user approval |
| 2 | Info | 18 duplicate TY/JC namespaced source notes in vault (0 inbound references) | Carried over; optional cleanup |
| 3 | Info | 134 unresolved person *references* in the dry-run manifest (63 distinct names) — rendered as plain text in Relationships tables, NOT as broken wikilinks. Most are persons not yet in the 29-person set. | Documented in `_29_person_dryrun_generation_report_v1.md` §6; non-blocking |
| 4 | Cosmetic (deferred) | Em-dash `—` Status column where source JSONL lacks the field | Unchanged since 22-person mirror |
| 5 | Cosmetic (deferred) | Augustus + Mark-Antony Relationships row formatting for related-persons whose JSONL lacks `related_person_name` | Unchanged |
| 6 | Info | OneDrive + Syncthing will propagate ~283 file operations to other devices over the next sync cycle | Expected; monitor for sync conflicts on first open |

No blocking items.

---

## 12. Is the live Obsidian vault ready for human review?

**✅ Yes.**

Open Obsidian → navigate to `01-Projects/Historical-Persons-Wiki/`. All 29 person notes are accessible with link-clean cross-references (the only 2 unresolved person wikilinks are in the preserved pilot, with the trade-off documented).

### Suggested review path

1. Open `01_Persons/Chinese/wang-shizhen.md` — first of the newly mirrored Chinese persons; verify v3 generator output renders correctly.
2. Open `01_Persons/Western/marcus-licinius-crassus.md` — Batch 3 western package; sample of the v3 person-link resolution.
3. Open `01_Persons/Western/cato-the-younger.md` — Batch 4 western package.
4. Click a `[[<slug>__SRC_xx>]]` source link in any of them — verify the D-LEVEL banner shows immediately for any D-level source.
5. Click a forward person wikilink like `[[julius-caesar]]` — verify it now resolves cleanly (no more `[[marcus-tullius-cicero]]` slug-guesses).
6. Toggle Obsidian Graph View — should show 29 person nodes with dense source clusters around each, plus the cross-person link edges resolving to real targets.
7. Open `01_Persons/Chinese/tang-yin.md` and `01_Persons/Western/julius-caesar.md` — confirm the reviewed pilots are still the same (no surprises).

### Known cosmetic items to expect during review

- Some Life Timeline / Works rows show `—` for Status (issue #4 above — deferred).
- Some Relationships rows render the Person column as plain text where the registry couldn't confidently resolve (issue #3 — expected; better than fake wikilinks).

---

## 13. What this PR / mirror does NOT do

- Does not edit `incoming/` source data.
- Does not modify the pilot person notes (MD5 verified unchanged).
- Does not delete any vault files.
- Does not generate Phase D standalone notes (`02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/` remain empty scaffolds).
- Does not collect new persons.
- Does not promote anything to master.
- Does not modify `.obsidian/`, `.stfolder/`, `.stignore`, or any sync-conflict file.
- Does not patch the generator further.
- Does not delete the 18 namespaced TY/JC duplicate source notes (defer per `_post_import_cleanup_plan_v1.md` §2).
- Does not write outside `obsidian-vault-pilot/_dryrun_29_v1/` and `reviewed/staging/obsidian_import/` on the repo side, and only inside `01-Projects/Historical-Persons-Wiki/` on the vault side.
