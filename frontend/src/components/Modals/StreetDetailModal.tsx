import React from 'react';
import { StreetSegment } from '../../types';
import { X, Droplets, Gauge, Mountain, ShieldAlert, Route, Activity } from 'lucide-react';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

interface StreetDetailModalProps {
  street: StreetSegment;
  onClose: () => void;
  onNavigateAround: (street: StreetSegment) => void;
}

export const StreetDetailModal: React.FC<StreetDetailModalProps> = ({
  street,
  onClose,
  onNavigateAround
}) => {
  const isImpassable = street.waterDepthCm >= 15;
  const isCaution = street.waterDepthCm >= 5 && street.waterDepthCm < 15;
  const badgeColor = isImpassable ? '#ef4444' : isCaution ? '#f59e0b' : '#10b981';

  // Synthetic storage vs time data
  const hydrographData = [
    { time: 'T-30m', inflow: (street.runoffInflowM3s * 0.3).toFixed(1), capacity: street.drainageCapacityM3s, depth: (street.waterDepthCm * 0.2).toFixed(1) },
    { time: 'T-15m', inflow: (street.runoffInflowM3s * 0.7).toFixed(1), capacity: street.drainageCapacityM3s, depth: (street.waterDepthCm * 0.6).toFixed(1) },
    { time: 'NOW', inflow: street.runoffInflowM3s.toFixed(1), capacity: street.drainageCapacityM3s, depth: street.waterDepthCm.toFixed(1) },
    { time: 'T+15m', inflow: (street.runoffInflowM3s * 1.2).toFixed(1), capacity: street.drainageCapacityM3s, depth: (street.waterDepthCm * 1.25).toFixed(1) },
    { time: 'T+30m', inflow: (street.runoffInflowM3s * 0.8).toFixed(1), capacity: street.drainageCapacityM3s, depth: (street.waterDepthCm * 1.1).toFixed(1) },
    { time: 'T+60m', inflow: (street.runoffInflowM3s * 0.2).toFixed(1), capacity: street.drainageCapacityM3s, depth: (street.waterDepthCm * 0.4).toFixed(1) },
  ];

  return (
    <div style={{
      position: 'absolute',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      zIndex: 1200,
      background: 'rgba(0, 0, 0, 0.65)',
      backdropFilter: 'blur(8px)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '24px'
    }}>
      <div style={{
        width: '560px',
        maxHeight: '90vh',
        background: 'rgba(13, 21, 39, 0.98)',
        border: `1px solid ${badgeColor}`,
        borderRadius: '20px',
        boxShadow: '0 24px 60px rgba(0,0,0,0.8)',
        display: 'flex',
        flexDirection: 'column',
        overflow: 'hidden'
      }}>
        {/* Modal Header */}
        <div style={{ padding: '20px 24px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
              <span style={{ fontSize: '18px', fontWeight: 800, color: '#f8fafc' }}>
                {street.name}
              </span>
              <span style={{
                background: badgeColor,
                color: '#fff',
                fontSize: '10px',
                fontWeight: 800,
                padding: '2px 8px',
                borderRadius: '4px',
                textTransform: 'uppercase'
              }}>
                {street.riskLevel}
              </span>
            </div>
            <div style={{ fontSize: '12px', color: '#94a3b8', marginTop: '3px' }}>
              {street.ward} • Elevation: {street.elevationM}m MSL
            </div>
          </div>

          <button onClick={onClose} style={{ background: 'rgba(255,255,255,0.05)', color: '#94a3b8', padding: '6px', borderRadius: '8px' }}>
            <X size={18} />
          </button>
        </div>

        {/* Modal Body */}
        <div style={{ padding: '24px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>
          {/* Key Metrics Grid */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '10px' }}>
            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '10px', borderRadius: '10px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>WATER DEPTH</div>
              <div style={{ fontSize: '18px', fontWeight: 800, color: badgeColor, marginTop: '2px' }}>
                {street.waterDepthCm} cm
              </div>
            </div>

            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '10px', borderRadius: '10px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>FLOW VELOCITY</div>
              <div style={{ fontSize: '18px', fontWeight: 800, color: '#38bdf8', marginTop: '2px' }}>
                {street.flowVelocityMs} m/s
              </div>
            </div>

            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '10px', borderRadius: '10px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>RUNOFF INFLOW</div>
              <div style={{ fontSize: '18px', fontWeight: 800, color: '#f8fafc', marginTop: '2px' }}>
                {street.runoffInflowM3s} m³/s
              </div>
            </div>

            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '10px', borderRadius: '10px', textAlign: 'center' }}>
              <div style={{ fontSize: '10px', color: '#94a3b8' }}>DRAIN CAPACITY</div>
              <div style={{ fontSize: '18px', fontWeight: 800, color: '#10b981', marginTop: '2px' }}>
                {street.drainageCapacityM3s} m³/s
              </div>
            </div>
          </div>

          {/* Hydrodynamic Surcharge Chart */}
          <div style={{ background: 'rgba(7, 11, 20, 0.7)', borderRadius: '12px', padding: '14px', border: '1px solid rgba(255,255,255,0.06)' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '10px' }}>
              <span style={{ fontSize: '12px', fontWeight: 700, color: '#f8fafc', display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Activity size={14} color="#38bdf8" /> Nodal Inflow Flux vs Conveyance Hydrograph
              </span>
              <span style={{ fontSize: '10px', color: '#94a3b8' }}>Finite-Difference Reservoir Balance</span>
            </div>

            <div style={{ height: '140px', width: '100%' }}>
              <ResponsiveContainer width="100%" height="100%">
                <LineChart data={hydrographData}>
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                  <XAxis dataKey="time" stroke="#64748b" fontSize={10} />
                  <YAxis stroke="#64748b" fontSize={10} />
                  <Tooltip contentStyle={{ background: '#0d1527', borderColor: 'rgba(255,255,255,0.1)', borderRadius: '6px', fontSize: '11px' }} />
                  <Line type="monotone" dataKey="inflow" stroke="#38bdf8" strokeWidth={2} name="Runoff Q_in (m³/s)" />
                  <Line type="monotone" dataKey="capacity" stroke="#10b981" strokeDasharray="4 4" strokeWidth={2} name="Drainage Cap (m³/s)" />
                  <Line type="monotone" dataKey="depth" stroke="#ef4444" strokeWidth={2} name="Water Depth (cm)" />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Mathematical Formulations Badge */}
          <div style={{ background: 'rgba(6, 182, 212, 0.08)', border: '1px solid rgba(6, 182, 212, 0.2)', borderRadius: '10px', padding: '12px', fontSize: '11px', color: '#94a3b8', lineHeight: 1.5 }}>
            <b style={{ color: '#38bdf8' }}>Coupled Mass Conservation Model:</b><br/>
            {"Water volume update: S(t+1) = max(0, S(t) + (Q_in - Q_cap) * dt)"}<br/>
            {"Street ponding depth: h_street(t+1) = (S(t+1) / A_surface) * 100 cm"}
          </div>

          {/* Navigation Action */}
          {isImpassable && (
            <button
              onClick={() => {
                onClose();
                onNavigateAround(street);
              }}
              style={{
                background: 'linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%)',
                color: '#fff',
                padding: '12px',
                borderRadius: '10px',
                fontWeight: 700,
                fontSize: '13px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                gap: '8px',
                boxShadow: '0 0 20px rgba(139, 92, 246, 0.4)'
              }}
            >
              <Route size={16} /> Plan Safe Detour Around This Corridor
            </button>
          )}
        </div>
      </div>
    </div>
  );
};
