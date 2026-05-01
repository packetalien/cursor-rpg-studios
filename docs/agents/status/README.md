# FCoP — `docs/agents/status/`

**File-based Coordination Protocol:** payloads are Markdown files whose **filenames route** work to the next agent.

## Naming pattern (examples)

| Stage | Filename |
| --- | --- |
| Concept handoff | `concept-to-narrative-director.md` |
| Approved downstream | `approved-to-world-architect.md` |
| Blocked | `blocked-pending-producer.md` |

## Rules

- One logical writer per target resource at a time.
- Collisions escalate to **Producer** (`/.cursor/agents/directors/producer.md`).
- Cursor rule: [`.cursor/rules/fcop-routing.mdc`](../../../.cursor/rules/fcop-routing.mdc).
