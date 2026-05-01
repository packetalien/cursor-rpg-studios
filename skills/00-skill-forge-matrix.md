# Skill Forge matrix — Cursor RPG Studios (stub)

Nine **production phases** from the architectural blueprint; representative slash commands (72 total deferred to Phase 2).

| Production phase | Example skill playbooks | MCP / notes |
| --- | --- | --- |
| 1. Onboarding | `/start-campaign`, `/import-system`, `/adopt-vault`, `/initialize-graph`, `/parse-manifest`, `/set-tone-mandate`, `/establish-factions`, `/define-physics` | Seed Chroma/SQLite from Obsidian (Phase 3+) |
| 2. Worldbuilding | `/team-worldbuild`, `/generate-geography`, `/map-economy`, `/build-city-node`, `/draft-history`, `/simulate-weather`, `/place-artifacts`, `/audit-borders` | `graph_traversal` for territory collisions |
| 3. Character | `/forge-npc`, `/build-relationship-graph`, `/audit-motivations`, `/generate-ancestry`, `/assign-quirks`, `/draft-dialogue`, `/link-nemesis`, `/verify-npc-count` | `add_character_v1` |
| 4. Narrative | `/team-narrative`, `/draft-sensory-covenant`, `/inject-quotes`, `/weave-subplot`, `/write-readaloud-text`, `/escalate-tension`, `/draft-clues`, `/audit-horror-tone` | Voice Matcher affinity |
| 5. Mechanics | `/team-mechanics`, `/validate-gurps-math`, `/forge-loot-table`, `/scale-encounter`, `/apply-armor-divisor`, `/calculate-mass-combat`, `/generate-hazards`, `/audit-spells` | `simulate_roll`, validators |
| 6. Polish | `/audit-canon`, `/schwartz-mode-pass`, `/format-tables`, `/verify-phase-bridges`, `/eradicate-ai-slop`, `/balance-economy`, `/check-anchor-links`, `/generate-glossary` | Editorial Lead |
| 7. Playtest | `/simulate-combat`, `/run-monte-carlo`, `/test-skill-checks`, `/audit-backfire-rates`, `/stress-test-economy`, `/log-casualties`, `/verify-stealth-mechanics`, `/triage-bugs` | Deterministic dice oracle |
| 8. Publish | `/export-vtt`, `/generate-pdf`, `/build-manifest`, `/compile-json`, `/sync-obsidian`, `/update-changelog`, `/create-handouts`, `/finalize-release` | Foundry/Roll20 exporters |
| 9. Orchestration | `/delegate`, `/escalate`, `/resolve-conflict`, `/route-file`, `/merge-status`, `/clear-queue`, `/request-human-override`, `/halt-pipeline` | FCoP filenames |

## Next step

Phase 2 generator or hand-authored `SKILL.md` files under `.cursor/skills/` with semantic routing hints.
