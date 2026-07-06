# Access Review Agent

## Pattern

Scheduled identity review, entitlement normalization, policy comparison, risky-access scoring, manager approval routing, and audit.

## Flow

Access Review Schedule -> Fetch Users -> Fetch Entitlements -> Normalize Access -> Access Review Agent -> Risk Gate -> Manager Approval or Auto Attest -> Audit -> Summary.

## Useful For

Security operations, SOC2 evidence, offboarding reviews, quarterly access certifications, finance system access, and SaaS admin governance.

## Setup Notes

Reconnect OpenAI, Slack, Google Sheets, and identity-provider credentials. Replace the user endpoint, entitlement endpoint, manager channel, and audit sheet IDs before running against live access data.

## Validation Focus

The workflow does not remove access automatically. It identifies risky entitlements, routes exceptions to managers/security, and writes review evidence for audit.
