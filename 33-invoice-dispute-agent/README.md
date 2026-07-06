# Invoice Dispute Agent

## Pattern

Invoice intake, purchase-order matching, discrepancy classification, dispute packet generation, approval routing, vendor response draft, and audit.

## Flow

Invoice Webhook -> Normalize Invoice -> Fetch PO Record -> Fetch Receipt Evidence -> Merge Evidence -> Dispute Agent -> Dispute Gate -> AP Approval or Payment Queue -> Vendor Draft -> Audit -> Respond.

## Useful For

Accounts payable, procurement operations, vendor management, finance shared services, and teams that need explainable invoice exception handling.

## Setup Notes

Reconnect OpenAI, Slack, Gmail, Google Sheets, and finance-system credentials. Replace the PO lookup endpoint, receipt endpoint, AP channel, vendor email workflow, and audit sheet IDs.

## Validation Focus

The workflow does not pay or reject invoices blindly. It creates an evidence packet, routes meaningful discrepancies to AP, and drafts vendor-facing language for review.
