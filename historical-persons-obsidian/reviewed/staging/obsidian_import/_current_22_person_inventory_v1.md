# Current 22-Person Staging Inventory v1

**Date:** 2026-05-16
**Status:** All 22 packages validated and staging-ready

## 1. Chinese Persons (12)

| # | Display Name | Person ID | Folder | Batch | Claims | Src (non-D) | Density | Ready |
|---|-------------|-----------|--------|-------|--------|-------------|---------|-------|
| 1 | Shen Zhou / 沈周 | P_CHN_MING_SHEN_ZHOU | shen-zhou | MVP | 22 | 6 (4) | 0.18 | yes |
| 2 | Wang Yangming / 王阳明 | P_CHN_MING_WANG_YANGMING | wang-yangming | MVP | 37 | 18 (15) | 0.41 | yes |
| 3 | Qiu Ying / 仇英 | P_CHN_MING_001_QIU_YING | qiu-ying | MVP | 34 | 23 (18) | 0.53 | yes |
| 4 | Wu Kuan / 吴宽 | P_CHN_MING_WU_KUAN | wu-kuan | MVP | 22 | 7 (5) | 0.23 | yes |
| 5 | Tang Yin / 唐寅 | P_CHN_MING_TANG_YIN | tang-yin | B1 | 18 | 9 (7) | 0.39 | yes |
| 6 | Wen Zhengming / 文徵明 | P_CHN_MING_WEN_ZHENGMING | wen-zhengming | B1 | 14 | 8 (6) | 0.43 | yes |
| 7 | Zhu Yunming / 祝允明 | P_CHN_MING_ZHU_YUNMING | zhu-yunming | B1 | 10 | 8 (6) | 0.60 | yes |
| 8 | Xu Zhenqing / 徐祯卿 | P_CHN_MING_XU_ZHENQING | xu-zhenqing | B1 | 10 | 10 (8) | 0.80 | yes |
| 9 | Li Dongyang / 李东阳 | P_CHN_MING_LI_DONGYANG | li-dongyang | B2 | 10 | 6 (4) | 0.40 | yes |
| 10 | Wang Ao / 王鏊 | P_CHN_MING_WANG_AO | wang-ao | B2 | 8 | 4 (2) | 0.25 | yes |
| 11 | Li Mengyang / 李梦阳 | P_CHN_MING_LI_MENGYANG | li-mengyang | B2 | 8 | 7 (5) | 0.63 | yes |
| 12 | He Jingming / 何景明 | P_CHN_MING_HE_JINGMING | he-jingming | B2 | 10 | 6 (4) | 0.40 | yes |

## 2. Western Persons (10)

| # | Display Name | Person ID | Folder | Batch | Claims | Src (non-D) | Density | Ready |
|---|-------------|-----------|--------|-------|--------|-------------|---------|-------|
| 13 | Pompey | P_WEST_LATE_REPUBLIC_GNAEUS_POMPEIUS_MAGNUS | gnaeus-pompeius-magnus | MVP | 42 | 17 (14) | 0.33 | yes |
| 14 | Augustus | P_WEST_ROMAN_001_AUGUSTUS | augustus-octavian | MVP | 35 | 18 (15) | 0.43 | yes |
| 15 | Mark Antony | P_WEST_LATE_REPUBLIC_MARCUS_ANTONIUS | mark-antony | MVP | 35 | 11 (9) | 0.26 | yes |
| 16 | Julius Caesar | P_WEST_LATE_REPUBLIC_GAIUS_JULIUS_CAESAR | julius-caesar | B1 | 18 | 9 (7) | 0.39 | yes |
| 17 | Cicero | P_WEST_LATE_REPUBLIC_MARCUS_TULLIUS_CICERO | cicero | B1 | 16 | 8 (6) | 0.38 | yes |
| 18 | Cleopatra VII | P_WEST_PTOLEMAIC_CLEOPATRA_VII | cleopatra-vii | B1 | 15 | 7 (5) | 0.33 | yes |
| 19 | Marcus Agrippa | P_WEST_EARLY_PRINCIPATE_MARCUS_VIPSANIUS_AGRIPPA | marcus-agrippa | B1 | 14 | 8 (6) | 0.43 | yes |
| 20 | Lepidus | P_WEST_LATE_REPUBLIC_LEPIDUS | lepidus | B2 | 9 | 4 (3) | 0.33 | yes |
| 21 | Octavia Minor | P_WEST_LATE_REPUBLIC_OCTAVIA_MINOR | octavia-minor | B2 | 9 | 4 (3) | 0.33 | yes |
| 22 | Sextus Pompey | P_WEST_LATE_REPUBLIC_SEXTUS_POMPEY | sextus-pompey | B2 | 9 | 5 (4) | 0.44 | yes |

## 3. Totals

| Metric | Count |
|--------|-------|
| Total persons | 22 |
| Chinese | 12 |
| Western | 10 |
| MVP batch | 7 |
| Batch 1 | 8 |
| Batch 2 | 7 |
| Total claims | 385 |
| Total sources | 217 |
| All validation | PASSED |

## 4. Pilot Candidates

| Pilot | Person | Rationale |
|-------|--------|-----------|
| 1st | Tang Yin / 唐寅 | Chinese, moderate claims (18), strong source density (0.39), legend/folk separation tested |
| 2nd | Julius Caesar | Western, moderate claims (18), moderate density (0.39), reception/literary separation tested |

## 5. Known Caveats

| Package | Caveat |
|---------|--------|
| Shen Zhou | Low source density (0.18); needs source enrichment before master |
| Wu Kuan | Low source density (0.23); short_description softened, relationships marked uncertain |
| Wang Ao | Thin sources (2 non-D); honest about limitations |
| Cleopatra VII | Lowest Western non-D count (5); Roman propaganda separation enforced |
| Mark Antony | Low source density (0.26); ancient source caveats |
| Li Dongyang | SRC_LDY_003 = B_high + needs_verification; acceptable for staging |
| All MVP | Schema normalization recommended (simple vs rich inconsistency) |

## 6. All Clear for Staging Import

All 22 packages pass validation and are staging-acceptable.
No package is blocked from Obsidian pilot import.
Source verification and enrichment are recommended but not blocking for staging use.
