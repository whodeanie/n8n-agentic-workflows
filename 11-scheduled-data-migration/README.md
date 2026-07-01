# Scheduled Data Migration With Verification

## Pattern

Nightly migration with source checksum, transform validation, batched writes, destination checksum, rollback branch, and alerting.

## Flow

Schedule -> Read Source -> Source Checksum -> Transform Rows -> Validate Schema -> Batch Writes -> Read Destination -> Destination Checksum -> Compare -> Success or Rollback.

## Useful For

Back-office sync jobs, CRM migrations, reporting warehouse updates, and API-to-API movement where silent drift is unacceptable.

## Setup Notes

Reconnect source API, destination API, Slack, and OpenAI credentials. Replace example transform rules with your destination schema and rollback API.

## Validation Focus

The workflow does not trust a successful write alone. It verifies the destination after the write and pages on mismatch.
