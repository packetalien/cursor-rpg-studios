---
name: anchor-validation-sync
description: Verify reader-cited {#anchors} and table IDs exist in paired canonical file; flag STALE/drift per dual-layer Section 2.3 Section 7.
---

# Anchor Validation and Sync

**Use this skill when:** validating **Run tonight**, **Worked example**, or **Anchor index** in a reader companion against its **Canonical source (SSoT)** file.

**Normative:** [`docs/human-machine-dual-layer-pattern.md`](../../../docs/human-machine-dual-layer-pattern.md) **Section 2.3** (sync), **Section 7** (drift / STALE), **Section 2.2** (no orphan mechanics).  
**Pairs with:** `reader-template-enforcer`, `dual-layer-content-generation`.

---

## 1. Inputs

| Input | Source |
| --- | --- |
| Reader file | Path from working tree |
| Canonical file | Exact path from reader header **Canonical source (SSoT):** |

If canonical path is missing or ambiguous → **STOP** (template enforcer fail).

---

## 2. Extract citations from reader

Collect all tokens matching:

- `` `{#word…}` `` or `{#…}` in inline text  
- Table refs like `T-SG101`, `T-HCB12` (regex `\bT-[A-Z]{2,}[0-9]+\b` or project table prefix)  
- Seed IDs if used (`SO-…`, `MC-…` per book convention)

Ignore code fences that are examples *about* anchors unless they claim to be live cites.

---

## 3. Validate against canonical (mechanical)

For each `{#anchor}`:

1. Open canonical file (or `rg '\{#anchor\}' canonical.md'`).  
2. **Pass:** at least **one** defining occurrence in **that** canonical file (dual-layer sync test: prefer single authoritative definition per anchor in chapter file).  
3. **Fail:** zero matches → **remove cite**, **fix typo**, or **update canonical first** (machine layer owns truth).

For each `T-…` ID:

1. `rg 'T-…' canonical.md`  
2. **Fail** if absent → reader must not reference that row.

---

## 4. STALE and drift (human + machine)

**STALE banner** (dual-layer Section 2.3) — reader top must include if canonical moved under reader:

```markdown
**STALE:** Canonical `{#old-anchor}` split; see issue <URL>. Last verified: YYYY-MM-DD.
```

**When to require STALE or block merge:**

- Canonical PR renamed/split anchors cited by reader **without** reader update in same release.  
- Table numbers renumbered (`T-SG101` → removed).  
- JSON keys in canonical chapter changed and reader **Worked example** still cites old keys.

**Producer / Editorial:** do not merge reader until STALE is resolved or reader is updated.

---

## 5. Output format (paste into PR)

```markdown
## Anchor validation summary
| Cite | In canonical? | Notes |
| --- | --- | --- |
| `{#surgeons-ch01-tables}` | yes | |
| `{#fake-anchor}` | **no** | Remove or fix |
```

---

## 6. Stub tooling note

If you used `graph_traversal` only to “validate” anchors — **do not**. Anchor check is **text search in canonical file**. For graph-dependent *relationship* claims, use **`stub-aware-graph-handling`** skill.

---

## 7. Lore Keeper / Editorial handoff

- **Lore Keeper** — graph truth, faction edges (when not stub).  
- **Editorial Lead** — reader presentation; you supply the summary table for `reader_gates`.
