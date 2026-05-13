# Web AI Prompt: Priority 2 — Qiu Ying + Augustus v2.5

Use this with weaker web AI tools. Keep the task narrow.

Repository:
https://github.com/shensiongchoo-art/historical-persons

Task: regenerate exactly two MVP person packages under v2.5 rules:

1. 仇英 / Qiu Ying
2. Augustus / Octavian

Read first:
- project-rules/MVP_COLLECTION_RULES_V2_5.md
- prompts/01_COLLECT_CHINESE_PERSON_PROMPT_V2_5.md
- prompts/02_COLLECT_WESTERN_PERSON_PROMPT_V2_5.md
- tools/validate_package.py

Create branch:
collect/qiu-ying-and-augustus-v2-5

Create/update:
- incoming/chinese/qiu-ying/
- incoming/western/augustus-octavian/

Each folder must include 11 files:
README.md, person_profile.md, person_record.json, claims.jsonl, sources.jsonl, relationships.jsonl, events.jsonl, works.jsonl, visual_media.jsonl, legendary_notes.jsonl, open_questions.md

Rules:
- Do not pause for approval.
- Do not create references.jsonl.
- One claim = one fact.
- Every important claim needs source_ids.
- Wikipedia/Baidu/Britannica are clues only.
- Do not invent bibliographic metadata.
- Use needs_verification when unsure.
- Later groupings must be reception/later_grouping_only.
- Visual media stays staging unless fully verified.

Qiu Ying focus:
- Ming professional painter.
- Approximate birth/death.
- Names: 字实父, 号十洲.
- Professional/artisan background.
- Zhou Chen, Wen Zhengming, Tang Yin, Shen Zhou, Xiang Yuanbian only where sourced.
- 明四家 as later art-historical grouping.
- Separate verified, attributed, disputed, and copied works.
- Strengthen sources beyond Wikipedia.

Augustus focus:
- Name stages: Gaius Octavius, Octavian, Augustus.
- BCE/CE date schema.
- Julius Caesar adoption.
- Second Triumvirate.
- Actium.
- 27 BCE settlement.
- Principate and first emperor as nuanced historiographical wording.
- Res Gestae as self-presentation.
- Relationships with Caesar, Antony, Cleopatra, Lepidus, Agrippa, Livia, Tiberius, Julia only where sourced.
- Use Suetonius, Cassius Dio, Appian, Res Gestae, and modern scholarship where possible.

Validate:
python tools/validate_package.py incoming/chinese/qiu-ying
python tools/validate_package.py incoming/western/augustus-octavian

Final response:
branch, folders, files, validation results, key limitations, PR or branch link.
Do not ask whether to continue.
