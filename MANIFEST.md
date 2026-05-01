# MANIFEST — Cursor RPG Studios

| Path | Role |
| --- | --- |
| `README.md` | Project overview, doc-surface waiver note, quick links |
| `ROADMAP.md` | Phases 0–10, Quantum Plaid, exit criteria |
| `TASKLIST.md` | Living sprint / program checklist |
| `STATUS.md` | Health and recent updates |
| `CHANGES.md` | Changelog |
| `SECURITY.md` | MCP + secret handling policy |
| `LICENSE` | MIT — project license |
| `MANIFEST.md` | This file — path index |
| `quantum_plaid.md` | Density rubric and studio overlays |
| `STYLE_BIBLE.md` | Voice, cartography, sensory covenant hooks |
| `.cursor/agents/directors/*.md` | Tier 1 — Opus-class directors |
| `.cursor/agents/leads/*.md` | Tier 2 — department leads |
| `.cursor/agents/specialists/*.md` | Tier 3 — execution specialists |
| `agents/README.md` | Human index of agent paths (mirrors `.cursor/agents`) |
| `.cursor/rules/*.mdc` | Path-scoped enforcement (Quantum Plaid, FCoP, JSON, HITL, output organization) |
| `.cursor/rules/output-organization.mdc` | Forensic `attachments/` naming + tree (active; alwaysApply) |
| `.cursor/rules/output-organization-universal.mdc` | Same standard for copying to other repos (reference; alwaysApply false) |
| `attachments/` | Local-only agent outputs (gitignored); see README **Output Organization** |
| `.cursor/skills/README.md` | Skill Forge pointer + core skills index |
| `.cursor/skills/dual-layer-content-generation/SKILL.md` | Reader companion playbook (`docs/human-machine-dual-layer-pattern.md`) |
| `.cursor/skills/forensic-output-compliance/SKILL.md` | `attachments/` naming + promotion playbook |
| `.cursor/skills/reader-template-enforcer/SKILL.md` | Five-section reader checklist enforcer |
| `.cursor/skills/anchor-validation-sync/SKILL.md` | Reader cites vs canonical `rg`; STALE/drift |
| `.cursor/skills/stub-aware-graph-handling/SKILL.md` | Stub lorevault MCP (`_stub` / `stub_notice`); LORE_STUB_ATTESTATION |
| `.cursor/skills/schwartz-mode-pass/SKILL.md` | Restraint pass on reader companions (Schwartz density) |
| `.cursor/skills/check-anchor-links/SKILL.md` | rg-first anchor/table sweep before full sync |
| `.cursor/skills/request-human-override/SKILL.md` | Escalation packet for Producer / Editorial |
| `.cursor/skills/delegate-producer-merge-packet/SKILL.md` | Merge packet field checklist |
| `.cursor/skills/ci-reader-template-smoke/SKILL.md` | pytest reader template + anchor subset smoke |
| `tests/reader_template_checks.py` | Shared validators for reader template + anchor subset |
| `tests/fixtures/*.md` | Reader + canonical excerpts for template/anchor tests |
| `skills/00-skill-forge-matrix.md` | Nine production phases × example slash commands |
| `docs/index.md` | Link hub (no prose duplication) |
| `docs/cursor-setup.md` | Cursor + MCP + env deep setup (GitHub-safe paths) |
| `docs/cursor-install.md` | Short pointer to setup + README quick path (`install` search aid) |
| `docs/human-machine-dual-layer-pattern.md` | Canonical vs reader companion studio contract |
| `docs/audits/style-audit-phase0.md` | Phase 0 Schwartz / style gate report vs Alexandria + OsirisForge |
| `docs/drafts/**/*.md` | Draft manuscript staging (`quantum-plaid-density.mdc` scoped) |
| `docs/agents/status/*.md` | FCoP filename-as-routing queue |
| `docs/cartography-standards.md` | CRS/datum discipline placeholder |
| `docs/hardware-runbook.md` | OpenClaw / operator paths placeholder |
| `.github/workflows/ci.yml` | GitHub Actions — install `mcp-server[dev]`, run `pytest -q` |
| `mcp-server/` | **lorevault-mcp** Python package (stdio) |
| `mcp.json` | Cursor MCP config fragment (merge into user/project config) |
| `data/schemas/alexandria_npc_entry_v1.schema.json` | NPC JSON schema stub |
| `lore/alexandria-unbound/README.md` | Pointer to sibling Alexandria canon repo |
| `procedural/roads/`, `settlements/`, `gis/`, `datum/` | Procedural pipeline placeholders |
| `hardware/README.md` | OpenClaw job types / machine roles placeholder |
| `tests/` | `pytest` — schema + tool stubs |
| `pytest.ini` | Root pytest config + `pythonpath` for `lorevault_mcp` and `tests` helpers |
| `.gitignore` | Python, venv, local DB/Chroma patterns |

## External canon (not vendored)

| Path | Role |
| --- | --- |
| `../Alexandria_Unleashed/lore/Alexandria-Unleashed/` | Canonical *Alexandria Unbound* Markdown SSoT (operator machine) |
