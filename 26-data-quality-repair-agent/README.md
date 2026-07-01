# Data Quality Repair Agent

## Pattern

Scheduled anomaly ingestion, field-level diagnosis, repair proposal, confidence gate, safe patch execution, quarantine, and audit.

## Flow

Data Quality Schedule -> Fetch Anomalies -> Expand Records -> Repair Agent -> Confidence Gate -> Patch Clean Records or Quarantine -> Audit Log -> Summary.

## Useful For

CRM hygiene, product catalog cleanup, billing data QA, warehouse sync checks, and operations teams that need repair suggestions without letting an agent silently mutate questionable records.

## Setup Notes

Reconnect OpenAI, Slack, Google Sheets, and the record-system API. Replace the anomaly endpoint, patch endpoint, quarantine channel, and audit sheet with your own systems.

## Validation Focus

Repairs only apply when the agent returns a high-confidence, schema-valid patch. Low-confidence records go to quarantine with the original value, proposed patch, and reason preserved for review.
