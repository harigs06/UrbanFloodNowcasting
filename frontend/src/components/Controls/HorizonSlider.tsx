import React, { useState, useEffect } from 'react';
import { HorizonMinute } from '../../types';
import { Play, Pause, Clock, CloudRain, Layers, Eye, EyeOff } from 'lucide-react';

interface HorizonSliderProps {
  selectedHorizon: HorizonMinute;
  onSelectHorizon: (h: HorizonMinute) => void;
  showRadar: boolean;
  onToggleRadar: () => void;
  showDrainage: boolean;
  onToggleDrainage: () => void;
}

const HORIZONS: HorizonMinute[] = [0, 15, 30, 60, 120, 180];

export const HorizonSlider: React.FC<HorizonSliderProps> = ({
  selectedHorizon,
  onSelectHorizon,
  showRadar,
  onToggleRadar,
  showDrainage,
  onToggleDrainage
}) => {
  const [isPlaying, setIsPlaying] = useState(false);

  useEffect(() => {
    let interval: any;
    if (isPlaying) {
      interval = setInterval(() => {
        const currentIdx = HORIZONS.indexOf(selectedHorizon);
        const nextIdx = (currentIdx + 1) % HORIZONS.length;
        onSelectHorizon(HORIZONS[nextIdx]);
      }, 3000);
    }
    return () => clearInterval(interval);
  }, [isPlaying, selectedHorizon, onSelectHorizon]);

  return (
    <div style={{
      position: 'absolute',
      bottom: '24px',
      left: '50%',
      transform: 'translateX(-50%)',
      zIndex: 1050,
      width: '780px',
      maxWidth: 'calc(100vw - 48px)',
      background: 'rgba(13, 21, 39, 0.92)',
      backdropFilter: 'blur(16px)',
      border: '1px solid rgba(255, 255, 255, 0.1)',
      borderRadius: '16px',
      boxShadow: '0 12px 40px rgba(0, 0, 0, 0.6)',
      padding: '16px 20px',
      display: 'flex',
      flexDirection: 'column',
      gap: '12px'
    }}>
      {/* Top row: Status, Play Button, Layer Toggles */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <button
            onClick={() => setIsPlaying(!isPlaying)}
            style={{
              width: '34px',
              height: '34px',
              borderRadius: '50%',
              background: isPlaying ? '#ef4444' : '#0284c7',
              color: '#ffffff',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              boxShadow: isPlaying ? '0 0 12px rgba(239,68,68,0.5)' : '0 0 12px rgba(2,132,199,0.5)'
            }}
            title={isPlaying ? 'Pause Nowcast Loop' : 'Play Forward Simulation'}
          >
            {isPlaying ? <Pause size={16} /> : <Play size={16} style={{ marginLeft: '2px' }} />}
          </button>

          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Clock size={15} color="#38bdf8" />
              <span style={{ fontSize: '13px', fontWeight: 700, color: '#f8fafc' }}>
                Forecast Horizon: {selectedHorizon === 0 ? 'NOW (0 min)' : `+${selectedHorizon} Minutes (${(selectedHorizon / 60).toFixed(1)} hrs)`}
              </span>
            </div>
            <div style={{ fontSize: '11px', color: '#94a3b8' }}>
              Optical Flow Advection & Finite-Difference Mass Balance
            </div>
          </div>
        </div>

        {/* Layer Toggles */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <button
            onClick={onToggleRadar}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              padding: '6px 12px',
              borderRadius: '8px',
              fontSize: '12px',
              fontWeight: 600,
              background: showRadar ? 'rgba(6, 182, 212, 0.2)' : 'rgba(255, 255, 255, 0.05)',
              border: showRadar ? '1px solid #06b6d4' : '1px solid rgba(255, 255, 255, 0.1)',
              color: showRadar ? '#38bdf8' : '#64748b'
            }}
          >
            <CloudRain size={14} /> Radar QPE {showRadar ? <Eye size={12} /> : <EyeOff size={12} />}
          </button>

          <button
            onClick={onToggleDrainage}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              padding: '6px 12px',
              borderRadius: '8px',
              fontSize: '12px',
              fontWeight: 600,
              background: showDrainage ? 'rgba(245, 158, 11, 0.2)' : 'rgba(255, 255, 255, 0.05)',
              border: showDrainage ? '1px solid #f59e0b' : '1px solid rgba(255, 255, 255, 0.1)',
              color: showDrainage ? '#fbbf24' : '#64748b'
            }}
          >
            <Layers size={14} /> Drains & Inlets {showDrainage ? <Eye size={12} /> : <EyeOff size={12} />}
          </button>
        </div>
      </div>

      {/* Horizon Step Pills */}
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(6, 1fr)',
        gap: '8px',
        background: 'rgba(7, 11, 20, 0.6)',
        padding: '6px',
        borderRadius: '12px'
      }}>
        {HORIZONS.map((h) => {
          const isActive = selectedHorizon === h;
          return (
            <button
              key={h}
              onClick={() => onSelectHorizon(h)}
              style={{
                padding: '8px 4px',
                borderRadius: '8px',
                background: isActive ? 'linear-gradient(135deg, #0284c7 0%, #2563eb 100%)' : 'transparent',
                color: isActive ? '#ffffff' : '#94a3b8',
                fontWeight: isActive ? 700 : 500,
                fontSize: '12px',
                boxShadow: isActive ? '0 0 12px rgba(2,132,199,0.5)' : 'none',
                textAlign: 'center'
              }}
            >
              {h === 0 ? 'NOW' : `+${h}m`}
            </button>
          );
        })}
      </div>
    </div>
  );
};
