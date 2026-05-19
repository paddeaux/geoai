---
type: knowledge
category: research-engineer
id: geoai-research:concepts:study-design
parent: geoai-research:concepts
---

# Study Design

## Overview
The GeoAI 2026 paper (submission 3192, "Integrating LLM-based workflows into GIS classroom learning
activities") investigates whether LLMs can generate usable geospatial datasets for GIS education.
The study compares three data generation approaches across multiple LLMs and two cities, with each
LLM-generated dataset compared against its RADIAN counterpart as a spatial baseline.

## Research Question

Can LLMs generate geospatial point datasets (synthetic, OSM-derived, or randomly distributed)
that are spatially valid and comparable to baseline datasets produced by RADIAN?

## Task Types

### Task A — Synthetic Data Generation
- **Prompt**: Generate a synthetic dataset of 500 restaurant locations in [city]
- **Constraint**: Points must fall within the provided GeoJSON boundary
- **Output**: GeoJSON FeatureCollection with 500 Point features
- **Nature**: LLM invents plausible but fictional restaurant locations

### Task B — OSM-Derived Data Generation
- **Prompt**: Generate a geospatial dataset of 500 restaurant locations in [city] using
  openly available data such as OpenStreetMap
- **Constraint**: Points must fall within the provided GeoJSON boundary
- **Output**: GeoJSON FeatureCollection with 500 Point features
- **Nature**: LLM should recall/generate real-world OSM data (or attempt to)

### Task C — Random Point Generation
- **Prompt**: Generate a geospatial dataset of 500 randomly distributed points in [city]
- **Constraint**: Points must fall within the provided GeoJSON boundary
- **Output**: GeoJSON FeatureCollection with 500 Point features
- **Nature**: LLM generates a point set under complete spatial randomness (CSR baseline)
- **Purpose**: Establishes whether LLMs can produce spatially random distributions,
  serving as a null spatial model for comparison

## Study Cities

| City | Boundary File | Approx. BBox |
|---|---|---|
| London | `london_4326.geojson` | `-0.51, 51.28, 0.33, 51.69` |
| Berlin | `berlin_4326.geojson` | `13.09, 52.34, 13.76, 52.68` |

## Experimental Matrix

| Task | City | Method | Output dir |
|---|---|---|---|
| A | London | LLM (all 6 models) | `llm-outputs/{model}/` |
| A | Berlin | LLM (all 6 models) | `llm-outputs/{model}/` |
| A | London | RADIAN (baseline) | `llm-outputs/radian/` |
| A | Berlin | RADIAN (baseline) | `llm-outputs/radian/` |
| B | London | LLM (all 6 models) | `llm-outputs/{model}/` |
| B | Berlin | LLM (all 6 models) | `llm-outputs/{model}/` |
| B | London | RADIAN baseline | `llm-outputs/radian/` |
| B | Berlin | RADIAN baseline | `llm-outputs/radian/` |
| C | London | LLM (all 6 models) | `llm-outputs/{model}/` |
| C | Berlin | LLM (all 6 models) | `llm-outputs/{model}/` |
| C | London | RADIAN baseline (CSR) | `llm-outputs/radian/` |
| C | Berlin | RADIAN baseline (CSR) | `llm-outputs/radian/` |

## Models in Scope (Levente's responsibility via Navigator)

1. `gpt-4.1`
2. `claude-4.7-opus`
3. `gemini-3.1-pro`
4. `gpt-oss-120b`
5. `gpt-oss-20b`
6. `llama-3.1-8b-instruct`

*(Note: `llama-3.1-70b-instruct` was initially in scope but dropped due to API proxy timeouts when generating 500-point GeoJSON payloads)*

## Output Requirements

- **Format**: GeoJSON FeatureCollection
- **Count**: 500 Point features
- **CRS**: WGS84 (EPSG:4326)
- **Properties**: At minimum `name` (restaurant name) for Tasks A & B; any property for Task C
- **Validity**: All points inside city boundary
- **Storage**: `data/llm-outputs/{model_id}/raw/` (raw) and `data/llm-outputs/{model_id}/validated/` (clean)

## Analysis Plan (post-collection)

1. Plot outputs on map for each model × task × city
2. Measure: percentage of valid points (inside boundary)
3. Measure: spatial distribution (clustering, coverage, nearest-neighbor statistics)
4. Qualitative: do names/properties seem plausible? (Tasks A & B)
5. Compare Task A vs Task B vs Task C outputs within each model
6. **RADIAN comparison**: For each model × task × city, compute spatial similarity metrics
   between the LLM-generated dataset and its RADIAN counterpart baseline
7. Cross-model comparison: rank models by spatial validity and RADIAN similarity

## Related Topics

- Parent: [Domain Concepts](../concepts/)
- Related: [Data Collection Workflow](../workflows/data-collection.md)
- Related: [Boundary Files](../resources/boundary-files.md)
- Related: [Model Catalog](../resources/model-catalog.md)
