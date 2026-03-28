#!/usr/bin/env bun

/**
 * Auto-Close Duplicates - Minimal Placeholder Implementation
 *
 * This script is a placeholder that prevents GitHub Actions workflow failures.
 * It exists because this is a personal portfolio repository that doesn't actively
 * use GitHub issues, so automated duplicate detection/closure is not needed.
 *
 * Purpose:
 * - Validates required environment variables
 * - Logs execution status
 * - Exits successfully to prevent workflow errors
 *
 * If this repository grows to need real issue management, refer to:
 * https://github.com/anthropics/claude-code/tree/main/scripts
 *
 * Triggered by: .github/workflows/auto-close-duplicates.yml (scheduled: daily at 9am UTC)
 */

import { validateEnv, getEnvOrDefault, log, info, success } from "./lib/github";

// Validate required environment variables
const env = validateEnv([
  "GITHUB_TOKEN",
  "GITHUB_REPOSITORY_OWNER",
  "GITHUB_REPOSITORY_NAME",
]);

// Optional: STATSIG_API_KEY (for analytics, not required for placeholder)
const statsigKey = getEnvOrDefault("STATSIG_API_KEY", "not-configured");

// Log execution details
info("Auto-Close Duplicates script started");

log("auto-close-duplicates.ts", {
  status: "placeholder",
  mode: "no-op",
  message: "This is a minimal placeholder implementation",
  reason: "Personal portfolio repository with zero issues - duplicate detection not needed",
  repository: `${env.GITHUB_REPOSITORY_OWNER}/${env.GITHUB_REPOSITORY_NAME}`,
  environment: {
    hasToken: !!env.GITHUB_TOKEN,
    hasStatsigKey: statsigKey !== "not-configured",
    owner: env.GITHUB_REPOSITORY_OWNER,
    repo: env.GITHUB_REPOSITORY_NAME,
  },
});

success("Auto-Close Duplicates completed successfully (placeholder mode)");

// Exit successfully
process.exit(0);
