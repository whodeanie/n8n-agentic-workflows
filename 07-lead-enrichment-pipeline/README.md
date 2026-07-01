# Lead Enrichment Pipeline

## Pattern

Parallel enrichment fan-out, provenance capture, scoring, CRM upsert, and tier-based routing.

## Flow

Form Submit -> LinkedIn Lookup / Company Enrich / Intent Score -> Combine Enrichments -> Score Lead -> Normalize Record -> Upsert HubSpot -> Route by Tier.

## Useful For

Sales operations teams that need faster lead qualification while still preserving why a lead was scored hot, warm, or cold.

## Setup Notes

Reconnect HubSpot, Google Sheets, Slack, Gmail, enrichment API, and OpenAI credentials. Replace sample enrichment endpoints with approved vendors or internal data sources.

## Validation Focus

The provenance object travels with the record so scoring decisions can be audited after routing.
