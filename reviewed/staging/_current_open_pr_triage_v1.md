# Open PR Triage v1

**Date:** 2026-05-21
**Branch:** `triage/open-prs-v1` (off `main`)
**Repo:** https://github.com/shensiongchoo-art/historical-persons
**PRs covered:** #35, #36, #37, #38, #39 — all currently `OPEN` / `CLEAN` / `MERGEABLE`

This report classifies each open PR, identifies dependencies, and recommends a merge order. No PRs are merged automatically by this triage — recommendations only.

---

## 1. PR-by-PR triage

### PR #35 — `cleanup: 22-person post-import — link drift fixes + cleanup plan v1`

| Field | Value |
|-------|-------|
| Type | **cleanup** |
| Head branch | `cleanup/obsidian-post-import-v1` |
| Files changed | 5 (3 dry-run Markdown wikilink fixes + 2 new reports) |
| Additions / deletions | +340 / -8 |
| Touches `incoming/`? | **No** |
| Touches Obsidian output? | **Yes** — `obsidian-vault-pilot/_dryrun_22_v1/` only (the regeneratable sandbox; not the canonical pilot, not the live vault) |
| Reports-only? | No (3 wikilink sed-replacements + 2 reports). All edits are trivial-safe and reversible. |
| Risk level | **LOW** — sed-style replacements of unresolved `[[gaius-julius-caesar]]` / `[[marcus-antonius-mark-antony]]` / `[[marcus-tullius-cicero]]` to canonical slugs; pilot files MD5-verified unchanged. |
| Recommended action | **Merge after quick review.** No prerequisites. |
| Depends on | — |
| Blocks | — |

### PR #36 — `Collect Batch 3: Crassus and Brutus packages (v2.5)`

| Field | Value |
|-------|-------|
| Type | **collection** |
| Head branch | `collect/batch3-crassus-brutus-v1` |
| Files changed | 22 (2 packages × 11 required files each, both new) |
| Additions / deletions | +243 / -0 |
| Touches `incoming/`? | **Yes** — adds two NEW packages: `incoming/western/marcus-licinius-crassus/`, `incoming/western/marcus-junius-brutus/`. No edits to existing packages. |
| Touches Obsidian output? | **No** |
| Reports-only? | No |
| Risk level | **MEDIUM** — new staging data (32 claims, ~16 sources combined). Crassus and Brutus are both in the late Republic / triumvirate network and connect to existing 22-person network. |
| Recommended action | **Merge AFTER PR #37 is reviewed/merged.** Per the user's expected order, source verification (PR #37) precedes acceptance of the collection PR. |
| Depends on | **PR #37** (source-check report must clear sources before collection is accepted) |
| Blocks | Phase D / Obsidian re-import for these 2 persons (deferred per existing project rules) |

### PR #37 — `Verification: Batch 3 Crassus + Brutus source check — all 13 sources confirmed`

| Field | Value |
|-------|-------|
| Type | **verification** |
| Head branch | `verification/batch3-crassus-brutus-source-check-v1` |
| Files changed | 1 (`reviewed/staging/batch3/_batch3_crassus_brutus_source_verification_v1.md`) |
| Additions / deletions | +203 / -0 |
| Touches `incoming/`? | **No** |
| Touches Obsidian output? | **No** |
| Reports-only? | **Yes** |
| Risk level | **LOW** — reports-only; documents 13/13 sources confirmed (Marshall 1976, Tempest 2017, Crawford RRC 1974, all ancient sources verified). |
| Recommended action | **Merge first** (clears the gate for PR #36). Reports-only and clearly safe. |
| Depends on | — |
| Blocks | **PR #36** |

### PR #38 — `Plan: Batch 4 candidate scope — 5 recommended, 2 deferred`

| Field | Value |
|-------|-------|
| Type | **planning** |
| Head branch | `planning/batch4-candidate-scope-v1` |
| Files changed | 1 (`reviewed/staging/batch4/_batch4_candidate_scope_v1.md`) |
| Additions / deletions | +203 / -0 |
| Touches `incoming/`? | **No** |
| Touches Obsidian output? | **No** |
| Reports-only? | **Yes** |
| Risk level | **LOW** — reports-only; documents the 6-candidate evaluation and the 5 recommended for collection (Wang Shizhen, Chen Chun, Li Panlong, Cato the Younger, Gaius Cassius Longinus). |
| Recommended action | **Merge before PR #39.** PR #39 is the implementation of this plan, so the plan should be in `main` first so the collection PR can reference it as a merged artifact. Reports-only and clearly safe. |
| Depends on | — |
| Blocks | **PR #39** (logically — plan should precede implementation in `main`) |

### PR #39 — `Collect Batch 4 network expansion packages`

| Field | Value |
|-------|-------|
| Type | **collection** |
| Head branch | `deliver/5-person-packages-v1` |
| Files changed | 55 (5 packages × 11 required files each, all new) |
| Additions / deletions | +703 / -0 |
| Touches `incoming/`? | **Yes** — adds 5 NEW packages: `incoming/chinese/wang-shizhen/`, `incoming/chinese/chen-chun/`, `incoming/chinese/li-panlong/`, `incoming/western/cato-the-younger/`, `incoming/western/gaius-cassius-longinus/`. No edits to existing packages. |
| Touches Obsidian output? | **No** |
| Reports-only? | No |
| Risk level | **MEDIUM** — large staging addition (5 packages, ~70 claims, ~38 sources combined). Network-expansion logic from the plan in PR #38. |
| Recommended action | **Merge AFTER PR #38 is reviewed/merged.** Recommend running `python3 tools/validate_package.py` on each of the 5 packages locally first to confirm v2.5 schema conformance. |
| Depends on | **PR #38** (plan documents the scope; implementation should follow merged plan) |
| Blocks | Phase D / Obsidian re-import for these 5 persons (deferred per existing project rules) |

---

## 2. Recommended merge order

Per the user's expected order, with rationale:

| Step | PR | Type | Why this position |
|------|----|------|--------------------|
| 1 | **#35** | cleanup | Standalone — no prerequisites. Closing out the previous wave keeps `main` tidy before new collection lands. |
| 2 | **#37** | verification | Reports-only. Establishes that sources for #36's packages are validated. |
| 3 | **#36** | collection | Now safe to merge once #37 confirms source integrity. |
| 4 | **#38** | planning | Reports-only. Documents the 5-candidate scope that #39 implements. |
| 5 | **#39** | collection | Final step. Merge after the plan it implements is in `main`, and after pre-merge `tools/validate_package.py` confirms v2.5 schema on all 5 new packages. |

**Estimated review effort:**
- #35 and #37 and #38 are low-effort (reports + trivial fixes).
- #36 and #39 are medium-effort (new data — claim grouping, source level calibration, AI-COLLECTED status all to be spot-checked per MVP rules v2.5).

---

## 3. Blockers and gates

### Hard blockers

None. All 5 PRs show `mergeStateStatus: CLEAN` and `mergeable: MERGEABLE`. No merge conflicts. No required CI checks. The project repo has no PR auto-checks configured.

### Soft gates (recommended before merge)

| PR | Gate | Why |
|----|------|-----|
| #35 | User confirms the 3 link replacements are visually correct in the vault (cicero.md and cleopatra-vii.md already mirrored on 2026-05-18) | Vault edits are already live; merging only updates the repo dry-run sandbox + adds reports. Trivial. |
| #36 | PR #37 merged | Source verification gate per user spec. |
| #36 | Run `tools/validate_package.py incoming/western/marcus-licinius-crassus` and `incoming/western/marcus-junius-brutus` | Confirms v2.5 schema (11 files, JSON parses, source_ids resolve). |
| #37 | Read the report; confirm "13/13 sources confirmed" matches `sources.jsonl` in PR #36 | Cross-check the assertion. |
| #38 | Read the report; confirm the 5 recommended persons match the 5 packages in PR #39 | Cross-check before #39 merges. |
| #39 | PR #38 merged | Plan-before-implementation gate per user spec. |
| #39 | Run `tools/validate_package.py` on all 5 new packages | Confirms v2.5 schema. |

### Non-blocking items deferred to follow-on work

- Phase D standalone event/work/relationship notes — still deferred per `_post_import_cleanup_plan_v1.md` §4.
- Generator v3 hardening (name→slug lookup, em-dash status auto-hide) — still deferred per `_post_import_cleanup_plan_v1.md` §7.
- Pilot vault `julius-caesar.md` `[[marcus-antonius]]` → `[[mark-antony]]` rewrite — still requires explicit user approval.
- Cleanup of 18 duplicate TY/JC namespaced source notes in the live vault — still requires explicit user decision.

These do NOT block the open PRs from merging.

---

## 4. Whether more collection is allowed

**Current state:** PR #39 already adds 5 new persons (Batch 4). Collection is in flight, not paused.

**Recommendation:** **Pause new collection AFTER PRs #35–#39 land.** Rationale:

1. The previous post-import status report (`_post_import_status_v1.md`, 2026-05-18) recommended pausing collection until the generator v3 hardening completes. That recommendation still stands.
2. PRs #36 and #39 collectively add 7 new persons (Crassus, Brutus, Wang Shizhen, Chen Chun, Li Panlong, Cato the Younger, Gaius Cassius Longinus), bringing the staging-ready set from 22 → 29. After they merge, the project will have 29 staging packages but the Obsidian vault still reflects only 22.
3. Re-mirroring the +7 new persons into the Obsidian vault requires a second sandbox/dry-run/mirror cycle. Doing that BEFORE further collection prevents the gap between staging data and vault state from growing.

**Soft alternative:** if collection must continue concurrently, restrict new persons to packages with **namespaced** source IDs (`SRC_XX_NNN` style) — avoid the generic-ID (`SRC001`) convention used by 8 of the original 22 packages. Generic-ID packages reintroduce the filename collision risk that namespacing solves at emit time. (See `_22_person_import_plan_v1.md` §5 and `_22_person_dryrun_generation_report_v1.md` §3b.)

Quick spot-check of the 7 new packages in PRs #36 + #39 — based on file diffs alone, they appear to use namespaced source IDs (the file listings show v2.5 schema layouts). Worth confirming during the PR #36 and PR #39 review pass.

**Hard recommendation: pause new collection** after this wave lands. Plan one Obsidian re-mirror task to bring the vault from 22 → 29, then resume.

---

## 5. What this triage does NOT do

- Does not merge any PR.
- Does not modify any package under `incoming/`.
- Does not run `tools/validate_package.py` against the new packages (recommended as a pre-merge step per the gates table above).
- Does not modify any Obsidian file (vault or repo sandbox).
- Does not collect new persons.
- Does not promote anything to master.
- Does not touch `prompts/` or `project-rules/`.
