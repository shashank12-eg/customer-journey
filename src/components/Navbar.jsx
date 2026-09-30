import React from 'react';
import { 
  Activity, 
  Sparkles, 
  Bell, 
  RefreshCw, 
  ShieldAlert, 
  Layers, 
  PlayCircle,
  ExternalLink,
  ChevronDown,
  ShoppingBag,
  Store
} from 'lucide-react';

export default function Navbar({ onOpenSimulation, onResetData, pendingCount = 4 }) {
  return (
    <header className="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-xl border-b border-slate-800/80 px-4 lg:px-8 py-3 transition-all">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-4">
        
        {/* Brand & Store Selector */}
        <div className="flex items-center gap-3.5">
          <div className="relative">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-purple-600 flex items-center justify-center text-white shadow-lg shadow-indigo-500/25">
              <Activity className="w-5 h-5 animate-pulse" />
            </div>
            <span className="absolute -top-1 -right-1 flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500 border-2 border-slate-950"></span>
            </span>
          </div>

          <div>
            <div className="flex items-center gap-2.5">
              <h1 className="text-lg font-extrabold tracking-tight text-white flex items-center gap-1.5">
                PathPulse <span className="text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-purple-400 font-black">AI</span>
              </h1>
              <span className="text-[11px] font-semibold text-slate-400 bg-slate-900 border border-slate-800 px-2 py-0.5 rounded-md flex items-center gap-1">
                <Store className="w-3 h-3 text-indigo-400" />
                Global Storefront (US & EU)
              </span>
            </div>
            <p className="text-xs text-slate-400 flex items-center gap-1.5 mt-0.5">
              <span>Customer Journey Friction Detection & Real-Time Checkout Recovery</span>
            </p>
          </div>
        </div>

        {/* Live Telemetry Health & Action Controls */}
        <div className="flex items-center gap-3 flex-wrap">
          <div className="hidden lg:flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900/90 border border-slate-800 text-xs text-slate-300">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
            <span className="text-slate-400">Event Stream:</span>
            <span className="font-mono font-bold text-emerald-400">1,420 events/sec</span>
          </div>

          <button
            onClick={onOpenSimulation}
            className="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white text-xs font-semibold shadow-md shadow-indigo-600/25 hover:shadow-indigo-600/40 transition-all active:scale-95 cursor-pointer"
          >
            <PlayCircle className="w-4 h-4" />
            <span>Simulate Traffic Incident</span>
          </button>

          <button
            onClick={onResetData}
            title="Reset telemetry to baseline"
            className="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-400 hover:text-slate-200 transition-colors"
          >
            <RefreshCw className="w-4 h-4" />
          </button>

          <div className="relative">
            <button className="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-400 hover:text-slate-200 transition-colors relative">
              <Bell className="w-4 h-4" />
              {pendingCount > 0 && (
                <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-rose-500 text-white text-[10px] font-bold flex items-center justify-center">
                  {pendingCount}
                </span>
              )}
            </button>
          </div>
        </div>

      </div>
    </header>
  );
}
