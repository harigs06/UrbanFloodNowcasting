import React from 'react';
import { CityConfig, ActiveTab } from '../types';
import { CITIES } from '../data/mockData';
import { 
  Route, 
  Map as MapIcon, 
  Radio, 
  Bell
} from 'lucide-react';

interface NavbarProps {
  activeCity: CityConfig;
  onSelectCity: (city: CityConfig) => void;
  activeTab: ActiveTab;
  onSelectTab: (tab: ActiveTab) => void;
  unreadAlertsCount: number;
  onToggleAlerts: () => void;
  isLiveWsConnected: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeCity,
  onSelectCity,
  activeTab,
  onSelectTab,
  unreadAlertsCount,
  onToggleAlerts,
  isLiveWsConnected
}) => {
  return (
    <header style={{
      position: 'absolute',
      top: 0,
      left: 0,
      right: 0,
      height: '68px',
      zIndex: 1100,
      background: 'rgba(7, 11, 20, 0.88)',
      backdropFilter: 'blur(16px)',
      borderBottom: '1px solid rgba(255, 255, 255, 0.08)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      padding: '0 24px'
    }}>
      {/* Center/Left: Navigation View Tabs */}
      <nav style={{
        display: 'flex',
        alignItems: 'center',
        background: 'rgba(13, 21, 39, 0.7)',
        padding: '4px',
        borderRadius: '12px',
        border: '1px solid rgba(255, 255, 255, 0.06)'
      }}>
        <button
          onClick={() => onSelectTab('nowcast')}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
            padding: '8px 16px',
            borderRadius: '8px',
            fontSize: '13px',
            fontWeight: 600,
            background: activeTab === 'nowcast' ? '#0284c7' : 'transparent',
            color: activeTab === 'nowcast' ? '#ffffff' : '#94a3b8'
          }}
        >
          <MapIcon size={16} /> Live Inundation Map
        </button>

        <button
          onClick={() => onSelectTab('safe_routing')}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
            padding: '8px 16px',
            borderRadius: '8px',
            fontSize: '13px',
            fontWeight: 600,
            background: activeTab === 'safe_routing' ? '#8b5cf6' : 'transparent',
            color: activeTab === 'safe_routing' ? '#ffffff' : '#94a3b8'
          }}
        >
          <Route size={16} /> Flood-Safe Routing
        </button>
      </nav>

      {/* Right: Multi-City Selector & Status Center */}
      <div style={{ display: 'flex', alignItems: 'center', gap: '14px' }}>
        {/* City Selector */}
        <select
          value={activeCity.id}
          onChange={(e) => {
            const found = CITIES.find(c => c.id === e.target.value);
            if (found) onSelectCity(found);
          }}
          style={{
            background: 'rgba(19, 31, 56, 0.9)',
            color: '#f8fafc',
            border: '1px solid rgba(255, 255, 255, 0.12)',
            padding: '8px 14px',
            borderRadius: '10px',
            fontSize: '13px',
            fontWeight: 600,
            outline: 'none',
            cursor: 'pointer'
          }}
        >
          {CITIES.map(c => (
            <option key={c.id} value={c.id} style={{ background: '#0d1527', color: '#f8fafc' }}>
              📍 {c.name} ({c.state})
            </option>
          ))}
        </select>

        {/* Live Radar Doppler Badge */}
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '8px',
          background: 'rgba(6, 182, 212, 0.1)',
          border: '1px solid rgba(6, 182, 212, 0.25)',
          padding: '6px 12px',
          borderRadius: '8px',
          fontSize: '12px',
          color: '#38bdf8'
        }}>
          <span style={{
            width: '8px',
            height: '8px',
            borderRadius: '50%',
            background: isLiveWsConnected ? '#10b981' : '#06b6d4',
            boxShadow: '0 0 8px currentColor'
          }} className="radar-live-dot" />
          <Radio size={14} />
          <span style={{ fontWeight: 600 }}>DWR {activeCity.radarStation}</span>
        </div>

        {/* Alerts Button */}
        <button
          onClick={onToggleAlerts}
          style={{
            position: 'relative',
            background: unreadAlertsCount > 0 ? 'rgba(239, 68, 68, 0.2)' : 'rgba(255, 255, 255, 0.05)',
            border: unreadAlertsCount > 0 ? '1px solid rgba(239, 68, 68, 0.5)' : '1px solid rgba(255, 255, 255, 0.1)',
            padding: '8px 12px',
            borderRadius: '10px',
            color: unreadAlertsCount > 0 ? '#ef4444' : '#94a3b8',
            display: 'flex',
            alignItems: 'center',
            gap: '6px',
            fontSize: '13px',
            fontWeight: 600
          }}
        >
          <Bell size={16} />
          <span>Alerts</span>
          {unreadAlertsCount > 0 && (
            <span style={{
              background: '#ef4444',
              color: '#ffffff',
              fontSize: '11px',
              fontWeight: 800,
              padding: '1px 6px',
              borderRadius: '9999px',
              marginLeft: '2px'
            }}>
              {unreadAlertsCount}
            </span>
          )}
        </button>
      </div>
    </header>
  );
};
