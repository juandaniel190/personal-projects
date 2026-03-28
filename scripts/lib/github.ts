/**
 * Shared utilities for GitHub Actions scripts.
 *
 * These utilities provide environment validation and structured logging
 * for GitHub Actions workflow scripts.
 */

/**
 * Safely retrieves a required environment variable.
 * Throws an error if the variable is not set.
 */
export function getEnv(key: string): string {
  const value = process.env[key];
  if (!value) {
    throw new Error(`Missing required environment variable: ${key}`);
  }
  return value;
}

/**
 * Safely retrieves an optional environment variable with a default value.
 */
export function getEnvOrDefault(key: string, defaultValue: string): string {
  return process.env[key] || defaultValue;
}

/**
 * Validates that all required environment variables are present.
 * Returns an object with the validated values.
 */
export function validateEnv(required: string[]): Record<string, string> {
  const env: Record<string, string> = {};
  const missing: string[] = [];

  for (const key of required) {
    const value = process.env[key];
    if (!value) {
      missing.push(key);
    } else {
      env[key] = value;
    }
  }

  if (missing.length > 0) {
    console.error(`❌ Missing required environment variables: ${missing.join(", ")}`);
    process.exit(1);
  }

  return env;
}

/**
 * Structured logging for GitHub Actions.
 * Outputs JSON-formatted logs with timestamp and script name.
 */
export function log(script: string, data: Record<string, any>): void {
  const logEntry = {
    script,
    timestamp: new Date().toISOString(),
    ...data,
  };
  console.log(JSON.stringify(logEntry, null, 2));
}

/**
 * Simple console logging with a prefix for better readability.
 */
export function info(message: string): void {
  console.log(`ℹ️  ${message}`);
}

/**
 * Success message logging.
 */
export function success(message: string): void {
  console.log(`✅ ${message}`);
}

/**
 * Error message logging.
 */
export function error(message: string): void {
  console.error(`❌ ${message}`);
}
