# Self-Correcting Agent

## Pattern

Generate, evaluate, retry, and stop. The workflow creates an output, asks a separate judge pass to score it, then loops with feedback until it passes or reaches the attempt cap.

## Flow

Webhook In -> Set Initial State -> Generate Output -> Quality Check -> Check Quality Gate -> Pass Branch or Retry Branch.

## Useful For

Structured outputs where quality can be scored: summaries with required sections, JSON responses, decision memos, checklists, and generated drafts that need a minimum rubric score.

## Setup Notes

Reconnect the LLM credential, tune the judge rubric, and keep the attempt cap low. The retry loop is valuable only when failures are measurable.

## Validation Focus

The workflow carries attempt state through the loop so it terminates predictably instead of trusting the model to stop itself.
