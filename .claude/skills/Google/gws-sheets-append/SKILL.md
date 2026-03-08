---
name: gws-sheets-append
description: >
  Google Sheets: Append a row (or rows) to a spreadsheet via the gws CLI. Use when
  adding data to the end of a sheet. Requires gws on PATH and auth (see gws-shared).
---

# sheets +append

Append one or more rows to a spreadsheet. Ensure auth is configured (see the gws-shared skill).

## Usage

```bash
gws sheets +append --spreadsheet <ID>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--spreadsheet` | ✓ | — | Spreadsheet ID |
| `--values` | — | — | Comma-separated values (simple strings) for a single row |
| `--json-values` | — | — | JSON array of rows, e.g. `'[["a","b"],["c","d"]]'` |

## Examples

```bash
gws sheets +append --spreadsheet ID --values 'Alice,100,true'
gws sheets +append --spreadsheet ID --json-values '[["a","b"],["c","d"]]'
```

## Tips

- Use `--values` for simple single-row appends.
- Use `--json-values` for bulk multi-row inserts.
- **Write command** — confirm with the user before executing.
