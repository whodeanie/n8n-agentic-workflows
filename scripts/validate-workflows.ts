import { mkdir, readdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

type N8nNode = {
  id?: unknown;
  name?: unknown;
  type?: unknown;
};

type N8nConnection = {
  node?: unknown;
};

type N8nWorkflow = {
  name?: unknown;
  nodes?: unknown;
  connections?: unknown;
};

type CatalogEntry = {
  slug: string;
  name: string;
  nodeCount: number;
  stickyNoteCount: number;
  triggerTypes: string[];
  integrationTypes: string[];
  workflowPath: string;
};

type ValidationResult = {
  filePath: string;
  errors: string[];
  catalogEntry?: CatalogEntry;
};

const MIN_NODE_COUNT = 6;
const MIN_STICKY_NOTE_COUNT = 2;
const WORKFLOW_DIR_PATTERN = /^\d{2}-.+$/;
const repoRoot = process.cwd();

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function asString(value: unknown): string | undefined {
  return typeof value === "string" && value.trim().length > 0 ? value : undefined;
}

function nodeTypeLabel(nodeType: string): string {
  return nodeType.replace(/^n8n-nodes-base\./, "");
}

async function discoverWorkflowFiles(): Promise<string[]> {
  const entries = await readdir(repoRoot, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isDirectory() && WORKFLOW_DIR_PATTERN.test(entry.name))
    .map((entry) => path.join(repoRoot, entry.name, "workflow.json"))
    .sort();
}

async function readWorkflow(filePath: string): Promise<N8nWorkflow> {
  const raw = await readFile(filePath, "utf8");
  return JSON.parse(raw) as N8nWorkflow;
}

function validateWorkflow(filePath: string, workflow: N8nWorkflow): ValidationResult {
  const errors: string[] = [];
  const slug = path.basename(path.dirname(filePath));

  const workflowName = asString(workflow.name);
  if (!workflowName) {
    errors.push("Missing required string field: name");
  }

  if (!Array.isArray(workflow.nodes)) {
    errors.push("Missing required array field: nodes");
  }

  if (!isRecord(workflow.connections)) {
    errors.push("Missing required object field: connections");
  }

  if (errors.length > 0) {
    return { filePath, errors };
  }

  const nodes = workflow.nodes as N8nNode[];
  const connections = workflow.connections as Record<string, unknown>;
  const nodeNames = new Set<string>();
  const nodeIds = new Set<string>();
  const nodeTypes = new Set<string>();
  const triggerTypes = new Set<string>();
  const duplicateNames = new Set<string>();
  const duplicateIds = new Set<string>();

  if (nodes.length < MIN_NODE_COUNT) {
    errors.push(`Expected at least ${MIN_NODE_COUNT} nodes, got ${nodes.length}`);
  }

  for (const [index, node] of nodes.entries()) {
    if (!isRecord(node)) {
      errors.push(`Node at index ${index} must be an object`);
      continue;
    }

    const nodeName = asString(node.name);
    const nodeId = asString(node.id);
    const nodeType = asString(node.type);

    if (!nodeName) {
      errors.push(`Node at index ${index} is missing a name`);
    } else if (nodeNames.has(nodeName)) {
      duplicateNames.add(nodeName);
    } else {
      nodeNames.add(nodeName);
    }

    if (node.id !== undefined) {
      if (!nodeId) {
        errors.push(`Node '${nodeName ?? index}' has an invalid id`);
      } else if (nodeIds.has(nodeId)) {
        duplicateIds.add(nodeId);
      } else {
        nodeIds.add(nodeId);
      }
    }

    if (nodeType) {
      nodeTypes.add(nodeType);
      if (nodeType.includes("Trigger") || nodeType.endsWith(".webhook")) {
        triggerTypes.add(nodeTypeLabel(nodeType));
      }
    }
  }

  for (const name of [...duplicateNames].sort()) {
    errors.push(`Duplicate node name: ${name}`);
  }

  for (const nodeId of [...duplicateIds].sort()) {
    errors.push(`Duplicate node id: ${nodeId}`);
  }

  const stickyNoteCount = nodes.filter((node) => node.type === "n8n-nodes-base.stickyNote").length;
  if (stickyNoteCount < MIN_STICKY_NOTE_COUNT) {
    errors.push(`Expected at least ${MIN_STICKY_NOTE_COUNT} sticky notes, got ${stickyNoteCount}`);
  }

  for (const [sourceName, sourceConnections] of Object.entries(connections)) {
    if (!nodeNames.has(sourceName)) {
      errors.push(`Connection references unknown source node: ${sourceName}`);
      continue;
    }

    if (!isRecord(sourceConnections)) {
      errors.push(`Connections for '${sourceName}' must be an object`);
      continue;
    }

    const mainConnections = sourceConnections.main;
    if (mainConnections === undefined) {
      continue;
    }

    if (!Array.isArray(mainConnections)) {
      errors.push(`Main connections for '${sourceName}' must be an array`);
      continue;
    }

    for (const branch of mainConnections) {
      if (!Array.isArray(branch)) {
        errors.push(`Connection branch for '${sourceName}' must be an array`);
        continue;
      }

      for (const connection of branch as N8nConnection[]) {
        if (!isRecord(connection)) {
          errors.push(`Connection from '${sourceName}' must be an object`);
          continue;
        }

        const targetName = asString(connection.node);
        if (!targetName || !nodeNames.has(targetName)) {
          errors.push(`Connection from '${sourceName}' references unknown target node: ${targetName}`);
        }
      }
    }
  }

  const integrationTypes = [...nodeTypes]
    .filter((nodeType) => nodeType !== "n8n-nodes-base.stickyNote")
    .map(nodeTypeLabel)
    .sort();

  return {
    filePath,
    errors,
    catalogEntry: {
      slug,
      name: workflowName ?? slug,
      nodeCount: nodes.length,
      stickyNoteCount,
      triggerTypes: [...triggerTypes].sort(),
      integrationTypes,
      workflowPath: path.relative(repoRoot, filePath),
    },
  };
}

async function writeCatalog(entries: CatalogEntry[]): Promise<void> {
  const catalogPath = path.join(repoRoot, "catalog", "workflows.json");
  await mkdir(path.dirname(catalogPath), { recursive: true });
  await writeFile(catalogPath, `${JSON.stringify(entries, null, 2)}\n`);
}

async function main(): Promise<void> {
  const shouldWriteCatalog = process.argv.includes("--write-catalog");
  const workflowFiles = await discoverWorkflowFiles();

  if (workflowFiles.length === 0) {
    console.error("ERROR: No numbered workflow.json files found.");
    process.exitCode = 1;
    return;
  }

  const results: ValidationResult[] = [];
  for (const filePath of workflowFiles) {
    try {
      const workflow = await readWorkflow(filePath);
      results.push(validateWorkflow(filePath, workflow));
    } catch (error) {
      const message = error instanceof Error ? error.message : String(error);
      results.push({ filePath, errors: [`Unable to read workflow JSON: ${message}`] });
    }
  }

  const failed = results.filter((result) => result.errors.length > 0);
  for (const result of results) {
    const slug = path.basename(path.dirname(result.filePath));
    if (result.errors.length > 0) {
      console.error(`FAIL ${slug}`);
      for (const error of result.errors) {
        console.error(`  - ${error}`);
      }
    } else {
      console.log(`PASS ${slug}`);
    }
  }

  if (failed.length > 0) {
    console.error(`\n${failed.length} workflow(s) failed validation.`);
    process.exitCode = 1;
    return;
  }

  const catalogEntries = results
    .map((result) => result.catalogEntry)
    .filter((entry): entry is CatalogEntry => entry !== undefined);

  if (shouldWriteCatalog) {
    await writeCatalog(catalogEntries);
    console.log(`\nCatalog written with ${catalogEntries.length} workflows.`);
  } else {
    console.log(`\nAll ${catalogEntries.length} workflows valid.`);
  }
}

main().catch((error: unknown) => {
  const message = error instanceof Error ? error.message : String(error);
  console.error(message);
  process.exitCode = 1;
});
