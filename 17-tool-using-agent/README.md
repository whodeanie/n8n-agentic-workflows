# Tool Using Agent With Function Calling

## Pattern

Planner loop with explicit tool selection, tool execution, transcript update, step cap, final composition, and audit logging.

## Flow

Goal Webhook -> Stamp Idempotency -> Initialize State -> Planner -> Finish Gate -> Tool Switch -> Execute Tool -> Advance Transcript -> Loop or Respond.

## Useful For

Operations copilots, internal lookup tools, account research assistants, and constrained agents that should call known tools instead of improvising.

## Setup Notes

Reconnect OpenAI, Sheets, and HTTP credentials. Replace the sample tools with a short allowlist of business-approved APIs.

## Validation Focus

The step cap is enforced by workflow logic, not by a model promise.
