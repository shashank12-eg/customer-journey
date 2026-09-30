import React from 'react';
import { 
  Users, 
  AlertTriangle, 
  DollarSign, 
  CheckCircle2, 
  Brain, 
  Clock, 
  TrendingUp, 
  TrendingDown, 
  ArrowUpRight 
} from 'lucide-react';
import { KPI_DATA } from '../data/mockData';

export default function KPIHeader({ dynamicStats }) {
  const stats = dynamicStats || KPI_DATA;

  const kpis = [
    {
      title: "Sessions Monitored (24h)",
      value: stats.sessionsMonitored,
      change: stats.sessionsGrowth,
      isPositive: true,
      icon: Users,
      color: "from-blue-500/20 to-cyan-500/20",
      border: "border-blue-500/30",
      iconColor: "text-blue-400"
    },
    {
      title: "Friction Incidents",
      value: stats.frictionDetected,
      change: stats.frictionRate,
      isPositive: false,
      icon: AlertTriangle,
      color: "from-amber-500/20 to-rose-500/20",
      border: "border-amber-500/30",
      iconColor: "text-amber-400"
    },
    {
      title: "Gross GMV at Risk",
      value: stats.revenueAtRisk,
      change: stats.revenueAtRiskTrend,
      isPositive: true,
      icon: DollarSign,
      color: "from-rose-500/20 to-orange-500/20",
      border: "border-rose-500/30",
      iconColor: "text-rose-400"
    },
    {
      title: "Recovered Revenue",
      value: stats.recoveredRevenue,
      change: `${stats.recoveryRate} Recovery Rate`,
      isPositive: true,
      icon: CheckCircle2,
      color: "from-emerald-500/20 to-teal-500/20",
      border: "border-emerald-500/30",
      iconColor: "text-emerald-400"
    },
    {
      title: "AI Diagnostic Accuracy",
      value: stats.aiModelConfidence,
      change: "Validated on 14.2k events",
      isPositive: true,
      icon: Brain,
      color: "from-purple-500/20 to-indigo-500/20",
      border: "border-purple-500/30",
      iconColor: "text-purple-400"
    },
    {
      title: "Mean Time to Recovery",
      value: stats.avgRecoveryTime,
      change: "-42s vs manual queue",
      isPositive: true,
      icon: Clock,
      color: "from-indigo-500/20 to-blue-500/20",
      border: "border-indigo-500/30",
      iconColor: "text-indigo-400"
    }
  ];

  return (
    <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-3.5 mb-6">
      {kpis.map((kpi, idx) => {
        const Icon = kpi.icon;
        return (
          <div
            key={idx}
            className={`relative overflow-hidden rounded-2xl p-4 bg-slate-900/70 border ${kpi.border} backdrop-blur-sm hover:border-slate-600 transition-all group`}
          >
            <div className={`absolute -right-6 -bottom-6 w-20 h-20 rounded-full bg-gradient-to-br ${kpi.color} blur-xl group-hover:scale-125 transition-transform duration-500`} />
            
            <div className="flex items-center justify-between mb-2">
              <span className="text-[11px] font-semibold tracking-wide text-slate-400 uppercase">
                {kpi.title}
              </span>
              <div className={`p-1.5 rounded-lg bg-slate-800/80 ${kpi.iconColor}`}>
                <Icon className="w-4 h-4" />
              </div>
            </div>

            <div className="flex flex-col">
              <span className="text-xl font-extrabold text-white tracking-tight">
                {kpi.value}
              </span>
              <div className="flex items-center gap-1 mt-1 text-[11px] font-medium">
                {kpi.isPositive ? (
                  <TrendingUp className="w-3.5 h-3.5 text-emerald-400" />
                ) : (
                  <TrendingDown className="w-3.5 h-3.5 text-amber-400" />
                )}
                <span className={kpi.isPositive ? "text-emerald-400" : "text-amber-400"}>
                  {kpi.change}
                </span>
              </div>
            </div>
          </div>
        );
      })}
    </div>
  );
}
