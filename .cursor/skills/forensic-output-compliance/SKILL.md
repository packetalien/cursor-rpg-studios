---
name: forensic-output-compliance
description: Route agent-generated audits, reports, and logs under attachments/ with mandatory naming; promotion to docs/ via CHANGES.
---

# Forensic Output Compliance

**Use this skill when:** writing **any** agent-generated audit, status report, review, scratch draft, or raw prompt/response log in cursor-rpg-studios — before saving to disk or handing off to a human.

**STOP:** Do not save formal audits/reports under `docs/` or repo root without promotion + `CHANGES.md` (see Section 4).

**Normative source (locked):** [`.cursor/rules/output-organization.mdc`](../../rules/output-organization.mdc) **v1.0**.  
**Ops alignment:** Producer agent [`.cursor/agents/directors/producer.md`](../../agents/directors/producer.md) (forensic routing + merge packet `attachments_paths`).

---

## 1. Mandatory naming format

Every forensic file name **must** match:

```text
YYYY-MM-DD_HH-MM_agent-or-purpose_short-descriptive-slug.md
```

| Segment | Rule |
| --- | --- |
| `YYYY-MM-DD` | ISO date (local or agreed studio TZ) |
| `HH-MM` | 24-hour clock, zero-padded |
| `agent-or-purpose` | Lowercase, hyphens; e.g. `editorial-lead`, `c1-audit`, `grok-reader-pass` |
| `short-descriptive-slug` | Lowercase, hyphens; no spaces |

**Examples:**

- `2026-05-01_14-30_editorial-lead_surgeon-ch01-reader-draft-v2.md` → `attachments/drafts/`  
- `2026-05-01_10-36_cursor_auditor_agent-system-review.md` → `attachments/reports/`  
- `2026-05-01_09-15_style-audit_phase0-schwartz-notes.md` → `attachments/audits/`

---

## 2. Folder rules (`attachments/` tree)

All agent outputs live under **`attachments/`** (repo **gitignored**). Use **one** primary folder per artifact:

| Folder | Contents |
| --- | --- |
| `attachments/audits/` | Formal audits, Schwartz gates, structured quality reviews |
| `attachments/reports/` | Status reports, inventories, C1/C2 assessments, architecture reviews |
| `attachments/drafts/` | Working drafts, multi-iteration LLM output, exploratory reader passes |
| `attachments/agent-logs/` | Raw prompt + response pairs (highest forensic value) |
| `attachments/misc/` | Everything that does not fit above (sparingly) |

**Do not** park formal audits in `reports/` or vice versa if the distinction matters for later mining — when ambiguous, prefer **`reports/`** for narrative assessments and **`audits/`** for pass/fail gate documents.

---

## 3. Compliance header (reports and audits)

For **structured human-facing reports** (especially `audits/` and `reports/`), include **line 1** as a blockquote so operators see compliance at a glance:

```markdown
> **This report was generated in compliance with the Output Organization Rule (v1.0).**
```

Optional second line (studio habit):

```markdown
> File saved to `attachments/<folder>/` per forensic standards.
```

**Drafts** (`attachments/drafts/`) may omit the blockquote if the file is throwaway scratch — but naming convention still applies.

---

## 4. Promotion process to `docs/`

Tracked documentation lives in **`docs/`** (or designated root ops files). **Promotion** from `attachments/` is **manual** and requires:

1. **Human decision** that the text is normative or worth versioning in git.  
2. **Edit or paste** into the target `docs/…` or root file (never bulk-commit `attachments/`).  
3. **`CHANGES.md`** — append one line under `[Unreleased]` describing what was promoted.  
4. **Tone-bearing norms:** Producer + Creative Director acknowledgment on the PR when policy changes (per Producer / Editorial Lead alignment).

**Reject** landing formal audits directly in `docs/` without going through promotion + `CHANGES.md`.

---

## 5. Merge packets (Producer integration)

When a session creates forensic files, the merge / handoff packet should list:

- `attachments_paths`: array of full paths or repo-relative paths under `attachments/`  
- `forensic_folder`: one of `audits` | `reports` | `drafts` | `agent-logs` | `misc`

---

## 6. Quick checklist before save

| # | Check |
| ---: | --- |
| 1 | Path is under `attachments/<subfolder>/` |
| 2 | Filename matches `YYYY-MM-DD_HH-MM_…slug.md` |
| 3 | Subfolder matches artifact type (Section 2) |
| 4 | Reports/audits have compliance header (Section 3) when appropriate |
| 5 | No secrets or `.env` content in forensic files |

---

## 7. Cross-links

| Resource | Role |
| --- | --- |
| `.cursor/rules/output-organization.mdc` | Locked rule text |
| `docs/human-machine-dual-layer-pattern.md` | Dual-layer; reader vs canonical when content touches both |
| `CHANGES.md` | Promotion log |
