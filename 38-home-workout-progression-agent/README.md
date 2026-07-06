# Home Workout Progression Agent

## Pattern

Workout history intake, equipment-aware programming, progression planning, recovery check, review routing, and training-log audit.

## Flow

Workout Plan Webhook -> Normalize Training Goal -> Fetch Workout History -> Fetch Equipment List -> Workout Progression Agent -> Recovery Gate -> Coach Review or Save Plan -> Audit -> Respond.

## Useful For

Home gyms, busy parents, former athletes, beginners, strength blocks, conditioning plans, and anyone trying to train consistently without guessing every session.

## Setup Notes

Reconnect OpenAI, Google Sheets, and Slack credentials. Replace the workout-history sheet, equipment sheet, review channel, and training-log sheet before live use.

## Validation Focus

The workflow treats injury and recovery flags as hard review triggers, keeps progression conservative, and stores a reusable plan instead of giving a one-off chat answer.
