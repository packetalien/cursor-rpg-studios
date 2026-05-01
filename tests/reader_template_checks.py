"""Shared helpers for reader companion template tests."""

from __future__ import annotations

import re
from pathlib import Path

REQUIRED_H2 = [
    "Start here (90 seconds)",
    "Run tonight (procedure)",
    "Worked example (canonical mechanics only)",
    "Anchor index (this chapter)",
    "Do not use for ingest",
]

_ANCHOR_RE = re.compile(r"\{#([^}]+)\}")


def anchors_in_text(text: str, *, exclude_first_line: bool = False) -> set[str]:
    """Collect ``{#…}`` tokens; optionally drop the first line (H1 reader id)."""
    src = text
    if exclude_first_line:
        lines = text.splitlines()
        src = "\n".join(lines[1:]) if lines else text
    return set(_ANCHOR_RE.findall(src))


def extract_h2_headings(md: str) -> list[str]:
    """Return first-level ## headings in document order."""
    out: list[str] = []
    for line in md.splitlines():
        if line.startswith("## ") and not line.startswith("###"):
            out.append(line[3:].strip())
    return out


def validate_reader_template(md: str) -> tuple[bool, list[str]]:
    """Return (ok, list of failure messages)."""
    errors: list[str] = []
    h2 = extract_h2_headings(md)
    if h2[: len(REQUIRED_H2)] != REQUIRED_H2:
        errors.append(f"heading_order: expected {REQUIRED_H2!r}, got {h2!r}")
    if "(reader companion)" not in md:
        errors.append("missing reader companion marker in title")
    if "**Layer:**" not in md:
        errors.append("missing **Layer:** header")
    elif "Project Tortuga" not in md or "Osiris" not in md:
        errors.append("Layer must reference Project Tortuga and Osiris ingest guard")
    if "Canonical source (SSoT):" not in md:
        errors.append("missing Canonical source (SSoT)")
    low = md.lower()
    if "do not use for ingest" not in low:
        errors.append("missing Do not use for ingest section body")
    if "tortuga" not in low or "osiris" not in low or "automation" not in low:
        errors.append("ingest ban must mention tortuga, osiris, automation")
    return (len(errors) == 0, errors)


def table_ids_in_text(text: str) -> set[str]:
    return set(re.findall(r"\bT-[A-Z]{2,}[0-9]+\b", text))


def validate_anchor_subset(reader_md: str, canonical_md: str) -> tuple[bool, list[str]]:
    """
    Every {#anchor} (except H1 title line) and T-… in reader must appear in canonical.

    Title-line `{#reader-…}` is companion identity, not a canon anchor.
    """
    errors: list[str] = []
    canon = canonical_md
    for aid in anchors_in_text(reader_md, exclude_first_line=True):
        token = "{#" + aid + "}"
        if token not in canon:
            errors.append(f"missing anchor in canonical: {token}")
    for tid in table_ids_in_text(reader_md):
        if tid not in canon:
            errors.append(f"missing table id in canonical: {tid}")
    return (len(errors) == 0, errors)


def load_fixture(name: str) -> str:
    path = Path(__file__).resolve().parent / "fixtures" / name
    return path.read_text(encoding="utf-8")
