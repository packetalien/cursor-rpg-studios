# Style audit — Phase 0 (Schwartz / REVENGE gate)

**Auditor role:** Style Auditor and Quality Gatekeeper (Schwartz Mode).  
**Scope:** This repository (**cursor-rpg-studios**) compared to reference scaffolds **Alexandria_Unleashed** and **Cursor-Game-Studios** / OsirisForge Game Studio (optional local clones for side-by-side review; not vendored here).  
**Date:** 2026-04-30.

---

## 1. Executive summary

**Overall score: 6.2 / 10.** The scaffold lands the **right file classes** (root ops docs, `.cursor/agents/`, `.mdc`, `mcp-server/`, FCoP queue, procedural stubs, tests) and reads as a **serious studio contract**, not a toy README. It does **not** yet match the **information density**, **cross-link gravity**, or **operational ritual** of Alexandria’s living corpus or OsirisForge’s **generator-backed** rigor. Several **hard deltas** block “same author” illusion: Quantum Plaid **numeric targets** disagree with Alexandria’s published phase contract; `docs/` layout conflicts with Alexandria’s stated “`docs/` holds `index.md` only” rule (TASKLIST note) yet this audit adds another subfolder; reference filenames in the audit brief (`ROADMAP-PHASE0-UNIFIED.md`, root `STYLE_BIBLE.md` / `CARTOGRAPHY_STANDARDS.md` in Cursor-Game-Studios) **do not exist** there—the real CGS Phase 0 analogue is `Cursor-Game-Studios/00-osirisforge-game-studio-roadmap-and-phase-1.md` (local clone).

**One-sentence verdict:** **Go for engineering**, **no-go for “indistinguishable from Alexandria/Osiris voice”** until the critical gaps below are closed.

---

## 2. Category scores

| Category | Score | Justification |
| --- | ---: | --- |
| Overall structural fidelity | **6** | Core folders exist; missing CGS-style `scripts/`, generators, `.cursor/subagents/registry.json`, Phase operator manuals (`01-foreword…`, `02-phase-02…`), and 49/72 population. |
| ROADMAP style | **6** | Good ToC, phase tables, veto column; lacks Alexandria’s **program pulse**, **book spine enumeration**, **file naming law**, and **word-count bands**; Quantum Plaid table conflicts with Alexandria on quotes/NPC counts. |
| TASKLIST style | **5** | Correct header + sprint table shape; missing **Grok grade column discipline**, **dense Last Updated lineage**, **three-party instructions** block, **completed archive** usage. |
| Agent prompt quality | **6** | YAML frontmatter + HITL closer present; shorter than CGS **Phase 2** contracts—no `projectosiris_lane`, sensory hooks, skill affinities, anti-patterns, or merge key rigor on most files. |
| Rule files | **5** | HITL + density + FCoP + JSON stubs exist; **thin** vs CGS `.mdc` + missing Alexandria **`narrative-alexandria`** equivalent for `lore/**`; no `cursor-doc-sprawl` cousin. |
| Documentation density and voice | **5** | Professional; **not** Alexandria/Osiris **baroque** density (no “we are building a canon, not herding cats,” no machinery of anchors in STATUS/CHANGES). |
| MCP and schema integration | **7** | FastMCP stdio, tool names match spec, JSON Schema + pytest—**native enough**; missing `alexandria_gamestudio_entry_v1` / registry story from CGS roadmap and merge semantics. |
| Procedural and lore folder readiness | **6** | READMEs exist; **no** `MANIFEST.md` per pipeline, no numbered book folders, no Templates—acceptable for studio repo, **weak** vs Alexandria **lore** depth. |
| Human-in-the-loop and quality gates | **7** | `human-in-the-loop.mdc` always-on is strong; **Producer-as-veto** under-specified vs Alexandria **Grok ≥ 9.0** gate; silent edit ban stated but not wired to CI. |

**Weighted read:** the scaffold is a **credible Phase 1 skeleton**, not a **Phase 2 Necropolis**-grade operator manual.

---

## 3. Detailed findings

### 3.1 Overall structural fidelity

| File / area | Problem | Recommended fix |
| --- | --- | --- |
| Entire repo vs **Cursor-Game-Studios** | No `scripts/generate-osirisforge-studio.py`, `scripts/agent_phase2_data.py`, `scripts/skill_phase3_data.py`, `scripts/studio-health-check.py`, `tests/test_generator_contracts.py`, `.cursor/subagents/registry.json`. | Add **thin** `scripts/studio_health_stub.py` + `tests/test_repo_layout.py` asserting counts (agents ≥ N, rules ≥ M) until full generator lands. |
| Root vs CGS | CGS ships `00-osirisforge-game-studio-roadmap-and-phase-1.md`, `01-foreword-and-chapter-01-…`, phase manuals—**cursor-rpg** has no “Chapter 1” studio tome. | Add **`00-cursor-rpg-studios-roadmap-and-phase-1.md`** (or symlink content into `ROADMAP.md` §appendix) matching Osiris **voice + hygiene** section. |
| `docs/` | Alexandria `Alexandria_Unleashed/TASKLIST.md` states *`docs/` holds `index.md` only`*—cursor-rpg has `docs/cartography-standards.md`, `docs/hardware-runbook.md`, `docs/drafts/`, `docs/agents/`, now `docs/audits/`. | Either **embrace** multi-file `docs/` and **drop** the Alexandria-only rule for this repo (document in `README.md`), or **collapse** satellites into `docs/index.md` anchors + single appendices file per operator policy. |
| Reference brief | `ROADMAP-PHASE0-UNIFIED.md`, CGS root `STYLE_BIBLE.md` / `CARTOGRAPHY_STANDARDS.md` **not found** in Cursor-Game-Studios. | Update internal references to **actual** CGS paths (`00-osirisforge-…`, `quantum_plaid.md` at CGS root, `docs/unreal-mcp-self-hosted.md`). |

### 3.2 ROADMAP style

| File | Problem | Recommended fix |
| --- | --- | --- |
| [`ROADMAP.md`](../../ROADMAP.md) | **Quantum Plaid** row says **15** quotes and **12** NPCs; Alexandria `Alexandria_Unleashed/ROADMAP.md` contract says **12–15** quotes and **8–12** NPCs. | Add explicit **“Studio Gemini overlay”** footnote reconciling targets **or** align scaffold to Alexandria SSoT to avoid **dual canon**. |
| [`ROADMAP.md`](../../ROADMAP.md) | Missing **front matter / word count / ProjectOsiris** rows present in Alexandria phase contract. | Copy **row set** from Alexandria §Quantum Plaid (adapt labels for studio repo). |
| [`ROADMAP.md`](../../ROADMAP.md) | Index links `quantum_plaid.md` with anchor **`{#quantum-plaid-phase-contract}`** but heading slug may not match GitHub anchor generation when `{#…}` embedded. | Verify generated anchors; prefer **explicit HTML comment anchors** or **duplicate** plain heading. |

### 3.3 TASKLIST style

| File | Problem | Recommended fix |
| --- | --- | --- |
| [`TASKLIST.md`](../../TASKLIST.md) | **Instructions** block does not mirror Alexandria’s **Human / Cursor / Grok** contract, **Grok grade ≥ 9.0**, **never delete rows**. | Paste adapted **three-party** instructions; add **Grade** column if Grok used; else state **N/A** explicitly. |
| [`TASKLIST.md`](../../TASKLIST.md) | Sprint marks many items **Done** without external grade—fine for scaffolding, **violates** Alexandria discipline if copied literally. | Add footnote: “Scaffolding exception; manuscript tasks require Grok gate.” |
| [`TASKLIST.md`](../../TASKLIST.md) | **Last Updated** field is a **single date**, not Alexandria’s **rolling lineage** of anchors and file paths. | After first real manuscript sprint, switch to **dense** updates or accept **studio** brevity and link to `CHANGES.md`. |

### 3.4 Agent prompt quality

| File | Problem | Recommended fix |
| --- | --- | --- |
| [`.cursor/agents/directors/producer.md`](../../.cursor/agents/directors/producer.md) vs `Cursor-Game-Studios/.cursor/agents/directors/producer.md` | Missing **Phase 2** hooks (`phase_contract`, `projectosiris_lane`, **sensory line**, **semantic skill affinity**, **anti-patterns**, OsirisForge map-first notes). | Add **optional** YAML keys matching CGS even if values are `TBD`. |
| [`.cursor/agents/leads/lore-keeper.md`](../../.cursor/agents/leads/lore-keeper.md) | Strong mission; **no** worked example of **graph_traversal** payload format. | Add **fenced JSON example** (stub graph). |
| Multiple agents | **Tier 2/3 depth** uneven—**Narrative Director** and **Stat Block Engineer** are acceptable; others are **memo-length**. | Expand **one** lead and **one** specialist to **CGS paragraph density** as templates for Phase 2 regeneration. |

### 3.5 Rule files

| File | Problem | Recommended fix |
| --- | --- | --- |
| [`.cursor/rules/quantum-plaid-density.mdc`](../../.cursor/rules/quantum-plaid-density.mdc) | Strong content; **15 / 12** targets conflict with Alexandria ROADMAP (see §3.2). | Reconcile numbers; cite **authoritative** doc in-rule. |
| `.cursor/rules` vs CGS | CGS has **12** rules including `mcp-mutation-queue`, `postgis-sql`, `openclaw-heavy`, `security-secrets`—cursor-rpg has **4**. | Add **stub** `.mdc` files for **lore graph**, **timeline**, **cosmic-backfire** (paths aligned to future `vault/` or `lore/`), matching Gemini blueprint table. |
| Alexandria parity | No rule scoped to **`lore/**/*.md`** mirroring `Cursor-Game-Studios/.cursor/rules/narrative-alexandria.mdc`. | Add **`narrative-alexandria-studio.mdc`** → `lore/**/*.md` + `docs/drafts/**/*.md` with **graph_traversal** mandate. |

### 3.6 Documentation density and voice

| File | Problem | Recommended fix |
| --- | --- | --- |
| [`STATUS.md`](../../STATUS.md) | One short update—Alexandria **STATUS** is a **chronicle** with anchors, book IDs, Grok states. | For studio repo, either **own** minimalism or add **“pulse”** paragraph in Osiris tone. |
| [`CHANGES.md`](../../CHANGES.md) | Single unreleased bullet—fine; lacks **version** rhythm. | Keep **Unreleased**; add **target tag** when Phase 1 closes. |
| [`README.md`](../../README.md) | Relative link `../../Alexandria_Unleashed` **breaks** if repo is not a Dropbox sibling. | Document **`ALEXANDRIA_CANON_ROOT`** env var + example path. |
| [`quantum_plaid.md`](../../quantum_plaid.md) | Reads like a **summary**; Alexandria `Alexandria_Unleashed/docs/quantum_plaid.md` is a **full protocol** with grading table, workflow steps. | Either **vendor** a short excerpt with pointer or **increase** local density (grading rubric rows). |

### 3.7 MCP and schema integration

| File | Problem | Recommended fix |
| --- | --- | --- |
| [`mcp.json`](../../mcp.json) | Uses `"mcpServers"` wrapper—Cursor projects often expect **flat** server entries depending on merge target. | Document **exact merge** into `~/.cursor/mcp.json` with example **without** double nesting if needed. |
| [`data/schemas/alexandria_npc_entry_v1.schema.json`](../../data/schemas/alexandria_npc_entry_v1.schema.json) | Minimal schema—**no** derived-stat **validation** (HP vs ST) in schema; correct for JSON Schema limits, but **business rules** belong in Python (stub). | Add **`tools_logic.py`** checks for HP/Will/Per defaults **after** schema pass. |
| CGS `Cursor-Game-Studios/00-osirisforge-game-studio-roadmap-and-phase-1.md` | Defines **`alexandria_gamestudio_entry_v1` sketch** and studio operator voices. | Add **`data/schemas/alexandria_gamestudio_entry_v1.schema.json`** stub + MANIFEST row. |

### 3.8 Procedural and lore readiness

| Area | Problem | Recommended fix |
| --- | --- | --- |
| [`procedural/gis/README.md`](../../procedural/gis/README.md) | Points to cartography standards—**good**; no **sample** `geojson/` or `fixtures/`. | Add **`procedural/gis/examples/.gitkeep`** + one **fake** GeoJSON with CRS metadata block. |
| [`lore/alexandria-unbound/README.md`](../../lore/alexandria-unbound/README.md) | Pointer-only—**correct** to avoid canon fork. | Add **“do not edit canon here”** bold line + link to **Alexandria** `MANIFEST` hub. |
| Alexandria **book structure** | Numbered dirs `10-…`, `11-…`, `MANIFEST.md` per book—absent by design. | **No fix** unless this repo is meant to host lore; if yes, **wrong repo**. |

### 3.9 Human-in-the-loop and quality gates

| File | Problem | Recommended fix |
| --- | --- | --- |
| [`.cursor/rules/human-in-the-loop.mdc`](../../.cursor/rules/human-in-the-loop.mdc) | **Always apply**—excellent. | Add **exception list** (e.g., typo fixes in `README`) to avoid absurdity. |
| `Producer` / `Creative Director` | **Veto** language weaker than Alexandria **Grok** gate. | In `TASKLIST.md` + `STATUS.md`, name **who** may veto (Producer vs Creative) per phase. |
| CI | No **workflow** enforcing rules—**policy-only**. | Phase 1.5: **markdownlint** + **anchor** check + **JSON schema** in GitHub Actions. |

---

## 4. Critical gaps (blockers for “style-complete”)

| # | Gap |
| --- | --- |
| C1 | **Dual Quantum Plaid numbers** (15/12 vs 12–15 / 8–12) — **must** resolve before any chapter drafting. |
| C2 | **docs/ sprawl policy** vs Alexandria **index-only** note — pick **one** governance story. |
| C3 | **Missing** CGS-equivalent **registry / generator / health scripts** — structural parity claim is **incomplete**. |
| C4 | **Agent** prompts lack **CGS Phase 2** YAML richness — scaling to 49 agents will **not** match Osiris tone without a **template**. |
| C5 | **Reference path** `../../Alexandria_Unleashed` in [`README.md`](../../README.md) — fragile. |

---

## 5. Strengths

| # | Strength |
| --- | --- |
| S1 | **Root operational spine** (`ROADMAP`, `TASKLIST`, `STATUS`, `CHANGES`, `MANIFEST`, `quantum_plaid`, `STYLE_BIBLE`) matches the **intended Osiris/Alexandria dashboard** pattern. |
| S2 | **FCoP** queue [`docs/agents/status/README.md`](../../docs/agents/status/README.md) is **clear** and on-theme. |
| S3 | **MCP + pytest** proves the repo is **testable**—rare for a “docs” scaffold. |
| S4 | **`human-in-the-loop.mdc` always-on** is the **right** cultural circuit breaker. |
| S5 | **MANIFEST path table** mirrors CGS style and is **maintainable**. |

---

## 6. Final recommendation

| Gate | Result |
| --- | --- |
| **Go** for **continued tooling** (MCP Phases 3–4, skills, CI) | **Yes** |
| **No-go** for **starting Quantum Plaid manuscript drafts** in-repo until **C1** fixed and **TASKLIST** grading story defined | **Hold** |

---

## 7. Action items (priority order)

| P | Action | Owner |
| ---: | --- | --- |
| **P0** | Reconcile **Quantum Plaid** numeric targets with Alexandria `Alexandria_Unleashed/ROADMAP.md` or document **supersession** in [`quantum_plaid.md`](../../quantum_plaid.md) + [`ROADMAP.md`](../../ROADMAP.md) + `.mdc`. | Creative Director + Producer |
| **P0** | Replace fragile **relative** Alexandria path with **env var** + documented default in [`README.md`](../../README.md) and [`lore/alexandria-unbound/README.md`](../../lore/alexandria-unbound/README.md). | Producer |
| **P1** | Add **`TASKLIST.md`** **three-party** instructions + **grade / veto** column policy (even if Grok **TBD**). | Producer |
| **P1** | Add **studio Phase 0** markdown analogue to `Cursor-Game-Studios/00-osirisforge-game-studio-roadmap-and-phase-1.md` (local clone) (voice + hygiene + MCP inheritance tables). | Narrative + Producer |
| **P1** | Expand **one** director and **one** lead agent to **CGS Phase 2** depth; use as **templates** for generator. | Creative Director |
| **P2** | Add **stub** `.mdc` rules: lore graph, timeline, cosmic backfire, optional `cursor-doc-sprawl` variant. | Producer |
| **P2** | Add **`scripts/studio_health_check.py`** + layout tests; optional **`.cursor/subagents/registry.json`**. | Mechanics Director |
| **P2** | Add **`alexandria_gamestudio_entry_v1`** schema sketch per CGS roadmap. | Mechanics Director |
| **P3** | Decide **`docs/`** policy: **index-only** vs **structured subfolders**; update [`README.md`](../../README.md) waiver accordingly. | Producer |

---

## 8. Index

| Term | Location |
| --- | --- |
| Schwartz Mode | [`quantum_plaid.md`](../../quantum_plaid.md) |
| FCoP | [`docs/agents/status/README.md`](../../docs/agents/status/README.md) |

---

*End of audit — Phase 0.*
