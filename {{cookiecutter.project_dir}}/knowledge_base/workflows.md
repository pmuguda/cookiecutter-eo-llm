# Workflows

## ExampleWorkflow

- **Purpose**: Demonstrates the workflow pattern. Not for production use.
- **Config type**: `ExampleWorkflow`
- **Required parameters**:
  - `input_path` — path to input GeoTIFF
  - `output_path` — path to output GeoTIFF
  - `crs` — target CRS string (e.g. `EPSG:4326`)
- **Outputs**: Logs input/output paths. No file I/O in this stub.
- **Added**: initial scaffold
