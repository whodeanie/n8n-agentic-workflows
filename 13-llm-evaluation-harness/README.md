# LLM Evaluation Harness

## Pattern

Prompt test cases in a spreadsheet, candidate model run, judge model run, structured logging, aggregate report.

## Flow

Manual Trigger -> Read Test Cases -> Split In Batches -> Run Candidate -> Judge Assertions -> Log Result -> Aggregate -> Email Report.

## Useful For

Teams changing prompts, adding examples, or swapping models who need a lightweight regression check before shipping.

## Setup Notes

Reconnect Google Sheets, Gmail, and OpenAI credentials. Store expected assertions as concrete checks instead of vague preferences.

## Validation Focus

Every run logs inputs, raw outputs, judge scores, and pass rate, so prompt changes can be compared instead of guessed at.
