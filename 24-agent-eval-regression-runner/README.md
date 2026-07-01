# Agent Eval Regression Runner

## Pattern

Scheduled eval cases, candidate agent execution, judge pass, threshold gate, regression alert, and cataloged results.

## Flow

Nightly Schedule -> Fetch Eval Cases -> Run Candidate Agent -> Judge Output -> Aggregate Scores -> Release Gate -> Notify Regression or Record Pass.

## Useful For

RAG assistants, support agents, routing agents, document extractors, and any LLM workflow that needs a repeatable release gate before prompt or model changes ship.

## Setup Notes

Reconnect OpenAI, Slack, HTTP, and Sheets credentials. Replace the eval-case endpoint and candidate-agent webhook URL with your own test harness.

## Validation Focus

The judge is separate from the candidate agent, and the release gate is deterministic: fail when pass rate drops below the threshold.
