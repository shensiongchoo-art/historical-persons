# Web AI Prompt: Priority 3 — Source Verification Reports

Use this with weaker web AI tools. Do not edit person packages. Produce source verification reports only.

Repository:
https://github.com/shensiongchoo-art/historical-persons

Task: create source verification reports for existing MVP persons.

Create branch:
verification/source-reports-v1

Create folder:
reviewed/staging/source_verification/

Create these reports:

1. reviewed/staging/source_verification/pompey_source_verification.md
2. reviewed/staging/source_verification/wang-yangming_source_verification.md
3. reviewed/staging/source_verification/qiu-ying_source_verification.md
4. reviewed/staging/source_verification/augustus_source_verification.md

Rules:
- Do not collect new people.
- Do not edit incoming person packages.
- Do not merge PRs.
- Do not invent page numbers, passages, editions, ISBNs, or object IDs.
- If not verified, write needs_verification.
- Prefer exact passage/chapter/object IDs, but only if confidently found.
- Separate verified facts from unresolved items.

Pompey focus:
- Plutarch Life of Pompey.
- Plutarch Life of Crassus.
- Appian Civil Wars.
- Cassius Dio Roman History.
- Caesar Civil War.
- Cicero Pro Lege Manilia.
- Florus quote passage.

Wang Yangming focus:
- 明史·王守仁传.
- 传习录.
- 大学问.
- 王文成公全书 / 王阳明全集.
- Dictionary of Ming Biography page references.
- Longchang, Ning Prince, Four-Sentence Teaching.

Qiu Ying focus:
- 无声诗史.
- 明画录.
- 图绘宝鉴续编.
- Ellen Johnston Laing scholarship.
- Museum object IDs for key works.

Augustus focus:
- Suetonius Divus Augustus.
- Cassius Dio Roman History Books 45-56.
- Appian Civil Wars.
- Res Gestae section references.
- Velleius Paterculus if useful.

Each report should include:
- sources checked
- verified citations
- uncertain citations
- claims affected
- recommended source_id updates
- remaining gaps

Final response:
branch, files created, verification completed, remaining gaps, PR or branch link.
Do not ask whether to continue.
