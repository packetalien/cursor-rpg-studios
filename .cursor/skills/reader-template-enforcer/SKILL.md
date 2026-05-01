---
name: reader-template-enforcer
description: Validate reader companion Markdown against dual-layer Section 3 five-section template and Editorial Lead pre-merge checklist.
---

# Reader Companion Template Enforcer

**Use this skill when:** reviewing a `*-reader.md` (or equivalent human-layer file) before merge, or after an LLM fill pass.

**Normative:** [`docs/human-machine-dual-layer-pattern.md`](../../../docs/human-machine-dual-layer-pattern.md) **Section 3**, **Section 2.2**, **Section 7**; [`.cursor/rules/output-organization.mdc`](../../rules/output-organization.mdc) for where drafts live.  
**Agent:** [`.cursor/agents/leads/editorial-lead.md`](../../agents/leads/editorial-lead.md) — **Pre-merge checklist** table.

---

## 1. Required heading sequence (fail = block)

Scan **top-level** `##` headings **after** the YAML/title/header block. They **must** appear **exactly once each**, in this order, with this text (parentheticals allowed as written):

| # | Required `##` heading |
| ---: | --- |
| 1 | `Start here (90 seconds)` |
| 2 | `Run tonight (procedure)` |
| 3 | `Worked example (canonical mechanics only)` |
| 4 | `Anchor index (this chapter)` |
| 5 | `Do not use for ingest` |

**Pass:** five headings, no extras between them, no renamed sections.  
**Fail:** missing section, duplicate section, wrong order, or extra top-level `##` that breaks the contract.

---

## 2. Header block (fail = block)

Before section 1, confirm:

- [ ] Line contains `(reader companion)` and `{#reader-…}` style anchor (dual-layer Section 3).
- [ ] **Layer:** states human companion and **not** for Tortuga/Osiris ingest.
- [ ] **Canonical source (SSoT):** one path to **one** `.md` canonical file.

---

## 3. Ten-gate checklist (Editorial Lead)

| Gate | Pass criterion |
| ---: | --- |
| 1 | Five sections, order, heading text |
| 2 | Layer + Canonical source lines present |
| 3 | `Do not use for ingest` mentions Tortuga, Osiris, **and** automation ingest ban |
| 4 | **Start here** word count ≤ ~250; no new mechanics (spot-check) |
| 5 | **Run tonight:** each step that rolls or sets difficulty has `{#…}` or `T-…` / seed ID |
| 6 | **Worked example:** reads as **one** scenario path |
| 7 | **Anchor index:** only `{#…}` tokens; no obvious fan-out to whole-book ToC |
| 8 | No Section 2.2 forbidden content (invented costs, DCs, tags, JSON) |
| 9 | **Last synced:** date or `reader_doc_rev` in header or **Do not use for ingest** footer |
| 10 | If file was agent-drafted, companion scratch lived under `attachments/drafts/` until PR |

Output a **table** `Gate | Pass/Fail | Notes` for human sign-off.

---

## 4. Common failures (fix these first)

| Symptom | Fix |
| --- | --- |
| `## Session prep` inserted as extra section | Remove or fold into **Run tonight** |
| Ingest ban only says “not for ingest” | Add Tortuga + Osiris + automation explicitly |
| Two worked examples | Merge into **one** path or split PR scope |
| Anchor index lists 80 anchors | Trim to session subset per dual-layer Section 2.3 |

---

## 5. Example output (snippet)

```text
Gate 1: PASS — headings H2 order matches Section 3
Gate 3: FAIL — Do not use for ingest missing "automation"
Gate 9: FAIL — no Last synced line
```

---

## 6. Who uses this

- **Editorial Lead** — primary enforcer.  
- **Producer** — may require `reader_gates` table in merge packet before approving reader PR.
