#!/usr/bin/env python3
"""
Pytest suite for workflow validation.
Run with: pytest tests/test_workflows_valid.py -v
"""

import json
from pathlib import Path
import pytest


def get_workflows():
    """Discover all workflow.json files."""
    repo_root = Path(__file__).parent.parent
    return sorted(repo_root.glob("0?-*/workflow.json"))


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda p: p.parent.name)
def test_workflow_valid_json(workflow_path):
    """Test that workflow is valid JSON."""
    with open(workflow_path) as f:
        json.load(f)


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda p: p.parent.name)
def test_workflow_has_required_fields(workflow_path):
    """Test that workflow has required top-level fields."""
    with open(workflow_path) as f:
        workflow = json.load(f)

    assert "name" in workflow, "Workflow must have a name field"
    assert "nodes" in workflow, "Workflow must have a nodes field"
    assert "connections" in workflow, "Workflow must have a connections field"


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda p: p.parent.name)
def test_workflow_has_minimum_nodes(workflow_path):
    """Test that workflow has at least 6 nodes."""
    with open(workflow_path) as f:
        workflow = json.load(f)

    nodes = workflow.get("nodes", [])
    assert len(nodes) >= 6, f"Workflow must have at least 6 nodes, got {len(nodes)}"


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda p: p.parent.name)
def test_workflow_has_sticky_notes(workflow_path):
    """Test that workflow has at least 2 sticky notes."""
    with open(workflow_path) as f:
        workflow = json.load(f)

    nodes = workflow.get("nodes", [])
    sticky_notes = [n for n in nodes if n.get("type") == "n8n-nodes-base.stickyNote"]
    assert len(sticky_notes) >= 2, f"Workflow must have at least 2 sticky notes, got {len(sticky_notes)}"


@pytest.mark.parametrize("workflow_path", get_workflows(), ids=lambda p: p.parent.name)
def test_workflow_connections_valid(workflow_path):
    """Test that all connections reference existing nodes."""
    with open(workflow_path) as f:
        workflow = json.load(f)

    nodes = workflow.get("nodes", [])
    node_ids = {n.get("id") for n in nodes if "id" in n}

    connections = workflow.get("connections", {})
    for node_id, conn in connections.items():
        assert node_id in node_ids, f"Connection from unknown node: {node_id}"

        if "main" in conn:
            for main_branch in conn.get("main", []):
                for connection in main_branch:
                    target_id = connection.get("node")
                    assert target_id in node_ids, f"Connection to unknown node: {target_id}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
