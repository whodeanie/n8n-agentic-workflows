# Knowledge Base Freshness Agent

## Pattern

Support-search gap analysis, article freshness scoring, update recommendation, owner routing, and publishing audit.

## Flow

Freshness Schedule -> Fetch Search Gaps -> Fetch KB Articles -> Merge Signals -> Freshness Agent -> Review Gate -> Docs Ticket or Low-Risk Update Queue -> Audit -> Summary.

## Useful For

Support operations, internal enablement, customer help centers, product documentation, and teams that need content maintenance driven by real ticket/search signals.

## Setup Notes

Reconnect OpenAI, Slack, Google Sheets, and documentation-system credentials. Replace the search-gap endpoint, article export endpoint, docs channel, and audit sheet with your own systems.

## Validation Focus

The workflow makes stale-content recommendations from evidence rather than guesses. Anything with product-risk, pricing-risk, or low confidence goes to a human owner before publishing.
