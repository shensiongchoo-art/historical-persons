# Historical Persons Database Wiki

This repository is the staging workspace for the 历史人物数据库 Wiki MVP.

## Workflow

1. Third-party AI agents read collection prompts from `prompts/`.
2. AI-generated person packages must be submitted under `incoming/`.
3. No generated package is trusted until central review.
4. Reviewed records may later move into `reviewed/staging/`, `reviewed/master_candidates/`, or `reviewed/rejected/`.

## Core Rules

- Unified model across Chinese and Western historical persons.
- Chinese figures may be collected Chinese-first; Western figures may be collected English-first.
- Every important claim must have source IDs.
- Separate confirmed fact, probable claim, disputed claim, legendary material, and fictional/literary depiction.
- Visual media is optional metadata only.
- AI output goes to `incoming/` only, never directly to master.

## Repository Layout

```text
project-rules/          Collection and data-quality rules
prompts/                Current prompts for third-party AI agents
tools/                  Validation scripts
incoming/               AI-collected, unreviewed person packages
reviewed/staging/       Reviewed but not master-approved records
reviewed/master_candidates/ Candidate facts/records for future master import
reviewed/rejected/      Rejected or superseded generated packages
```
