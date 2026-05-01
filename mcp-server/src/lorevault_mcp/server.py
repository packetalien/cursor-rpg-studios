"""stdio MCP server — lorevault tools (stub backends)."""

from __future__ import annotations

import argparse
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from lorevault_mcp.tools_logic import add_character_v1 as validate_npc_payload
from lorevault_mcp.tools_logic import graph_traversal as graph_traversal_impl
from lorevault_mcp.tools_logic import semantic_search_lore as semantic_search_impl
from lorevault_mcp.tools_logic import simulate_roll as simulate_roll_impl

mcp = FastMCP("lorevault")


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


@mcp.tool()
def semantic_search_lore(query: str, tags: str | None = None) -> dict:
    """
    Natural-language semantic search over lore embeddings.
    Input: query string; optional comma-separated metadata tags.
    Returns ranked matches (stub: empty list until ChromaDB Phase 3).
    """
    return semantic_search_impl(query=query, tags=tags)


@mcp.tool()
def graph_traversal(entity_id: str, depth: int = 2) -> dict:
    """
    Traverse the entity graph from entity_id up to depth hops.
    Input: entity_id (stable ID); depth integer >= 0.
    Returns nodes and edges as JSON-serializable structures (stub).
    """
    return graph_traversal_impl(entity_id=entity_id, depth=depth)


@mcp.tool()
def simulate_roll(expression: str) -> dict:
    """
    Deterministic dice evaluation using Python RNG (not LLM math).
    Accepts NdM with optional modifier, e.g. 3d6, 2d6+3, 1d20-1.
    """
    return simulate_roll_impl(expression)


@mcp.tool()
def add_character_v1(payload: dict) -> dict:
    """
    Validate and accept NPC payload against alexandria_npc_entry_v1 JSON Schema.
    Rejects malformed payloads with structured errors (stub: no vault write).
    """
    return validate_npc_payload(payload, repo_root=_repo_root())


def main() -> None:
    parser = argparse.ArgumentParser(description="lorevault MCP stdio server")
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=("stdio", "streamable-http"),
        help="MCP transport (default stdio for Cursor)",
    )
    args = parser.parse_args()
    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport="streamable-http", host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
