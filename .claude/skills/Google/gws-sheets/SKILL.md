---
name: gws-sheets
description: >
  Google Sheets: Read and write spreadsheets via the gws CLI. Use when listing,
  creating, or updating spreadsheets; reading or writing ranges; or applying batch updates.
  Requires gws on PATH and auth (see gws-shared).
---

# sheets (Google Sheets API v4)

Use the `gws` CLI for Google Sheets. Ensure auth is configured (see the gws-shared skill).

```bash
gws sheets <resource> <method> [flags]
```

## Helper Skills

| Skill | Description |
|-------|-------------|
| gws-sheets-append | Append a row to a spreadsheet |
| gws-sheets-read | Read values from a spreadsheet |

## API Resources

### spreadsheets

- `batchUpdate` — Applies one or more updates to the spreadsheet. Each request is validated before being applied.
- `create` — Creates a spreadsheet, returning the newly created spreadsheet.
- `get` — Returns the spreadsheet at the given ID. Use `fields` or `includeGridData` to control returned data.
- `getByDataFilter` — Returns the spreadsheet with optional data filters for subsets of data.
- `developerMetadata` — Operations on developer metadata.
- `sheets` — Operations on sheet metadata.
- `values` — Operations on the 'values' resource (get, update, append, clear, etc.).

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws sheets --help

# Inspect a method's required params, types, and defaults
gws schema sheets.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

## Examples

```bash
# Get spreadsheet metadata
gws sheets spreadsheets get --params '{"spreadsheetId": "YOUR_ID"}'

# Get values in a range
gws sheets spreadsheets values get --params '{"spreadsheetId": "ID", "range": "Sheet1!A1:D10"}'

# Create a spreadsheet
gws sheets spreadsheets create --json '{"properties": {"title": "My Sheet"}}'
```
