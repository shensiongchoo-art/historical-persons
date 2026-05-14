# PR #16 Batch 1 Core Network Collection — Initial Review

**Branch:** `collect/batch1-core-network-v3`
**Date:** 2026-05-14
**Status:** Reviewing — do not merge

---

## Review Criteria (from MVP_COLLECTION_RULES_V2_5.md)

Each package assessed against 13 criteria:

1. Folder structure (11 files present)
2. person_id stability (no numeric suffixes)
3. validate_package.py pass
4. Source quality (A/B vs D-level)
5. Wikipedia/Baidu overuse (D/clue_only discipline)
6. One-claim-one-fact discipline
7. confirmed/high overuse
8. Relationship discipline (no over-inflated friendship claims)
9. Reception/legendary separation
10. Visual media caution
11. Strongest parts
12. Main risks
13. Recommendation tier

---

## Per-Person Assessment

### 1. Tang Yin (唐寅) — P_CHN_MING_TANG_YIN

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS — all 11 required files present |
| person_id | PASS — `P_CHN_MING_TANG_YIN`, stable, no suffix |
| Validation | PASS |
| Sources (8 total, 6 non-D) | OK — 2x A_candidate (明史, 六如居士全集), 2x B_high, 2x D/clue_only, 1x A_candidate (苏州府志), 1x A_candidate (故宫博物院) |
| Wiki/Baidu discipline | OK — SRC_TY_005 (Baidu) and SRC_TY_006 (Wikipedia) correctly D/clue_only |
| One-claim-one-fact | GOOD — 18 claims well-separated. 1498=解元 is CLM_TY_004, 科场案=disputed is CLM_TY_006 |
| confirmed/high usage | ACCEPTABLE — 10/18 confirmed, 5 probable, 1 disputed, 1 reception, 1 legendary |
| Relationship discipline | GOOD — 6 relationships use `probable_association` and `later_grouping_only`; no over-inflated friendship |
| Reception separation | GOOD — 明四家 as `reception_label` (CLM_TY_010), 吴中四才子 as `reception_label` (CLM_TY_011), 点秋香 as `legendary` (CLM_TY_015) |
| Visual media | OK — visual_media.jsonl exists with appropriate caveats |
| Strongest parts | 科场案 treated as `disputed` with explicit caveat (CLM_TY_006); 点秋香 cleanly separated as `legendary`; 九美图 in legendary_notes.jsonl |
| Main risks | 明史·文苑传 at A_candidate needs exact juan/passage; Suzhou gazetteer citation incomplete |
| **Tier** | **ready_for_staging** with source verification note |

---

### 2. Wen Zhengming (文徵明) — P_CHN_MING_WEN_ZHENGMING

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS |
| person_id | PASS — `P_CHN_MING_WEN_ZHENGMING`, stable |
| Validation | PASS |
| Sources (9 total, 7 non-D) | OK — 明史·文苑传 A_candidate, 甫田集 A_candidate, B_high academic, museum records |
| Wiki/Baidu discipline | OK — D/clue_only correctly flagged |
| One-claim-one-fact | GOOD — 14 claims cleanly separated. Hanlin Daizhao path correct (CLM_WZM_006) |
| confirmed/high usage | ACCEPTABLE — 8/14 confirmed, 4 probable, 2 reception_label |
| Relationship discipline | GOOD — Shen Zhou teacher as `probable` (CLM_WZM_004), Suzhou circle as `probable` with explicit caution note |
| Reception separation | GOOD — 明四家 (CLM_WZM_010) and 吴中四才子 (CLM_WZM_011) both `reception_label` |
| Visual media | OK |
| Strongest parts | Short Hanlin tenure and resignation correctly captured (CLM_WZM_007); same-birth-year with Tang Yin noted as historical observation (CLM_WZM_014) |
| Main risks | CLM_WZM_012 lists 6 Suzhou associates in one claim — slightly overloaded but acceptable as network enumeration |
| **Tier** | **ready_for_staging** |

---

### 3. Zhu Yunming (祝允明) — P_CHN_MING_ZHU_YUNMING

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS |
| person_id | PASS — `P_CHN_MING_ZHU_YUNMING`, stable |
| Validation | PASS |
| Sources (5 total, 3 non-D) | WEAK — only 3 non-D sources: 明史 A_candidate, 怀星堂集 A_candidate, calligraphy paper B_high. Two D-level encyclopedias. |
| Wiki/Baidu discipline | OK — both D/clue_only |
| One-claim-one-fact | GOOD — 10 claims, clean |
| confirmed/high usage | ACCEPTABLE — 4/10 confirmed, 3 probable, 3 reception |
| Relationship discipline | GOOD — 吴中四才子 as `later_grouping_only`; folk Zhu Zhishan warned as distinct from historical figure |
| Reception separation | GOOD — Four Talents as `reception_label` (CLM_ZYM_007), comedic folk image as `reception_label` (CLM_ZYM_010) |
| Visual media | OK |
| Strongest parts | Family background correctly noted (grandfather Zhu Hao jinshi, maternal grandfather Xu Youzhen); folk vs historical distinction clear |
| Main risks | **Only 5 sources** — the thinnest of all 8 packages. At minimum needs one more academic monograph or museum collection reference. |
| **Tier** | **needs_minor_cleanup** — add 1-2 additional sources before staging |

---

### 4. Xu Zhenqing (徐祯卿) — P_CHN_MING_XU_ZHENQING

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS |
| person_id | PASS — `P_CHN_MING_XU_ZHENQING`, stable |
| Validation | PASS |
| Sources (5 total, 3 non-D) | ADEQUATE — 明史 A_candidate, 迪功集 A_candidate, B_high academic, 2x D/clue_only. Thin but Xu Zhenqing is the least-documented of the four. |
| Wiki/Baidu discipline | OK |
| One-claim-one-fact | GOOD — 10 claims. Conservative with relationships. |
| confirmed/high usage | ACCEPTABLE — 5/10 confirmed, 3 probable, 2 reception_label |
| Relationship discipline | **EXCELLENT** — CLM_XZQ_009 explicitly states Four Talents is "后世归类"; CLM_XZQ_010 explicitly warns against over-inference due to early death. Most disciplined in the batch. |
| Reception separation | GOOD — Four Talents (CLM_XZQ_006) and Former Seven Masters (CLM_XZQ_007) both as `reception_label` |
| Visual media | OK |
| Strongest parts | Relationship conservatism — explicitly limits claims based on short lifespan (died at 33); "不宜过度推断其关系网络深广度" is model language |
| Main risks | Same source thinness as Zhu Yunming; the Former Seven Masters grouping reference needs verification |
| **Tier** | **ready_for_staging** |

---

### 5. Julius Caesar — P_WEST_LATE_REPUBLIC_GAIUS_JULIUS_CAESAR

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS |
| person_id | PASS — `P_WEST_LATE_REPUBLIC_GAIUS_JULIUS_CAESAR`, era-scoped, stable |
| Validation | PASS |
| Sources (9 total, 7 non-D) | STRONG — Commentarii (A_candidate), Plutarch/Suetonius/Dio (B_high), Cicero letters (A_candidate), Goldsworthy monograph (B_high with ISBN) |
| Wiki/Baidu discipline | OK — Wikipedia and Britannica both D/clue_only |
| One-claim-one-fact | GOOD — 18 claims. "First Triumvirate" split into historical event (CLM_JC_004) and historiographical label (CLM_JC_005) |
| confirmed/high usage | ACCEPTABLE — 12/18 confirmed, 1 probable, 2 reception, 1 legendary, 1 disputed |
| Relationship discipline | GOOD — Caesar-Cicero as complex (opponent + admiration, CLM_JC_018); Caesar-Cleopatra properly scoped |
| Reception separation | **EXCELLENT** — First Triumvirate as "后世标签" (CLM_JC_005); Et tu Brute as `legendary` with Suetonius/Plutarch sourcing note (CLM_JC_016); Caesarean section myth in legendary_notes.jsonl |
| Visual media | OK |
| Strongest parts | Triumvirate handled correctly (event vs label split); Commentarii bias explicitly noted; Caesarean section myth debunked with Aurelia survival evidence; calendar reform captured |
| Main risks | Commentarii as A_candidate is defensible but self-serving nature means cross-referencing needed; Cicero letters as source for Caesar needs specific passage refs |
| **Tier** | **ready_for_staging** — strongest Western package |

---

### 6. Cicero — P_WEST_LATE_REPUBLIC_MARCUS_TULLIUS_CICERO

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS |
| person_id | PASS — stable |
| Validation | PASS |
| Sources (8 total, 6 non-D) | STRONG — Speeches/Letters/Philosophical Works all A_candidate, Plutarch/Dio B_high, academic monograph B_high |
| Wiki/Baidu discipline | OK |
| One-claim-one-fact | GOOD — 16 claims |
| confirmed/high usage | ACCEPTABLE — 11/16 confirmed, 1 disputed, 1 reception_label, 1 legendary |
| Relationship discipline | GOOD — Atticus relationship as `confirmed` (CLM_CC_012), decades-spanning correspondence noted |
| Reception separation | GOOD — "greatest orator" as `reception_label` (CLM_CC_013); Fulvia tongue-piercing as `legendary` (CLM_CC_016) |
| Visual media | OK |
| Strongest parts | Catilinarian execution legality as `disputed` (CLM_CC_006) shows source-criticism; Caesar's clementia correctly contextualized (CLM_CC_010); contemporary source value of letters explicitly stated (CLM_CC_014) |
| Main risks | Cicero's speeches are advocacy documents — A_candidate designation needs "forensic bias" note (present in SRC_CC_001 notes); "Cicero: A Political Biography" needs author verification |
| **Tier** | **ready_for_staging** |

---

### 7. Cleopatra VII — P_WEST_PTOLEMAIC_CLEOPATRA_VII

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS |
| person_id | PASS — `P_WEST_PTOLEMAIC_CLEOPATRA_VII`, dynasty-scoped, stable |
| Validation | PASS |
| Sources (7 total, 5 non-D) | OK — Plutarch Antony B_high, Dio B_high, Suetonius B_high, coinage A_candidate, academic monograph B_high |
| Wiki/Baidu discipline | OK |
| One-claim-one-fact | GOOD — 15 claims |
| confirmed/high usage | ACCEPTABLE — 9/15 confirmed, 2 probable, 1 disputed, 1 reception_label |
| Relationship discipline | GOOD — Caesar-Cleopatra as alliance/relationship; Antony-Cleopatra as alliance with three children |
| Reception separation | **EXCELLENT** — Asp death as "不应视为确定的医学事实" (CLM_CL_011); manner of death as `disputed` (CLM_CL_012); Roman propaganda caveat "不应被视为客观历史评价" (CLM_CL_013); Shakespeare/film as romanticized (CLM_CL_015) |
| Visual media | OK |
| Strongest parts | Propaganda awareness — explicitly flags pro-Augustan bias in sources; death accounts handled with appropriate uncertainty; coinage included as contemporary evidence; Egyptian-language claim correctly at `probable` |
| Main risks | CLM_CL_015 has `confidence: reception` and `confidence_level: reception_label` as literal field values — consistent with other packages but needs schema confirmation |
| **Tier** | **ready_for_staging** |

---

### 8. Marcus Agrippa — P_WEST_EARLY_PRINCIPATE_MARCUS_VIPSANIUS_AGRIPPA

| Criterion | Assessment |
|-----------|-----------|
| Folder (11 files) | PASS |
| person_id | PASS — `P_WEST_EARLY_PRINCIPATE_MARCUS_VIPSANIUS_AGRIPPA`, era-scoped, stable |
| Validation | PASS |
| Sources (7 total, 5 non-D) | OK — Suetonius/Dio/Strabo B_high, Cassius Dio B_high, academic monograph B_high |
| Wiki/Baidu discipline | OK |
| One-claim-one-fact | GOOD — 14 claims |
| confirmed/high usage | ACCEPTABLE — 10/14 confirmed, 2 probable, 1 unknown, 1 reception |
| Relationship discipline | **EXCELLENT** — Agrippa-Octavian as "政治/军事伙伴" with explicit warning against overstating friendship (CLM_MA_004); succession mechanics correctly captured (CLM_MA_010, CLM_MA_011) |
| Reception separation | GOOD — Independent achievements asserted (CLM_MA_013), "不应仅将其简化为奥古斯都的朋友"; birth year uncertainty flagged as `unknown` (CLM_MA_014) |
| Visual media | OK |
| Strongest parts | Relationship framing — resists "Augustus' best friend" trope; succession planning correctly mapped (Julia marriage → Gaius/Lucius adoption → Tiberius backup); public works (Pantheon, aqueducts) independently noted; birth year `unknown` shows restraint |
| Main risks | CLM_MA_012 (Spanish/Gaul operations) is broad — could potentially split into separate military and infrastructure claims |
| **Tier** | **ready_for_staging** |

---

## Cross-Package Issues

### 1. Confidence field values for reception claims
Some claims use literal values `confidence: reception` and `confidence_level: reception_label` where the standard vocabulary of `confirmed`/`probable`/`disputed`/`legendary` might be expected. This affects: Tang Yin (CLM_TY_010, CLM_TY_011, CLM_TY_015), Wen Zhengming (CLM_WZM_010, CLM_WZM_011), Zhu Yunming (CLM_ZYM_007, CLM_ZYM_010), Xu Zhenqing (CLM_XZQ_006, CLM_XZQ_007), Cleopatra (CLM_CL_015). This may be intentional v2.5 behavior for reception claims — needs confirmation from MVP_COLLECTION_RULES_V2_5.md.

### 2. Source density gap
Chinese packages average 5.5 total sources; Western packages average 7.75 total sources. Non-D sources: Chinese average 4.75, Western average 5.75. Zhu Yunming (3 non-D sources) is below threshold and needs supplement.

### 3. Relationship type vocabulary
Chinese packages use `later_grouping_only` and `probable_association`. Western packages use `same_political_context` and `opponent`. Cross-cultural relationship_type vocabulary may need intentional alignment.

### 4. Review status consistency
All 8 packages correctly have `review_status: ai_collected_unreviewed`. No false-positive "reviewed" flags.

---

## Summary Table

| Person | Claims | Sources (non-D) | Relationship discipline | Reception handling | Tier |
|--------|--------|-----------------|------------------------|-------------------|------|
| Tang Yin | 18 | 6 | Good | Excellent | ready_for_staging |
| Wen Zhengming | 14 | 7 | Good | Good | ready_for_staging |
| Zhu Yunming | 10 | 3 | Good | Good | needs_minor_cleanup |
| Xu Zhenqing | 10 | 3 | Excellent | Good | ready_for_staging |
| Julius Caesar | 18 | 7 | Good | Excellent | ready_for_staging |
| Cicero | 16 | 6 | Good | Good | ready_for_staging |
| Cleopatra VII | 15 | 5 | Good | Excellent | ready_for_staging |
| Marcus Agrippa | 14 | 5 | Excellent | Good | ready_for_staging |
