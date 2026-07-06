# Home Maintenance Seasonal Agent

## Pattern

Home profile intake, seasonal checklist generation, weather and warranty lookup, task prioritization, reminder routing, and audit.

## Flow

Maintenance Schedule -> Fetch Home Profile -> Fetch Seasonal Weather -> Fetch Warranty Notes -> Maintenance Agent -> Urgency Gate -> Reminder or Contractor Review -> Audit -> Summary.

## Useful For

Homeowners, renters, property managers, seasonal chores, appliance upkeep, filter changes, and avoiding expensive repairs because small tasks got forgotten.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, and weather credentials. Replace the home profile sheet, warranty sheet, reminder channel, and maintenance audit sheet before live use.

## Validation Focus

The workflow separates DIY reminders from contractor-review tasks, flags safety risks, and stores the seasonal checklist so future runs do not start from scratch.
