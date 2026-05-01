# Cursor RPG Studios

**Cursor RPG Studios** is a **production scaffold** for *Alexandria Unbound* (GURPS 4e): a **49-agent / 72-skill** target architecture, **lorevault-mcp** (Python MCP stdio stub), **File-based Coordination Protocol (FCoP)** queues, and **Quantum Plaid** density gates—while keeping **human editorial authority** explicit in rules and workflow docs.

This repository holds **studio mechanics** (agents, rules, MCP, tests, procedural placeholders). It does **not** ship the Alexandria manuscript corpus; that stays in **Alexandria_Unleashed** (separate clone). See [`lore/alexandria-unbound/README.md`](lore/alexandria-unbound/README.md).

## Output Organization

All agent-generated reports, audits, and working outputs are stored in `attachments/` using a strict date-time naming convention.  
This folder is gitignored but preserved locally for forensic review and long-term knowledge mining.

**Like this rule?**  
Copy the prompt below and run it in any other Cursor project to apply the same organization system:

> You are Cursor — Universal Repo Hygiene Engineer.  
> Install the universal Output Organization Rule in this project.  
> Create `.cursor/rules/output-organization.mdc` using the Universal Standard version.  
> Add `attachments/` to `.gitignore`.  
> Reply with: "Universal Output Organization Rule installed in this project."

**License:** [MIT](LICENSE).

## Acknowledgments

This repository is an **independent** studio scaffold. It draws **architectural inspiration** from:

- **[OsirisForge Game Studio](https://github.com/packetalien/OsirisForge-Game-Studio)** — operator layout, Skill Forge framing, and studio discipline.
- **Cursor Game Studios** reference patterns (local **Cursor-Game-Studios** trees and Claude Code–style agent+MCP scaffolding), as compared in [`docs/audits/style-audit-phase0.md`](docs/audits/style-audit-phase0.md).

It is **not** a fork of those repositories unless explicitly stated elsewhere. Upstream names and layouts belong to their respective authors.

## Legal and responsible use

- Software and **documentation in this repository** are provided under the **[MIT License](LICENSE)** *as is*, without warranty.
- This project is **not** legal, medical, or professional tabletop advice. You are responsible for how you use tools, prompts, and generated text at your table.
- **Respect intellectual property:** do not commit third-party manuscript text, licensed setting material, or artwork you do not have rights to redistribute. Pair this tooling only with content you own or may lawfully use.
- **Trademarks** (e.g. *GURPS*) belong to their owners; this repo does not claim affiliation beyond factual references to rules you choose to run.
- If you redistribute a **substantial** portion of this repo’s docs or code, **preserve** license and copyright notices and **attribute** this project appropriately.

---

## Autonomous Cursor Setup (Recommended)

Follow these steps in order. **No API tokens are stored in this repo**—add your own keys only in Cursor settings, `~/.secrets`, or environment variables when you wire optional third-party MCP servers later.

1. **Clone**  
   `git clone https://github.com/packetalien/cursor-rpg-studios.git`  
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

   **CI:** Pushes and pull requests to `main` or `master` run the same suite via [`.github/workflows/ci.yml`](.github/workflows/ci.yml) (`pytest -q` from repo root).

5. **Wire lorevault MCP**  
   Merge the [`mcp.json`](mcp.json) `lorevault` block into **Cursor Settings → MCP**. Use the repo’s `python3` or your venv interpreter; keep `cwd` and `PYTHONPATH` as in the fragment. Restart MCP or reload the window. **The stub needs no API key.**

6. **Point at canon (when you have it)**  
   Clone your Alexandria manuscript repo separately, then set **`ALEXANDRIA_CANON_ROOT`** to its `lore/Alexandria-Unleashed` directory (absolute path). Example:  
   `export ALEXANDRIA_CANON_ROOT="$HOME/Projects/Alexandria_Unleashed/lore/Alexandria-Unleashed"`

7. **Secrets**  
   Never commit `.env` or API keys. Use **`~/.secrets`** (`KEY=value` per line) per [`SECURITY.md`](SECURITY.md).

**Deeper walkthrough (merge semantics, troubleshooting):** [`docs/cursor-setup.md`](docs/cursor-setup.md).

## Reader companion pilots (dual-layer)

Normative contract: [`docs/human-machine-dual-layer-pattern.md`](docs/human-machine-dual-layer-pattern.md) **v1.0.2** (Section 3 five-section template, Section 8 pilot paths). Filled exemplars and machine-validation reports live under **`attachments/drafts/`** and **`attachments/reports/`** (folder is **gitignored** — copies exist on machines that ran the pilots). Set **`ALEXANDRIA_CANON_ROOT`** to your `Alexandria_Unleashed/lore/Alexandria-Unleashed` checkout for the optional **live-canon** pytest (`12` tests); without it, CI and local default runs stay **fixtures-first** (`11` passed, `1` skipped).

---

## Documentation surface

This repository intentionally uses **multiple root operational Markdown files** (`ROADMAP.md`, `TASKLIST.md`, `MANIFEST.md`, `quantum_plaid.md`, `STYLE_BIBLE.md`, …) aligned with [OsirisForge Game Studio](https://github.com/packetalien/OsirisForge-Game-Studio) and the **Alexandria_Unleashed** operator layout. Navigation hub: [`docs/index.md`](docs/index.md).

## Quick links

| Document | Role |
| --- | --- |
| [`docs/cursor-setup.md`](docs/cursor-setup.md) | Clone, MCP merge, two workspace modes, pytest, troubleshooting |
| [`docs/cursor-install.md`](docs/cursor-install.md) | One-screen pointer to setup (for `install` / agent filename search) |
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
- **lorevault-mcp:** [`mcp-server/`](mcp-server/) — stdio MCP stub (`semantic_search_lore`, `graph_traversal`, `simulate_roll`, `add_character_v1`). Graph/search return **sentinel** payloads until Phase 3 backends — not production lore retrieval.
- **Canon pointer:** [`lore/alexandria-unbound/README.md`](lore/alexandria-unbound/README.md).
- **FCoP queue:** [`docs/agents/status/`](docs/agents/status/).

## MCP (local)

See step **5** above and [`mcp-server/README.md`](mcp-server/README.md). Full merge and env details: [`docs/cursor-setup.md`](docs/cursor-setup.md).
