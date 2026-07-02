# Executive Briefing Agent

## Pattern

Scheduled metric ingestion, risk synthesis, leadership brief generation, human review routing, email draft, and audit.

## Flow

Briefing Schedule -> Fetch Metrics Snapshot -> Fetch Calendar Risks -> Merge Signals -> Briefing Agent -> Validate Brief -> Review Gate -> Leadership Digest or Review Queue -> Audit.

## Useful For

Operating reviews, weekly business updates, customer-success leadership, revenue operations, delivery teams, and executives who need a concise brief sourced from real system signals.

## Setup Notes

Reconnect OpenAI, Slack, Gmail, Google Sheets, and metrics-system credentials. Replace the metric snapshot endpoint, calendar-risk endpoint, leadership channel, and audit sheet before live use.

## Validation Focus

The workflow requires the brief to cite source metrics, separate facts from recommendations, and route high-risk or low-confidence summaries to human review before broad distribution.
