import React, { useState } from 'react';
import { AlertNotification, RiskLevel } from '../../types';
import { Bell, AlertTriangle, AlertOctagon, X, Volume2, VolumeX, Send, ShieldAlert, Check } from 'lucide-react';

interface AlertsPanelProps {
  alerts: AlertNotification[];
  onDismissAlert: (id: string) => void;
  onClearAll: () => void;
  onClose: () => void;
  onAddBroadcastAlert: (title: string, message: string, risk: RiskLevel, location: string) => void;
}

export const AlertsPanel: React.FC<AlertsPanelProps> = ({
  alerts,
  onDismissAlert,
  onClearAll,
  onClose,
  onAddBroadcastAlert
}) => {
  const [soundEnabled, setSoundEnabled] = useState(true);
  const [isComposing, setIsComposing] = useState(false);
  const [composeTitle, setComposeTitle] = useState('');
  const [composeMessage, setComposeMessage] = useState('');
  const [composeLocation, setComposeLocation] = useState('');
  const [composeRisk, setComposeRisk] = useState<RiskLevel>('impassable');

  const handleBroadcast = (e: React.FormEvent) => {
    e.preventDefault();
    if (!composeTitle || !composeMessage) return;
    onAddBroadcastAlert(composeTitle, composeMessage, composeRisk, composeLocation || 'City-Wide');
    setComposeTitle('');
    setComposeMessage('');
    setComposeLocation('');
    setIsComposing(false);
  };

  return (
    <div style={{
      position: 'absolute',
      top: '84px',
      right: '24px',
      width: '420px',
      maxHeight: 'calc(100vh - 120px)',
      zIndex: 1150,
      background: 'rgba(13, 21, 39, 0.96)',
      backdropFilter: 'blur(20px)',
      border: '1px solid rgba(239, 68, 68, 0.4)',
      borderRadius: '16px',
      boxShadow: '0 16px 48px rgba(0, 0, 0, 0.7)',
      display: 'flex',
      flexDirection: 'column',
      overflow: 'hidden'
    }}>
      {/* Header */}
      <div style={{ padding: '16px 20px', borderBottom: '1px solid rgba(255, 255, 255, 0.08)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <div style={{ width: '28px', height: '28px', borderRadius: '50%', background: 'rgba(239, 68, 68, 0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Bell size={16} color="#ef4444" />
          </div>
          <div>
            <div style={{ fontSize: '15px', fontWeight: 800, color: '#f8fafc' }}>
              Emergency Alert Stream
            </div>
            <div style={{ fontSize: '11px', color: '#94a3b8' }}>
              {alerts.length} active emergency bulletins
            </div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          <button
            onClick={() => setSoundEnabled(!soundEnabled)}
            style={{ background: 'rgba(255,255,255,0.05)', color: soundEnabled ? '#10b981' : '#64748b', padding: '6px', borderRadius: '6px' }}
            title={soundEnabled ? 'Mute Alert Chimes' : 'Enable Alert Chimes'}
          >
            {soundEnabled ? <Volume2 size={15} /> : <VolumeX size={15} />}
          </button>

          <button
            onClick={onClose}
            style={{ background: 'rgba(255,255,255,0.05)', color: '#94a3b8', padding: '6px', borderRadius: '6px' }}
          >
            <X size={15} />
          </button>
        </div>
      </div>

      {/* Action Bar */}
      <div style={{ padding: '10px 20px', background: 'rgba(7, 11, 20, 0.5)', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid rgba(255, 255, 255, 0.05)' }}>
        <button
          onClick={() => setIsComposing(!isComposing)}
          style={{
            background: isComposing ? '#ef4444' : 'rgba(239, 68, 68, 0.2)',
            border: '1px solid rgba(239, 68, 68, 0.4)',
            color: '#ffffff',
            padding: '5px 10px',
            borderRadius: '6px',
            fontSize: '11px',
            fontWeight: 700,
            display: 'flex',
            alignItems: 'center',
            gap: '4px'
          }}
        >
          <ShieldAlert size={12} /> {isComposing ? 'Cancel Broadcast' : '+ Broadcast CAP Emergency Alert'}
        </button>

        {alerts.length > 0 && (
          <button
            onClick={onClearAll}
            style={{ background: 'transparent', color: '#64748b', fontSize: '11px', fontWeight: 600 }}
          >
            Clear All
          </button>
        )}
      </div>

      {/* Compose Emergency Alert Form */}
      {isComposing && (
        <form onSubmit={handleBroadcast} style={{ padding: '14px 20px', background: 'rgba(19, 31, 56, 0.9)', borderBottom: '1px solid rgba(255, 255, 255, 0.1)', display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <div style={{ fontSize: '12px', fontWeight: 700, color: '#f87171' }}>
            CIVIC BROADCAST COMPOSER (NDRF / POLICE)
          </div>
          <input
            type="text"
            placeholder="Alert Headline (e.g. FLASH FLOOD WARNING: PVNR Underpass)"
            value={composeTitle}
            onChange={(e) => setComposeTitle(e.target.value)}
            required
            style={{ background: 'rgba(7, 11, 20, 0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '6px', padding: '6px 10px', color: '#fff', fontSize: '12px', outline: 'none' }}
          />
          <input
            type="text"
            placeholder="Location (e.g. Begumpet Corridor)"
            value={composeLocation}
            onChange={(e) => setComposeLocation(e.target.value)}
            style={{ background: 'rgba(7, 11, 20, 0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '6px', padding: '6px 10px', color: '#fff', fontSize: '12px', outline: 'none' }}
          />
          <textarea
            placeholder="Detailed instructions for citizens & emergency transit..."
            value={composeMessage}
            onChange={(e) => setComposeMessage(e.target.value)}
            required
            rows={2}
            style={{ background: 'rgba(7, 11, 20, 0.8)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '6px', padding: '6px 10px', color: '#fff', fontSize: '12px', outline: 'none', resize: 'none' }}
          />
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <select
              value={composeRisk}
              onChange={(e: any) => setComposeRisk(e.target.value)}
              style={{ background: 'rgba(7, 11, 20, 0.8)', color: '#fff', border: '1px solid rgba(255,255,255,0.1)', borderRadius: '6px', padding: '4px 8px', fontSize: '11px' }}
            >
              <option value="impassable">Critical / Impassable (Red)</option>
              <option value="caution">Caution Advisory (Yellow)</option>
              <option value="safe">All Clear (Green)</option>
            </select>
            <button
              type="submit"
              style={{ background: '#ef4444', color: '#fff', padding: '6px 14px', borderRadius: '6px', fontSize: '12px', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '4px' }}
            >
              <Send size={12} /> Push Alert
            </button>
          </div>
        </form>
      )}

      {/* Alert Feed List */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '16px' }}>
        {alerts.length === 0 ? (
          <div style={{ textAlign: 'center', padding: '32px 16px', color: '#64748b', fontSize: '13px' }}>
            No active emergency alerts. All monitored corridors nominal.
          </div>
        ) : (
          alerts.map((alert) => {
            const isImpassable = alert.riskLevel === 'impassable';
            const isCaution = alert.riskLevel === 'caution';
            const color = isImpassable ? '#ef4444' : isCaution ? '#f59e0b' : '#10b981';

            return (
              <div
                key={alert.id}
                style={{
                  background: isImpassable ? 'rgba(239, 68, 68, 0.12)' : 'rgba(19, 31, 56, 0.8)',
                  border: `1px solid ${color}`,
                  borderRadius: '10px',
                  padding: '12px 14px',
                  marginBottom: '10px',
                  position: 'relative'
                }}
              >
                <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '8px' }}>
                  <div style={{ display: 'flex', alignItems: 'flex-start', gap: '8px' }}>
                    {isImpassable ? <AlertOctagon size={16} color="#ef4444" style={{ marginTop: '2px' }} /> : <AlertTriangle size={16} color="#f59e0b" style={{ marginTop: '2px' }} />}
                    <div>
                      <div style={{ fontSize: '13px', fontWeight: 800, color: '#f8fafc' }}>
                        {alert.title}
                      </div>
                      <div style={{ fontSize: '10px', color: '#94a3b8', marginTop: '1px' }}>
                        📍 {alert.locationName} • <span style={{ color: '#38bdf8' }}>{alert.timestamp}</span>
                      </div>
                    </div>
                  </div>

                  <button
                    onClick={() => onDismissAlert(alert.id)}
                    style={{ background: 'transparent', color: '#64748b', padding: '2px' }}
                    title="Dismiss"
                  >
                    <X size={14} />
                  </button>
                </div>

                <div style={{ fontSize: '11px', color: '#cbd5e1', marginTop: '8px', lineHeight: 1.4 }}>
                  {alert.message}
                </div>

                {alert.waterDepthCm > 0 && (
                  <div style={{ marginTop: '6px', fontSize: '11px', fontWeight: 700, color: color }}>
                    Current Recorded Depth: {alert.waterDepthCm} cm
                  </div>
                )}
              </div>
            );
          })
        )}
      </div>
    </div>
  );
};
