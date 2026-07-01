# n8n Agentic + Business Workflows

Importable n8n workflow exports that show AI automation patterns in practical business systems: lead routing, support escalation, reconciliation, competitive monitoring, idempotent webhooks, eval gates, structured extraction, RAG, model fallbacks, and tool-using agents.

Built by Kerry Dean Jr. as a portfolio-grade workflow library, not a sales bundle. Every workflow is checked into GitHub as JSON, documented, and validated in CI.

## What This Proves

- Designing n8n workflows with clear triggers, routing, audit points, and failure paths.
- Using AI where it has a real job: extraction, scoring, classification, grounded answers, evals, and tool planning.
- Keeping automation safer with idempotency, human escalation, schema checks, retries, fallback providers, and quality gates.
- Building repo-level validation so workflow exports are not just screenshots or claims.

## Workflow Catalog

| # | Workflow | What it demonstrates |
|---|---|---|
| 01 | RAG Retrieval With Citations | Webhook Q&A with embedding search and cited answers. |
| 02 | Self-Correcting Agent | Generate, judge, retry, and terminate with an attempt cap. |
| 03 | Structured Extraction With Retry | Schema extraction with validation feedback loops. |
| 04 | LLM Router | Cheap intent classification before specialized handlers. |
| 05 | Fallback Model On Error | Provider fallback path for more resilient LLM calls. |
| 06 | Evaluation Gate Before Publish | Drafting plus deterministic scoring before content is released. |
| 07 | Lead Enrichment Pipeline | Parallel enrichment, provenance, CRM upsert, and tier routing. |
| 08 | Customer Support Agent With Human Escalation | RAG answer path with urgency and confidence gates. |
| 09 | Idempotent Webhook Gateway | HMAC verification, duplicate detection, and protected workflow execution. |
| 10 | Financial Reconciliation Agent | Transaction categorization, anomaly rules, ledger logging, and monthly reports. |
| 11 | Scheduled Data Migration With Verification | Nightly migration, checksum verification, rollback, and alerting. |
| 12 | Real Time Competitive Monitoring | Scheduled ingestion and weekly insight digest. |
| 13 | LLM Evaluation Harness | Prompt test cases, judge scoring, and pass-rate reporting. |
| 14 | Content Moderation Pipeline | Fast moderation filter, deeper classifier, audit logging, and escalation. |
| 15 | Multi Modal Document Understanding | OCR-style extraction, schema selection, validation, and routing. |
| 16 | Multi Step Research Agent With Self Correction | Query decomposition, parallel retrieval, judging, and refinement. |
| 17 | Tool Using Agent With Function Calling | Planner loop, tool router, durable transcript, and step cap. |
| 18 | Code Review Assistant For Non Engineers | PR diff review, severity bucketing, and human-readable Slack summary. |
| 19 | Multi Agent Intake Triage Council | Specialist routing, independent policy review, auto-reply gate, and audit trail. |
| 20 | Long Running Agent Task Supervisor | Step planning, per-step validation, repair loop, checkpoints, and escalation. |
| 21 | Memory Backed Account Copilot | Native AI Agent with model, memory, tool, parser, confidence gate, and audit log. |
| 22 | Incident Runbook Agent | Alert classification, runbook retrieval, safety review, owner routing, and audit. |
| 23 | Human Approval Tool Agent | Tool intent planning, risk scoring, approval routing, safe execution, and audit. |
| 24 | Agent Eval Regression Runner | Scheduled eval cases, independent judging, pass-rate gate, and regression alerts. |

The generated machine-readable catalog lives at `catalog/workflows.json`.

## Quick Start

1. Clone the repo.
2. Open n8n.
3. Import any `workflow.json` file from a numbered workflow folder.
4. Reconnect credentials inside n8n. Placeholder credentials are intentional.
5. Read the workflow canvas notes and the folder README before running against live data.

## Validation

Run the full local check:

```bash
npm install
npm run validate
```

The validation suite checks:

- JSON parses cleanly.
- Required n8n fields exist.
- Each workflow has at least 6 nodes and 2 sticky-note setup guides.
- Node names are unique.
- Connections point to existing node names, matching n8n's export format.
- The TypeScript catalog generator can summarize all workflows.

Python-only check:

```bash
python3 scripts/validate_workflows.py
python3 -m pytest tests/test_workflows_valid.py -q
```

TypeScript-only check:

```bash
npm run validate:ts
```

## Notes On Claims

These exports are portfolio examples and reusable starting points. They are designed to be imported, inspected, adapted, and connected to real credentials. They are not presented as live managed services. The repo proves workflow design, validation discipline, and automation architecture.

## License

MIT. Use freely and modify for your own systems.
