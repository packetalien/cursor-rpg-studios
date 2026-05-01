# Roadmap — Cursor RPG Studios

## Table of contents

- [Executive summary](#executive-summary)
- [Phase 0 — Bootstrap](#phase-0--bootstrap)
- [Quantum Plaid phase contract](#quantum-plaid-phase-contract)
- [Build phases 1–10 (Gemini pipeline)](#build-phases-110-gemini-pipeline)
- [Risk and mitigation](#risk-and-mitigation)
- [Public vs private layers](#public-vs-private-layers)
- [Index](#index)

## Executive summary

**Cursor RPG Studios** implements a **49-agent / 72-skill** hierarchy (Claude-Code-Game-Studios pattern) adapted for **TTRPG publishing** and *Alexandria Unbound* **GURPS 4e** rigor. Coordination uses **FCoP** (file renames in `docs/agents/status/`) to avoid context-window bloat; memory uses **lorevault-mcp** (vectors + graph + Obsidian SSoT). **Phase 1 is IN PROGRESS** at initial scaffolding: agents, `.mdc` rules, MCP **stdio stub**, documentation spine.

## Phase 0 — Bootstrap {#phase-0--bootstrap}

| Deliverable | Exit criteria | Owner veto gate |
| --- | --- | --- |
| Root operational docs | `ROADMAP`, `TASKLIST`, `STATUS`, `CHANGES`, `MANIFEST`, `quantum_plaid`, `STYLE_BIBLE` present | Producer |
| Agent skeleton | Tier 1–3 prompts + Phase 1 deep prompts (Narrative Director, Lore Keeper, Stat Block Engineer) | Creative Director |
| Rules | `quantum-plaid-density.mdc` + HITL + FCoP + JSON safety stubs | Producer |
| MCP stub | `mcp-server` registers `semantic_search_lore`, `graph_traversal` (schemas documented) | Mechanics Director |
| Tests | `pytest` green on schema + stub tools | Producer |

## Quantum Plaid phase contract {#quantum-plaid-phase-contract}

| Element | Target |
| --- | --- |
| Density (standard) | **≥ 9.0** composite |
| Density (Gear Library / Centerpiece) | **≥ 9.5** |
| Operator quotes | **15** per chapter |
| GURPS NPC stat blocks | **12** per chapter |
| Tables | **8–12** numbered with `{#table-…}` |
| Adventure seeds | **10–15** high-stakes |
| Sensory covenant | Explicit multisensory + mechanical hooks |
| Phase bridges | Anchored cross-links to prior/sister books |
| 5% Cosmic Backfire | Artifact value **≥ 80** → full severe-failure table |

## Build phases 1–10 (Gemini pipeline) {#build-phases-110-gemini-pipeline}

| Phase | Name | Exit criteria | Owner veto gate |
| --- | --- | --- | --- |
| **1** | Studio initialization | Tier 1–2 agent files; lorevault SQLite/vector **stubs**; baseline `.mdc` rules | Producer |
| **2** | Skill Forge | 72 skill playbooks under `.cursor/skills/` with YAML frontmatter | Producer |
| **3** | MCP memory integration | Chroma + graph DB wired to MCP tools (read paths) | Mechanics Director |
| **4** | Vault synchronization | Bidirectional Obsidian sync + optimistic locking | Producer |
| **5** | GM runtime | GURPS / PF2e validators ported to Tier 3 | Mechanics Director |
| **6** | Quantum Plaid alignment | Automated gates: 15 quotes + 12 NPCs + backfire tables | Creative Director |
| **7** | FCoP orchestration | Queue conventions + collision surfacing to Producer | Producer |
| **8** | MCP Apps UI | HTML/CSS character sheet previews in chat | Creative Director |
| **9** | Playtest + Cosmic Backfire | Monte Carlo on stress scenarios; backfire rate audit | Mechanics Director |
| **10** | Marketplace polish | Security audit; packaging; operator runbooks | Producer |

### Phase 1 status

**IN PROGRESS** — see [`TASKLIST.md`](TASKLIST.md) sprint rows and [`STATUS.md`](STATUS.md).

## Risk and mitigation

| Risk | Mitigation |
| --- | --- |
| Context window asphyxiation | FCoP routing; no monolithic orchestrator chat |
| Canon drift | `graph_traversal` before lore edits; Canon Auditor |
| LLM math errors | MCP `simulate_roll` + schema validators only |
| MCP tool supply chain | Pin SDK versions; minimal tool surface; no silent writes |

## Public vs private layers

| Layer | Contents |
| --- | --- |
| **Public (this repo)** | Agents, rules, procedural placeholders, MCP stub, schemas, docs index |
| **Private (operator machine)** | Obsidian vault path, API keys in `~/.secrets`, OpenClaw job secrets |

## Index {#index}

- **FCoP:** [`docs/agents/status/README.md`](docs/agents/status/README.md)
- **lorevault-mcp:** [`mcp-server/README.md`](mcp-server/README.md)
- **Quantum Plaid:** [`quantum_plaid.md`](quantum_plaid.md) **`{#quantum-plaid-phase-contract}`**
