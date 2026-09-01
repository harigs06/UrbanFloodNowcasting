import React from 'react';
import { CityConfig, StreetSegment, SafeRouteResult } from '../../types';
import { Route, ShieldCheck, AlertOctagon, ArrowRight, CornerDownRight, RefreshCw, CheckCircle2 } from 'lucide-react';

interface FloodSafeRoutePanelProps {
  city: CityConfig;
  streets: StreetSegment[];
  originCoord: [number, number] | null;
  destinationCoord: [number, number] | null;
  safeRoute: SafeRouteResult | null;
  onSetOrigin: (coord: [number, number]) => void;
  onSetDestination: (coord: [number, number]) => void;
  onCalculateRoute: (vehicleType: 'car' | 'two_wheeler' | 'bus' | 'emergency') => void;
  onClearRoute: () => void;
  isCalculating: boolean;
}

export const FloodSafeRoutePanel: React.FC<FloodSafeRoutePanelProps> = ({
  city,
  streets,
  originCoord,
  destinationCoord,
  safeRoute,
  onSetOrigin,
  onSetDestination,
  onCalculateRoute,
  onClearRoute,
  isCalculating
}) => {
  // Preset location hubs for active city across all available streets
  const presetLocations = React.useMemo(() => {
    const seen = new Set<string>();
    const list: { name: string; coords: [number, number] }[] = [];
    for (const s of streets) {
      if (s.name && !seen.has(s.name) && s.coordinates && s.coordinates.length > 0) {
        seen.add(s.name);
        list.push({
          name: s.name,
          coords: s.coordinates[0] || city.center
        });
      }
    }
    return list.sort((a, b) => a.name.localeCompare(b.name));
  }, [streets, city.center]);

  const isRouteBlockedOrFailed = safeRoute && (safeRoute.status === 'no_safe_route_found' || safeRoute.steps.length === 0);

  return (
    <div style={{
      position: 'absolute',
      top: '84px',
      left: '24px',
      width: '440px',
      maxHeight: 'calc(100vh - 120px)',
      zIndex: 1050,
      background: 'rgba(13, 21, 39, 0.94)',
      backdropFilter: 'blur(16px)',
      border: '1px solid rgba(139, 92, 246, 0.3)',
      borderRadius: '16px',
      boxShadow: '0 12px 40px rgba(0, 0, 0, 0.6)',
      display: 'flex',
      flexDirection: 'column',
      overflow: 'hidden'
    }}>
      {/* Header */}
      <div style={{ padding: '18px 20px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <Route size={20} color="#c084fc" />
            <span style={{ fontSize: '16px', fontWeight: 800, color: '#f8fafc' }}>
              Flood-Safe A* Navigation
            </span>
          </div>
          <span style={{ fontSize: '10px', background: 'rgba(139, 92, 246, 0.2)', color: '#c084fc', padding: '2px 8px', borderRadius: '9999px', fontWeight: 700 }}>
            Dynamic Impedance
          </span>
        </div>
        <div style={{ fontSize: '12px', color: '#94a3b8' }}>
          Automatically prunes &ge;15cm submerged corridors & minimizes hydrodynamic drag
        </div>

        {/* Origin / Destination Pickers */}
        <div style={{ marginTop: '14px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
          {/* Origin Picker */}
          <div>
            <label style={{ fontSize: '11px', color: '#10b981', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '4px' }}>
              <span>🟢</span> START LOCATION (ORIGIN A)
            </label>
            <div style={{ display: 'flex', gap: '6px' }}>
              <select
                onChange={(e) => {
                  if (e.target.value) {
                    const val = JSON.parse(e.target.value);
                    onSetOrigin(val);
                  }
                }}
                style={{
                  flex: 1,
                  background: 'rgba(7, 11, 20, 0.7)',
                  color: '#f8fafc',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                  borderRadius: '8px',
                  padding: '7px 10px',
                  fontSize: '12px',
                  outline: 'none'
                }}
              >
                <option value="">Select origin preset or click on map...</option>
                {presetLocations.map((loc, i) => (
                  <option key={i} value={JSON.stringify(loc.coords)}>
                    {loc.name}
                  </option>
                ))}
              </select>
            </div>
            {originCoord && (
              <div style={{ fontSize: '10px', color: '#10b981', marginTop: '2px' }}>
                Coordinates: [{originCoord[0].toFixed(4)}, {originCoord[1].toFixed(4)}]
              </div>
            )}
          </div>

          {/* Destination Picker */}
          <div>
            <label style={{ fontSize: '11px', color: '#ef4444', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px', marginBottom: '4px' }}>
              <span>🔴</span> DESTINATION (TARGET B)
            </label>
            <div style={{ display: 'flex', gap: '6px' }}>
              <select
                onChange={(e) => {
                  if (e.target.value) {
                    const val = JSON.parse(e.target.value);
                    onSetDestination(val);
                  }
                }}
                style={{
                  flex: 1,
                  background: 'rgba(7, 11, 20, 0.7)',
                  color: '#f8fafc',
                  border: '1px solid rgba(255, 255, 255, 0.1)',
                  borderRadius: '8px',
                  padding: '7px 10px',
                  fontSize: '12px',
                  outline: 'none'
                }}
              >
                <option value="">Select destination preset or click on map...</option>
                {presetLocations.map((loc, i) => (
                  <option key={i} value={JSON.stringify(loc.coords)}>
                    {loc.name}
                  </option>
                ))}
              </select>
            </div>
            {destinationCoord && (
              <div style={{ fontSize: '10px', color: '#ef4444', marginTop: '2px' }}>
                Coordinates: [{destinationCoord[0].toFixed(4)}, {destinationCoord[1].toFixed(4)}]
              </div>
            )}
          </div>
        </div>

        {/* Action Buttons */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '14px' }}>
          <button
            onClick={() => onCalculateRoute('car')}
            disabled={isCalculating || !originCoord || !destinationCoord}
            style={{
              flex: 1,
              background: 'linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%)',
              color: '#ffffff',
              padding: '10px',
              borderRadius: '8px',
              fontSize: '13px',
              fontWeight: 700,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '6px',
              boxShadow: '0 0 16px rgba(139, 92, 246, 0.4)',
              opacity: isCalculating || !originCoord || !destinationCoord ? 0.6 : 1,
              cursor: isCalculating || !originCoord || !destinationCoord ? 'not-allowed' : 'pointer'
            }}
          >
            {isCalculating ? <RefreshCw size={15} className="radar-live-dot" /> : <Route size={15} />}
            {isCalculating ? 'Computing Safe A* Path...' : 'Find Flood-Safe Route'}
          </button>

          {safeRoute && (
            <button
              onClick={onClearRoute}
              style={{
                background: 'rgba(255, 255, 255, 0.08)',
                color: '#94a3b8',
                padding: '10px 14px',
                borderRadius: '8px',
                fontSize: '12px',
                fontWeight: 600,
                cursor: 'pointer'
              }}
            >
              Reset
            </button>
          )}
        </div>
      </div>

      {/* Route Results & Turn-by-Turn Guidance */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '16px' }}>
        {!safeRoute ? (
          <div style={{ textAlign: 'center', padding: '32px 16px', color: '#64748b', fontSize: '13px' }}>
            <div style={{ fontSize: '28px', marginBottom: '8px' }}>🚗</div>
            Select start and destination points to compute a real-time flood-safe navigation path.
          </div>
        ) : isRouteBlockedOrFailed ? (
          /* Error / Impassable State */
          <div style={{
            background: 'rgba(239, 68, 68, 0.12)',
            border: '1px solid rgba(239, 68, 68, 0.35)',
            borderRadius: '12px',
            padding: '16px'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: '#ef4444', fontWeight: 800, fontSize: '14px', marginBottom: '8px' }}>
              <AlertOctagon size={18} />
              <span>{safeRoute.errorMessage ? 'Backend Connection Error' : 'No Safe Route Found'}</span>
            </div>
            <div style={{ fontSize: '12px', color: '#f87171', lineHeight: '1.5' }}>
              {safeRoute.errorMessage || safeRoute.warningMessage || 'All viable paths between these points are currently blocked by deep inundation (>=15cm) or no road connection exists.'}
            </div>
            <div style={{ marginTop: '12px', fontSize: '11px', color: '#94a3b8' }}>
              💡 <b>Recommendation:</b> Try switching to the <b>Rescue (NDRF)</b> mode for higher water clearance, or choose higher-elevation alternative waypoints.
            </div>
          </div>
        ) : (
          /* Success: Real Calculated Route */
          <div>
            {/* Route KPI Summary Grid */}
            <div style={{
              background: 'rgba(139, 92, 246, 0.12)',
              border: '1px solid rgba(139, 92, 246, 0.3)',
              borderRadius: '12px',
              padding: '14px',
              marginBottom: '14px'
            }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '10px', color: '#c084fc', fontWeight: 800, fontSize: '13px' }}>
                <CheckCircle2 size={16} /> SAFE DETOUR PATH COMPUTED
              </div>

              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px' }}>
                <div style={{ background: 'rgba(0, 0, 0, 0.3)', padding: '8px 10px', borderRadius: '8px' }}>
                  <div style={{ fontSize: '10px', color: '#94a3b8' }}>TOTAL DISTANCE</div>
                  <div style={{ fontSize: '16px', fontWeight: 800, color: '#f8fafc' }}>
                    {(safeRoute.totalDistanceM / 1000).toFixed(2)} km
                  </div>
                </div>

                <div style={{ background: 'rgba(0, 0, 0, 0.3)', padding: '8px 10px', borderRadius: '8px' }}>
                  <div style={{ fontSize: '10px', color: '#94a3b8' }}>ESTIMATED TIME</div>
                  <div style={{ fontSize: '16px', fontWeight: 800, color: '#38bdf8' }}>
                    {safeRoute.estimatedDurationMin} mins
                  </div>
                </div>

                <div style={{ background: 'rgba(0, 0, 0, 0.3)', padding: '8px 10px', borderRadius: '8px' }}>
                  <div style={{ fontSize: '10px', color: '#94a3b8' }}>MAX WATER DEPTH</div>
                  <div style={{ fontSize: '16px', fontWeight: 800, color: '#10b981' }}>
                    {safeRoute.maxWaterDepthCm} cm
                  </div>
                </div>

                <div style={{ background: 'rgba(0, 0, 0, 0.3)', padding: '8px 10px', borderRadius: '8px' }}>
                  <div style={{ fontSize: '10px', color: '#94a3b8' }}>SAFETY STATUS</div>
                  <div style={{ fontSize: '14px', fontWeight: 800, color: safeRoute.status === 'safe' ? '#10b981' : '#f59e0b', textTransform: 'capitalize' }}>
                    {safeRoute.status.replace('_', ' ')}
                  </div>
                </div>
              </div>
            </div>

            {/* Turn-by-Turn Steps */}
            <div style={{ fontSize: '12px', fontWeight: 700, color: '#94a3b8', marginBottom: '8px' }}>
              TURN-BY-TURN GUIDANCE ({safeRoute.steps.length} segments)
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
              {safeRoute.steps.map((st, i) => (
                <div
                  key={i}
                  style={{
                    background: 'rgba(19, 31, 56, 0.6)',
                    border: '1px solid rgba(255, 255, 255, 0.06)',
                    borderRadius: '8px',
                    padding: '10px 12px',
                    display: 'flex',
                    alignItems: 'flex-start',
                    gap: '10px'
                  }}
                >
                  <CornerDownRight size={16} color="#c084fc" style={{ marginTop: '2px' }} />
                  <div style={{ flex: 1 }}>
                    <div style={{ fontSize: '13px', fontWeight: 700, color: '#f8fafc' }}>
                      {st.streetName}
                    </div>
                    <div style={{ fontSize: '11px', color: '#94a3b8', marginTop: '2px' }}>
                      {st.instruction}
                    </div>
                    <div style={{ display: 'flex', gap: '12px', marginTop: '6px', fontSize: '10px', color: '#64748b' }}>
                      <span>Distance: <b>{st.distanceM} m</b></span>
                      <span>Water Depth: <b style={{ color: st.waterDepthCm >= 5 ? '#f59e0b' : '#10b981' }}>{st.waterDepthCm} cm</b></span>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
