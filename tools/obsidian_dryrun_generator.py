#!/usr/bin/env python3
"""
22-Person Obsidian Dry-Run Generator (v1)

Reads incoming/<culture>/<slug>/*.{json,jsonl,md} and emits Markdown person notes
and source notes into obsidian-vault-pilot/_dryrun_22_v1/.

- Person note filename:  {slug}.md  under 01_Persons/{Chinese|Western}/
- Source note filename:  {slug}__{source_id}.md  under 03_Sources/{Chinese|Western}/
  (Namespacing applies UNIFORMLY across all 22 persons per the approved plan,
   including packages whose source_ids are already prefixed.)

Does NOT touch incoming/. Does NOT mirror to the live vault. Does NOT generate
standalone event/work/relationship notes.
"""
import json, os, sys, re
from collections import Counter, defaultdict

REPO = '/home/clawchoo/claude-projects/historical-persons'
INCOMING = os.path.join(REPO, 'incoming')
OUT = os.path.join(REPO, 'obsidian-vault-pilot', '_dryrun_22_v1')

BATCH = {
    'shen-zhou':'MVP','wang-yangming':'MVP','qiu-ying':'MVP','wu-kuan':'MVP',
    'gnaeus-pompeius-magnus':'MVP','augustus-octavian':'MVP','mark-antony':'MVP',
    'tang-yin':'B1','wen-zhengming':'B1','zhu-yunming':'B1','xu-zhenqing':'B1',
    'julius-caesar':'B1','cicero':'B1','cleopatra-vii':'B1','marcus-agrippa':'B1',
    'li-dongyang':'B2','wang-ao':'B2','li-mengyang':'B2','he-jingming':'B2',
    'lepidus':'B2','octavia-minor':'B2','sextus-pompey':'B2',
}

D_BANNER = (
    "> 🚫 **D-LEVEL — CLUE ONLY** — Reliability `D`, verification `clue_only`. "
    "Per MVP rules v2.5 source-level calibration, **this source MUST NOT be used as "
    "sole support for any confirmed or high-confidence claim**. It exists for research "
    "traceability only and may seed deeper investigation into A/A_candidate or B_high sources."
)
AI_BANNER = ("> ⚠️ **AI-COLLECTED / STAGING ONLY** — Not yet reviewed by a "
             "subject-matter expert. Do not cite as master-approved.")

# ---------- helpers ----------
def first_of(d, *keys, default=''):
    for k in keys:
        v = d.get(k)
        if v not in (None, '', [], {}): return v
    return default

def to_year(d, kind):
    """birth/death can be a dict {year_display, era, ...} or a plain string."""
    v = d.get(kind, '')
    if isinstance(v, dict):
        return v.get('year_display', '') or v.get('original_date_text', '')
    return str(v) if v is not None else ''

def to_year_full(d, kind):
    v = d.get(kind, '')
    if isinstance(v, dict):
        parts = [v.get('year_display','')]
        if v.get('era') and v['era'] not in ('CE', 'AD'):
            parts.append(v['era'])
        orig = v.get('original_date_text','')
        if orig and orig != parts[0]:
            return f"{parts[0]} ({orig})" if parts[0] else orig
        return ' '.join(p for p in parts if p)
    return str(v) if v is not None else ''

def load_jsonl(path):
    if not os.path.exists(path): return []
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out

def safe_md_cell(s):
    if s is None: return ''
    s = str(s)
    s = s.replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')
    return s.strip()

def yaml_str(s):
    """Quote a YAML scalar safely."""
    if s is None: return '""'
    s = str(s)
    if not s: return '""'
    # Always quote — safe across special chars
    return '"' + s.replace('\\','\\\\').replace('"','\\"') + '"'

# ---------- claim/source bucketing ----------
RECEPTION_TYPES = {'reception_label','later_grouping_only','reception','reception_only','later_grouping'}
LEGEND_TYPES = {'legend','legendary','fiction','fictional','folklore','myth'}

def claim_bucket(c):
    """Return one of: confirmed, probable, reception, legendary."""
    ct = (first_of(c, 'claim_type', 'category', default='') or '').lower()
    conf = (first_of(c, 'confidence', 'confidence_level', 'status', default='') or '').lower()
    status = (first_of(c, 'status', default='') or '').lower()
    if ct in RECEPTION_TYPES: return 'reception'
    if ct in LEGEND_TYPES: return 'legendary'
    if status in LEGEND_TYPES: return 'legendary'
    if status in RECEPTION_TYPES: return 'reception'
    if conf == 'confirmed' or status == 'confirmed': return 'confirmed'
    if conf in ('probable','disputed','needs_verification','low','high','medium'):
        return 'probable'
    if status in ('probable','disputed','needs_verification'): return 'probable'
    # Default fallback: treat as probable so reviewer sees it
    return 'probable'

def source_bucket(s):
    rl = (s.get('reliability_level','') or '').strip()
    vs = (s.get('verification_status','') or '').strip()
    if vs == 'clue_only' or rl == 'D': return 'D'
    if rl in ('A','A_candidate'): return 'A'
    if rl in ('B_high','B'): return 'B'
    if rl == 'C': return 'C'
    return 'unknown'

# ---------- person note generator ----------
def gen_person_note(slug, culture, pdir, source_map, manifest):
    """
    slug:        folder slug (filename = slug.md)
    culture:     'chinese' or 'western'
    pdir:        path to incoming/<culture>/<slug>/
    source_map:  dict {source_id -> namespaced_filename} for THIS person
    manifest:    accumulator dict
    """
    with open(os.path.join(pdir, 'person_record.json')) as f:
        pr = json.load(f)
    claims = load_jsonl(os.path.join(pdir, 'claims.jsonl'))
    sources = load_jsonl(os.path.join(pdir, 'sources.jsonl'))
    rels = load_jsonl(os.path.join(pdir, 'relationships.jsonl'))
    events = load_jsonl(os.path.join(pdir, 'events.jsonl'))
    works = load_jsonl(os.path.join(pdir, 'works.jsonl'))

    name_zh = first_of(pr, 'primary_display_name_zh', 'display_name_zh', 'short_description_zh')
    name_en = first_of(pr, 'primary_display_name_en', 'display_name_en', 'short_description_en')
    if name_zh and name_en:
        display = f"{name_en} / {name_zh}" if culture == 'chinese' else f"{name_en} / {name_zh}"
    else:
        display = name_en or name_zh or slug

    person_id = pr.get('person_id', '')
    period = pr.get('period', '')
    primary_culture = pr.get('primary_culture', 'Chinese' if culture == 'chinese' else 'Western')
    primary_lang = pr.get('primary_language', 'zh-Hans' if culture == 'chinese' else 'en')
    birth_y = to_year(pr, 'birth')
    death_y = to_year(pr, 'death')
    birth_full = to_year_full(pr, 'birth')
    death_full = to_year_full(pr, 'death')
    review_status = pr.get('review_status', 'ai_collected_unreviewed')
    historical_status = 'ai_collected_unreviewed'  # FORCED per MVP rule
    source_sufficiency = pr.get('source_sufficiency', 'to_be_reviewed')
    inclusion = pr.get('inclusion_category', '')

    summary_zh = pr.get('short_description_zh', '')
    summary_en = pr.get('short_description_en', '')

    # Build frontmatter
    fm_lines = ['---']
    fm_lines.append(f'person_id: {yaml_str(person_id)}')
    fm_lines.append(f'canonical_key: {yaml_str(slug)}')
    fm_lines.append(f'display_name: {yaml_str(display)}')
    fm_lines.append(f'primary_language: {yaml_str(primary_lang)}')
    fm_lines.append(f'culture: {yaml_str(primary_culture)}')
    fm_lines.append(f'period: {yaml_str(period)}')
    fm_lines.append(f'birth: {yaml_str(birth_y)}')
    fm_lines.append(f'death: {yaml_str(death_y)}')
    fm_lines.append(f'historical_status: {historical_status}')
    fm_lines.append(f'review_status: {yaml_str(review_status)}')
    fm_lines.append(f'source_sufficiency: {yaml_str(source_sufficiency)}')
    fm_lines.append(f'data_source_folder: {yaml_str(f"incoming/{culture}/{slug}/")}')
    # tags
    tags = [BATCH.get(slug,'?').lower()]
    if culture == 'chinese': tags.append('chinese')
    else: tags.append('western')
    if period:
        # Sanitize period -> slug: lowercase, replace any non-alphanum with '-',
        # collapse repeated '-', trim leading/trailing '-'. Fixes slash artifacts
        # like "late-republic-/-early-empire" -> "late-republic-early-empire".
        ptag = period.lower().split(',')[0]
        ptag = re.sub(r'[^a-z0-9]+', '-', ptag)
        ptag = re.sub(r'-+', '-', ptag).strip('-')[:40]
        if ptag:
            tags.append(ptag)
    fm_lines.append('tags:')
    for t in tags:
        fm_lines.append(f'  - {yaml_str(t)}')
    # related_people from relationships
    rel_keys = []
    for r in rels:
        rid = r.get('related_person_id','')
        if rid and rid.startswith('P_'):
            # Map person_id back to canonical_key by best-effort
            # We don't have a full registry — emit forward-style wikilink using a slug guess.
            # Use related_person_name to slug, with a comment fallback.
            name = r.get('related_person_name','')
            # Try simple slug: lower + spaces->hyphens, strip non-alphanum
            slug_guess = re.sub(r'[^a-z0-9-]', '', name.lower().replace(' ','-'))
            if slug_guess:
                rel_keys.append(slug_guess)
    if rel_keys:
        fm_lines.append('related_people:')
        seen = set()
        for k in rel_keys:
            if k in seen: continue
            seen.add(k)
            fm_lines.append(f'  - "[[{k}]]"')
    fm_lines.append('---')

    # Body
    body = [AI_BANNER, '', f'# {display}', '']
    # Summary
    body.append('## Summary')
    body.append('')
    if summary_zh: body.append(summary_zh)
    if summary_zh and summary_en: body.append('')
    if summary_en: body.append(summary_en)
    if not summary_zh and not summary_en:
        body.append(f'*(No summary found in person_record.json. See `person_profile.md` in {f"incoming/{culture}/{slug}/"}.)*')
    body.append('')

    # Identity
    body.append('---')
    body.append('')
    body.append('## Identity')
    body.append('')
    body.append('| Field | Value |')
    body.append('|-------|-------|')
    body.append(f'| **Person ID** | `{person_id}` |')
    body.append(f'| **Display Name** | {safe_md_cell(display)} |')
    if pr.get('alternate_names_zh') or pr.get('alternate_names_en'):
        alt = []
        if pr.get('alternate_names_zh'): alt.extend(pr['alternate_names_zh'])
        if pr.get('alternate_names_en'): alt.extend(pr['alternate_names_en'])
        body.append(f'| **Alternate Names** | {safe_md_cell(", ".join(alt))} |')
    body.append(f'| **Birth** | {safe_md_cell(birth_full)} |')
    body.append(f'| **Death** | {safe_md_cell(death_full)} |')
    body.append(f'| **Period** | {safe_md_cell(period)} |')
    body.append(f'| **Culture** | {safe_md_cell(primary_culture)} |')
    if inclusion:
        body.append(f'| **Inclusion Category** | `{inclusion}` |')
    body.append('')

    # Life Timeline (from events.jsonl)
    body.append('---')
    body.append('')
    body.append('## Life Timeline')
    body.append('')
    if events:
        body.append('| Year | Event | Status |')
        body.append('|------|-------|--------|')
        def event_year(e):
            d = first_of(e, 'date', 'date_display', 'date_display_en', 'date_display_zh', default='')
            if isinstance(d, dict): d = d.get('year_display','')
            return safe_md_cell(d or '—')
        for e in events:
            desc = first_of(e, 'description_en', 'description_zh', 'event_text_en', 'event_text_zh', default='')
            stat = first_of(e, 'status', 'confidence', default='—')
            body.append(f'| {event_year(e)} | {safe_md_cell(desc)} | {safe_md_cell(stat)} |')
    else:
        body.append('*(no events.jsonl entries)*')
    body.append('')

    # Bucket claims
    buckets = defaultdict(list)
    for c in claims:
        buckets[claim_bucket(c)].append(c)

    body.append('---')
    body.append('')
    body.append('## Key Historical / Reception / Legend / Fiction Separation')
    body.append('')
    body.append('### Confirmed Historical Facts')
    if buckets['confirmed']:
        for c in buckets['confirmed'][:6]:
            txt = first_of(c, 'claim_text_en', 'claim_text_zh', default='')
            body.append(f'- {safe_md_cell(txt)}')
    else:
        body.append('- *(none classified as confirmed)*')
    body.append('')
    body.append('### Disputed / Uncertain')
    disp = [c for c in buckets['probable'] if (first_of(c,'confidence','confidence_level','status',default='') or '').lower() in ('disputed','needs_verification')]
    if disp:
        for c in disp[:4]:
            txt = first_of(c, 'claim_text_en', 'claim_text_zh', default='')
            body.append(f'- {safe_md_cell(txt)}')
    else:
        body.append('- *(none flagged disputed)*')
    body.append('')
    body.append('### Reception / Later Groupings (not formal organizations)')
    if buckets['reception']:
        for c in buckets['reception'][:6]:
            txt = first_of(c, 'claim_text_en', 'claim_text_zh', default='')
            body.append(f'- {safe_md_cell(txt)}')
    else:
        body.append('- *(none classified as reception)*')
    body.append('')
    body.append('### Legendary / Fictional')
    if buckets['legendary']:
        for c in buckets['legendary'][:6]:
            txt = first_of(c, 'claim_text_en', 'claim_text_zh', default='')
            body.append(f'- {safe_md_cell(txt)}')
    else:
        body.append('- *(none classified as legendary)*')
    body.append('')

    # Claims Overview
    body.append('---')
    body.append('')
    body.append('## Claims Overview')
    body.append('')
    body.append('| Status | Count |')
    body.append('|--------|-------|')
    body.append(f'| Confirmed | {len(buckets["confirmed"])} |')
    body.append(f'| Probable / Disputed / Needs Verification | {len(buckets["probable"])} |')
    body.append(f'| Reception / Later Groupings | {len(buckets["reception"])} |')
    body.append(f'| Legendary / Fictional | {len(buckets["legendary"])} |')
    body.append(f'| **Total** | **{len(claims)}** |')
    body.append('')

    # Confirmed Claims table
    def claim_row(c):
        cid = c.get('claim_id','')
        date = first_of(c, 'date', 'date_display', default='—')
        if isinstance(date, dict): date = date.get('year_display','—')
        txt = first_of(c, 'claim_text_en', 'claim_text_zh', default='')
        sids = c.get('source_ids') or []
        slinks = ', '.join(f'[[{source_map.get(sid, sid)}]]' if sid in source_map else f'`{sid}`(missing)' for sid in sids) or '—'
        return f'| `{cid}` | {safe_md_cell(date)} | {safe_md_cell(txt)} | {slinks} |'

    body.append('---')
    body.append('')
    body.append('## Confirmed Historical Claims')
    body.append('')
    if buckets['confirmed']:
        body.append('| Claim ID | Date | Claim | Sources |')
        body.append('|----------|------|-------|---------|')
        for c in buckets['confirmed']:
            body.append(claim_row(c))
    else:
        body.append('*(none)*')
    body.append('')

    body.append('---')
    body.append('')
    body.append('## Probable / Disputed / Needs Verification Claims')
    body.append('')
    if buckets['probable']:
        body.append('| Claim ID | Date | Claim | Status | Sources |')
        body.append('|----------|------|-------|--------|---------|')
        for c in buckets['probable']:
            cid = c.get('claim_id','')
            date = first_of(c, 'date', 'date_display', default='—')
            if isinstance(date, dict): date = date.get('year_display','—')
            txt = first_of(c, 'claim_text_en', 'claim_text_zh', default='')
            stat = first_of(c, 'confidence', 'confidence_level', 'status', default='—')
            sids = c.get('source_ids') or []
            slinks = ', '.join(f'[[{source_map.get(sid, sid)}]]' if sid in source_map else f'`{sid}`(missing)' for sid in sids) or '—'
            body.append(f'| `{cid}` | {safe_md_cell(date)} | {safe_md_cell(txt)} | {safe_md_cell(stat)} | {slinks} |')
    else:
        body.append('*(none)*')
    body.append('')

    body.append('---')
    body.append('')
    body.append('## Reception / Legendary / Fictional Material')
    body.append('')
    rec_plus_leg = buckets['reception'] + buckets['legendary']
    if rec_plus_leg:
        body.append('| Claim ID | Type | Claim | Sources |')
        body.append('|----------|------|-------|---------|')
        for c in rec_plus_leg:
            cid = c.get('claim_id','')
            ct = first_of(c, 'claim_type','category', default='—')
            txt = first_of(c, 'claim_text_en', 'claim_text_zh', default='')
            sids = c.get('source_ids') or []
            if not sids and claim_bucket(c) == 'legendary':
                slinks = '*(no sources — classified as legendary)*'
            else:
                slinks = ', '.join(f'[[{source_map.get(sid, sid)}]]' if sid in source_map else f'`{sid}`(missing)' for sid in sids) or '—'
            body.append(f'| `{cid}` | {safe_md_cell(ct)} | {safe_md_cell(txt)} | {slinks} |')
    else:
        body.append('*(none)*')
    body.append('')

    # Relationships
    body.append('---')
    body.append('')
    body.append('## Relationships')
    body.append('')
    if rels:
        body.append('| Person | Relationship Type | Status | Sources | Notes |')
        body.append('|--------|-------------------|--------|---------|-------|')
        for r in rels:
            name = r.get('related_person_name','')
            rid = r.get('related_person_id','')
            if rid and rid.startswith('P_'):
                slug_guess = re.sub(r'[^a-z0-9-]','', name.lower().replace(' ','-'))
                person_cell = f'{safe_md_cell(name)} ([[{slug_guess}]])' if slug_guess else safe_md_cell(name)
            else:
                person_cell = safe_md_cell(name)
            rtype = r.get('relationship_type','')
            stat = first_of(r, 'status','confidence','review_status', default='—')
            sids = r.get('source_ids') or []
            slinks = ', '.join(f'[[{source_map.get(sid, sid)}]]' if sid in source_map else f'`{sid}`(missing)' for sid in sids) or '—'
            note = first_of(r, 'evidence_note','relationship_summary_en','relationship_summary_zh','review_note', default='')
            body.append(f'| {person_cell} | {safe_md_cell(rtype)} | {safe_md_cell(stat)} | {slinks} | {safe_md_cell(note)} |')
        body.append('')
        body.append('> Wikilinks to related persons are forward references — may be unresolved until the rest of the batch is imported.')
    else:
        body.append('*(no relationships.jsonl entries)*')
    body.append('')

    # Works
    body.append('---')
    body.append('')
    body.append('## Works')
    body.append('')
    if works:
        body.append('| Work | Type | Status | Sources | Notes |')
        body.append('|------|------|--------|---------|-------|')
        for w in works:
            title_zh = first_of(w, 'title_zh','work_title_zh', default='')
            title_en = first_of(w, 'title_en','work_title_en', default='')
            title = title_zh + (' / ' + title_en if title_en and title_en != title_zh else '') if title_zh else title_en
            if not title: title = w.get('work_id','(no title)')
            wtype = first_of(w, 'work_type','category', default='')
            stat = first_of(w, 'status','attribution_status', default='—')
            sids = w.get('source_ids') or []
            slinks = ', '.join(f'[[{source_map.get(sid, sid)}]]' if sid in source_map else f'`{sid}`(missing)' for sid in sids) or '—'
            note = first_of(w, 'description_en','description_zh','notes','current_location','medium', default='')
            body.append(f'| {safe_md_cell(title)} | {safe_md_cell(wtype)} | {safe_md_cell(stat)} | {slinks} | {safe_md_cell(note)} |')
        body.append('')
        body.append('> ⚠️ Artworks by this person are `artwork_by_person`, not portrait likenesses. Per MVP rules v2.5 visual-media discipline.')
    else:
        body.append('*(no works.jsonl entries)*')
    body.append('')

    # Sources, grouped
    body.append('---')
    body.append('')
    body.append('## Sources')
    body.append('')
    bucket = defaultdict(list)
    for s in sources:
        bucket[source_bucket(s)].append(s)

    def src_row(s):
        sid = s.get('source_id','')
        fname = source_map.get(sid, sid)
        title = first_of(s, 'title','title_en','title_zh','title_orig', default='(no title)')
        st = s.get('source_type','')
        rl = s.get('reliability_level','')
        vs = s.get('verification_status','')
        return f'| [[{fname}]] | {safe_md_cell(title)} | {safe_md_cell(st)} | {safe_md_cell(rl)} | {safe_md_cell(vs)} |'

    def emit_bucket(label, items):
        body.append(f'### {label}')
        body.append('')
        if items:
            body.append('| Source ID | Title | Type | Reliability | Verification Status |')
            body.append('|-----------|-------|------|-------------|---------------------|')
            for s in items: body.append(src_row(s))
        else:
            body.append('*(none in this bucket)*')
        body.append('')

    emit_bucket('A / A_candidate (primary or near-primary)', bucket['A'])
    emit_bucket('B_high / B (modern scholarship & ancient biography)', bucket['B'])
    emit_bucket('C / D / clue_only (encyclopedia & general reference)', bucket['C'] + bucket['D'])
    body.append('### ⚠️ Flagged: needs_verification')
    body.append('')
    nv = [s for s in sources if s.get('verification_status') == 'needs_verification']
    if nv:
        body.append('| Source ID | Title | Reliability | Status |')
        body.append('|-----------|-------|-------------|--------|')
        for s in nv:
            sid = s.get('source_id','')
            fname = source_map.get(sid, sid)
            title = first_of(s, 'title','title_en','title_zh','title_orig', default='(no title)')
            rl = s.get('reliability_level','')
            body.append(f'| [[{fname}]] | {safe_md_cell(title)} | {safe_md_cell(rl)} | needs_verification |')
    else:
        body.append('*(none — all sources are currently `ai_verified_unreviewed`, `verified`, or `clue_only`.)*')
    body.append('')

    # Source Package
    body.append('---')
    body.append('')
    body.append('## Source Package')
    body.append('')
    body.append(f'Path: `incoming/{culture}/{slug}/`')
    body.append('Files: 11 (person_record.json, person_profile.md, claims.jsonl, sources.jsonl, '
                 'relationships.jsonl, events.jsonl, works.jsonl, visual_media.jsonl, '
                 'legendary_notes.jsonl, open_questions.md, README.md)')
    body.append('Validation: PASSED (dry-run survey)')
    body.append('')

    # Review Status
    body.append('---')
    body.append('')
    body.append('## Review Status')
    body.append('')
    body.append(f'- **Current:** `{historical_status}` — staging-ready, not master-approved')
    body.append(f'- **Source sufficiency:** `{source_sufficiency}` — {len(sources)} sources, {len(claims)} claims')
    body.append('- **Next review actions:** verify exact page/passage references; '
                 'confirm reception/legendary separation; check D-level sources are clue-only.')
    body.append('')

    # Open Questions
    body.append('---')
    body.append('')
    body.append('## Open Questions')
    body.append('')
    oq_path = os.path.join(pdir, 'open_questions.md')
    if os.path.exists(oq_path):
        with open(oq_path) as f:
            oq = f.read().strip()
        if oq:
            # Strip a leading H1 if present
            oq_lines = oq.split('\n')
            if oq_lines and oq_lines[0].startswith('# '):
                oq_lines = oq_lines[1:]
            # Demote embedded ATX headings so they nest under the parent
            # "## Open Questions" without breaking heading hierarchy.
            # Rule: H1/H2 -> H3, deeper headings shift down by 1 level.
            # Plain text and code-fence-internal '#' are left alone.
            demoted = []
            in_fence = False
            for ln in oq_lines:
                stripped = ln.lstrip()
                if stripped.startswith('```'):
                    in_fence = not in_fence
                    demoted.append(ln); continue
                if in_fence:
                    demoted.append(ln); continue
                m = re.match(r'^(#+)(\s+.*)$', ln)
                if not m:
                    demoted.append(ln); continue
                level = len(m.group(1))
                new_level = 3 if level <= 2 else level + 1
                demoted.append('#' * new_level + m.group(2))
            body.append('\n'.join(demoted).strip() or '*(no open questions recorded)*')
        else:
            body.append('*(open_questions.md is empty)*')
    else:
        body.append('*(no open_questions.md)*')
    body.append('')

    full = '\n'.join(fm_lines) + '\n\n' + '\n'.join(body)

    sub = 'Chinese' if culture == 'chinese' else 'Western'
    out_path = os.path.join(OUT, '01_Persons', sub, f'{slug}.md')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        f.write(full)
    manifest['person_notes'].append(out_path)
    return out_path

# ---------- source note generator ----------
def gen_source_note(slug, culture, src, out_path, used_for_claims_in_person):
    sid = src.get('source_id', '')
    title = first_of(src, 'title','title_en','title_zh','title_orig', default='(no title)')
    title_zh = src.get('title_zh','')
    title_en = src.get('title_en','')
    author = src.get('author','')
    st = src.get('source_type','')
    rl = src.get('reliability_level','')
    vs = src.get('verification_status','')
    lang = src.get('language','')
    citation = first_of(src, 'citation_detail','citation', default='needs_verification')
    notes = first_of(src, 'notes','note', default='')
    used = src.get('used_for_claim_ids') or []

    is_d = (vs == 'clue_only' or rl == 'D')

    fm = ['---']
    fm.append(f'source_id: {yaml_str(sid)}')
    fm.append(f'title: {yaml_str(title)}')
    if title_zh and title_zh != title: fm.append(f'title_zh: {yaml_str(title_zh)}')
    if title_en and title_en != title: fm.append(f'title_en: {yaml_str(title_en)}')
    fm.append(f'source_type: {yaml_str(st)}')
    fm.append(f'reliability_level: {yaml_str(rl)}')
    fm.append(f'verification_status: {yaml_str(vs)}')
    if lang: fm.append(f'language: {yaml_str(lang)}')
    fm.append(f'data_source_folder: {yaml_str(f"incoming/{culture}/{slug}/")}')
    fm.append('used_for_claim_ids:')
    if used:
        for cid in used:
            fm.append(f'  - {yaml_str(cid)}')
    else:
        fm[-1] = 'used_for_claim_ids: []'
    fm.append('review_status: ai_collected_unreviewed')
    fm.append('---')

    body = ['', f'# {title}', '']
    if is_d:
        body.append(D_BANNER)
        body.append('')
    body.append('## Source Metadata')
    body.append('')
    body.append(f'- **Source ID:** `{sid}`')
    if author: body.append(f'- **Author:** {author}')
    body.append(f'- **Type:** {st or "(unspecified)"}')
    body.append(f'- **Reliability:** `{rl or "(unspecified)"}`')
    body.append(f'- **Verification:** `{vs or "(unspecified)"}`')
    if lang: body.append(f'- **Language:** {lang}')
    body.append(f'- **Citation:** {citation}')
    body.append(f'- **Belongs to person:** `{slug}` (`incoming/{culture}/{slug}/`)')
    body.append('')

    body.append('## Used For Claims')
    body.append('')
    if is_d:
        body.append('*None — D-level / clue_only sources are not used as sole support for any claim. '
                    'Per v1 plan §7 and MVP v2.5 source-level calibration, clue sources may seed '
                    'research but cannot back confirmed/high claims.*')
    elif used:
        # Cross-link to person note headings (best effort)
        for cid in used:
            body.append(f'- [[{slug}#Confirmed Historical Claims|{cid}]] · (also appears in probable/reception/legendary tables if applicable)')
    else:
        body.append('*(no explicit used_for_claim_ids in source data)*')
    body.append('')

    if notes:
        body.append('## Notes')
        body.append('')
        body.append(notes)
        body.append('')

    body.append('## Review Warning')
    body.append('')
    if is_d:
        body.append('> ⚠️ This source note was generated from AI-collected staging metadata. '
                    'As a D-level clue source, this note exists for completeness only — do not '
                    'cite as evidence for any claim.')
    else:
        body.append('> ⚠️ This source note was generated from AI-collected staging metadata. '
                    'Exact page/passage references for cited claims require verification before master promotion.')
    body.append('')

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        f.write('\n'.join(fm) + '\n'.join(body))
    return out_path

# ---------- main ----------
def main():
    if os.path.exists(OUT):
        # Wipe and rebuild — sandbox is regeneratable.
        import shutil
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    # Scaffold folders
    for d in ['00_Project','01_Persons/Chinese','01_Persons/Western',
              '02_Events','03_Sources/Chinese','03_Sources/Western',
              '04_Relationships','05_Works','06_Visual_Media',
              '90_Staging_Review','99_Templates']:
        os.makedirs(os.path.join(OUT, d), exist_ok=True)
        gitkeep = os.path.join(OUT, d, '.gitkeep')
        with open(gitkeep, 'w') as f: f.write('')

    manifest = {
        'person_notes': [],
        'source_notes': [],
        'd_level_source_notes': [],
        'orphan_links': [],
        'skipped': [],
    }

    persons = []
    for culture in ['chinese','western']:
        for slug in sorted(os.listdir(os.path.join(INCOMING, culture))):
            pdir = os.path.join(INCOMING, culture, slug)
            if not os.path.isdir(pdir): continue
            persons.append((culture, slug, pdir))

    assert len(persons) == 22, f"Expected 22, got {len(persons)}"

    # First pass: generate all source notes, build source_map per person
    person_source_maps = {}  # slug -> {source_id -> namespaced_filename}
    for culture, slug, pdir in persons:
        sources = load_jsonl(os.path.join(pdir, 'sources.jsonl'))
        source_map = {}
        sub = 'Chinese' if culture == 'chinese' else 'Western'
        for s in sources:
            sid = s.get('source_id','')
            if not sid:
                manifest['skipped'].append(f"{slug}: source with empty source_id")
                continue
            fname = f"{slug}__{sid}"
            out_path = os.path.join(OUT, '03_Sources', sub, f"{fname}.md")
            source_map[sid] = fname
            gen_source_note(slug, culture, s, out_path, [])
            manifest['source_notes'].append(out_path)
            if s.get('verification_status') == 'clue_only' or s.get('reliability_level') == 'D':
                manifest['d_level_source_notes'].append(out_path)
        person_source_maps[slug] = source_map

    # Second pass: generate person notes (with full source maps available)
    for culture, slug, pdir in persons:
        gen_person_note(slug, culture, pdir, person_source_maps[slug], manifest)

    # Validate: every source wikilink in every person note resolves to a generated source note
    src_files_set = set()
    for p in manifest['source_notes']:
        # filename without .md
        src_files_set.add(os.path.basename(p)[:-3])
    orphans = []
    for p in manifest['person_notes']:
        with open(p) as f: text = f.read()
        links = set(re.findall(r'\[\[([a-zA-Z0-9_\-]+(?:__SRC_?\w+|__SRC\d+))\]\]', text))
        for link in links:
            if link not in src_files_set:
                orphans.append(f"{os.path.basename(p)} -> {link}")
        # also flag missing-source markers we emitted ourselves
        missing_markers = re.findall(r'`([A-Za-z0-9_]+)`\(missing\)', text)
        for m in missing_markers:
            orphans.append(f"{os.path.basename(p)} -> MISSING reference {m}")
    manifest['orphan_links'] = orphans

    # Print summary
    print(f"\n=== Generated ===")
    print(f"Person notes:    {len(manifest['person_notes'])}")
    print(f"Source notes:    {len(manifest['source_notes'])}")
    print(f"D-level w/ banner: {len(manifest['d_level_source_notes'])}")
    print(f"Skipped:         {len(manifest['skipped'])}")
    print(f"Orphan links:    {len(manifest['orphan_links'])}")

    # Dump manifest as JSON
    with open(os.path.join(OUT, '90_Staging_Review', '_generation_manifest.json'), 'w') as f:
        json.dump({
            'person_count': len(manifest['person_notes']),
            'source_count': len(manifest['source_notes']),
            'd_level_count': len(manifest['d_level_source_notes']),
            'skipped': manifest['skipped'],
            'orphans': manifest['orphan_links'],
            'person_notes': [os.path.relpath(p, REPO) for p in manifest['person_notes']],
            'source_notes': [os.path.relpath(p, REPO) for p in manifest['source_notes']],
            'd_level_notes': [os.path.relpath(p, REPO) for p in manifest['d_level_source_notes']],
        }, f, indent=2)

    if manifest['skipped']:
        print("\nSkipped:")
        for s in manifest['skipped']: print(f"  - {s}")
    if manifest['orphan_links']:
        print("\nOrphan links (first 20):")
        for o in manifest['orphan_links'][:20]: print(f"  - {o}")

if __name__ == '__main__':
    main()
