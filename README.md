# Cursor RPG Studios

**Cursor RPG Studios** is a **production scaffold** for *Alexandria Unbound* (GURPS 4e): a **49-agent / 72-skill** target architecture, **lorevault-mcp** (Python MCP stdio stub), **File-based Coordination Protocol (FCoP)** queues, and **Quantum Plaid** density gates—while keeping **human editorial authority** explicit in rules and workflow docs.

This repository holds **studio mechanics** (agents, rules, MCP, tests, procedural placeholders). It does **not** ship the Alexandria manuscript corpus; that stays in **Alexandria_Unleashed** (separate clone). See [`lore/alexandria-unbound/README.md`](lore/alexandria-unbound/README.md).

**License:** [MIT](LICENSE).

---

## Autonomous Cursor Setup (Recommended)

Follow these steps in order. **No API tokens are stored in this repo**—add your own keys only in Cursor settings, `~/.secrets`, or environment variables when you wire optional third-party MCP servers later.

1. **Clone**  
   `git clone https://github.com/<your-account>/cursor-rpg-studios.git`  
   `cd cursor-rpg-studios`

2. **Open the repo root in Cursor**  
   Use **File → Open Folder…** and select the folder that contains this `README.md` and the `.cursor/` directory. (Opening a subfolder breaks `${workspaceFolder}` paths in MCP.)

3. **Let Cursor load project config**  
   Rules under [`.cursor/rules/`](.cursor/rules/) apply automatically to matched paths. Agent prompts live under [`.cursor/agents/`](.cursor/agents/) with a human index at [`agents/README.md`](agents/README.md). No separate “install rules” step.

4. **Python + tests (optional but recommended)**  
   ```bash
   cd mcp-server && python3 -m venv .venv && source .venv/bin/activate
   pip install -e ".[dev]" && cd .. && pytest
   ```

5. **Wire lorevault MCP**  
   Merge the [`mcp.json`](mcp.json) `lorevault` block into **Cursor Settings → MCP**. Use the repo’s `python3` or your venv interpreter; keep `cwd` and `PYTHONPATH` as in the fragment. Restart MCP or reload the window. **The stub needs no API key.**

6. **Point at canon (when you have it)**  
   Clone your Alexandria manuscript repo separately, then set **`ALEXANDRIA_CANON_ROOT`** to its `lore/Alexandria-Unleashed` directory (absolute path). Example:  
   `export ALEXANDRIA_CANON_ROOT="$HOME/Projects/Alexandria_Unleashed/lore/Alexandria-Unleashed"`

7. **Secrets**  
   Never commit `.env` or API keys. Use **`~/.secrets`** (`KEY=value` per line) per [`SECURITY.md`](SECURITY.md).

**Deeper walkthrough (merge semantics, troubleshooting):** [`docs/cursor-setup.md`](docs/cursor-setup.md).

---

## Documentation surface

This repository intentionally uses **multiple root operational Markdown files** (`ROADMAP.md`, `TASKLIST.md`, `MANIFEST.md`, `quantum_plaid.md`, `STYLE_BIBLE.md`, …) aligned with [OsirisForge Game Studio](https://github.com/packetalien/OsirisForge-Game-Studio) and the **Alexandria_Unleashed** operator layout. Navigation hub: [`docs/index.md`](docs/index.md).

## Quick links

| Document | Role |
| --- | --- |
| [`ROADMAP.md`](ROADMAP.md) | Phases 0–10, exit criteria, Quantum Plaid alignment |
| [`TASKLIST.md`](TASKLIST.md) | Living sprint board |
| [`STATUS.md`](STATUS.md) | Health and recent updates |
| [`CHANGES.md`](CHANGES.md) | Changelog |
| [`MANIFEST.md`](MANIFEST.md) | Path → purpose index |
| [`quantum_plaid.md`](quantum_plaid.md) | Density + workflow contract |
| [`STYLE_BIBLE.md`](STYLE_BIBLE.md) | Voice, cartography, sensory covenant |
| [`SECURITY.md`](SECURITY.md) | MCP posture and secrets |
| [`docs/human-machine-dual-layer-pattern.md`](docs/human-machine-dual-layer-pattern.md) | Canonical vs reader companion contract |

## Layout

- **Agents:** [`.cursor/agents/`](.cursor/agents/) — [`agents/README.md`](agents/README.md).
- **lorevault-mcp:** [`mcp-server/`](mcp-server/) — stdio MCP stub (`semantic_search_lore`, `graph_traversal`, `simulate_roll`, `add_character_v1`).
- **Canon pointer:** [`lore/alexandria-unbound/README.md`](lore/alexandria-unbound/README.md).
- **FCoP queue:** [`docs/agents/status/`](docs/agents/status/).

## MCP (local)

See step **5** above and [`mcp-server/README.md`](mcp-server/README.md). Full merge and env details: [`docs/cursor-setup.md`](docs/cursor-setup.md).
