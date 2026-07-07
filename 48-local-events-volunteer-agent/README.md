# Local Events Volunteer Agent

## Pattern

Interest intake, local event and volunteer opportunity lookup, schedule fit scoring, shortlist generation, reminder draft, and audit.

## Flow

Opportunity Schedule -> Fetch Interests -> Fetch Local Events -> Fetch Volunteer Opportunities -> Opportunity Agent -> Fit Gate -> Weekend Shortlist or Review Queue -> Audit.

## Useful For

Finding local events, volunteering, community networking, low-pressure social plans, family activities, and getting out of the house without doom-scrolling listings.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, calendar, event, and volunteer-opportunity credentials. Replace the interests sheet, event APIs, review channel, and audit sheet.

## Validation Focus

The workflow ranks opportunities by schedule fit, budget, distance, interest match, and accessibility notes, then preserves why each item made the shortlist.
