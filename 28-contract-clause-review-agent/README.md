# Contract Clause Review Agent

## Pattern

Contract intake, clause extraction, policy comparison, risk scoring, legal routing, and audit logging.

## Flow

Contract Intake Webhook -> Normalize Intake -> Fetch Clause Policy -> Extract Clauses -> Validate Extraction -> Risk Gate -> Legal Review or Standard Response -> Audit -> Respond.

## Useful For

Procurement teams, sales operations, vendor onboarding, MSAs, DPAs, order forms, and any workflow where non-lawyers need a safe first pass before legal review.

## Setup Notes

Reconnect OpenAI, Slack, Google Sheets, and policy-source credentials. Replace the contract-policy endpoint, legal-review channel, and audit sheet before importing into a real workspace.

## Validation Focus

The workflow does not approve legal terms by itself. It extracts and scores clauses, then sends anything high-risk, missing, or ambiguous to legal with the extracted evidence and reason.
