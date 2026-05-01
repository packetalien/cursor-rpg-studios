"""Reader companion five-section template (dual-layer Section 3)."""

from __future__ import annotations

from reader_template_checks import (
    load_fixture,
    validate_reader_template,
)


def test_valid_fixture_passes() -> None:
    ok, errs = validate_reader_template(load_fixture("reader_companion_valid.md"))
    assert ok, errs


def test_bad_heading_order_fails() -> None:
    ok, errs = validate_reader_template(load_fixture("reader_companion_bad_order.md"))
    assert not ok
    assert any("heading_order" in e for e in errs)
