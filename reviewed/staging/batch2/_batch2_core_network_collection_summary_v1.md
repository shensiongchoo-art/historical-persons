# Batch 2 Core Network Collection Summary v1

**Branch:** `collect/batch2-core-network-v1`
**Date:** 2026-05-16
**Author:** MorphMind AI
**Status:** All 7 packages collected, all validation PASSED

---

## 1. Persons Collected

| # | Person | Person ID | Folder | Claims | Sources (non-D) | Validation |
|---|--------|-----------|--------|--------|-----------------|------------|
| 1 | Li Dongyang (李东阳) | P_CHN_MING_LI_DONGYANG | incoming/chinese/li-dongyang/ | 10 | 6 (4) | PASSED |
| 2 | Wang Ao (王鏊) | P_CHN_MING_WANG_AO | incoming/chinese/wang-ao/ | 8 | 4 (4) | PASSED |
| 3 | Li Mengyang (李梦阳) | P_CHN_MING_LI_MENGYANG | incoming/chinese/li-mengyang/ | 8 | 6 (4) | PASSED |
| 4 | He Jingming (何景明) | P_CHN_MING_HE_JINGMING | incoming/chinese/he-jingming/ | 10 | 6 (4) | PASSED |
| 5 | Lepidus | P_WEST_LATE_REPUBLIC_LEPIDUS | incoming/western/lepidus/ | 9 | 4 (4) | PASSED |
| 6 | Octavia Minor | P_WEST_LATE_REPUBLIC_OCTAVIA_MINOR | incoming/western/octavia-minor/ | 9 | 4 (4) | PASSED |
| 7 | Sextus Pompey | P_WEST_LATE_REPUBLIC_SEXTUS_POMPEY | incoming/western/sextus-pompey/ | 9 | 5 (5) | PASSED |

**Total: 63 claims | 35 sources | all v2.5 schema | all validate_package.py PASSED**

---

## 2. Network Closures Achieved

### Chinese
- **Former Seven Masters (前七子) core:** Xu Zhenqing (Batch 1) + Li Mengyang + He Jingming = 3 of 7 members. Core leadership documented.
- **Ming court-literati axis:** Li Dongyang → Wu Kuan (jinshi 1464 cohort) → Wang Ao (Five Commonalities, Suzhou court network). Closes the court-Suzhou literati bridge.
- **Literary transition documented:** Cabinet Style (Li Dongyang) → Former Seven Masters reaction (Li Mengyang, He Jingming). Now traceable through the repository.

### Western
- **Second Triumvirate complete:** Lepidus + Mark Antony + Augustus. All three triumvirs now in the repository.
- **Dynastic triangle closed:** Octavia Minor bridges Augustus ↔ Antony; Antony ↔ Cleopatra. The personal-political network is now fully mapped.
- **Republican resistance node added:** Sextus Pompey as son of Pompey the Great and controller of Sicily. Closes the Pompeian resistance thread.

---

## 3. Source Quality Notes

| Issue | Packages | Severity |
|-------|----------|----------|
| Li Mengyang collected works edition unverified | li-mengyang | Medium |
| Li Mengyang academic monograph unverified | li-mengyang | Medium |
| He Jingming academic monograph on Li-He debate unverified | he-jingming | Low |
| Li Dongyang Chaling school monograph unverified | li-dongyang | Low |
| Western packages rely on modern scholarship (Syme, Gruen, CAH) as B_high | lepidus, octavia-minor, sextus-pompey | Info |
| Octavia, Lepidus, Sextus have thin primary sources | lepidus, octavia-minor, sextus-pompey | Info |

**None of these block staging.** The packages are honest about source gaps.

---

## 4. Rule Compliance

| Rule | Status |
|------|--------|
| No Wikipedia/Baidu as sole support for confirmed claims | ✅ |
| Later groupings → reception_label / later_grouping_only | ✅ |
| No inferred friendship/alliance without direct source | ✅ |
| Visual media → staging_only | ✅ |
| BCE dates using correct schema | ✅ |
| One claim = one fact | ✅ |
| All source_ids in claims exist in sources.jsonl | ✅ |

---

## 5. Known Gaps

- **Li Mengyang/He Jingming:** Academic monograph verification needed. Sources are A_candidate (明史) + needs_verification academic papers. Adequate for staging but thin compared to Tang Yin/Wen Zhengming.
- **Lepidus:** Ancient sources are thin and partially hostile. Modern scholarship (Syme, Gruen) is solid but general. A dedicated Lepidus monograph may not exist.
- **Sextus Pompey:** Powell & Welch (2002) is the key modern source. Ancient sources (Appian, Dio) are Augustan-hostile. Package correctly caveats this.
- **Octavia Minor:** Roman moralizing portrayal explicitly flagged as reception caveat. Modern feminist scholarship (e.g., Bauman, Hemelrijk) not yet cited.

---

## 6. Next Steps

1. **Immediate:** Review and merge this collection PR.
2. **Next sprint:** Source verification pass on Batch 2 — focus on Li Mengyang/He Jingming academic sources.
3. **Repository total:** 22 persons (15 pre-Batch-2 + 7 Batch 2) — sufficient for a viable Obsidian network demo.
4. **After verification:** Obsidian vault demo with selected Chinese and Western persons.
