import React, { useState } from 'react';
import { StreetSegment, RiskLevel } from '../../types';
import { AlertOctagon, AlertTriangle, ShieldCheck, Search, ArrowUpDown, Navigation2, Droplets } from 'lucide-react';

interface LiveRiskFeedPanelProps {
  streets: StreetSegment[];
  selectedStreet: StreetSegment | null;
  onSelectStreet: (street: StreetSegment) => void;
  onTriggerRouteToStreet: (street: StreetSegment) => void;
}

export const LiveRiskFeedPanel: React.FC<LiveRiskFeedPanelProps> = ({
  streets,
  selectedStreet,
  onSelectStreet,
  onTriggerRouteToStreet
}) => {
  const [filterSeverity, setFilterSeverity] = useState<'all' | RiskLevel>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [sortBy, setSortBy] = useState<'depth' | 'velocity' | 'inflow'>('depth');

  // Filter and sort streets
  const filteredStreets = streets
    .filter(s => {
      if (filterSeverity !== 'all' && s.riskLevel !== filterSeverity) return false;
      if (searchQuery && !s.name.toLowerCase().includes(searchQuery.toLowerCase()) && !s.ward.toLowerCase().includes(searchQuery.toLowerCase())) return false;
      return true;
    })
    .sort((a, b) => {
      if (sortBy === 'depth') return b.waterDepthCm - a.waterDepthCm;
      if (sortBy === 'velocity') return b.flowVelocityMs - a.flowVelocityMs;
      return b.runoffInflowM3s - a.runoffInflowM3s;
    });

  const impassableCount = streets.filter(s => s.riskLevel === 'impassable').length;
  const cautionCount = streets.filter(s => s.riskLevel === 'caution').length;
  const safeCount = streets.filter(s => s.riskLevel === 'safe').length;

  return (
    <div style={{
      position: 'absolute',
      top: '84px',
      left: '24px',
      width: '420px',
      maxHeight: 'calc(100vh - 120px)',
      zIndex: 1050,
      background: 'rgba(13, 21, 39, 0.92)',
      backdropFilter: 'blur(16px)',
      border: '1px solid rgba(255, 255, 255, 0.1)',
      borderRadius: '16px',
      boxShadow: '0 12px 40px rgba(0, 0, 0, 0.6)',
      display: 'flex',
      flexDirection: 'column',
      overflow: 'hidden'
    }}>
      {/* Header */}
      <div style={{ padding: '18px 20px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <AlertTriangle size={18} color="#ef4444" />
            <span style={{ fontSize: '15px', fontWeight: 800, color: '#f8fafc' }}>
              Live Street Risk Feed
            </span>
          </div>
          <span style={{ fontSize: '11px', color: '#38bdf8', background: 'rgba(6, 182, 212, 0.15)', padding: '2px 8px', borderRadius: '9999px', fontWeight: 700 }}>
            {filteredStreets.length} Monitored
          </span>
        </div>
        <div style={{ fontSize: '12px', color: '#94a3b8' }}>
          Continuously ranked by overland runoff accumulation & conduit surcharge
        </div>

        {/* Severity Count Summary Pills */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', marginTop: '14px' }}>
          <button
            onClick={() => setFilterSeverity(filterSeverity === 'impassable' ? 'all' : 'impassable')}
            style={{
              padding: '6px 8px',
              borderRadius: '8px',
              background: filterSeverity === 'impassable' ? '#ef4444' : 'rgba(239, 68, 68, 0.15)',
              border: '1px solid rgba(239, 68, 68, 0.4)',
              color: '#ffffff',
              fontSize: '11px',
              fontWeight: 700,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '4px'
            }}
          >
            <AlertOctagon size={12} /> {impassableCount} Impassable
          </button>

          <button
            onClick={() => setFilterSeverity(filterSeverity === 'caution' ? 'all' : 'caution')}
            style={{
              padding: '6px 8px',
              borderRadius: '8px',
              background: filterSeverity === 'caution' ? '#f59e0b' : 'rgba(245, 158, 11, 0.15)',
              border: '1px solid rgba(245, 158, 11, 0.4)',
              color: '#ffffff',
              fontSize: '11px',
              fontWeight: 700,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '4px'
            }}
          >
            <AlertTriangle size={12} /> {cautionCount} Caution
          </button>

          <button
            onClick={() => setFilterSeverity(filterSeverity === 'safe' ? 'all' : 'safe')}
            style={{
              padding: '6px 8px',
              borderRadius: '8px',
              background: filterSeverity === 'safe' ? '#10b981' : 'rgba(16, 185, 129, 0.15)',
              border: '1px solid rgba(16, 185, 129, 0.4)',
              color: '#ffffff',
              fontSize: '11px',
              fontWeight: 700,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: '4px'
            }}
          >
            <ShieldCheck size={12} /> {safeCount} Safe
          </button>
        </div>

        {/* Search and Sort controls */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '12px' }}>
          <div style={{
            flex: 1,
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
            background: 'rgba(7, 11, 20, 0.7)',
            borderRadius: '8px',
            padding: '6px 10px',
            border: '1px solid rgba(255, 255, 255, 0.1)'
          }}>
            <Search size={14} color="#64748b" />
            <input
              type="text"
              placeholder="Search street, subway or ward..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              style={{
                background: 'transparent',
                border: 'none',
                color: '#f8fafc',
                fontSize: '12px',
                width: '100%',
                outline: 'none'
              }}
            />
          </div>

          <select
            value={sortBy}
            onChange={(e: any) => setSortBy(e.target.value)}
            style={{
              background: 'rgba(7, 11, 20, 0.7)',
              color: '#94a3b8',
              border: '1px solid rgba(255, 255, 255, 0.1)',
              borderRadius: '8px',
              padding: '6px 8px',
              fontSize: '11px',
              outline: 'none'
            }}
          >
            <option value="depth">Depth (cm)</option>
            <option value="velocity">Velocity (m/s)</option>
            <option value="inflow">Inflow (m³/s)</option>
          </select>
        </div>
      </div>

      {/* Street List */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '12px' }}>
        {filteredStreets.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '32px 16px', color: '#64748b', fontSize: '13px' }}>
            No streets match current filters
          </div>
        ) : (
          filteredStreets.map((street, idx) => {
            const isImpassable = street.waterDepthCm >= 15;
            const isCaution = street.waterDepthCm >= 5 && street.waterDepthCm < 15;
            const isSelected = selectedStreet?.id === street.id;

            const badgeColor = isImpassable ? '#ef4444' : isCaution ? '#f59e0b' : '#10b981';

            return (
              <div
                key={street.id}
                onClick={() => onSelectStreet(street)}
                style={{
                  background: isSelected ? 'rgba(56, 189, 248, 0.12)' : 'rgba(19, 31, 56, 0.6)',
                  border: isSelected ? '1px solid #38bdf8' : '1px solid rgba(255, 255, 255, 0.05)',
                  borderRadius: '10px',
                  padding: '12px 14px',
                  marginBottom: '8px',
                  cursor: 'pointer',
                  transition: 'all 0.2s ease',
                  position: 'relative'
                }}
              >
                {/* Ranking Index & Title */}
                <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '8px' }}>
                  <div style={{ display: 'flex', gap: '8px', alignItems: 'flex-start' }}>
                    <span style={{
                      fontSize: '11px',
                      fontWeight: 800,
                      color: '#64748b',
                      minWidth: '18px'
                    }}>
                      #{idx + 1}
                    </span>
                    <div>
                      <div style={{ fontSize: '13px', fontWeight: 700, color: '#f8fafc' }}>
                        {street.name}
                      </div>
                      <div style={{ fontSize: '11px', color: '#94a3b8' }}>
                        {street.ward}
                      </div>
                    </div>
                  </div>

                  {/* Water Depth Badge */}
                  <div style={{ textAlign: 'right' }}>
                    <span style={{
                      fontSize: '13px',
                      fontWeight: 800,
                      color: badgeColor,
                      display: 'block'
                    }}>
                      {street.waterDepthCm} cm
                    </span>
                    <span style={{
                      fontSize: '9px',
                      textTransform: 'uppercase',
                      color: badgeColor,
                      fontWeight: 800
                    }}>
                      {street.riskLevel}
                    </span>
                  </div>
                </div>

                {/* Metrics Breakdown */}
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  marginTop: '10px',
                  paddingTop: '8px',
                  borderTop: '1px solid rgba(255, 255, 255, 0.05)',
                  fontSize: '11px',
                  color: '#94a3b8'
                }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
                    <Droplets size={12} color="#38bdf8" />
                    <span>Inflow: <b style={{ color: '#f8fafc' }}>{street.runoffInflowM3s} m³/s</b></span>
                  </div>
                  <div>
                    <span>Cap: <b style={{ color: '#f8fafc' }}>{street.drainageCapacityM3s} m³/s</b></span>
                  </div>
                  <div>
                    <span>Velocity: <b style={{ color: '#38bdf8' }}>{street.flowVelocityMs} m/s</b></span>
                  </div>
                </div>

                {/* Quick Action: Route Around Barrier */}
                {isImpassable && (
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      onTriggerRouteToStreet(street);
                    }}
                    style={{
                      marginTop: '8px',
                      width: '100%',
                      background: 'rgba(139, 92, 246, 0.2)',
                      border: '1px solid rgba(139, 92, 246, 0.4)',
                      color: '#c084fc',
                      padding: '5px',
                      borderRadius: '6px',
                      fontSize: '11px',
                      fontWeight: 700,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      gap: '4px'
                    }}
                  >
                    <Navigation2 size={12} /> Compute Safe Detour Around This Barrier
                  </button>
                )}
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};
