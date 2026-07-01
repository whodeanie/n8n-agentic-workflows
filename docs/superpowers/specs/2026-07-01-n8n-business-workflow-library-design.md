# n8n Business Workflow Library Design

## Goal

Turn the existing n8n workflow repo into a credible portfolio library that shows business automation architecture through importable workflow JSON, plain documentation, and validation.

## Audience

Hiring managers, senior/principal engineers, automation teams, and technical operators who want proof that the work is more than screenshots or vague AI claims.

## Scope

- Keep the original six agentic workflow patterns.
- Add twelve practical business workflows from the local workflow inventory.
- Require every workflow to have importable JSON and a folder README.
- Add TypeScript validation and catalog generation while preserving Python CI checks.
- Reframe documentation away from sales-pack language and toward engineering evidence.

## Selected Workflows

The added workflows cover lead enrichment, support escalation, idempotent webhooks, reconciliation, data migration, competitive monitoring, prompt evaluation, moderation, document understanding, research, tool use, and code review summaries.

## Validation

Validation should check JSON parseability, required n8n fields, minimum workflow substance, sticky-note setup guidance, unique node names, and connection targets. Connections must be checked against node names because n8n exports connections by node name.

## Portfolio Framing

The portfolio should describe the repo as a validated n8n workflow library and avoid implying these are hosted live services. The strongest claims are the measurable ones: eighteen workflow exports, TypeScript catalog generation, Python test coverage, CI validation, and clear import/setup docs.
