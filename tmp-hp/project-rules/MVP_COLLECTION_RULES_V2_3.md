# MVP Collection Rules v2.3

## Non-negotiable rules

1. `person_id` must not be empty.
2. Use one folder per person:
   - `incoming/chinese/[person-slug]/`
   - `incoming/western/[person-slug]/`
3. Required files:
   - `README.md`
   - `person_profile.md`
   - `person_record.json`
   - `claims.jsonl`
   - `sources.jsonl`
   - `relationships.jsonl`
   - `events.jsonl`
   - `works.jsonl`
   - `visual_media.jsonl`
   - `legendary_notes.jsonl`
   - `open_questions.md`
4. All JSON and JSONL files must parse successfully before submission.
5. Do not place `references.jsonl`, raw search output, or scout output in the person root folder.
6. Raw notes, if absolutely needed, go under `_raw/`.
7. Wikipedia / Baidu / Britannica may be used as clues, not as the sole source for confirmed/high claims.
8. Academic books are usually `B_high`, not automatically `A`.
9. `A` / `A_candidate` is reserved for primary texts, inscriptions, tomb epitaphs, official records, original writings, or verified museum records.
10. Later group labels such as “吴中四才子”, “江南四大才子”, “明四家”, “吴门画派代表” must be marked as `reception_label` or `later_grouping_only`.
11. Do not infer friendship, teacher-student relationship, factional membership, or direct influence from later grouping alone.
12. Visual media must distinguish:
    - `portrait_likeness`
    - `artwork_by_person`
    - `map`
    - `coin_or_inscription`
    - `later_imagined_scene`
13. Artwork created by the person is not a likeness of the person. Use `representation_status: not_a_likeness`.
14. For BCE dates, do not store only negative integers. Use explicit BCE/CE fields.
15. Claims about child prodigy stories, personality, thought influence, “greatest”, “first”, “leader”, “saved the country”, etc. default to staging unless directly supported.

## Claim statuses

Allowed:

- `confirmed`
- `probable`
- `disputed`
- `legendary`
- `fictional`
- `reception`
- `unknown`
- `needs_verification`

## Review status

Every AI-collected file should be treated as:

`review_status: ai_collected_unreviewed`
