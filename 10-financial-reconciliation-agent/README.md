# Financial Reconciliation Agent

## Pattern

Webhook transaction intake, AI-assisted categorization, deterministic anomaly rules, ledger logging, and scheduled summary reporting.

## Flow

Bank Export Webhook -> Parse Transactions -> Categorize -> Detect Anomaly -> Append Ledger -> Alert Review Queue -> Monthly Report.

## Useful For

Small finance teams, operators, and founders who need a reviewable first pass over transactions without giving the model control over final accounting.

## Setup Notes

Reconnect Google Sheets, Slack, Gmail, and OpenAI credentials. Replace anomaly thresholds and categories with your actual accounting policy.

## Validation Focus

The model labels transactions, while deterministic checks flag risk. That split keeps human review focused and auditable.
