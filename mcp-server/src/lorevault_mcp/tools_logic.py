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


def semantic_search_lore(query: str, tags: str | None = None) -> dict[str, Any]:
    """Stub semantic search — returns empty matches until Chroma is wired (Phase 3)."""
    return {
        "matches": [],
        "query": query.strip(),
        "tags": tags,
        "backend": "stub",
    }


def graph_traversal(entity_id: str, depth: int = 2) -> dict[str, Any]:
    """Stub graph traversal — empty graph until SQLite/NetworkX (Phase 3)."""
    return {
        "entity_id": entity_id.strip(),
        "depth": max(0, int(depth)),
        "nodes": [],
        "edges": [],
        "backend": "stub",
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
    gen = rng or random.Random()
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
    errors = validate_npc_payload(payload, repo_root=repo_root)
    if errors:
        return {"ok": False, "errors": errors, "backend": "stub"}
    return {"ok": True, "accepted": True, "backend": "stub", "name": payload.get("name")}
