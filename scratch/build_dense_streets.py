"""Script to generate dense, realistic, city-scale street networks for all 6 metropolitan cities."""

import json
from pathlib import Path

# We will generate rich TypeScript mockData.ts
output_path = Path("frontend/src/data/mockData.ts")

# Read existing file to preserve DRAINAGE_NODES_HYD, DRAINAGE_CONDUITS_HYD, HISTORICAL_SCENARIOS, INITIAL_ALERTS
with open(output_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's inspect the sections
print(f"Existing mockData.ts has {len(content)} characters.")
