# 仇英 (Qiu Ying) — 待解决问题

## 生卒年
1. 仇英的确切生卒年尚无定论。学界范围涵盖1482–1505年（生年）至1552年（卒年），跨度逾二十年。需要从明代藏家记录、墓碑、方志中寻找更多证据以精确化。
2. 若能确证周凤来寓居期间（约1537–1543年）的起止年份，可为仇英生平提供更可靠的时间锚点。

## 师承关系
3. 仇英拜周臣为师的年份与具体经过不详。周臣的生卒年（约1450–1535年）本身也不精确。
4. 仇英与文徵明合作始于何时？除《湘君湘夫人图》题跋中的记录外，是否有其他合作或交流的直接证据（书信、题画诗、诗文提及）？

## 作品归属
5. 天津博物馆所藏《桃源仙境图》是否为仇英真迹？需要查证该馆正式著录与学术鉴定文献。
6. 辽宁省博物馆所藏《赤壁图》的归属需要核实。
7. 克利夫兰艺术博物馆是否确实藏有《赵孟頫写经换茶图》？该馆在线目录检索中未确认此作品。
8. 仇英真迹与苏州作坊伪作的系统性区分尚需大量个案研究。Laing 指出许多传世仇英作品的实际归属存疑。

## 社会关系
9. 仇英与唐寅的具体交往情况不详。二人虽同出周臣门下，但唐寅卒于1524年，当时仇英可能还在早期阶段。
10. 仇英在同时代文人笔记中的出现频率和评价如何？王世贞、董其昌之外的明代文献有待系统检索。

## 图像资料
11. 是否有可靠的同时代仇英肖像传世？目前尚未确认任何仇英本人的肖像作品。
12. 仇英传世画作的高清数字化图像与博物馆正式授权信息需要逐一核实。

## Hardening Sprint Notes (v1, 2026-05-12)

- claims.jsonl: normalized from v2.3 schema (text_zh/text_en, category) to v2.5 schema (claim_text_zh/claim_text_en, claim_type, person_id added).
- sources.jsonl: normalized from v2.3 schema (level, bibliographic_hint) to v2.5 schema (reliability_level, title, author preserved from bibliographic_hint as combined title field).
- relationships.jsonl: normalized from v2.3 schema (rel_id, person_a/person_b, description_en) to v2.5 schema (relationship_id, person_id, related_person_name, evidence_note).
- REL_QY_004 (influence on Shen Zhou) retained at low confidence; REL_QY_010–012 correctly typed as later_grouping_only.
- Source discipline: museum records (SRC_QY_013–015) retained at level A; bibliographic sources (Laing papers) at B_high. No Wikipedia sources used for confirmed claims.
- 明清画史笔记 sources (无声诗史, 明画录, 图绘宝鉴续编) not present as separate sources — added to open questions. See item 13 below.
13. **明清画史笔记 sourcing**: Sources 无声诗史 (姜绍书), 明画录 (徐沁), 图绘宝鉴续编 (韩昂) cited in collection prompt but not separately represented in sources.jsonl. Need specific edition references and claim cross-referencing before promoting relevant claims from A_candidate to A.

## Source Verification Sprint Notes (v2, 2026-05-12)

### 明清画史笔记 source entries added (SRC_QY_021–SRC_QY_023)
- **SRC_QY_021 — 无声诗史 (姜绍书)**: Early Qing (Kangxi period, after 1679). 7 juan. Standard edition: 于安澜编《画史丛书》, 上海人民美术出版社, 1963. Level: **A** (early Qing compilation, ~120 years post-Qiu Ying). Covers Ming painter biographies. Used for: CLM_QY_001 (name), CLM_QY_002 (origin), CLM_QY_003 (lacquer worker), CLM_QY_010 (Zhou Chen teacher), CLM_QY_023 (copying skill).
- **SRC_QY_022 — 明画录 (徐沁)**: Early Qing. 8 juan. Standard edition: 于安澜编《画史丛书》, 1963. Level: **A**. Organized by painting category; professional painters section covers Qiu Ying. Used for: CLM_QY_001, CLM_QY_002, CLM_QY_003, CLM_QY_010, CLM_QY_020 (gongbi/blue-green), CLM_QY_022 (jiehua), CLM_QY_023.
- **SRC_QY_023 — 图绘宝鉴续编 (韩昂)**: 正德十四年 (1519). 1 juan. Standard edition: 四库全书本 + 于安澜《画史丛书》. Level: **A** (near-contemporary — compiled during Qiu Ying's youth). Covers Ming painters up to Zhengde period. Used primarily for: CLM_QY_010 (Zhou Chen documentation) and Suzhou professional painting context. Qiu Ying's own inclusion uncertain given his peak in Jiajing period (1522–1566).

### Author fields fixed
- All 20 pre-existing SRC_QY_ records: author field replaced from "see bibliographic_hint" to named author.
- Title fields cleaned of inline bibliographic junk.

### Claim cross-referencing
- 7 claims updated with supplementary source_ids linking to the painting histories:
  CLM_QY_001, CLM_QY_002, CLM_QY_003, CLM_QY_010, CLM_QY_020, CLM_QY_022, CLM_QY_023.
- These claims now cite both modern Western scholarship (Laing, Ngan) AND near-contemporary Chinese painting histories.

### Still needs_verification
- All three new source entries need **passage-level verification**: exact juan/page/entry references for Qiu Ying in each text.
- 图绘宝鉴续编: whether Qiu Ying has an entry at all needs confirmation (compiled 1519, his career peaked later).
- After passage verification, claims currently at `probable/medium` that cite these sources (CLM_QY_013, CLM_QY_019, CLM_QY_026) could be cross-referenced and potentially strengthened.
