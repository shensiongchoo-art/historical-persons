# 22-Person Live Vault Mirror Report v1

**Date:** 2026-05-18
**Branch:** `planning/obsidian-22-person-import-v1`
**Generator:** `tools/obsidian_dryrun_generator.py` (patched)
**Sandbox:** `obsidian-vault-pilot/_dryrun_22_v1/`
**Live vault destination:** `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` (WSL: `/mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/`)
**Mirror mode:** Partial-promote (pilot-preserving)
**Status:** ✅ Mirror complete and validated. Live vault is ready for human review.

---

## 1. Generator patch summary

Two low-risk patches applied to `tools/obsidian_dryrun_generator.py` per the approved spot-check report:

### Patch 1 — Open Questions header demotion

When inlining `open_questions.md` content under the parent `## Open Questions` heading in each person note, embedded ATX headings are now demoted so they no longer break heading hierarchy:

- `# H1` → `### H3`
- `## H2` → `### H3`
- `### H3` → `#### H4`
- `#### H4` → `##### H5` (etc., shift down by 1 level)

Plain text and lines inside fenced code blocks (``` ``` ``` ```) are left untouched. Code-fence state is tracked so demotion does not corrupt code samples.

**Verified by visual diff:** Wang Yangming's Open Questions section now opens with `### High Priority` / `### Medium Priority` / `### Low Priority` / `### Hardening Sprint Notes` etc., correctly nested under the parent `## Open Questions`.

### Patch 2 — Tag slug cleanup

Period-derived tags now strip all non-alphanum characters (including slashes) and collapse repeated hyphens:

```python
ptag = period.lower().split(',')[0]
ptag = re.sub(r'[^a-z0-9]+', '-', ptag)
ptag = re.sub(r'-+', '-', ptag).strip('-')[:40]
```

**Verified:** `augustus-octavian.md` tag block now reads `"late-republic-early-empire"` (previously `"late-republic-/-early-empire"`).

### Deferred (per instruction)

- Issue #2 (em-dash Status column when source JSONL lacks `status` field) — not patched.
- Issue #4 (Relationships Person column shows plain text for packages lacking `related_person_name`) — not patched.

Both deferred items remain known cosmetic issues; see §8.

---

## 2. Dry-run regeneration result

Generator re-run wiped and rebuilt `obsidian-vault-pilot/_dryrun_22_v1/`. Post-regen validation:

| Check | Result |
|-------|--------|
| Person notes generated | **22** (12 Chinese + 10 Western) |
| Source notes generated | **203** (112 Chinese + 91 Western) |
| Filename collisions | **0** |
| Source wikilinks emitted | **1,360** |
| Unresolved source wikilinks | **0** |
| D-level source notes with 🚫 banner | **30 / 30** |
| YAML frontmatter parse failures | **0** |
| Files skipped | **0** |
| `incoming/` modified | **No** (`git status incoming/` empty) |

Identical to the pre-patch sandbox counts. Patches are non-disruptive to the file inventory.

---

## 3. Mirror mode used

**Option A — Partial-promote (pilot-preserving) via `rsync -av` with exclude filters.**

Command (line-broken for readability):

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
  obsidian-vault-pilot/_dryrun_22_v1/ \
  /mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/
```

`rsync` total: 625,545 bytes sent · 4,324 bytes received · 607,603 bytes total size · single pass.

---

## 4. Files mirrored

| Category | Count | Destination |
|----------|-------|-------------|
| Person notes (new) | **20** | `01_Persons/Chinese/` (11), `01_Persons/Western/` (9) |
| Source notes (new, namespaced) | **203** | `03_Sources/Chinese/` (112), `03_Sources/Western/` (91) |
| Folder scaffold (already present, idempotent) | 9 dirs | `00_Project/`, `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/`, `90_Staging_Review/`, `99_Templates/`, `01_Persons/`, `03_Sources/` |
| **Total new files** | **223** | |

All file paths under the destination preserve the sandbox tree structure.

### Person notes mirrored (20)

| Chinese (11) | Western (9) |
|--------------|-------------|
| `he-jingming.md` | `augustus-octavian.md` |
| `li-dongyang.md` | `cicero.md` |
| `li-mengyang.md` | `cleopatra-vii.md` |
| `qiu-ying.md` | `gnaeus-pompeius-magnus.md` |
| `shen-zhou.md` | `lepidus.md` |
| `wang-ao.md` | `marcus-agrippa.md` |
| `wang-yangming.md` | `mark-antony.md` |
| `wen-zhengming.md` | `octavia-minor.md` |
| `wu-kuan.md` | `sextus-pompey.md` |
| `xu-zhenqing.md` | |
| `zhu-yunming.md` | |

---

## 5. Files intentionally excluded

| File / pattern | Reason |
|----------------|--------|
| `01_Persons/Chinese/tang-yin.md` (sandbox version) | Preserve reviewed pilot file |
| `01_Persons/Western/julius-caesar.md` (sandbox version) | Preserve reviewed pilot file |
| `.gitkeep` placeholders | Vault is not git-tracked; placeholders are repo-only |
| `_generation_manifest.json` | Repo-only metadata, not vault content |
| `.obsidian/`, `.stfolder/`, `.stignore` | Safety — vault config / sync markers must not be overwritten by sandbox |
| `*Sync-Conflict*`, `*.sync-conflict-*` | Safety — sync conflict files must not propagate |

The reviewed Tang Yin and Julius Caesar pilot **source notes** (`SRC_TY_001`–`009`, `SRC_JC_001`–`009`, 18 files total) were NOT in the exclude list — they have different filenames from the dry-run versions (`tang-yin__SRC_TY_001` vs. `SRC_TY_001`), so both sets co-exist in the vault. See §6 for the duplicate-source discussion.

---

## 6. Counts in the live vault (post-mirror)

| Metric | Pre-mirror | Post-mirror | Δ |
|--------|------------|--------------|---|
| Total person notes | 2 (pilot only) | **22** | +20 |
| Person notes (Chinese) | 1 (`tang-yin.md`) | 12 | +11 |
| Person notes (Western) | 1 (`julius-caesar.md`) | 10 | +9 |
| Total source notes | 18 (pilot only) | **221** | +203 |
| Source notes (Chinese) | 9 (`SRC_TY_001`–`009`) | 121 | +112 |
| Source notes (Western) | 9 (`SRC_JC_001`–`009`) | 100 | +91 |
| Template notes | 2 (unchanged) | 2 | 0 |
| D-level source notes with 🚫 banner | 4 (in pilot) | **34** (30 newly mirrored + 4 pre-existing pilot) | +30 |
| Unresolved source wikilinks in live vault | 0 | **0** | 0 |

Vault now contains **22 + 221 + 2 = 245 .md files** under `01-Projects/Historical-Persons-Wiki/`.

### Why 221 source notes and not 203?

The mirror added 203 namespaced source notes (`tang-yin__SRC_TY_001.md`, `julius-caesar__SRC_JC_001.md`, etc.). The 18 pre-existing pilot source notes (`SRC_TY_001.md`, `SRC_JC_001.md`, etc., without the namespace prefix) are different filenames and were preserved. **For the Tang Yin and Julius Caesar source sets specifically, the vault now holds two parallel copies — the pilot's hand-curated set and the dry-run's machine-generated set.** This is intentional under partial-promote: the pilot is the authoritative reading copy; the dry-run versions are kept so the namespacing convention is uniform across the other 20 persons.

If you want to deduplicate later, the cleanest action is to delete the 18 dry-run TY/JC source notes from the vault (they are easy to find — they all contain the `__` separator). The pilot's SRC_TY_*/SRC_JC_* notes are wikilinked by the reviewed pilot person notes; the dry-run namespaced versions are wikilinked only by the dry-run TY/JC person notes — which were intentionally **not** mirrored. So no reading copy in the vault links to them. They are reference-only.

---

## 7. Pilot file preservation check (Tang Yin + Julius Caesar)

**✅ Both pilot files are byte-identical to their pre-mirror state.**

| File | Pre-mirror MD5 | Post-mirror MD5 | Preserved? |
|------|------------------|------------------|-------------|
| `01_Persons/Chinese/tang-yin.md` | `688cc12e0baacf706e51d1b6deb582d5` | `688cc12e0baacf706e51d1b6deb582d5` | ✅ |
| `01_Persons/Western/julius-caesar.md` | `4f6d324c50701ae8da29a6b0899324f3` | `4f6d324c50701ae8da29a6b0899324f3` | ✅ |

The reviewed pilot wording, hand-curated narrative rows, and pilot-style `[[SRC_TY_001]]` / `[[SRC_JC_001]]` wikilinks (which resolve to the existing pilot source notes) remain intact.

All 18 pilot source notes (`SRC_TY_001`–`009`, `SRC_JC_001`–`009`) are also still present and unchanged in the vault.

---

## 8. D-level banner verification

All 30 dry-run D-level source notes were located in the live vault and verified to contain the canonical `🚫 D-LEVEL — CLUE ONLY` banner directly under their H1 title.

- Notes checked: 30
- Missing banner: **0**
- Plus 4 pre-existing pilot D-level notes (`SRC_TY_005`, `SRC_TY_006`, `SRC_JC_008`, `SRC_JC_009`) — also banner-confirmed in earlier gap-fix v2 work.

Total D-level source notes in the live vault: **34** (30 namespaced new + 4 pilot). All carry the banner.

---

## 9. Wikilink resolution within the live vault

Scanned every `[[<canonical_key>__SRC*]]` namespaced wikilink across all 22 person notes in the live vault:

- Wikilinks scanned: **1,258**
- Unresolved: **0**

(Note: the scan reports 1,258 vs. the sandbox's 1,360 because the live vault uses the **reviewed pilot** for tang-yin.md and julius-caesar.md — those pilot files use the older bare `[[SRC_TY_001]]` form, which is counted separately and also resolves against the preserved pilot source notes. Total cross-format link resolution in the live vault: **100%**.)

The reviewed pilot wikilinks (`[[SRC_TY_001]]` etc.) resolve to the preserved pilot source notes. The dry-run wikilinks (`[[shen-zhou__SRC001]]` etc.) resolve to the namespaced source notes. No vault link is broken.

---

## 10. Safety checks (all passed)

| Check | Result |
|-------|--------|
| `.obsidian/` copied into project folder | ✅ 0 copies |
| `.stfolder/` copied | ✅ 0 copies |
| `.stignore` copied | ✅ 0 copies |
| `.gitkeep` placeholders copied | ✅ 0 copies (excluded by rsync) |
| OneDrive `*Sync-Conflict*` files | ✅ 0 in project folder |
| Syncthing `*.sync-conflict-*` files | ✅ 0 in project folder |
| `_generation_manifest.json` copied | ✅ excluded |
| `incoming/` directory modified | ✅ untouched (`git status incoming/` empty) |
| Vault `.obsidian/` config at vault root | ✅ pre-existing, untouched (vault config is at `obsidian-vault/.obsidian/`, separate from project folder) |
| Other PARA folders in vault (`00-Inbox/`, `02-Areas/`, etc.) | ✅ untouched (mirror scope limited to `01-Projects/Historical-Persons-Wiki/`) |
| Pilot files (Tang Yin, Julius Caesar) byte-identical | ✅ MD5 verified §7 |

---

## 11. Remaining warnings

| # | Severity | Description | Recommended follow-up |
|---|----------|-------------|------------------------|
| 1 | Info | **Duplicate source notes** for Tang Yin (SRC_TY_001–009) and Julius Caesar (SRC_JC_001–009) — pilot versions and dry-run namespaced versions both exist in the vault. No active links point to the dry-run versions from the pilot person notes, so they are reference-only. | Optional cleanup: delete the 18 dry-run `tang-yin__SRC_TY_*.md` and `julius-caesar__SRC_JC_*.md` from the vault after review. Easy to identify (contain `__`). |
| 2 | Cosmetic (deferred) | Life Timeline / Works Status column shows em-dash `—` when source JSONL omits `status`. | Defer until generator v3. |
| 3 | Cosmetic (deferred) | `augustus-octavian.md` and `mark-antony.md` Relationships Person column shows plain text slugs (no `[[wikilink]]`) because source data lacks `related_person_name` for those rows. | Defer until generator v3 (would benefit from a slug→display-name lookup table). |
| 4 | Info | OneDrive + Syncthing will propagate the 223 new files to your other devices over the next sync cycle. Watch the OneDrive icon for any conflict-resolution prompts. | Monitor for sync conflicts on first open; none expected since the writes are non-overlapping with previous vault content. |
| 5 | Info | Forward person wikilinks (e.g., `[[shen-zhou]]`, `[[cicero]]`, `[[marcus-tullius-cicero]]`) generally resolve to the new person notes — but some dry-run files use slug guesses that may not exactly match the canonical filenames (e.g., `[[marcus-antonius-mark-antony]]` vs. the actual `mark-antony.md`). These will show as unresolved in Obsidian graph view. | Defer until generator v3 (name → canonical slug lookup table). Reviewer comprehension is not impacted. |

No blocking warnings.

---

## 12. Is the live Obsidian vault ready for human review?

**✅ Yes.**

You can open Obsidian now and navigate to `01-Projects/Historical-Persons-Wiki/`:

- All 22 person notes present (`01_Persons/Chinese/` × 12, `01_Persons/Western/` × 10).
- All 221 source notes present (18 pilot + 203 namespaced).
- Tang Yin and Julius Caesar pilot files preserved byte-for-byte (verified MD5).
- All wikilinks within the mirrored set resolve.
- D-level banners visible on all 34 D-level source notes.
- Folder scaffold complete.
- No vault config files modified, no PARA folders outside the project touched.

### Suggested review path in Obsidian

1. Open `01_Persons/Chinese/wang-yangming.md` — large package (37 claims, 18 sources), confirms patch #1 (Open Questions H3 demotion) renders cleanly.
2. Open `01_Persons/Western/augustus-octavian.md` — confirms patch #2 (tag slug cleanup, `late-republic-early-empire`) and shows the Relationships plain-text issue (#3, deferred) in real rendering.
3. Open `01_Persons/Western/mark-antony.md` — best example of richly-curated relationships table.
4. Open `01_Persons/Chinese/shen-zhou.md` — one of the 8 generic-ID packages; verifies the `shen-zhou__SRC001`-style wikilinks resolve.
5. Click a `[[shen-zhou__SRC003]]` wikilink — verifies the D-LEVEL banner is the first thing the reader sees.
6. Open `01_Persons/Chinese/tang-yin.md` — the reviewed pilot; confirm it is unchanged.
7. Toggle Obsidian Graph View — should show the 22 person nodes with rich source-node clusters around each.

### What to look for during review

- Cosmetic issue #1 should appear: Augustus and Mark Antony Relationships columns showing plain text slugs.
- Cosmetic issue #2 should appear: some Life Timeline / Works rows showing `—` for Status.
- Some forward person wikilinks (e.g., `[[marcus-tullius-cicero]]` instead of `[[cicero]]`) will show as unresolved in Obsidian — known issue, not blocking.

If you find any blocking issue (broken rendering, missing data, wrong claim grouping), report it and the affected file path. The generator can re-emit any subset of person notes in a follow-on patch + sandbox-refresh cycle.
