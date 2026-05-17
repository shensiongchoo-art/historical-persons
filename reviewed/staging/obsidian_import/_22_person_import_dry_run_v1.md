# 22-Person Obsidian Import — Dry-Run Report v1

**Date:** 2026-05-17
**Branch:** `planning/obsidian-22-person-import-v1`
**Companion:** `_22_person_import_plan_v1.md`
**Status:** Dry-run only — no person notes or source notes generated. The repo and live vault are unchanged for the 20 non-pilot persons.

This report walks the 22 person packages in `incoming/`, validates them, predicts every output filename, and surfaces the conflicts and risks that the next (generation) phase must handle.

---

## 1. 22 person packages found

All 22 expected packages exist under `incoming/` and parse cleanly. 0 missing required files, 0 JSON/JSONL parse errors, 0 orphan `source_id` references in claims/events/relationships/works.

| # | Slug | Batch | Culture | Display name (from person_record.json) |
|---|------|-------|---------|----------------------------------------|
| 1 | shen-zhou | MVP | Chinese | Shen Zhou / 沈周 |
| 2 | wang-yangming | MVP | Chinese | Wang Yangming / 王阳明 |
| 3 | qiu-ying | MVP | Chinese | Qiu Ying / 仇英 |
| 4 | wu-kuan | MVP | Chinese | Wu Kuan / 吴宽 |
| 5 | gnaeus-pompeius-magnus | MVP | Western | Gnaeus Pompeius Magnus (Pompey) |
| 6 | augustus-octavian | MVP | Western | Augustus / Octavian |
| 7 | mark-antony | MVP | Western | Marcus Antonius / Mark Antony |
| 8 | tang-yin | B1 | Chinese | Tang Yin / 唐寅  ⚠ pilot |
| 9 | wen-zhengming | B1 | Chinese | Wen Zhengming / 文徵明 |
| 10 | zhu-yunming | B1 | Chinese | Zhu Yunming / 祝允明 |
| 11 | xu-zhenqing | B1 | Chinese | Xu Zhenqing / 徐祯卿 |
| 12 | julius-caesar | B1 | Western | Gaius Julius Caesar  ⚠ pilot |
| 13 | cicero | B1 | Western | Marcus Tullius Cicero |
| 14 | cleopatra-vii | B1 | Western | Cleopatra VII |
| 15 | marcus-agrippa | B1 | Western | Marcus Vipsanius Agrippa |
| 16 | li-dongyang | B2 | Chinese | Li Dongyang / 李东阳 |
| 17 | wang-ao | B2 | Chinese | Wang Ao / 王鏊 |
| 18 | li-mengyang | B2 | Chinese | Li Mengyang / 李梦阳 |
| 19 | he-jingming | B2 | Chinese | He Jingming / 何景明 |
| 20 | lepidus | B2 | Western | Marcus Aemilius Lepidus |
| 21 | octavia-minor | B2 | Western | Octavia Minor |
| 22 | sextus-pompey | B2 | Western | Sextus Pompey |

Counts: 12 Chinese + 10 Western = 22. Match expected.

---

## 2. Counts per person

| Slug | Claims | Sources | Rels | Events | Works | VisualMedia | Legendary |
|------|--------|---------|------|--------|-------|-------------|-----------|
| he-jingming | 10 | 6 | 3 | 6 | 2 | 1 | 2 |
| li-dongyang | 10 | 6 | 3 | 3 | 2 | 1 | 1 |
| li-mengyang | 8 | 7 | 3 | 1 | 1 | 1 | 1 |
| qiu-ying | 34 | 23 | 12 | 8 | 13 | 4 | 3 |
| shen-zhou | 22 | 6 | 13 | 5 | 8 | 3 | 4 |
| tang-yin (pilot) | 18 | 9 | 6 | 5 | 5 | 2 | 2 |
| wang-ao | 8 | 4 | 3 | 6 | 3 | 1 | 2 |
| wang-yangming | 37 | 18 | 8 | 12 | 3 | 3 | 7 |
| wen-zhengming | 14 | 8 | 6 | 4 | 4 | 2 | 1 |
| wu-kuan | 22 | 7 | 4 | 5 | 4 | 2 | 2 |
| xu-zhenqing | 10 | 10 | 4 | 3 | 2 | 1 | 1 |
| zhu-yunming | 10 | 8 | 3 | 4 | 3 | 1 | 1 |
| augustus-octavian | 35 | 18 | 9 | 15 | 2 | 3 | 5 |
| cicero | 16 | 8 | 5 | 5 | 4 | 2 | 1 |
| cleopatra-vii | 15 | 7 | 5 | 6 | 1 | 2 | 2 |
| gnaeus-pompeius-magnus | 42 | 17 | 12 | 20 | 2 | 5 | 6 |
| julius-caesar (pilot) | 18 | 9 | 6 | 7 | 2 | 2 | 2 |
| lepidus | 9 | 4 | 3 | 7 | 1 | 1 | 2 |
| marcus-agrippa | 14 | 8 | 5 | 5 | 3 | 2 | 1 |
| mark-antony | 35 | 11 | 13 | 23 | 4 | 4 | 5 |
| octavia-minor | 9 | 4 | 4 | 5 | 1 | 1 | 2 |
| sextus-pompey | 9 | 5 | 4 | 6 | 1 | 1 | 2 |

**Totals:** 405 claims · 203 source entries (per-package, before namespacing dedup) · 132 relationships · 161 events · 70 works · 44 visual media · 55 legendary notes.

Top-3 densest packages by claims: gnaeus-pompeius-magnus (42), wang-yangming (37), augustus-octavian + mark-antony (35 each).

---

## 3. Source-note namespacing (CRITICAL FINDING)

`source_id` values are **not globally unique** across the 22 packages. Two ID conventions are in use:

### 3a. Already-namespaced packages (14)

These packages already use per-person prefixes (`SRC_TY_NNN` for Tang Yin, `SRC_JC_NNN` for Julius Caesar, etc.). Source-note filename strategy: **unchanged**.

| Package | Prefix | Source-note filename | Wikilink form |
|---------|--------|----------------------|---------------|
| tang-yin (pilot) | `SRC_TY_` | `SRC_TY_001.md` … `SRC_TY_009.md` | `[[SRC_TY_001]]` |
| julius-caesar (pilot) | `SRC_JC_` | `SRC_JC_001.md` … `SRC_JC_009.md` | `[[SRC_JC_001]]` |
| qiu-ying | `SRC_QY_` | `SRC_QY_001.md` … (23 files) | `[[SRC_QY_001]]` |
| wu-kuan | `SRC_WK_` | `SRC_WK_001.md` … (7 files) | `[[SRC_WK_001]]` |
| wen-zhengming | `SRC_WZM_` | `SRC_WZM_001.md` … (8 files) | `[[SRC_WZM_001]]` |
| zhu-yunming | `SRC_ZYM_` | `SRC_ZYM_001.md` … (8 files) | `[[SRC_ZYM_001]]` |
| xu-zhenqing | `SRC_XZQ_` | `SRC_XZQ_001.md` … (10 files) | `[[SRC_XZQ_001]]` |
| li-dongyang | `SRC_LDY_` | `SRC_LDY_001.md` … (6 files) | `[[SRC_LDY_001]]` |
| li-mengyang | `SRC_LMY_` | `SRC_LMY_001.md` … (7 files) | `[[SRC_LMY_001]]` |
| cicero | `SRC_CC_` | `SRC_CC_001.md` … (8 files) | `[[SRC_CC_001]]` |
| cleopatra-vii | `SRC_CL_` | `SRC_CL_001.md` … (7 files) | `[[SRC_CL_001]]` |
| marcus-agrippa | `SRC_MA_` | `SRC_MA_001.md` … (8 files) | `[[SRC_MA_001]]` |
| augustus-octavian | (verify at gen-time) | TBD per per-package check | TBD |
| mark-antony | (verify at gen-time) | TBD per per-package check | TBD |

augustus-octavian and mark-antony were not sampled in the survey — the generator must check their `source_id` convention at emit time. If they use generic IDs, they fall into §3b.

### 3b. Generic-ID packages (8) — collision risk

These packages use `SRC001`, `SRC002`, etc. — IDs that collide across packages:

| Package | Source count | Sample source_ids |
|---------|--------------|-------------------|
| shen-zhou (MVP) | 6 | SRC001…SRC006 |
| wang-yangming (MVP) | 18 | SRC001…SRC018 |
| gnaeus-pompeius-magnus (MVP) | 17 | SRC001…SRC017 |
| wang-ao (B2) | 4 | SRC001…SRC004 |
| he-jingming (B2) | 6 | SRC001…SRC006 |
| lepidus (B2) | 4 | SRC001…SRC004 |
| octavia-minor (B2) | 4 | SRC001…SRC004 |
| sextus-pompey (B2) | 5 | SRC001…SRC005 |

**Sample of the collision** — three different `SRC001`s in three different packages:

- `he-jingming` SRC001 = 明史·何景明传 (Ming History biography)
- `gnaeus-pompeius-magnus` SRC001 = Plutarch, Life of Pompey
- `octavia-minor` SRC001 = Cambridge Ancient History, Vol. X

These are **not** the same source — they are independent sources that happen to share an ID.

### 3c. Resolution: filename namespacing

Filename strategy for generic-ID packages: `{canonical_key}__{source_id}.md` (double-underscore separator).

| Package | Source filename | Wikilink form |
|---------|-----------------|---------------|
| shen-zhou | `shen-zhou__SRC001.md` … `shen-zhou__SRC006.md` | `[[shen-zhou__SRC001]]` |
| wang-yangming | `wang-yangming__SRC001.md` … (18 files) | `[[wang-yangming__SRC001]]` |
| gnaeus-pompeius-magnus | `gnaeus-pompeius-magnus__SRC001.md` … (17 files) | `[[gnaeus-pompeius-magnus__SRC001]]` |
| wang-ao | `wang-ao__SRC001.md` … (4 files) | `[[wang-ao__SRC001]]` |
| he-jingming | `he-jingming__SRC001.md` … (6 files) | `[[he-jingming__SRC001]]` |
| lepidus | `lepidus__SRC001.md` … (4 files) | `[[lepidus__SRC001]]` |
| octavia-minor | `octavia-minor__SRC001.md` … (4 files) | `[[octavia-minor__SRC001]]` |
| sextus-pompey | `sextus-pompey__SRC001.md` … (5 files) | `[[sextus-pompey__SRC001]]` |

The underlying `source_id` inside the source note's frontmatter stays as `SRC001` — the file structure is what changes, not the data. Wikilinks in the corresponding person note also use the namespaced filename, so generation must rewrite `SRC001` → `shen-zhou__SRC001` at emit time for that package.

This convention is reversible and machine-readable (`split('__', 1)` gives `(canonical_key, source_id)`).

---

## 4. Expected output file paths (preview)

### 4a. Person notes (22 total)

| Path | New / Overwrite |
|------|-----------------|
| `01_Persons/Chinese/shen-zhou.md` | new |
| `01_Persons/Chinese/wang-yangming.md` | new |
| `01_Persons/Chinese/qiu-ying.md` | new |
| `01_Persons/Chinese/wu-kuan.md` | new |
| `01_Persons/Chinese/tang-yin.md` | **OVERWRITE pilot — handled per §6** |
| `01_Persons/Chinese/wen-zhengming.md` | new |
| `01_Persons/Chinese/zhu-yunming.md` | new |
| `01_Persons/Chinese/xu-zhenqing.md` | new |
| `01_Persons/Chinese/li-dongyang.md` | new |
| `01_Persons/Chinese/wang-ao.md` | new |
| `01_Persons/Chinese/li-mengyang.md` | new |
| `01_Persons/Chinese/he-jingming.md` | new |
| `01_Persons/Western/gnaeus-pompeius-magnus.md` | new |
| `01_Persons/Western/augustus-octavian.md` | new |
| `01_Persons/Western/mark-antony.md` | new |
| `01_Persons/Western/julius-caesar.md` | **OVERWRITE pilot — handled per §6** |
| `01_Persons/Western/cicero.md` | new |
| `01_Persons/Western/cleopatra-vii.md` | new |
| `01_Persons/Western/marcus-agrippa.md` | new |
| `01_Persons/Western/lepidus.md` | new |
| `01_Persons/Western/octavia-minor.md` | new |
| `01_Persons/Western/sextus-pompey.md` | new |

### 4b. Source notes (counts after namespacing)

Total source-note files expected: **203** (sum of per-package `n_sources` from §2, since the filename namespacing makes every emit unique). Distribution:

- `03_Sources/Chinese/` — 12 Chinese packages × per-package source count = 112 files
- `03_Sources/Western/` — 10 Western packages × per-package source count = 91 files

Of these, **19 already exist** in the pilot (`SRC_TY_001`–`009` and `SRC_JC_001`–`009`, plus the namespaced TY/JC notes from the gap-fix passes). All 19 are pilot-overwrite candidates — handled per §6.

### 4c. Filename collision matrix (within the planned output)

After applying the namespacing convention §3c, the dry run finds **0 filename collisions** within the 203 source notes. The only collisions are between the 19 existing pilot files and the would-be 19 regenerated equivalents (covered in §6).

---

## 5. Missing files / malformed JSON / orphan refs

| Check | Result |
|-------|--------|
| All 22 packages have all 11 required files | ✅ 0 missing |
| All `.json` parse | ✅ 0 errors |
| All `.jsonl` parse line-by-line | ✅ 0 errors |
| All `source_id` referenced in `claims.jsonl` exist in `sources.jsonl` | ✅ 0 orphans |
| All `source_id` referenced in `events.jsonl` exist in `sources.jsonl` | ✅ 0 orphans |
| All `source_id` referenced in `relationships.jsonl` exist in `sources.jsonl` | ✅ 0 orphans |
| All `source_id` referenced in `works.jsonl` exist in `sources.jsonl` | ✅ 0 orphans |

No data-quality blockers.

---

## 6. Overwrite conflicts with current pilot

The pilot already occupies these paths in `obsidian-vault-pilot/`:

| Existing pilot file | Action under each import mode |
|---------------------|-------------------------------|
| `01_Persons/Chinese/tang-yin.md` | A: overwrite · B: emit to `_dryrun_22_v1/` only · C: skip if not in the 5-pick |
| `01_Persons/Western/julius-caesar.md` | A: overwrite · B: emit to `_dryrun_22_v1/` only · C: skip if not in the 5-pick |
| `03_Sources/Chinese/SRC_TY_001.md` … `SRC_TY_009.md` (9 files) | A: overwrite · B: emit to `_dryrun_22_v1/` only · C: skip |
| `03_Sources/Western/SRC_JC_001.md` … `SRC_JC_009.md` (9 files) | A: overwrite · B: emit to `_dryrun_22_v1/` only · C: skip |
| `99_Templates/tpl-person.md`, `tpl-source.md` | always preserve — generator input, not output |
| `00_Project/`, `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/`, `90_Staging_Review/` (empty + .gitkeep) | always preserve — populated by post-import or Phase D |

**Recommended conflict resolution (Option B):**

For tang-yin.md, julius-caesar.md, and all 18 pilot source notes: the generator emits to `_dryrun_22_v1/01_Persons/...` and `_dryrun_22_v1/03_Sources/...` only. The live pilot files are NEVER overwritten in the dry-run.

After the user reviews the sandbox output and explicitly approves promotion, only then do we decide per-file:

- If sandbox output for the pilot matches the live pilot byte-for-byte: discard the sandbox copy.
- If sandbox output differs: user diffs the two and chooses to either (a) replace the pilot with the generator output (regenerated baseline), or (b) keep the human-curated pilot and exempt it from generation. Option (b) is recommended because the pilot has been visually approved and any generator drift is a regression to debug, not to accept.

---

## 7. D-level sources needing the 🚫 CLUE ONLY banner

**Total D-level / clue_only sources across the 22 packages: 30 source notes.**

| Package | D-level source IDs (count) |
|---------|----------------------------|
| cicero | SRC_CC_007, SRC_CC_008 (2) |
| cleopatra-vii | SRC_CL_006, SRC_CL_007 (2) |
| he-jingming | SRC004, SRC006 (2) — namespaced as `he-jingming__SRC004`, `he-jingming__SRC006` |
| julius-caesar (pilot) | SRC_JC_008, SRC_JC_009 (2) — already banner'd |
| lepidus | SRC004 (1) — namespaced as `lepidus__SRC004` |
| li-dongyang | SRC_LDY_005, SRC_LDY_006 (2) |
| li-mengyang | SRC_LMY_005, SRC_LMY_006 (2) |
| marcus-agrippa | SRC_MA_006, SRC_MA_007 (2) |
| octavia-minor | SRC004 (1) — namespaced as `octavia-minor__SRC004` |
| qiu-ying | SRC_QY_017 (1) |
| sextus-pompey | SRC005 (1) — namespaced as `sextus-pompey__SRC005` |
| shen-zhou | SRC003 (1) — namespaced as `shen-zhou__SRC003` |
| tang-yin (pilot) | SRC_TY_005, SRC_TY_006 (2) — already banner'd |
| wang-ao | SRC003, SRC004 (2) — namespaced as `wang-ao__SRC003`, `wang-ao__SRC004` |
| wen-zhengming | SRC_WZM_005, SRC_WZM_006 (2) |
| wu-kuan | SRC_WK_005 (1) |
| xu-zhenqing | SRC_XZQ_004, SRC_XZQ_005 (2) |
| zhu-yunming | SRC_ZYM_004, SRC_ZYM_005 (2) |

Generator rule: emit the `🚫 D-LEVEL — CLUE ONLY` banner directly under the H1 for every source whose `reliability_level == 'D'` OR `verification_status == 'clue_only'`. Banner text is the canonical 4-line block established in the pilot v2 gap-fix.

augustus-octavian, mark-antony, wang-yangming, gnaeus-pompeius-magnus reported 0 D-level sources in the dry-run scan — verify at generation time.

---

## 8. Cross-package collisions (informational)

For completeness, the survey detected that **claim IDs** also collide across the 8 generic-ID packages — `C001` is used by 8 packages, `C002` by 8, etc., up through `C020`. This does **not** affect the import directly because claim IDs do not become filenames — they appear only as table cells inside person notes. But it does mean:

- `[[CLM_TY_001]]`-style claim wikilinks (which the pilot uses) cannot be uniformly extended to generic-ID packages without rewriting.
- The pilot's `## Used For Claims` cross-references in source notes (`[[tang-yin#Confirmed Historical Claims|CLM_TY_001]]`) work only because Tang Yin uses namespaced claim IDs. For generic-ID packages, the cross-reference becomes `[[shen-zhou#Confirmed Historical Claims|C001]]` — which is unambiguous because the heading anchor scopes it to the right person.

No generator change is required for claim IDs in this import.

---

## 9. Vault folder structure changes

Both the repo pilot folder and the vault target gain (under Option B, into the sandbox first):

```
obsidian-vault-pilot/_dryrun_22_v1/
├── 00_Project/             (placeholder, empty)
├── 01_Persons/
│   ├── Chinese/            ← 12 .md files
│   └── Western/            ← 10 .md files
├── 02_Events/              (empty — Phase D deferred)
├── 03_Sources/
│   ├── Chinese/            ← 112 .md files (per §4b)
│   └── Western/            ← 91 .md files (per §4b)
├── 04_Relationships/       (empty — Phase D deferred)
├── 05_Works/               (empty — Phase D deferred)
├── 06_Visual_Media/        (empty — no images imported)
├── 90_Staging_Review/      ← _import_log.md, _validation_results.md (written by generator)
└── 99_Templates/           ← symlink or copy of pilot templates for reviewer reference
```

Promotion (on approval) replaces `obsidian-vault-pilot/_dryrun_22_v1/` contents into `obsidian-vault-pilot/` proper (excluding pilot overrides per §6), then mirrors the entire `obsidian-vault-pilot/` tree to the vault.

---

## 10. Recommended import mode

| Option | Description | Recommendation |
|--------|-------------|----------------|
| A | Generate all 22 directly into `obsidian-vault-pilot/` and mirror to live vault | **Not recommended.** Overwrites 19 reviewed pilot files; namespacing is unverified; vault sync amplifies any error to all your devices. |
| B | Generate into `obsidian-vault-pilot/_dryrun_22_v1/` first, reviewer approves, promote | **RECOMMENDED.** Catches every issue before touching the pilot or vault; reviewer can diff sandbox vs. pilot to confirm format parity. |
| C | Generate 5 representative persons first | Acceptable fallback, but doesn't surface all 8 generic-ID packages in one pass. Useful as a sub-step inside Option B if Option B's full 22-pass is too noisy. |

**Pick: B.** Sandbox path: `obsidian-vault-pilot/_dryrun_22_v1/`. No writes to the live vault until promotion.

If the user prefers a hybrid: do Option C **inside** Option B — generate 5 representative persons (1 from each of MVP-Chinese, MVP-Western, B1-Chinese, B1-Western, B2-generic-ID) into the sandbox first, eyeball them, then expand to the full 22 in the same sandbox. This double-gates the work without forcing two separate sandboxes.

---

## 11. Risks summary

| Risk | Severity | Mitigation |
|------|----------|------------|
| Source-ID collision across 8 generic-ID packages | **High** | Filename namespacing (§3c) — codified in plan, validated in dry-run |
| Pilot files overwritten and silently degraded | **High** | Option B sandbox; promotion-time per-file approval |
| OneDrive/Syncthing conflict files generated during write | Medium | Single atomic `cp -r` from sandbox to vault, after sandbox approval — not file-by-file |
| Generator drift from human-curated pilot wording | Medium | Diff sandbox tang-yin.md vs. pilot tang-yin.md; treat any diff as a regression to investigate |
| Missing D-LEVEL banner on a source note | Medium | Generator rule §7 + automated post-generation grep validation |
| Empty Phase-D folders treated as broken/incomplete | Low | `.gitkeep` in repo, README in `90_Staging_Review/` explaining deferral |
| augustus-octavian, mark-antony, wang-yangming, gnaeus-pompeius-magnus D-level scan reported 0 | Low | Re-verify at generation time — may genuinely have 0, or convention used unrecognized labels |
| User opens the sandbox in the live Obsidian vault and indexes 200+ files into the graph | Low | Promote sandbox to vault only after approval; until then sandbox lives in repo only |

No blocking issues. All risks have a mitigation.

---

## 12. What is safe to do next

After the user reviews this dry-run report and approves:

1. Mark this report `approved` in `90_Staging_Review/` (post-import folder).
2. Implement the generator (script or templater workflow) per `_22_person_import_plan_v1.md` §4 + §5.
3. Run the generator into `obsidian-vault-pilot/_dryrun_22_v1/`.
4. Validate the sandbox output (frontmatter parses, wikilinks resolve, D-LEVEL banners present, no pilot overwrite).
5. User opens the sandbox in Obsidian (separate vault session preferred).
6. On approval, promote sandbox → `obsidian-vault-pilot/`, mirror to live vault.
7. Write `90_Staging_Review/_import_log.md`, `_validation_results.md`, `_known_issues.md`.

The 22-person import is **safe to plan and dry-run** (this report). It is **NOT yet safe to execute** — the namespacing convention and pilot-overwrite policy need explicit user sign-off first.
