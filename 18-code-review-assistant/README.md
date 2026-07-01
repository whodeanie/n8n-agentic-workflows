# Code Review Assistant For Non Engineers

## Pattern

Webhook PR intake, diff fetch, structured review, severity bucketing, friendly translation, Slack alert, and response payload.

## Flow

GitHub Webhook -> Filter Event -> Fetch Diff -> Review Findings -> Bucket Severity -> Translate Summary -> Slack Post -> Respond.

## Useful For

Product managers, founders, QA leads, and engineering teams that want non-engineers to understand the risk in a pull request without reading the raw diff.

## Setup Notes

Reconnect GitHub, Slack, and OpenAI credentials. Keep this as advisory output unless your team has calibrated the findings against real reviews.

## Validation Focus

The workflow separates structured findings from human-readable summary so the same review can power both dashboards and Slack updates.
