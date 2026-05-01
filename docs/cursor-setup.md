# Cursor setup — Cursor RPG Studios

**You:** someone who just opened this repository—on GitHub in a browser or already cloned on disk.  
**Goal:** Open the **correct folder** in Cursor so **rules**, **agents**, **tests**, and **lorevault-mcp** work the same way every time—**without** putting API keys in git.

**Time:** about **20–40 minutes** the first time (clone + Python venv + MCP merge). Skim [Section 0](#0-start-here) then follow sections **in order**.

---

## Table of contents

0. [Start here](#0-start-here)
1. [Prerequisites](#1-prerequisites)
2. [Clone and open](#2-clone-and-open)
3. [What configures itself](#3-what-configures-itself)
4. [Two workspace modes](#4-two-workspace-modes)
5. [Environment variables](#5-environment-variables)
6. [MCP — lorevault (local stdio)](#6-mcp--lorevault-local-stdio)
7. [Secrets policy](#7-secrets-policy)
8. [Verify Python + tests](#8-verify-python--tests)
9. [Troubleshooting](#9-troubleshooting)
10. [Publish checklist (maintainers)](#10-publish-checklist-maintainers)

---

## 0. Start here

1. Install **Cursor**, **Git**, and **Python 3.11+** ([Section 1](#1-prerequisites)).
2. **Clone** this repo and open the **repository root** in Cursor ([Section 2](#2-clone-and-open)).
3. Pick **one** workspace mode ([Section 4](#4-two-workspace-modes)): **Mode A** (this repo is the workspace) is the default for this scaffold.
4. Create the Python venv, install `mcp-server`, and run **pytest** ([Section 6](#6-mcp--lorevault-local-stdio), [Section 8](#8-verify-python--tests)).
5. Merge **lorevault** into Cursor’s MCP JSON ([Section 6](#6-mcp--lorevault-local-stdio)), then restart MCP.

**Checkpoint:** After [Section 8](#8-verify-python--tests), you should see either **11 passed, 1 skipped** (normal) or **12 passed** (optional live-canon path).

---

## 1. Prerequisites

| Requirement | Where to get it | Check |
| --- | --- | --- |
| **Cursor** (current stable) | [cursor.com](https://cursor.com/) | App opens; **File → Open Folder…** works |
| **Git** | [git-scm.com](https://git-scm.com/) (macOS/Linux often preinstalled) | `git --version` prints a version |
| **Python 3.11+** | [python.org](https://www.python.org/) or your OS package manager | `python3 --version` shows 3.11 or newer |

If any check fails, install the tool first, then continue.

---

## 2. Clone and open

Official clone URL (public):

```bash
git clone https://github.com/packetalien/cursor-rpg-studios.git
cd cursor-rpg-studios
```

**Checkpoint:** The folder you `cd` into must contain **`README.md`**, **`.cursor/`**, and **`mcp-server/`** at the top level.

In Cursor:

1. **File → Open Folder…**
2. Select that **`cursor-rpg-studios`** folder (not a parent and not a subfolder like `mcp-server` alone).

**Why this matters:** MCP and tests use **`${workspaceFolder}`**. If you open a nested folder, paths in MCP config will break.

---

## 3. What configures itself

When the **repo root** is the workspace, Cursor loads project files automatically:

| Path | What it does |
| --- | --- |
| [`.cursor/rules/*.mdc`](../.cursor/rules/) | Path-scoped rules (Quantum Plaid, FCoP, HITL, output organization, …). No separate install. |
| [`.cursor/agents/`](../.cursor/agents/) | Agent prompt library (directors, leads, specialists). |
| [`.cursor/skills/`](../.cursor/skills/) | Skill playbooks (dual-layer chain, forensic compliance, …). |
| [`agents/README.md`](../agents/README.md) | Human index of agent paths. |

There is **no** background installer and **no** required cloud account for the **lorevault** stub.

---

## 4. Two workspace modes

### Mode A — Studio root (default)

- **Workspace folder:** this repository (`cursor-rpg-studios`).
- **Canon:** lives in a **separate** clone of **Alexandria_Unleashed**. Set **`ALEXANDRIA_CANON_ROOT`** to the **absolute** path of `lore/Alexandria-Unleashed` **inside** that checkout ([Section 5](#5-environment-variables)).
- **Use when:** you are editing **agents, rules, MCP, tests**, or reader pilots under `attachments/` in this repo.

### Mode B — Alexandria manuscript root

- **Workspace folder:** your **Alexandria_Unleashed** checkout (or a subfolder you deliberately choose—prefer repo root for consistency).
- **Canon path:** often **inside** that tree, e.g. `lore/Alexandria-Unleashed/`. From the Alexandria repo root in a terminal:

```bash
export ALEXANDRIA_CANON_ROOT="$PWD/lore/Alexandria-Unleashed"
```

- **Using this repo’s rules/skills while editing canon:** recommended approach is a **multi-root workspace** in Cursor: add **both** `cursor-rpg-studios` and `Alexandria_Unleashed` so you can open rules from the studio repo and Markdown from Alexandria without copying files. Alternatively, copy selected `.mdc` / `SKILL.md` files into the other repo’s `.cursor/` tree—only if you accept drift between copies.

**Checkpoint:** In Mode B, still run **pytest** from the **studio** repo root when you change studio code—not from Alexandria alone unless you have mirrored the test tree.

---

## 5. Environment variables

<a id="alexandria_canon_root"></a>

| Variable | Purpose | Example (adjust paths) |
| --- | --- | --- |
| `ALEXANDRIA_CANON_ROOT` | Absolute path to *Alexandria Unbound* book Markdown root (`lore/Alexandria-Unleashed/`). | `/Users/you/Projects/Alexandria_Unleashed/lore/Alexandria-Unleashed` |
| `ALEXANDRIA_VAULT_ROOT` | Legacy alias in some notes; if set, keep it **identical** to `ALEXANDRIA_CANON_ROOT` unless you intentionally split. | Same as above |

**Current shell session (zsh/bash):**

```bash
export ALEXANDRIA_CANON_ROOT="$HOME/Projects/Alexandria_Unleashed/lore/Alexandria-Unleashed"
```

**Cursor:** **Settings → Cursor Settings → General → Environment Variables** (or your OS user environment) so integrated terminals and tools inherit the same values.

**Sanity check:**

```bash
test -d "$ALEXANDRIA_CANON_ROOT" && echo OK
```

Must print `OK`. This repo **does not** ship the manuscript tree; you clone **Alexandria_Unleashed** separately.

---

## 6. MCP — lorevault (local stdio)

The server lives in [`mcp-server/`](../mcp-server/). Phase 1 uses **no cloud API** for lorevault.

### Step 1 — Install Python package (from repo root)

```bash
cd mcp-server
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cd ..
```

On **Windows** with Git Bash, use `source .venv/Scripts/activate` if `bin` is not present.

### Step 2 — Merge MCP config in Cursor

1. Open **Cursor Settings → MCP** (or the JSON editor Cursor shows for MCP).
2. Ensure there is a top-level **`mcpServers`** object.
3. Paste or merge the **`lorevault`** block below **inside** `mcpServers` (do not nest `mcpServers` twice).

**Default fragment** (same as repo [`mcp.json`](../mcp.json)):

```json
"lorevault": {
  "command": "python3",
  "args": ["-m", "lorevault_mcp.server"],
  "cwd": "${workspaceFolder}/mcp-server",
  "env": {
    "PYTHONPATH": "${workspaceFolder}/mcp-server/src"
  }
}
```

**Recommended for reliability** — point `command` at the venv interpreter you just created (replace `YOU` and path):

```json
"lorevault": {
  "command": "/Users/YOU/Projects/cursor-rpg-studios/mcp-server/.venv/bin/python",
  "args": ["-m", "lorevault_mcp.server"],
  "cwd": "${workspaceFolder}/mcp-server",
  "env": {
    "PYTHONPATH": "${workspaceFolder}/mcp-server/src"
  }
}
```

4. Save the MCP file.
5. **Reload the window** or restart MCP from the MCP panel.

**Nested keys:** If your global MCP file already has `"mcpServers": { ... }`, merge **only** the `lorevault` key into that inner object.

---

## 7. Secrets policy

| Rule | Why |
| --- | --- |
| **Never** commit API keys or `.env` with real secrets | Git history is public or shared. |
| Use **`~/.secrets`** (`KEY=value` per line) or OS env | Matches [`SECURITY.md`](../SECURITY.md). |
| Optional MCP servers (Tavily, Firecrawl, HF, …) go in **Cursor MCP settings only** | Same rule: not in the repo. |

**lorevault** stub: **no token** required.

---

## 8. Verify Python + tests

From **this repo root** (studio workspace):

```bash
cd mcp-server && pip install -e ".[dev]" && cd .. && pytest -q
```

**Expected:**

| Situation | Result |
| --- | --- |
| `ALEXANDRIA_CANON_ROOT` **not** set | **11 passed, 1 skipped** — integration test that reads live canon is skipped. |
| `ALEXANDRIA_CANON_ROOT` set to a valid `…/lore/Alexandria-Unleashed` with pilot files present locally | **12 passed** — includes optional live reader vs canon check ([`tests/test_anchor_subset.py`](../tests/test_anchor_subset.py)). |

If anything fails, use [Section 9](#9-troubleshooting).

---

## 9. Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| MCP server fails to start | Wrong `cwd`, missing install, or wrong `python` | Re-run [Section 6](#6-mcp--lorevault-local-stdio) Step 1; set `command` to venv `python` |
| Rules “not firing” | Workspace is a subfolder | **File → Open Folder…** → select **repo root** |
| Lore tools look “weird” (one fake row, `stub_notice`) | **Expected** stub behavior | `semantic_search_lore` / `graph_traversal` return **sentinel** payloads (`_stub`, `stub_notice`) until Chroma/SQLite land ([`ROADMAP.md`](../ROADMAP.md)). **Do not** treat as retrieved canon; use text search in Markdown for anchors. |
| `ALEXANDRIA_CANON_ROOT` unset | Fresh machine | Set env ([Section 5](#5-environment-variables)); optional for default pytest |

---

## 10. Publish checklist (maintainers)

Use when creating or updating the **public** GitHub remote **`packetalien/cursor-rpg-studios`**:

1. **GitHub:** Create an **empty** public repository named `cursor-rpg-studios` under **`packetalien`** (no README commit from GitHub UI if you want a clean first push—or accept one and pull with `--allow-unrelated-histories` once).
2. **Local:** `git remote add origin https://github.com/packetalien/cursor-rpg-studios.git` (or `git remote set-url origin …`).
3. **Branch:** default **`main`** (matches [`.github/workflows/ci.yml`](../.github/workflows/ci.yml)).
4. **Push:** `git push -u origin main` (requires GitHub auth: HTTPS credential or SSH).

**Do not** bulk-upload the whole tree via GitHub “Add file” UI; use **git push**.

---

*Quick path:* [README.md](../README.md) → **Autonomous Cursor Setup (Recommended)**. Use **this file** for merge details, two workspace modes, and pytest expectations.
