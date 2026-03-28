#!/usr/bin/env bun

/**
 * Issue Sweep - Minimal Placeholder Implementation
 *
 * This script is a placeholder that prevents GitHub Actions workflow failures.
 * It exists because this is a personal portfolio repository that doesn't actively
 * use GitHub issues, so full issue lifecycle management is not needed.
 *
 * Purpose:
 * - Validates required environment variables
 * - Logs execution status
 * - Exits successfully to prevent workflow errors
 *
 * If this repository grows to need real issue management, refer to:
 * https://github.com/anthropics/claude-code/tree/main/scripts
 *
 * Triggered by: .github/workflows/sweep.yml (scheduled: twice daily at 10am, 10pm UTC)
 */

import { validateEnv, log, info, success } from "./lib/github";

// Validate required environment variables
const env = validateEnv([
  "GITHUB_TOKEN",
  "GITHUB_REPOSITORY_OWNER",
  "GITHUB_REPOSITORY_NAME",
]);

// Log execution details
info("Issue Sweep script started");

log("sweep.ts", {
  status: "placeholder",
  mode: "no-op",
  message: "This is a minimal placeholder implementation",
  reason: "Personal portfolio repository with zero issues - full lifecycle management not needed",
  repository: `${env.GITHUB_REPOSITORY_OWNER}/${env.GITHUB_REPOSITORY_NAME}`,
  environment: {
    hasToken: !!env.GITHUB_TOKEN,
    owner: env.GITHUB_REPOSITORY_OWNER,
    repo: env.GITHUB_REPOSITORY_NAME,
  },
});

success("Issue Sweep completed successfully (placeholder mode)");

// Exit successfully
process.exit(0);
