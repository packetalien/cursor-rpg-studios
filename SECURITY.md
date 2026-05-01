# Security

## Reporting

Report suspected vulnerabilities through the repository owner’s preferred channel (private issue or encrypted mail). Do not post exploit details in public issues before a fix window.

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
