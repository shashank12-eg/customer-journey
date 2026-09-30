import React from 'react';
import { Database, AlertOctagon, BrainCircuit, Lightbulb, Rocket, ChevronRight } from 'lucide-react';

export default function CoreFlowIndicator({ currentStage = 3 }) {
  const steps = [
    { id: 1, label: "Customer Telemetry", icon: Database, desc: "Clickstream & Events" },
    { id: 2, label: "Friction Detection", icon: AlertOctagon, desc: "Rage Clicks & Latency" },
    { id: 3, label: "Root Cause Diagnosis", icon: BrainCircuit, desc: "AI Behavioral Inference" },
    { id: 4, label: "Recovery Strategy", icon: Lightbulb, desc: "Dynamic Retention Offer" },
    { id: 5, label: "Automated Dispatch", icon: Rocket, desc: "Real-Time Execution" },
  ];

  return (
    <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4 backdrop-blur-md shadow-xl mb-6">
      <div className="flex items-center justify-between mb-3 px-2">
        <div className="flex items-center gap-2">
          <span className="flex h-2.5 w-2.5 rounded-full bg-emerald-400 animate-ping" />
          <h3 className="text-xs uppercase tracking-wider font-bold text-slate-400">
            Real-Time Friction Detection & Recovery Loop
          </h3>
        </div>
        <span className="text-xs font-semibold text-emerald-400 bg-emerald-950/60 px-2.5 py-0.5 rounded-full border border-emerald-800/60 flex items-center gap-1.5">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
          Autonomous Stream Active
        </span>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-5 gap-2 relative">
        {steps.map((step, idx) => {
          const Icon = step.icon;
          const isActive = currentStage >= step.id;
          const isCurrent = currentStage === step.id;

          return (
            <div key={step.id} className="relative flex items-center">
              <div
                className={`w-full p-3 rounded-xl border transition-all duration-300 flex items-center gap-3 ${
                  isCurrent
                    ? 'bg-gradient-to-r from-indigo-900/60 to-purple-900/60 border-indigo-500 shadow-lg shadow-indigo-500/20 ring-1 ring-indigo-400'
                    : isActive
                    ? 'bg-slate-800/80 border-slate-700/80 text-slate-200'
                    : 'bg-slate-900/40 border-slate-800/50 text-slate-500'
                }`}
              >
                <div
                  className={`w-9 h-9 rounded-lg flex items-center justify-center shrink-0 ${
                    isCurrent
                      ? 'bg-indigo-500 text-white shadow-md shadow-indigo-500/50'
                      : isActive
                      ? 'bg-slate-700 text-indigo-400'
                      : 'bg-slate-800 text-slate-600'
                  }`}
                >
                  <Icon className="w-5 h-5" />
                </div>
                <div className="min-w-0">
                  <div className="flex items-center gap-1.5">
                    <span className="text-[10px] font-mono px-1.5 py-0.2 rounded bg-slate-950 text-slate-400 font-semibold">
                      0{step.id}
                    </span>
                    <span className={`text-xs font-bold truncate ${isCurrent ? 'text-white' : 'text-slate-200'}`}>
                      {step.label}
                    </span>
                  </div>
                  <p className="text-[11px] text-slate-400 truncate mt-0.5">{step.desc}</p>
                </div>
              </div>

              {idx < steps.length - 1 && (
                <div className="hidden md:flex absolute -right-2.5 z-10 text-slate-600">
                  <ChevronRight className="w-5 h-5" />
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
