# Cursor setup — Cursor RPG Studios

**Audience:** A new operator cloning this repo for the first time.  
**Goal:** Open the workspace in Cursor and have **rules**, **agents**, and **MCP** behave predictably **without** any API keys committed to git.

---

## Table of contents

1. [Prerequisites](#1-prerequisites)
2. [Clone and open](#2-clone-and-open)
3. [What configures itself](#3-what-configures-itself)
4. [Environment variables](#4-environment-variables)
5. [MCP — lorevault (local stdio)](#5-mcp--lorevault-local-stdio)
6. [Secrets policy](#6-secrets-policy)
7. [Verify Python + tests](#7-verify-python--tests)
8. [Troubleshooting](#8-troubleshooting)

---

## 1. Prerequisites

| Requirement | Check |
| --- | --- |
| [Cursor](https://cursor.com/) current stable | Opens folders and reads project `.cursor/` config |
| **Python 3.11+** recommended | `python3 --version` |
| **Git** | `git --version` |

---

## 2. Clone and open

1. Clone this repository to a path of your choice (example uses `~/Projects`).

```bash
mkdir -p ~/Projects
cd ~/Projects
git clone https://github.com/<your-account>/cursor-rpg-studios.git
cd cursor-rpg-studios
```

2. In Cursor: **File → Open Folder…** and select the `cursor-rpg-studios` directory (the folder that contains `README.md` and `.cursor/`).

**Important:** Open the **repository root** as the workspace folder so `${workspaceFolder}` in MCP config resolves correctly.

---

## 3. What configures itself

Cursor loads project-local instructions automatically when the folder is the workspace root:

| Path | Effect |
| --- | --- |
| [`.cursor/rules/*.mdc`](../.cursor/rules/) | Path-scoped rules (Quantum Plaid density, FCoP routing, HITL, stat-block safety). No extra install step. |
| [`.cursor/agents/`](../.cursor/agents/) | Agent prompt library (directors, leads, specialists). Referenced by name in chat or automation. |
| [`agents/README.md`](../agents/README.md) | Human-readable index of agent files. |

There is **no** bootstrap script that phones home or downloads models. Everything is files on disk.

---

## 4. Environment variables

<a id="alexandria_canon_root"></a>

These variables are **optional** for Phase 1 scaffolding but **recommended** once you point tools at real canon.

| Variable | Purpose | Example |
| --- | --- | --- |
| `ALEXANDRIA_CANON_ROOT` | Absolute path to the **Alexandria Unbound** Markdown corpus root (`lore/Alexandria-Unleashed/` inside `Alexandria_Unleashed`). | `/Users/you/Projects/Alexandria_Unleashed/lore/Alexandria-Unleashed` |
| `ALEXANDRIA_VAULT_ROOT` | Legacy / Obsidian-oriented alias used in some notes; if set, keep it **identical** to `ALEXANDRIA_CANON_ROOT` unless you intentionally split vault vs export. | Same as above |

**Shell (zsh/bash), current session only:**

```bash
export ALEXANDRIA_CANON_ROOT="$HOME/Projects/Alexandria_Unleashed/lore/Alexandria-Unleashed"
```

**Cursor:** add the same keys under **Settings → Cursor Settings → General → Environment Variables** (or your OS user environment) so MCP and terminals inherit them.

**Test:** `test -d "$ALEXANDRIA_CANON_ROOT" && echo OK` must print `OK`.

**`ALEXANDRIA_CANON_ROOT` (anchor above):** Absolute path to the **machine-ingest** manuscript root for *Alexandria Unbound* book Markdown (`lore/Alexandria-Unleashed/` inside the Alexandria repo). This studio repo **does not** ship that tree; clone your **Alexandria_Unleashed** checkout (your fork or org remote) separately and set the variable accordingly.

---

## 5. MCP — lorevault (local stdio)

The stub server lives under [`mcp-server/`](../mcp-server/). It uses **no cloud API** in Phase 1.

1. Create a venv and install the package (from repo root):

```bash
cd mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cd ..
pytest
```

2. Merge [`mcp.json`](../mcp.json) into Cursor’s MCP configuration:

   - Open **Cursor Settings → MCP** (or edit the JSON config Cursor shows for MCP).
   - Add (or merge) the `lorevault` server block from this repo’s `mcp.json`.
   - Keep **`cwd`**: `${workspaceFolder}/mcp-server` and **`PYTHONPATH`**: `${workspaceFolder}/mcp-server/src` as in the fragment so `python3 -m lorevault_mcp.server` resolves.

3. If your Python is not `python3`, change the `command` in the merged config to the venv interpreter, for example:

```json
"command": "/Users/you/Projects/cursor-rpg-studios/mcp-server/.venv/bin/python"
```

4. Restart MCP or reload the window after edits.

**Nested `mcpServers`:** This repo’s fragment wraps servers under `"mcpServers"`. When merging into a file that already uses that shape, **nest once** — do not duplicate the outer key twice.

---

## 6. Secrets policy

| Rule | Rationale |
| --- | --- |
| **No API tokens** in this repository | Prevents accidental publish to GitHub. |
| Put keys in **`~/.secrets`** (line-based `KEY=value`) or OS environment | Matches [`SECURITY.md`](../SECURITY.md). |
| When you add Tavily, Firecrawl, HF, or other MCP servers later, configure them **only** in Cursor MCP settings or user config | Same policy: never commit `.env` with real keys (`.gitignore` already ignores `.env`). |

The **lorevault** stub does not require a token.

---

## 7. Verify Python + tests

From repository root:

```bash
cd mcp-server && pip install -e ".[dev]" && cd .. && pytest
```

Expect **all tests passed**. If not, see [§8](#8-troubleshooting).

---

## 8. Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| MCP server fails to start | Wrong `cwd` or missing install | Confirm `pip install -e ".[dev]"` from `mcp-server/`; use venv `python` in MCP config |
| Rules “not firing” | Nested folder opened as workspace | Re-open **repo root** as workspace folder |
| Lore tools return empty arrays | Phase 1 stubs | Expected until Chroma/graph backends land ([`ROADMAP.md`](../ROADMAP.md)) |
| `ALEXANDRIA_CANON_ROOT` unset | Fresh clone | Export variable or set in Cursor env ([§4](#4-environment-variables)) |

---

*For the five-minute path, follow [`README.md`](../README.md) → **Autonomous Cursor Setup (Recommended)** first; use this file for merge details and environment wiring.*
