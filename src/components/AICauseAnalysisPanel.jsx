import React from 'react';
import { 
  BrainCircuit, 
  CheckCircle, 
  AlertTriangle, 
  Lightbulb, 
  Rocket, 
  Send, 
  ShieldCheck, 
  Activity, 
  ArrowRight, 
  Zap, 
  Layers, 
  Cpu 
} from 'lucide-react';

export default function AICauseAnalysisPanel({ customer, onTriggerAction }) {
  if (!customer || !customer.aiAnalysis) {
    return null;
  }

  const { aiAnalysis } = customer;

  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-2xl p-5 mb-6 backdrop-blur-sm shadow-xl">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-5 pb-4 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-2">
            <div className="p-1.5 rounded-lg bg-indigo-500/10 border border-indigo-500/30 text-indigo-400">
              <BrainCircuit className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h3 className="text-base font-bold text-white">
                  Root Cause Diagnosis & Reasoning
                </h3>
                <span className="text-[10px] font-bold uppercase tracking-wider bg-indigo-500/15 text-indigo-300 border border-indigo-500/30 px-2 py-0.5 rounded-full">
                  Diagnostic Model v3.2
                </span>
              </div>
              <p className="text-xs text-slate-400 mt-0.5">
                Multi-signal inference correlating clickstream telemetry, error logs, and customer intent
              </p>
            </div>
          </div>
        </div>

        {/* Confidence Badge */}
        <div className="flex items-center gap-2.5 bg-slate-950 px-3.5 py-2 rounded-xl border border-slate-800 self-start sm:self-auto">
          <Cpu className="w-4 h-4 text-indigo-400" />
          <div className="flex flex-col">
            <span className="text-[10px] uppercase font-bold text-slate-400">Confidence Score</span>
            <div className="flex items-center gap-1.5">
              <span className="text-sm font-mono font-extrabold text-white">
                {aiAnalysis.confidence}%
              </span>
              <span className="text-[10px] text-emerald-400 font-semibold">High Certainty</span>
            </div>
          </div>
        </div>
      </div>

      {/* Main Analysis Card */}
      <div className="p-4 rounded-xl bg-gradient-to-br from-indigo-950/40 via-slate-950 to-purple-950/40 border border-indigo-500/30 mb-5 shadow-lg">
        <div className="flex items-start justify-between gap-3 mb-2">
          <div>
            <span className="text-[10px] font-bold uppercase tracking-wider text-indigo-400">
              Detected Primary Friction Cause
            </span>
            <h4 className="text-base font-extrabold text-white mt-0.5">
              {aiAnalysis.primaryCause}
            </h4>
          </div>
          <span className="px-2.5 py-1 rounded-lg bg-indigo-500/15 border border-indigo-500/30 text-xs font-semibold text-indigo-300">
            {aiAnalysis.category}
          </span>
        </div>

        <p className="text-xs text-slate-300 leading-relaxed mt-2 bg-slate-900/60 p-3 rounded-lg border border-slate-800/80">
          {aiAnalysis.rootCauseSummary}
        </p>

        {/* Evidence & Behavioral Signals */}
        <div className="mt-4">
          <div className="text-[11px] font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
            <Activity className="w-3.5 h-3.5 text-indigo-400" />
            Empirical Telemetry & Behavioral Evidence
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            {aiAnalysis.evidenceSignals.map((signal, idx) => (
              <div 
                key={idx} 
                className="p-2.5 rounded-lg bg-slate-950/70 border border-slate-800 flex items-start gap-2 text-xs"
              >
                <div className={`w-2 h-2 rounded-full mt-1.5 shrink-0 ${
                  signal.severity === 'high' ? 'bg-rose-400 ring-2 ring-rose-500/30' :
                  signal.severity === 'medium' ? 'bg-amber-400' : 'bg-blue-400'
                }`} />
                <div>
                  <span className="text-slate-400 font-semibold">{signal.label}:</span>
                  <div className="text-slate-200 font-medium mt-0.5 font-mono text-[11px]">
                    {signal.value}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Recommended Recovery Playbooks */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-center gap-2">
            <Lightbulb className="w-4 h-4 text-amber-400" />
            <h4 className="text-sm font-bold text-white">
              Recommended Recovery Playbooks
            </h4>
          </div>
          <span className="text-xs text-slate-400">
            Select a playbook to trigger automated customer recovery
          </span>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-3.5">
          {aiAnalysis.recommendations.map((rec) => (
            <div
              key={rec.id}
              className="p-4 rounded-xl bg-slate-950 border border-slate-800 hover:border-indigo-500/60 transition-all flex flex-col justify-between group"
            >
              <div>
                <div className="flex items-center justify-between gap-2 mb-2">
                  <span className="text-xs font-bold text-white group-hover:text-indigo-300 transition-colors">
                    {rec.type}
                  </span>
                  <span className="text-xs font-mono font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
                    {rec.expectedRecoveryRate} Est. Yield
                  </span>
                </div>

                <p className="text-xs text-slate-400 leading-relaxed mb-3">
                  {rec.description}
                </p>

                <div className="flex items-center gap-2 text-[11px] text-slate-500 mb-4">
                  <span>Channel: <strong className="text-slate-300">{rec.channel}</strong></span>
                  {rec.suggestedDiscount && (
                    <>
                      <span>•</span>
                      <span>Offer: <strong className="text-amber-300">{rec.suggestedDiscount}</strong></span>
                    </>
                  )}
                </div>
              </div>

              <button
                onClick={() => onTriggerAction(customer, rec)}
                disabled={customer.status === 'Recovered'}
                className={`w-full py-2 px-3 rounded-xl text-xs font-bold flex items-center justify-center gap-2 transition-all cursor-pointer ${
                  customer.status === 'Recovered'
                    ? 'bg-emerald-950/40 text-emerald-400 border border-emerald-800/40 cursor-not-allowed'
                    : 'bg-gradient-to-r from-indigo-600 to-purple-600 hover:from-indigo-500 hover:to-purple-500 text-white shadow-md shadow-indigo-600/30 hover:shadow-indigo-600/50 active:scale-98'
                }`}
              >
                {customer.status === 'Recovered' ? (
                  <>
                    <CheckCircle className="w-4 h-4 text-emerald-400" />
                    <span>Customer Successfully Recovered</span>
                  </>
                ) : (
                  <>
                    <Rocket className="w-4 h-4" />
                    <span>{rec.actionLabel}</span>
                  </>
                )}
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
