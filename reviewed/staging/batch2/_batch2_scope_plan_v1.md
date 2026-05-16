# Batch 2 Scope Plan v1

**Branch:** `planning/batch2-scope-v1`
**Date:** 2026-05-16
**Author:** MorphMind AI
**Status:** Planning — no collection yet

---

## 1. Context

**Repository state:** 15 staging packages (7 pre-Batch-1 + 8 Batch 1), all v2.5 schema, all validate_package.py PASSED.

**Goal:** Close key network nodes in Ming Suzhou literati network and Roman Late Republic. Batch 2 adds 7 new persons to bring the total to 22, enabling a viable Obsidian demo with minimal missing links.

---

## 2. Candidates

### Chinese (4 persons)

#### 2.1 Li Dongyang (李东阳)

| Field | Detail |
|-------|--------|
| Folder | `incoming/chinese/li-dongyang/` |
| Rationale | Ming court official, literary leader, Chaling school founder. Connects Wu Kuan (same cohort, both jinshi 1472), Wang Ao (court colleague), and Ming court-literati intersection. Essential for understanding the broader Ming literary-political network beyond Suzhou. |
| Connects to | Wu Kuan (jinshi cohort 1472), Wang Ao (court network), Xu Zhenqing (Former Seven Masters context — Li Dongyang's literary dominance was what the Former Seven Masters reacted against) |
| Source risks | Baidu/Wikipedia over-reliance risk (standard). Ming official sources (明史, 明实录) are solid. Li Dongyang is well-documented. Collected works (李东阳集) exist in modern editions. |
| Verdict | **Collect now.** Well-documented, low fabrication risk. |
| Special cautions | Do not overstate relationship to Jiangnan/Wu literati. Li was a northerner who served at court. His connections to Suzhou figures are through official/court channels, not local networks. |

#### 2.2 Wang Ao (王鏊)

| Field | Detail |
|-------|--------|
| Folder | `incoming/chinese/wang-ao/` |
| Rationale | Ming Suzhou official-scholar. Linked to Wu Kuan and the Five Commonalities Society (五同会). Closes the Suzhou official-literati sub-network. |
| Connects to | Wu Kuan (Suzhou network, Five Commonalities Society), Li Dongyang (court connection) |
| Source risks | Less studied in English than Tang Yin/Wen Zhengming. Chinese academic sources adequate. Check 明史 biography. |
| Verdict | **Collect now.** Moderate documentation, connects key nodes. |
| Special cautions | Five Commonalities Society was informal, not a formal organization. Do not infer close friendship without direct source. |

#### 2.3 Li Mengyang (李梦阳)

| Field | Detail |
|-------|--------|
| Folder | `incoming/chinese/li-mengyang/` |
| Rationale | Leader of the Former Seven Masters (前七子). Directly connected to Xu Zhenqing (literary exchanges), and the 前七子 grouping is already documented across multiple Batch 1 packages. His absence is the biggest structural gap in the Ming literary network. |
| Connects to | Xu Zhenqing (literary exchanges, 前七子 grouping), He Jingming (前七子 co-leader), Li Dongyang (literary reaction against) |
| Source risks | Well-documented figure. 李梦阳集 exists in modern edition. Academic monographs available. Moderate risk of overstating personal relationships. |
| Verdict | **Collect now.** Well-documented, closes critical network node. |
| Special cautions | The Former Seven Masters was not a formal organization. Treat as literary-historical grouping. Li Mengyang's poetry includes archaist manifesto statements — distinguish poetic polemic from biographical fact. |

#### 2.4 He Jingming (何景明)

| Field | Detail |
|-------|--------|
| Folder | `incoming/chinese/he-jingming/` |
| Rationale | Co-leader of the Former Seven Masters alongside Li Mengyang. Completes the 前七子 core. His literary debate with Li Mengyang is well-documented and important for understanding Ming literary history. |
| Connects to | Li Mengyang (前七子 co-leader, literary debate), Xu Zhenqing (前七子 member) |
| Source risks | Similar to Li Mengyang. 何景明集 exists. Academic coverage adequate. |
| Verdict | **Collect now.** Completes 前七子 core. |
| Special cautions | He-Li debate is literary, not personal feud. Avoid sensationalizing. |

### Western (3 persons)

#### 2.5 Marcus Aemilius Lepidus

| Field | Detail |
|-------|--------|
| Folder | `incoming/western/lepidus/` |
| Rationale | Third member of the Second Triumvirate. Currently missing from the repository while Caesar, Antony, Augustus, and Cicero are all present. His absence creates an incomplete political model. |
| Connects to | Julius Caesar (magister equitum), Mark Antony (triumvir colleague, later opponent), Augustus/Octavian (triumvir colleague, later marginalized), Cicero (Philippics target — Cicero advocated for Lepidus but later clashed) |
| Source risks | Thin ancient sources relative to Caesar/Antony/Augustus. Plutarch and Appian cover him but less extensively. Modern scholarship treats him as a secondary figure. Risk of under-documenting. |
| Verdict | **Collect now.** Essential for triumvirate completeness. Accept thin but honest package. |
| Special cautions | Do not treat him as merely "weak" or "irrelevant" — that's a later historiographical judgment. Separate his formal role (pontifex maximus, magister equitum, triumvir) from later reputation. |

#### 2.6 Octavia Minor

| Field | Detail |
|-------|--------|
| Folder | `incoming/western/octavia-minor/` |
| Rationale | Sister of Augustus, wife of Mark Antony. Key dynastic link. Her marriage to Antony and subsequent divorce is a critical turning point in the Antony-Octavian conflict. |
| Connects to | Augustus/Octavian (sister), Mark Antony (wife, then divorced), Cleopatra VII (rival — Antony left Octavia for Cleopatra) |
| Source risks | Ancient sources are Roman elite perspective — heavily moralized portrayal. Plutarch presents her as virtuous Roman matron vs. Cleopatra as foreign seductress. Modern scholarship has critiqued this framing. |
| Verdict | **Collect now.** Essential for dynastic network. |
| Special cautions | Separate historical Octavia from moralizing Roman portrayal. Do not frame her solely as "wronged wife." Her political role as dynastic link is the key fact. |

#### 2.7 Sextus Pompey

| Field | Detail |
|-------|--------|
| Folder | `incoming/western/sextus-pompey/` |
| Rationale | Son of Pompey the Great. Controlled Sicily, threatened Rome's grain supply, fought Octavian. Represents the Pompeian/Republican resistance after Caesar's assassination. |
| Connects to | Gnaeus Pompeius Magnus (father), Augustus/Octavian (opponent, later defeated), Mark Antony (initially allied against Octavian, then abandoned), Lepidus (defeated Sextus in Sicily, later stripped of power by Octavian) |
| Source risks | Ancient sources are hostile (Augustan propaganda). Appian covers the Sicilian war. Modern scholarship treats him as a genuine threat to the triumvirs, not a pirate as Augustan sources claim. |
| Verdict | **Collect now.** Closes Republican resistance node. |
| Special cautions | Do not use "pirate" label — that is Augustan propaganda. "Commander of Republican naval forces" or "controller of Sicily" is more accurate. |

---

## 3. Expected Folder Paths

```
incoming/chinese/li-dongyang/
incoming/chinese/wang-ao/
incoming/chinese/li-mengyang/
incoming/chinese/he-jingming/
incoming/western/lepidus/
incoming/western/octavia-minor/
incoming/western/sextus-pompey/
```

Each folder requires the standard 11 files per v2.5 rules.

---

## 4. Collection Order

| Priority | Person | Reason |
|----------|--------|--------|
| 1 | Li Dongyang | Best-documented Chinese; sets court-literati context for Wang Ao |
| 2 | Li Mengyang | Closes 前七子 node; directly connects to Xu Zhenqing (already collected) |
| 3 | Lepidus | Closes Second Triumvirate; links all three existing Western political figures |
| 4 | Wang Ao | Connects Wu Kuan to court network; Five Commonalities Society context |
| 5 | Octavia Minor | Dynastic link; Antony-Augustus-Cleopatra triangle closure |
| 6 | He Jingming | Completes 前七子 core; depends on Li Mengyang being collected first |
| 7 | Sextus Pompey | Republican resistance; most complex sourcing (Augustan propaganda) |

---

## 5. Maximum Batch Size

**7 persons maximum.** Do not add extra people. All 7 are listed above.

---

## 6. Rules Reminder

From MVP_COLLECTION_RULES_V2_5.md:
- One claim = one fact
- Every important claim must have source_ids
- Wikipedia/Baidu/Britannica → clue_only, never sole support for confirmed/high claims
- Academic books → B_high (not A)
- A/A_candidate reserved for primary texts, official histories, inscriptions
- Later groupings → reception_label or later_grouping_only
- Do not infer friendship, teacher-student, alliance without direct source
- Visual media → staging unless rights verified
- All JSON/JSONL must parse

---

## 7. Validation Target

After collection, all 7 new packages must pass:
```
python tools/validate_package.py incoming/chinese/li-dongyang
python tools/validate_package.py incoming/chinese/wang-ao
python tools/validate_package.py incoming/chinese/li-mengyang
python tools/validate_package.py incoming/chinese/he-jingming
python tools/validate_package.py incoming/western/lepidus
python tools/validate_package.py incoming/western/octavia-minor
python tools/validate_package.py incoming/western/sextus-pompey
```

---

## 8. Go/No-Go Decision

**Go.** Batch 1 is finalized (PRs #24, #25, #26 all merged). All 8 Batch 1 packages are staging-ready. No blocking source gaps in existing packages. Batch 2 collection can proceed.

**Next step:** Run `prompts/09_BATCH1_CORE_NETWORK_COLLECTION_PROMPT_V1.md` adapted for Batch 2 scope with these 7 candidates.
