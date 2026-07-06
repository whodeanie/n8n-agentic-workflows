# Renewal Risk Agent

## Pattern

Account renewal ingestion, usage and ticket signal merge, risk scoring, success-plan generation, owner routing, and audit.

## Flow

Renewal Schedule -> Fetch Renewal Accounts -> Fetch Usage Signals -> Fetch Support Signals -> Merge Account Context -> Renewal Risk Agent -> Risk Gate -> CSM Task or Leadership Alert -> Audit -> Summary.

## Useful For

Customer success, SaaS renewal operations, account management, revenue retention, and teams that need early churn-risk signals with practical next actions.

## Setup Notes

Reconnect OpenAI, HubSpot or Salesforce, Slack, Google Sheets, and usage/support data credentials. Replace the renewal query, usage endpoint, support endpoint, alert channel, and audit sheet IDs.

## Validation Focus

The workflow separates evidence, risk score, and recommended action. High-value or high-risk accounts route to leadership; lower-risk accounts get owner tasks with cited usage/support signals.
