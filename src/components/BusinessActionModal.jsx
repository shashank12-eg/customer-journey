import React, { useState } from 'react';
import { 
  X, 
  Send, 
  CheckCircle2, 
  Smartphone, 
  MessageSquare, 
  Sparkles, 
  ArrowRight, 
  ShieldCheck, 
  DollarSign, 
  Zap,
  Globe
} from 'lucide-react';
import confetti from 'canvas-confetti';

export default function BusinessActionModal({ 
  isOpen, 
  onClose, 
  customer, 
  action, 
  onConfirmRecovery 
}) {
  const [isExecuting, setIsExecuting] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);

  if (!isOpen || !customer || !action) return null;

  const handleExecute = () => {
    setIsExecuting(true);
    setTimeout(() => {
      setIsExecuting(false);
      setIsSuccess(true);
      
      try {
        confetti({
          particleCount: 80,
          spread: 70,
          origin: { y: 0.6 }
        });
      } catch (e) {
        // graceful fallback
      }

      onConfirmRecovery(customer.id);
    }, 1200);
  };

  const getSimulatedMessage = () => {
    if (action.actionLabel.includes('Payment')) {
      return {
        type: 'SMS Notification',
        title: 'SMS Delivery to ' + customer.name,
        sender: 'Store Checkout Pay',
        body: `Hi ${customer.name.split(' ')[0]}, we noticed a banking gateway hiccup on your order ($${customer.cartValue.toFixed(2)}). Tap below for 1-click Apple Pay / Google Pay with your reserved items: https://shop.store/pay/${customer.id.toLowerCase()}`
      };
    }
    if (action.actionLabel.includes('Shipping')) {
      return {
        type: 'In-Session Dynamic Banner',
        title: 'Browser Real-Time Banner',
        sender: 'Checkout Engine',
        body: `🎉 Free Expedited Shipping Unlocked! Guaranteed delivery by Friday, Oct 4. Proceed with 1-click checkout.`
      };
    }
    if (action.actionLabel.includes('FESTIVE20') || action.actionLabel.includes('Discount') || action.actionLabel.includes('Spec')) {
      return {
        type: 'In-Session Support Drawer',
        title: 'Proactive Checkout Assist',
        sender: 'Concierge Assistant',
        body: `We noticed your promo code inquiry. We have automatically applied your 20% discount ($15.70 savings) to complete your order.`
      };
    }
    return {
      type: 'Direct Concierge Message',
      title: 'Priority Customer Outreach',
      sender: 'Customer Experience Team',
      body: `Hello ${customer.name.split(' ')[0]}, your personal shopping concierge is here to assist with your cart. Can we help complete your checkout without hassle?`
    };
  };

  const preview = getSimulatedMessage();

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md">
      <div className="relative w-full max-w-xl bg-slate-900 border border-slate-800 rounded-3xl shadow-2xl overflow-hidden animate-in fade-in zoom-in-95 duration-200">
        
        {/* Header */}
        <div className="flex items-center justify-between p-5 border-b border-slate-800 bg-slate-950/80">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-indigo-600 to-purple-600 flex items-center justify-center text-white shadow-md">
              <Zap className="w-4 h-4" />
            </div>
            <div>
              <h3 className="text-base font-bold text-white">Execute Recovery Playbook</h3>
              <p className="text-xs text-slate-400">Autonomous customer retention and cart recovery dispatch</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 space-y-5">
          {!isSuccess ? (
            <>
              {/* Target Customer Context */}
              <div className="flex items-center justify-between p-3.5 rounded-xl bg-slate-950 border border-slate-800 text-xs">
                <div className="flex items-center gap-3">
                  <img
                    src={customer.avatar}
                    alt={customer.name}
                    className="w-10 h-10 rounded-full object-cover ring-2 ring-slate-800"
                  />
                  <div>
                    <span className="font-bold text-white text-sm">{customer.name}</span>
                    <p className="text-slate-400 text-[11px]">{customer.email} • {customer.device}</p>
                  </div>
                </div>

                <div className="text-right">
                  <span className="text-[10px] uppercase font-bold text-slate-500">Cart Total</span>
                  <div className="font-mono font-extrabold text-emerald-400 text-sm">
                    ${customer.cartValue.toFixed(2)}
                  </div>
                </div>
              </div>

              {/* Action Strategy Details */}
              <div className="p-4 rounded-xl bg-indigo-950/30 border border-indigo-500/30 text-xs">
                <div className="flex items-center justify-between mb-1.5">
                  <span className="font-bold text-indigo-300 text-sm">{action.type}</span>
                  <span className="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold font-mono">
                    {action.expectedRecoveryRate} Est. Conversion
                  </span>
                </div>
                <p className="text-slate-300 leading-relaxed">
                  {action.description}
                </p>
              </div>

              {/* Live Preview Screen */}
              <div>
                <span className="text-[10px] font-bold uppercase tracking-wider text-slate-400 mb-2 block flex items-center gap-1.5">
                  <Smartphone className="w-3.5 h-3.5 text-indigo-400" />
                  Live Preview ({preview.type})
                </span>

                <div className="bg-slate-950 p-4 rounded-2xl border border-slate-800 relative">
                  <div className="flex items-center justify-between text-[11px] text-slate-500 border-b border-slate-800/80 pb-2 mb-2">
                    <span className="font-semibold text-slate-300">{preview.sender}</span>
                    <span>Just Now</span>
                  </div>
                  <div className="p-3 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 leading-relaxed">
                    {preview.body}
                  </div>
                </div>
              </div>

              {/* CTA Buttons */}
              <div className="flex items-center justify-end gap-3 pt-2">
                <button
                  type="button"
                  onClick={onClose}
                  className="px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
                >
                  Cancel
                </button>
                <button
                  type="button"
                  disabled={isExecuting}
                  onClick={handleExecute}
                  className="px-5 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold text-xs shadow-lg shadow-emerald-600/30 flex items-center gap-2 cursor-pointer transition-all active:scale-95 disabled:opacity-50"
                >
                  {isExecuting ? (
                    <>
                      <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                      <span>Dispatching Playbook via Webhook...</span>
                    </>
                  ) : (
                    <>
                      <Send className="w-4 h-4" />
                      <span>Dispatch Recovery Playbook</span>
                    </>
                  )}
                </button>
              </div>
            </>
          ) : (
            /* Success State */
            <div className="text-center py-6 space-y-4">
              <div className="w-16 h-16 rounded-full bg-emerald-500/20 border-2 border-emerald-500 text-emerald-400 flex items-center justify-center mx-auto shadow-xl shadow-emerald-500/20 animate-bounce">
                <CheckCircle2 className="w-8 h-8" />
              </div>

              <div>
                <h4 className="text-lg font-bold text-white">Recovery Playbook Dispatched</h4>
                <p className="text-xs text-slate-400 mt-1 max-w-sm mx-auto">
                  Action dispatched to customer <strong>{customer.name}</strong>. Webhook returned 200 OK. Cart value of <strong>${customer.cartValue.toFixed(2)}</strong> secured.
                </p>
              </div>

              <div className="p-3 bg-slate-950 rounded-xl border border-slate-800 text-xs font-mono text-emerald-400 max-w-md mx-auto">
                Status: RECOVERY_CONFIRMED | Latency: 420ms | Response: 200 OK
              </div>

              <button
                onClick={onClose}
                className="px-6 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition-colors cursor-pointer"
              >
                Close & Return to Dashboard
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
