import React, { useState, useEffect } from 'react';
import { HistoricalStormScenario, StormReplayFrame, StreetSegment } from '../../types';
import { HISTORICAL_SCENARIOS } from '../../data/mockData';
import { History, Play, Pause, SkipBack, SkipForward, CloudRain, BarChart3, CheckCircle, Droplets } from 'lucide-react';
import { ResponsiveContainer, AreaChart, Area, XAxis, YAxis, Tooltip } from 'recharts';

interface HistoricalReplayPanelProps {
  onApplyReplayFrame: (frame: StormReplayFrame) => void;
  streets: StreetSegment[];
}

export const HistoricalReplayPanel: React.FC<HistoricalReplayPanelProps> = ({
  onApplyReplayFrame,
  streets
}) => {
  const [selectedScenario, setSelectedScenario] = useState<HistoricalStormScenario>(HISTORICAL_SCENARIOS[0]);
  const [frameIndex, setFrameIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [playbackSpeed, setPlaybackSpeed] = useState<1 | 2 | 5>(1);

  const currentFrame = selectedScenario.frames[frameIndex] || selectedScenario.frames[0];

  // Auto-play replay frames
  useEffect(() => {
    let interval: any;
    if (isPlaying) {
      interval = setInterval(() => {
        setFrameIndex((prev) => {
          const next = (prev + 1) % selectedScenario.frames.length;
          onApplyReplayFrame(selectedScenario.frames[next]);
          return next;
        });
      }, 3500 / playbackSpeed);
    }
    return () => clearInterval(interval);
  }, [isPlaying, playbackSpeed, selectedScenario, onApplyReplayFrame]);

  const handleSelectScenario = (sc: HistoricalStormScenario) => {
    setSelectedScenario(sc);
    setFrameIndex(0);
    setIsPlaying(false);
    onApplyReplayFrame(sc.frames[0]);
  };

  const handleStep = (direction: 'prev' | 'next') => {
    let nextIdx = direction === 'next' ? frameIndex + 1 : frameIndex - 1;
    if (nextIdx >= selectedScenario.frames.length) nextIdx = 0;
    if (nextIdx < 0) nextIdx = selectedScenario.frames.length - 1;
    setFrameIndex(nextIdx);
    onApplyReplayFrame(selectedScenario.frames[nextIdx]);
  };

  // Chart data
  const chartData = selectedScenario.frames.map((f, idx) => ({
    time: f.displayTime.split(' ')[0],
    rainfall: f.rainfallIntensityMmHr,
    flooded: f.inundatedStreetsCount,
    maxDepth: f.maxDepthCm,
    isCurrent: idx === frameIndex
  }));

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
      border: '1px solid rgba(16, 185, 129, 0.3)',
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
            <History size={20} color="#10b981" />
            <span style={{ fontSize: '16px', fontWeight: 800, color: '#f8fafc' }}>
              Historical Storm Replay
            </span>
          </div>
          <span style={{ fontSize: '10px', background: 'rgba(16, 185, 129, 0.2)', color: '#10b981', padding: '2px 8px', borderRadius: '9999px', fontWeight: 700 }}>
            Model Calibration Mode
          </span>
        </div>
        <div style={{ fontSize: '12px', color: '#94a3b8' }}>
          Replay calibrated radar & SWMM dynamic-wave ground truth benchmarks
        </div>

        {/* Scenario Selector */}
        <div style={{ marginTop: '12px' }}>
          <select
            value={selectedScenario.id}
            onChange={(e) => {
              const sc = HISTORICAL_SCENARIOS.find(s => s.id === e.target.value);
              if (sc) handleSelectScenario(sc);
            }}
            style={{
              width: '100%',
              background: 'rgba(7, 11, 20, 0.8)',
              color: '#f8fafc',
              border: '1px solid rgba(255, 255, 255, 0.12)',
              borderRadius: '8px',
              padding: '8px 12px',
              fontSize: '12px',
              fontWeight: 600,
              outline: 'none'
            }}
          >
            {HISTORICAL_SCENARIOS.map(s => (
              <option key={s.id} value={s.id}>
                ⛈️ {s.cityName}: {s.eventTitle}
              </option>
            ))}
          </select>
        </div>

        {/* Playback Controls Bar */}
        <div style={{
          marginTop: '12px',
          background: 'rgba(7, 11, 20, 0.6)',
          padding: '10px 14px',
          borderRadius: '12px',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <button
              onClick={() => handleStep('prev')}
              style={{ background: 'rgba(255,255,255,0.05)', color: '#f8fafc', padding: '6px', borderRadius: '6px' }}
              title="Step Backward"
            >
              <SkipBack size={14} />
            </button>

            <button
              onClick={() => setIsPlaying(!isPlaying)}
              style={{
                background: isPlaying ? '#ef4444' : '#10b981',
                color: '#ffffff',
                width: '32px',
                height: '32px',
                borderRadius: '50%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                boxShadow: isPlaying ? '0 0 10px rgba(239,68,68,0.5)' : '0 0 10px rgba(16,185,129,0.5)'
              }}
            >
              {isPlaying ? <Pause size={14} /> : <Play size={14} style={{ marginLeft: '2px' }} />}
            </button>

            <button
              onClick={() => handleStep('next')}
              style={{ background: 'rgba(255,255,255,0.05)', color: '#f8fafc', padding: '6px', borderRadius: '6px' }}
              title="Step Forward"
            >
              <SkipForward size={14} />
            </button>
          </div>

          {/* Current Frame Timestamp */}
          <div style={{ fontSize: '11px', color: '#38bdf8', fontWeight: 700 }}>
            {currentFrame.displayTime}
          </div>

          {/* Speed Multiplier */}
          <div style={{ display: 'flex', gap: '4px' }}>
            {[1, 2, 5].map((spd) => (
              <button
                key={spd}
                onClick={() => setPlaybackSpeed(spd as any)}
                style={{
                  padding: '3px 6px',
                  borderRadius: '4px',
                  fontSize: '10px',
                  fontWeight: 700,
                  background: playbackSpeed === spd ? '#10b981' : 'rgba(255,255,255,0.05)',
                  color: playbackSpeed === spd ? '#fff' : '#64748b'
                }}
              >
                {spd}x
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Replay Details & Analytics */}
      <div style={{ flex: 1, overflowY: 'auto', padding: '16px' }}>
        {/* Frame Metrics Grid */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '8px', marginBottom: '14px' }}>
          <div style={{ background: 'rgba(19, 31, 56, 0.6)', padding: '8px 10px', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.05)' }}>
            <div style={{ fontSize: '9px', color: '#94a3b8' }}>RAINFALL INTENSITY</div>
            <div style={{ fontSize: '14px', fontWeight: 800, color: '#38bdf8' }}>
              {currentFrame.rainfallIntensityMmHr} mm/h
            </div>
          </div>

          <div style={{ background: 'rgba(19, 31, 56, 0.6)', padding: '8px 10px', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.05)' }}>
            <div style={{ fontSize: '9px', color: '#94a3b8' }}>RADAR REFLECTIVITY</div>
            <div style={{ fontSize: '14px', fontWeight: 800, color: '#f59e0b' }}>
              {currentFrame.radarReflectivityDbz} dBZ
            </div>
          </div>

          <div style={{ background: 'rgba(19, 31, 56, 0.6)', padding: '8px 10px', borderRadius: '8px', border: '1px solid rgba(255,255,255,0.05)' }}>
            <div style={{ fontSize: '9px', color: '#94a3b8' }}>MAX INUNDATION</div>
            <div style={{ fontSize: '14px', fontWeight: 800, color: '#ef4444' }}>
              {currentFrame.maxDepthCm} cm
            </div>
          </div>
        </div>

        {/* Hyetograph Chart */}
        <div style={{
          background: 'rgba(7, 11, 20, 0.7)',
          borderRadius: '10px',
          padding: '12px',
          border: '1px solid rgba(255, 255, 255, 0.05)',
          marginBottom: '14px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '8px' }}>
            <span style={{ fontSize: '11px', fontWeight: 700, color: '#94a3b8' }}>
              STORM HYETOGRAPH & FLOOD PEAK TIMELINE
            </span>
            <span style={{ fontSize: '10px', color: '#38bdf8' }}>Intensity vs Inundation</span>
          </div>

          <div style={{ height: '110px', width: '100%' }}>
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={chartData}>
                <defs>
                  <linearGradient id="rainGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#38bdf8" stopOpacity={0.8}/>
                    <stop offset="95%" stopColor="#38bdf8" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <XAxis dataKey="time" stroke="#64748b" fontSize={10} />
                <YAxis stroke="#64748b" fontSize={10} />
                <Tooltip
                  contentStyle={{ background: '#0d1527', borderColor: 'rgba(255,255,255,0.1)', borderRadius: '6px', fontSize: '11px' }}
                />
                <Area type="monotone" dataKey="rainfall" stroke="#38bdf8" fillOpacity={1} fill="url(#rainGrad)" name="Rainfall (mm/h)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Benchmark Calibration Scores */}
        <div style={{
          background: 'rgba(16, 185, 129, 0.1)',
          border: '1px solid rgba(16, 185, 129, 0.3)',
          borderRadius: '10px',
          padding: '12px'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '6px', marginBottom: '6px', color: '#10b981', fontWeight: 700, fontSize: '12px' }}>
            <CheckCircle size={14} /> GNN SURROGATE VALIDATION BENCHMARK
          </div>
          <div style={{ fontSize: '11px', color: '#94a3b8', lineHeight: 1.4, marginBottom: '8px' }}>
            Calibrated against full 2D EPA-SWMM dynamic-wave simulation on {selectedScenario.date}.
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '6px', textAlign: 'center' }}>
            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '6px', borderRadius: '6px' }}>
              <div style={{ fontSize: '9px', color: '#64748b' }}>PROB. DETECTION (POD)</div>
              <div style={{ fontSize: '13px', fontWeight: 800, color: '#10b981' }}>94.2%</div>
            </div>
            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '6px', borderRadius: '6px' }}>
              <div style={{ fontSize: '9px', color: '#64748b' }}>FALSE ALARM (FAR)</div>
              <div style={{ fontSize: '13px', fontWeight: 800, color: '#38bdf8' }}>6.8%</div>
            </div>
            <div style={{ background: 'rgba(0,0,0,0.3)', padding: '6px', borderRadius: '6px' }}>
              <div style={{ fontSize: '9px', color: '#64748b' }}>CRITICAL INDEX (CSI)</div>
              <div style={{ fontSize: '13px', fontWeight: 800, color: '#f59e0b' }}>0.88</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
