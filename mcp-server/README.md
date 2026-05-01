# lorevault-mcp (stdio stub)

Python **Model Context Protocol** server for **Cursor RPG Studios**. Backends are **stubs** until Phases 3–4 (Chroma, SQLite graph, Obsidian sync).

## Tools

| Tool | Inputs | Behavior (Phase 1) |
| --- | --- | --- |
| `semantic_search_lore` | `query: str`, optional `tags: str` | Stub: one sentinel `matches[]` entry with `_stub`, plus `stub_notice` (not vector search) |
| `graph_traversal` | `entity_id: str`, `depth: int` | Stub: one sentinel `nodes[]` entry with `_stub`, `edges: []`, plus `stub_notice` (not a real graph) |
| `simulate_roll` | `expression: str` (e.g. `3d6`, `2d6+2`) | Python RNG result |
| `add_character_v1` | `payload: object` | Validates against `../data/schemas/alexandria_npc_entry_v1.schema.json` |

## Install

From repo root:

```bash
cd mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Run (stdio)

```bash
cd mcp-server
source .venv/bin/activate
python -m lorevault_mcp.server
# or: lorevault-mcp
```

## Cursor wiring

Merge the repo-root [`mcp.json`](../mcp.json) fragment into **Cursor Settings → MCP** (or project MCP config). Adjust `command`/`args` if your venv path differs. Step-by-step merge, env vars, and troubleshooting: [`docs/cursor-setup.md`](../docs/cursor-setup.md).

## JSON Schema

Canonical schema path (repo root): `data/schemas/alexandria_npc_entry_v1.schema.json`.

## Build / test

```bash
cd mcp-server && pip install -e ".[dev]" && cd .. && pytest
```
