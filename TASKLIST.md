# TASKLIST — Cursor RPG Studios

## 1. Header

| Field | Value |
| --- | --- |
| **Project** | Cursor RPG Studios — *Alexandria Unbound* / GURPS 4e — lorevault-mcp + FCoP |
| **Overall health** | **On track** (scaffolding) |
| **Last updated** | 2026-04-30 — Phase 1 initialization |
| **Master roadmap** | [`ROADMAP.md`](ROADMAP.md) |

**Instructions:** Keep rows dated. Tick **Done** only after Producer review for scaffolding tasks; Grok/editor gates apply to manuscript rows when that program starts.

---

## 2. Current active sprint (Phase 1)

| Task | Status | Owner | Notes | Last updated |
| --- | --- | --- | --- | --- |
| Root docs (`ROADMAP`, `TASKLIST`, `STATUS`, `CHANGES`, `MANIFEST`, `quantum_plaid`, `STYLE_BIBLE`, `README`, `SECURITY`) | Done | Producer | Doc-surface waiver in `README.md` | 2026-04-30 |
| `.cursor/agents/` Tier 1–3 + Phase 1 deep prompts | Done | Creative / Mech | `narrative-director`, `lore-keeper`, `stat-block-engineer` | 2026-04-30 |
| `.cursor/rules/quantum-plaid-density.mdc` + companion `.mdc` stubs | Done | Producer | See rules dir | 2026-04-30 |
| `mcp-server/` stdio stub + root `mcp.json` | Done | Mechanics | Tools: search, graph, dice, add_character | 2026-04-30 |
| FCoP `docs/agents/status/` + procedural + hardware placeholders | Done | Producer | Naming README | 2026-04-30 |
| `pytest` smoke tests | Done | Producer | `tests/test_npc_schema.py`, `tests/test_mcp_tools.py` | 2026-04-30 |
| Operator validation: inspect `.mdc` globs | Pending | Human | Ensure `docs/drafts/**` only for density rule | — |
| Register MCP in Cursor; run `uv sync` / `pytest` locally | Pending | Human | Merge `mcp.json` fragment | — |

---

## 3. Next sprint (Phase 2 preview — Skill Forge)

- [ ] **S1:** Create `skills/00-skill-forge-matrix.md` expansion + first 8 onboarding skills (`/start-campaign`, `/import-system`, …).
- [ ] **S2:** Stub remaining skill files or generator script mirroring Osiris `skill_phase3_data.py` pattern.
- [ ] **S3:** Wire slash discovery in `.cursor/skills/README.md`.

---

## 4. Program checklist (phased)

### Phase A — Lorevault hardening

- [ ] **A1:** Chroma persistence path + embedding model choice — **Target:** TBD
- [ ] **A2:** SQLite + NetworkX graph schema — **Target:** TBD
- [ ] **A3:** Obsidian vault root env var + read-only ingest — **Target:** TBD

### Phase B — Quantum Plaid automation

- [ ] **B1:** Quote counter + NPC counter CI on `docs/drafts/`
- [ ] **B2:** Artifact value ≥ 80 backfire table linter

---

## 5. Completed archive

| Task | Completed | Notes |
| --- | --- | --- |
| — | — | — |
