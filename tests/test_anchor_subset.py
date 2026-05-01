"""Reader cites must exist in paired canonical (dual-layer Section 2.3 sync test)."""

from __future__ import annotations

import os
from pathlib import Path

import pytest

from reader_template_checks import (
    load_fixture,
    validate_anchor_subset,
)


def test_fixture_reader_subset_of_fixture_canonical() -> None:
    reader = load_fixture("reader_companion_valid.md")
    canon = load_fixture("canonical_excerpt.md")
    ok, errs = validate_anchor_subset(reader, canon)
    assert ok, errs


def test_missing_anchor_fails() -> None:
    reader = load_fixture("reader_companion_valid.md").replace(
        "{#demo-anchor}", "{#nonexistent-anchor}"
    )
    canon = load_fixture("canonical_excerpt.md")
    ok, errs = validate_anchor_subset(reader, canon)
    assert not ok
    assert any("nonexistent" in e for e in errs)


@pytest.mark.skipif(
    not os.environ.get("ALEXANDRIA_CANON_ROOT"),
    reason="ALEXANDRIA_CANON_ROOT not set",
)
def test_pilot_reader_against_live_canon_when_env_set() -> None:
    root = Path(os.environ["ALEXANDRIA_CANON_ROOT"])
    canon_path = (
        root
        / "04-Surgeons-Grimoire"
        / "01-foreword-and-chapter-01-living-roman-tradition.md"
    )
    if not canon_path.is_file():
        pytest.skip("canonical chapter not present at ALEXANDRIA_CANON_ROOT")
    pilot = (
        Path(__file__).resolve().parents[1]
        / "attachments"
        / "drafts"
        / "2026-05-01_20-00_cursor_pilot-surgeon-ch01-reader-draft.md"
    )
    if not pilot.is_file():
        pytest.skip("pilot reader draft not in workspace")
    reader_md = pilot.read_text(encoding="utf-8")
    canon_md = canon_path.read_text(encoding="utf-8")
    ok, errs = validate_anchor_subset(reader_md, canon_md)
    assert ok, errs
