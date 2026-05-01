"""Schema file presence and shape."""

from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_npc_schema_is_json_and_has_required_keys() -> None:
    path = REPO_ROOT / "data" / "schemas" / "alexandria_npc_entry_v1.schema.json"
    assert path.is_file()
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data.get("title") == "alexandria_npc_entry_v1"
    assert "required" in data
    for key in ("schema_version", "name", "st", "dx", "iq", "ht"):
        assert key in data["required"]
