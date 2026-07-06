# Subscription Savings Agent

## Pattern

Recurring transaction scan, subscription clustering, usage and price review, savings recommendations, cancellation checklist, and audit.

## Flow

Subscription Review Schedule -> Fetch Transactions -> Detect Recurring Charges -> Fetch App Usage Notes -> Savings Agent -> Confidence Gate -> Cancel Review or Keep Watchlist -> Audit -> Summary.

## Useful For

Personal finance cleanup, family budgeting, small creator expenses, SaaS sprawl, forgotten trials, and monthly money reviews.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, and banking/export credentials. Replace the transaction source, usage notes sheet, review channel, and audit sheet before running with real financial data.

## Validation Focus

The workflow makes recommendations, not financial decisions. Low-confidence matches and any cancellation action go to review, with evidence preserved.
