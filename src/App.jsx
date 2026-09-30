import React, { useState } from 'react';
import Navbar from './components/Navbar';
import CoreFlowIndicator from './components/CoreFlowIndicator';
import KPIHeader from './components/KPIHeader';
import AnalyticsCharts from './components/AnalyticsCharts';
import CustomerList from './components/CustomerList';
import JourneyTimeline from './components/JourneyTimeline';
import AICauseAnalysisPanel from './components/AICauseAnalysisPanel';
import BusinessActionModal from './components/BusinessActionModal';
import LiveSimulationModal from './components/LiveSimulationModal';
import { INITIAL_CUSTOMERS, KPI_DATA } from './data/mockData';
import { 
  Sparkles, 
  ShoppingBag, 
  ArrowRight, 
  CheckCircle, 
  AlertCircle, 
  Zap,
  Info
} from 'lucide-react';

export default function App() {
  const [customers, setCustomers] = useState(INITIAL_CUSTOMERS);
  const [selectedCustomerId, setSelectedCustomerId] = useState(INITIAL_CUSTOMERS[0].id);
  const [isActionModalOpen, setIsActionModalOpen] = useState(false);
  const [selectedAction, setSelectedAction] = useState(null);
  const [isSimulationModalOpen, setIsSimulationModalOpen] = useState(false);
  const [currentPipelineStage, setCurrentPipelineStage] = useState(4);
  const [toastMessage, setToastMessage] = useState(null);

  // Dynamic KPI calculations
  const [kpiStats, setKpiStats] = useState(KPI_DATA);

  const selectedCustomer = customers.find(c => c.id === selectedCustomerId) || customers[0];

  const showToast = (title, subtitle, type = 'info') => {
    setToastMessage({ title, subtitle, type });
    setTimeout(() => {
      setToastMessage(null);
    }, 4500);
  };

  const handleSelectCustomer = (customer) => {
    setSelectedCustomerId(customer.id);
    setCurrentPipelineStage(customer.status === 'Recovered' ? 5 : 4);
  };

  const handleTriggerAction = (customer, action) => {
    setSelectedCustomerId(customer.id);
    setSelectedAction(action);
    setIsActionModalOpen(true);
    setCurrentPipelineStage(5);
  };

  const handleConfirmRecovery = (customerId) => {
    setCustomers(prev =>
      prev.map(c => {
        if (c.id === customerId) {
          return {
            ...c,
            status: 'Recovered',
            riskLevel: 'Low',
            riskScore: 12
          };
        }
        return c;
      })
    );

    // Update KPIs dynamically
    const customer = customers.find(c => c.id === customerId);
    if (customer) {
      setKpiStats(prev => {
        const recoveredNum = parseFloat(prev.recoveredRevenue.replace(/[^0-9.-]+/g, '')) + customer.cartValue;
        const atRiskNum = Math.max(0, parseFloat(prev.revenueAtRisk.replace(/[^0-9.-]+/g, '')) - customer.cartValue);
        return {
          ...prev,
          revenueAtRisk: `$${atRiskNum.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}`,
          recoveredRevenue: `$${recoveredNum.toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 0 })}`,
          recoveryRate: "73.8%"
        };
      });

      showToast(
        "Friction Successfully Resolved!",
        `Customer ${customer.name} received recovery action. Secured $${customer.cartValue.toFixed(2)} in revenue.`,
        'success'
      );
    }
  };

  const handleInjectScenario = (scenario) => {
    const newCustomer = {
      id: `CUST-${Math.floor(1000 + Math.random() * 9000)}`,
      name: scenario.customerName,
      email: scenario.email,
      avatar: "https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?w=120&auto=format&fit=crop&q=80",
      segment: "Live Real-Time Session",
      cartValue: scenario.cartValue,
      device: "Mobile Safari (iOS 17)",
      location: "San Francisco, CA",
      journeyStage: "Checkout",
      riskLevel: scenario.riskLevel,
      riskScore: scenario.riskScore,
      frictionType: scenario.frictionType,
      status: "Pending Action",
      timeElapsed: "Just now",
      itemsInCart: [
        { name: "Simulated Retail Order", price: scenario.cartValue, qty: 1, img: "📦" }
      ],
      journeySteps: [
        {
          id: "step-1",
          stepNumber: 1,
          title: "Session Initiation",
          page: "/store",
          dwellTime: "30s",
          timestamp: "Just now",
          type: "navigation",
          sentiment: "neutral",
          details: "Entered store via live simulation hook.",
          friction: false
        },
        {
          id: "step-2",
          stepNumber: 2,
          title: "Cart & Checkout Trigger",
          page: "/checkout",
          dwellTime: "1m 15s",
          timestamp: "Just now",
          type: "form",
          sentiment: "frustrated",
          details: scenario.description,
          friction: true,
          frictionAlert: scenario.description
        }
      ],
      aiAnalysis: {
        primaryCause: scenario.frictionType,
        category: scenario.frictionType,
        confidence: 95,
        rootCauseSummary: scenario.description,
        evidenceSignals: [
          { label: "Real-time Telemetry Alert", value: "Anomaly threshold exceeded (Live Trigger)", severity: "high" },
          { label: "Simulated Cart Value", value: `$${scenario.cartValue.toFixed(2)}`, severity: "info" }
        ],
        recommendations: [
          {
            id: "rec-sim-1",
            type: "Priority Autonomous Fallback Intervention",
            description: "Dispatch instant automated coupon or 1-click fallback protocol to recover checkout before abandonment.",
            expectedRecoveryRate: "89%",
            actionLabel: "Dispatch Immediate Recovery Protocol",
            suggestedDiscount: "10% Courtesy Incentive",
            channel: "SMS / In-App"
          }
        ]
      }
    };

    setCustomers(prev => [newCustomer, ...prev]);
    setSelectedCustomerId(newCustomer.id);
    setCurrentPipelineStage(3);

    showToast(
      "Live Incident Ingested!",
      `New friction detected for ${scenario.customerName}: ${scenario.frictionType}`,
      'alert'
    );
  };

  const handleResetData = () => {
    setCustomers(INITIAL_CUSTOMERS);
    setSelectedCustomerId(INITIAL_CUSTOMERS[0].id);
    setKpiStats(KPI_DATA);
    setCurrentPipelineStage(4);
    showToast("Telemetry Baseline Restored", "Reset all live session filters and real-time streams to default baseline.", "info");
  };

  const pendingCount = customers.filter(c => c.status === 'Pending Action').length;

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-['Plus_Jakarta_Sans',sans-serif]">
      {/* Top Navbar */}
      <Navbar 
        onOpenSimulation={() => setIsSimulationModalOpen(true)}
        onResetData={handleResetData}
        pendingCount={pendingCount}
      />

      {/* Main Body */}
      <main className="flex-1 max-w-7xl w-full mx-auto px-4 lg:px-8 py-6">
        
        {/* Core Flow Pipeline Banner (Step 1 -> 5) */}
        <CoreFlowIndicator currentStage={currentPipelineStage} />

        {/* Executive Business KPIs */}
        <KPIHeader dynamicStats={kpiStats} />

        {/* Analytics & Charts View */}
        <AnalyticsCharts />

        {/* Customer List (Searchable & Filterable) */}
        <CustomerList 
          customers={customers}
          selectedCustomer={selectedCustomer}
          onSelectCustomer={handleSelectCustomer}
          onTriggerAction={handleTriggerAction}
        />

        {/* Detailed Deep-Dive Workspace (Selected Customer) */}
        {selectedCustomer && (
          <div className="space-y-6">
            
            {/* Customer Snapshot Card */}
            <div className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 flex flex-col lg:flex-row lg:items-center justify-between gap-4 shadow-xl">
              <div className="flex items-center gap-4">
                <img
                  src={selectedCustomer.avatar}
                  alt={selectedCustomer.name}
                  className="w-14 h-14 rounded-2xl object-cover ring-2 ring-indigo-500/50 shadow-md"
                />
                <div>
                  <div className="flex items-center gap-2 flex-wrap">
                    <h3 className="text-lg font-extrabold text-white">
                      {selectedCustomer.name}
                    </h3>
                    <span className="font-mono text-xs px-2 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700">
                      {selectedCustomer.id}
                    </span>
                    <span className="text-xs px-2.5 py-0.5 rounded-full font-bold bg-indigo-500/15 text-indigo-300 border border-indigo-500/30">
                      {selectedCustomer.segment}
                    </span>
                  </div>
                  <div className="flex items-center gap-3 text-xs text-slate-400 mt-1 flex-wrap">
                    <span>{selectedCustomer.email}</span>
                    <span>•</span>
                    <span>{selectedCustomer.device}</span>
                    <span>•</span>
                    <span>{selectedCustomer.location}</span>
                  </div>
                </div>
              </div>

              {/* Cart Preview */}
              <div className="flex items-center gap-3 bg-slate-950 p-3 rounded-xl border border-slate-800">
                <div className="flex -space-x-2 overflow-hidden text-lg">
                  {selectedCustomer.itemsInCart.map((item, idx) => (
                    <div 
                      key={idx} 
                      title={item.name}
                      className="w-9 h-9 rounded-lg bg-slate-800 border border-slate-700 flex items-center justify-center shadow"
                    >
                      {item.img}
                    </div>
                  ))}
                </div>
                <div>
                  <div className="text-[10px] uppercase font-bold text-slate-500">Cart Total</div>
                  <div className="text-sm font-extrabold font-mono text-emerald-400">
                    ${selectedCustomer.cartValue.toFixed(2)}
                  </div>
                </div>
              </div>
            </div>

            {/* Split Grid: Journey Visualizer + AI Root Cause & Recovery */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
              
              {/* Left Column: Visual Journey Timeline */}
              <div className="lg:col-span-7">
                <JourneyTimeline customer={selectedCustomer} />
              </div>

              {/* Right Column: AI Root Cause Analysis & Recommendations */}
              <div className="lg:col-span-5">
                <AICauseAnalysisPanel 
                  customer={selectedCustomer}
                  onTriggerAction={handleTriggerAction}
                />
              </div>

            </div>

          </div>
        )}

      </main>

      {/* Floating Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 animate-in slide-in-from-bottom-5 duration-300">
          <div className={`p-4 rounded-2xl shadow-2xl border flex items-start gap-3 max-w-md ${
            toastMessage.type === 'success' 
              ? 'bg-emerald-950/90 border-emerald-500/50 text-emerald-200' 
              : toastMessage.type === 'alert'
              ? 'bg-rose-950/90 border-rose-500/50 text-rose-200'
              : 'bg-indigo-950/90 border-indigo-500/50 text-indigo-200'
          } backdrop-blur-md`}>
            {toastMessage.type === 'success' && <CheckCircle className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />}
            {toastMessage.type === 'alert' && <AlertCircle className="w-5 h-5 text-rose-400 shrink-0 mt-0.5" />}
            {toastMessage.type === 'info' && <Info className="w-5 h-5 text-indigo-400 shrink-0 mt-0.5" />}
            <div>
              <h5 className="font-bold text-sm text-white">{toastMessage.title}</h5>
              <p className="text-xs mt-0.5 opacity-90">{toastMessage.subtitle}</p>
            </div>
          </div>
        </div>
      )}

      {/* Business Recovery Action Modal */}
      <BusinessActionModal 
        isOpen={isActionModalOpen}
        onClose={() => setIsActionModalOpen(false)}
        customer={selectedCustomer}
        action={selectedAction}
        onConfirmRecovery={handleConfirmRecovery}
      />

      {/* Live Simulation Modal */}
      <LiveSimulationModal 
        isOpen={isSimulationModalOpen}
        onClose={() => setIsSimulationModalOpen(false)}
        onInjectScenario={handleInjectScenario}
      />

      {/* Footer */}
      <footer className="border-t border-slate-900 bg-slate-950 py-6 text-center text-xs text-slate-500">
        <div className="max-w-7xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
          <span>PathPulse Enterprise • Autonomous Journey Friction Detection & Checkout Recovery</span>
          <span className="font-mono text-slate-400">All Telemetry Systems Operational • SLA: 99.98%</span>
        </div>
      </footer>
    </div>
  );
}
