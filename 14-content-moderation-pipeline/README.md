# Content Moderation Pipeline

## Pattern

Two-stage moderation with cheap fast filtering, deeper policy classification, decision routing, audit logging, and human review alerts.

## Flow

Content Webhook -> Fast Moderation API -> Flag Gate -> Policy Classifier -> Decision Switch -> Allow / Review / Block.

## Useful For

Communities, marketplaces, education tools, and submission systems that need reviewable moderation decisions.

## Setup Notes

Reconnect Airtable, Slack, OpenAI, and moderation API credentials. Replace policy categories with the rules your product actually enforces.

## Validation Focus

The workflow stores the decision and rationale, which supports appeals, QA, and policy iteration.
