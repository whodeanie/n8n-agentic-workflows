# Memory Backed Account Copilot

## Pattern

n8n AI Agent node with OpenAI chat model, memory, calculator tool, structured parser, confidence gate, CRM-safe response, and audit logging.

## Flow

Account Webhook -> Normalize Message -> AI Agent With Memory + Tool + Parser -> Confidence Gate -> Customer Reply or Human Review -> Audit Log.

## Useful For

Account-management copilots, customer-success assistants, renewal prep, and internal support bots that need short-term conversation memory.

## Setup Notes

Reconnect OpenAI, Slack, and Sheets credentials. Replace the system prompt with your approved account policy and use a stable account ID as the memory key.

## Validation Focus

The agent uses structured output and a confidence gate. Memory helps continuity but does not bypass review for low-confidence or high-risk responses.
