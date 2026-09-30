import React, { useState, useMemo } from 'react';
import { 
  Search, 
  Filter, 
  ShieldAlert, 
  ChevronRight, 
  Sparkles, 
  Smartphone, 
  Laptop, 
  Tablet, 
  AlertCircle,
  CheckCircle,
  Clock,
  ArrowUpDown
} from 'lucide-react';

export default function CustomerList({ 
  customers, 
  selectedCustomer, 
  onSelectCustomer, 
  onTriggerAction 
}) {
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedRisk, setSelectedRisk] = useState('ALL');
  const [selectedStatus, setSelectedStatus] = useState('ALL');

  const filteredCustomers = useMemo(() => {
    return customers.filter(customer => {
      const matchesSearch = 
        customer.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        customer.email.toLowerCase().includes(searchQuery.toLowerCase()) ||
        customer.id.toLowerCase().includes(searchQuery.toLowerCase()) ||
        customer.frictionType.toLowerCase().includes(searchQuery.toLowerCase());

      const matchesRisk = 
        selectedRisk === 'ALL' || customer.riskLevel.toUpperCase() === selectedRisk;

      const matchesStatus = 
        selectedStatus === 'ALL' || customer.status.toUpperCase() === selectedStatus;

      return matchesSearch && matchesRisk && matchesStatus;
    });
  }, [customers, searchQuery, selectedRisk, selectedStatus]);

  const getRiskBadge = (level, score) => {
    switch (level?.toLowerCase()) {
      case 'critical':
        return (
          <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-rose-500/15 text-rose-400 border border-rose-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-rose-500 animate-pulse" />
            Critical ({score})
          </span>
        );
      case 'high':
        return (
          <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-amber-500/15 text-amber-400 border border-amber-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-amber-500" />
            High ({score})
          </span>
        );
      default:
        return (
          <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold bg-blue-500/15 text-blue-400 border border-blue-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-blue-500" />
            Medium ({score})
          </span>
        );
    }
  };

  const getDeviceIcon = (device) => {
    if (device.toLowerCase().includes('phone') || device.toLowerCase().includes('android')) {
      return <Smartphone className="w-3.5 h-3.5 text-slate-400" />;
    }
    if (device.toLowerCase().includes('ipad') || device.toLowerCase().includes('tablet')) {
      return <Tablet className="w-3.5 h-3.5 text-slate-400" />;
    }
    return <Laptop className="w-3.5 h-3.5 text-slate-400" />;
  };

  return (
    <div className="bg-slate-900/70 border border-slate-800 rounded-2xl p-5 mb-6 backdrop-blur-sm shadow-xl">
      {/* List Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-4 pb-4 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-2">
            <ShieldAlert className="w-5 h-5 text-rose-400" />
            <h2 className="text-base font-bold text-white">Live Customer Sessions with Friction Alerts</h2>
            <span className="px-2 py-0.5 rounded-full text-xs font-bold bg-rose-500/20 text-rose-400 border border-rose-500/30">
              {filteredCustomers.length} Active Sessions
            </span>
          </div>
          <p className="text-xs text-slate-400 mt-0.5">
            Real-time session stream prioritized by churn risk, friction severity, and checkout value
          </p>
        </div>

        {/* Filter Controls */}
        <div className="flex flex-wrap items-center gap-2.5">
          {/* Search Bar */}
          <div className="relative min-w-[220px]">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder="Search customer, email, friction..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-9 pr-3 py-1.5 text-xs bg-slate-950 border border-slate-800 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
            />
          </div>

          {/* Risk Filter */}
          <div className="flex items-center bg-slate-950 border border-slate-800 rounded-xl p-1 text-xs">
            <span className="text-[11px] text-slate-500 px-2 font-medium">Risk:</span>
            {['ALL', 'CRITICAL', 'HIGH', 'MEDIUM'].map((risk) => (
              <button
                key={risk}
                onClick={() => setSelectedRisk(risk)}
                className={`px-2 py-0.5 rounded-lg text-[11px] font-semibold transition-colors cursor-pointer ${
                  selectedRisk === risk
                    ? 'bg-slate-800 text-white shadow-sm'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                {risk}
              </button>
            ))}
          </div>

          {/* Status Filter */}
          <div className="flex items-center bg-slate-950 border border-slate-800 rounded-xl p-1 text-xs">
            <span className="text-[11px] text-slate-500 px-2 font-medium">Status:</span>
            {['ALL', 'PENDING ACTION', 'RECOVERED'].map((st) => (
              <button
                key={st}
                onClick={() => setSelectedStatus(st)}
                className={`px-2 py-0.5 rounded-lg text-[11px] font-semibold transition-colors cursor-pointer ${
                  selectedStatus === st
                    ? 'bg-slate-800 text-white shadow-sm'
                    : 'text-slate-400 hover:text-slate-200'
                }`}
              >
                {st === 'PENDING ACTION' ? 'Pending' : st === 'RECOVERED' ? 'Recovered' : 'All'}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Table Container */}
      <div className="overflow-x-auto rounded-xl border border-slate-800/80 bg-slate-950/40">
        <table className="w-full text-left border-collapse text-xs">
          <thead>
            <tr className="border-b border-slate-800 bg-slate-950/90 text-slate-400 font-semibold uppercase tracking-wider text-[10px]">
              <th className="py-3 px-4">Customer</th>
              <th className="py-3 px-4">Journey Stage</th>
              <th className="py-3 px-4">Detected Friction</th>
              <th className="py-3 px-4">Cart Value</th>
              <th className="py-3 px-4">Risk Level</th>
              <th className="py-3 px-4">Status</th>
              <th className="py-3 px-4 text-right">Actions</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {filteredCustomers.length === 0 ? (
              <tr>
                <td colSpan={7} className="py-8 text-center text-slate-500">
                  No customers found matching the filter criteria.
                </td>
              </tr>
            ) : (
              filteredCustomers.map((cust) => {
                const isSelected = selectedCustomer?.id === cust.id;
                const isRecovered = cust.status === 'Recovered';

                return (
                  <tr
                    key={cust.id}
                    onClick={() => onSelectCustomer(cust)}
                    className={`cursor-pointer transition-all ${
                      isSelected
                        ? 'bg-indigo-950/40 border-l-4 border-l-indigo-500 hover:bg-indigo-950/60'
                        : 'hover:bg-slate-850/60 hover:bg-slate-800/30'
                    }`}
                  >
                    {/* Customer Info */}
                    <td className="py-3.5 px-4">
                      <div className="flex items-center gap-3">
                        <img
                          src={cust.avatar}
                          alt={cust.name}
                          className="w-9 h-9 rounded-full object-cover ring-2 ring-slate-800 shrink-0"
                        />
                        <div>
                          <div className="flex items-center gap-1.5">
                            <span className="font-bold text-white text-xs">{cust.name}</span>
                            <span className="text-[10px] px-1.5 py-0.2 rounded bg-slate-800 text-slate-400 font-mono">
                              {cust.id}
                            </span>
                          </div>
                          <div className="flex items-center gap-2 mt-0.5 text-[11px] text-slate-400">
                            <span>{cust.email}</span>
                            <span className="text-slate-600">•</span>
                            <span className="flex items-center gap-1">
                              {getDeviceIcon(cust.device)}
                              <span className="truncate max-w-[110px]">{cust.location}</span>
                            </span>
                          </div>
                        </div>
                      </div>
                    </td>

                    {/* Journey Stage */}
                    <td className="py-3.5 px-4 font-medium text-slate-300">
                      <span className="px-2.5 py-1 rounded-lg bg-slate-900 border border-slate-800 text-[11px]">
                        {cust.journeyStage}
                      </span>
                    </td>

                    {/* Detected Friction */}
                    <td className="py-3.5 px-4">
                      <div className="flex flex-col">
                        <span className="font-semibold text-rose-300 flex items-center gap-1">
                          <AlertCircle className="w-3.5 h-3.5 text-rose-400 shrink-0" />
                          {cust.frictionType}
                        </span>
                        <span className="text-[10px] text-slate-500 mt-0.5">
                          {cust.journeySteps[cust.journeySteps.length - 1]?.frictionAlert || 'Drop-off imminent'}
                        </span>
                      </div>
                    </td>

                    {/* Cart Value */}
                    <td className="py-3.5 px-4">
                      <span className="font-mono font-bold text-emerald-400 text-xs">
                        ${cust.cartValue.toFixed(2)}
                      </span>
                      <div className="text-[10px] text-slate-500">
                        {cust.itemsInCart.length} item{cust.itemsInCart.length > 1 ? 's' : ''}
                      </div>
                    </td>

                    {/* Risk Level */}
                    <td className="py-3.5 px-4">
                      {getRiskBadge(cust.riskLevel, cust.riskScore)}
                    </td>

                    {/* Status */}
                    <td className="py-3.5 px-4">
                      {isRecovered ? (
                        <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
                          <CheckCircle className="w-3.5 h-3.5" />
                          Recovered
                        </span>
                      ) : (
                        <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-semibold bg-amber-500/15 text-amber-400 border border-amber-500/30">
                          <Clock className="w-3.5 h-3.5" />
                          Action Needed
                        </span>
                      )}
                    </td>

                    {/* Actions */}
                    <td className="py-3.5 px-4 text-right">
                      <div className="flex items-center justify-end gap-2">
                        <button
                          onClick={(e) => {
                            e.stopPropagation();
                            onSelectCustomer(cust);
                          }}
                          className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1 transition-all cursor-pointer ${
                            isSelected
                              ? 'bg-indigo-600 text-white shadow-md shadow-indigo-600/30'
                              : 'bg-slate-900 hover:bg-slate-800 text-slate-300 border border-slate-800'
                          }`}
                        >
                          <span>Inspect Session</span>
                          <ChevronRight className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    </td>
                  </tr>
                );
              })
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
