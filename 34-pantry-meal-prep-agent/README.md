# Pantry Meal Prep Agent

## Pattern

Pantry inventory intake, preference matching, recipe planning, grocery-list generation, substitution handling, and weekly prep summary.

## Flow

Meal Plan Webhook -> Normalize Preferences -> Fetch Pantry Items -> Fetch Recipe Candidates -> Meal Prep Agent -> Budget Gate -> Grocery List or Substitution Review -> Audit -> Respond.

## Useful For

Meal prep, family grocery planning, macro tracking, reducing food waste, allergy-aware cooking, and anyone trying to stop ordering takeout by Wednesday.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, and recipe or grocery API credentials. Replace the pantry sheet, recipe endpoint, review channel, and grocery-list destination with your own tools.

## Validation Focus

The workflow keeps dietary constraints and allergies explicit, flags low-confidence substitutions for review, and writes a reusable weekly plan instead of producing a one-off chat answer.
