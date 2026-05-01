---
name: stub-aware-graph-handling
description: Safe behavior when lorevault graph_traversal / semantic_search_lore are stubbed (sentinel or legacy empty); human attestation; no false canon claims.
---

# Stub-Aware Graph Handling

**Use this skill when:** calling **`graph_traversal`** or **`semantic_search_lore`** from lorevault-mcp in **Phase 1–2** (stub backends: sentinel payloads with `_stub` / `stub_notice`, or legacy empty arrays).

**Normative:** [`.cursor/agents/leads/lore-keeper.md`](../../agents/leads/lore-keeper.md) **Stub mode** section; [`docs/human-machine-dual-layer-pattern.md`](../../../docs/human-machine-dual-layer-pattern.md) (do not treat reader as canon).  
**Rule:** Empty MCP output **proves nothing** about lore safety or precedent.

---

## 1. Detect stub response

| Tool | Stub signal |
| --- | --- |
| `graph_traversal` | `stub_notice` present; and/or every `nodes[]` item has `_stub: true`; or **legacy** `nodes` length 0 |
| `semantic_search_lore` | `stub_notice` present; and/or `matches[0]._stub === true`; or **legacy** empty `matches` |

**Sentinel payloads are still not canon.** They only prevent mistaking “empty JSON” for “verified empty lore.”

If **any** stub signal → apply **Sections 2–4** below before claiming continuity.

---

## 2. Forbidden claims (STOP)

Never output:

- “Graph confirms no conflicts.”  
- “Search found no precedent.”  
- “Canon allows this retcon” **based solely** on empty MCP payload.

Replace with: **“MCP returned empty; human review required for graph/search claims.”**

---

## 3. Mandatory human attestation (PR packet)

When stub mode applies, the review packet **must** include (verbatim structure from Lore Keeper):

```text
LORE_STUB_ATTESTATION: graph_traversal / semantic_search_lore returned stub sentinel, empty, or minimal results.
Human graph/search review performed by: <name>
Date: <YYYY-MM-DD>
Scope checked: <entities / chapters / search queries>
```

Until filled by a **human**, **Editorial Lead** / **Producer** should **hold merge** on PRs whose safety story depends only on those tool calls.

---

## 4. What agents should do instead

| Need | Action |
| --- | --- |
| Anchor exists in chapter | **Text** `rg` in canonical `.md` — use `anchor-validation-sync` skill |
| Continuity / factions | Human Lore review + attestation block |
| Tone precedent | Human or full-text read of canonical prose — not empty search |

---

## 5. Example (good vs bad)

**Bad:** “Ran `graph_traversal('FACTION-X', 2)` — no edges, so FACTION-X is isolated.”  
**Good:** “`graph_traversal` returned stub sentinel (`_stub` / `stub_notice`). LORE_STUB_ATTESTATION required before asserting faction isolation. Suggest `rg` canonical chapter for FACTION-X string hits.”

---

## 6. Role owners

| Role | Responsibility |
| --- | --- |
| **Lore Keeper** | Insists on attestation; owns graph narrative when live DB exists |
| **Editorial Lead** | Does not merge reader that cites graph “proof” from empty calls |
| **Producer** | Merge packet lists whether stub attestation present |

---

## 7. When this skill expires

Update or retire strict stub language when **ROADMAP** Phases 3–4 deliver live Chroma/SQLite graph + search — then re-verify tool payloads before loosening wording.
