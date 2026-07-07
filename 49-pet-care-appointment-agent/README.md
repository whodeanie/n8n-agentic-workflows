# Pet Care Appointment Agent

## Pattern

Pet profile lookup, medication and appointment history, symptom intake, care reminder generation, vet-review routing, and audit.

## Flow

Pet Care Webhook -> Normalize Pet Check -> Fetch Pet Profile -> Fetch Care History -> Pet Care Agent -> Vet Gate -> Vet Review or Save Care Reminders -> Audit -> Respond.

## Useful For

Pet owners, family pet schedules, medication reminders, grooming cycles, vaccine tracking, boarding prep, and keeping small health changes from getting lost.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, and calendar credentials. Replace the pet profile sheet, care history sheet, review channel, reminder destination, and audit sheet.

## Validation Focus

The workflow does not diagnose pets. Concerning symptoms route to vet review, while routine reminders are saved with dates, evidence, and owner notes.
