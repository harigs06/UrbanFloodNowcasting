import React, { useEffect, useRef } from 'react';
import L from 'leaflet';
import { CityConfig, StreetSegment, DrainageNode, DrainageConduit, SafeRouteResult, RiskLevel } from '../../types';

interface GISMapProps {
  city: CityConfig;
  streets: StreetSegment[];
  drainageNodes?: DrainageNode[];
  drainageConduits?: DrainageConduit[];
  safeRoute?: SafeRouteResult | null;
  selectedStreet?: StreetSegment | null;
  onSelectStreet?: (street: StreetSegment) => void;
  onMapClickCoord?: (coord: [number, number]) => void;
  showRadarOverlay?: boolean;
  showDrainageLayer?: boolean;
  routingModeActive?: boolean;
  originCoord?: [number, number] | null;
  destinationCoord?: [number, number] | null;
}

export const GISMap: React.FC<GISMapProps> = ({
  city,
  streets,
  drainageNodes = [],
  drainageConduits = [],
  safeRoute,
  selectedStreet,
  onSelectStreet,
  onMapClickCoord,
  showRadarOverlay = true,
  showDrainageLayer = false,
  routingModeActive = false,
  originCoord,
  destinationCoord
}) => {
  const mapContainerRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);
  const layersGroupRef = useRef<L.FeatureGroup | null>(null);
  const routeLayerRef = useRef<L.FeatureGroup | null>(null);
  const drainageLayerRef = useRef<L.FeatureGroup | null>(null);
  const radarOverlayRef = useRef<L.Circle | null>(null);

  // Initialize Map
  useEffect(() => {
    if (!mapContainerRef.current) return;

    if (!mapInstanceRef.current) {
      const map = L.map(mapContainerRef.current, {
        center: city.center,
        zoom: city.zoom,
        zoomControl: false,
        attributionControl: false
      });

      // Esri World Dark Gray Canvas Tiles (100% Free, No Watermark, No API Key Required)
      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 16,
        attribution: 'Esri, DeLorme, NAVTEQ'
      }).addTo(map);

      L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Reference/MapServer/tile/{z}/{y}/{x}', {
        maxZoom: 16
      }).addTo(map);

      // Attribution
      L.control.attribution({ position: 'bottomright', prefix: 'Urban Flood Nowcasting Engine | IMD DWR' }).addTo(map);
      L.control.zoom({ position: 'topright' }).addTo(map);

      layersGroupRef.current = L.featureGroup().addTo(map);
      routeLayerRef.current = L.featureGroup().addTo(map);
      drainageLayerRef.current = L.featureGroup().addTo(map);

      // Map click handler
      map.on('click', (e: L.LeafletMouseEvent) => {
        if (onMapClickCoord) {
          onMapClickCoord([e.latlng.lat, e.latlng.lng]);
        }
      });

      mapInstanceRef.current = map;
    }

    return () => {
      if (mapInstanceRef.current) {
        mapInstanceRef.current.remove();
        mapInstanceRef.current = null;
      }
    };
  }, []);

  // Update map view when city changes
  useEffect(() => {
    if (mapInstanceRef.current) {
      mapInstanceRef.current.flyTo(city.center, city.zoom, { duration: 1.2 });
    }
  }, [city]);

  // Render Street Inundation Polylines
  useEffect(() => {
    if (!mapInstanceRef.current || !layersGroupRef.current) return;
    const group = layersGroupRef.current;
    group.clearLayers();

    streets.forEach((street) => {
      const isImpassable = street.waterDepthCm >= 15;
      const isCaution = street.waterDepthCm >= 5 && street.waterDepthCm < 15;
      const isSelected = selectedStreet?.id === street.id;

      const strokeColor = isImpassable ? '#ef4444' : isCaution ? '#f59e0b' : '#10b981';
      const weight = isSelected ? 8 : isImpassable ? 6 : 4;
      const opacity = isSelected ? 1.0 : 0.85;

      const polyline = L.polyline(street.coordinates, {
        color: strokeColor,
        weight: weight,
        opacity: opacity,
        lineCap: 'round',
        lineJoin: 'round',
        dashArray: isImpassable ? '6, 6' : undefined
      });

      // Interactive Popup
      const popupHtml = `
        <div style="font-family: inherit; font-size: 13px; line-height: 1.4; min-width: 200px;">
          <div style="font-weight: 700; color: #f8fafc; font-size: 14px; margin-bottom: 4px; display: flex; align-items: center; justify-content: space-between;">
            <span>${street.name}</span>
            <span style="font-size: 10px; padding: 2px 6px; border-radius: 4px; background: ${isImpassable ? '#ef4444' : isCaution ? '#f59e0b' : '#10b981'}; color: #fff; font-weight: 800; text-transform: uppercase;">
              ${street.riskLevel}
            </span>
          </div>
          <div style="color: #94a3b8; font-size: 11px; margin-bottom: 8px;">${street.ward}</div>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; background: rgba(0,0,0,0.3); padding: 8px; border-radius: 6px; margin-bottom: 6px;">
            <div>
              <div style="color: #64748b; font-size: 10px;">WATER DEPTH</div>
              <div style="color: ${strokeColor}; font-weight: 700; font-size: 15px;">${street.waterDepthCm} cm</div>
            </div>
            <div>
              <div style="color: #64748b; font-size: 10px;">VELOCITY</div>
              <div style="color: #38bdf8; font-weight: 700; font-size: 15px;">${street.flowVelocityMs} m/s</div>
            </div>
            <div>
              <div style="color: #64748b; font-size: 10px;">INFLOW FLUX</div>
              <div style="color: #f8fafc; font-weight: 600;">${street.runoffInflowM3s} m³/s</div>
            </div>
            <div>
              <div style="color: #64748b; font-size: 10px;">CONDUIT CAP.</div>
              <div style="color: #f8fafc; font-weight: 600;">${street.drainageCapacityM3s} m³/s</div>
            </div>
          </div>
          ${isImpassable ? '<div style="color: #f87171; font-weight: 600; font-size: 11px; margin-top: 4px;">⚠️ BARRIER ACTIVE: Closed to light vehicular traffic</div>' : ''}
        </div>
      `;

      polyline.bindPopup(popupHtml);
      polyline.on('click', () => {
        if (onSelectStreet) onSelectStreet(street);
      });

      group.addLayer(polyline);

      // Add Barrier Pulse Marker if Impassable
      if (isImpassable && street.coordinates.length > 0) {
        const midIdx = Math.floor(street.coordinates.length / 2);
        const midPoint = street.coordinates[midIdx];

        const barrierIcon = L.divIcon({
          className: 'barrier-marker',
          html: `
            <div style="width: 22px; height: 22px; border-radius: 50%; background: #ef4444; border: 2px solid #ffffff; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 11px; box-shadow: 0 0 12px rgba(239,68,68,0.8); animation: pulse-critical 1.5s infinite;">
              ✕
            </div>
          `,
          iconSize: [22, 22],
          iconAnchor: [11, 11]
        });

        const barrierMarker = L.marker(midPoint, { icon: barrierIcon });
        barrierMarker.bindPopup(`<b>${street.name}</b><br/>Water Depth: <b>${street.waterDepthCm} cm</b> (Impassable Cutoff)`);
        group.addLayer(barrierMarker);
      }
    });
  }, [streets, selectedStreet, onSelectStreet]);

  // Render Radar Overlay
  useEffect(() => {
    if (!mapInstanceRef.current) return;

    if (radarOverlayRef.current) {
      radarOverlayRef.current.remove();
      radarOverlayRef.current = null;
    }

    if (showRadarOverlay) {
      // Create radar coverage radial zone
      radarOverlayRef.current = L.circle(city.center, {
        radius: 8500,
        color: '#06b6d4',
        weight: 1,
        fillColor: '#0284c7',
        fillOpacity: 0.12,
        dashArray: '4, 8'
      }).addTo(mapInstanceRef.current);
    }
  }, [city, showRadarOverlay]);

  // Render Drainage Network Layer
  useEffect(() => {
    if (!mapInstanceRef.current || !drainageLayerRef.current) return;
    const group = drainageLayerRef.current;
    group.clearLayers();

    if (!showDrainageLayer) return;

    // Render conduits
    drainageConduits.forEach((cond) => {
      const isBlocked = cond.status === 'overflowing' || cond.siltationFactor > 0.5;
      const color = isBlocked ? '#ec4899' : '#06b6d4';

      const poly = L.polyline(cond.coordinates, {
        color: color,
        weight: 3,
        opacity: 0.7,
        dashArray: '3, 6'
      });
      poly.bindPopup(`<b>Conduit: ${cond.id}</b><br/>Flow: ${cond.currentFlowM3s} / ${cond.maxCapacityM3s} m³/s<br/>Siltation: ${(cond.siltationFactor * 100).toFixed(0)}%`);
      group.addLayer(poly);
    });

    // Render nodes / manholes
    drainageNodes.forEach((node) => {
      const isWarning = node.healthStatus === 'critical_blockage';
      const marker = L.circleMarker(node.coordinates, {
        radius: isWarning ? 7 : 5,
        fillColor: isWarning ? '#f43f5e' : '#38bdf8',
        color: '#ffffff',
        weight: 1.5,
        fillOpacity: 0.9
      });
      marker.bindPopup(`<b>${node.name}</b> (${node.type})<br/>Surcharge: ${node.surchargeDepthCm} cm<br/>Siltation Index: ${(node.siltationIndex * 100).toFixed(0)}%`);
      group.addLayer(marker);
    });
  }, [showDrainageLayer, drainageNodes, drainageConduits]);

  // Render Safe Route Navigation Layer & Origin/Destination Pins
  useEffect(() => {
    if (!mapInstanceRef.current || !routeLayerRef.current) return;
    const group = routeLayerRef.current;
    group.clearLayers();

    // Origin Pin
    if (originCoord) {
      const originIcon = L.divIcon({
        className: 'origin-marker',
        html: `
          <div style="background: #10b981; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; border: 2px solid white; box-shadow: 0 0 10px rgba(16,185,129,0.8);">
            A
          </div>
        `,
        iconSize: [28, 28],
        iconAnchor: [14, 14]
      });
      group.addLayer(L.marker(originCoord, { icon: originIcon }).bindPopup('<b>Origin Point (Start)</b>'));
    }

    // Destination Pin
    if (destinationCoord) {
      const destIcon = L.divIcon({
        className: 'dest-marker',
        html: `
          <div style="background: #ef4444; color: white; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: bold; border: 2px solid white; box-shadow: 0 0 10px rgba(239,68,68,0.8);">
            B
          </div>
        `,
        iconSize: [28, 28],
        iconAnchor: [14, 14]
      });
      group.addLayer(L.marker(destinationCoord, { icon: destIcon }).bindPopup('<b>Destination Point (End)</b>'));
    }

    // Safe Route Line
    if (safeRoute && safeRoute.routeCoordinates.length > 1) {
      // Glow underlay
      const glowLine = L.polyline(safeRoute.routeCoordinates, {
        color: '#8b5cf6',
        weight: 10,
        opacity: 0.4
      });
      group.addLayer(glowLine);

      // Core line
      const mainLine = L.polyline(safeRoute.routeCoordinates, {
        color: '#c084fc',
        weight: 5,
        opacity: 0.95
      });
      group.addLayer(mainLine);
    }
  }, [originCoord, destinationCoord, safeRoute]);

  return (
    <div style={{ position: 'relative', width: '100%', height: '100%' }}>
      <div ref={mapContainerRef} style={{ width: '100%', height: '100%' }} />

      {/* Map Interactive Hint Badge */}
      {routingModeActive && (
        <div style={{
          position: 'absolute',
          top: '20px',
          left: '50%',
          transform: 'translateX(-50%)',
          zIndex: 1000,
          background: 'rgba(13, 21, 39, 0.9)',
          backdropFilter: 'blur(8px)',
          border: '1px solid rgba(139, 92, 246, 0.5)',
          padding: '8px 18px',
          borderRadius: '9999px',
          color: '#c084fc',
          fontSize: '13px',
          fontWeight: 600,
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          boxShadow: '0 4px 20px rgba(0,0,0,0.5)',
          pointerEvents: 'none'
        }}>
          <span>📍</span> Click anywhere on map to set Origin (A) and Destination (B)
        </div>
      )}
    </div>
  );
};
