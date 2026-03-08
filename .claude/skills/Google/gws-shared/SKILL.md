---
name: gws-shared
description: >
  gws CLI: Shared patterns for authentication, global flags, and output formatting.
  Required context when using any gws (Google Workspace CLI) skill. Install gws with
  `npm install -g @googleworkspace/cli`.
---

# gws — Shared Reference

## Installation

The `gws` binary must be on `$PATH`. Install with:

```bash
npm install -g @googleworkspace/cli
```

## Authentication

```bash
# Browser-based OAuth (interactive)
gws auth login

# Service Account
export GOOGLE_WORKSPACE_CLI_CREDENTIALS_FILE=/path/to/key.json
```

Credentials can also be set via `GOOGLE_WORKSPACE_CLI_CLIENT_ID` and `GOOGLE_WORKSPACE_CLI_CLIENT_SECRET`, or a `client_secret.json` in `~/.config/gws/`.

## Global Flags

| Flag | Description |
|------|-------------|
| `--format <FMT>` | Output format: `json` (default), `table`, `yaml`, `csv` |
| `--dry-run` | Validate locally without calling the API |
| `--sanitize <TEMPLATE>` | Screen responses through Model Armor |

## CLI Syntax

```bash
gws <service> <resource> [sub-resource] <method> [flags]
```

### Method Flags

| Flag | Description |
|------|-------------|
| `--params '{"key": "val"}'` | URL/query parameters |
| `--json '{"key": "val"}'` | Request body |
| `-o, --output <PATH>` | Save binary responses to file |
| `--upload <PATH>` | Upload file content (multipart) |
| `--page-all` | Auto-paginate (NDJSON output) |
| `--page-limit <N>` | Max pages when using --page-all (default: 10) |
| `--page-delay <MS>` | Delay between pages in ms (default: 100) |

## Security Rules

- **Never** output secrets (API keys, tokens) directly
- **Always** confirm with user before executing write/delete commands
- Prefer `--dry-run` for destructive operations
- Use `--sanitize` for PII/content safety screening
