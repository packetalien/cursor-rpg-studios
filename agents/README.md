# Agents — index

Authoritative prompts live under **`.cursor/agents/`** (Cursor-native). This directory is a **human-readable index** only.

| Tier | Path |
| --- | --- |
| **1 — Directors** | [`.cursor/agents/directors/`](../.cursor/agents/directors) |
| **2 — Leads** | [`.cursor/agents/leads/`](../.cursor/agents/leads) |
| **3 — Specialists** | [`.cursor/agents/specialists/`](../.cursor/agents/specialists) |

**Human vs machine layers:** Reader companions and canonical SSoT are governed by [`docs/human-machine-dual-layer-pattern.md`](../docs/human-machine-dual-layer-pattern.md) (v1.0, locked). Tier 1–2 agents that touch manuscript paths should treat that document as normative alongside `quantum_plaid.md` and `STYLE_BIBLE.md`.

## Phase 1 deep prompts

| File | Role |
| --- | --- |
| [`narrative-director.md`](../.cursor/agents/directors/narrative-director.md) | Macro-plot, phase bridges, sensory covenants |
| [`editorial-lead.md`](../.cursor/agents/leads/editorial-lead.md) | Human layer (reader companions), dual-layer merge gates, forensic draft routing, Schwartz coordination |
| [`lore-keeper.md`](../.cursor/agents/leads/lore-keeper.md) | Graph / timeline; `graph_traversal` (stub-aware) |
| [`stat-block-engineer.md`](../.cursor/agents/specialists/stat-block-engineer.md) | GURPS 4e + `alexandria_npc_entry_v1` |

Every agent file ends with the **Human-First** closing: present options, pros/cons, then **“What do you think, Director?”**
