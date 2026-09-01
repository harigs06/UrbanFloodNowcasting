"""Decoupled Drainage Network Training & GNN Surrogate Exporter for Multi-City Scaling.

Processes and trains municipal stormwater networks independently per city:
  1. Parses KML / GeoJSON / Shapefile municipal drainage layers into nodes & conduits
  2. Solves Manning full-pipe conveyance capacities
  3. Builds high-scale igraph topology
  4. Trains city-specific GNN hydraulic surrogate and exports optimized ONNX model

Usage:
  python -m src.offline.train_drainage --city hyderabad --epochs 10 --hidden-dim 32
"""

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple
import numpy as np

from src.config import settings
from src.cities import get_city_profile
from src.core.drainage_graph import DrainageGraph
from src.offline.gnn_training import GNNTrainer
from src.offline.ingest_real_data import parse_drainage_kml


def train_drainage_for_city(
    city_id: str,
    epochs: int = 10,
    hidden_dim: int = 32,
    kml_override: Path = None,
) -> dict:
    """Parses drainage topology, builds graph, and trains GNN surrogate for a city."""
    city_profile = get_city_profile(city_id)
    print("=" * 65)
    print(f"  DRAINAGE NETWORK TRAINING & GNN SURROGATE — {city_profile.display_name.upper()} ({city_profile.state})")
    print("=" * 65)

    city_net_dir = settings.get_city_network_dir(city_id)
    city_model_path = settings.get_city_model_path(city_id)

    # 1. Locate Drainage KML or JSON
    kml_file = None
    if kml_override and kml_override.exists():
        kml_file = kml_override
    else:
        candidates = list(city_net_dir.glob("*.kml"))
        if not candidates:
            candidates = list(settings.NETWORK_DIR.glob("*.kml"))
        if candidates:
            kml_file = candidates[0]

    nodes = []
    conduits = []

    if kml_file:
        print(f"[NETWORK] Parsing municipal drainage map: {kml_file.name}")
        nodes, conduits = parse_drainage_kml(kml_file)
        print(f"          Extracted {len(nodes)} Junction Nodes and {len(conduits)} Conduit Segments.")
    else:
        # Check for existing drainage_topology.json
        json_candidates = list(city_net_dir.glob("drainage_topology.json")) + list(settings.NETWORK_DIR.glob("drainage_topology.json"))
        if json_candidates:
            with open(json_candidates[0], "r", encoding="utf-8") as f:
                data = json.load(f)
            nodes = data.get("nodes", [])
            conduits = data.get("conduits", [])
            print(f"[NETWORK] Loaded existing topology: {len(nodes)} nodes, {len(conduits)} conduits.")
        else:
            print(f"[NETWORK] No drainage map found. Initializing nominal network for {city_profile.display_name}...")
            from src.api.v1.drainage import SAMPLE_NODES, SAMPLE_CONDUITS
            nodes = [n.model_dump() for n in SAMPLE_NODES]
            conduits = [c.model_dump() for c in SAMPLE_CONDUITS]

    # Save to city network directory
    out_json = city_net_dir / "drainage_topology.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump({"nodes": nodes, "conduits": conduits}, f, indent=2)
    print(f"          [OK] Saved topology to {out_json}")

    # Also mirror to default network dir if default city
    if city_id.lower() == settings.DEFAULT_CITY_ID:
        default_out = settings.NETWORK_DIR / "drainage_topology.json"
        with open(default_out, "w", encoding="utf-8") as f:
            json.dump({"nodes": nodes, "conduits": conduits}, f, indent=2)

    # 2. Build igraph & calculate Manning capacities
    drainage_graph = DrainageGraph()
    drainage_graph.build_graph(nodes, conduits)
    print(f"[IGRAPH] Built graph with {len(drainage_graph.node_ids)} nodes.")

    # 3. Train City-Specific GNN Surrogate
    print(f"\n[GNN SURROGATE] Training neural hydraulic surrogate ({epochs} epochs)...")
    num_sample_nodes = min(30, len(nodes))
    trainer = GNNTrainer(
        model_save_path=city_model_path,
    )
    model_path = trainer.train_and_export(epochs=epochs, num_nodes=num_sample_nodes)
    print(f"                [OK] Exported ONNX surrogate model to: {model_path.name}")

    # Mirror to default model path if default city
    if city_id.lower() == settings.DEFAULT_CITY_ID:
        import shutil
        shutil.copy(model_path, settings.SURROGATE_MODEL_PATH)

    print("\n" + "=" * 65)
    print(f"  DRAINAGE TRAINING COMPLETE FOR {city_profile.display_name.upper()}!")
    print("=" * 65)

    return {
        "city_id": city_id,
        "total_nodes": len(nodes),
        "total_conduits": len(conduits),
        "model_path": str(city_model_path),
        "topology_file": str(out_json),
    }


def main():
    parser = argparse.ArgumentParser(description="Parse drainage network and train GNN surrogate for a city.")
    parser.add_argument("--city", type=str, default="hyderabad", help="Target city ID (e.g. hyderabad, mumbai, chennai)")
    parser.add_argument("--epochs", type=int, default=5, help="Number of GNN training epochs")
    parser.add_argument("--hidden-dim", type=int, default=32, help="Hidden dimension for GNN layers")
    parser.add_argument("--kml-file", type=str, default=None, help="Optional explicit path to .kml file")

    args = parser.parse_args()
    kml_path = Path(args.kml_file) if args.kml_file else None
    train_drainage_for_city(
        city_id=args.city,
        epochs=args.epochs,
        hidden_dim=args.hidden_dim,
        kml_override=kml_path,
    )


if __name__ == "__main__":
    main()
