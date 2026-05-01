---
name: delegate-producer-merge-packet
description: Minimal merge packet shape for Producer — reader gates, forensic paths, attachments tree — for dual-layer + FCoP handoffs.
---

# Delegate — Producer Merge Packet

**Use this skill when:** handing work from **agents → Producer** or opening a merge-ready PR that touches **reader companions**, **forensic reports**, or **MCP-stubbed** lore checks.

**Normative:** [`.cursor/rules/output-organization.mdc`](../../rules/output-organization.mdc); [`dual-layer-content-generation`](../dual-layer-content-generation/SKILL.md).  
**Pairs with:** `forensic-output-compliance`, `request-human-override`.

---

## 1. Required fields (all non-empty when applicable)

| Field | Content |
| --- | --- |
| `reader_gates` | Result of `reader-template-enforcer` (pass/fail per gate) or link to validation report under `attachments/reports/`. |
| `attachments_paths` | Every new `attachments/drafts/*.md` and `attachments/reports/*.md` with forensic filenames. |
| `forensic_folder` | Root: `attachments/` (confirm tree matches `output-organization.mdc`). |
| `canonical_ssot` | Path(s) read for SSoT; note **read-only** if outside this repo. |
| `stub_tools_used` | If `graph_traversal` / `semantic_search_lore` invoked: include **`stub_notice`** / `_stub` acknowledgment + attestation status. |

---

## 2. Optional but high value

| Field | Content |
| --- | --- |
| `fcop_queue` | `docs/agents/status/` filename if routing a follow-up. |
| `risk_notes` | Invented crunch, STALE banners, anchor renames. |

---

## 3. Anti-patterns

- Omitting `attachments_paths` when files were written to `attachments/`.  
- Claiming “anchors verified” with only MCP search results.  
- Single wall-of-text PR body with no labeled fields — Producer should reject or bounce to this packet shape.
