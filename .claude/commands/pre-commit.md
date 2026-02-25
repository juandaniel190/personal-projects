---
name: pre-commit
description: Run SQLFluff on modified SQL files to fix linting issues. Detects changed SQL files from git, auto-fixes formatting, and offers to commit the fixes.
disable-model-invocation: true
---

Run SQLFluff linting on modified SQL files in the Eventbrite Analytics Engineering repo.

**Steps:**

```bash
# 1. Get modified SQL files from last commit
git diff --name-only HEAD~1 HEAD | grep '\.sql$' | grep '^docker/dbtae/dbtae/'

# Or get staged SQL files
git diff --cached --name-only | grep '\.sql$' | grep '^docker/dbtae/dbtae/'

# 2. Run SQLFluff on those files
./run_sqlfluff.sh docker/dbtae/dbtae <file1> <file2> ...
```

**What SQLFluff fixes:**
- Trailing whitespace removal
- Keyword capitalization (e.g. `IS NULL` → `is NULL`)
- Indentation fixes
- Line break formatting for multi-line conditions

**Output:**
1. Show which files were processed.
2. Show how many violations were found and fixed.
3. Show `git diff` of any changes made.
4. Ask user if they want to commit the formatting fixes.

Run after committing SQL file changes.
