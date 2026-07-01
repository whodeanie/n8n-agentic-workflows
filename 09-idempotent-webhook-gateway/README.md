# Idempotent Webhook Gateway

## Pattern

Signed webhook gateway in front of a protected workflow. It verifies HMAC, computes an idempotency key, drops duplicates, and forwards only new valid payloads.

## Flow

Public Webhook -> Verify HMAC -> Signature Gate -> Compute Key -> Check Seen Keys -> Record Key -> Execute Inner Workflow -> Respond.

## Useful For

Payment webhooks, form submissions, CRM callbacks, partner APIs, and any integration where duplicate delivery can create real operational damage.

## Setup Notes

Reconnect Google Sheets or replace it with Postgres/Redis for the seen-key store. Set the shared secret and inner workflow ID before exposing the webhook.

## Validation Focus

The sensitive side effect is behind duplicate and signature gates, so replay and double-submit behavior is controlled.
