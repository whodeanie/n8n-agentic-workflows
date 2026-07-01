# Multi Modal Document Understanding

## Pattern

File intake, OCR or vision extraction, document-type routing, schema extraction, validation, retry hints, and destination-specific storage.

## Flow

Document Webhook -> Download File -> Vision/OCR Extract -> Detect Type -> Extract Schema -> Validate Fields -> Route by Type.

## Useful For

Invoices, receipts, forms, intake packets, and operational documents where the workflow needs a typed record instead of a free-text summary.

## Setup Notes

Reconnect file download, Airtable, and OpenAI credentials. Replace example schemas with the fields needed by your downstream system.

## Validation Focus

The retry loop passes missing-field hints back to extraction, avoiding a blind second attempt.
