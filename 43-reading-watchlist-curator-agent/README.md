# Reading Watchlist Curator Agent

## Pattern

Saved-link intake, preference matching, duplicate detection, reading queue prioritization, summary drafting, and audit.

## Flow

Reading Queue Schedule -> Fetch Saved Links -> Fetch Preference Notes -> Reading Curator Agent -> Priority Gate -> Weekend Queue or Archive Suggestions -> Audit -> Summary.

## Useful For

Readers, newsletter collectors, research rabbit holes, movie/show watchlists, learning queues, and anyone whose saved links became a junk drawer.

## Setup Notes

Reconnect OpenAI, Google Sheets, Slack, and bookmark/RSS credentials. Replace the saved-links sheet, preference sheet, review channel, and queue destination.

## Validation Focus

The workflow ranks items with reasons, detects duplicates and stale links, and preserves why each item should be read, watched, archived, or skipped.
