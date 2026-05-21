# 29-Person Obsidian Internal MVP Baseline v1

## 1. Baseline name

**29-Person Obsidian Internal MVP Baseline (v1)**

This is the first formally-closed Obsidian baseline of the Historical Persons Database. It marks the state of the live Obsidian vault as accepted for **internal review use** after human visual approval.

---

## 2. Date / branch / commit context

| Field | Value |
|-------|-------|
| Baseline date | 2026-05-21 |
| Closing branch | `baseline/29-person-obsidian-mvp-v1` (this PR) |
| `main` HEAD at baseline | `328497b` (post-merge of PR #43) |
| Last linked merge to `main` | PR #43 — `cleanup: pilot Julius Caesar — [[marcus-antonius]] → [[mark-antony]] (2 links)` |
| Pilot file MD5 (Tang Yin) | `688cc12e0baacf706e51d1b6deb582d5` |
| Pilot file MD5 (Julius Caesar, post-cleanup) | `84e7da1c2d395d59b90105a220286cdb` |
| Open PRs at baseline close | **#42** — `mirror: 29-person Obsidian dry-run v1 + generator v3` (still OPEN; underlies this baseline's live-vault state; see §11) |
| `incoming/` state | clean — `git status incoming/` empty |
| Generator referenced | `tools/obsidian_dryrun_generator.py` (v3 — registry-based person-link resolution; on PR #42 branch) |

### Merge sequence that produced this baseline (chronological)

| PR | Squash commit | Subject |
|----|----|----|
| #34 | `b00b1f8` | plan + dry-run + mirror: 22-person Obsidian import |
| #35 | `30f60af` | cleanup: 22-person post-import — link drift fixes + cleanup plan v1 |
| #37 | `150ccdb` | Verification: Batch 3 Crassus + Brutus source check — all 13 sources confirmed |
| #36 | `dfca6a4` | Collect Batch 3: Crassus and Brutus packages (v2.5) |
| #38 | `8e7c719` | Plan: Batch 4 candidate scope — 5 recommended, 2 deferred |
| #39 | `7265486` | Collect Batch 4 network expansion packages |
| #40 | `567b337` | triage: open PR review order for #35-#39 |
| #41 | (squash) | report: post-Batch 4 merge status v1 |
| **#42** | **NOT YET MERGED** | mirror: 29-person Obsidian dry-run v1 + generator v3 |
| #43 | `328497b` | cleanup: pilot Julius Caesar wikilink fix |

The state in the live Obsidian vault reflects the v3 generator's output plus the cleanup from #43, even though the v3 generator code itself is technically still on the PR #42 branch and not yet on `main`. See §11.

---

## 3. Live vault path

| Surface | Path |
|---------|------|
| Windows | `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` |
| WSL | `/mnt/h/OneDrive/obsidian-vault/01-Projects/Historical-Persons-Wiki/` |

Vault root contains a working `.obsidian/` configuration at `/mnt/h/OneDrive/obsidian-vault/`, separate from the project folder. The project folder follows the existing PARA structure under `01-Projects/`.

---

## 4. Accepted scope

| Metric | Count | Notes |
|--------|-------|-------|
| Person notes | **29** | 15 Chinese + 14 Western under `01_Persons/{Chinese,Western}/` |
| Source notes | **274** | 256 namespaced (`{slug}__{source_id}.md`) + 18 preserved pilot (`SRC_TY_001`–`009`, `SRC_JC_001`–`009`) |
| D-level source notes with 🚫 banner | **42** | 38 v3-emitted + 4 pilot — 0 missing banners |
| Templates | 2 | `99_Templates/tpl-person.md`, `tpl-source.md` |
| Unresolved person wikilinks across vault | **0** | (was 2 before PR #43) |
| Unresolved source wikilinks across vault | **0** | (1,733 source wikilinks scanned) |
| Total `.md` files under project folder | 305 | (29 + 274 + 2 + folder placeholders / empty scaffolds) |
| Folder scaffold present | yes | `00_Project/`, `02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/`, `90_Staging_Review/`, `99_Templates/` |

### Pilot files preserved (byte-identical across the mirror sequence)

| File | MD5 at this baseline | Status |
|------|------------------------|--------|
| `01_Persons/Chinese/tang-yin.md` | `688cc12e0baacf706e51d1b6deb582d5` | unchanged since first pilot import |
| `01_Persons/Western/julius-caesar.md` | `84e7da1c2d395d59b90105a220286cdb` | one trivial cleanup applied via PR #43 (2 person-link occurrences fixed; source links untouched) |

---

## 5. Accepted use

The 29-person Obsidian vault is accepted for:

1. **Internal review** — subject-matter experts can navigate the staging data via the vault, follow source citations, audit claim discipline, and surface review issues.
2. **Readable wiki reference** — the vault is the canonical *readable* surface of the historical persons knowledge base; structured `incoming/` JSON is the canonical *structured* surface.
3. **Staging knowledge base** — the vault represents `ai_collected_unreviewed` data that has cleared schema validation and visual review but has NOT been promoted to master.

Reviewers may use the vault to draft notes, mark up text in their own tools, and propose corrections. Any correction that affects underlying claims, sources, relationships, events, or works must be back-propagated to the GitHub `incoming/` JSON/JSONL (see §7).

---

## 6. NOT accepted as

The 29-person Obsidian vault is **NOT** accepted as:

1. **Master-approved historical database.** Every person carries the `⚠️ AI-COLLECTED / STAGING ONLY` banner. No claim, source, relationship, event, or work in this baseline has been master-promoted.
2. **Public-facing UI.** The vault is dense, jargon-heavy, and assumes reviewer familiarity with MVP rules v2.5. A simplified UI / dashboard layer is explicitly out of scope for this baseline.
3. **Final visual experience.** Tables show em-dashes for missing status data, some Relationships rows show plain text where the v3 generator could not confidently resolve a person, and 18 duplicate TY/JC source notes are present. These are tolerable for internal review but not for end-user presentation.
4. **Complete coverage.** 134 unresolved person references (63 distinct names) remain logged in the v3 generator's manifest — historical persons referenced in relationship data but not yet collected as their own packages.
5. **A self-syncing live system.** Manual edits to the vault do not propagate back to `incoming/`. See §7.

---

## 7. Source-of-truth policy

Codifying the directional flow established during the 22-person and 29-person mirrors:

| Surface | Role | Authority |
|---------|------|-----------|
| GitHub `incoming/*/` (JSON / JSONL) | **Structured source data** | Canonical |
| GitHub `obsidian-vault-pilot/` (generated Markdown) | Repo-side canonical generated output | Tracks `incoming/` via generator |
| `H:\…\Historical-Persons-Wiki\` (live Obsidian vault) | **Readable working copy** | Reflects repo-side canonical generated output |

### Direction of trust

- **Forward (canonical → readable):** `incoming/` → generator → `obsidian-vault-pilot/` → `rsync` mirror → live vault.
- **Reverse (manual vault edits):** must be **back-ported to `incoming/`** via a normal collection / verification PR before they become canonical. A vault edit that is not back-ported is treated as personal annotation only and will be overwritten by the next regeneration.

### Specific consequences

- Manual vault edits to wikilinks, claim text, or source citations have **no canonical effect** until they appear in `incoming/`.
- The next regeneration will overwrite any non-pilot vault file. The two pilot files (Tang Yin, Julius Caesar) remain protected by the `rsync --exclude` policy in the partial-promote mirror.
- New historical claims, sources, relationships, events, or works must enter via `incoming/` collection PRs, not via vault edits.
- Cleanup edits to the pilot files (like PR #43) are an exception: they require explicit user authorisation and the pilot MD5 is updated on the next regeneration's safety check.

---

## 8. Remaining non-blocking issues

| # | Issue | Severity | Cited in |
|---|-------|----------|-----------|
| 1 | 18 duplicate TY/JC namespaced source notes in vault (0 inbound references) | Info | `_post_import_cleanup_plan_v1.md` §2 |
| 2 | 134 unresolved person *references* (63 distinct names) — rendered as plain text in Relationships tables, not as broken wikilinks; mostly persons not yet in the 29-person set | Info | `_29_person_dryrun_generation_report_v1.md` §6 |
| 3 | Em-dash `—` Status column where source JSONL lacks the field | Cosmetic | `_22_person_dryrun_spotcheck_report_v1.md` §6 |
| 4 | Relationships row formatting for related-persons whose JSONL lacks `related_person_name` (mainly Augustus + Mark Antony) | Cosmetic | same as above |
| 5 | No standalone event / work / relationship notes generated yet (folder scaffold present but empty) | Deferred | `_post_import_cleanup_plan_v1.md` §4 |
| 6 | PR #42 (29-person mirror + v3 generator) still **OPEN** at baseline close — see §11 | Paper-trail | — |

No blocking items.

---

## 9. Next phase options

| Letter | Option | Estimated effort | Strategic value |
|--------|--------|-------------------|------------------|
| **A** | **Obsidian Phase D** — generate standalone event / work / relationship notes (`02_Events/`, `04_Relationships/`, `05_Works/`) | Medium (~1 focused session) | Enables cross-person navigation in vault; surfaces shared events (e.g. Battle of Actium) as graph nodes |
| **B** | **Batch 5 collection** — add 5–10 more persons to the staging set | Medium per batch | Grows the network density; risks widening vault/staging gap if mirrors don't keep up |
| **C** | **Simplified UI / visual dashboard planning** — design a non-Obsidian reader (web, static-site) for non-expert reviewers | Large (planning + build) | Unlocks broader review pool; the most significant UX improvement available |
| **D** | **Schema normalization / SQLite import planning** — define a normalised relational schema and prototype `incoming/*.jsonl` → SQLite ingestion | Large (planning + build) | Foundation for analytical queries, true cross-person graphs, and eventual master-promotion workflow |
| **E** | **Source verification hardening** — second-pass review of A-candidate / B_high sources for the existing 29 persons (especially the 8 generic-ID packages that haven't had a Batch-3-style source audit yet) | Medium per batch | Closer to master-promotion-ready data; addresses the source-discipline gap |

### Trade-off summary

- **A** and **E** mature what we have; **B** broadens; **C** and **D** lay foundation for the long game.
- The order in which **C** and **D** happen matters: a UI built on `incoming/` JSON without a normalised schema will need rework. **D** before **C** is the more durable sequence.
- **B** without **E** risks doubling staging volume without strengthening the existing data's reviewability.

---

## 10. Recommended next step

**Do not immediately collect 20 more people (avoid Option B at scale right now).**

**Recommended action: create a roadmap document comparing Options A–E and choose one deliberately.**

Concrete sub-steps for the next session:

1. **Triage Open PR #42** — decide whether to merge it as-is (capturing the v3 generator into `main`) or close it (keeping the generator code unmerged but using the live-vault outcome). Either is defensible, but the choice should be deliberate before the baseline is operationally closed.
2. **Draft `reviewed/staging/_phase_decision_roadmap_v1.md`** — short comparison of Options A–E with predicted effort, dependencies, and risk for each. Score them against the current project state.
3. **Pick one option** based on the roadmap. Document the decision.
4. **Pause new-person collection** (Option B) until a strategic option is chosen — collecting more persons without choosing a direction increases the cleanup backlog and the vault/staging gap.

If a default must be picked without a roadmap session:

- **Default: A (Phase D) + E (source verification hardening, partial).** These mature the existing 29 without expanding scope, surface cross-person graph value, and prepare the data for eventual master promotion. Both are well-understood from the current project's prior work.

---

## 11. Note on PR #42 (still open at baseline close)

PR #42 contains the v3 generator (`tools/obsidian_dryrun_generator.py`), the dry-run sandbox (`obsidian-vault-pilot/_dryrun_29_v1/`), the dry-run generation report, and the live mirror report. The live vault state being closed in this baseline IS the v3 generator's output (subsequently cleaned up by PR #43 which has merged).

The PR shows `mergeStateStatus: UNKNOWN` on the GitHub API at baseline close — likely a snapshot lag after the #43 merge. The PR itself is non-conflicting (its file set does not overlap any other recent PR's file set; verified earlier in this project's history).

**Recommendation:** merge PR #42 in the next session so the v3 generator and the dry-run sandbox land in `main` as a paper trail for how the baseline came about. Until then, the v3 generator code lives on the PR branch only. The live vault state does not depend on this merge — it's already there — but the canonical commit history will be incomplete.

This baseline closure does **not** merge PR #42 because the user's task spec scoped Step 1 strictly to PR #43.

---

## 12. What this baseline does NOT change

- Does not edit `incoming/` source data.
- Does not modify any vault file (this PR is repo-side reports only).
- Does not merge PR #42.
- Does not delete the 18 namespaced TY/JC duplicate source notes.
- Does not generate Phase D standalone notes.
- Does not promote anything to master (project has no master layer yet).
- Does not start new-person collection.
- Does not build any UI / dashboard / visual layer.
- Does not modify the v3 generator further.
