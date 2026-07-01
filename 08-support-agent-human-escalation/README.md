# Customer Support Agent With Human Escalation

## Pattern

Tier-1 answer automation with urgency, confidence, and human-review gates.

## Flow

Ticket Webhook -> Classify Intent -> Urgency Switch -> Retrieval / Draft Answer -> Confidence Gate -> Auto Reply or Human Queue.

## Useful For

Support teams that want automation for routine questions without hiding risky, angry, or low-confidence tickets from humans.

## Setup Notes

Reconnect Airtable, Gmail, Slack, OpenAI, and any knowledge-base search endpoint. Tune the confidence threshold with real support tickets before enabling auto replies.

## Validation Focus

Escalation is a first-class path. The workflow demonstrates when not to automate, which is often the more important production decision.
