---
name: gws-slides
description: >
  Google Slides: Read and write presentations via the gws CLI. Use when creating
  presentations, fetching slides, or applying batch updates. Requires gws on PATH
  and auth (see gws-shared).
---

# slides (Google Slides API v1)

Use the `gws` CLI for Google Slides. Ensure auth is configured (see the gws-shared skill).

```bash
gws slides <resource> <method> [flags]
```

## API Resources

### presentations

- `batchUpdate` — Applies one or more updates to the presentation. Each request is validated before being applied.
- `create` — Creates a blank presentation using the title given in the request. Optional `presentationId` in the request.
- `get` — Gets the latest version of the specified presentation.
- `pages` — Operations on the 'pages' resource (get, getThumbnail).

## Discovering Commands

Before calling any API method, inspect it:

```bash
# Browse resources and methods
gws slides --help

# Inspect a method's required params, types, and defaults
gws schema slides.<resource>.<method>
```

Use `gws schema` output to build your `--params` and `--json` flags.

## Examples

```bash
# Get presentation metadata and structure
gws slides presentations get --params '{"presentationId": "YOUR_ID"}'

# Create a presentation
gws slides presentations create --json '{"title": "My Deck"}'
```
