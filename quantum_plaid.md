# Quantum Plaid Protocol — Cursor RPG Studios

**Version:** 1.0 (studio overlay)  
**Last updated:** 2026-04-30  
**Purpose:** Align generated manuscripts and tooling with *Alexandria Unbound* density, GURPS 4e integrity, and **human editorial veto**.

## Core principles

| Principle | Studio enforcement |
| --- | --- |
| **Human imagination first, AI-readable second** | No `alexandria_*_entry_v1` JSON export until prose gates pass Editorial Lead review. |
| **Quantum Plaid density** | Standard books **≥ 9.0** composite; Gear Libraries / Centerpieces **≥ 9.5**. |
| **Fifteen operator voices** | Carved-voice quotes / marginalia — personas include **EIC Ledger Clerk**, **Clockwork Baron**, **Marcus Agrippa** flavor lines, *Forbidden Wing* warnings, etc. |
| **Twelve GURPS 4e NPCs per chapter** | Stat Block Engineer + MCP validation; **no LLM arithmetic** for derived stats. |
| **5% Cosmic Backfire** | On critical failure bands per setting doc; **artifacts with value ≥ 80** get full severe-failure tables (Temporal Inversion, Sanity Blast, …). |
| **Sensory covenant** | Smell / sound / touch explicitly tied to mechanics where applicable. |
| **Phase bridges** | Explicit `{#anchor}` cross-links to prior books and sister volumes. |

## Schwartz Mode (centerpieces)

Recursive high-temperature expansion for Library-grade deliverables: **Flavor Author** + **Editorial Lead** drive obsessive sensory density (*ozone stench of raw thaumaturgy*, brass-sea acoustics, bureaucratic horror).

## Workflow gates (summary)

1. **Graph check** — Lore Keeper runs `graph_traversal` before retconning factions or timelines.  
2. **Math check** — All numeric derivation through **MCP** (`simulate_roll`, validators); LLM formats only.  
3. **Density check** — `quantum-plaid-density.mdc` on `docs/drafts/**/*.md`.  
4. **Human stop** — Every generative pass ends: options, pros/cons, **“What do you think, Director?”**

## References

- Sibling canon: `../Alexandria_Unleashed/docs/quantum_plaid.md` (full protocol prose).  
- Roadmap integration: [`ROADMAP.md`](ROADMAP.md) **`{#quantum-plaid-phase-contract}`**.
