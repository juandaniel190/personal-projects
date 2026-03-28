#!/usr/bin/env bun

/**
 * Issue Lifecycle Comment - Minimal Placeholder Implementation
 *
 * This script is a placeholder that prevents GitHub Actions workflow failures.
 * It exists because this is a personal portfolio repository that doesn't actively
 * use GitHub issues, so automated lifecycle comments are not needed.
 *
 * Purpose:
 * - Validates required environment variables
 * - Logs label event details
 * - Exits successfully to prevent workflow errors
 *
 * If this repository grows to need real issue management, refer to:
 * https://github.com/anthropics/claude-code/tree/main/scripts
 *
 * Triggered by: .github/workflows/issue-lifecycle-comment.yml (on issue labeled events)
 */

import { validateEnv, log, info, success } from "./lib/github";

// Validate required environment variables
const env = validateEnv(["GITHUB_TOKEN", "LABEL", "ISSUE_NUMBER"]);

// Log execution details
info("Issue Lifecycle Comment script started");

log("lifecycle-comment.ts", {
  status: "placeholder",
  mode: "no-op",
  message: "This is a minimal placeholder implementation",
  reason: "Personal portfolio repository - automated lifecycle comments not needed",
  event: {
    label: env.LABEL,
    issueNumber: env.ISSUE_NUMBER,
    hasToken: !!env.GITHUB_TOKEN,
  },
});

success("Issue Lifecycle Comment completed successfully (placeholder mode)");

// Exit successfully
process.exit(0);
