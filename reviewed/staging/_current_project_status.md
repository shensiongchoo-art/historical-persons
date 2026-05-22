# Current Project Status

**Last updated:** 2026-05-21
**Maintained on:** `main` (this file is the rolling snapshot)
**Baseline:** [29-Person Obsidian Internal MVP Baseline v1](obsidian_import/_29_person_obsidian_mvp_baseline_v1.md)

---

## Current data count

| Surface | Count |
|---------|-------|
| `incoming/` person packages | **29** (15 Chinese + 14 Western, all v2.5 schema, all `tools/validate_package.py` PASSED) |
| Total claims across 29 packages | ~475 |
| Total source entries across 29 packages | ~256 (after namespacing dedup) |

---

## Current vault count

| Surface | Count |
|---------|-------|
| Live Obsidian vault person notes | **29** (matches `incoming/`) |
| Live Obsidian vault source notes | **274** (256 namespaced + 18 preserved pilot duplicates) |
| Live Obsidian vault D-level banners (🚫 CLUE ONLY) | **42** |
| Unresolved person wikilinks | **0** |
| Unresolved source wikilinks | **0** |
| Pilot files preserved (MD5 stable) | 2 (Tang Yin, Julius Caesar) |

Live vault path: `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\`

---

## Current accepted baseline

**29-Person Obsidian Internal MVP Baseline (v1)** — closed 2026-05-21 after human visual review.

- Accepted use: internal review, readable wiki reference, staging knowledge base.
- NOT accepted as: master-approved data, public-facing UI, or final visual experience.
- See full baseline doc: `reviewed/staging/obsidian_import/_29_person_obsidian_mvp_baseline_v1.md`.

---

## Next recommended action

**Pause new-person collection. Pick a strategic direction before adding more data.**

Concrete next steps:

1. Draft a roadmap document comparing the 5 phase options (Phase D, Batch 5, UI/dashboard, schema/SQLite, source-verification hardening). Live in `reviewed/staging/_phase_decision_roadmap_v1.md`.
2. Pick one option deliberately.

**Default if no roadmap session happens:** Phase D (standalone event/work/relationship notes) + partial source-verification hardening on the existing 29. Mature what we have before broadening.

---

## Active blockers

**None.**

---

## Open PRs (snapshot)

**None.** All Obsidian-import-related PRs in this wave have been merged to `main`:

| PR | Squash commit | Title |
|----|----|----|
| #42 | `0abe7e5` | mirror: 29-person Obsidian dry-run v1 + generator v3 |
| #43 | `328497b` | cleanup: pilot Julius Caesar wikilink fix |
| #44 | (this PR) | baseline: close 29-Person Obsidian Internal MVP Baseline v1 |

Repository is at a clean checkpoint. Next work begins with the roadmap decision (see "Next recommended action" above).

---

## Quick reference

| Thing | Where |
|-------|-------|
| Project rules | `project-rules/MVP_COLLECTION_RULES_V2_5.md` |
| Validator | `tools/validate_package.py` |
| Obsidian generator (v3, on `main`) | `tools/obsidian_dryrun_generator.py` |
| Repo canonical generated output | `obsidian-vault-pilot/` |
| Latest dry-run sandbox (on `main`) | `obsidian-vault-pilot/_dryrun_29_v1/` |
| Live Obsidian vault | `H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\` |
| Latest baseline | `reviewed/staging/obsidian_import/_29_person_obsidian_mvp_baseline_v1.md` |
| Live mirror report | `reviewed/staging/obsidian_import/_29_person_live_mirror_report_v1.md` |
| Cleanup plan (last) | `reviewed/staging/obsidian_import/_post_import_cleanup_plan_v1.md` |
