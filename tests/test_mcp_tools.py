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
    assert len(out["matches"]) == 1
    assert out["matches"][0].get("_stub") is True
    assert "stub_notice" in out and out["stub_notice"]
    assert out["query"] == "burning copper"
    assert out["tags"] == "atmospheric"


def test_graph_traversal_stub() -> None:
    out = graph_traversal("faction:clockwork-barons", depth=3)
    assert out["entity_id"] == "faction:clockwork-barons"
    assert out["depth"] == 3
    assert len(out["nodes"]) == 1
    assert out["nodes"][0].get("_stub") is True
    assert "stub_notice" in out and out["stub_notice"]
    assert out["edges"] == []


def test_graph_traversal_depth_capped() -> None:
    out = graph_traversal("e:1", depth=10_000)
    assert out["depth"] == 50


def test_graph_traversal_entity_id_too_long() -> None:
    out = graph_traversal("x" * 9000, depth=1)
    assert out.get("error") == "entity_id_too_long"
    assert out["nodes"] == []


def test_semantic_search_query_too_long() -> None:
    out = semantic_search_lore("q" * 9000)
    assert out.get("error") == "query_too_long"
    assert out["matches"] == []


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


def test_simulate_roll_dice_limits() -> None:
    out = simulate_roll("200d6")
    assert out["ok"] is False
    assert out.get("error") == "dice_limits_exceeded"
    out2 = simulate_roll("2d2000")
    assert out2["ok"] is False
    assert out2.get("error") == "dice_limits_exceeded"


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


def test_add_character_v1_payload_too_large() -> None:
    huge = {"schema_version": "1.0.0", "name": "X", "st": 10, "dx": 10, "iq": 10, "ht": 10, "pad": "y" * 600_000}
    out = add_character_v1(huge, repo_root=REPO_ROOT)
    assert out["ok"] is False
    assert "payload_too_large" in out["errors"]
