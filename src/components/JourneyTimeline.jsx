import React, { useState } from 'react';
import { 
  GitCommit, 
  Clock, 
  Globe, 
  AlertOctagon, 
  Smile, 
  Meh, 
  Frown, 
  Flame, 
  HelpCircle,
  CheckCircle2, 
  Zap, 
  MousePointer, 
  CreditCard, 
  ShoppingCart, 
  Search, 
  Package, 
  Eye, 
  Terminal 
} from 'lucide-react';

export default function JourneyTimeline({ customer }) {
  const [activeStepId, setActiveStepId] = useState(null);

  if (!customer) {
    return (
      <div className="bg-slate-900/70 border border-slate-800 rounded-2xl p-8 text-center text-slate-400">
        Select a customer to inspect their journey touchpoint timeline.
      </div>
    );
  }

  const getStepIcon = (type, isFriction) => {
    if (isFriction) return AlertOctagon;
    switch (type) {
      case 'navigation': return Globe;
      case 'search': return Search;
      case 'interaction': return Eye;
      case 'action': return ShoppingCart;
      case 'form': return MousePointer;
      case 'transaction': return CreditCard;
      case 'error': return Flame;
      case 'dropoff': return AlertOctagon;
      default: return GitCommit;
    }
  };

  const getSentimentBadge = (sentiment) => {
    switch (sentiment) {
      case 'positive':
        return (
          <span className="flex items-center gap-1 text-[11px] font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-md border border-emerald-500/20">
            <Smile className="w-3 h-3" />
            Engaged
          </span>
        );
      case 'neutral':
        return (
          <span className="flex items-center gap-1 text-[11px] font-semibold text-slate-300 bg-slate-800 px-2 py-0.5 rounded-md border border-slate-700">
            <Meh className="w-3 h-3" />
            Browsing
          </span>
        );
      case 'confused':
        return (
          <span className="flex items-center gap-1 text-[11px] font-semibold text-amber-400 bg-amber-500/10 px-2 py-0.5 rounded-md border border-amber-500/20">
            <HelpCircle className="w-3 h-3" />
            Hesitant
          </span>
        );
      case 'frustrated':
      case 'critical':
        return (
          <span className="flex items-center gap-1 text-[11px] font-semibold text-rose-400 bg-rose-500/15 px-2 py-0.5 rounded-md border border-rose-500/30 animate-pulse">
            <Frown className="w-3 h-3" />
            Friction Spike
          </span>
        );
      default:
        return null;
    }
  };

  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-2xl p-5 mb-6 backdrop-blur-sm shadow-xl">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 mb-6 pb-4 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-2">
            <GitCommit className="w-5 h-5 text-indigo-400" />
            <h3 className="text-base font-bold text-white">
              Session Journey Timeline: {customer.name}
            </h3>
            <span className="text-xs font-mono text-slate-400 bg-slate-950 px-2 py-0.5 rounded border border-slate-800">
              {customer.id}
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-1">
            Chronological session touchpoints reconstructed from clickstream events, page dwell telemetry, and DOM interactions
          </p>
        </div>

        <div className="flex items-center gap-2">
          <div className="text-xs text-slate-400 flex items-center gap-2 bg-slate-950 px-3 py-1.5 rounded-xl border border-slate-800">
            <span>Total Steps: <strong className="text-white">{customer.journeySteps.length}</strong></span>
            <span>•</span>
            <span>Cart: <strong className="text-emerald-400">${customer.cartValue.toFixed(2)}</strong></span>
          </div>
        </div>
      </div>

      {/* Visual Step Timeline */}
      <div className="relative pl-6 md:pl-8 space-y-6 before:absolute before:left-3 md:before:left-4 before:top-3 before:bottom-3 before:w-0.5 before:bg-gradient-to-b before:from-indigo-500 before:via-purple-500/50 before:to-rose-500">
        {customer.journeySteps.map((step, idx) => {
          const StepIcon = getStepIcon(step.type, step.friction);
          const isSelected = activeStepId === step.id;

          return (
            <div 
              key={step.id} 
              className="relative group transition-all"
              onClick={() => setActiveStepId(isSelected ? null : step.id)}
            >
              {/* Timeline Node Badge */}
              <div 
                className={`absolute -left-6 md:-left-8 top-1.5 w-6 h-6 md:w-8 md:h-8 rounded-xl flex items-center justify-center border transition-all ${
                  step.friction
                    ? 'bg-rose-500/20 border-rose-500 text-rose-400 shadow-md shadow-rose-500/30 ring-2 ring-rose-500/50'
                    : 'bg-slate-900 border-indigo-500/50 text-indigo-400 group-hover:border-indigo-400'
                }`}
              >
                <StepIcon className="w-3.5 h-3.5 md:w-4 md:h-4" />
              </div>

              {/* Step Card Content */}
              <div
                className={`p-4 rounded-xl border transition-all cursor-pointer ${
                  step.friction
                    ? 'bg-rose-950/20 border-rose-900/60 hover:border-rose-700/80 shadow-lg shadow-rose-950/20'
                    : isSelected
                    ? 'bg-indigo-950/30 border-indigo-700 shadow-md shadow-indigo-950/30'
                    : 'bg-slate-950/60 border-slate-800 hover:border-slate-700 hover:bg-slate-900/60'
                }`}
              >
                {/* Step Top Bar */}
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-2">
                  <div className="flex items-center gap-2">
                    <span className="text-[11px] font-mono px-2 py-0.5 rounded bg-slate-900 text-slate-400 border border-slate-800 font-bold">
                      Step {step.stepNumber}
                    </span>
                    <h4 className="text-sm font-bold text-white flex items-center gap-2">
                      {step.title}
                    </h4>
                  </div>

                  <div className="flex items-center gap-2">
                    {getSentimentBadge(step.sentiment)}
                    <span className="flex items-center gap-1 text-[11px] text-slate-400 bg-slate-900/80 px-2 py-0.5 rounded border border-slate-800">
                      <Clock className="w-3 h-3 text-slate-500" />
                      {step.dwellTime}
                    </span>
                    <span className="text-[11px] text-slate-500 font-mono">
                      {step.timestamp}
                    </span>
                  </div>
                </div>

                {/* Page URL & Details */}
                <div className="flex items-center gap-2 text-xs text-indigo-300 font-mono mb-2">
                  <span className="px-2 py-0.5 rounded bg-indigo-950/50 border border-indigo-800/40 text-[10px] text-indigo-300">
                    URL
                  </span>
                  <span className="truncate">{step.page}</span>
                </div>

                <p className="text-xs text-slate-300 leading-relaxed">
                  {step.details}
                </p>

                {/* Friction Callout Box if friction flagged */}
                {step.friction && (
                  <div className="mt-3 p-3 rounded-lg bg-rose-500/10 border border-rose-500/30 flex items-start gap-2.5">
                    <AlertOctagon className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
                    <div>
                      <span className="text-xs font-bold text-rose-300">
                        Journey Friction Trigger:
                      </span>
                      <p className="text-xs text-rose-200 mt-0.5">
                        {step.frictionAlert}
                      </p>
                    </div>
                  </div>
                )}

                {/* Technical Telemetry Drawer (Click to toggle) */}
                {isSelected && (
                  <div className="mt-3 pt-3 border-t border-slate-800 text-[11px] font-mono text-slate-400">
                    <div className="flex items-center gap-1 text-slate-300 font-bold mb-1.5">
                      <Terminal className="w-3.5 h-3.5 text-indigo-400" />
                      Raw Event Telemetry Payload
                    </div>
                    <div className="bg-slate-950 p-2.5 rounded-lg border border-slate-800 text-slate-300 overflow-x-auto">
                      <pre className="text-[10px]">
{JSON.stringify({
  session_id: customer.id,
  step_idx: step.stepNumber,
  page_route: step.page,
  dwell_time_ms: parseInt(step.dwellTime) * 1000 || 45000,
  event_category: step.type,
  device_type: customer.device,
  friction_flag: step.friction,
  friction_metadata: step.frictionAlert || null,
  user_agent_platform: customer.location
}, null, 2)}
                      </pre>
                    </div>
                  </div>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
