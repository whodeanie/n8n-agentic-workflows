# Multi Agent Intake Triage Council

## Pattern

Webhook intake, shared normalization, intent classification, specialist agent selection, independent policy review, and a final action gate.

## Flow

Intake Webhook -> Normalize Request -> Classify Work -> Route Specialist -> Specialist Draft -> Policy Review -> Decision Gate -> Auto Reply or Human Queue -> Audit Log.

## Useful For

Support operations, internal service desks, customer-success queues, and shared inboxes where different specialist prompts should handle different work types.

## Setup Notes

Reconnect OpenAI, Slack, and Sheets credentials. Replace the specialist prompts with your team-approved operating policy before turning on auto-response.

## Validation Focus

The specialist output is not trusted directly. A separate policy reviewer decides whether the answer can be sent or must be escalated.
