# Structured Extraction With Retry

## Pattern

LLM extraction with deterministic validation. The workflow extracts fields from messy text, validates the parsed JSON, and retries with the validation error as feedback.

## Flow

Webhook In -> Initialize State -> Extract via Function Calling -> Parse JSON Response -> Validation Pass? -> Success or Retry.

## Useful For

Lead intake, invoice metadata, support-ticket classification, application forms, and email-to-record automation where missing fields should fail visibly.

## Setup Notes

Reconnect the OpenAI credential and replace the sample schema with the fields your downstream system requires. Keep required fields strict and optional fields explicit.

## Validation Focus

The Code node is the trust boundary. It decides whether output is usable before anything is written downstream.
