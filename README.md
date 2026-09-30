# PathPulse AI — Enterprise Customer Journey Friction Detection & Autonomous Recovery

> **Industry**: Enterprise Retail & E-Commerce  
> **Platform**: Real-Time Behavioral Telemetry, AI Root-Cause Diagnostics & Automated Checkout Recovery

---

## 🎯 Platform Overview

E-commerce brands lose billions in revenue annually due to hidden checkout friction—such as 3DS payment gateway timeouts, delivery date uncertainty, unexpected courier surcharges, broken discount rules, and comparison fatigue. Traditional web analytics platforms only display *where* shoppers drop off, without diagnosing *why* it happened or taking real-time recovery action.

**PathPulse AI** is an enterprise intelligence and recovery platform that continuously monitors high-velocity clickstream events, detects micro-friction patterns (rage clicks, latency anomalies, rapid back-navigation), diagnoses the exact technical or behavioral root cause, and autonomously executes margin-preserving recovery playbooks before the shopper abandons the store.

---

## 🔄 Real-Time Closed-Loop Pipeline

PathPulse operates on an autonomous 5-stage closed loop:

```
[ Customer Telemetry ] ➔ [ Friction Detection ] ➔ [ Root Cause Diagnosis ] ➔ [ Recovery Strategy ] ➔ [ Automated Dispatch ]
   (Clickstream &           (Rage Clicks &            (Diagnostic AI             (Dynamic Margin-        (1-Click Real-Time
    Event Stream)           Latency Spikes)             Inference)              Preserving Offers)            Webhook)
```

---

## 🚀 Key Modules & Architecture

### 1. 📊 Executive Operations Center (`src/components/KPIHeader.jsx`)
- **Sessions Monitored (24h)**: 42,850 live sessions (+14.2% growth)
- **Friction Incidents Detected**: 1,842 sessions flagged (4.3% anomaly rate)
- **Gross GMV at Risk**: $184,200 identified
- **Recovered Revenue**: $129,500 secured (70.3% recovery rate)
- **AI Diagnostic Accuracy**: 94.2% (validated on 14,200 events)
- **Mean Time to Recovery**: 1.8 mins (-42s vs manual queues)

### 2. 📈 Conversion & Telemetry Analytics (`src/components/AnalyticsCharts.jsx`)
- **Funnel Drop-Off & Friction Points**: Visualizes visitor drop-offs and incident concentrations across 6 stages (Store Entry ➔ Product Detail ➔ Cart ➔ Checkout ➔ Payment ➔ Order Completed).
- **Friction Root Cause Distribution**: Donut breakdown highlighting Payment Gateways (34%), Delivery Uncertainty (26%), Promo Invalidation (18%), Specs Gaps (14%), and Policy/Fees (8%).
- **Friction vs Recovery Rate (24h)**: Continuous area chart monitoring incoming friction alerts against autonomous recovery confirmations.
- **Playbook Recovery Efficiency**: Performance benchmarks across recovery channels (Alternative Pay Link: 85.8%, In-App Dynamic Banner: 81.9%, Concierge VIP Assist: 75.1%, Shipping Waiver: 75.0%).

### 3. 👥 Live Customer Sessions (`src/components/CustomerList.jsx`)
- Prioritized real-time stream filtered by **Churn Risk** (*Critical, High, Medium*), **Friction Category**, and **Status** (*Action Required, Recovered*).
- Complete session context: client device (iOS Safari, Chrome Desktop, Edge, iPadOS), location, item details, cart values, and real-time risk scores.

### 4. 🧭 Session Journey Timeline (`src/components/JourneyTimeline.jsx`)
- Reconstructed chronological user path from landing to drop-off.
- Tracks step-by-step dwell times, route URLs, sentiment analysis (Engaged, Browsing, Hesitant, Friction Spike), and specific behavioral flags (e.g. *5 Rapid Rage Clicks*, *ERR_3DS_CHALLENGE_TIMEOUT*).
- Click any touchpoint to expand the **raw event telemetry JSON payload**.

### 5. 🧠 Root Cause Diagnosis & Reasoning (`src/components/AICauseAnalysisPanel.jsx`)
- High-certainty root cause explanation powered by multi-signal behavioral inference.
- Empirical telemetry breakdown (error codes, click velocity, customer lifetime value, historical order frequency).
- Ranked dynamic recovery playbooks with expected conversion yield.

### 6. ⚡ Autonomous Recovery Dispatch (`src/components/BusinessActionModal.jsx`)
- One-click trigger for autonomous retention playbooks.
- **Interactive Live Preview** of customer touchpoint (SMS notification, in-session dynamic toast banner, or proactive support drawer).
- Real-time webhook dispatch simulation with confetti feedback and dynamic revenue balance adjustments.

### 7. 🧪 Live Friction Incident Simulator (`src/components/LiveSimulationModal.jsx`)
- Allows operators to inject real-world retail edge cases:
  - *Incident A*: 3DS Bank OTP Gateway Challenge Timeout ($420 cart)
  - *Incident B*: Unexpected Express Shipping Surcharge Shock ($185 cart)
  - *Incident C*: Promo Code Validation Rule Bug at $190
  - *Incident D*: Product Specification Vacuum & Return Fear ($650 cart)

---

## 🛠️ Technology Stack

- **Framework**: React 19 + Vite 8
- **Styling**: Tailwind CSS v4 (Production Enterprise Dark Theme)
- **Visualizations**: Recharts (Funnel, Pie, Area, Bar)
- **Icons**: Lucide React
- **Micro-Interactions**: Canvas Confetti

---

## 🚀 Getting Started

```bash
# 1. Install dependencies
npm install

# 2. Launch production development server
npm run dev

# 3. Production build
npm run build
```

Application URL: **http://127.0.0.1:5173/**
