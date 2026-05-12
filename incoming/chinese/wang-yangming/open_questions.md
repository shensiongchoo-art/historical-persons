# Open Questions — 王阳明 / Wang Yangming

## High Priority

1. **Exact birth date**: 成化八年九月三十日 converts to both 26 October 1472 (English Wikipedia) and 31 October 1472 (Chinese sources). Needs verification against 明实录·宪宗实录 or 王阳明年谱.

2. **明史·王守仁传 exact juan/volume number**: Source SRC001 cited as Ming History without specific volume reference. Needs location.

3. **传习录 edition and recension**: Primary text used as source but exact edition, chapter/volume references are not specified. Which recension (薛侃刻本? 南大吉刻本? 钱德洪编本?) is cited?

## Medium Priority

4. **湛若水 relationship**: Listed as `probable_association`. The Dictionary of Ming Biography mentions intellectual exchange between Wang and Zhan Ruoshui. Needs verification from 明儒学案 or collected works of both philosophers.

5. **Japanese Yangmingism detailed verification**: Both SRC014 and SRC015 are marked `needs_verification`. Need academic monograph or peer-reviewed article on the transmission of Yangmingism to Japan, specifically confirming Nakae Tōju as founder and the influence on Saigō Takamori.

6. **Korean Yangmingism (Yangmyeonghak)**: Not included in current package. The Stanford Encyclopedia of Philosophy and Internet Encyclopedia of Philosophy entries both omit Korean reception. Known in scholarship that Jeong Je-du (郑齐斗, 1649–1736) of Ganghwa School was a key figure but needs dedicated source verification.

7. **Calligraphy holdings**: Wang is known as a calligrapher. Specific museum inventory numbers, work titles, collection locations, and dates are not verified.

8. **Poetry collection**: Wang wrote poetry. A specific collection title/reference is not yet identified.

## Low Priority

9. **Tang Yin and Zhu Yunming association**: Both contemporary Ming cultural figures from the same region. No direct evidence of association found. Zhu Yunming's claims mention his admiration for Wang Yangming's philosophy but the nature of any personal relationship is unverified.

10. **“格竹七日” story's earliest source**: Frequently cited as Wang Yangming's turning point away from Zhu Xi. Needs confirmation of the earliest textual source — possibly in 传习录 or 年谱.

11. **Portrait authenticity**: Surviving portraits (Wikimedia Commons: Wang_Shoujen.jpg) lack provenance verification. Museum catalogue numbers and attribution needed.

12. **东乡平八郎 (Tōgō Heihachirō) seal**: The admiral's personal seal reading "一生低首拜阳明" is widely cited in Chinese popular culture as evidence of Japanese Yangmingism's influence. Its historical authenticity needs verification against Japanese sources.

## Hardening Sprint Notes (v1, 2026-05-12)

- R002 (陆九渊) relationship_type changed from `philosophical_predecessor` to `reception_label`; status changed to `reception/medium` — "陆王心学" is a later historiographical label, not a direct relationship.
- SRC014 (日本阳明学) downgraded from `B_high` to `B` and marked placeholder; specific academic monograph (e.g. Julia Ching) with page references needed before promoting.
- Compound claims (name titles, Ning rebellion, Tianquan Bridge, Four-Sentence Teaching) were split in PR#4 and are retained.
- Tang Yin and Zhu Yunming relationships: no relationship rows created (correctly absent). See open question #9.

## Recommended Review Actions

1. Cross-reference birth date against 明实录 and 王阳明年谱
2. Cite 明史 王守仁传 with exact juan number
3. Verify 传习录 edition and provide chapter references for key doctrines
4. Confirm Japanese Yangmingism transmission with Japanese academic sources
5. Attempt museum catalogue verification for calligraphy holdings and portraits
