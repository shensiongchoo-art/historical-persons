## Context
- Repo: historical-persons on master branch with 7 persons already in `incoming/`
- Goal: Consolidate current MVP inventory, write central review notes for all 7 persons, expand with exactly 6 new persons using v2.5 rules
- All existing packages are `ai_collected_unreviewed` — none promoted to master
- Work happens on `step1.2/staging-consolidation-small-expansion-v1` branch

## Plan

### 1. Create Branch
Switch off master, create `step1.2/staging-consolidation-small-expansion-v1`.
→ Branch created on remote

### 2. Part A — Inventory File
Write `reviewed/staging/_current_mvp_inventory.md` listing all 7 persons with folder path, person_id, status, source sufficiency, weaknesses, Obsidian suitability, verification needs, visual media staging status, and recommended next action.
→ reviewed/staging/_current_mvp_inventory.md

*Considered: embedding this in a single flat section of the expansion summary (would lose per-person traceability and not meet the user's explicit Part A spec)*

### 3. Part B — Central Review Notes
Write 7 individual `central_review.md` files under `reviewed/staging/{person-slug}/`. Each includes all 13 required sections. Derive content from existing incoming files, hardening report v1, source verification reports, and repo state review v1.
→ 7 × reviewed/staging/{slug}/central_review.md

*Considered: using a script to template them (inconsistent quality — manual composition from existing review data is safer)*

### 4. Part C — Collect 6 New Person Packages
Research then generate 11 files per person using v2.5 rules. Research via scout (Wikipedia, academic sources, primary texts) then assemble structured files. Each package needs research before writing.

Chinese persons:
- `incoming/chinese/li-dongyang/` — Ming literary figure, Chaling school
- `incoming/chinese/wang-ao/` — Ming Suzhou official-scholar, Five Commonalities Society
- `incoming/chinese/xu-zhenqing/` — Wu Zhong Four Talents poet

Western persons:
- `incoming/western/cleopatra-vii/` — Ptolemaic ruler, separate from myth
- `incoming/western/marcus-agrippa/` — Roman general, Augustus's associate
- `incoming/western/lepidus/` — Roman triumvir

→ 6 × 11 files = 66 new files

*Considered: generating all packages from memory (violates research requirement — must scout first)*
*Considered: using a single batch scout (would mix Chinese/Western research requirements — need separate scouts per cultural context)*

### 5. Part D — Validation
Run `python tools/validate_package.py` on each of the 6 new folders. Fix errors. Re-validate until all pass.
→ Validation PASSED for all 6

### 6. Part E — Expansion Summary
Write `reviewed/staging/_step1.2_expansion_summary_v1.md` covering all 10 required sections.
→ reviewed/staging/_step1.2_expansion_summary_v1.md

### 7. Commit, Push, Open PR
Commit all changes, push branch, open PR to main.
→ PR link in final output

## Risks
- Scout research may be limited for Chinese figures (Baidu/Wikipedia are clues only; academic sources may need creative search) → use Europe PMC for any Ming studies, search academic literature
- 66 new files + 8 review files + 2 summary files = ~76 files to create — may hit rate limits → batch file writes efficiently
- Wrong historical facts: packages are `ai_collected_unreviewed` by design — central review catches errors later
- Existing packages on master branch are the source of truth (not hardened branches)
