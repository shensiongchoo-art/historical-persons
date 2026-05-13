# PR #7 Hardening Plan v1
**Branch:** `hardening/pr7-wu-kuan-mark-antony-v1`
**Source PR:** https://github.com/shensiongchoo-art/historical-persons/pull/7
**Date:** 2026-05-12

---

## Wu Kuan (吴宽) — v2.3 → v2.5 Normalization

1. Claims: `text_zh/text_en` → `claim_text_zh/claim_text_en`, `category` → `claim_type`, add `person_id`
2. Sources: `level` → `reliability_level`, `bibliographic_hint` → `citation_detail`, add `author`
3. Relationships: `rel_id` → `relationship_id`, `person_a/person_b` → `person_id/related_person_name`, `description_zh/en` → `evidence_note`
4. Replace Baidu Baike (SRC_WK_005) claim support with 明史 or Dictionary of Ming Biography
5. Soften "close friends" (CLM_WK_012) → `documented_association`
6. Add 明史·吴宽传 juan number

## Mark Antony — Schema Normalization

1. Claims: `claim_text` → `claim_text_en`, add `claim_text_zh`, `category` → `claim_type`
2. Sources: `level` → `reliability_level`, `type` → `source_type`, add `citation_detail`
3. Relationship type remap: commander_and_subordinate, political_opponent, political_ally_then_rival, marriage, romantic_partner_and_political_ally, military_opponent, stepchild_and_political_ally → v2.5 allowed set
4. Add Loeb Classical Library references
5. Verify `person_id`: P_WEST_ROMAN_002_MARK_ANTONY vs late-Republic pattern
