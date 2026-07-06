# Travel Packing Weather Agent

## Pattern

Trip preference intake, itinerary and forecast lookup, packing checklist generation, document reminder, weather-risk backup planning, and audit.

## Flow

Packing Webhook -> Normalize Trip -> Fetch Forecast -> Fetch Itinerary -> Packing Agent -> Risk Gate -> Travel Review or Save Checklist -> Audit -> Respond.

## Useful For

Weekend trips, work travel, family vacations, tournaments, conferences, festivals, and anyone who remembers the charger at the airport.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, and weather or travel API credentials. Replace the forecast endpoint, itinerary source, review channel, and checklist sheet before live use.

## Validation Focus

The workflow separates essentials, weather-dependent items, documents, and optional comfort items, and routes severe-weather or missing-document risk to review.
