# Incident Runbook Agent

## Pattern

Alert intake, severity classification, runbook retrieval, action recommendation, safety gate, human notification, and post-incident audit.

## Flow

Alert Webhook -> Normalize Alert -> Classify Severity -> Fetch Runbook -> Draft Response Plan -> Safety Review -> Route Action -> Notify Owner -> Audit Incident.

## Useful For

SRE support, customer-impact triage, internal platform incidents, and any workflow where an agent should recommend actions without silently executing risky changes.

## Setup Notes

Reconnect OpenAI, Slack, HTTP, and Sheets credentials. Replace the runbook API URL with your docs source or internal knowledge endpoint.

## Validation Focus

The agent recommends actions; the safety review decides whether the plan is informational, requires approval, or should page an owner immediately.
