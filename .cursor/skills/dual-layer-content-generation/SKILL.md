---
name: dual-layer-content-generation
description: Create and maintain reader companions per Human–Machine Dual-Layer Pattern (see docs header for version); no shadow canon; forensic drafts.
---

# Dual-Layer Content Generation

**Use this skill when:** drafting or revising **reader companions** (`*-reader.md`, human session layer), filling Surgeon-style reader passes, or validating a chapter’s human layer against Alexandria canonical SSoT.

**Normative source (locked):** [`docs/human-machine-dual-layer-pattern.md`](../../../docs/human-machine-dual-layer-pattern.md) **v1.0.2** (check file header for current).  
**Supporting rules:** [`.cursor/rules/output-organization.mdc`](../../rules/output-organization.mdc); Editorial Lead agent [`.cursor/agents/leads/editorial-lead.md`](../../agents/leads/editorial-lead.md).

---

## 1. Two layers (non-negotiable)

| Layer | Role | Ingest |
| --- | --- | --- |
| **Machine (canonical)** | `lore/…` in *Alexandria_Unleashed* — anchors, tables, JSON, Quantum Plaid | **Yes** — Tortuga / Osiris / validators |
| **Human (reader companion)** | Session surface — procedural, low choice paralysis | **No** — default out of ingest |

Never move “the real rules” into the reader file only. Never strip canonical density “for comfort.”

---

## 2. Five-section reader template (exact order)

After the title + header block, the companion **must** contain **only** these top-level sections, in this order (headings may keep parenthetical labels as written):

1. `## Start here (90 seconds)`
2. `## Run tonight (procedure)`
3. `## Worked example (canonical mechanics only)`
4. `## Anchor index (this chapter)`
5. `## Do not use for ingest`

**Header block (required):**

- Title line including `(reader companion)` and a stable `{#reader-…}` anchor.
- **Layer:** Human-readable companion — **not** for Project Tortuga / Osiris ingest.
- **Canonical source (SSoT):** exact path to **one** canonical `.md` file.

See dual-layer doc **Section 3** for the canonical skeleton copy-paste block.

---

## 3. No new mechanics (hard rules)

From **Section 2.2** — reader files **must not** introduce:

- New advantage costs, skill defaults not in canonical, invented DCs  
- Renamed or invented triage/system tags  
- New JSON schema keys or “helpful” house rules  

**Every** number, threshold, and procedure in **Run tonight** and **Worked example** must **cite** a canonical `{#anchor}` or table ID (`T-…`, `SO-…`, etc.). If it does not trace → **fix or remove**.

**Worked example:** exactly **one** path; no invented NPC stat blocks — cite canonical tables or “use row X of **T-…**”.

**Start here:** ≤ ~250 words; no net-new rules; at most **one** flagship anchor beyond orientation.

---

## 4. Forensic routing (drafts vs promotions)

| Stage | Where | Naming |
| --- | --- | --- |
| Scratch, Grok iterations, exploratory reader passes | `attachments/drafts/` | `YYYY-MM-DD_HH-MM_agent-or-purpose_short-descriptive-slug.md` |
| Formal companion ready for human PR (optional snapshot) | Still **drafts** until merged via normal git flow in Alexandria/cursor-rpg per repo policy | Same |
| **Promoted** studio norms (pattern tweaks, checklists) | `docs/` or root ops per charter | Plus **`CHANGES.md`** `[Unreleased]` line |

`attachments/` is **gitignored** — forensic material stays local until a human promotes text into tracked `docs/`. Do not commit raw multi-pass dumps to `docs/` without Producer + (if tone) Creative Director acknowledgment (see Editorial Lead + Producer agents).

---

## 5. Pre-merge checklist (reference)

Use Editorial Lead’s **10-row** reader checklist (canonical path: `editorial-lead.md` → **Pre-merge checklist**). Minimum gates:

- Five sections, correct order  
- Ingest ban string present (`Do not use for ingest` + Tortuga/Osiris/automation)  
- Anchor index ⊆ canonical anchors for that chapter  
- **Last synced:** or `reader_doc_rev` per dual-layer **Section 7**

---

## 6. Voice (dual-layer Section 6)

Reader = same **moral universe** as canonical, **shorter** sentences, **procedural** diction. **Do not** let sarcasm smuggle new facts. One grim hook in “Start here” is enough; the spine is **Run tonight**.

---

## 7. Example (fragment)

**Bad:** “Roll 3d6 vs a new DC 14 I invented for triage stress.”  
**Good:** “Roll reaction per `{#surgeons-ch01-tables}` **T-SG102** crimson row; command consequence as printed.”

---

## 8. Integration summary

| Document / rule | Use |
| --- | --- |
| `docs/human-machine-dual-layer-pattern.md` | Contract, Sections 2–7, lock statement |
| `.cursor/rules/output-organization.mdc` | Where drafts live on disk |
| `editorial-lead` agent | Veto authority, merge gates, MCP posture |

When unsure: **machine layer wins** for truth; **human layer wins** for *how to run tonight’s session* without inventing rules.

---

## 9. Execution chain (use with sibling skills)

| Step | Skill |
| --- | --- |
| 1 | This skill — draft reader content |
| 2 | `reader-template-enforcer` — validate headings + checklist |
| 3 | `anchor-validation-sync` — cite only anchors that exist in canonical |
| 4 | `stub-aware-graph-handling` — if using MCP graph/search |
| 5 | `forensic-output-compliance` — save drafts under `attachments/drafts/` |
