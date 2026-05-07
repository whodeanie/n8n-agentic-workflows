#!/usr/bin/env python3
"""
Validate n8n workflow JSON files.

Checks:
- Valid JSON syntax
- Required fields: name, nodes, connections
- At least 6 nodes per workflow
- At least 2 sticky notes
- Node connections are wired correctly
"""

import json
import sys
from pathlib import Path


def validate_workflow(workflow_path):
    """Validate a single workflow.json file."""
    errors = []

    try:
        with open(workflow_path) as f:
            workflow = json.load(f)
    except json.JSONDecodeError as e:
        return [f"JSON parse error: {e}"]
    except FileNotFoundError:
        return [f"File not found: {workflow_path}"]

    if not isinstance(workflow, dict):
        errors.append("Workflow must be a JSON object")
        return errors

    if "name" not in workflow:
        errors.append("Missing required field: name")
    if "nodes" not in workflow:
        errors.append("Missing required field: nodes")
    if "connections" not in workflow:
        errors.append("Missing required field: connections")

    if errors:
        return errors

    nodes = workflow.get("nodes", [])
    if not isinstance(nodes, list) or len(nodes) < 6:
        errors.append(f"Expected at least 6 nodes, got {len(nodes)}")

    sticky_notes = [n for n in nodes if n.get("type") == "n8n-nodes-base.stickyNote"]
    if len(sticky_notes) < 2:
        errors.append(f"Expected at least 2 sticky notes, got {len(sticky_notes)}")

    node_ids = {n.get("id") for n in nodes if "id" in n}
    for node_id, connections in workflow.get("connections", {}).items():
        if node_id not in node_ids:
            errors.append(f"Connection references unknown node: {node_id}")
        if "main" in connections:
            for main_branch in connections.get("main", []):
                for connection in main_branch:
                    target_id = connection.get("node")
                    if target_id and target_id not in node_ids:
                        errors.append(f"Connection references unknown node: {target_id}")

    return errors


def main():
    """Run validation on all workflows."""
    repo_root = Path(__file__).parent.parent
    workflows = sorted(repo_root.glob("0?-*/workflow.json"))

    if not workflows:
        print("ERROR: No workflows found")
        return 1

    all_passed = True
    for workflow_path in workflows:
        print(f"Validating {workflow_path.parent.name}...", end=" ")
        errors = validate_workflow(workflow_path)

        if errors:
            print("FAILED")
            for error in errors:
                print(f"  - {error}")
            all_passed = False
        else:
            print("PASSED")

    if all_passed:
        print(f"\nAll {len(workflows)} workflows valid.")
        return 0
    else:
        print(f"\nValidation failed for one or more workflows.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
