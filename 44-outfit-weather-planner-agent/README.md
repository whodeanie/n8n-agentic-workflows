# Outfit Weather Planner Agent

## Pattern

Calendar and weather lookup, wardrobe inventory matching, dress-code interpretation, outfit recommendation, backup option, and audit.

## Flow

Outfit Webhook -> Normalize Day Context -> Fetch Weather -> Fetch Calendar Events -> Fetch Wardrobe -> Outfit Agent -> Confidence Gate -> Review or Save Outfit -> Audit -> Respond.

## Useful For

Workdays, events, travel days, date nights, interviews, conferences, and mornings where the weather and the calendar are both doing too much.

## Setup Notes

Reconnect OpenAI, Google Calendar, Google Sheets, Slack, and weather credentials. Replace the wardrobe sheet, calendar ID, review channel, and outfit audit sheet.

## Validation Focus

The workflow keeps dress code, weather, comfort, and available clothing explicit. Low-confidence or missing wardrobe matches route to review instead of pretending the closet has everything.
