"""Tests for lorevault_mcp tool logic."""

from __future__ import annotations

import random
from pathlib import Path

import pytest

from lorevault_mcp.tools_logic import (
    add_character_v1,
    graph_traversal,
    semantic_search_lore,
    simulate_roll,
)

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_semantic_search_lore_stub() -> None:
    out = semantic_search_lore("burning copper", tags="atmospheric")
    assert out["matches"] == []
    assert out["query"] == "burning copper"
    assert out["tags"] == "atmospheric"


def test_graph_traversal_stub() -> None:
    out = graph_traversal("faction:clockwork-barons", depth=3)
    assert out["entity_id"] == "faction:clockwork-barons"
    assert out["depth"] == 3
    assert out["nodes"] == []


def test_simulate_roll_deterministic() -> None:
    rng = random.Random(42)
    a = simulate_roll("3d6", rng=rng)
    rng = random.Random(42)
    b = simulate_roll("3d6", rng=rng)
    assert a["ok"] and b["ok"]
    assert a["total"] == b["total"]
    assert len(a["rolls"]) == 3


def test_simulate_roll_invalid() -> None:
    out = simulate_roll("not dice")
    assert out["ok"] is False


def test_add_character_v1_valid() -> None:
    payload = {
        "schema_version": "1.0.0",
        "name": "Test Bosun",
        "st": 11,
        "dx": 12,
        "iq": 10,
        "ht": 11,
    }
    out = add_character_v1(payload, repo_root=REPO_ROOT)
    assert out["ok"] is True


def test_add_character_v1_invalid() -> None:
    out = add_character_v1({"name": "Broken"}, repo_root=REPO_ROOT)
    assert out["ok"] is False
    assert out["errors"]
