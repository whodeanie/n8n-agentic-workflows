# n8n Business Workflow Library Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expand and validate the n8n workflow library as a portfolio-grade automation repo.

**Architecture:** Numbered workflow folders hold importable `workflow.json` files plus concise READMEs. A TypeScript validator generates a catalog and a Python validator backs CI compatibility.

**Tech Stack:** n8n JSON exports, TypeScript, Node.js, Python, pytest, GitHub Actions.

---

### Task 1: Curate Workflow Folders

**Files:**
- Create: `07-lead-enrichment-pipeline/workflow.json`
- Create: `08-support-agent-human-escalation/workflow.json`
- Create: `09-idempotent-webhook-gateway/workflow.json`
- Create: `10-financial-reconciliation-agent/workflow.json`
- Create: `11-scheduled-data-migration/workflow.json`
- Create: `12-competitive-monitoring/workflow.json`
- Create: `13-llm-evaluation-harness/workflow.json`
- Create: `14-content-moderation-pipeline/workflow.json`
- Create: `15-multimodal-doc-understanding/workflow.json`
- Create: `16-multi-step-research-agent/workflow.json`
- Create: `17-tool-using-agent/workflow.json`
- Create: `18-code-review-assistant/workflow.json`

- [x] Copy the strongest local workflow exports into numbered folders.
- [x] Add a second sticky-note implementation guide to workflows that only had one canvas note.

### Task 2: Rewrite Documentation

**Files:**
- Modify: `README.md`
- Create/modify: `[0-9][0-9]-*/README.md`

- [x] Reframe the repo as a validated engineering portfolio library.
- [x] Replace hype language with pattern, flow, setup notes, and validation focus.
- [x] State that workflows are reusable/importable examples, not live managed services.

### Task 3: Add TypeScript Validation

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Create: `scripts/validate-workflows.ts`
- Create: `catalog/workflows.json`

- [x] Discover numbered workflow folders.
- [x] Parse workflow JSON.
- [x] Validate required fields, node count, sticky notes, duplicate node names, and connection targets.
- [x] Generate `catalog/workflows.json`.

### Task 4: Fix Python Validation

**Files:**
- Modify: `scripts/validate_workflows.py`
- Modify: `tests/test_workflows_valid.py`

- [x] Update connection validation to use node names instead of node IDs.
- [x] Expand tests for unique names and sticky-note coverage.

### Task 5: Verify And Publish

**Files:**
- Modify: `.github/workflows/ci.yml`

- [ ] Install npm dependencies.
- [ ] Run `npm run validate`.
- [ ] Update CI to run TypeScript and Python checks.
- [ ] Commit with a professional message that does not use starter/scaffold language.
- [ ] Push to GitHub.
