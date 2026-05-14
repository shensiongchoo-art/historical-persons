# Central Review: 吴宽 (Wu Kuan)

**Reviewer:** MorphMind AI
**Date:** 2026-05-14
**Package:** `incoming/chinese/wu-kuan/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_WU_KUAN` |
| **Name (ZH)** | 吴宽 |
| **Name (EN)** | Wu Kuan |
| **Birth** | 1435 (宣德十年) |
| **Death** | 1504 (弘治十七年七月十日) |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#7 (`collect/wu-kuan-and-mark-antony-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 (normalized PR #9, cleanup PR #11) |

---

## 2. Current Package Status

Package is complete (11/11 required files) and passes validation. Normalized to v2.5 schema in PR #9 hardening pass. Cleanup applied in PR #11 (person_id standardized, relationship type fixed, description softened). Compound claims split with a/b/c suffixes. Baidu correctly marked D/clue_only. However, several claims have empty source_ids — these need source assignment or status downgrade.

---

## 3. Overall Central Review Verdict

**STAGING ONLY — NOT READY FOR MASTER PROMOTION. REQUIRES SUBSTANTIAL SOURCE WORK.** Wu Kuan is the weakest package in the MVP inventory. Only 7 sources for 22 claims. Several claims with empty source_ids. Only 4 recorded relationships despite Wu Kuan's position as zhuangyuan (状元) and Minister of Rites — relational data is critically thin. No B-level academic monograph sources.

---

## 4. Master-Candidate Facts

- Born 1435 in Suzhou, Ming Dynasty; died 1504
- Zhuangyuan (状元) of 1472 (成化八年)
- Rose to Minister of Rites (礼部尚书)
- Active in Suzhou literati circles; associated with Shen Zhou and Wen Zhengming
- Author of 《匏翁家藏集》 (Collected Works of Paoweng)
- Posthumous name: 文定

---

## 5. Staging-Only Claims

- Claims with empty source_ids — essentially unsupported, should be needs_verification
- Claims about Wu Kuan's specific influence on Wen Zhengming — needs primary evidence
- Claims about Dongzhuang Album and Suzhou saying — needs source assignment

---

## 6. Reception / Legendary / Disputed Material

- Wu Kuan's place in Wu School literary/calligraphic tradition — later historiographical construction
- "Suzhou literati circle" framing — partially a modern art-historical construct

---

## 7. Source Issues

| Issue | Severity |
|-------|----------|
| Claims with empty source_ids (no source assignment) | Critical |
| Only 7 sources for 22 claims | High |
| No B-level academic monograph sources | High |
| Baidu (SRC_WK_005) is D/clue_only — must not support confirmed claims | Medium |
| 明史·吴宽传 (SRC_WK_001) at A_candidate — needs juan verification | Medium |

---

## 8. Relationship Issues

| Issue | Detail |
|-------|--------|
| Only 4 relationships | Critically thin for a Ming literatus of Wu Kuan's prominence |
| Shen Zhou association | Needs primary evidence (correspondence, colophons, poems) |
| Wen Zhengming as student claim | Needs primary evidence verification |
| Wang Ao relationship | Needs verification from primary sources |

---

## 9. Visual Media Issues

- 2 entries, both staging
- No verified object IDs or source holders

---

## 10. Recommended Cleanup Actions

1. **CRITICAL**: Assign source_ids to all empty claims or downgrade to needs_verification
2. Promote 明史·吴宽传 from A_candidate to A with verified juan 184 refs
3. Add 《匏翁家藏集》 as A_candidate source with edition details
4. Add at least one B_high academic monograph on Ming Suzhou literary culture
5. Search for primary correspondence documenting Wu Kuan's relationships

---

## 11. Obsidian Demo Suitability

**MARGINAL — not recommended as primary demo person.** Package structure is v2.5 compliant, but source base is too thin. Empty source_ids and minimal relationships would make the package look incomplete.

---

## 12. Do-Not-Promote-Yet Notes

- **Do not promote to master_candidates** until all claims have source_ids assigned
- **Do not promote relationship claims** until primary evidence is cited
- **Do not use for demo** without first resolving empty source_ids
