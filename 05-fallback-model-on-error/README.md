# Fallback Model On Error

## Pattern

Sequential provider fallback. The workflow tries a primary model, checks the response, then falls through to alternate providers when the primary path fails.

## Flow

Webhook In -> Try GPT-4 -> GPT-4 Success? -> Fallback to Claude Haiku -> Haiku Success? -> Fallback to Gemini Flash.

## Useful For

Customer-facing automation, scheduled jobs, and critical internal assistants where one provider outage should not stop the whole workflow.

## Setup Notes

Reconnect each provider credential and order the providers by your own cost, latency, and quality preferences. Log which provider handled the request.

## Validation Focus

The fallback decision is explicit, making provider reliability measurable over time.
