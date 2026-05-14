# Central Review: 王阳明 (Wang Yangming / Wang Shouren)

**Reviewer:** MorphMind AI
**Date:** 2026-05-14
**Package:** `incoming/chinese/wang-yangming/`
**Review Status:** `ai_collected_unreviewed`

---

## 1. Package Identity

| Field | Value |
|-------|-------|
| **Person ID** | `P_CHN_MING_WANG_YANGMING` |
| **Name (ZH)** | 王阳明 / 王守仁 |
| **Name (EN)** | Wang Yangming / Wang Shouren |
| **Birth** | 1472 (成化八年九月三十日) |
| **Death** | 1529 (嘉靖七年十一月二十九日) |
| **Culture** | Chinese / Ming Dynasty |
| **Canonical Source** | PR#4 (`collect/wang-yangming-and-pompey-v1`) |
| **Validation** | PASSED |
| **Schema** | v2.5 native |

---

## 2. Current Package Status

Package is complete (11/11 required files) and passes validation. Compound claims pre-split in PR #4. Relationship types corrected in hardening sprint (PR #8). SRC017 (Steben 1998) page range corrected in PR #12. SRC018 (Najita 1980) caveat applied — only p.54 mentions Wang Yangming; Saigo Takamori ZERO mentions. C026 confidence downgraded to low.

---

## 3. Overall Central Review Verdict

**STAGING ONLY — NOT READY FOR MASTER PROMOTION.** Package is structurally sound and well-documented for Ming dynasty career and philosophy, but requires SRC014 replacement before C025–C026 can be promoted. Primary texts (传习录, 大学问, 明史) are present as A_candidate but lack specific passage citations. Source verification sprint resolved page range errors and added source caveats but the critical Japan gap remains.

---

## 4. Master-Candidate Facts

- Born 1472, died 1529; native of Yuyao, Zhejiang
- Passed jinshi examination 1499; held major civil and military offices
- Suppressed Prince Ning (Zhu Chenhao) rebellion 1519
- Developed the philosophy of 知行合一 (unity of knowledge and action) and 致良知 (extension of innate knowledge)
- Major works: 《传习录》, 《大学问》, collected in 《王文成公全书》
- Posthumous title: 新建伯 (1509/1529), 文成 (1567)

---

## 5. Staging-Only Claims

- C025–C026 (Japanese Yangmingism influence on Meiji Restoration figures) — depends on SRC014 placeholder
- C027 (Tang Yin and Zhu Yunming relationships) — correctly `needs_verification`
- Several reception-labeled claims about philosophical school labels (陆王心学)

---

## 6. Reception / Legendary / Disputed Material

- "陆王心学" (Lu-Wang School of Mind) — correctly reception_label
- "龙场悟道" (Longchang Enlightenment) — event historical; framing label is reception
- "Four-Sentence Teaching" (四句教) — documented by disciples; exact wording may vary
- 諡号 (posthumous titles) — correctly sourced from 明史

---

## 7. Source Issues

| Issue | Severity |
|-------|----------|
| SRC014 (Ching 1976) Japan pages unverified — physical book required | High |
| SRC018 (Najita 1980) does NOT support C026 — C026 downgraded to low | High |
| A_candidate sources (传习录, 大学问, 明史) lack specific passage refs | Medium |
| 5 C-level sources remain — excessive | Medium |
| Dictionary of Ming Biography (SRC015) needs exact page refs | Low |

---

## 8. Relationship Issues

| Issue | Detail |
|-------|--------|
| Only 8 relationships | Thin for a major Ming figure with many disciples |
| R002 (Lu Jiuyuan) | Correctly reception_label (not documented_association) |

---

## 9. Visual Media Issues

- All 3 entries staging
- No verified contemporary portrait
- Portraits in circulation are later traditional portraits, not confirmed likenesses

---

## 10. Recommended Cleanup Actions

1. Replace SRC014 with verified monograph (e.g., Julia Ching, *To Acquire Wisdom: The Way of Wang Yang-ming*, Columbia UP, 1976, Part Three on Japan, with specific page refs)
2. Add specific juan/passage citations for 明史·王守仁传 (卷195)
3. Add part/section refs for 传习录 (上/中/下)
4. Promote SRC018 to C/clue_only or remove as support for C026
5. Reduce C-level sources by promoting claims to academic sources
6. Add specific page refs for Dictionary of Ming Biography (vol. 2, pp. 1408-1416)

---

## 11. Obsidian Demo Suitability

**YES — recommended as primary Chinese demo person.** Rich biographical narrative covering philosophy, military career, and reception. Claims well-structured with Chinese and English text. Pre-split compound claims with proper suffixes. Philosophical terms correctly marked as reception labels. The SRC014 gap does not affect the Ming dynasty core claims.

---

## 12. Do-Not-Promote-Yet Notes

- **Do not promote C025–C026** to master_candidates until SRC014 is replaced with verified Japan Yangmingism monograph
- **Do not promote A_candidate sources** to A until specific passage citations are verified
- **Do not promote visual media** until portrait source verification is complete
