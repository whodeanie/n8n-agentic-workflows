#!/usr/bin/env python3
"""Validate importable n8n workflow JSON files.

The n8n export format stores workflow connections by node *name*, not by node
ID. This validator follows that convention and catches the failure modes that
make imported templates feel broken: missing names, dangling connections,
duplicate nodes, thin canvases, and missing setup notes.
"""

import json
import sys
from pathlib import Path
from typing import Optional


MIN_NODE_COUNT = 6
MIN_STICKY_NOTE_COUNT = 2


def discover_workflows(repo_root: Path):
    """Return numbered workflow exports such as 01-example/workflow.json."""

    return sorted(repo_root.glob("[0-9][0-9]-*/workflow.json"))


def _load_json(workflow_path: Path) -> tuple[Optional[dict], list[str]]:
    try:
        with workflow_path.open() as workflow_file:
            workflow = json.load(workflow_file)
    except json.JSONDecodeError as exc:
        return None, [f"JSON parse error: {exc}"]
    except FileNotFoundError:
        return None, [f"File not found: {workflow_path}"]

    if not isinstance(workflow, dict):
        return None, ["Workflow must be a JSON object"]

    return workflow, []


def validate_workflow(workflow_path: Path) -> list[str]:
    """Validate a single workflow.json file."""

    errors = []
    workflow, load_errors = _load_json(workflow_path)
    if load_errors:
        return load_errors

    assert workflow is not None

    for field in ("name", "nodes", "connections"):
        if field not in workflow:
            errors.append(f"Missing required field: {field}")

    if errors:
        return errors

    nodes = workflow.get("nodes", [])
    connections = workflow.get("connections", {})

    if not isinstance(nodes, list):
        errors.append("Field 'nodes' must be a list")
        nodes = []
    elif len(nodes) < MIN_NODE_COUNT:
        errors.append(f"Expected at least {MIN_NODE_COUNT} nodes, got {len(nodes)}")

    if not isinstance(connections, dict):
        errors.append("Field 'connections' must be an object")
        connections = {}

    node_names = set()
    node_ids = set()
    duplicate_names = set()
    duplicate_ids = set()

    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"Node at index {index} must be an object")
            continue

        node_name = node.get("name")
        node_id = node.get("id")

        if not isinstance(node_name, str) or not node_name.strip():
            errors.append(f"Node at index {index} is missing a name")
        elif node_name in node_names:
            duplicate_names.add(node_name)
        else:
            node_names.add(node_name)

        if node_id is not None:
            if not isinstance(node_id, str) or not node_id.strip():
                errors.append(f"Node '{node_name or index}' has an invalid id")
            elif node_id in node_ids:
                duplicate_ids.add(node_id)
            else:
                node_ids.add(node_id)

    for name in sorted(duplicate_names):
        errors.append(f"Duplicate node name: {name}")

    for node_id in sorted(duplicate_ids):
        errors.append(f"Duplicate node id: {node_id}")

    sticky_notes = [node for node in nodes if node.get("type") == "n8n-nodes-base.stickyNote"]
    if len(sticky_notes) < MIN_STICKY_NOTE_COUNT:
        errors.append(f"Expected at least {MIN_STICKY_NOTE_COUNT} sticky notes, got {len(sticky_notes)}")

    for source_name, source_connections in connections.items():
        if source_name not in node_names:
            errors.append(f"Connection references unknown source node: {source_name}")
            continue

        if not isinstance(source_connections, dict):
            errors.append(f"Connections for '{source_name}' must be an object")
            continue

        for branch_index, branch in enumerate(source_connections.get("main", [])):
            if not isinstance(branch, list):
                errors.append(f"Main branch {branch_index} for '{source_name}' must be a list")
                continue

            for connection in branch:
                if not isinstance(connection, dict):
                    errors.append(f"Connection from '{source_name}' must be an object")
                    continue

                target_name = connection.get("node")
                if target_name not in node_names:
                    errors.append(f"Connection from '{source_name}' references unknown target node: {target_name}")

    return errors


def main() -> int:
    """Run validation on all numbered workflows."""

    repo_root = Path(__file__).parent.parent
    workflows = discover_workflows(repo_root)

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

    print("\nValidation failed for one or more workflows.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
