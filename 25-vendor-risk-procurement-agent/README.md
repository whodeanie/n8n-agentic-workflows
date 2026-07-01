# Vendor Risk Procurement Agent

## Pattern

Procurement intake, vendor policy review, budget check, risk scoring, approval routing, and audit logging.

## Flow

Procurement Request Webhook -> Normalize Request -> Vendor Risk Agent -> Budget Lookup -> Approval Gate -> Approval Queue or Auto Approve -> Audit Log -> Respond.

## Useful For

Vendor onboarding, software spend review, compliance intake, procurement operations, and internal tool requests that need a consistent approval path.

## Setup Notes

Reconnect OpenAI, Slack, Google Sheets, and procurement-system credentials. Replace the policy URL, vendor database endpoint, approval channel, and audit sheet IDs with your own systems.

## Validation Focus

The workflow separates agent reasoning from approval authority. High-risk vendors, high spend, missing security docs, and unknown budget owners route to a human before any purchasing action is marked approved.
