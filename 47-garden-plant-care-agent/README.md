# Garden Plant Care Agent

## Pattern

Plant inventory lookup, local weather and watering signals, care-plan generation, pest/disease review routing, and audit.

## Flow

Plant Care Schedule -> Fetch Plant Inventory -> Fetch Local Weather -> Fetch Care History -> Plant Care Agent -> Risk Gate -> Plant Review or Save Care Tasks -> Audit.

## Useful For

Houseplants, balcony gardens, vegetable gardens, landscaping chores, seed-starting, and people trying to keep one more basil plant alive.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, and weather credentials. Replace the plant inventory sheet, care history sheet, plant review channel, and audit sheet.

## Validation Focus

The workflow distinguishes routine care from pest/disease risk, adjusts watering for weather, and preserves care history for future recommendations.
