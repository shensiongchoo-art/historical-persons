# Post-Batch 4 Merge Status v1

**Date:** 2026-05-21
**Branch:** `reports/post-batch4-merge-status-v1` (off `main`)
**Main HEAD:** `7265486` (post-#39 merge)
**Scope:** Snapshot taken immediately after merging PRs #35, #37, #36, #38, #39.

---

## 1. PRs merged (in order)

| Step | PR | Squash commit | Title |
|------|----|----|----|
| 1 | **#35** | `30f60af` | cleanup: 22-person post-import — link drift fixes + cleanup plan v1 |
| 2 | **#37** | `150ccdb` | Verification: Batch 3 Crassus + Brutus source check — all 13 sources confirmed |
| 3 | **#36** | `dfca6a4` | Collect Batch 3: Crassus and Brutus packages (v2.5) |
| 4 | **#38** | `8e7c719` | Plan: Batch 4 candidate scope — 5 recommended, 2 deferred |
| 5 | **#39** | `7265486` | Collect Batch 4 network expansion packages |

All 5 merged via `--squash --delete-branch=false`. PR branches preserved on origin.

PR #40 (triage report — opened by this session before the merge sequence) remains **OPEN**. Reports-only; safe to merge anytime as a record of the triage decision.

---

## 2. Validation results

Validator: `tools/validate_package.py` (run on each branch before merging the collection PR).

### Batch 3 (PR #36 prerequisites)

| Package | Result |
|---------|--------|
| `incoming/western/marcus-licinius-crassus` | ✅ **VALIDATION PASSED** |
| `incoming/western/marcus-junius-brutus` | ✅ **VALIDATION PASSED** |

### Batch 4 (PR #39 prerequisites)

| Package | Result |
|---------|--------|
| `incoming/chinese/wang-shizhen` | ✅ **VALIDATION PASSED** |
| `incoming/chinese/chen-chun` | ✅ **VALIDATION PASSED** |
| `incoming/chinese/li-panlong` | ✅ **VALIDATION PASSED** |
| `incoming/western/cato-the-younger` | ✅ **VALIDATION PASSED** |
| `incoming/western/gaius-cassius-longinus` | ✅ **VALIDATION PASSED** |

**Total: 7/7 packages PASSED** before their respective collection PR was merged.

---

## 3. Total staging person count

| Culture | Count | Delta |
|---------|-------|-------|
| Chinese | **15** | +0 from previous; +3 from Batch 4 (wang-shizhen, chen-chun, li-panlong) means previous was 12 ✓ |
| Western | **14** | +2 from Batch 3 (Crassus, Brutus) and +2 from Batch 4 (Cato, Cassius); previous was 10 ✓ |
| **Total** | **29** | +7 net (22 → 29) |

The staging set has grown from 22 persons (post-22-person-import wave) to **29 persons** after this merge sequence. All 29 packages live under `incoming/{chinese,western}/<slug>/` with the v2.5 11-file schema.

---

## 4. Live Obsidian vault state

**Unchanged.** Still reflects 22 persons / 221 source notes / 2 templates (from the 2026-05-18 partial-promote mirror). No mirror operation performed during this merge sequence per user instruction.

The vault is now **7 persons behind the staging repo**.

---

## 5. Remaining blockers

| # | Item | Severity | Notes |
|---|------|----------|-------|
| 1 | Obsidian vault is 7 persons behind staging | **Medium** | Re-mirror needed; see §6 |
| 2 | Open PR #40 (triage report) not yet merged | Low | Reports-only; merge or close at your convenience |
| 3 | Pilot vault `julius-caesar.md` `[[marcus-antonius]]` → `[[mark-antony]]` | Low | Still requires explicit user authorisation; documented in `_post_import_cleanup_plan_v1.md` |
| 4 | 18 duplicate TY/JC namespaced source notes in vault | Low | Optional cleanup; documented in `_post_import_cleanup_plan_v1.md` §2 |
| 5 | Generator v3 hardening (name→slug map, em-dash status auto-hide) | Medium | Recommended before next collection wave so new persons don't reintroduce link drift |
| 6 | Phase D standalone notes (events/works/relationships) | Low | Explicit deferral; not blocking |

**No hard blockers.** All items are tracked, none prevent the next recommended task from starting.

---

## 6. Next recommended task

**Obsidian re-mirror: 22 → 29 persons.**

Concrete sub-steps for the next session:

1. **(Optional) Apply generator v3 hardening first** — add the name→canonical-slug lookup map so the 7 new persons' forward person wikilinks resolve cleanly without a post-mirror cleanup PR. Without it, expect a second link-drift cleanup pass for the new 7. With it, the re-mirror is link-clean from emit-time.
2. **Spot-check the 7 new packages** for namespaced vs. generic source-ID convention. Survey existing 22 showed 8 of 22 were generic-ID. Confirm the new 7 do not introduce new generic-ID collisions before regeneration.
3. **Re-run `tools/obsidian_dryrun_generator.py`** to rebuild `obsidian-vault-pilot/_dryrun_22_v1/` — but rename to `_dryrun_29_v1/` (or similar) so the 22-person sandbox stays as a reference. Validate counts, banners, link resolution.
4. **Mirror to live vault** using the partial-promote pattern from `_22_person_live_mirror_report_v1.md`. Continue to preserve the reviewed pilot files (tang-yin.md, julius-caesar.md) via rsync `--exclude`.
5. **Spot-check the 7 new person notes** in Obsidian after mirror. Confirm D-LEVEL banners on any new D-level source notes from the 7 packages.
6. **Update `_post_import_status_v1.md`** with the new 29-person count.
7. **Pause collection** until step 6 is done. Otherwise the vault/staging gap will widen further.

Estimated effort: one focused session, similar to the 2026-05-17/18 wave (~half a day).

---

## 7. What this report does NOT do

- Does not merge any PR (besides the 5 already merged in the sequence above).
- Does not modify any package under `incoming/`.
- Does not run any further validation.
- Does not modify any Obsidian file (vault or repo sandbox).
- Does not collect new persons.
- Does not promote anything to master (project does not yet have a master layer).
- Does not patch `tools/obsidian_dryrun_generator.py`.
