# 22-Person Obsidian Import Plan v1

**Date:** 2026-05-17
**Branch:** `planning/obsidian-22-person-import-v1`
**Status:** Planning only — no files generated into the live Obsidian vault yet
**Predecessor:** `_obsidian_import_plan_v1.md` (vault-structure plan), `_pilot_gap_fix_report_v2.md` (pilot format-complete)
**Companion:** `_22_person_import_dry_run_v1.md` (this plan + the dry-run together gate the import)

---

## 1. Scope

Import all 22 staging-ready persons enumerated in `_current_22_person_inventory_v1.md`. No new collection. No master promotion. No simplified data model. No UI/dashboard layer.

| Batch | Count | Persons |
|-------|-------|---------|
| MVP | 7 | shen-zhou, wang-yangming, qiu-ying, wu-kuan, gnaeus-pompeius-magnus, augustus-octavian, mark-antony |
| B1  | 8 | tang-yin, wen-zhengming, zhu-yunming, xu-zhenqing, julius-caesar, cicero, cleopatra-vii, marcus-agrippa |
| B2  | 7 | li-dongyang, wang-ao, li-mengyang, he-jingming, lepidus, octavia-minor, sextus-pompey |
| **Total** | **22** | (12 Chinese + 10 Western) |

The pilot persons (tang-yin, julius-caesar) are included in scope but are subject to the overwrite-handling rules in §10.

---

## 2. Output target

Two parallel destinations remain, per the canonical/working-copy split established in the pilot:

| Role | Path | Git? |
|------|------|------|
| Canonical generated output | `obsidian-vault-pilot/` (in repo) | yes |
| Working/readable copy | `/mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/` (Windows: `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\`) | no |

Generation writes to the canonical path first. Mirror is `cp -r` to the vault after each batch. Mirror direction: repo → vault, one-way.

For the actual 22-person run, dry-run output lands in a sibling sandbox (see §10) so the live vault is not perturbed until the user signs off.

---

## 3. Input source

For each of the 22 person packages under `incoming/<culture>/<slug>/`, the generator reads:

| File | Purpose |
|------|---------|
| `person_record.json` | person_id, canonical_key, display name, dates, period, culture |
| `person_profile.md` | Summary prose (long-form) |
| `claims.jsonl` | All structured claims (Confirmed / Probable / Disputed / Reception / Legendary tables) |
| `sources.jsonl` | Source-note generation, plus the `## Sources` section grouped by reliability |
| `relationships.jsonl` | `## Relationships` table |
| `events.jsonl` | `## Life Timeline` table (no standalone event notes in this import) |
| `works.jsonl` | `## Works` table |
| `legendary_notes.jsonl` | Cross-input to the Reception / Legendary section |
| `visual_media.jsonl` | Metadata note inside person note only — no images, no standalone visual-media notes |

`incoming/` is read-only for this import. The generator must not write to it.

---

## 4. Generated output per person

One Markdown file per person under `01_Persons/Chinese/<canonical_key>.md` or `01_Persons/Western/<canonical_key>.md`, following the structure validated by the pilot (and codified in `obsidian-vault-pilot/99_Templates/tpl-person.md`):

1. **YAML frontmatter** — all 14 spec'd keys (`person_id`, `canonical_key`, `display_name`, `primary_language`, `culture`, `period`, `birth`, `death`, `historical_status: ai_collected_unreviewed`, `review_status`, `source_sufficiency`, `data_source_folder`, `tags[]`, `related_people[]`).
2. **`⚠️ AI-COLLECTED / STAGING ONLY`** banner directly under the H1.
3. **`## Summary`** — bilingual ZH + EN paragraphs derived from `person_record.json.short_description_*`. Must not assert reception material as fact.
4. **`## Identity`** — table of name forms, dates with era, place of origin/death, primary role, culture.
5. **`## Life Timeline`** — table of (Year, Event, Status) from `events.jsonl` + key dates from `person_record.json` / `person_profile.md`.
6. **`## Key Historical / Reception / Legend / Fiction Separation`** — narrative subsections: Confirmed Historical Facts / Source Caveats / Disputed or Uncertain / Reception or Later Groupings / Legendary or Fictional.
7. **`## Claims Overview`** — count table by status (Confirmed / Probable / Disputed / Reception / Legendary / Total).
8. **`## Confirmed Historical Claims`** — table of (claim_id, date, statement, sources) filtered to `confidence ∈ {confirmed}` and `claim_type ∈ {biography, "", null}`.
9. **`## Probable / Disputed / Needs Verification Claims`** — combined table for `confidence ∈ {probable, disputed, needs_verification, low, high}` (biography). Status column distinguishes each row.
10. **`## Reception / Legendary / Fictional Material`** — table for `claim_type ∈ {reception_label, later_grouping_only, legend, fiction, folklore}`. Wording must use "later regarded as…" / "后世美术史中常被视为…" per MVP rules v2.5.
11. **`## Relationships`** — table of (Person, Relationship Type, Status, Sources, Notes) from `relationships.jsonl`. Use only allowed relationship types. Forward wikilinks to other persons.
12. **`## Works`** — table of (Work, Type, Status, Sources, Notes) from `works.jsonl`. Callout: `artwork_by_person` ≠ portrait likeness.
13. **`## Sources`** — grouped by reliability into 4 buckets: A/A_candidate; B_high/B; C/D/clue_only; ⚠️ Flagged needs_verification. Each row: `[[SRC_*]]` | Title | Type | Reliability | Verification Status.
14. **`## Source Package`** — path back to `incoming/<culture>/<slug>/`, file count, validation status.
15. **`## Review Status`** — current label, source sufficiency, listed next review actions.
16. **`## Open Questions`** — items from `open_questions.md`.

Filename = `{canonical_key}.md`. UTF-8, LF endings, no BOM.

---

## 5. Source notes

One source note per unique `(canonical_key, source_id)` pair. **Critical:** source_id is NOT globally unique across the 22 packages — see Dry-Run §SRC for the namespacing problem. The plan addresses this by **filename namespacing**:

| Package convention | Filename strategy | Example |
|---------------------|-------------------|---------|
| Already-namespaced source_ids (`SRC_TY_NNN`, `SRC_JC_NNN`, `SRC_CC_NNN`, `SRC_WZM_NNN`, etc. — 14 packages) | Filename = `{source_id}.md` (unchanged) | `SRC_TY_001.md` |
| Generic source_ids (`SRC001`, `SRC002`, etc. — 8 packages) | Filename = `{canonical_key}__{source_id}.md` (double-underscore separator) | `shen-zhou__SRC001.md` |

Why: Obsidian wikilinks resolve by filename. With 8 packages each using `SRC001`, a bare `SRC001.md` filename would collide. Double-underscore namespacing is reversible, machine-readable, and visible to the reviewer.

Wikilinks from person notes follow the same namespacing:
- Tang Yin's claims use `[[SRC_TY_001]]` (already namespaced).
- Shen Zhou's claims must use `[[shen-zhou__SRC001]]` (generator must rewrite at emit time — the JSONL data keeps `SRC001` as the structured ID).

Source-note structure (per `obsidian-vault-pilot/99_Templates/tpl-source.md`):

- Frontmatter: `source_id`, `title`, optional `title_zh`/`title_en`, `source_type`, `reliability_level`, `verification_status`, `language`, `used_for_claim_ids[]`, `review_status: ai_collected_unreviewed`.
- H1 title.
- **`🚫 D-LEVEL — CLUE ONLY`** banner directly under H1 — required for every source with `reliability_level == D` OR `verification_status == clue_only` (30 such notes across all 22 packages per dry-run §D).
- `## Source Metadata` — bullet list (Source ID, Type, Reliability, Verification, Language, Citation).
- `## Used For Claims` — reverse wikilinks to claim anchors in person notes: `[[<canonical_key>#Confirmed Historical Claims|<claim_id>]]`. For D-level, replace with the boilerplate "None — clue only" paragraph.
- `## Notes` — author/period, editorial framing, edition details, what needs verification.
- `## Review Warning` — `⚠️ AI-COLLECTED / STAGING ONLY` banner at the bottom.

Duplicate suppression: source notes are emitted once per `(canonical_key, source_id)`. Since SRC001/etc. are package-local IDs (not actually shared sources), the dedup key is the namespaced filename. No actual shared-source merging happens in this import (deferred to a later phase when source_id global identity is established).

---

## 6. Folders

After the import, both the repo pilot output and the vault target must contain:

```
00_Project/
01_Persons/Chinese/         ← 12 person notes
01_Persons/Western/         ← 10 person notes
02_Events/                  ← empty (deferred per Phase D)
03_Sources/Chinese/         ← Chinese-package source notes (count per dry-run)
03_Sources/Western/         ← Western-package source notes (count per dry-run)
04_Relationships/           ← empty (deferred per Phase D)
05_Works/                   ← empty (deferred per Phase D)
06_Visual_Media/            ← empty (no images imported)
90_Staging_Review/          ← post-import _import_log.md, _validation_results.md, _known_issues.md
99_Templates/               ← tpl-person.md, tpl-source.md (carried over from pilot)
```

Empty folders use `.gitkeep` in the repo only; the vault leaves them empty.

The dry-run sandbox (§10) uses a parallel structure under `_dryrun_22_v1/` so the live pilot folder is not touched until the user approves promotion.

---

## 7. Do not generate yet

This is a plan + dry-run pass. The dry-run report enumerates expected output paths, counts, and risks. No person notes or source notes for the other 20 persons are written to either the repo pilot folder or the Obsidian vault in this commit.

When generation is approved (next phase), the generator will:
1. Emit to the dry-run sandbox first (`obsidian-vault-pilot/_dryrun_22_v1/`).
2. The user reviews the sandbox files locally (or in a temporary Obsidian vault folder).
3. On approval, the sandbox is promoted to `obsidian-vault-pilot/` proper, then mirrored to the vault.

---

## 8. Dry-run report

See `_22_person_import_dry_run_v1.md`. Key items it answers:
- Inventory of 22 packages found and validated.
- Expected output filename for every person note and every source note (with namespacing applied).
- Claim and source counts per person, totals.
- ID collision analysis: which packages collide on `SRC001`/`SRC002`/...`SRC017` and `C001`...`C020`.
- All 30 D-level sources that need the `🚫 D-LEVEL — CLUE ONLY` banner.
- Filename collision detection against the existing pilot.
- Missing files / malformed JSON: none, all 22 packages parse cleanly.
- Orphan source references (claims/etc. pointing to non-existent `source_id`): none.
- Overwrite-conflict resolution for tang-yin.md and julius-caesar.md (existing pilot).
- Recommended import mode (A / B / C) with rationale.

---

## 9. Safety

Hard restrictions for this and the next generation pass:

- Do not modify any file under `incoming/`.
- Do not commit anything under the Obsidian vault path. The vault is not a git repo.
- Do not copy `.obsidian/`, `.stfolder`, `.stignore`, or any OneDrive / Syncthing conflict files into the repo.
- Do not write outside `obsidian-vault-pilot/` and `reviewed/staging/obsidian_import/` on the repo side.
- Do not edit any vault file outside `01-Projects/Historical-Persons-Wiki/`.
- Do not collect new persons. Do not promote staging to master. Do not build dashboards / UI / simplified-model overlays in this phase.
- Do not overwrite tang-yin.md / julius-caesar.md or any existing pilot source note unless explicit conflict-resolution decision §10 says so.
- Do not skip the dry-run sandbox in favour of generating in place.

---

## 10. Recommendation — preferred import mode

**Recommendation: Option B — generate a separate dry-run folder first.**

Rationale:
1. **Source-ID namespacing must be applied for the first time at the 20 non-pilot packages.** This is a non-trivial generator behaviour — the sandbox lets reviewers verify the namespacing is correct before it lands in the live vault.
2. **Pilot files (tang-yin.md, julius-caesar.md) and 17 pilot source notes already exist** in `obsidian-vault-pilot/`. In-place generation would overwrite the pilot — which has been visually reviewed and accepted. A regression in the generator could silently degrade the format the user has signed off on.
3. **Vault is OneDrive + Syncthing synced.** Writing 100+ Markdown files into the live vault triggers cloud propagation. A sandbox lets us batch the final copy as one well-formed atomic operation rather than streaming intermediate states to other devices.
4. The 5-representative-persons option (C) is faster but doesn't surface the collision risks across all 8 generic-ID packages in one pass. Option B catches every problem before any of it touches the live pilot or vault.

**Sandbox path:** `obsidian-vault-pilot/_dryrun_22_v1/` (in repo, git-tracked).

**Promotion plan (after sandbox approval):**
1. User reviews the sandbox folder in Obsidian (by temporarily opening that folder as a vault, or by copying it into a scratch location inside the vault under `01-Projects/Historical-Persons-Wiki/_dryrun_22_v1/`).
2. User signs off on format and on conflict-resolution choices for the pilot files (the dry-run report's §"Overwrite conflict resolution" proposes "keep pilot as-is — generator output for tang-yin and julius-caesar goes into `_dryrun_22_v1/01_Persons/.../` for diff-comparison only").
3. On approval, mv/cp the sandbox into the canonical pilot folder, mirror to vault, and write `90_Staging_Review/_import_log.md`.

Options A and C are documented in the dry-run report but not recommended given the findings.

---

## 11. What this plan does NOT cover (out of scope)

- Phase D standalone notes in `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/` — deferred until after the 22-person Phase A+B+C import is approved.
- A simplified UI / dashboard layer — explicitly out of scope per the task brief.
- Reconciling globally-shared sources across packages. The 17 source_id "collisions" in the survey are *not* actually shared sources — they are independent sources reusing the same generic ID in different packages. True cross-package source deduplication requires reviewer-led identity resolution and is deferred.
- Backfilling namespaced source/claim IDs into the generic-ID packages' `incoming/` JSONL files. The data is not edited; namespacing happens only at filename/wikilink emission time.
- `00_Project/` content (project README, glossary, collection rules summary, review-status dashboard) — recommend a separate task after Phase A+B+C is in.

---

## 12. Acceptance gates

The 22-person import may proceed when ALL of the following hold:

1. Dry-run report (`_22_person_import_dry_run_v1.md`) is reviewed and approved by the user.
2. The user has confirmed the proposed source-filename namespacing convention (`{canonical_key}__{source_id}.md` for generic-ID packages).
3. The user has confirmed the pilot files (tang-yin.md, julius-caesar.md) are NOT to be overwritten during the 22-batch generation — generator output for those two persons goes to the sandbox only, for diff-comparison.
4. The user has chosen import mode (B recommended).
5. The generator is implemented or the manual import is scheduled.

Once gates 1–4 pass, generation proceeds into the sandbox. Gates 5+ are operational (writing the generator script and validating its output) and live in a follow-on task.
