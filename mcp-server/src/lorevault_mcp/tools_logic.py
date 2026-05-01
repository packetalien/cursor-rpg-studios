"""Pure functions for MCP tools — testable without running stdio server."""

from __future__ import annotations

import json
import random
import re
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

_DICE_RE = re.compile(
    r"^\s*(?P<count>\d+)\s*d\s*(?P<sides>\d+)(?P<mod>[+-]\d+)?\s*$",
    re.IGNORECASE,
)

# Resource limits (MCP callers are untrusted planners; avoid CPU/memory blowups)
_MAX_DICE_COUNT = 100
_MAX_DICE_SIDES = 1000
_MAX_GRAPH_DEPTH = 50
_MAX_TOOL_STRING = 8192
_MAX_PAYLOAD_JSON_BYTES = 512 * 1024


def semantic_search_lore(query: str, tags: str | None = None) -> dict[str, Any]:
    """
    Stub semantic search until Chroma is wired (Phase 3).

    Returns one sentinel match so clients never misread ``matches == []`` as
    “no lore exists.” Use ``_stub`` and ``stub_notice`` for proof posture.
    """
    q = query.strip()
    if len(q) > _MAX_TOOL_STRING:
        return {
            "matches": [],
            "query": q[:200] + "…",
            "tags": tags,
            "backend": "stub",
            "error": "query_too_long",
            "stub_notice": "Query exceeded maximum length; shorten the string.",
        }
    return {
        "matches": [
            {
                "_stub": True,
                "title": "lorevault_stub_notice",
                "snippet": (
                    "semantic_search_lore is not backed by a vector index yet; "
                    "do not treat this result as retrieved canon. "
                    "Use read-only Alexandria paths or filesystem search."
                ),
                "query_echo": q,
            }
        ],
        "query": q,
        "tags": tags,
        "backend": "stub",
        "stub_notice": (
            "Empty-match stubs are unsafe for canon proof; "
            "see stub-aware-graph-handling skill and ROADMAP Phase 3."
        ),
    }


def graph_traversal(entity_id: str, depth: int = 2) -> dict[str, Any]:
    """
    Stub graph traversal until SQLite/NetworkX (Phase 3).

    Returns one sentinel node so ``nodes == []`` is never confused with a
    validated empty subgraph.
    """
    eid = entity_id.strip()
    if len(eid) > _MAX_TOOL_STRING:
        return {
            "entity_id": eid[:200] + "…",
            "depth": 0,
            "nodes": [],
            "edges": [],
            "backend": "stub",
            "error": "entity_id_too_long",
            "stub_notice": "entity_id exceeded maximum length.",
        }
    try:
        d_raw = int(depth)
    except (TypeError, ValueError):
        d_raw = 0
    d = max(0, min(d_raw, _MAX_GRAPH_DEPTH))
    return {
        "entity_id": eid,
        "depth": d,
        "nodes": [
            {
                "_stub": True,
                "id": eid,
                "label": "lorevault_graph_stub",
                "message": (
                    "graph_traversal has no persisted edges yet; "
                    "this node is a placeholder, not Lore Keeper audit output."
                ),
            }
        ],
        "edges": [],
        "backend": "stub",
        "stub_notice": (
            "Graph backend not live; do not merge narrative gates on this output alone."
        ),
    }


def simulate_roll(expression: str, rng: random.Random | None = None) -> dict[str, Any]:
    """
    Minimal NdM + optional static modifier (e.g. 3d6, 2d6+2).
    Deterministic if rng is provided.
    """
    raw = expression.strip()
    m = _DICE_RE.match(raw)
    if not m:
        return {"ok": False, "error": "unsupported_notation", "expression": raw}
    count = int(m.group("count"))
    sides = int(m.group("sides"))
    mod = int(m.group("mod") or 0)
    if count < 1 or sides < 2:
        return {"ok": False, "error": "invalid_dice", "expression": raw}
    if count > _MAX_DICE_COUNT or sides > _MAX_DICE_SIDES:
        return {
            "ok": False,
            "error": "dice_limits_exceeded",
            "expression": raw,
            "limits": {"max_count": _MAX_DICE_COUNT, "max_sides": _MAX_DICE_SIDES},
        }
    # TTRPG dice only — not a CSPRNG; deterministic tests pass an explicit rng.
    gen = rng or random.Random()  # nosec B311
    rolls = [gen.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + mod
    return {
        "ok": True,
        "expression": raw,
        "rolls": rolls,
        "modifier": mod,
        "total": total,
    }


def _schema_path(repo_root: Path | None = None) -> Path:
    root = repo_root or Path(__file__).resolve().parents[3]
    return root / "data" / "schemas" / "alexandria_npc_entry_v1.schema.json"


def load_npc_validator(repo_root: Path | None = None) -> Draft202012Validator:
    path = _schema_path(repo_root)
    with path.open(encoding="utf-8") as f:
        schema = json.load(f)
    return Draft202012Validator(schema)


def validate_npc_payload(payload: dict[str, Any], repo_root: Path | None = None) -> list[str]:
    """Return list of validation error messages (empty if valid)."""
    validator = load_npc_validator(repo_root)
    return [e.message for e in validator.iter_errors(payload)]


def add_character_v1(payload: dict[str, Any], repo_root: Path | None = None) -> dict[str, Any]:
    """
    Validate alexandria_npc_entry_v1. Stub does not persist to vault (Phase 4).
    """
    try:
        raw_json = json.dumps(payload, separators=(",", ":"), sort_keys=True)
    except (TypeError, ValueError):
        return {"ok": False, "errors": ["payload_not_json_serializable"], "backend": "stub"}
    if len(raw_json.encode("utf-8")) > _MAX_PAYLOAD_JSON_BYTES:
        return {"ok": False, "errors": ["payload_too_large"], "backend": "stub"}
    errors = validate_npc_payload(payload, repo_root=repo_root)
    if errors:
        return {"ok": False, "errors": errors, "backend": "stub"}
    return {"ok": True, "accepted": True, "backend": "stub", "name": payload.get("name")}
