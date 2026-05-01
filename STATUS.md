# Project Status

## Current status

**On track — dual-layer reader pipeline proven on live Alexandria canon; studio mechanics hardened (2026-05-02).** Two Surgeon’s Grimoire **reader companion pilots** (Ch.01 + Ch.02) were drafted and machine-validated under `attachments/` (gitignored locally) with human Editorial/Producer close-out on Ch.01; contract is **[`docs/human-machine-dual-layer-pattern.md`](docs/human-machine-dual-layer-pattern.md) v1.0.3**. **GitHub Actions** runs `pytest -q` on push/PR to `main`/`master` ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)). **`lorevault-mcp`** remains a **stdio stub**: `semantic_search_lore` / `graph_traversal` return **sentinel** payloads (`_stub`, `stub_notice`) — they are **not** production vector/graph proof; attestation rules still apply ([`ROADMAP.md`](ROADMAP.md) Phases 3–4).

## Key metrics

| Metric | Value |
| --- | --- |
| Dual-layer pilots (validated) | Surgeon Ch.01 + Ch.02 reader drafts + validation reports under `attachments/` (see exemplar paths in dual-layer doc Sections 3 and 8) |
| Pytest | **11** passed + **1** skipped without `ALEXANDRIA_CANON_ROOT`; **12** passed when env points at sibling `Alexandria_Unleashed/lore/Alexandria-Unleashed` |
| CI | [`pytest`](.github/workflows/ci.yml) on `main` / `master` (fixtures-first; no canon secrets in repo) |
| MCP tools (stub) | `semantic_search_lore`, `graph_traversal`, `simulate_roll`, `add_character_v1` — graph/search **not** live backends |
| Agent tiers scaffolded | Tier 1–3 + Phase 1 deep prompts |
| Skill Batch 3 | **Held** — add **4–6** skills only after **named friction** from playtests or CI (not from 72-matrix inventory alone); see [`CHANGES.md`](CHANGES.md) `[Unreleased]` |
| Phase | **Phase 1 — reader pilot track complete**; MCP data plane + Skill Forge scale still per `ROADMAP.md` |

## Recent updates

- **2026-05-02:** Grok-assessment plan executed — Ch.01 human close-out + Ch.02 second pilot under `attachments/` (local forensic), `docs/human-machine-dual-layer-pattern.md` **v1.0.3**, GitHub Actions `pytest` CI, Skill Batch 3 gated pending friction (`CHANGES.md`).
- **2026-04-30:** GitHub ship prep — README onboarding, `docs/cursor-setup.md`, `LICENSE`, style-audit link hygiene, canon pointer env (`ALEXANDRIA_CANON_ROOT`).
- **2026-04-30:** Initial scaffolding: roadmap, tasklist, manifest, FCoP queue dir, MCP package stub, pytest wired.

## GM friction log (playtests)

Use one reader pilot (`attachments/drafts/…surgeon-ch01-reader-draft.md` or `…ch02-reader-draft.md`) at the table; append **dated** bullets after each session (voice, length, anchors, sensory covenant at table, etc.). Alternatively log under `attachments/misc/` with forensic filenames if you prefer not to commit notes.

- **2026-05-02:** *No playtest logged yet — template in place. Append bullets after first GM/solo session.*

## Known issues

- Slash-command skills (`/start-campaign`, …) deferred to **Phase 2 — Skill Forge** (see [`ROADMAP.md`](ROADMAP.md)).
- **MCP Apps** interactive sheets not yet built (Phase 8).
- **Skill Batch 3:** intentionally **empty** until friction is documented above or in `attachments/misc/` — do not pre-build from [`skills/00-skill-forge-matrix.md`](skills/00-skill-forge-matrix.md) alone.
