---
name: gws-sheets-read
description: >
  Google Sheets: Read values from a spreadsheet via the gws CLI. Use when fetching
  cell ranges or sheet data. Read-only; never modifies the spreadsheet. Requires
  gws on PATH and auth (see gws-shared).
---

# sheets +read

Read values from a spreadsheet. Ensure auth is configured (see the gws-shared skill).

## Usage

```bash
gws sheets +read --spreadsheet <ID> --range <RANGE>
```

## Flags

| Flag | Required | Default | Description |
|------|----------|---------|-------------|
| `--spreadsheet` | ✓ | — | Spreadsheet ID |
| `--range` | ✓ | — | Range to read (e.g. `Sheet1!A1:B2` or `Sheet1`) |

## Examples

```bash
gws sheets +read --spreadsheet ID --range 'Sheet1!A1:D10'
gws sheets +read --spreadsheet ID --range Sheet1
```

## Tips

- Read-only — never modifies the spreadsheet.
- For advanced options (value render, date format), use the raw `spreadsheets values get` API with `--params`.
