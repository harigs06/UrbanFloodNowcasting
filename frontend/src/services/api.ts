import { CityConfig, StreetSegment, DrainageNode, DrainageConduit, SafeRouteResult, HorizonMinute } from '../types';
import { CITIES, DRAINAGE_NODES_HYD, DRAINAGE_CONDUITS_HYD, getCityStreets } from '../data/mockData';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';
const API_KEY = import.meta.env.VITE_API_KEY || 'dev-api-key-12345';

const headers: HeadersInit = {
  'Content-Type': 'application/json',
  'X-API-Key': API_KEY,
};

export async function fetchCities(): Promise<CityConfig[]> {
  try {
    const res = await fetch(`${API_BASE_URL}/cities`, { headers });
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data) && data.length > 0) {
        return data.map((c: any) => ({
          id: c.city_id,
          name: c.display_name,
          state: c.state,
          center: [c.center_coords[0], c.center_coords[1]],
          zoom: 13,
          radarStation: `${c.radar_station_code} (${c.radar_endpoint_key})`,
          radarEndpoint: `https://mausam.imd.gov.in/Radar/${c.radar_endpoint_key}.gif`,
          description: `${c.state} Regional Metropolitan Watershed`
        }));
      }
    }
  } catch (err) {
    console.debug('[API] fetchCities fallback to local configs:', err);
  }
  return CITIES;
}

export async function fetchStreetsInundation(
  cityId: string,
  horizonMin: HorizonMinute = 15
): Promise<StreetSegment[]> {
  const baseStreets = getCityStreets(cityId);

  try {
    const res = await fetch(
      `${API_BASE_URL}/nowcast/streets?city_id=${cityId}&horizon_min=${horizonMin}`,
      { headers }
    );
    if (res.ok) {
      const data = await res.json();
      if (Array.isArray(data)) {
        // Map real calculated backend inundation depths to street network
        return baseStreets.map(st => {
          const pt = data.find((d: any) => 
            d.entity_id === st.id || 
            d.entity_id === st.name || 
            d.node_id === st.id ||
            d.entity_id?.toLowerCase() === st.id?.toLowerCase()
          );
          if (pt) {
            const depth = Number(pt.water_depth_cm.toFixed(1));
            const surcharge = Number((pt.surcharge_flow_m3s || 0).toFixed(2));
            return {
              ...st,
              waterDepthCm: depth,
              riskLevel: (pt.risk_level as any) || (depth >= 15 ? 'impassable' : depth >= 5 ? 'caution' : 'safe'),
              blocked: depth >= 15,
              runoffInflowM3s: Number((st.runoffInflowM3s + surcharge).toFixed(1)),
            };
          }
          return {
            ...st,
            waterDepthCm: 0.0,
            riskLevel: 'safe',
            blocked: false,
          };
        });
      }
    }
  } catch (err) {
    console.error('[API] fetchStreetsInundation failed to reach backend:', err);
  }

  // Return base streets with zero inundation when offline (No fake math/simulated numbers)
  return baseStreets.map(st => ({
    ...st,
    waterDepthCm: 0.0,
    riskLevel: 'safe',
    blocked: false
  }));
}

export async function fetchDrainageNetwork(cityId: string): Promise<{ nodes: DrainageNode[]; conduits: DrainageConduit[] }> {
  try {
    const [nodesRes, conduitsRes] = await Promise.all([
      fetch(`${API_BASE_URL}/drainage/nodes?city_id=${cityId}`, { headers }),
      fetch(`${API_BASE_URL}/drainage/conduits?city_id=${cityId}`, { headers }),
    ]);

    if (nodesRes.ok && conduitsRes.ok) {
      const nodesData = await nodesRes.json();
      const conduitsData = await conduitsRes.json();

      if (Array.isArray(nodesData) && nodesData.length > 0) {
        const mappedNodes: DrainageNode[] = nodesData.map((n: any) => ({
          id: n.id,
          name: n.name,
          type: (n.node_type === 'outfall' ? 'outfall' : n.node_type === 'storage' ? 'storage_basin' : n.node_type === 'manhole' ? 'manhole' : 'inlet'),
          coordinates: [n.latitude, n.longitude],
          rimElevationM: n.rim_elevation_m || 512.0,
          invertElevationM: n.invert_elevation_m || 508.0,
          surchargeDepthCm: 0,
          isFlooded: n.is_outfall || false,
          siltationIndex: 0.25,
          healthStatus: n.is_outfall ? 'healthy' : 'warning'
        }));

        const mappedConduits: DrainageConduit[] = conduitsData.map((c: any) => ({
          id: c.id,
          fromNode: c.from_node_id,
          toNode: c.to_node_id,
          lengthM: c.length_m || 400,
          diameterM: c.diameter_m || 1.5,
          slope: c.slope || 0.005,
          maxCapacityM3s: c.full_capacity_m3s || 4.5,
          currentFlowM3s: Number(((c.full_capacity_m3s || 4.5) * 0.6).toFixed(1)),
          utilizationPercent: 60,
          siltationFactor: 0.2,
          status: 'optimal',
          coordinates: []
        }));

        return { nodes: mappedNodes, conduits: mappedConduits };
      }
    }
  } catch (err) {
    console.error('[API] fetchDrainageNetwork error:', err);
  }

  // Return empty network on failure (No fake/dummy fallback nodes)
  return {
    nodes: [],
    conduits: []
  };
}

export async function calculateSafeRoute(
  cityId: string,
  startCoord: [number, number],
  endCoord: [number, number],
  vehicleType: 'car' | 'two_wheeler' | 'bus' | 'emergency' = 'car',
  streets: StreetSegment[] = []
): Promise<SafeRouteResult> {
  try {
    const res = await fetch(`${API_BASE_URL}/route/safe-path?city_id=${cityId}`, {
      method: 'POST',
      headers,
      body: JSON.stringify({
        origin: { latitude: startCoord[0], longitude: startCoord[1] },
        destination: { latitude: endCoord[0], longitude: endCoord[1] },
        vehicle_type: vehicleType,
        consider_forecast_horizon_min: 15
      })
    });

    if (res.ok) {
      const data = await res.json();
      if (data.path_found) {
        // Backend returns geometry as [[lon, lat], ...] -> Leaflet requires [[lat, lon], ...]
        const leafletCoords: [number, number][] = (data.geometry && data.geometry.length > 0)
          ? data.geometry.map((c: [number, number]) => [c[1], c[0]])
          : [startCoord, endCoord];

        const blockedCount = streets.filter(s => s.blocked || s.waterDepthCm >= 15).length;
        const maxDepth = data.max_flood_depth_encountered_cm || 0.0;

        return {
          routeCoordinates: leafletCoords,
          totalDistanceM: data.total_distance_m || 0,
          estimatedDurationMin: Number(((data.estimated_travel_time_seconds || 60) / 60).toFixed(1)),
          maxWaterDepthCm: maxDepth,
          avoidedFloodedSegments: blockedCount,
          riskScore: maxDepth >= 15 ? 90 : maxDepth >= 5 ? 35 : 8,
          status: data.overall_safety_rating === 'safe' ? 'safe' : (maxDepth >= 15 ? 'no_safe_route_found' : 'caution_advisory'),
          vehicleType,
          steps: (data.steps && data.steps.length > 0) ? data.steps.map((s: any) => ({
            streetName: s.street_name,
            instruction: `Proceed along ${s.street_name} (${s.water_depth_cm > 0 ? `${s.water_depth_cm}cm depth` : 'Clear passage'})`,
            distanceM: Math.round(s.length_m),
            durationSec: Math.round(s.length_m / 11),
            waterDepthCm: s.water_depth_cm,
            riskLevel: (s.risk_level as any) || 'safe'
          })) : []
        };
      } else {
        // Path blocked or not found by real A* search
        return {
          routeCoordinates: [],
          totalDistanceM: 0,
          estimatedDurationMin: 0,
          maxWaterDepthCm: data.max_flood_depth_encountered_cm || 0.0,
          avoidedFloodedSegments: 0,
          riskScore: 100,
          status: 'no_safe_route_found',
          vehicleType,
          steps: [],
          warningMessage: data.warning_message || 'All viable paths between these points are blocked by deep flooding (>=15cm) or lack connected road geometry.'
        };
      }
    } else {
      const errData = await res.json().catch(() => ({}));
      return {
        routeCoordinates: [],
        totalDistanceM: 0,
        estimatedDurationMin: 0,
        maxWaterDepthCm: 0,
        avoidedFloodedSegments: 0,
        riskScore: 100,
        status: 'no_safe_route_found',
        vehicleType,
        steps: [],
        errorMessage: errData.detail || `Route computation failed with status ${res.status}.`
      };
    }
  } catch (err: any) {
    console.error('[API] calculateSafeRoute backend error:', err);
    return {
      routeCoordinates: [],
      totalDistanceM: 0,
      estimatedDurationMin: 0,
      maxWaterDepthCm: 0,
      avoidedFloodedSegments: 0,
      riskScore: 100,
      status: 'no_safe_route_found',
      vehicleType,
      steps: [],
      errorMessage: 'Backend connection failed. Please verify that the FastAPI backend server is running at http://localhost:8000.'
    };
  }
}

export async function fetchLiveWeatherAnalysis(cityId: string): Promise<any> {
  try {
    const res = await fetch(`${API_BASE_URL}/nowcast/weather-analysis?city_id=${cityId}`, { headers });
    if (res.ok) {
      return await res.json();
    }
  } catch (err) {
    console.debug('[API] fetchLiveWeatherAnalysis error:', err);
  }
  return null;
}

export async function triggerLiveNowcast(cityId: string): Promise<any> {
  try {
    const res = await fetch(`${API_BASE_URL}/nowcast/trigger-live?city_id=${cityId}`, {
      method: 'POST',
      headers,
    });
    if (res.ok) {
      return await res.json();
    }
  } catch (err) {
    console.debug('[API] triggerLiveNowcast error:', err);
  }
  return null;
}

