# Security

## Reporting

Report suspected vulnerabilities through the repository owner’s preferred channel (private issue or encrypted mail). Do not post exploit details in public issues before a fix window.

## Content and IP

Do **not** commit full **Alexandria_Unleashed** manuscript trees, licensed third-party setting text, or other material you do not have the right to publish in **this** repository. Use pointers (`ALEXANDRIA_CANON_ROOT`, sibling clones) instead. If you are unsure about redistribution, obtain permission first.

## Threat model (studio)

- **MCP tool registry:** Treat every MCP server as **privileged code**. Compromise of a server or tool schema can expand filesystem and network reach; prefer **path allowlists** and **policy-as-code** for writes.
- **Prompt injection:** The LLM is an **untrusted** planner. **No silent auto-edits** to canonical lore; human approval gates for vault writes.
- **Secrets:** API keys and vault paths live in **`~/.secrets`** (key=value per line) or environment variables — **never** committed.

## lorevault-mcp posture (target state)

- **Just-in-time approval tokens** for destructive or additive writes to the Obsidian vault (stub until Phase 4).
- **Optimistic locking** when parallel agents touch the same faction or entity file (coordinated with FCoP).
- **Structured logging** without embedding full payloads that contain personal data.

## Dependencies

Run `pip-audit` / `uv pip audit` on `mcp-server` before production use; pin MCP SDK versions in lockfiles when introduced.

## Audit history

### 2026-05-01 — lorevault-mcp and repository surface

| Area | Result |
| --- | --- |
| **Secrets in tree** | No API keys, tokens, or `.env` bodies in tracked code; `mcp.json` uses workspace-relative paths only. |
| **Dangerous primitives** | No `pickle`, `eval`, `exec`, `subprocess` with `shell=True`, or unsafe `yaml.load` in application Python. |
| **lorevault-mcp** | Default transport is **stdio** (Cursor). Optional `streamable-http` binds **127.0.0.1:8000** — local development only; do not expose without TLS and auth. |
| **Input hardening** | `simulate_roll` caps dice **count** and **sides**; `graph_traversal` caps **depth** and string lengths; `semantic_search_lore` caps **query** length; `add_character_v1` rejects oversize or non-JSON-serializable payloads. |
| **Static analysis** | **Bandit** (`-ll`) on `mcp-server/src`: clean; `random` use is **TTRPG dice only** (documented `nosec B311`), not cryptography. |
| **Dependency audit** | **pip-audit** on an editable install of `mcp-server[dev]`: **mcp** / **jsonschema** transitive set had **no** reported CVEs at audit time; vulnerabilities reported against **pip** / **setuptools** inside disposable venvs are mitigated in **CI** by upgrading the installer stack before `pip install`. |
| **CI** | GitHub Actions `permissions: contents: read` only; checkout and setup-python from official actions. |

Residual risk: MCP servers remain **high-trust** local code; Phase 3+ backends must repeat threat modeling (path traversal, SSRF, auth on any HTTP surface).
