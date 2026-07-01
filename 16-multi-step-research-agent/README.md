# Multi Step Research Agent With Self Correction

## Pattern

Question decomposition, parallel source lookup, synthesis, independent judging, bounded refinement, and cited final composition.

## Flow

Research Webhook -> Decompose Query -> Fetch Sources -> Merge Evidence -> Synthesize -> Judge -> Refine or Accept -> Compose Final.

## Useful For

Research assistants, analyst briefs, diligence notes, content planning, and search workflows where citations and decomposition matter.

## Setup Notes

Reconnect search, OpenAI, and any storage credentials. Replace sample source APIs with approved sources for your domain.

## Validation Focus

The judge is separate from the synthesizer, and the attempt cap keeps refinement bounded.
