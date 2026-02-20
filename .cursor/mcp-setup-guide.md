stg# Rovo Dev MCP with JIRA Setup Guide

## Overview
This guide helps you set up the Rovo Dev MCP server with JIRA in Cursor.

## Prerequisites
- Cursor IDE installed
- Atlassian account with JIRA access
- Eventbrite JIRA instance access

## Setup Steps

### 1. Open Cursor Settings
1. Open Cursor
2. Go to **Settings** (Cmd+, on Mac, Ctrl+, on Windows/Linux)
3. Navigate to **Features** → **Model Context Protocol** (or search for "MCP")

### 2. Add Rovo Dev MCP Server
In the MCP settings, you'll need to add a new server configuration. The configuration should include:

**Server Name:** `rovo-dev-jira` or `jira`

**Configuration Options:**

**Option A: Using Rovo Dev Binary (from Atlassian Code Extension)**
- **Command:** Full path to the binary (Cursor will auto-detect this)
  - Example: `/Users/damezquita/Library/Application Support/Cursor/User/workspaceStorage/[workspace-id]/atlassian.atlascode/atlascode-rovodev-bin/0.12.16/atlassian_cli_rovodev`
- **Args:** `serve`, `40526`, `--xid`, `rovodev-ide-vscode`, `--site-url`, `https://eventbrite.atlassian.net`, `--respect-configured-permissions`
  - **Important:** Each argument must be on a separate line or comma-separated, NOT as a single quoted string
  - The port number (40526) may vary - Cursor will assign it dynamically

**Option B: Using npm-based JIRA MCP Server (Recommended if Rovo Dev fails)**
- **Command:** `npx`
- **Args:** `-y`, `@modelcontextprotocol/server-jira`
- **Environment Variables:**
  - `JIRA_EMAIL`: `damezquita@eventbrite.com`
  - `JIRA_API_TOKEN`: Your JIRA API token (get from https://id.atlassian.com/manage-profile/security/api-tokens)
  - `JIRA_INSTANCE_URL`: `https://eventbrite.atlassian.net`

**Option C: Using Rovo Dev CLI (if installed globally)**
- **Command:** `rovodev`
- **Args:** `serve`, `40526`, `--xid`, `rovodev-ide-vscode`, `--site-url`, `https://eventbrite.atlassian.net`, `--respect-configured-permissions`

**Environment Variables (for Rovo Dev):**
Rovo Dev uses OAuth authentication, so you typically don't need to set environment variables. However, if needed:
- `ATLASSIAN_EMAIL`: Your Atlassian email (e.g., `damezquita@eventbrite.com`)
- `ATLASSIAN_INSTANCE_URL`: Your JIRA instance URL (e.g., `https://eventbrite.atlassian.net`)

### 3. Authentication
Rovo Dev MCP uses OAuth 2.1 for authentication:
1. When you first use the MCP server, you'll be prompted to authenticate
2. You'll be redirected to Atlassian to log in
3. Approve the necessary permissions for Rovo Dev to access your JIRA data

### 4. Verify Connection
After setup, test the connection by:
1. Using the `/jira` command in Cursor
2. Asking: "which tickets do I have assigned?"
3. If it works, you should see your JIRA issues

## Alternative: Direct JIRA MCP Server

If Rovo Dev MCP isn't available, you can use a direct JIRA MCP server:

**Configuration:**
```json
{
  "mcpServers": {
    "jira": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-jira"],
      "env": {
        "JIRA_EMAIL": "damezquita@eventbrite.com",
        "JIRA_API_TOKEN": "your-api-token",
        "JIRA_INSTANCE_URL": "https://eventbrite.atlassian.net"
      }
    }
  }
}
```

## Getting Your JIRA API Token

1. Go to https://id.atlassian.com/manage-profile/security/api-tokens
2. Click **Create API token**
3. Give it a label (e.g., "Cursor MCP")
4. Copy the token and use it in your MCP configuration

## Troubleshooting

### Rovo Dev Binary Exit Code 1 Error

If you see an error like:
```
atlassian_cli_rovodev 'serve', '40526', '--xid', 'rovodev-ide-vscode' terminated with exit code: 1
```

**Possible Causes and Solutions:**

1. **Binary Permissions Issue**
   - The binary may not have execute permissions
   - **Fix:** Open Terminal and run:
     ```bash
     chmod +x "/Users/damezquita/Library/Application Support/Cursor/User/workspaceStorage/7566f44e38863fc21dd51e4380c2fbb0/atlassian.atlascode/atlascode-rovodev-bin/0.12.16/atlassian_cli_rovodev"
     ```
   - **Note:** The path may vary. Check Cursor's error message for the exact path.

2. **Corrupted or Incomplete Binary**
   - The binary may be corrupted or incomplete
   - **Fix:** 
     - Find your workspace storage path (check Cursor's error message)
     - Remove the binary directory:
       ```bash
       rm -rf "/Users/damezquita/Library/Application Support/Cursor/User/workspaceStorage/[your-workspace-id]/atlassian.atlascode/atlascode-rovodev-bin"
       ```
     - Restart Cursor to re-download the binary
     - Or reinstall the Atlassian Code extension in Cursor

3. **Missing Dependencies**
   - The binary may require system libraries
   - **Fix:** Check if you have the required dependencies:
     ```bash
     # Check if the binary exists and is executable
     ls -la "/Users/damezquita/Library/Application Support/Cursor/User/workspaceStorage/[workspace-id]/atlassian.atlascode/atlascode-rovodev-bin/0.12.16/atlassian_cli_rovodev"
     
     # Try running it manually to see the actual error
     "/Users/damezquita/Library/Application Support/Cursor/User/workspaceStorage/[workspace-id]/atlassian.atlascode/atlascode-rovodev-bin/0.12.16/atlassian_cli_rovodev" --help
     ```

4. **Use Alternative JIRA MCP Server (Recommended)**
   - If Rovo Dev continues to fail, use the direct JIRA MCP server instead
   - **Fix:** 
     - Open Cursor Settings → Features → Model Context Protocol
     - Remove the existing Rovo Dev MCP server configuration
     - Add a new server with:
       - **Server Name:** `jira`
       - **Command:** `npx`
       - **Args:** `-y`, `@modelcontextprotocol/server-jira`
       - **Environment Variables:**
         - `JIRA_EMAIL`: `damezquita@eventbrite.com`
         - `JIRA_API_TOKEN`: (your API token from https://id.atlassian.com/manage-profile/security/api-tokens)
         - `JIRA_INSTANCE_URL`: `https://eventbrite.atlassian.net`

5. **Argument Parsing Issue (Most Common)**
   - Cursor may be passing arguments incorrectly as a single quoted string
   - **Fix:** 
     - Open Cursor Settings → Features → Model Context Protocol
     - Find your Rovo Dev MCP server configuration
     - **Command field:** Should be the full path to `atlassian_cli_rovodev` binary
     - **Args field:** Should be separate arguments, one per line or comma-separated:
       ```
       serve
       40526
       --xid
       rovodev-ide-vscode
       --site-url
       https://eventbrite.atlassian.net
       --respect-configured-permissions
       ```
     - **NOT** as a single string: `'serve', '40526', '--xid', ...`
     - If you can't fix the argument format, switch to Option B (npm-based server) above

6. **Check Cursor MCP Configuration**
   - The MCP server configuration might be incorrect
   - **Fix:** 
     - Open Cursor Settings → Features → Model Context Protocol
     - Verify the command and arguments are correct
     - For Rovo Dev, the command should be the full path to the binary
     - Arguments should be passed separately, not as a single quoted string
     - If the configuration UI doesn't allow proper argument formatting, use the alternative npm-based server

### MCP Server Not Found
- Ensure Rovo Dev CLI is installed: `npm install -g @atlassian/rovo-dev-cli`
- Or install the JIRA MCP server: `npm install -g @modelcontextprotocol/server-jira`

### Authentication Errors
- Verify your API token is correct
- Check that your email matches your Atlassian account
- Ensure you have the necessary JIRA permissions
- For Rovo Dev, you may need to authenticate via OAuth in a browser

### Connection Timeout
- Verify your JIRA instance URL is correct
- Check your network connection
- Ensure firewall isn't blocking the connection

## Testing the Setup

Once configured, test with these commands:
```
/jira which tickets do I have assigned?
/jira show me my open issues
/jira what's the status of EB-304407?
```

## Available MCP Tools

Once set up, you'll have access to:
- `mcp_jira_get_issue` - Get details of a specific issue
- `mcp_jira_search_issues` - Search for issues using JQL
- `mcp_jira_create_issue` - Create new issues
- `mcp_jira_update_issue` - Update existing issues
- `mcp_jira_add_comment` - Add comments to issues
- `mcp_jira_transition_issue` - Change issue status

## Notes

- The MCP server configuration is stored in Cursor's settings, not in this project
- API tokens should be kept secure and not committed to version control
- If you're using Rovo Dev, make sure you have the latest version installed

