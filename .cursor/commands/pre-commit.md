### 🧩 **Cursor Command: pre-commit**

```yaml
name: pre-commit
description: Run SQLFluff on modified SQL files to fix linting issues after committing changes
prompt: |
  You are a coding assistant helping to run SQLFluff linting on SQL files in the Eventbrite Analytics Engineering repo.

  **Task**
  Run SQLFluff on modified SQL files to automatically fix linting violations. This should be run after committing changes to SQL files.

  **Steps**
  1. Get the list of modified SQL files from git (files that were changed in the last commit or currently staged)
  2. Run the SQLFluff script: `./run_sqlfluff.sh docker/dbtae/dbtae <sql_file1> <sql_file2> ...`
  3. Show the user what was fixed
  4. If there are changes, ask if they want to commit the formatting fixes

  **Command to run**
  ```bash
  # Get modified SQL files from last commit
  git diff --name-only HEAD~1 HEAD | grep '\.sql$' | grep '^docker/dbtae/dbtae/'
  
  # Or get staged SQL files
  git diff --cached --name-only | grep '\.sql$' | grep '^docker/dbtae/dbtae/'
  
  # Run SQLFluff on those files
  ./run_sqlfluff.sh docker/dbtae/dbtae <file1> <file2> ...
  ```

  **What SQLFluff fixes**
  - Trailing whitespace removal
  - Keyword capitalization (IS NULL → is NULL)
  - Indentation fixes
  - Line break formatting for multi-line conditions

  **Output**
  - Show which files were processed
  - Show how many violations were found and fixed
  - Show git diff of any changes made
  - Ask user if they want to commit the formatting fixes
```

**Behavior**

* Automatically detects modified SQL files from git
* Runs SQLFluff with auto-fix enabled
* Shows what was changed
* Prompts user to commit formatting fixes if any were made

**Usage**

After committing SQL changes, run:
```
/cursor-command pre-commit
```

The command will:
1. Find modified SQL files
2. Run SQLFluff to fix formatting
3. Show you the changes
4. Ask if you want to commit the fixes

