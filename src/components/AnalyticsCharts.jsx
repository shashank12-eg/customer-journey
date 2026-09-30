import React, { useState } from 'react';
import { 
  BarChart, Bar, LineChart, Line, AreaChart, Area, PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Legend 
} from 'recharts';
import { 
  FUNNEL_DATA, 
  ROOT_CAUSES_BREAKDOWN, 
  RECOVERY_CHANNEL_STATS, 
  HOURLY_FRICTION_TREND 
} from '../data/mockData';
import { 
  BarChart3, 
  PieChart as PieIcon, 
  TrendingUp, 
  Zap, 
  Layers, 
  Info 
} from 'lucide-react';

const CustomTooltip = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-slate-900 border border-slate-700/80 p-3 rounded-xl shadow-xl text-xs backdrop-blur-md">
        <p className="font-bold text-white mb-1.5">{label}</p>
        {payload.map((item, idx) => (
          <div key={idx} className="flex items-center justify-between gap-4 py-0.5">
            <span className="flex items-center gap-1.5 text-slate-300">
              <span className="w-2.5 h-2.5 rounded-full" style={{ backgroundColor: item.color || item.fill }} />
              {item.name}:
            </span>
            <span className="font-mono font-bold text-white">{item.value.toLocaleString()}</span>
          </div>
        ))}
      </div>
    );
  }
  return null;
};

export default function AnalyticsCharts() {
  const [activeTab, setActiveTab] = useState('funnel'); // 'funnel' | 'rootcauses' | 'recovery' | 'trend'

  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-2xl p-5 mb-6 backdrop-blur-sm shadow-xl">
      {/* Header & View Switcher */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-5 pb-4 border-b border-slate-800/80">
        <div>
          <div className="flex items-center gap-2">
            <BarChart3 className="w-5 h-5 text-indigo-400" />
            <h2 className="text-base font-bold text-white">E-Commerce Journey Friction Analytics</h2>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Telemetry combining clickstream events, cart abandonment drop-offs, and automated recovery yields
          </p>
        </div>

        {/* Tab Controls */}
        <div className="flex items-center p-1 bg-slate-950 rounded-xl border border-slate-800 self-start sm:self-auto overflow-x-auto max-w-full">
          <button
            onClick={() => setActiveTab('funnel')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all whitespace-nowrap cursor-pointer ${
              activeTab === 'funnel'
                ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/30'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Conversion Funnel Drop-offs
          </button>
          <button
            onClick={() => setActiveTab('rootcauses')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all whitespace-nowrap cursor-pointer ${
              activeTab === 'rootcauses'
                ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/30'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Friction Root Causes
          </button>
          <button
            onClick={() => setActiveTab('trend')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all whitespace-nowrap cursor-pointer ${
              activeTab === 'trend'
                ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/30'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Friction vs Recovery Stream
          </button>
          <button
            onClick={() => setActiveTab('recovery')}
            className={`px-3 py-1.5 rounded-lg text-xs font-semibold transition-all whitespace-nowrap cursor-pointer ${
              activeTab === 'recovery'
                ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/30'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Intervention Efficiency
          </button>
        </div>
      </div>

      {/* Chart Canvas */}
      <div className="w-full h-72">
        {activeTab === 'funnel' && (
          <div className="w-full h-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={FUNNEL_DATA} margin={{ top: 10, right: 30, left: 10, bottom: 20 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis 
                  dataKey="stage" 
                  stroke="#94a3b8" 
                  fontSize={11} 
                  tickLine={false} 
                  dy={8} 
                />
                <YAxis 
                  stroke="#94a3b8" 
                  fontSize={11} 
                  tickLine={false} 
                  tickFormatter={(val) => `${(val / 1000).toFixed(0)}k`} 
                />
                <Tooltip content={<CustomTooltip />} />
                <Legend 
                  verticalAlign="top" 
                  align="right" 
                  iconType="circle"
                  wrapperStyle={{ paddingBottom: 15, fontSize: 12 }} 
                />
                <Bar dataKey="sessions" name="Active Sessions" fill="#6366f1" radius={[6, 6, 0, 0]} />
                <Bar dataKey="dropoff" name="Drop-off Volume" fill="#f43f5e" radius={[6, 6, 0, 0]} />
                <Bar dataKey="frictionPoints" name="Friction Incidents Detected" fill="#eab308" radius={[6, 6, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}

        {activeTab === 'rootcauses' && (
          <div className="w-full h-full flex flex-col md:flex-row items-center justify-around gap-4">
            <div className="w-full md:w-1/2 h-full">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={ROOT_CAUSES_BREAKDOWN}
                    cx="50%"
                    cy="50%"
                    innerRadius={65}
                    outerRadius={95}
                    paddingAngle={4}
                    dataKey="count"
                  >
                    {ROOT_CAUSES_BREAKDOWN.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip 
                    formatter={(value, name, props) => [
                      `${value} incidents (${props.payload.percentage}%)`, 
                      props.payload.name
                    ]}
                    contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '0.75rem', fontSize: '12px' }}
                  />
                </PieChart>
              </ResponsiveContainer>
            </div>

            {/* Custom Legend & Context Table */}
            <div className="w-full md:w-1/2 flex flex-col justify-center gap-2">
              <div className="text-xs font-semibold uppercase tracking-wider text-slate-400 mb-1">
                Friction Categories Identified by AI
              </div>
              {ROOT_CAUSES_BREAKDOWN.map((item, idx) => (
                <div 
                  key={idx} 
                  className="flex items-center justify-between p-2 rounded-xl bg-slate-950/60 border border-slate-800 text-xs"
                >
                  <div className="flex items-center gap-2.5">
                    <span className="w-3 h-3 rounded-full shrink-0" style={{ backgroundColor: item.color }} />
                    <span className="font-medium text-slate-200">{item.name}</span>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className="text-slate-400 font-mono">{item.count} alerts</span>
                    <span className="font-bold text-white px-2 py-0.5 rounded bg-slate-800 border border-slate-700">
                      {item.percentage}%
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {activeTab === 'trend' && (
          <div className="w-full h-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={HOURLY_FRICTION_TREND} margin={{ top: 10, right: 30, left: 10, bottom: 20 }}>
                <defs>
                  <linearGradient id="frictionGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#ef4444" stopOpacity={0.4}/>
                    <stop offset="95%" stopColor="#ef4444" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="recoveredGrad" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#10b981" stopOpacity={0.4}/>
                    <stop offset="95%" stopColor="#10b981" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" vertical={false} />
                <XAxis dataKey="hour" stroke="#94a3b8" fontSize={11} tickLine={false} dy={8} />
                <YAxis stroke="#94a3b8" fontSize={11} tickLine={false} />
                <Tooltip content={<CustomTooltip />} />
                <Legend verticalAlign="top" align="right" wrapperStyle={{ paddingBottom: 15, fontSize: 12 }} />
                <Area type="monotone" dataKey="friction" name="Friction Alerts Triggered" stroke="#ef4444" fillOpacity={1} fill="url(#frictionGrad)" strokeWidth={2} />
                <Area type="monotone" dataKey="recovered" name="Autonomous Recoveries" stroke="#10b981" fillOpacity={1} fill="url(#recoveredGrad)" strokeWidth={2} />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        )}

        {activeTab === 'recovery' && (
          <div className="w-full h-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={RECOVERY_CHANNEL_STATS} layout="vertical" margin={{ top: 10, right: 30, left: 40, bottom: 10 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" horizontal={false} />
                <XAxis type="number" stroke="#94a3b8" fontSize={11} domain={[0, 100]} unit="%" tickLine={false} />
                <YAxis type="category" dataKey="channel" stroke="#94a3b8" fontSize={11} tickLine={false} width={180} />
                <Tooltip 
                  formatter={(value, name) => [`${value}% Success Rate`, 'Recovery Efficacy']}
                  contentStyle={{ backgroundColor: '#0f172a', borderColor: '#334155', borderRadius: '0.75rem', fontSize: '12px' }}
                />
                <Bar dataKey="rate" name="Recovery Success Rate (%)" fill="#10b981" radius={[0, 6, 6, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </div>
        )}
      </div>

      {/* Footer Info Callout */}
      <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs text-slate-400">
        <div className="flex items-center gap-1.5">
          <Info className="w-4 h-4 text-indigo-400 shrink-0" />
          <span>Friction points flagged via clickstream anomaly detection, latency thresholds, and rage-click telemetry.</span>
        </div>
        <span className="hidden sm:inline font-mono text-[11px] text-slate-500">Live Window: Last 24 Hours</span>
      </div>
    </div>
  );
}
