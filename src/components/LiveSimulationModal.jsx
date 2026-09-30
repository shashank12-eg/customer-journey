import React, { useState } from 'react';
import { 
  X, 
  Play, 
  Sparkles, 
  AlertTriangle, 
  CreditCard, 
  Truck, 
  HelpCircle, 
  Tag, 
  ChevronRight,
  ShieldCheck 
} from 'lucide-react';

export default function LiveSimulationModal({ isOpen, onClose, onInjectScenario }) {
  if (!isOpen) return null;

  const scenarios = [
    {
      id: "sim-1",
      title: "Incident A: 3DS Bank OTP Gateway Challenge Timeout",
      customerName: "Lucas Vance",
      email: "lucas.v@gmail.com",
      cartValue: 420.00,
      frictionType: "Payment Gateway Failure",
      riskLevel: "Critical",
      riskScore: 98,
      icon: CreditCard,
      color: "text-rose-400 bg-rose-500/10 border-rose-500/30",
      description: "Customer attempts checkout for 4K Drone ($420). Bank iframe fails to load OTP challenge. 6 rage clicks recorded."
    },
    {
      id: "sim-2",
      title: "Incident B: Unexpected Express Shipping Surcharge Shock",
      customerName: "Maya Lin",
      email: "maya.l@design.co",
      cartValue: 185.00,
      frictionType: "Delivery Uncertainty & Shipping Shock",
      riskLevel: "High",
      riskScore: 86,
      icon: Truck,
      color: "text-amber-400 bg-amber-500/10 border-amber-500/30",
      description: "Customer added 3 fashion items, but cart shows $28.00 unexpected courier surcharge with no delivery date guarantee."
    },
    {
      id: "sim-3",
      title: "Incident C: Promo Code Validation Rule Bug at $190",
      customerName: "Jordan Smith",
      email: "jordan.s@apple.com",
      cartValue: 190.00,
      frictionType: "Promo Code Failure & Rage Clicks",
      riskLevel: "High",
      riskScore: 84,
      icon: Tag,
      color: "text-purple-400 bg-purple-500/10 border-purple-500/30",
      description: "First-time visitor tried entering promo code from homepage banner. System threw 'Invalid campaign code' bug."
    },
    {
      id: "sim-4",
      title: "Incident D: Product Specification Vacuum & Return Fear",
      customerName: "Aiden Scott",
      email: "aiden.scott@home.net",
      cartValue: 650.00,
      frictionType: "Comparison Fatigue & Unclear Specs",
      riskLevel: "Medium",
      riskScore: 72,
      icon: HelpCircle,
      color: "text-blue-400 bg-blue-500/10 border-blue-500/30",
      description: "Customer toggled between 2 sectional couches 18 times; furniture dimension drawing image is broken on mobile."
    }
  ];

  const handleSelect = (scenario) => {
    onInjectScenario(scenario);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="relative w-full max-w-2xl bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="flex items-center justify-between p-5 border-b border-slate-800 bg-slate-950/80">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-indigo-600 to-purple-600 flex items-center justify-center text-white shadow-md">
              <Play className="w-4 h-4 fill-current" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">Live Friction Incident Simulator</h3>
              <p className="text-xs text-slate-400">Inject real-time e-commerce edge cases to evaluate autonomous detection</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* List of Scenarios */}
        <div className="p-6 space-y-3.5 max-h-[70vh] overflow-y-auto">
          {scenarios.map((sc) => {
            const Icon = sc.icon;
            return (
              <div
                key={sc.id}
                onClick={() => handleSelect(sc)}
                className="p-4 rounded-2xl bg-slate-950 border border-slate-800 hover:border-indigo-500 hover:bg-slate-850/80 transition-all cursor-pointer group flex flex-col sm:flex-row sm:items-center justify-between gap-4"
              >
                <div className="flex items-start gap-3.5">
                  <div className={`p-2.5 rounded-xl border shrink-0 ${sc.color}`}>
                    <Icon className="w-5 h-5" />
                  </div>
                  <div>
                    <div className="flex items-center gap-2">
                      <h4 className="text-sm font-bold text-white group-hover:text-indigo-300 transition-colors">
                        {sc.title}
                      </h4>
                      <span className="text-[10px] font-mono font-bold px-1.5 py-0.5 rounded bg-slate-800 text-slate-300">
                        ${sc.cartValue.toFixed(2)}
                      </span>
                    </div>
                    <p className="text-xs text-slate-400 mt-1 leading-relaxed">
                      {sc.description}
                    </p>
                    <div className="flex items-center gap-2 mt-2 text-[11px] text-slate-500">
                      <span>Customer: <strong className="text-slate-300">{sc.customerName}</strong></span>
                      <span>•</span>
                      <span>Risk: <strong className="text-rose-400">{sc.riskLevel} ({sc.riskScore})</strong></span>
                    </div>
                  </div>
                </div>

                <button
                  type="button"
                  className="px-3.5 py-2 rounded-xl bg-slate-900 group-hover:bg-indigo-600 text-slate-300 group-hover:text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition-all shrink-0 border border-slate-800 group-hover:border-indigo-500"
                >
                  <span>Inject Incident</span>
                  <ChevronRight className="w-3.5 h-3.5" />
                </button>
              </div>
            );
          })}
        </div>

        {/* Footer */}
        <div className="p-4 bg-slate-950/80 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
          <span className="flex items-center gap-1.5">
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            PathPulse Real-Time Telemetry & Anomaly Ingestion Engine
          </span>
          <button
            onClick={onClose}
            className="px-3 py-1.5 rounded-lg text-slate-400 hover:text-white"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
}
