# Post-Import Status v1

**Date:** 2026-05-18
**Branch:** `cleanup/obsidian-post-import-v1`
**Live vault path:** `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` (WSL: `/mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/`)

This document is the canonical "where things stand" snapshot after the 22-person import wave landed on `main`.

---

## 1. PR #34 status

- **PR:** https://github.com/shensiongchoo-art/historical-persons/pull/34
- **State:** **MERGED** as squash commit `b00b1f8` (subject: `plan + dry-run + mirror: 22-person Obsidian import (#34)`).
- **Mergeable status before merge:** `CLEAN` / `MERGEABLE`. No required CI checks (`statusCheckRollup: []`).
- **Branch retained:** `planning/obsidian-22-person-import-v1` left on origin (not auto-deleted) — safe to delete in housekeeping; preserved for now as reference.

---

## 2. Live vault counts (snapshot now)

| Category | Count | Source |
|----------|-------|--------|
| Person notes | **22** | 12 Chinese + 10 Western under `01_Persons/{Chinese,Western}/` |
| Source notes | **221** | 203 newly mirrored namespaced + 18 preserved pilot (`SRC_TY_001`–`009`, `SRC_JC_001`–`009`) |
| Source notes (Chinese) | 121 | 112 namespaced + 9 pilot |
| Source notes (Western) | 100 | 91 namespaced + 9 pilot |
| Template notes | 2 | `99_Templates/tpl-person.md`, `tpl-source.md` |
| D-level source notes carrying 🚫 banner | **34** | 30 newly mirrored + 4 pilot |
| Folder scaffold (empty subfolders ready for future Phase D) | 6 dirs | `00_Project/`, `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/`, `90_Staging_Review/` |
| Total `.md` files in project folder | **245** | (22 + 221 + 2) |

---

## 3. Unresolved person wikilink count (post-cleanup-v1 fixes)

| Scope | Distinct unresolved | Notes |
|-------|---------------------|-------|
| **Repo dry-run** (`obsidian-vault-pilot/_dryrun_22_v1/`) | **0** | All 3 prior unresolved links fixed in this cleanup PR |
| **Live vault** (`H:\…\Historical-Persons-Wiki\`) | **1** | `[[marcus-antonius]]` in pilot `julius-caesar.md` (lines 24, 160); intentionally not modified pending user authorisation per cleanup plan §1 |

Pilot file integrity preserved:
- `tang-yin.md` MD5 = `688cc12e0baacf706e51d1b6deb582d5` (unchanged from pre-mirror)
- `julius-caesar.md` MD5 = `4f6d324c50701ae8da29a6b0899324f3` (unchanged from pre-mirror)

Source wikilinks: 1,258 scanned in live vault, **0 unresolved**.

---

## 4. Remaining cleanup tasks

From `_post_import_cleanup_plan_v1.md`:

| # | Task | Severity | Blocking? |
|---|------|----------|------------|
| 1 | Modify pilot vault `julius-caesar.md`: `[[marcus-antonius]]` → `[[mark-antony]]` | Cosmetic / 1 link | No — requires explicit user approval |
| 2 | Delete 18 namespaced TY/JC duplicate source notes from live vault (cleanup plan §2 Option B) | Visual-clutter | No |
| 3 | Generator v3: add `RELATED_PERSON_NAME → CANONICAL_SLUG` lookup map | Prevents regression | No |
| 4 | Generator v3: auto-hide Status column when all rows are `—` (cleanup plan §3) | Cosmetic — affects 364 cells | No |
| 5 | Phase D: generate standalone event / work / relationship notes (cleanup plan §4) | Enhancement | No — explicitly deferred until §1–§4 resolved |

None of the above blocks ongoing review or use of the live vault. The vault is functionally complete and link-clean for the 22 newly mirrored persons; only one pilot wikilink remains unresolved by intent.

---

## 5. Safety verification (re-run today)

| Check | Result |
|-------|--------|
| OneDrive `*Sync-Conflict*` files in project folder | ✅ 0 |
| Syncthing `*.sync-conflict-*` files in project folder | ✅ 0 |
| `.obsidian`, `.stfolder`, `.stignore` accidentally copied into project folder | ✅ 0 (correctly absent — they live at vault root only) |
| Vault-root `.obsidian/`, `.stfolder`, `.stignore` modified | ✅ Untouched |
| `incoming/` modified | ✅ `git status incoming/` empty |
| PARA folders outside the project | ✅ Untouched |
| Pilot files byte-identical to pre-mirror | ✅ MD5 verified |

---

## 6. Recommendation on whether collection can resume

**Recommendation: do NOT resume new-person collection yet.** Defer until the following gates pass:

| Gate | Reason |
|------|--------|
| ☐ Cleanup plan §1 (pilot link fix decision) | One unresolved link in the vault. Decide now whether to fix the pilot in-place or accept it permanently. Future review tools may flag it. |
| ☐ Cleanup plan §2 (duplicate TY/JC source notes decision) | 18 duplicate files exist in the vault with zero inbound references. Decide whether to delete or keep. |
| ☐ Cleanup plan §3 (generator v3 hardening) | Without the name→slug lookup, the next collection batch will reintroduce link drift for any new person whose `related_person_name` does not match the canonical slug. |
| ☐ User performs a second visual review pass after the cleanup decisions | Confirms the post-cleanup state is acceptable before more data piles on top. |

**Why these gates matter for collection:**
- New collection adds persons whose forward wikilinks will reference existing 22-batch persons. Without §3 fixed, every new person's related-people block risks unresolved links.
- New persons will likely re-use generic source-IDs (SRC001, etc.) per the existing pattern in 8 of 22 packages — namespacing convention works, but only if the generator is in good shape.
- The pilot vs. namespaced source-note duplication will compound: every new person added on top of the current state inherits the same ambiguity if §2 isn't resolved.

**Soft alternative:** if business pressure requires collection to resume now, restrict to **only persons whose source packages already use namespaced IDs** (the 14 namespaced packages of the existing 22 had no collision issues). Avoid collecting persons that would add to the generic-ID set until generator v3 lands.

**Hard recommendation: pause collection** for one short cleanup iteration (1–2 PRs covering the 5 items above), then resume cleanly.

---

## 7. Quick reference — important files and paths

| Artifact | Path |
|----------|------|
| Live Obsidian vault project folder | `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` |
| Repo canonical pilot output | `obsidian-vault-pilot/` |
| Repo dry-run sandbox (regeneratable) | `obsidian-vault-pilot/_dryrun_22_v1/` |
| Generator script | `tools/obsidian_dryrun_generator.py` |
| Plan v1 | `reviewed/staging/obsidian_import/_22_person_import_plan_v1.md` |
| Dry-run report v1 | `reviewed/staging/obsidian_import/_22_person_dryrun_generation_report_v1.md` |
| Spot-check report v1 | `reviewed/staging/obsidian_import/_22_person_dryrun_spotcheck_report_v1.md` |
| Live mirror report v1 | `reviewed/staging/obsidian_import/_22_person_live_mirror_report_v1.md` |
| Cleanup plan v1 | `reviewed/staging/obsidian_import/_post_import_cleanup_plan_v1.md` |
| This status report v1 | `reviewed/staging/obsidian_import/_post_import_status_v1.md` |
| Merged PR | https://github.com/shensiongchoo-art/historical-persons/pull/34 |
| Cleanup branch | `cleanup/obsidian-post-import-v1` |
