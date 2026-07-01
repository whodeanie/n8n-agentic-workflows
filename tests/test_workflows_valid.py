#!/usr/bin/env python3
"""Pytest suite for n8n workflow exports."""

import json
from pathlib import Path

import pytest


MIN_NODE_COUNT = 6
MIN_STICKY_NOTE_COUNT = 2


def get_workflows() -> list[Path]:
    """Discover all numbered workflow.json files."""

    repo_root = Path(__file__).parent.parent
    return sorted(repo_root.glob("[0-9][0-9]-*/workflow.json"))


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda path: path.parent.name)
def test_workflow_valid_json(workflow_path: Path) -> None:
    with workflow_path.open() as workflow_file:
        json.load(workflow_file)


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda path: path.parent.name)
def test_workflow_has_required_fields(workflow_path: Path) -> None:
    with workflow_path.open() as workflow_file:
        workflow = json.load(workflow_file)

    assert "name" in workflow, "Workflow must have a name field"
    assert "nodes" in workflow, "Workflow must have a nodes field"
    assert "connections" in workflow, "Workflow must have a connections field"


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda path: path.parent.name)
def test_workflow_has_enough_nodes_and_notes(workflow_path: Path) -> None:
    with workflow_path.open() as workflow_file:
        workflow = json.load(workflow_file)

    nodes = workflow.get("nodes", [])
    sticky_notes = [node for node in nodes if node.get("type") == "n8n-nodes-base.stickyNote"]

    assert len(nodes) >= MIN_NODE_COUNT, (
        f"Workflow must have at least {MIN_NODE_COUNT} nodes, got {len(nodes)}"
    )
    assert len(sticky_notes) >= MIN_STICKY_NOTE_COUNT, (
        f"Workflow must have at least {MIN_STICKY_NOTE_COUNT} sticky notes, got {len(sticky_notes)}"
    )


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda path: path.parent.name)
def test_workflow_node_names_are_unique(workflow_path: Path) -> None:
    with workflow_path.open() as workflow_file:
        workflow = json.load(workflow_file)

    node_names = [node.get("name") for node in workflow.get("nodes", [])]
    assert all(node_names), "Every node must have a name"
    assert len(node_names) == len(set(node_names)), "Node names must be unique"


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda path: path.parent.name)
def test_workflow_connections_reference_existing_node_names(workflow_path: Path) -> None:
    with workflow_path.open() as workflow_file:
        workflow = json.load(workflow_file)

    node_names = {node.get("name") for node in workflow.get("nodes", [])}

    for source_name, source_connections in workflow.get("connections", {}).items():
        assert source_name in node_names, f"Connection from unknown node: {source_name}"

        for main_branch in source_connections.get("main", []):
            for connection in main_branch:
                target_name = connection.get("node")
                assert target_name in node_names, f"Connection to unknown node: {target_name}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
