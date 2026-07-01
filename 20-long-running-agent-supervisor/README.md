# Long Running Agent Task Supervisor

## Pattern

Plan expansion, per-step execution, independent validation, repair loop, checkpoint logging, and final run summary.

## Flow

Task Webhook -> Build Plan -> Fan Out Steps -> Execute Step -> Validate Step -> Repair or Checkpoint -> Final Summary -> SLA Gate -> Close or Escalate.

## Useful For

Back-office agents, research runs, migration assistants, QA workers, and any automation where an agent should make bounded progress over several steps.

## Setup Notes

Reconnect OpenAI, Slack, and Sheets credentials. Start with mock tasks and short step limits before moving this pattern onto real operational work.

## Validation Focus

Each step is validated by a separate pass. Failed steps can be repaired once, and every step is checkpointed for auditability.
