# Creator Content Remix Agent

## Pattern

Long-form content intake, platform-specific remixing, caption generation, brand-safety check, posting queue, and performance audit.

## Flow

Content Remix Webhook -> Normalize Source -> Fetch Brand Voice -> Remix Agent -> Safety Gate -> Review Queue or Schedule Drafts -> Audit -> Respond.

## Useful For

Creators, podcasters, YouTubers, coaches, newsletter writers, small brands, and anyone turning one strong idea into shorts, posts, carousels, and email snippets.

## Setup Notes

Reconnect OpenAI, Slack, Google Sheets, and social scheduling credentials. Replace the brand voice sheet, review channel, and scheduler endpoint before live publishing.

## Validation Focus

The workflow generates drafts, not silent posts. Brand-risk or low-confidence content goes to review, and every platform draft keeps source attribution so the remix does not invent claims.
