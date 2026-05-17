---
source_id: "{{SRC_XX_NNN}}"                          # e.g. SRC_TY_001 or SRC_JC_003
title: "{{Primary title in source language}}"
title_zh: "{{Chinese title (omit key if same as title)}}"
title_en: "{{English title (omit key if same as title)}}"
source_type: "{{official_history|collected_works|primary_text|ancient_biography|ancient_history|ancient_text|academic_monograph|academic_paper|museum_record|local_gazetteer|encyclopedia}}"
reliability_level: "{{A|A_candidate|B_high|B|C|D}}"
verification_status: "{{ai_verified_unreviewed|needs_verification|clue_only}}"
language: "{{zh|en|grc|la|zh-classical}}"
used_for_claim_ids:
  - "{{CLM_XX_NNN}}"
review_status: ai_collected_unreviewed             # FIXED for staging
---

# {{Primary title — bilingual if both ZH and EN are useful}}

<!--
If reliability_level == D, include the D-LEVEL CLUE ONLY banner directly below the H1:

> 🚫 **D-LEVEL — CLUE ONLY** — Reliability `D`, verification `clue_only`. Per MVP rules v2.5 source-level calibration, **this source MUST NOT be used as sole support for any confirmed or high-confidence claim**. It exists for research traceability only and may seed deeper investigation into A/A_candidate or B_high sources.

For A / A_candidate / B_high / B / C sources, OMIT the D-level banner. Keep the bottom-of-page Review Warning regardless.
-->

## Source Metadata

- **Source ID:** `{{SRC_XX_NNN}}`
- **Type:** {{source_type, expanded in plain English — e.g. "Official history (正史)" or "Ancient biography (Parallel Lives)"}}
- **Reliability:** `{{reliability_level}}` — {{one-line justification, e.g. "primary official history compiled under imperial authority" or "ancient biography drawing on earlier sources now lost"}}
- **Verification:** `{{verification_status}}`
- **Language:** {{full language name, e.g. "Classical Chinese", "Greek", "English"}}
- **Citation:** {{full citation: author, title, edition, publisher, year, ISBN, key chapters/juan/page ranges. For clue_only sources, write: "clue_only — {Source}, '{Article title}' (general reference)".}}

## Used For Claims

<!--
For A / A_candidate / B / B_high / C sources: list each claim this source supports.
For D / clue_only sources: write the boilerplate paragraph below.
-->

[[{{canonical-key}}#Confirmed Historical Claims|{{CLM_XX_NNN}}]] — {{short reason/topic}}

*OR (D / clue_only):*

*None — D-level / clue_only sources are not used as sole support for any claim. Per v1 plan §7 and MVP v2.5 source-level calibration, clue sources may seed research but cannot back confirmed/high claims.*

## Notes

<!--
A short paragraph (2-5 sentences) covering:
- Author / compiler / period of composition relative to the subject person.
- Editorial framing, biases, or known scholarly caveats.
- Specific edition details (Loeb vol., Zhonghua Shuju 中华书局 punctuated edition, etc.) — and whether exact passage/page is verified.
- If verification_status == needs_verification, name what specifically needs verifying.
-->

Exact {{page/passage/juan}} reference for the cited claims requires verification against the {{specific edition}}.

## Review Warning

> ⚠️ This source note was generated from AI-collected staging metadata. {{Exact page/passage references need verification.  OR for D-level:  As a D-level clue source, this note exists for completeness only — do not cite as evidence for any claim.}}

<!--
TEMPLATE NOTES (delete before publishing):
- Filename = `{{source_id}}.md` placed under 03_Sources/Chinese/ or 03_Sources/Western/ matching the person culture.
- `used_for_claim_ids` in frontmatter is the structured list; the "Used For Claims" body section is the human-readable cross-reference.
- Wikilinks like [[tang-yin#Confirmed Historical Claims|CLM_TY_001]] target the heading within the person note, so renaming a section there will break these — keep section names stable.
- The 🚫 D-LEVEL banner is REQUIRED for reliability_level == D. The ⚠️ Review Warning at the bottom is REQUIRED on EVERY source note regardless of level.
- Reliability calibration per MVP rules v2.5:
    A           = verified primary (epitaph, inscription, collected works, letters with volume/page/passage)
    A_candidate = primary but exact passage/page not yet verified
    B_high / B  = academic monographs, peer-reviewed papers, museum catalogues
    C / D       = encyclopedias, general web, Wikipedia, Baidu, Britannica, news, blogs
-->
