# PR #16 Batch 1 Core Network Collection — Recommendation

**PR:** [#16](https://github.com/shensiongchoo-art/historical-persons/pull/16)
**Branch:** `collect/batch1-core-network-v3`
**Date:** 2026-05-14
**Reviewer:** AI initial review

---

## Overall Verdict

**CONDITIONAL APPROVAL.** 7 of 8 packages are ready for staging with source verification notes. 1 package (Zhu Yunming) needs 1-2 additional sources before staging. No packages should be rejected.

---

## Package Rankings (Strongest to Weakest)

| Rank | Package | Strength |
|------|---------|----------|
| 1 | Julius Caesar | Triangulated sources, Triumvirate label split, legendary/ reception separation model-quality |
| 2 | Cleopatra VII | Propaganda-aware, death uncertainty handled correctly, coinage as contemporary evidence |
| 3 | Marcus Agrippa | Relationship discipline exemplary, succession mechanics correct, "Augustus' friend" resisted |
| 4 | Cicero | Catilinarian legality as disputed, Atticus correspondence documented, Fulvia legend flagged |
| 5 | Tang Yin | 科场案 as disputed, 点秋香 as legendary, 九美图 flagged |
| 6 | Wen Zhengming | Clean but unremarkable — Hanlin path correct, Suzhou circle with caveats |
| 7 | Xu Zhenqing | Most disciplined relationships, early-death caveat model-quality, but thin sources |
| 8 | Zhu Yunming | Thin sources (3 non-D), otherwise clean — needs supplement |

---

## Should PR Be Split?

**No.** The batch is cohesive — 4 Chinese Ming dynasty literati forming one cultural network and 4 Western late Republic/early Principate figures forming a political-military network. Splitting would lose the cross-cultural comparison value. All 8 packages were collected under the same v2.5 rules and same AI session, ensuring consistency in review_status, confidence labeling, and schema application.

The one weak package (Zhu Yunming) can be supplemented in a follow-up commit to the same branch without blocking the other 7.

---

## Required Actions Before Merge

### Immediate (blocking)

1. **Zhu Yunming sources**: Add 1-2 additional non-D sources. Priority options:
   - Museum catalog entry for Zhu Yunming calligraphy works (e.g., 故宫博物院 or 上海博物馆 collection record)
   - Academic monograph on Ming calligraphy (e.g., a monograph covering Zhu Yunming in context of Ming caoshu tradition)
   - Ming dynasty calligraphy compendium entry

### Recommended (non-blocking, can be follow-up PR)

2. **confidence/confidence_level schema check**: Verify whether `confidence: reception` / `confidence_level: reception_label` is the intended v2.5 pattern for later-grouping claims versus using standard vocabulary values.

3. **relationship_type vocabulary**: Decide whether cross-cultural relationship types should share a unified vocabulary or remain culturally specific (e.g., `later_grouping_only` for Chinese literati groups vs `same_political_context` for Roman political alliances).

4. **Source verification sprint**: All A_candidate and B_high sources need specific page/chapter/passage references. This applies to all 8 packages equally and should be handled in a dedicated verification branch rather than blocking this PR.

---

## What This Batch Proves (for Batch 2 Readiness)

| Capability | Demonstrated? | Evidence |
|-----------|---------------|----------|
| v2.5 schema adherence | YES | All 8 packages pass validate_package.py |
| One-claim-one-fact | YES | Cross-package consistency; no multi-fact aggregation |
| Reception vs fact separation | YES | All later groupings flagged as reception_label; legends in dedicated files |
| Source bias awareness | YES | Commentarii bias noted, pro-Augustan propaganda flagged, advocacy speeches caveated |
| Relationship conservatism | YES | All packages resist over-inflating friendship; Agrippa and Xu Zhenqing model-quality |
| Cross-cultural consistency | MOSTLY | Chinese and Western packages follow same schema; relationship_type vocabulary needs alignment |
| Batch collection efficiency | YES | 8 packages in a single collection session, all validated |

**Verdict: Ready for Batch 2**, with the caveat that source verification should be prioritized as a parallel sprint.

---

## Merge Recommendation

```
STATUS:        CONDITIONAL APPROVAL

CONDITION:     Add 1-2 sources to Zhu Yunming package
               (can be done in same PR or follow-up commit to this branch)

MERGE AFTER:   Zhu Yunming source supplement committed + validate_package.py pass

DO NOT:        Merge without addressing Zhu Yunming source gap
               Merge into master (target is staging consolidation branch)
               Delete collect/batch1-core-network-v3 after merge
```

---

## Next Actions After Merge

1. Create `collect/batch2-secondary-network-v1` branch
2. Apply same v2.5 rules to Batch 2 targets (if defined in 10_BATCH2 prompt)
3. Parallel sprint: source verification for all staged packages (Loeb references, juan/page numbers, museum object IDs)
4. relationship_type vocabulary standardization across Chinese/Western packages
