#!/usr/bin/env bun

/**
 * Backfill Duplicate Comments - Minimal Placeholder Implementation
 *
 * This script is a placeholder that prevents GitHub Actions workflow failures.
 * It exists because this is a personal portfolio repository that doesn't actively
 * use GitHub issues, so backfilling duplicate comments is not needed.
 *
 * Purpose:
 * - Validates required environment variables
 * - Reads configuration inputs (DAYS_BACK, DRY_RUN)
 * - Logs execution status
 * - Exits successfully to prevent workflow errors
 *
 * If this repository grows to need real issue management, refer to:
 * https://github.com/anthropics/claude-code/tree/main/scripts
 *
 * Triggered by: .github/workflows/backfill-duplicate-comments.yml (manual dispatch only)
 */

import { validateEnv, getEnvOrDefault, log, info, success } from "./lib/github";

// Validate required environment variables
const env = validateEnv(["GITHUB_TOKEN"]);

// Read optional configuration inputs
const daysBack = getEnvOrDefault("DAYS_BACK", "90");
const dryRun = getEnvOrDefault("DRY_RUN", "true");

// Log execution details
info("Backfill Duplicate Comments script started");

log("backfill-duplicate-comments.ts", {
  status: "placeholder",
  mode: "no-op",
  message: "This is a minimal placeholder implementation",
  reason: "Personal portfolio repository - backfilling duplicate comments not needed",
  configuration: {
    daysBack: parseInt(daysBack),
    dryRun: dryRun === "true",
    hasToken: !!env.GITHUB_TOKEN,
  },
});

success("Backfill Duplicate Comments completed successfully (placeholder mode)");

// Exit successfully
process.exit(0);
