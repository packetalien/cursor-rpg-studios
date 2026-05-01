---
name: check-anchor-links
description: Fast rg-first anchor and table-ID sweep before full anchor-validation-sync; copy-paste recipes for CI-minded humans.
---

# Check Anchor Links (quick sweep)

**Use this skill when:** you want a **fast** mechanical check before running the full **`anchor-validation-sync`** pass or opening a PR.

**Normative:** [`anchor-validation-sync`](../anchor-validation-sync/SKILL.md) (authoritative procedure).  
**Pairs with:** `reader-template-enforcer`, `stub-aware-graph-handling` (do not substitute `rg` with MCP search).

---

## 1. Preconditions

- Reader path and canonical path from reader header **Canonical source (SSoT):** resolved on disk (or `ALEXANDRIA_CANON_ROOT` + relative tail).

---

## 2. Recipes (repo root, zsh/bash)

**List every `{#…}` in reader (skip title line manually if it is a `reader-…` id):**

```bash
rg -o '\{#([^}]+)\}' path/to/reader.md
```

**Confirm each anchor string exists in canonical:**

```bash
CANON="path/to/canonical.md"
rg -o '\{#([^}]+)\}' path/to/reader.md | while read -r line; do
  raw="${line#\{#}"; raw="${raw%\}}"
  rg -F "{#$raw}" "$CANON" -q || echo "MISSING: {#$raw}"
done
```

**Table IDs (`T-XX###`):**

```bash
rg -o '\bT-[A-Z]{2,}[0-9]+\b' path/to/reader.md | sort -u | while read -r tid; do
  rg -F "$tid" "$CANON" -q || echo "MISSING TABLE: $tid"
done
```

---

## 3. When clean

Escalate to **`anchor-validation-sync`** for STALE/drift wording and PR table format.

When dirty → fix reader or canonical per dual-layer promotion rules (studio vs Alexandria scope).
