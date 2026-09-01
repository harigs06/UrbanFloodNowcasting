export type RiskLevel = 'safe' | 'caution' | 'impassable';

export interface CityConfig {
  id: string;
  name: string;
  state: string;
  center: [number, number]; // [lat, lng]
  zoom: number;
  radarStation: string;
  radarEndpoint: string;
  description: string;
}

export interface InundationPoint {
  id: string;
  name: string;
  coordinates: [number, number]; // [lat, lng]
  waterDepthCm: number;
  excessStorageM3: number;
  surchargeFlowM3s: number;
  riskLevel: RiskLevel;
  flowVelocityMs: number;
  nearestManholeId: string;
  lastUpdated: string;
}

export interface StreetSegment {
  id: string;
  name: string;
  ward: string;
  fromIntersection: string;
  toIntersection: string;
  lengthM: number;
  waterDepthCm: number;
  riskLevel: RiskLevel;
  flowVelocityMs: number;
  coordinates: [number, number][]; // LineString coords [[lat, lng], ...]
  blocked: boolean;
  elevationM: number;
  drainageCapacityM3s: number;
  runoffInflowM3s: number;
}

export interface DrainageNode {
  id: string;
  name: string;
  type: 'inlet' | 'manhole' | 'storage_basin' | 'outfall';
  coordinates: [number, number];
  rimElevationM: number;
  invertElevationM: number;
  surchargeDepthCm: number;
  isFlooded: boolean;
  siltationIndex: number; // 0.0 to 1.0 (clogging factor kappa)
  healthStatus: 'healthy' | 'warning' | 'critical_blockage';
}

export interface DrainageConduit {
  id: string;
  fromNode: string;
  toNode: string;
  lengthM: number;
  diameterM: number;
  slope: number;
  maxCapacityM3s: number;
  currentFlowM3s: number;
  utilizationPercent: number;
  siltationFactor: number;
  status: 'optimal' | 'congested' | 'overflowing' | 'blocked';
  coordinates: [number, number][];
}

export interface RouteStep {
  streetName: string;
  instruction: string;
  distanceM: number;
  durationSec: number;
  waterDepthCm: number;
  riskLevel: RiskLevel;
}

export interface SafeRouteResult {
  routeCoordinates: [number, number][];
  totalDistanceM: number;
  estimatedDurationMin: number;
  maxWaterDepthCm: number;
  avoidedFloodedSegments: number;
  riskScore: number; // 0 (safest) to 100 (hazardous)
  status: 'safe' | 'caution_advisory' | 'no_safe_route_found';
  steps: RouteStep[];
  vehicleType: 'car' | 'two_wheeler' | 'bus' | 'emergency';
  warningMessage?: string;
  errorMessage?: string;
}

export interface AlertNotification {
  id: string;
  timestamp: string;
  title: string;
  message: string;
  riskLevel: RiskLevel;
  locationName: string;
  waterDepthCm: number;
  coordinates?: [number, number];
  dismissed?: boolean;
}

export interface StormReplayFrame {
  timeOffsetMin: number; // e.g. -60, -30, 0, +30, +60, +120
  displayTime: string;
  rainfallIntensityMmHr: number;
  radarReflectivityDbz: number;
  inundatedStreetsCount: number;
  maxDepthCm: number;
  streetsData: Record<string, number>; // streetId -> waterDepthCm
  radarImage?: string;
}

export interface HistoricalStormScenario {
  id: string;
  cityName: string;
  eventTitle: string;
  date: string;
  peakRainfallMmHr: number;
  totalRainfallMm: number;
  description: string;
  frames: StormReplayFrame[];
}

export type ActiveTab = 'nowcast' | 'safe_routing';
export type HorizonMinute = 0 | 15 | 30 | 60 | 120 | 180;
