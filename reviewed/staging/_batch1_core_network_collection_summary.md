# Batch 1 Core Network Collection Summary

**Branch:** `collect/batch1-core-network-v1`
**Date:** 2026-05-14
**Collector:** MorphMind AI

---

## Persons Collected (8)

### Chinese — Ming Jiangnan / Wu Cultural Network

| # | Person | Person ID | Folder | Claims | Sources | Validation |
|---|--------|-----------|--------|--------|---------|------------|
| 1 | 唐寅 / Tang Yin | `P_CHN_MING_TANG_YIN` | `incoming/chinese/tang-yin/` | 18 | 8 | PASSED |
| 2 | 文徵明 / Wen Zhengming | `P_CHN_MING_WEN_ZHENGMING` | `incoming/chinese/wen-zhengming/` | 14 | 7 | PASSED |
| 3 | 祝允明 / Zhu Yunming | `P_CHN_MING_ZHU_YUNMING` | `incoming/chinese/zhu-yunming/` | 10 | 5 | PASSED |
| 4 | 徐祯卿 / Xu Zhenqing | `P_CHN_MING_XU_ZHENQING` | `incoming/chinese/xu-zhenqing/` | 10 | 5 | PASSED |

### Western — Late Roman Republic / Early Principate Network

| # | Person | Person ID | Folder | Claims | Sources | Validation |
|---|--------|-----------|--------|--------|---------|------------|
| 5 | Julius Caesar | `P_WEST_LATE_REPUBLIC_GAIUS_JULIUS_CAESAR` | `incoming/western/julius-caesar/` | 18 | 9 | PASSED |
| 6 | Cicero | `P_WEST_LATE_REPUBLIC_MARCUS_TULLIUS_CICERO` | `incoming/western/cicero/` | 16 | 8 | PASSED |
| 7 | Cleopatra VII | `P_WEST_PTOLEMAIC_CLEOPATRA_VII` | `incoming/western/cleopatra-vii/` | 15 | 7 | PASSED |
| 8 | Marcus Agrippa | `P_WEST_EARLY_PRINCIPATE_MARCUS_VIPSANIUS_AGRIPPA` | `incoming/western/marcus-agrippa/` | 14 | 7 | PASSED |

### Totals

- **Total claims:** 115
- **Total sources:** 56
- **Total relationships:** 40
- **All 8 packages pass validation**

---

## Schema Compliance

All packages follow v2.5 schema:
- Stable person IDs without numeric suffixes
- `review_status: ai_collected_unreviewed` on all records
- One claim = one fact (compound claims split)
- No `references.jsonl` in any person root folder
- BCE dates use explicit `era`/`year_number`/`astronomical_year` fields
- Later groupings marked as `reception_label` or `later_grouping_only`
- D-level sources (Wikipedia/Baidu/Britannica) correctly marked `clue_only`

---

## Known Source Limitations

### Per Chinese Person

| Person | Top Limitation |
|--------|---------------|
| Tang Yin | 明史·文苑传 passage refs need verification; teacher-student (Zhou Chen) needs primary evidence |
| Wen Zhengming | Shen Zhou teacher relationship needs primary evidence; 90 sui age calculation verification |
| Zhu Yunming | Only 5 sources; calligraphy reputation based on modern scholarship |
| Xu Zhenqing | Died young (33); limited interaction window; Four Talents grouping is later reception |

### Per Western Person

| Person | Top Limitation |
|--------|---------------|
| Julius Caesar | All ancient source chapter refs need Loeb verification; Caesar's Commentarii are self-serving |
| Cicero | Own speeches are advocacy; Catilinarian execution legality disputed; Fulvia story is legendary |
| Cleopatra VII | Ancient sources predominantly hostile Roman/pro-Augustan; asp death is tradition not fact |
| Marcus Agrippa | Birth year uncertain; independent achievements often subsumed into Augustan narrative |

---

## Relationship / Network Value

### Chinese Network

The "Four Talents of Wu" (吴中四才子) is now fully represented:
- Tang Yin ↔ Wen Zhengming ↔ Zhu Yunming ↔ Xu Zhenqing
- All relationships correctly typed as `probable_association` or `later_grouping_only`
- Tang Yin and Wen Zhengming link to existing Shen Zhou (teacher) and Qiu Ying (Four Masters grouping)
- Wen Zhengming links to existing Wu Kuan

### Western Network

The late Republican network is substantially filled:
- Caesar ↔ Pompey (opponent) ↔ Cicero (political context) ↔ Cleopatra (association) ↔ Antony (association) ↔ Agrippa (opponent)
- Augustus linked via Caesar (adoption), Cleopatra (opponent), Agrippa (association)
- Cross-links: Cicero ↔ Antony (opponent), Caesar ↔ Brutus (opponent)

---

## Strongest Packages

1. **Julius Caesar** — 9 sources, 18 claims, strong ancient source coverage
2. **Cicero** — 8 sources including primary texts (speeches, letters, philosophy)
3. **Cleopatra VII** — Well-caveated; legendary material properly separated from history

## Packages Needing Immediate Source Verification

1. **Zhu Yunming** — Only 5 sources; needs more academic references
2. **Xu Zhenqing** — Thin source base; needs primary text verification
3. **Wen Zhengming** — Shen Zhou teacher relationship needs primary evidence

## Recommended Next Action

1. Source verification sprint for Chinese packages (明史·文苑传 passage refs)
2. Loeb reference verification for Western packages (Plutarch, Suetonius, Cassius Dio chapters)
3. Cross-reference relationships against existing packages (Shen Zhou, Pompey, Augustus, Wu Kuan, Qiu Ying, Mark Antony)
