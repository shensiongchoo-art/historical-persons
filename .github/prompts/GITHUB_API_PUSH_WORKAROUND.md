# Prompt: GitHub API Push Workaround v1

When `git push` fails with authentication errors (HTTPS "Password authentication not supported" or SSH "Host key verification failed"), use the GitHub API via `gh api` to push commits directly.

## Prerequisites

Verify `gh` is authenticated:
```bash
gh auth status
# Should show: ✓ Logged in to github.com, Token scopes: 'repo'
```

## Method: Git Data API (4 steps)

### Step 1: Create blobs for each file

For each file in the package:

```bash
# 1. Base64-encode the file content
python3 -c "
import json, base64
with open('PATH/TO/FILE', 'rb') as f:
    content = base64.b64encode(f.read()).decode()
payload = json.dumps({'content': content, 'encoding': 'base64'})
with open('/workspace/blob_FILENAME.json', 'w') as out:
    out.write(payload)
"

# 2. Create the blob via API
gh api /repos/OWNER/REPO/git/blobs --input /workspace/blob_FILENAME.json --jq .sha
# Returns: <blob_sha>
```

Record all blob SHAs mapped to their file paths.

### Step 2: Create a tree

Build a tree payload referencing the parent tree and all blobs:

```json
{
  "base_tree": "<parent_commit_tree_sha>",
  "tree": [
    {"path": "incoming/chinese/person-slug/FILE", "mode": "100644", "type": "blob", "sha": "<blob_sha>"},
    ...
  ]
}
```

```bash
gh api /repos/OWNER/REPO/git/trees --input /workspace/tree_payload.json --jq .sha
# Returns: <tree_sha>
```

Get the parent tree SHA from the base branch:
```bash
gh api /repos/OWNER/REPO/git/commits/<base_branch_head_sha> --jq .tree.sha
```

### Step 3: Create a commit

```json
{
  "message": "commit message",
  "tree": "<tree_sha>",
  "parents": ["<base_branch_head_sha>"]
}
```

```bash
gh api /repos/OWNER/REPO/git/commits --input /workspace/commit_payload.json --jq .sha
# Returns: <commit_sha>
```

### Step 4: Create the branch ref

```bash
gh api /repos/OWNER/REPO/git/refs \
  -f ref=refs/heads/BRANCH-NAME \
  -F sha=<commit_sha>
```

### Step 5: Open a PR

```bash
gh pr create --repo OWNER/REPO --base main --head BRANCH-NAME \
  --title "PR title" --body "PR description"
```

## Important notes

- This bypasses the local git repository entirely — the remote branch is created from scratch via API.
- The local repo won't be aware of the remote branch unless you fetch after (which may also fail if SSH/HTTPS auth is broken).
- All 11 files must be blob-created before the tree step.
- `gh api` uses the token from `gh auth` — this is independent from git's credential helper.

## Cleanup

Remove temp payload files after success:
```bash
rm -f /workspace/blob_*.json /workspace/tree_payload.json /workspace/commit_payload.json
```
