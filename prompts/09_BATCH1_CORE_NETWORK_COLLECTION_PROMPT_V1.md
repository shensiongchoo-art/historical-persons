# Prompt: Batch 1 Core Network Collection v1

Use this prompt with Claude Code / Codex for controlled expansion after the MVP staging workflow has stabilized.

Repository:

`https://github.com/shensiongchoo-art/historical-persons`

## Objective

Collect Batch 1: eight core-network historical persons.

This batch fills major gaps in the current MVP networks:

- Chinese Ming Jiangnan / Wu cultural network
- Late Roman Republic / early Principate network

Do NOT collect more than these eight people.
Do NOT merge PRs.
Do NOT build Obsidian/local vault.
Do NOT build SQLite.
Do NOT create visual/dashboard features.
Do NOT promote anything to master.

All generated data remains `ai_collected_unreviewed` and staging only.

## Required reading

Before starting, read:

1. `README.md`
2. `project-rules/MVP_COLLECTION_RULES_V2_5.md`
3. `prompts/01_COLLECT_CHINESE_PERSON_PROMPT_V2_5.md`
4. `prompts/02_COLLECT_WESTERN_PERSON_PROMPT_V2_5.md`
5. `tools/validate_package.py`
6. `reviewed/staging/_current_mvp_inventory.md`

## Branch

Create branch:

`collect/batch1-core-network-v1`

## Target persons

### Chinese persons

1. 唐寅 / Tang Yin
2. 文徵明 / Wen Zhengming
3. 祝允明 / Zhu Yunming
4. 徐祯卿 / Xu Zhenqing

### Western persons

1. Julius Caesar
2. Marcus Tullius Cicero / Cicero
3. Cleopatra VII
4. Marcus Vipsanius Agrippa / Marcus Agrippa

## Required folders

Create these folders:

```text
incoming/chinese/tang-yin/
incoming/chinese/wen-zhengming/
incoming/chinese/zhu-yunming/
incoming/chinese/xu-zhenqing/
incoming/western/julius-caesar/
incoming/western/cicero/
incoming/western/cleopatra-vii/
incoming/western/marcus-agrippa/
```

## Required files per person

Each person folder must contain exactly these 11 files:

1. `README.md`
2. `person_profile.md`
3. `person_record.json`
4. `claims.jsonl`
5. `sources.jsonl`
6. `relationships.jsonl`
7. `events.jsonl`
8. `works.jsonl`
9. `visual_media.jsonl`
10. `legendary_notes.jsonl`
11. `open_questions.md`

Do NOT create `references.jsonl` in any person root folder.
Raw search notes, if absolutely necessary, must go under `_raw/` and must be marked non-curated.

## Global collection rules

- One claim = one fact.
- Every important claim must have `source_ids`.
- Every `source_id` used must exist in `sources.jsonl`.
- No confirmed/high claim may rely only on Wikipedia, Baidu, Britannica, or generic web sources.
- Wikipedia/Baidu/Britannica may be used only as clues.
- Academic books are usually `B_high`, not `A`.
- `A` or `A_candidate` is reserved for primary texts, official histories, inscriptions, collected works, museum records, ancient texts, or verified primary editions.
- If exact volume, page, passage, edition, URL, DOI, ISBN, object ID, or museum catalogue number is not verified, write `needs_verification`.
- Do not invent bibliographic metadata.
- Later groupings must be `reception_label` or `later_grouping_only`.
- Do not infer friendship, teacher-student relationship, alliance, faction, or influence without direct source support.
- Visual media must remain staging unless source holder, object ID, attribution, date, and rights/license are verified.
- All JSON/JSONL files must parse.
- All records must use `review_status: ai_collected_unreviewed`.

## Person ID guidance

Use stable IDs without arbitrary numeric suffixes.

Suggested IDs:

```text
P_CHN_MING_TANG_YIN
P_CHN_MING_WEN_ZHENGMING
P_CHN_MING_ZHU_YUNMING
P_CHN_MING_XU_ZHENQING
P_WEST_LATE_REPUBLIC_GAIUS_JULIUS_CAESAR
P_WEST_LATE_REPUBLIC_MARCUS_TULLIUS_CICERO
P_WEST_PTOLEMAIC_CLEOPATRA_VII
P_WEST_EARLY_PRINCIPATE_MARCUS_VIPSANIUS_AGRIPPA
```

## Chinese batch focus

### Tang Yin / 唐寅

Focus:

- Real historical person: Ming Suzhou literati, painter, poet, calligrapher.
- Names: 唐寅, 字伯虎/子畏, 号六如居士 etc.
- 1498 应天府乡试第一 / 解元.
- 1499 科场案: separate confirmed involvement from disputed guilt/innocence.
- Later life as artist and writer.
- Relationship to Wen Zhengming, Zhu Yunming, Xu Zhenqing, Shen Zhou, Zhou Chen only where sourced.
- “江南四大才子 / 吴中四才子” as later grouping/reception.
- “唐伯虎点秋香” as literary/legendary/fictional reception, not biography.
- Visual media: portraits as later/traditional unless verified; artworks as `artwork_by_person`, not likeness.

Special caution:

- Do not write “中进士” for 1498. It was provincial exam success / 解元, not jinshi.
- Do not treat “唐伯虎点秋香” as historical fact.
- Do not infer close friendship from later grouping alone.

### Wen Zhengming / 文徵明

Focus:

- Real historical person: Ming Suzhou painter, calligrapher, poet, literatus.
- Names: 文壁, 文徵明, 字徵明/徵仲, 号衡山居士 etc.
- Long life timeline 1470–1559.
- Repeated examination failure, later Hanlin appointment.
- Relationship with Shen Zhou, Tang Yin, Zhu Yunming, Xu Zhenqing, Qiu Ying, Wu Kuan only where sourced.
- Wu School / Four Masters of Ming as later art-historical categories.
- Works: separate verified works, attributed works, disputed works, museum records.
- Visual media: his own works as `artwork_by_person`, not likeness.

Special caution:

- Do not write “明四家” as a living organization.
- Do not overstate friendship without evidence.
- Do not treat museum images as verified unless object ID and source holder are known.

### Zhu Yunming / 祝允明

Focus:

- Real historical person: Ming Suzhou calligrapher, poet, writer.
- Names: 祝允明, 字希哲, 号枝山, 枝指生.
- Birth/death, juren status, official posts if sourced.
- Calligraphy, literary works, thought/reception.
- Relationship with Tang Yin, Wen Zhengming, Xu Zhenqing as later grouping and possible cultural circle.
- “吴中四才子 / 江南四大才子” as later grouping.
- Separate historical Zhu Yunming from popular “祝枝山” comic/folk image.

Special caution:

- Do not treat “四才子” as a formal brotherhood or organization.
- Child prodigy / eccentric anecdotes default to `legendary`, `reception`, or `probable` unless well sourced.
- Avoid unescaped English double quotes in Chinese JSON strings.

### Xu Zhenqing / 徐祯卿

Focus:

- Real historical person: Ming poet, Wu Zhong Four Talents figure.
- Names, birth/death, Suzhou/Jiangnan background.
- Poetry and literary role.
- Relationship to Tang Yin, Wen Zhengming, Zhu Yunming as later grouping/cultural circle.
- Relationship to Li Mengyang / Former Seven Masters if sourced.
- Works and poems where source-backed.
- “吴中四才子 / 江南四大才子” as later grouping.

Special caution:

- Xu Zhenqing died relatively young; do not overstate long-term relationship networks.
- Do not infer friendship from group label.
- Do not overstate literary school membership without source.

## Western batch focus

### Julius Caesar

Focus:

- Real historical person: Roman general, politician, dictator.
- Name forms: Gaius Julius Caesar.
- Birth/death BCE schema.
- Gallic Wars, crossing Rubicon, civil war, dictatorship, assassination.
- Relationship with Pompey, Crassus, Cicero, Mark Antony, Cleopatra VII, Augustus/Octavian, Brutus, Cassius where sourced.
- Works: Commentarii de Bello Gallico, Commentarii de Bello Civili.
- Reception: Shakespeare, “Et tu, Brute?”, Caesar salad, Caesarean section myths separated.
- Visual media: coins/statues/busts cautious; no unverified likeness claims.

Special caution:

- Do not confuse Caesar with later imperial title “Caesar”.
- “First Triumvirate” should be treated as informal political alliance / later label.
- Ancient sources have bias; mark source caveats.

### Cicero / Marcus Tullius Cicero

Focus:

- Real historical person: Roman orator, statesman, lawyer, philosopher, writer.
- Birth/death BCE schema.
- Names and titles: Marcus Tullius Cicero, novus homo, pater patriae.
- Catilinarian conspiracy and executions: separate confirmed actions from legal dispute.
- Exile and recall.
- Role in late Republic, relation to Pompey, Caesar, Antony, Octavian, Atticus, Brutus.
- Works: speeches, letters, philosophical works.
- Reception and legends: Fulvia tongue-piercing story, “saved Rome” narrative, etc.

Special caution:

- Cicero’s own speeches and letters are primary but self-interested/advocacy sources.
- Do not treat legal justification of executions as confirmed; mark disputed.
- Separate historical Cicero from later humanist reception.

### Cleopatra VII

Focus:

- Real historical person: last active ruler of Ptolemaic Egypt.
- Names and titles: Cleopatra VII Philopator.
- Birth/death BCE schema.
- Ptolemaic dynasty, co-rule, political context.
- Relationship with Julius Caesar, Caesarion, Mark Antony, Augustus/Octavian, Ptolemy XIII/XIV/XV where sourced.
- Actium, Alexandria, death.
- Reception: Roman propaganda, Shakespeare, film/popular image, “seductress” trope.
- Visual media: coin portraits, sculptures, later paintings, but all cautious/staging.

Special caution:

- Do not sensationalize Cleopatra.
- Separate historical ruler from Roman hostile propaganda and later exoticized image.
- Death by asp/snake should be treated carefully: ancient tradition, not certain medical fact.

### Marcus Agrippa

Focus:

- Real historical person: Roman general, admiral, administrator, close associate of Augustus.
- Name: Marcus Vipsanius Agrippa.
- Birth/death BCE schema.
- Role in Actium, naval campaigns, public works, administrative reforms.
- Relationship with Augustus, Mark Antony, Cleopatra VII, Julia, Tiberius, Marcellus where sourced.
- Marriage and succession context.
- Works/buildings: Pantheon precursor, baths, aqueducts, maps if sourced.
- Reception: avoid reducing him to “Augustus’ friend”; capture independent role.

Special caution:

- Do not overstate “friendship” unless source-backed; use `documented_association`, `political_military_associate`, or similar.
- Separate his own achievements from Augustan propaganda.

## Batch summary

Create:

`reviewed/staging/_batch1_core_network_collection_summary.md`

Include:

1. Branch name
2. Persons collected
3. Folder paths
4. Validation result per person
5. Known source limitations per person
6. Relationship/network value per person
7. Which packages look strongest
8. Which packages need immediate source verification
9. Recommended next action

## Validation commands

Run:

```bash
python tools/validate_package.py incoming/chinese/tang-yin
python tools/validate_package.py incoming/chinese/wen-zhengming
python tools/validate_package.py incoming/chinese/zhu-yunming
python tools/validate_package.py incoming/chinese/xu-zhenqing
python tools/validate_package.py incoming/western/julius-caesar
python tools/validate_package.py incoming/western/cicero
python tools/validate_package.py incoming/western/cleopatra-vii
python tools/validate_package.py incoming/western/marcus-agrippa
```

Fix all validation errors before committing.

## Final response

At the end, report only:

1. Branch name
2. PR link
3. Persons collected
4. Folder paths
5. Validation result for each person
6. Files created
7. Known limitations
8. Recommended next step

Do not ask “should I continue?”.
