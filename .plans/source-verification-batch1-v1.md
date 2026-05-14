## Context
- 8 packages across PR #16 need source verification
- ~53 sources total (28 Western, 25 Chinese)
- Western: Loeb Classical Library references confirmed by scout
- Chinese: 明史 juan confirmed (卷286), academic monographs partially verified
- Goal: upgrade citation_detail + verification_status for all verifiable sources

## Plan

### 1. Verify Western Loeb References
Update sources.jsonl for Julius Caesar, Cicero, Cleopatra VII, Marcus Agrippa with Loeb volume/chapter/section details. Confirmed LCL numbers and chapter mappings available from scout.
→ updated sources.jsonl (4 files)

### 2. Verify Western Academic Monographs
Update Cicero (Stockton 1971, OUP, ISBN 0198720335), Cleopatra (Roller 2010, OUP, ISBN 978-0-19-536553-5), Caesar (Goldsworthy 2006, Yale UP, ISBN 978-0-300-12048-6).
→ updated sources.jsonl (3 files)

### 3. Verify Chinese Official History
Update 明史·文苑传 references — confirmed 卷286 for all four Ming figures.
→ updated sources.jsonl (4 files: Tang Yin, Wen Zhengming, Zhu Yunming, Xu Zhenqing)

### 4. Verify Chinese Academic References
Update 文徵明集 (Zhou Daozhen ed., Shanghai Guji) and 文徵明年谱 (Zhou Daozhen, Zhonghua, 2020, ISBN 9787101147339). Mark unverifiable monographs as still needs_verification with detailed notes.
→ updated sources.jsonl (4 files)

### 5. Validate All 8 Packages
Re-run validate_package.py on all 8 packages to ensure no regressions.
→ validation output

### 6. Commit and Push
Commit updated sources.jsonl files to collect/batch1-core-network-v3.
→ git commit + push

## Risks
- Loeb chapter mappings are from scout verification, not direct primary source check — verification_status stays "ai_verified_unreviewed" (not "verified")
- 苏州府志 edition remains unconfirmed — keep as A_candidate
- Some Chinese academic sources could not be fully verified — will mark with detailed notes
- Relationship between claims and updated source citations should remain consistent
