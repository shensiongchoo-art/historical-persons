#!/usr/bin/env python3
import json
import sys
from pathlib import Path

REQUIRED = [
    "README.md",
    "person_profile.md",
    "person_record.json",
    "claims.jsonl",
    "sources.jsonl",
    "relationships.jsonl",
    "events.jsonl",
    "works.jsonl",
    "visual_media.jsonl",
    "legendary_notes.jsonl",
    "open_questions.md",
]

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except Exception as e:
                raise ValueError(f"{path}:{i}: invalid JSONL: {e}") from e
    return rows

def collect_source_ids(rows):
    ids = set()
    for r in rows:
        sid = r.get("source_id") or r.get("id")
        if sid:
            ids.add(sid)
    return ids

def refs_from_obj(obj):
    vals = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k in {"source_id", "source_ids"}:
                vals.extend(v if isinstance(v, list) else [v])
            else:
                vals.extend(refs_from_obj(v))
    elif isinstance(obj, list):
        for v in obj:
            vals.extend(refs_from_obj(v))
    return vals

def main():
    if len(sys.argv) != 2:
        print("Usage: validate_package.py <person_folder>")
        return 2

    folder = Path(sys.argv[1])
    errors = []

    if not folder.exists():
        errors.append(f"Folder does not exist: {folder}")
    else:
        for name in REQUIRED:
            if not (folder / name).exists():
                errors.append(f"Missing required file: {name}")

        if (folder / "references.jsonl").exists():
            errors.append("references.jsonl is not allowed in the person root folder. Move raw notes to _raw/ or remove it.")

        try:
            record = load_json(folder / "person_record.json")
            if not record.get("person_id"):
                errors.append("person_record.json: person_id is empty")
        except Exception as e:
            errors.append(f"person_record.json invalid: {e}")

        jsonl_data = {}
        for name in [
            "claims.jsonl",
            "sources.jsonl",
            "relationships.jsonl",
            "events.jsonl",
            "works.jsonl",
            "visual_media.jsonl",
            "legendary_notes.jsonl",
        ]:
            p = folder / name
            if p.exists():
                try:
                    jsonl_data[name] = load_jsonl(p)
                except Exception as e:
                    errors.append(str(e))

        source_ids = collect_source_ids(jsonl_data.get("sources.jsonl", []))
        for name, rows in jsonl_data.items():
            if name == "sources.jsonl":
                continue
            for row in rows:
                for sid in refs_from_obj(row):
                    if sid and sid not in source_ids:
                        errors.append(f"{name}: references undefined source_id {sid}")

    if errors:
        print("VALIDATION FAILED")
        for e in errors:
            print(f"- {e}")
        return 1

    print("VALIDATION PASSED")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
