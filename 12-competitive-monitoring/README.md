# Real Time Competitive Monitoring

## Pattern

Scheduled source ingestion plus weekly digest generation. Raw source items are normalized first, then summarized into themes and suggested responses.

## Flow

Hourly Schedule -> Source Fetches -> Normalize -> Merge -> Store / Embed -> Weekly Schedule -> Analyze Week -> Email Digest.

## Useful For

Marketing, product, creator, and growth teams that need a repeatable way to watch market shifts without manually checking every channel.

## Setup Notes

Reconnect source APIs, Gmail, OpenAI, and storage credentials. Tune source cadence and summary prompts around the channels that matter to the business.

## Validation Focus

Ingestion and analysis are separate paths, which makes the digest rerunnable without refetching every source.
