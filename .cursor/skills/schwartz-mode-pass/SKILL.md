---
name: schwartz-mode-pass
description: Tight editorial pass on reader companions — restraint, no invented crunch; Schwartz-style density without expanding scope.
---

# Schwartz-Mode Pass (reader companions)

**Use this skill when:** a reader companion draft reads **fluffy**, **marketing-heavy**, or **adds mechanics** not present in the paired canonical file.

**Normative:** [`docs/audits/style-audit-phase0.md`](../../../docs/audits/style-audit-phase0.md) (Schwartz gate); [`docs/human-machine-dual-layer-pattern.md`](../../../docs/human-machine-dual-layer-pattern.md) Section 2.2 (no orphan mechanics).  
**Pairs with:** `reader-template-enforcer`, `dual-layer-content-generation`.

---

## 1. Hard stops

- **No new DCs, tags, or table rows** not verbatim in canonical. If the draft “helpfully” adds numbers → delete or replace with “cite canonical cell.”
- **No lorevault search/graph as proof** of tone or absence — use human read or `rg` on canonical only.

---

## 2. Pass checklist (10–15 minutes)

| Check | Action |
| --- | --- |
| Opening | **Start here** ≤ ~120 words; one sharp promise, no series recap. |
| Procedure | **Run tonight** steps cite `{#anchors}` / `T-…` only; each step traceable to canonical text. |
| Example | **Worked example** uses printed columns only; flag “invented rule?” for Editorial Lead. |
| Ingest ban | **Do not use for ingest** repeats Tortuga / Osiris / automation. |

---

## 3. Output

Paste into PR comment:

```markdown
## Schwartz-mode pass
| Issue | Resolution |
| --- | --- |
| (line / section) | tightened / removed / cited |
```

If any **hard stop** cannot be fixed without canonical change → **`request-human-override`** and hold merge.
