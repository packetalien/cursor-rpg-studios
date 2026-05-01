# Style Bible — Cursor RPG Studios

## Voice and tone

| Axis | Target |
| --- | --- |
| **Genre** | Age of Sail × eldritch horror × clockwork decay |
| **Humor** | Dark graveyard humor — horrific, never lazy grimdark |
| **Operators** | Fifteen recurring personas (bureaucratic cruelty, stoic brass-age fatalism, forbidden-archive dread) |
| **Table voice** | Precise GURPS terminology; avoid generic fantasy filler |

## Visual and cartographic

- **Datum / CRS:** All real-world or hybrid maps document CRS in [`docs/cartography-standards.md`](docs/cartography-standards.md); procedural outputs under `procedural/gis/` and `procedural/datum/` must cite source CRS and transforms.  
- **Handouts:** High contrast, period-appropriate frames; Foundry/Roll20 export hooks live under future `Formatting & Export` agents.

## Sensory covenant (minimum)

Each location-scale draft should name **at least three senses** with **mechanical consequence** where possible (e.g., acrid soot → visibility / HT check).

## NPC and stat block

- **3D6 System** stat blocks; IDs book-scoped.  
- **Derived stats** must match Strength → HP/damage ladders per GURPS 4e; validators enforce.

## Commit annotations

Use **Commit (public)** for repo-only scaffolding; **Commit (private)** when referencing unpublished vault paths or operator machine layout (avoid secrets).
