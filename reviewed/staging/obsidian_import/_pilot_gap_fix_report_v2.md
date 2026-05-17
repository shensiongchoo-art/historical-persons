# Pilot Gap-Fix Report v2

**Date:** 2026-05-17
**Scope:** 2-person Obsidian import pilot (Tang Yin + Julius Caesar)
**Status:** Format-complete, internally consistent — awaiting human visual approval before 22-person import
**Supersedes:** `_pilot_gap_fix_report_v1.md` §10 (open D-source policy question) and §4 (Tang Yin Sources section showing SRC_TY_005/006 as plain text)
**Carries forward unchanged from v1:** §1–§3 (Caesar source backfill, Relationships sections, Works sections), §5–§8 (folder scaffold, mirroring, skipped files, link resolution), §9 (Phase D deferral recommendation)

This report is a follow-on consistency pass, not a re-import. No new historical data was collected, no incoming/ files were touched, and the 22-person import was not triggered.

---

## 1. D-source policy decision is now resolved

**Decision:** D-level / `clue_only` sources **do get standalone source notes** in this vault, contrary to the original v1 import plan §7.

Rationale:
- v1 plan §7 specified D-level sources would appear inline only, no standalone notes. The v1 gap-fix pass deviated from this for Caesar (SRC_JC_008, SRC_JC_009) on explicit instruction, leaving Tang Yin asymmetric.
- The v2 pass resolves the inconsistency by accepting the deviation as the new policy across both pilot persons.
- The new policy is acceptable because: (a) D-level entries appear in `sources.jsonl` whether or not they back any claim, so 1:1 vault coverage with `sources.jsonl` is now a clean invariant; (b) every D-level note carries a prominent `🚫 D-LEVEL — CLUE ONLY` banner that makes misuse difficult; (c) reviewers benefit from being able to follow source IDs to a destination rather than dead-ending on plain text.

This decision should be back-propagated to the import plan when v2 of the plan is written. Until then, this report is the authoritative reference.

---

## 2. SRC_TY_005 and SRC_TY_006 were backfilled as D-level clue-only source notes

| Source ID | Title | Created at |
|-----------|-------|------------|
| `SRC_TY_005` | 百度百科·唐寅 (Baidu Baike: Tang Yin) | `obsidian-vault-pilot/03_Sources/Chinese/SRC_TY_005.md` |
| `SRC_TY_006` | Wikipedia: Tang Yin | `obsidian-vault-pilot/03_Sources/Chinese/SRC_TY_006.md` |

Both files carry:
- The `🚫 D-LEVEL — CLUE ONLY` banner directly below the H1 title.
- An "Used For Claims = None" section with the MVP v2.5 / v1 plan §7 boilerplate explaining why clue sources cannot back confirmed claims.
- The standard bottom-of-page `⚠️ AI-COLLECTED / STAGING ONLY` review warning.

Tang Yin's `## Sources` section was also updated: SRC_TY_005 and SRC_TY_006 are now rendered as `[[SRC_TY_005]]` / `[[SRC_TY_006]]` wikilinks (previously plain text), and the inline note now points to the per-note D-LEVEL banner rather than saying "no standalone source notes."

---

## 3. SRC_JC_008 and SRC_JC_009 now have D-level clue-only banners

Both Caesar D-level source notes were updated in-place to insert the `🚫 D-LEVEL — CLUE ONLY` banner immediately under the H1 title. Frontmatter, citation, "Used For Claims," Notes, and Review Warning sections were unchanged.

The banner is identical in wording across all four D-level notes:

```markdown
> 🚫 **D-LEVEL — CLUE ONLY** — Reliability `D`, verification `clue_only`. Per MVP rules v2.5 source-level calibration, **this source MUST NOT be used as sole support for any confirmed or high-confidence claim**. It exists for research traceability only and may seed deeper investigation into A/A_candidate or B_high sources.
```

Placement choice — directly under H1 — matches the placement of the `⚠️ AI-COLLECTED / STAGING ONLY` banner used on every person note, so reviewers encounter the warning before reading any content.

---

## 4. Tang Yin and Julius Caesar now have 1:1 source-note coverage with sources.jsonl

| Person | `sources.jsonl` entries | Source notes present | Status |
|--------|-------------------------|----------------------|--------|
| Tang Yin | 9 (SRC_TY_001–009) | 9 (`03_Sources/Chinese/SRC_TY_001.md` … `SRC_TY_009.md`) | ✅ 1:1 |
| Julius Caesar | 9 (SRC_JC_001–009) | 9 (`03_Sources/Western/SRC_JC_001.md` … `SRC_JC_009.md`) | ✅ 1:1 |

All 18 wikilinks from the two pilot person notes resolve. Validated with a regex scan over `[[SRC_*]]` patterns: 0 unresolved source links across both pilot person notes.

---

## 5. tpl-person.md and tpl-source.md were added

Templates were created based on the current pilot format and live in `obsidian-vault-pilot/99_Templates/` (and mirrored to the vault).

**`tpl-person.md`** — full person-note skeleton with:
- All 14 frontmatter keys with allowed-value hints inline.
- `⚠️ AI-COLLECTED / STAGING ONLY` banner in place under H1.
- All sections in the canonical order: Summary → Identity → Life Timeline → Historical/Reception/Legend separation → Claims Overview → Confirmed Claims → Probable/Disputed Claims → Reception/Legendary → Relationships → Works → Sources (4 sub-buckets) → Source Package → Review Status → Open Questions.
- HTML comments at each section pointing to the relevant MVP v2.5 rule (claim discipline, reception language, visual-media discipline, allowed status labels, allowed relationship types).

**`tpl-source.md`** — full source-note skeleton with:
- All 9 frontmatter keys with allowed-value enumerations.
- Conditional D-LEVEL banner instructions ("include if reliability_level == D, omit otherwise").
- Two boilerplate variants for the "Used For Claims" section (non-D vs D / clue_only).
- Inline MVP v2.5 reliability-calibration cheat sheet.

Templates have placeholders in `{{...}}` form so they read cleanly with Obsidian's core Templates plugin or by manual copy-paste. Each template ends with a "delete before publishing" notes block.

---

## 6. Pilot is format-complete and internally consistent

| Dimension | Status |
|-----------|--------|
| Frontmatter spec | ✅ All required keys present on both person notes; YAML parses cleanly. |
| Body structure | ✅ All canonical sections present and in order on both person notes. |
| Claims grouping | ✅ Confirmed / Probable+Disputed / Reception / Legendary clearly separated per MVP v2.5. |
| Reception language | ✅ "later regarded as…" / "后世美术史中常被视为…" used; reception not asserted as fact. |
| Source-level calibration | ✅ A_candidate / B_high / D used per MVP v2.5; no D-level source supports a claim alone. |
| Source-note coverage | ✅ 1:1 with `sources.jsonl` for both pilot persons. |
| D-LEVEL banner | ✅ Present on all 4 D-level source notes (SRC_TY_005, SRC_TY_006, SRC_JC_008, SRC_JC_009). |
| AI-COLLECTED warning | ✅ Present on every person note and every source note. |
| Wikilink resolution (sources) | ✅ 0 unresolved source wikilinks in either pilot person note. |
| Forward wikilinks (other persons) | ✅ Intentionally unresolved — will only resolve when 22-batch is imported. |
| Folder scaffold | ✅ All 7 spec'd top-level folders present in repo and vault. |
| Templates | ✅ tpl-person.md and tpl-source.md present in both repo and vault. |
| Mirror integrity | ✅ `diff -q` clean between repo pilot and vault for every modified/created file across both gap-fix passes. |

No internal inconsistencies remain in the pilot.

---

## 7. Full 22-person import still requires human visual approval

The pilot is technically clearable for 22-person scaling, but **the human gate is not closed**. Required before scaling:

1. **Visual review in Obsidian.** User opens `01-Projects/Historical-Persons-Wiki/01_Persons/Chinese/tang-yin.md` and `…/Western/julius-caesar.md` in the Obsidian app, follows at least one source wikilink end-to-end, scans the Graph view, and signs off on format.
2. **Confirm template usability.** User opens `99_Templates/tpl-person.md` and `99_Templates/tpl-source.md` and confirms the placeholder syntax / inline comments are usable for their workflow. If they prefer a different placeholder style (e.g. Templater `<% %>` over `{{...}}`), the templates can be reissued before the 22-batch.
3. **Decide import mechanism for the 22-batch.** Two options:
   - **Manual via templates** — apply tpl-person.md + tpl-source.md to each of the remaining 20 persons by hand. Reliable but slow.
   - **Generator script** — write a small script that reads `incoming/<culture>/<slug>/*.jsonl` + the two templates and emits Markdown deterministically for all 22. Faster and reduces format drift; recommended once user has signed off on the pilot format.

Phase D standalone notes (`02_Events/`, `04_Relationships/`, `05_Works/`, `06_Visual_Media/`) remain deferred per v1 §9. Those folders are scaffolded but empty by design.

Until items 1–2 are signed off, do not proceed with the 22-person import.

---

## 8. incoming/ remains untouched

`git status incoming/` is empty. The `incoming/**` source data was not read for write, was not modified in any pass (v1 gap-fix, v2 consistency pass), and continues to serve as the canonical source of truth. The Obsidian vault remains the generated/readable working output, with the repo's `obsidian-vault-pilot/` as the canonical version-controlled generated output between them.

---

## Files affected in this v2 pass

**Created in repo:**
- `obsidian-vault-pilot/03_Sources/Chinese/SRC_TY_005.md`
- `obsidian-vault-pilot/03_Sources/Chinese/SRC_TY_006.md`
- `obsidian-vault-pilot/99_Templates/tpl-person.md`
- `obsidian-vault-pilot/99_Templates/tpl-source.md`
- `reviewed/staging/obsidian_import/_pilot_gap_fix_report_v2.md` (this file)

**Modified in repo:**
- `obsidian-vault-pilot/03_Sources/Western/SRC_JC_008.md` (banner added under H1)
- `obsidian-vault-pilot/03_Sources/Western/SRC_JC_009.md` (banner added under H1)
- `obsidian-vault-pilot/01_Persons/Chinese/tang-yin.md` (SRC_TY_005/006 wikilinked; inline D-source note rewritten)

**Mirrored to Obsidian vault** (`H:\OneDrive\obsidian-vault\01-Projects\Historical-Persons-Wiki\`):
- All 7 above (excluding this report — reports stay in the repo only).

**Untouched:** `incoming/**`, `julius-caesar.md` body (other than the v1 gap-fix changes), all 15 non-D source notes, the v1 report.

---

## Next recommended action

User opens Obsidian, reviews the 2 pilot person notes plus a sample of source notes (recommend one of each level: SRC_TY_001 for A_candidate, SRC_TY_003 for B_high, SRC_TY_005 for D), and confirms format. Then we plan the 22-person import as a separate task.
