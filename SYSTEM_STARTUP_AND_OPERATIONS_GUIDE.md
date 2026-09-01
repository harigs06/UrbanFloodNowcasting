# 🚀 Urban Flood Nowcasting Engine — System Startup & Operations Guide

This document is an exhaustive, step-by-step operational runbook for configuring, preprocessing, training, provisioning, launching, and validating the **Urban Flood Nowcasting and Emergency Navigation Engine** (`urban_flood_engine`).

---

## 📑 Table of Contents

1. [System Prerequisites & Environment Setup](#1-system-prerequisites--environment-setup)
2. [Order of Operations Overview](#2-order-of-operations-overview)
3. [Pre-Backend Offline Preparation & Preprocessing Pipeline](#3-pre-backend-offline-preparation--preprocessing-pipeline)
   - [3.1 Multi-City Automated Ingestion (Recommended Fast Path)](#31-multi-city-automated-ingestion-recommended-fast-path)
   - [3.2 Step 1: Terrain Ingestion & D8 Elevation Preprocessing](#32-step-1-terrain-ingestion--d8-elevation-preprocessing)
   - [3.3 Step 2: Drainage Network Parsing & igraph Construction](#33-step-2-drainage-network-parsing--igraph-construction)
   - [3.4 Step 3: Real-Time IMD Radar Scraping & Ingestion](#34-step-3-real-time-imd-radar-scraping--ingestion)
   - [3.5 Step 4: EPA-SWMM Ground Truth Generation](#35-step-4-epa-swmm-ground-truth-generation)
   - [3.6 Step 5: GNN Surrogate Model Training & ONNX Export](#36-step-5-gnn-surrogate-model-training--onnx-export)
   - [3.7 Step 6: Model Calibration & Accuracy Benchmarking](#37-step-6-model-calibration--accuracy-benchmarking)
   - [3.8 Ingesting Custom City Datasets (.tif DEM & .kml Drains)](#38-ingesting-custom-city-datasets-tif-dem--kml-drains)
4. [Database Provisioning & Alembic Migrations](#4-database-provisioning--alembic-migrations)
5. [Starting the Backend Services](#5-starting-the-backend-services)
   - [5.1 Starting FastAPI Web & WebSocket Server](#51-starting-fastapi-web--websocket-server)
   - [5.2 Starting ARQ Background Task Worker](#52-starting-arq-background-task-worker)
   - [5.3 Starting IMD Radar Poller Daemon](#53-starting-imd-radar-poller-daemon)
6. [Starting the Frontend Web Application](#6-starting-the-frontend-web-application)
7. [One-Command Multi-Service Docker Deployment](#7-one-command-multi-service-docker-deployment)
8. [System Verification, Testing & Health Checks](#8-system-verification-testing--health-checks)
9. [Common Operational Workflows & Troubleshooting](#9-common-operational-workflows--troubleshooting)

---

## 1. System Prerequisites & Environment Setup

### Required System Software
- **Operating System**: Windows 10/11, Linux (Ubuntu 20.04+), or macOS.
- **Python**: Version `3.10` or higher (`3.11` recommended).
- **Node.js**: Version `18.x` or `20.x` LTS.
- **npm**: Version `9.x` or `10.x`.
- **Database & Cache (Optional for dev, required for full persistence)**:
  - **PostgreSQL 16+** with **PostGIS 3.4+** and **TimescaleDB**.
  - **Redis 5.0+** (port `6379`).
- **Docker & Docker Compose** (Optional, for 1-command containerized execution).

---

### Step 1.1: Clone and Set Up Python Virtual Environment

Open PowerShell (Windows) or Terminal (Linux/macOS) in your project directory:

```powershell
# Navigate to the workspace root
cd doobegaKya

# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Windows Command Prompt:
# .venv\Scripts\activate.bat
# Linux / macOS:
# source .venv/bin/activate

# Upgrade pip to latest version
python -m pip install --upgrade pip
```

---

### Step 1.2: Install Backend Python Dependencies

Install all core web, geospatial, hydraulic, and machine learning libraries:

```powershell
pip install -r requirements.txt
```

> **Note on Optional PyTorch & SWMM packages**:
> - If you have a GPU or wish to train custom GNN architectures using PyG from scratch, install `torch` and `torch-geometric`.
> - If you want full EPA-SWMM dynamic-wave ground truth generation, install `pyswmm`.
> - **The codebase includes built-in ONNX and numerical fallbacks**, meaning the entire system operates out of the box even without PyTorch or PySWMM installed.

---

### Step 1.3: Configure Environment Variables

Create or verify the `.env` file in the root directory:

```env
# Application Core
APP_NAME="Urban Flood Nowcasting Engine"
ENVIRONMENT=development
DEBUG=True
API_V1_PREFIX=/api/v1
DEFAULT_CITY_ID=hyderabad

# API Authentication Key
API_KEYS=["dev-api-key-12345", "test-api-key-67890", "sih_flood_secret_key_2024"]

# Database & Cache (Defaults to local PostgreSQL & Redis)
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/flood_engine
SYNC_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/flood_engine
REDIS_URL=redis://localhost:6379/0

# Hydrology & Inundation Parameters
RADAR_STALENESS_THRESHOLD_MINUTES=15
MARSHALL_PALMER_A=200.0
MARSHALL_PALMER_B=1.6
CYCLE_DT_SECONDS=300.0
CRITICAL_FLOOD_DEPTH_CM=15.0
CAUTION_FLOOD_DEPTH_CM=5.0
ROUTING_PENALTY_BETA=8.0
```

---

## 2. Order of Operations Overview

To ensure all cache files, neural surrogate weights, and terrain rasters exist before the API boots, follow this exact sequence:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        ORDER OF OPERATIONS                             │
├────────────────────────────────────────────────────────────────────────┤
│  1. PREPROCESSING & PROVISIONING (Before turning Backend on)          │
│     ├── Ingest/Train Terrain: Precompute D8 Flow & Curve Numbers       │
│     ├── Ingest/Train Drainage: Build igraph & Conduits Topology        │
│     ├── Fetch Live IMD Doppler Radar: Calibrate dBZ Matrices           │
│     └── Train/Export GNN Surrogate: Generate surrogate_gnn.onnx        │
│                                                                        │
│  2. DATABASE MIGRATIONS (Optional if using PostGIS)                    │
│     └── alembic upgrade head                                           │
│                                                                        │
│  3. START BACKEND APPLICATION                                          

']]v                                                                                             6 f  │
│     ├── Terminal 1: FastAPI Uvicorn Server (Port 8000)                 │
│     ├── Terminal 2: ARQ Background Pipeline Worker                     │
│     └── Terminal 3: IMD Live Radar Poller Daemon                       │
│                                                                        │
│  4. START FRONTEND APPLICATION                                         │
│     └── Terminal 4: Vite Dev Server (Port 5173)                        │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Pre-Backend Offline Preparation & Preprocessing Pipeline

Before starting the web server, you must generate the required cached binary matrices (`flow_direction.npy`, `curve_number.npy`, `drainage_topology.json`, `surrogate_gnn.onnx`, and radar data).

### 3.1 Multi-City Automated Ingestion (Recommended Fast Path)

The engine provides a unified CLI `src.offline.ingest_city` that runs terrain conditioning, drainage graph construction, GNN surrogate training, and live IMD radar fetching in one go.

#### Option A: Provision Specific Metropolitan City
```powershell
# Provision Hyderabad
python -m src.offline.ingest_city --city hyderabad

# Provision Mumbai
python -m src.offline.ingest_city --city mumbai

# Provision Chennai
python -m src.offline.ingest_city --city chennai

# Provision Delhi NCR
python -m src.offline.ingest_city --city delhi

# Provision Bengaluru
python -m src.offline.ingest_city --city bengaluru

# Provision Kolkata
python -m src.offline.ingest_city --city kolkata
```

#### Option B: Provision All Registered Indian Metropolitan Cities
```powershell
python -m src.offline.ingest_city --all-cities
```

---

### 3.2 Step 1: Terrain Ingestion & D8 Elevation Preprocessing

If you want to run the terrain conditioning independently:

```powershell
python -m src.offline.train_terrain --city hyderabad --grid-res 300 --cell-size 30.0
```

**What this step executes:**
1. Loads raw Digital Elevation Model (.tif GeoTIFF) or synthesizes real-world topography for the city's bounding box.
2. Performs sink pit-filling and flat-surface resolution using depression-filling algorithms (`pyflwdir` / `DEMPreprocessor`).
3. Computes steepest descent **D8 flow direction matrix** (codes: 1, 2, 4, 8, 16, 32, 64, 128).
4. Generates **flow accumulation grid** and **SCS Curve Number (CN) urban imperviousness grid**.
5. Precomputes **1D flattened ridge-to-valley topological routing vectors** for zero-latency runtime overland flux routing.
6. Caches binary arrays in `data/cities/<city_id>/dem_cache/` and mirrors to `data/dem_cache/`.

---

### 3.3 Step 2: Drainage Network Parsing & igraph Construction

To parse municipal drainage networks, calculate Manning pipe conveyance capacities, and construct the directed graph:

```powershell
python -m src.offline.train_drainage --city hyderabad --epochs 10 --hidden-dim 32
```

**What this step executes:**
1. Parses municipal GIS drainage files (`.kml` or `.json`) from `data/cities/<city_id>/network/`.
2. Extracts stormwater junction nodes (inlets, manholes, storage basins, and outfalls).
3. Applies **Manning's open-channel and full-pipe equation** to calculate maximum gravity conveyance capacities:
   $$Q_{full} = \frac{1}{n} A R_h^{2/3} S^{1/2}$$
4. Constructs an `igraph` directed acyclic graph (DAG) structure capable of scaling to 50,000+ nodes.
5. Saves the parsed network to `data/cities/<city_id>/network/drainage_topology.json`.

---

### 3.4 Step 3: Real-Time IMD Radar Scraping & Ingestion

To test and ingest real Doppler Weather Radar (DWR) sweeps from the official India Meteorological Department portal:

```powershell
python -m src.core.imd_radar
```

**What this step executes:**
1. Connects to official IMD Doppler Radar endpoints (e.g., `https://mausam.imd.gov.in/Radar/caz_hyd.gif`, `caz_mum.gif`, `caz_chn.gif`).
2. Downloads the raw multi-band GIF/PNG radar sweep.
3. Decodes the color-mapped image pixels into a continuous calibrated reflectivity matrix (10 dBZ to 65 dBZ cloudburst scale).
4. Converts dBZ into Quantitative Precipitation Estimation (QPE in mm/hr) using Marshall-Palmer:
   $$Z = 200 R^{1.6} \implies R = \left(\frac{Z}{200}\right)^{1 / 1.6}$$
5. Saves the calibrated matrix to `data/cities/<city_id>/radar/latest_radar_dbz.npy`.

---

### 3.5 Step 4: EPA-SWMM Ground Truth Generation

To generate hydrodynamic dynamic-wave training pairs:

```powershell
python -m src.offline.swmm_groundtruth
```

**What this step executes:**
1. Synthesizes Chicago / SCS Type II design storm hyetographs (15 mm/hr to 120 mm/hr convective pulses).
2. Runs dynamic-wave Saint-Venant hydraulic routing with backwater and surcharge tracking.
3. Exports paired training datasets to `data/calibration/swmm_training_data.npz`.

---

### 3.6 Step 5: GNN Surrogate Model Training & ONNX Export

To train the message-passing Graph Neural Network surrogate and export to ONNX:

```powershell
python -m src.offline.gnn_training
```

**What this step executes:**
1. Reads dynamic-wave ground truth pairs.
2. Trains a spatial message-passing GNN model to predict nodal water depth and surcharge flow rates.
3. Exports the trained model to `data/surrogate_gnn.onnx` and city-specific model folders `data/cities/<city_id>/models/surrogate_gnn.onnx` with dynamic axes for ultra-fast CPU inference.

---

### 3.7 Step 6: Model Calibration & Accuracy Benchmarking

To compute formal hydrological verification metrics against held-out ground truth:

```powershell
python -m src.offline.calibration
```

**What this step executes:**
1. Calculates **Probability of Detection (POD)**: $TP / (TP + FN)$
2. Calculates **False Alarm Rate (FAR)**: $FP / (TP + FP)$
3. Calculates **Critical Success Index (CSI / Threat Score)**: $TP / (TP + FP + FN)$
4. Calculates Depth **MAE** and **RMSE** across 5 cm (caution) and 15 cm (impassable barrier) thresholds.
5. Generates `data/calibration/calibration_report.json`.

---

### 3.8 Ingesting Custom City Datasets (.tif DEM & .kml Drains)

If you have real municipal GeoTIFF rasters and KML canal maps:

1. Copy your `.tif` elevation raster to `data/dem/city_dem.tif` (or `data/cities/<city_id>/dem/`).
2. Copy your municipal `.kml` drainage map to `data/network/drains.kml` (or `data/cities/<city_id>/network/`).
3. Run the automated ingestion script:

```powershell
python -m src.offline.ingest_real_data
```

---

## 4. Database Provisioning & Alembic Migrations

*(Optional if running in in-memory / cache mode; required if persisting time-series historical nowcasts in PostgreSQL/PostGIS).*

### 4.1 Start Local PostgreSQL & Redis

If running PostgreSQL and Redis natively or via Docker:

```powershell
# Using Docker to run PostGIS and Redis only
docker run -d --name flood_pg -p 5432:5432 -e POSTGRES_DB=flood_engine -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres postgis/postgis:16-3.4
docker run -d --name flood_redis -p 6379:6379 redis:7-alpine
```

### 4.2 Apply Alembic Migrations

```powershell
# Run all schema migrations
alembic upgrade head
```

---

## 5. Starting the Backend Services

The complete backend runtime consists of three cooperating components:

### 5.1 Starting FastAPI Web & WebSocket Server

Open **Terminal 1** (with virtualenv activated):

```powershell
.venv\Scripts\Activate.ps1
python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

- **API Base URL**: `http://localhost:8000`
- **Interactive Swagger Docs**: `http://localhost:8000/docs`
- **ReDoc Documentation**: `http://localhost:8000/redoc`
- **Readiness Probe**: `http://localhost:8000/ready`
- **Prometheus Telemetry**: `http://localhost:8000/metrics`
- **WebSocket Depth Stream**: `ws://localhost:8000/ws/inundation`

---

### 5.2 Starting ARQ Background Task Worker

Open **Terminal 2** (with virtualenv activated):

```powershell
.venv\Scripts\Activate.ps1
python -m arq src.workers.pipeline_worker.WorkerSettings
```

- Listens for scheduled 5-minute nowcasting jobs dispatched via Redis.
- Orchestrates Stages 1 to 5 (Radar QPE $\to$ Overland D8 Routing $\to$ GNN Surrogate $\to$ Reservoir Storage Balance $\to$ Live Broadcast).

---

### 5.3 Starting IMD Radar Poller Daemon

Open **Terminal 3** (with virtualenv activated):

```powershell
.venv\Scripts\Activate.ps1
python -m src.workers.radar_poller
```

- Periodically scrapes the official IMD Doppler Weather Radar portal at a configurable interval (default: every 5 minutes).
- Automatically decodes updated reflectivity sweeps and triggers new nowcast cycles.

---

## 6. Starting the Frontend Web Application

The frontend is built with React 19, TypeScript, Vite, and Leaflet Web GIS.

### Step 6.1: Navigate to Frontend Directory & Install Packages

Open **Terminal 4**:

```powershell
cd frontend

# Install Node dependencies
npm install
```

### Step 6.2: Start Vite Development Server

```powershell
npm run dev
```

- **Frontend Application URL**: `http://localhost:5173` (or port indicated in console)
- The frontend will automatically load the Leaflet Web GIS map, connect to the backend REST API (`http://localhost:8000/api/v1`), and establish a persistent WebSocket connection with `ws://localhost:8000/ws/inundation`.

---

## 7. One-Command Multi-Service Docker Deployment

To launch the complete production stack (FastAPI API, ARQ Worker, TimescaleDB/PostGIS, Redis, Prometheus, and Grafana) inside isolated containers:

```powershell
# Build and start all microservices in detached mode
docker compose -f docker/docker-compose.yml up -d --build

# Inspect service container status
docker compose -f docker/docker-compose.yml ps

# View real-time logs across all services
docker compose -f docker/docker-compose.yml logs -f

# Teardown the stack when done
docker compose -f docker/docker-compose.yml down
```

### Exposed Service Ports in Docker Stack:
| Service | Port | Description & URL |
|---|---|---|
| **FastAPI Backend** | `8000` | REST API, WebSockets & Swagger: `http://localhost:8000/docs` |
| **PostgreSQL / PostGIS** | `5432` | Spatial database (User: `postgres`, Pass: `postgrespassword`) |
| **Redis Broker** | `6379` | In-memory message queue & cache |
| **Prometheus** | `9090` | Metrics scraper: `http://localhost:9090` |
| **Grafana Dashboard** | `3000` | Telemetry visualizer: `http://localhost:3000` (`admin` / `admin`) |

---

## 8. System Verification, Testing & Health Checks

### 8.1 API Health & Readiness Probes

Run these curl commands to confirm that the backend and cache are operational:

```powershell
# 1. Check Liveness Probe
curl http://localhost:8000/health

# 2. Check Readiness Probe (validates cached D8 rasters and GNN model)
curl http://localhost:8000/ready

# 3. Retrieve Registered Cities
curl -H "X-API-Key: dev-api-key-12345" http://localhost:8000/api/v1/cities

# 4. Retrieve Latest Flood Depths for Hyderabad
curl -H "X-API-Key: dev-api-key-12345" "http://localhost:8000/api/v1/nowcast/latest?city_id=hyderabad&horizon_min=15"

# 5. Test Live IMD Weather Analysis
curl -H "X-API-Key: dev-api-key-12345" "http://localhost:8000/api/v1/nowcast/weather-analysis?city_id=hyderabad"

# 6. Test Flood-Safe Route Calculation (avoiding 15 cm barriers)
curl -X POST "http://localhost:8000/api/v1/route/safe-path?city_id=hyderabad" `
  -H "Content-Type: application/json" `
  -H "X-API-Key: dev-api-key-12345" `
  -d '{"origin": {"latitude": 17.4400, "longitude": 78.4700}, "destination": {"latitude": 17.4100, "longitude": 78.4720}, "consider_forecast_horizon_min": 15}'
```

---

### 8.2 Running the Automated Test Suite

Execute the full pytest suite covering multi-city routing, mass-balance conservation, GNN inference, and radar QPE:

```powershell
# Run all unit and integration tests
.venv\Scripts\python -m pytest tests/ -v

# Run with full code coverage report
.venv\Scripts\python -m pytest tests/ --cov=src --cov-report=term-missing
```

---

## 9. Common Operational Workflows & Troubleshooting

| Issue / Symptom | Root Cause | Resolution |
|---|---|---|
| **`/ready` returns `"status": "initializing"`** | Precomputed terrain grids (`flow_direction.npy`) or GNN model missing. | Run `python -m src.offline.ingest_city --city hyderabad` to generate all caches. |
| **`401 Unauthorized` on API endpoints** | Missing `X-API-Key` header. | Add header `X-API-Key: dev-api-key-12345` or set `DEBUG=True` in `.env`. |
| **`429 Too Many Requests`** | Sliding window rate limit exceeded ($>120$ req/min). | Wait 60 seconds or increase `RATE_LIMIT_PER_MINUTE` in `src/config.py`. |
| **Radar status shows `"degraded"`** | IMD portal timeout or radar sweep older than 15 minutes. | The engine automatically falls back to rain-gauge IDW spatial interpolation and decaying storm models. |
| **WebSocket disconnects immediately** | Exceeded maximum concurrent WebSocket connection threshold ($500$). | Disconnect stale clients or increase `MAX_WS_CONNECTIONS` in `.env`. |
| **Frontend map displays offline tiles or blank layer** | Network restriction or missing coordinates. | Verify that internet connectivity is enabled for OpenStreetMap tile fetching or use cached tiles. |
