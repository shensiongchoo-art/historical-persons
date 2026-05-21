# Post-Mirror Cleanup Report v1

**Date:** 2026-05-21
**Branch:** `cleanup/pilot-marcus-antonius-link-v1` (off `main`)
**Scope:** Single trivial link fix in the preserved Julius Caesar pilot note. Two occurrences of `[[marcus-antonius]]` replaced with `[[mark-antony]]` in both the repo pilot file and the live Obsidian vault file.
**Predecessors:** `_post_import_cleanup_plan_v1.md` §1 (where this fix was documented as deferred pending explicit user approval), `_29_person_live_mirror_report_v1.md` §8 (which identified the same 2 occurrences as the only remaining unresolved person wikilinks in the live vault).

---

## 1. Files changed

| # | File | Path | Change |
|---|------|------|--------|
| 1 | Repo pilot | `obsidian-vault-pilot/01_Persons/Western/julius-caesar.md` | 2 lines changed: `[[marcus-antonius]]` → `[[mark-antony]]` |
| 2 | Live vault | `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\01_Persons\Western\julius-caesar.md` | Same 2 lines |

**MD5 transition** (both files in lock-step):

- Pre-fix: `4f6d324c50701ae8da29a6b0899324f3`
- Post-fix: `84e7da1c2d395d59b90105a220286cdb`

Both files post-fix are byte-identical (matching MD5) — repo and vault remain in sync for the pilot.

---

## 2. Links fixed

Exactly 2 link occurrences updated per file (4 total across the two files):

| File | Line | Old | New | Context |
|------|------|-----|-----|---------|
| both | 24 | `"[[marcus-antonius]]"` | `"[[mark-antony]]"` | `related_people:` frontmatter |
| both | 160 | `([[marcus-antonius]])` | `([[mark-antony]])` | Relationships table Person column |

The Relationships table row's display text "Marcus Antonius / Mark Antony" was kept as-is — only the wikilink target inside the parentheses changed.

### Resolution proof

- `[[mark-antony]]` resolves to existing note at `H:\…\01_Persons\Western\mark-antony.md` (verified present, 28,074 bytes).
- Live vault person-wikilink unresolved count: **0** (down from 2 before this fix).
- Repo pilot file: previously the only file emitting unresolved `[[marcus-antonius]]` — now resolves.

---

## 3. Diff scope

`git diff` shows exactly 2 insertions and 2 deletions on the repo pilot file, both on the lines documented above. No collateral changes.

```diff
@@ -21,7 +21,7 @@ tags:
   - batch-1
 related_people:
   - "[[gnaeus-pompeius-magnus]]"
-  - "[[marcus-antonius]]"
+  - "[[mark-antony]]"
   - "[[cleopatra-vii]]"
@@ -157,7 +157,7 @@ ...
-| Marcus Antonius / Mark Antony ([[marcus-antonius]]) | documented_association | ...
+| Marcus Antonius / Mark Antony ([[mark-antony]]) | documented_association | ...
```

---

## 4. Source-link preservation check

| Metric | Pre-fix | Post-fix |
|--------|---------|----------|
| Repo pilot `[[SRC_JC_*]]` link count | 55 | **55** (unchanged) |
| Vault pilot `[[SRC_JC_*]]` link count | 55 | **55** (unchanged) |

No source wikilinks touched. The fix is scoped strictly to the 2 person-link occurrences.

---

## 5. Live vault link health (post-fix)

| Metric | Value |
|--------|-------|
| Person wikilinks scanned across all 29 vault person notes | **207** |
| Unresolved person wikilinks | **0** |

The vault now has **zero unresolved person wikilinks** — a clean state since pilot import began. Down from the documented 2 unresolved that were carried through every mirror up to this point.

---

## 6. Safety checks (all passed)

| Check | Result |
|-------|--------|
| `incoming/` modified | ✅ untouched (`git status incoming/` empty) |
| `.obsidian/` in project folder | ✅ 0 (vault-root `.obsidian/` preserved) |
| `.stfolder/` in project folder | ✅ 0 (vault-root `.stfolder` preserved) |
| `.stignore` in project folder | ✅ 0 (vault-root `.stignore` preserved) |
| Vault-root `.obsidian/`, `.stfolder`, `.stignore` (must still be 3) | ✅ 3 present, untouched |
| OneDrive `*Sync-Conflict*` / Syncthing `*.sync-conflict-*` in project folder | ✅ 0 |
| Repo pilot and vault pilot MD5 in sync (both files identical) | ✅ both `84e7da1c…` |
| Pilot person notes other than Julius Caesar (Tang Yin) untouched | ✅ `tang-yin.md` MD5 still `688cc12e…` |
| 27 other person notes in vault untouched | ✅ no rewrites |
| 274 source notes in vault untouched | ✅ no rewrites |
| Other PARA folders in vault (`00-Inbox/`, `02-Areas/`, etc.) | ✅ untouched |

---

## 7. Remaining warnings

| # | Severity | Description | Status |
|---|----------|-------------|--------|
| 1 | Info | 18 duplicate TY/JC namespaced source notes in vault (0 inbound references) | Carried over; optional cleanup |
| 2 | Info | 134 unresolved person *references* in the v3 generator manifest (63 distinct names) — rendered as plain text in Relationships tables, NOT as broken wikilinks; mostly persons not yet in the 29-person set | Documented in `_29_person_dryrun_generation_report_v1.md` §6; non-blocking |
| 3 | Cosmetic (deferred) | Em-dash `—` Status column where source JSONL lacks the field | Deferred to generator v4 |
| 4 | Cosmetic (deferred) | Augustus + Mark-Antony Relationships row formatting for related-persons whose JSONL lacks `related_person_name` | Deferred to generator v4 |
| 5 | Info | OneDrive + Syncthing will sync this 1 file change to other devices over the next sync cycle | Expected |

No blocking warnings. The previously-documented "pilot link drift" item from `_post_import_cleanup_plan_v1.md` §1 is now **resolved**.

### Resolved by this PR

- ✅ Pilot vault `julius-caesar.md` `[[marcus-antonius]]` → `[[mark-antony]]` (2 occurrences) — both files now use the canonical link.

---

## 8. Is the live Obsidian vault still ready for human review?

**✅ Yes — and now strictly cleaner than before.**

- All 29 person notes still present and accessible.
- All 274 source notes still present.
- All 42 D-LEVEL banners still in place.
- Pilot files (Tang Yin + Julius Caesar) still preserved (Tang Yin MD5 unchanged; Julius Caesar deliberately updated by this PR per explicit user authorisation).
- **Person wikilinks now 100% resolved** in the live vault — `0/207` unresolved (down from `2/207`).
- Source wikilinks remain 100% resolved.
- No vault config files touched. No sync conflicts. No `incoming/` edits. No new collection.

---

## 9. What this PR does NOT do

- Does not delete the 18 namespaced TY/JC duplicate source notes (still deferred).
- Does not generate standalone event/work/relationship notes (still deferred).
- Does not patch the generator (the v3 generator's emitted output for `julius-caesar.md` was excluded from the mirror by design; the file edited here is the preserved pilot, which the generator does not regenerate).
- Does not modify `incoming/`.
- Does not promote anything to master.
- Does not modify any other person note, source note, vault folder, or repo file.
- Does not touch `.obsidian/`, `.stfolder/`, `.stignore`, or any sync-conflict file.
