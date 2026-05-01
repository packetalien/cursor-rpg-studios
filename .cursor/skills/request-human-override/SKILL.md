---
name: request-human-override
description: Escalation playbook when machine gates fail, MCP is stubbed, or “invented rule?” — Producer merge packet fields.
---

# Request Human Override

**Use this skill when:** `reader-template-enforcer` reports **FAIL**, anchor checks disagree, **LORE_STUB_ATTESTATION** is missing, or Editorial Lead flags **invented rule?**

**Normative:** [`forensic-output-compliance`](../forensic-output-compliance/SKILL.md); Producer merge policy in repo rules.  
**Pairs with:** `delegate-producer-merge-packet`, `stub-aware-graph-handling`.

---

## 1. Stop conditions (do not self-merge)

- Template **10/10** not green and you lack canonical authority to edit SSoT.  
- Safety story depends on **`graph_traversal` / `semantic_search_lore`** without human attestation.  
- Dual-layer **promotion** crosses Alexandria boundary without maintainer approval.

---

## 2. Packet block (paste into FCoP / PR)

Use verbatim labels so Producer can grep packets:

```text
HUMAN_OVERRIDE_REQUEST
reason: <template_fail | anchor_drift | stub_dependent_claim | invented_rule | scope_ambiguous>
blocked_gates: <list reader_template_enforcer gate ids or "anchor_sync">
proposed_fix: <one paragraph — human applies or rejects>
attachments_paths: <list forensic paths under attachments/>
reader_gates: <pass|fail + notes>
forensic_folder: attachments/reports/
```

---

## 3. Owner routing

| Reason | Default owner |
| --- | --- |
| invented_rule / tone | Editorial Lead |
| anchor_drift / canonical edit | Lore Keeper + Editorial |
| stub_dependent_claim | Lore Keeper attestation |
| template only | Producer (fast path) |

---

## 4. Resume criteria

Continue automation only after a **human** replies in-thread with **OVERRIDE_APPROVED** or supplies a **canonical patch** / **reader fix** you can apply without guessing.
