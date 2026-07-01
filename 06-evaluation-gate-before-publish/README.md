# Evaluation Gate Before Publish

## Pattern

Draft, score, gate, then publish. The workflow generates content, scores it against a rubric, and only calls the publish endpoint when the score clears the threshold.

## Flow

Webhook In -> Draft Content -> Eval Scorer -> Parse Eval JSON -> Quality Gate -> Publish Content or Reject.

## Useful For

Content operations, outbound email drafts, knowledge-base updates, social posts, and any workflow where model output should be checked before release.

## Setup Notes

Reconnect the LLM credential and replace the publish endpoint with your CMS, queue, or review system. Calibrate the score threshold against real examples.

## Validation Focus

The publish step is isolated behind a gate, so low-quality output can be logged and improved without being sent live.
