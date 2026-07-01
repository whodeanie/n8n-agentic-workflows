# LLM Router

## Pattern

Cheap classification before specialized handling. The workflow classifies intent first, then routes the request into focused handler prompts instead of running one large generic prompt.

## Flow

Webhook In -> Classify Intent -> Extract Intent -> Route Based on Intent -> Specialist Handler -> Merge.

## Useful For

Support intake, billing questions, internal help desks, triage bots, and any workflow where requests should land in different response paths.

## Setup Notes

Reconnect the LLM credential and adjust the intent labels to match the business process. Add examples to the classifier prompt before adding more branches.

## Validation Focus

Routing keeps cost and behavior inspectable. Misclassification can be measured separately from specialist response quality.
