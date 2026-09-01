import React, { useState } from 'react';
import { DrainageNode, DrainageConduit } from '../../types';
import { Wrench, AlertTriangle, CheckCircle2, FileText, Send, Filter, HardHat, Gauge } from 'lucide-react';

interface AdminDrainHealthPanelProps {
  nodes: DrainageNode[];
  conduits: DrainageConduit[];
}

export const AdminDrainHealthPanel: React.FC<AdminDrainHealthPanelProps> = ({
  nodes,
  conduits
}) => {
  const [filterBlockedOnly, setFilterBlockedOnly] = useState(false);
  const [dispatchedOrderId, setDispatchedOrderId] = useState<string | null>(null);

  const blockedConduits = conduits.filter(c => c.siltationFactor >= 0.5 || c.status === 'overflowing');
  const criticalNodes = nodes.filter(n => n.healthStatus === 'critical_blockage');

  const displayedConduits = filterBlockedOnly ? blockedConduits : conduits;

  const handleDispatchCrew = (conduitId: string) => {
    setDispatchedOrderId(conduitId);
    setTimeout(() => setDispatchedOrderId(null), 3000);
  };

  return (
    <div style={{
      position: 'absolute',
      top: '84px',
      left: '24px',
      width: '450px',
      maxHeight: 'calc(100vh - 120px)',
      zIndex: 1050,
      background: 'rgba(13, 21, 39, 0.94)',
      backdropFilter: 'blur(16px)',
      border: '1px solid rgba(245, 158, 11, 0.3)',
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
            <Wrench size={20} color="#f59e0b" />
            <span style={{ fontSize: '16px', fontWeight: 800, color: '#f8fafc' }}>
              Admin Drain-Health & Siltation View
            </span>
          </div>
          <span style={{ fontSize: '10px', background: 'rgba(245, 158, 11, 0.2)', color: '#fbbf24', padding: '2px 8px', borderRadius: '9999px', fontWeight: 700 }}>
            Municipal Operations
          </span>
        </div>
        <div style={{ fontSize: '12px', color: '#94a3b8' }}>
          Real-time pipe siltation index (κ) & manhole surcharge blockage detection
        </div>

        {/* Quick KPI Stats */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', marginTop: '14px' }}>
          <div style={{ background: 'rgba(239, 68, 68, 0.15)', border: '1px solid rgba(239, 68, 68, 0.3)', borderRadius: '8px', padding: '8px 10px' }}>
            <div style={{ fontSize: '9px', color: '#f87171' }}>CHOKED CONDUITS</div>
            <div style={{ fontSize: '15px', fontWeight: 800, color: '#ef4444' }}>
              {blockedConduits.length} Blockages
            </div>
          </div>

          <div style={{ background: 'rgba(245, 158, 11, 0.15)', border: '1px solid rgba(245, 158, 11, 0.3)', borderRadius: '8px', padding: '8px 10px' }}>
            <div style={{ fontSize: '9px', color: '#fbbf24' }}>SURCHARGED INLETS</div>
            <div style={{ fontSize: '15px', fontWeight: 800, color: '#f59e0b' }}>
              {criticalNodes.length} Inlets
            </div>
          </div>

          <div style={{ background: 'rgba(16, 185, 129, 0.15)', border: '1px solid rgba(16, 185, 129, 0.3)', borderRadius: '8px', padding: '8px 10px' }}>
            <div style={{ fontSize: '9px', color: '#34d399' }}>AVG CONDUIT CAP.</div>
            <div style={{ fontSize: '15px', fontWeight: 800, color: '#10b981' }}>
              5.8 m³/s
            </div>
          </div>
        </div>

        {/* Filter Switch */}
        <div style={{ marginTop: '12px', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <button
            onClick={() => setFilterBlockedOnly(!filterBlockedOnly)}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              padding: '6px 12px',
              borderRadius: '6px',
              fontSize: '11px',
              fontWeight: 700,
              background: filterBlockedOnly ? '#f59e0b' : 'rgba(255, 255, 255, 0.05)',
              color: filterBlockedOnly ? '#ffffff' : '#94a3b8',
              border: '1px solid rgba(255, 255, 255, 0.1)'
            }}
          >
            <Filter size={12} /> {filterBlockedOnly ? 'Showing Choked Drains Only' : 'Show All Monitored Conduits'}
          </button>

          <span style={{ fontSize: '11px', color: '#64748b' }}>
            Manning $n = 0.015$
          </span>
        </div>
      </div>

      {/* Conduits & Manhole Health List */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '16px' }}>
        {displayedConduits.map((cond) => {
          const isOverflowing = cond.status === 'overflowing';
          const isSilted = cond.siltationFactor >= 0.5;

          return (
            <div
              key={cond.id}
              style={{
                background: 'rgba(19, 31, 56, 0.7)',
                border: isOverflowing ? '1px solid #ef4444' : isSilted ? '1px solid #f59e0b' : '1px solid rgba(255,255,255,0.06)',
                borderRadius: '10px',
                padding: '12px 14px',
                marginBottom: '10px'
              }}
            >
              {/* Top Title & Status */}
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '6px' }}>
                <div>
                  <div style={{ fontSize: '13px', fontWeight: 700, color: '#f8fafc' }}>
                    Conduit: {cond.id}
                  </div>
                  <div style={{ fontSize: '10px', color: '#94a3b8' }}>
                    From: {cond.fromNode} ➔ To: {cond.toNode}
                  </div>
                </div>

                <span style={{
                  fontSize: '10px',
                  fontWeight: 800,
                  textTransform: 'uppercase',
                  padding: '2px 8px',
                  borderRadius: '4px',
                  background: isOverflowing ? '#ef4444' : isSilted ? '#f59e0b' : '#10b981',
                  color: '#ffffff'
                }}>
                  {cond.status}
                </span>
              </div>

              {/* Siltation & Capacity Meter */}
              <div style={{ marginTop: '8px', marginBottom: '8px' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '10px', color: '#94a3b8', marginBottom: '3px' }}>
                  <span>Siltation Index (κ Blockage):</span>
                  <span style={{ color: isSilted ? '#f59e0b' : '#10b981', fontWeight: 700 }}>
                    {(cond.siltationFactor * 100).toFixed(0)}% Silted
                  </span>
                </div>
                <div style={{ width: '100%', height: '6px', background: 'rgba(0,0,0,0.4)', borderRadius: '9999px', overflow: 'hidden' }}>
                  <div style={{
                    width: `${Math.min(100, cond.siltationFactor * 100)}%`,
                    height: '100%',
                    background: isSilted ? '#f59e0b' : '#10b981'
                  }} />
                </div>
              </div>

              {/* Hydraulic Metrics */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px', fontSize: '11px', color: '#94a3b8', background: 'rgba(0,0,0,0.2)', padding: '6px 8px', borderRadius: '6px' }}>
                <div>Flow / Max: <b style={{ color: isOverflowing ? '#ef4444' : '#f8fafc' }}>{cond.currentFlowM3s} / {cond.maxCapacityM3s} m³/s</b></div>
                <div>Utilization: <b style={{ color: isOverflowing ? '#ef4444' : '#38bdf8' }}>{cond.utilizationPercent.toFixed(1)}%</b></div>
                <div>Diameter: <b>{cond.diameterM} m</b></div>
                <div>Length: <b>{cond.lengthM} m</b></div>
              </div>

              {/* Dispatch Action */}
              {(isOverflowing || isSilted) && (
                <button
                  onClick={() => handleDispatchCrew(cond.id)}
                  style={{
                    marginTop: '10px',
                    width: '100%',
                    background: dispatchedOrderId === cond.id ? '#10b981' : 'rgba(245, 158, 11, 0.2)',
                    border: '1px solid rgba(245, 158, 11, 0.4)',
                    color: dispatchedOrderId === cond.id ? '#ffffff' : '#fbbf24',
                    padding: '6px',
                    borderRadius: '6px',
                    fontSize: '11px',
                    fontWeight: 700,
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    gap: '6px'
                  }}
                >
                  {dispatchedOrderId === cond.id ? (
                    <>
                      <CheckCircle2 size={13} /> Work Order #GHMC-902 Dispatched to Silt Crew
                    </>
                  ) : (
                    <>
                      <HardHat size={13} /> Dispatch Desilting Work-Order to Maintenance Crew
                    </>
                  )}
                </button>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
