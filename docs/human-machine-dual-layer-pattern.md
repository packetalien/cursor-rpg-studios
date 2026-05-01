# Human–machine dual-layer pattern — Cursor RPG Studios

**Version:** 1.0.2  
**Status:** Canonical studio standard (contract)  
**Last updated:** 2026-05-02  
**Aligns with:** [`quantum_plaid.md`](../quantum_plaid.md), Alexandria *Reader-facing manuscript program* (see `Alexandria_Unleashed/ROADMAP.md` when that repo is cloned locally — [Canon path](cursor-setup.md#alexandria_canon_root)), [`STYLE_BIBLE.md`](../STYLE_BIBLE.md).

---

## Table of contents

- [1. Executive summary](#1-executive-summary)
- [2. Core contract](#2-core-contract)
- [3. Reader companion template](#3-reader-companion-template-mandatory-structure)
- [4. Canonical file human affordances](#4-canonical-file-human-affordances-minimal)
- [5. Mechanical generation strategy](#5-mechanical-generation-strategy)
- [6. Voice and tone guidelines](#6-voice-and-tone-guidelines)
- [7. Maintenance rules](#7-maintenance-rules)
- [8. Examples](#8-examples-reference-surgeon-grimoire-ch01)
- [9. Future application](#9-future-application-agents-skills-enforcement)
- [10. Lock statement](#10-lock-statement)

---

## 1. Executive summary

**Cursor RPG Studios** ships two **non-interchangeable** layers for every major manuscript unit: the **machine layer** (canonical Markdown under `lore/…` in *Alexandria_Unleashed*, or future canonical roots) remains the **single source of truth** for `{#anchors}`, numbered tables, stat blocks, JSON fragments, phase bridges, and Quantum Plaid density—**nothing is removed, dumbed down, or “simplified away”** for comfort. The **human layer** (reader companion files) is a **session surface**: procedural, enjoyable, low **choice paralysis**, optimized for **one sitting** at the table or one night of prep. The machine layer **feeds** tooling (Tortuga, ProjectOsiris, lorevault-mcp, validators); the human layer **feeds** GMs’ working memory. **Ingest, indexing, and canon law always follow the machine layer.** Reader companions are **explicitly out of ingest** unless maintainers promote them—a promotion that must be **documented** and **versioned**.

**Pedagogical debt (external analysis):** Commercial GURPS *Basic Set* Ch.1 and *Bio-Tech* Ch.1 succeed because they **promise** competence first, then **teach operations** in a fixed order, then **show a constrained example**—without deleting the rigorous tables elsewhere. This pattern is **normative** for the human layer’s **Run tonight** and **Worked example** sections; it does **not** relax Quantum Plaid on the canonical file.

---

## 2. Core contract

### 2.1 Machine layer only (canonical file)

| Requirement | Test |
| --- | --- |
| All stable `{#anchor}` IDs used by cross-books, Osiris, and indexes | `rg '\\{#…\\}'` / ingest manifest lists match |
| Full **Quantum Plaid** payload for that phase: quotes, NPCs, tables, sensory covenant, seeds, JSON as mandated by [`quantum_plaid.md`](../quantum_plaid.md) and Alexandria ROADMAP | Checklist row in TASKLIST or CI gate |
| **`alexandria_*_entry_v1`** (and kin) JSON blocks where the book contract requires them | Schema validator passes |
| **Phase bridges** to sister volumes with explicit anchor links | No orphan references |
| **5% Cosmic Backfire** and artifact rules where scope requires | Mechanics Director sign-off on exceptions |
| **No** “reader-friendly” stripping of tables, IDs, or marginalia for length | Diff review rejects summary-only replacements |

**Forbidden in canonical-only duty:** replacing dense tables with prose summaries **without** keeping the full table; moving “the real rules” to the reader file only.

### 2.2 Human layer only (reader companion)

| Requirement | Test |
| --- | --- |
| Exactly **five** top-level sections after the header block—see [Section 3](#3-reader-companion-template-mandatory-structure) | Lint or manual |
| **No new mechanics**—numbers, traits, and procedures must **cite** canonical tables / anchors | Editorial diff: any number must trace to canonical anchor |
| **Banner** stating not for ingest / Tortuga | String `Do not use for ingest` present |
| **Single** worked example using **only** mechanics already in canonical chapter | Cross-check anchors exist in canonical |
| Optional **reading** voice—more conversational—but **not** a second canon | Grok/human pass: “invented rule?” → must be absent |

**Forbidden in reader-only duty:** introducing a new advantage cost, new DC, new tag, or new JSON schema not present in canonical.

### 2.3 Both layers (synchronization)

| Element | Rule |
| --- | --- |
| **1:1 chapter mapping** | Each `…-reader.md` names exactly **one** canonical source file in its header (path + primary anchor). |
| **Anchor index** | Reader file lists the **subset** of canonical `{#anchors}` needed for that session—not a duplicate ToC of the whole book. |
| **Drift control** | When canonical **patch** changes a cited anchor (rename, split table), reader file **must** update in the **same release** or the **same TASKLIST row**, or reader file gets a **STALE** banner with link to issue. |
| **Promotion** | If ingest ever consumes reader content, that is a **new** explicit project; default remains **no**. |

**Sync test:** For every `{#anchor}` cited in reader **Worked example** or **Run tonight**, `rg` that anchor in canonical file → **exactly one** defining occurrence.

---

## 3. Reader companion template (mandatory structure)

Every reader companion **must** use this skeleton (order fixed, headings may keep parenthetical timing labels):

```markdown
# <Title> (reader companion) {#reader-…}

**Layer:** Human-readable companion — **not** for Project Tortuga / Osiris ingest.
**Canonical source (SSoT):** `<repo-relative path to canonical .md>`

---

## Start here (90 seconds)

## Run tonight (procedure)

## Worked example (canonical mechanics only)

## Anchor index (this chapter)

## Do not use for ingest
```

| Section | Purpose | Hard rules |
| --- | --- | --- |
| **Start here (90 seconds)** | Orientation, stakes, what the GM gets | ≤ **~250 words**; **no** new rules; may cite **one** flagship anchor |
| **Run tonight** | Numbered or bulleted **procedure** (prep loop, encounter loop) | Every step that rolls dice or sets difficulty **links** an anchor or table ID |
| **Worked example** | One path through **existing** mechanics | **No** invented NPC stats; pull from canonical stat blocks or cite “use table T-…” |
| **Anchor index** | GM-facing list of `{#anchors}` for this session | Subset only; must mirror canonical spelling |
| **Do not use for ingest** | Legal and tooling boundary | Must forbid Tortuga/Osiris/automation ingest explicitly |

**Reference implementation (skeleton):** `Alexandria_Unleashed/attachments/reader-drafts/surgeons-grimoire/01-foreword-and-chapter-01-living-roman-tradition-reader.md`. **Pilot exemplars (filled, cursor-rpg only):** Ch.01 `attachments/drafts/2026-05-01_20-00_cursor_pilot-surgeon-ch01-reader-draft.md`; Ch.02 `attachments/drafts/2026-05-02_15-30_cursor_pilot-surgeon-ch02-reader-draft.md` (validations under `attachments/reports/` with matching forensic timestamps).

---

## 4. Canonical file human affordances (minimal)

Allowed **without** violating machine SSoT:

| Affordance | Specification |
| --- | --- |
| **Read Paths** (near ToC) | Markdown table: **Path** (e.g. “Tonight’s arena triage”), **Start anchor**, **Stop anchor**, **Best for** (one line). Max **8** rows per chapter unless centerpiece. |
| **When to use this** labels | One line **immediately above** a **major table group** (e.g. “When to use: mass-casualty fleet boarding”). Does not replace table intro text. |
| **Voice / sensory** | Sensory covenant and carved-voice quotes stay **in** canonical; reader layer **compresses navigation**, not voice quality. |
| **Glossary / Index** | Remain canonical; reader file does **not** duplicate—points back via Anchor index. |

**Not allowed** as “affordance creep”: duplicating the full chapter into simplified form inside canonical.

---

## 5. Mechanical generation strategy

| Stage | Action | Owner |
| --- | --- | --- |
| **Extract** | Parse canonical for `{#anchors}`, `T-…` table IDs, `SO-…` seeds, JSON keys | Automation / Editorial |
| **Map** | Build **anchor graph** for chapter (lorevault `graph_traversal` when live) | Lore Keeper |
| **Draft reader** | LLM or human fills **Start here** + **Run tonight** using **only** extracted IDs | Editorial Lead |
| **Verify** | Script: every mechanical claim in reader → resolvable anchor | QA / CI |
| **Schwartz pass** | Optional **density** pass on **canonical** only; reader stays **legible** | Creative Director policy |

**Testable rule:** A script can emit **Anchor index** from canonical file; reader’s Anchor index must be a **subset** of script output for that chapter.

---

## 6. Voice and tone guidelines

| Layer | Voice |
| --- | --- |
| **Canonical** | Quantum Plaid: **dark graveyard humor**, bureaucratic cruelty, sensory overload, **no** lazy grimdark; **15** carved-voice lanes where contract says so |
| **Reader** | Same **moral universe**, **shorter** sentences; **procedural** diction (“Do this, then this”); **no** sarcasm that smuggles new facts |

| Do | Do not |
| --- | --- |
| Use smell/sound as **prompts** in Start here | Invent a new smell that implies a new rule |
| Keep **one** grim joke in 90-second hook | Turn chapter into joke list without procedures |
| Cite **Black Tag** / triage only if canonical defines tags | Rename tags for “accessibility” |

---

## 7. Maintenance rules

| Question | Rule |
| --- | --- |
| **Versioning** | Canonical file carries **book/chapter** truth; reader file header includes **`reader_doc_rev`** (optional YAML) or **Last synced:** date in **Do not use for ingest** section. |
| **When to update reader** | Any change to **cited** anchors, table numbers, or JSON keys in canonical **requires** reader update **before** merge, or explicit STALE. |
| **Ownership** | **Editorial Lead** owns reader voice; **Lore Keeper** owns anchor truth; **Mechanics Director** owns stat/math alignment; **Producer** merges conflicts. |
| **Branch policy** | Never merge reader-only PR that touches canonical **without** canonical reviewer. |

---

## 8. Examples (reference: Surgeon’s Grimoire Ch.01)

**Canonical (machine SSoT):**  
`lore/Alexandria-Unleashed/04-Surgeons-Grimoire/01-foreword-and-chapter-01-living-roman-tradition.md`  
Primary anchor: `{#surgeons-ch01}` (file also uses `{#surgeons-ch01-toc}`, `{#surgeons-ch01-quotes}`, `{#surgeons-ch01-core}`, `{#surgeons-ch01-sensory-covenant}`, `{#surgeons-ch01-tables}`, …).

**Reader (human surface) — long-term (Alexandria_Unleashed):**  
`Alexandria_Unleashed/attachments/reader-drafts/surgeons-grimoire/01-foreword-and-chapter-01-living-roman-tradition-reader.md`  
Reader anchor: `{#reader-surgeons-grimoire-ch01}`.

**Pilot phase (cursor-rpg-studios only):** Reader companions may be drafted under **`attachments/drafts/`** in this repo (Output Organization v1.0 naming) while **Canonical source (SSoT)** points at the **read-only** Alexandria canonical file via `ALEXANDRIA_CANON_ROOT` / sibling checkout — **no** writes to Alexandria_Unleashed during tooling bring-up. Example pilots: Ch.01 `attachments/drafts/2026-05-01_20-00_cursor_pilot-surgeon-ch01-reader-draft.md` + `attachments/reports/2026-05-01_20-05_cursor_pilot-surgeon-ch01-reader-validation.md`; Ch.02 `attachments/drafts/2026-05-02_15-30_cursor_pilot-surgeon-ch02-reader-draft.md` + `attachments/reports/2026-05-02_15-45_cursor_pilot-surgeon-ch02-reader-validation.md`; human close-out `attachments/reports/2026-05-02_15-00_editorial-lead_pilot-ch01-human-closeout.md`.

| Contract point | How the example obeys it |
| --- | --- |
| Separation | Reader header names canonical path; **Do not use for ingest** paragraph present |
| Template | Five sections present; pilot may be filled in `cursor-rpg-studios` `attachments/drafts/` or skeleton in sibling repo |
| Worked example constraint | When filled, must use e.g. **T-SG101–T-SG103** and triage tags from canonical **only** |
| Voice | Canonical holds **18** quotes; reader **Start here** may quote **one** line **verbatim** with attribution to carved-voice block |

**Mini worked example (illustrative excerpt for *this* contract doc only):**

- **Run tonight (sketch):** (1) Open canonical `{#surgeons-ch01-tables}`. (2) Run mass-casualty scene using **T-SG101** site row + **T-SG102** tag row. (3) Apply **Section 5a** sensory check from `{#surgeons-ch01-sensory-covenant}`—if fewer than three channels, deny elite insight bonus **as canonical states**.

---

## 9. Future application (agents, skills enforcement)

| Mechanism | Enforcement |
| --- | --- |
| **`.cursor/rules`** | Add path-scoped rule: `attachments/reader-drafts/**/*.md` and `**/*-reader.md` → must match Section 3 template; `lore/**/*.md` → no reader-only mechanics |
| **Agents** | **Editorial Lead** approves reader PRs; **Lore Keeper** verifies anchors; **Stat Block Engineer** blocks invented numbers |
| **Skills** | Slash/playbooks e.g. `/reader-pass`, `/sync-reader-layer` must run **extract → diff → verify** pipeline |
| **CI** | `tests/test_reader_template.py` (headings), `tests/test_anchor_subset.py` (reader ⊆ canonical) when paths exist in this repo |

---

## 10. Lock statement

This **Human–machine dual-layer pattern** is **locked** as of **version 1.0.2** in **`cursor-rpg-studios`** (v1.0.1 Section 8 pilot-path clarification; v1.0.2 adds second pilot exemplar paths + human close-out references in Sections 3 and 8). All new chapters, reader companions, agents, and skills **must** treat this file as **normative**. Amendments require **Producer** approval, a **version bump**, and an entry in [`CHANGES.md`](../CHANGES.md). **No agent may invent a third layer** (e.g. “summary canon”) without a **charter ADR** in this repository.

**This pattern is now locked.**
