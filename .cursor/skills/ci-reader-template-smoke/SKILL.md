---
name: ci-reader-template-smoke
description: Run in-repo pytest for reader five-section template and anchor subset; optional ALEXANDRIA_CANON_ROOT integration skip.
---

# CI — Reader Template Smoke

**Use this skill when:** closing a reader companion PR or after editing `tests/reader_template_checks.py` / fixtures.

**Normative:** [`docs/human-machine-dual-layer-pattern.md`](../../../docs/human-machine-dual-layer-pattern.md) Section 9 (automation intent).  
**Pairs with:** `reader-template-enforcer`, `anchor-validation-sync`.

---

## 1. Command (repo root)

```bash
cd /path/to/cursor-rpg-studios
pip install -e "mcp-server[dev]"
pytest -q tests/test_reader_template.py tests/test_anchor_subset.py tests/test_mcp_tools.py tests/test_npc_schema.py
```

Full suite: `pytest -q`

---

## 2. What the tests enforce

| Test module | Role |
| --- | --- |
| `test_reader_template.py` | Five `##` headings in order + Layer / SSoT / ingest-ban strings (fixtures). |
| `test_anchor_subset.py` | Fixture subset sync; optional live pilot vs canon when `ALEXANDRIA_CANON_ROOT` set and files exist. |
| `test_mcp_tools.py` | Stub tools return deterministic dice + **sentinel** search/graph payloads (`_stub`, `stub_notice`). |

---

## 3. Environment

| Variable | Effect |
| --- | --- |
| `ALEXANDRIA_CANON_ROOT` | When set and canonical chapter + pilot draft exist, `test_pilot_reader_against_live_canon_when_env_set` runs; else skipped. |

---

## 4. On failure

Fix reader or tests; do not weaken assertions without Producer + Editorial sign-off. Escalate systematic doc/test mismatch via **`request-human-override`**.
