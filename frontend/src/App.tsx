import React, { useState, useEffect, useCallback } from 'react';
import {
  CityConfig,
  ActiveTab,
  HorizonMinute,
  StreetSegment,
  DrainageNode,
  DrainageConduit,
  SafeRouteResult,
  AlertNotification,
  RiskLevel
} from './types';
import { CITIES, INITIAL_ALERTS, getCityStreets } from './data/mockData';
import { fetchStreetsInundation, fetchDrainageNetwork, calculateSafeRoute } from './services/api';
import { inundationWs } from './services/websocket';

// Components
import { Navbar } from './components/Navbar';
import { GISMap } from './components/Map/GISMap';
import { FloodSafeRoutePanel } from './components/Panels/FloodSafeRoutePanel';
import { AlertsPanel } from './components/Panels/AlertsPanel';
import { StreetDetailModal } from './components/Modals/StreetDetailModal';

// Initial fallback streets for Hyderabad
const HYDERABAD_STREETS_INITIAL = getCityStreets('hyderabad');

export const App: React.FC = () => {
  // Global State
  const [activeCity, setActiveCity] = useState<CityConfig>(CITIES[0]);
  const [activeTab, setActiveTab] = useState<ActiveTab>('nowcast');
  const [selectedHorizon, setSelectedHorizon] = useState<HorizonMinute>(15);

  // Data State
  const [streets, setStreets] = useState<StreetSegment[]>(HYDERABAD_STREETS_INITIAL);
  const [drainageNodes, setDrainageNodes] = useState<DrainageNode[]>([]);
  const [drainageConduits, setDrainageConduits] = useState<DrainageConduit[]>([]);
  const [backendError, setBackendError] = useState<string | null>(null);

  // Selection & Modals
  const [selectedStreet, setSelectedStreet] = useState<StreetSegment | null>(null);
  const [showAlertsDrawer, setShowAlertsDrawer] = useState<boolean>(false);
  const [alerts, setAlerts] = useState<AlertNotification[]>(INITIAL_ALERTS);

  // Map Layer Toggles
  const [showRadar, setShowRadar] = useState<boolean>(true);
  const [showDrainage, setShowDrainage] = useState<boolean>(false);

  // Routing State
  const [originCoord, setOriginCoord] = useState<[number, number] | null>(null);
  const [destinationCoord, setDestinationCoord] = useState<[number, number] | null>(null);
  const [safeRoute, setSafeRoute] = useState<SafeRouteResult | null>(null);
  const [isCalculatingRoute, setIsCalculatingRoute] = useState<boolean>(false);
  const [isLiveWsConnected, setIsLiveWsConnected] = useState<boolean>(false);

  // Load city streets & drainage data
  useEffect(() => {
    async function loadData() {
      const loadedStreets = await fetchStreetsInundation(activeCity.id, selectedHorizon);
      setStreets(loadedStreets);

      const drainage = await fetchDrainageNetwork(activeCity.id);
      setDrainageNodes(drainage.nodes);
      setDrainageConduits(drainage.conduits);

      // Reset routing when city switches
      setOriginCoord(null);
      setDestinationCoord(null);
      setSafeRoute(null);
    }
    loadData();
  }, [activeCity, selectedHorizon]);

  // WebSocket Subscription
  useEffect(() => {
    inundationWs.connect();
    const unsubscribe = inundationWs.subscribe((data) => {
      setIsLiveWsConnected(true);
      if (data) {
        if (data.type === 'nowcast_update' || data.type === 'connection_established') {
          // Live nowcast cycle completed on backend - fetch updated state
          fetchStreetsInundation(activeCity.id, selectedHorizon).then(updatedStreets => {
            setStreets(updatedStreets);
          });
        } else if (data.points && Array.isArray(data.points)) {
          setStreets(prev => prev.map(st => {
            const pt = data.points.find((p: any) => p.entity_id === st.id || p.node_id === st.id || p.id === st.id);
            if (pt) {
              const depth = Number(pt.water_depth_cm.toFixed(1));
              return {
                ...st,
                waterDepthCm: depth,
                riskLevel: (pt.risk_level as any) || (depth >= 15 ? 'impassable' : depth >= 5 ? 'caution' : 'safe'),
                blocked: depth >= 15
              };
            }
            return st;
          }));
        }
      }
    });

    return () => {
      unsubscribe();
      inundationWs.disconnect();
    };
  }, [activeCity.id, selectedHorizon]);

  // Handle map click in routing mode
  const handleMapClickCoord = useCallback((coord: [number, number]) => {
    if (activeTab === 'safe_routing') {
      if (!originCoord) {
        setOriginCoord(coord);
      } else if (!destinationCoord) {
        setDestinationCoord(coord);
      } else {
        // If both already set, reset and start over
        setOriginCoord(coord);
        setDestinationCoord(null);
        setSafeRoute(null);
      }
    }
  }, [activeTab, originCoord, destinationCoord]);

  // Calculate Safe Route
  const handleCalculateRoute = async (vehicleType: 'car' | 'two_wheeler' | 'bus' | 'emergency') => {
    if (!originCoord || !destinationCoord) return;
    setIsCalculatingRoute(true);
    try {
      const result = await calculateSafeRoute(activeCity.id, originCoord, destinationCoord, vehicleType, streets);
      setSafeRoute(result);
    } finally {
      setIsCalculatingRoute(false);
    }
  };

  // Trigger Safe Route around a specific flooded street
  const handleTriggerRouteToStreet = (street: StreetSegment) => {
    setActiveTab('safe_routing');
    const start: [number, number] = [street.coordinates[0][0] - 0.015, street.coordinates[0][1] - 0.015];
    const end: [number, number] = [street.coordinates[street.coordinates.length - 1][0] + 0.015, street.coordinates[street.coordinates.length - 1][1] + 0.015];
    setOriginCoord(start);
    setDestinationCoord(end);
    handleCalculateRoute('car');
  };

  // Add Broadcast Emergency Alert
  const handleAddBroadcastAlert = (title: string, message: string, riskLevel: RiskLevel, locationName: string) => {
    const newAlert: AlertNotification = {
      id: `alt-${Date.now()}`,
      timestamp: 'Just now',
      title,
      message,
      riskLevel,
      locationName,
      waterDepthCm: riskLevel === 'impassable' ? 24.0 : 8.0
    };
    setAlerts(prev => [newAlert, ...prev]);
  };

  return (
    <div style={{ position: 'relative', width: '100vw', height: '100vh', overflow: 'hidden', background: '#070b14' }}>
      {/* Top Navigation Bar */}
      <Navbar
        activeCity={activeCity}
        onSelectCity={setActiveCity}
        activeTab={activeTab}
        onSelectTab={setActiveTab}
        unreadAlertsCount={alerts.length}
        onToggleAlerts={() => setShowAlertsDrawer(!showAlertsDrawer)}
        isLiveWsConnected={isLiveWsConnected}
      />

      {/* Main Interactive Leaflet Web GIS Map */}
      <main style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0 }}>
        <GISMap
          city={activeCity}
          streets={streets}
          drainageNodes={drainageNodes}
          drainageConduits={drainageConduits}
          safeRoute={safeRoute}
          selectedStreet={selectedStreet}
          onSelectStreet={setSelectedStreet}
          onMapClickCoord={handleMapClickCoord}
          showRadarOverlay={showRadar}
          showDrainageLayer={showDrainage}
          routingModeActive={activeTab === 'safe_routing'}
          originCoord={originCoord}
          destinationCoord={destinationCoord}
        />
      </main>

      {/* Floating Active Feature Panels */}
      {activeTab === 'safe_routing' && (
        <FloodSafeRoutePanel
          city={activeCity}
          streets={streets}
          originCoord={originCoord}
          destinationCoord={destinationCoord}
          safeRoute={safeRoute}
          onSetOrigin={setOriginCoord}
          onSetDestination={setDestinationCoord}
          onCalculateRoute={handleCalculateRoute}
          onClearRoute={() => {
            setOriginCoord(null);
            setDestinationCoord(null);
            setSafeRoute(null);
          }}
          isCalculating={isCalculatingRoute}
        />
      )}

      {/* Emergency Alerts Drawer */}
      {showAlertsDrawer && (
        <AlertsPanel
          alerts={alerts}
          onDismissAlert={(id) => setAlerts(prev => prev.filter(a => a.id !== id))}
          onClearAll={() => setAlerts([])}
          onClose={() => setShowAlertsDrawer(false)}
          onAddBroadcastAlert={handleAddBroadcastAlert}
        />
      )}

      {/* Street Detail Hydrograph Modal */}
      {selectedStreet && (
        <StreetDetailModal
          street={selectedStreet}
          onClose={() => setSelectedStreet(null)}
          onNavigateAround={handleTriggerRouteToStreet}
        />
      )}
    </div>
  );
};

export default App;


