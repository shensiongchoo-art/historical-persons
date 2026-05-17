# Pilot Gap-Fix Report v1

**Date:** 2026-05-17
**Scope:** 2-person Obsidian import pilot (Tang Yin + Julius Caesar)
**Plan reference:** `reviewed/staging/obsidian_import/_obsidian_import_plan_v1.md`
**Rules reference:** `project-rules/MVP_COLLECTION_RULES_V2_5.md`
**Status:** Completed — pilot now covers Phase A + Phase B + Phase C (full) + partial Phase D

---

## 1. Missing Caesar source notes created

| Source ID | Status | Repo path | Vault path |
|-----------|--------|-----------|------------|
| `SRC_JC_008` (Wikipedia: Julius Caesar) | Created | `obsidian-vault-pilot/03_Sources/Western/SRC_JC_008.md` | `01-Projects/Historical-Persons-Wiki/03_Sources/Western/SRC_JC_008.md` |
| `SRC_JC_009` (Britannica: Julius Caesar) | Created | `obsidian-vault-pilot/03_Sources/Western/SRC_JC_009.md` | `01-Projects/Historical-Persons-Wiki/03_Sources/Western/SRC_JC_009.md` |

Format matches existing source notes (frontmatter keys: `source_id`, `title`, `title_zh`, `source_type`, `reliability_level`, `verification_status`, `language`, `used_for_claim_ids`, `review_status`). Both files carry the `⚠️ AI-COLLECTED / STAGING ONLY` warning.

**Deviation from v1 plan §7 noted:** the original import plan stated that D-level / clue_only sources should appear inline in person source lists without standalone notes. These two notes were created on explicit instruction to make Caesar source coverage match `sources.jsonl` 1:1. The notes are flagged inside as "exists for record-keeping completeness" so future reviewers understand the intent.

---

## 2. Relationships sections added

Both `tang-yin.md` and `julius-caesar.md` now have a `## Relationships` section with the spec'd columns: **Person | Relationship Type | Status | Sources | Notes**.

| Person note | Rows added | Source data |
|-------------|------------|-------------|
| Tang Yin    | 6 | `incoming/chinese/tang-yin/relationships.jsonl` |
| Julius Caesar | 6 | `incoming/western/julius-caesar/relationships.jsonl` |

Rules applied:
- Only `relationship_type` values present in source JSONL used (`probable_association`, `later_grouping_only`, `probable_teacher_student`, `opponent`, `same_political_context`, `documented_association`, `family`).
- No friendship/influence inferred beyond source evidence.
- `source_ids` rendered as `[[SRC_*]]` wikilinks.
- Related persons rendered as forward-style wikilinks (e.g. `[[shen-zhou]]`) where a `canonical_key` is implied by `related_person_id`; plain text where `related_person_id` is empty (Zhou Chen 周臣, Marcus Junius Brutus). No new person notes were created.

---

## 3. Works sections added

Both person notes now have a `## Works` section with columns: **Work | Type | Status | Sources | Notes**.

| Person note | Rows added | Source data |
|-------------|------------|-------------|
| Tang Yin    | 5 (1 collected_writings + 4 paintings) | `incoming/chinese/tang-yin/works.jsonl` |
| Julius Caesar | 2 (2 historical_commentary) | `incoming/western/julius-caesar/works.jsonl` |

Each section includes a visible callout reminding the reviewer that `artwork_by_person` ≠ portrait likeness, per MVP rules v2.5 visual-media discipline.

No standalone work notes were created in `05_Works/` (deferred — see §9).

---

## 4. Sources sections added

Both person notes now have a `## Sources` section grouped into four buckets:

1. **A / A_candidate** — primary or near-primary
2. **B_high / B** — modern scholarship & ancient biography
3. **C / D / clue_only** — encyclopedia & general reference
4. **⚠️ Flagged: needs_verification** — re-listing of any source with `verification_status: needs_verification`

Table columns per spec: **Source ID | Title | Type | Reliability | Verification Status**.

Distribution:

| Person | A/A_candidate | B_high/B | C/D/clue_only | needs_verification (flagged) |
|--------|---------------|----------|---------------|------------------------------|
| Tang Yin | 4 | 3 | 2 (SRC_TY_005, SRC_TY_006 — plain text, no notes) | 2 (SRC_TY_004, SRC_TY_007) |
| Julius Caesar | 3 | 4 | 2 (SRC_JC_008, SRC_JC_009 — now have notes) | 0 |

Source IDs that have a standalone note are rendered as `[[SRC_*]]` wikilinks. SRC_TY_005 / SRC_TY_006 are rendered as plain text with an inline note explaining D-level clue-only sources have no standalone notes per v1 plan §7.

---

## 5. Vault folders scaffolded

Created in **both** the repo pilot and the Obsidian vault:

- `00_Project/`
- `02_Events/`
- `04_Relationships/`
- `05_Works/`
- `06_Visual_Media/`
- `90_Staging_Review/`
- `99_Templates/`

In the repo, each folder contains a `.gitkeep` placeholder so the structure is committed to git. In the Obsidian vault, folders are left empty (the vault is not git-tracked).

No standalone notes were generated inside any of these folders.

---

## 6. Files mirrored to Obsidian vault

| File | Repo (canonical) → Vault (working copy) | Verified |
|------|------------------------------------------|----------|
| `01_Persons/Chinese/tang-yin.md` | mirrored | `diff -q` clean |
| `01_Persons/Western/julius-caesar.md` | mirrored | `diff -q` clean |
| `03_Sources/Western/SRC_JC_008.md` | mirrored | `diff -q` clean |
| `03_Sources/Western/SRC_JC_009.md` | mirrored | `diff -q` clean |

Mirror direction: repo → vault (one-way). The 15 source notes mirrored in the earlier pass remain unchanged.

Vault folder structure now matches the repo pilot structure 1:1 (minus `.gitkeep` placeholders).

---

## 7. Files skipped

No files skipped during this gap-fix pass. Specifically excluded by safety policy and not touched:

- `incoming/**` — source data (read only)
- `.obsidian/` — vault config (never copied)
- `.stfolder` / `.stignore` — Syncthing markers
- Any OneDrive/Syncthing conflict files (none present at time of pass)
- The 20 other staging persons in `reviewed/staging/persons/` — out of pilot scope

---

## 8. Source link resolution

All `[[SRC_*]]` wikilinks in both pilot person notes resolve to existing source notes in `03_Sources/`:

- `tang-yin.md` — 7 unique source wikilinks, **0 unresolved** (SRC_TY_001/002/003/004/007/008/009 all present).
- `julius-caesar.md` — 9 unique source wikilinks, **0 unresolved** (SRC_JC_001–009 all present).

Forward wikilinks to other persons (`[[shen-zhou]]`, `[[cicero]]`, etc.) intentionally remain unresolved — these will only resolve when the rest of the 22-person batch is approved and imported. Obsidian's graph view will show them as outline nodes. This is by design per the user's instruction: "do not create new person notes."

---

## 9. Phase D standalone notes — recommendation

**Recommendation: defer.** Phase D standalone notes inside `02_Events/`, `04_Relationships/`, `05_Works/`, and `06_Visual_Media/` are not necessary for the 2-person pilot to be reviewable.

Reasoning:
- The Phase B claims tables + new Relationships / Works tables already give a reviewer everything they need to audit each person's package end-to-end.
- Standalone event/work notes mainly add value when **multiple persons share an event or work** (e.g. Battle of Actium, First Triumvirate). With only Tang Yin + Caesar in the vault, no event or work is currently shared.
- Once the 22-person batch is approved and imported, shared events (e.g. `battle-of-actium.md`, `ides-of-march-44-bce.md`) will pay off as crossroads in the graph view. At that point, generate them all at once from the unioned `events.jsonl` / `works.jsonl` data rather than piecemeal.

Suggested trigger for Phase D: **after the 22-person Phase A+B+C import is approved**, regenerate Phase D notes in one pass.

---

## 10. Is full 22-person import safe yet?

**Not yet — one human gate remains.**

The pilot is now **format-complete enough to evaluate**:
- Frontmatter spec ✓
- Body structure (Summary → Identity → Timeline → Claims grouped → Reception/Legendary → Relationships → Works → Sources → Source Package → Review Status → Open Questions) ✓
- All MVP v2.5 disciplines visible (claim grouping, source-level calibration, reception language, visual-media disclaimer) ✓
- AI-COLLECTED / STAGING ONLY warning on every person and source note ✓
- Source links resolvable, forward person links explicitly deferred ✓

What still must happen before scaling to 22:

1. **Human format review of the pilot** — user opens `tang-yin.md` and `julius-caesar.md` in Obsidian, eyeballs them, signs off on format.
2. **Decide on the D-level source-note policy.** This pass deviated from v1 plan §7 to create SRC_JC_008/009 by instruction. Either: (a) accept the deviation as the new policy and backfill SRC_TY_005/006 for symmetry, or (b) revert the policy to v1 plan §7 and treat SRC_JC_008/009 as a one-off exception. Mixing both leaves the vault inconsistent.
3. **Decide whether to expand `00_Project/`, `90_Staging_Review/`, `99_Templates/`** with actual content (README, Collection Rules, Glossary, Review Status, Import Log, Validation Results, Known Issues, person template, source template) before the 22-batch, or after. Templates in particular are useful **before** scaling since they prevent format drift.
4. **Pilot-driven import script.** A 22-person manual import is feasible but error-prone — a generator script reading the `incoming/` JSONLs and emitting Markdown would produce more uniform output. The 2-person pilot can serve as the reference output for that script.

Once items 1–3 are decided, the 22-person import is safe to proceed. Item 4 is a strong recommendation but not strictly required.

---

## Validation summary

| Check | Result |
|-------|--------|
| YAML frontmatter parses on all 4 modified/created files | ✅ |
| All 7 SRC_TY_* wikilinks in tang-yin.md resolve | ✅ |
| All 9 SRC_JC_* wikilinks in julius-caesar.md resolve (incl. new 008/009) | ✅ |
| SRC_JC_008.md exists in repo AND vault | ✅ |
| SRC_JC_009.md exists in repo AND vault | ✅ |
| `incoming/` directory untouched | ✅ (`git status incoming/` empty) |
| Repo ↔ vault mirror byte-identical for 4 modified files | ✅ (`diff -q` clean) |
| `.obsidian/`, `.stfolder`, `.stignore` not copied into repo | ✅ |
| No new historical data collected | ✅ |
| 22-person import NOT triggered | ✅ |

---

## Next recommended actions

1. User opens the vault folder `01-Projects/Historical-Persons-Wiki/` in Obsidian and reviews:
   - `01_Persons/Chinese/tang-yin.md`
   - `01_Persons/Western/julius-caesar.md`
   - Graph view (cmd/ctrl + G)
2. User decides on the open policy questions in §10.
3. After format sign-off, commit `obsidian-vault-pilot/` changes to the repo.
4. Plan the 22-person Phase A+B+C import (script or manual) — separate task.
