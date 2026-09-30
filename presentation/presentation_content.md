# AI-Powered Customer Journey Friction Detection and Recovery Assistant
## Final Project Presentation Content (10 Slides)
**Course / Capstone:** College Engineering Project / Pair Programming Team  
**Role:** Member 4 (Synthetic Datasets, Journey Scenarios, Testing Framework & Presentation Lead)

---

### Slide 1: Problem Statement
**Title:** The Hidden Leak in Modern E-Commerce: Silent Customer Journey Friction

#### Key Presentation Points
- **The E-Commerce Abandonment Crisis:** On average, 68%–74% of online shopping carts are abandoned prior to purchase, with billions lost annually to silent, unaddressed checkout and post-order friction.
- **Why Traditional Analytics Fail:**
  - Standard dashboards (Google Analytics, Mixpanel) report *aggregate drop-offs* after users leave, offering zero real-time remediation.
  - Funnel metrics show *where* drop-offs occur (e.g. 35% drop at payment), but fail to diagnose *why* (gateway timeouts, card limits, hidden shipping fees, spec ambiguity).
- **The Customer Experience Reality:** Modern shoppers rarely complain before leaving; they encounter friction (repeated payment card declines, ambiguous sizing, unexpected fees) and simply close the tab to buy from a competitor.
- **The Opportunity:** Moving from passive post-mortem analytics to proactive, real-time friction detection and automated recovery.

#### Visual / Diagram Suggestion
- A split graphic: Left side showing a "Leaky Funnel" with lost customers; Right side showing an AI safety net catching and recovering at-risk shoppers before they bounce.

#### Speaker Notes
> *"Respected professors and evaluators, welcome to our presentation. Every day, e-commerce platforms invest heavily in customer acquisition through search ads and social campaigns. However, up to 70% of shoppers abandon their journey before completing a purchase. Traditional analytics tell us that users left, but they do so too late. Our project, the AI-Powered Customer Journey Friction Detection and Recovery Assistant, is built to change this paradigm by monitoring real-time telemetry, diagnosing root causes, and triggering automated recovery interventions before the customer is lost."*

---

### Slide 2: Understanding Customer Journey Friction
**Title:** Taxonomy & Anatomy of E-Commerce Friction Points

#### Key Presentation Points
- **Friction Definition:** Any cognitive hesitation, technical impediment, or logistical breakdown that impedes a customer from achieving their intended shopping goal.
- **Pre-Purchase Friction:**
  - *Product Information Confusion:* Rapid toggling between specs, size charts, and reviews with high dwell time and zero cart additions.
  - *Choice Paralysis / High Browsing:* Viewing dozens of products across categories without committing to an add-to-cart.
- **Checkout & Transactional Friction:**
  - *Cart Abandonment:* Sticker shock at shipping fee reveal or complicated multi-step checkout.
  - *Single Payment Failure:* Payment gateway timeout (`GATEWAY_TIMEOUT`) or network drop.
  - *Repeated Payment Failure:* Consecutive declines (`CARD_DECLINED`, `INSUFFICIENT_FUNDS`) driving extreme customer frustration.
- **Post-Purchase & Fulfillment Friction:**
  - *Logistics Delivery Delays:* Packages overdue past ETA causing repeated parcel tracking inquiries.
  - *Unresolved Support Complaints:* Priority tickets languishing past SLA due to support backlogs.
  - *Negative Product Reviews:* Hardware defects or quality mismatches leading to 1-star reviews.

#### Visual / Diagram Suggestion
- A horizontal journey map spanning **Discovery ➔ Consideration ➔ Checkout ➔ Fulfillment ➔ Retention**, with friction icons pinned at critical vulnerability points.

#### Speaker Notes
> *"To address friction effectively, we established a clear taxonomy across the entire customer lifecycle. Friction is not just a failed payment. It begins during discovery with sizing confusion and choice overload, peaks at checkout with unexpected fees and card declines, and continues post-purchase with delivery delays and unanswered support tickets. By categorizing these friction types, we can assign tailored recovery strategies to each."*

---

### Slide 3: Proposed Solution
**Title:** AI-Powered Friction Detection & Recovery Assistant

#### Key Presentation Points
- **Core Philosophy:** Real-Time Telemetry Ingestion + Explainable AI Reasoning + Automated Omnichannel Recovery.
- **Three Pillar System:**
  1. **Omnichannel Telemetry Ingestion:** Continuous event streaming capturing clickstream, checkout dwell time, gateway response codes, carrier tracking, and sentiment.
  2. **Explainable AI Friction Engine:** Multi-signal behavioral heuristics and pattern recognition that classify friction category, quantify severity, calculate confidence, and isolate root causes.
  3. **Automated Recovery Orchestrator:** Dynamic dispatch of personalized micro-interventions (alternate payment links, free shipping coupons, warranty outreach, carrier GPS updates).
- **Key Differentiator:** Transparent, explainable AI outputs—giving customer experience teams clear evidence and audit trails rather than black-box guesses.

#### Visual / Diagram Suggestion
- Three-pillar workflow diagram showing: `Telemetry Streams ➔ AI Cognitive Engine ➔ Omnichannel Recovery Dispatch`.

#### Speaker Notes
> *"Our solution acts as an intelligent co-pilot for e-commerce platforms. Rather than relying on static rules or black-box predictions, our AI Assistant combines multi-signal telemetry—from clickstream dwell times to payment gateway error codes—to continuously evaluate customer journey health. When friction is detected, it immediately calculates a confidence score, identifies the root cause, and prescribes a precise recovery intervention."*

---

### Slide 4: System Architecture
**Title:** End-to-End System Architecture & Data Flow

#### Key Presentation Points
```
+-----------------------------------------------------------------------------------+
|                            E-COMMERCE DATA LAYER                                  |
|  customers.csv | products.csv | journey_events.csv | payments.csv | orders.csv     |
|                   support_tickets.csv | feedback.csv                              |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                       DATA INGESTION & NORMALIZATION PIPELINE                     |
|  - Referential Integrity Validation     - Chronological Session Sorting           |
|  - JSON Metadata Extraction             - Multi-Table Entity Linking              |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                        AI FRICTION ANALYZER ENGINE                                |
|  - Payment Failure Streak Classifier    - Support Ticket SLA Monitor              |
|  - Cart Abandonment Hesitation Detector - Product Spec Confusion Index            |
|  - Logistics Delay & Tracking Detector  - Sentiment & Feedback Analyzer           |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                 EXPLAINABLE OUTPUT & RECOVERY ORCHESTRATOR                        |
|  * Friction Category * Severity (CRITICAL/HIGH/MED/LOW/NONE) * Confidence Score   |
|  * Empirical Evidence Trail      * Prescribed Omnichannel Intervention            |
+------------------------------------------+----------------------------------------+
                                           |
                                           v
+-----------------------------------------------------------------------------------+
|                    INTERACTIVE DASHBOARD & TEST AUTOMATION                        |
|  - Real-Time Journey Timeline           - Interactive Recovery Simulation         |
|  - 120-Customer Directory Explorer      - Live 13-Test Scenario Validation Runner |
+-----------------------------------------------------------------------------------+
```

#### Speaker Notes
> *"Slide 4 illustrates our system architecture. At the base is our relational data layer covering 7 key entities. The ingestion engine validates foreign keys and orders events chronologically. The AI Friction Analyzer runs specialized detection algorithms—such as payment failure streak tracking and hesitation indexing. The output includes category classification, severity rating, confidence score, and root-cause evidence, which feed directly into our interactive dashboard and automated test suite."*

---

### Slide 5: Synthetic Dataset Design & Integrity
**Title:** Comprehensive Synthetic E-Commerce Telemetry (Member 4 Contribution)

#### Key Presentation Points
- **Zero Real PII:** Designed 100% synthetic, ethically sound, GDPR-compliant profiles with realistic customer personas, addresses, and transaction histories.
- **Relational Dataset Schema (7 Relational Tables in `data/`):**
  - `customers.csv` (120 records): Demographic segments (Loyal VIP, High Value, Window Shopper, Lapsed), lifetime order counts, payment preferences.
  - `products.csv` (25 records): Diverse catalog (Electronics, Apparel, Furniture, Wearables) with pricing and stock.
  - `orders.csv` (81 records): Order dates, totals, delivery dates, and real-time fulfillment statuses.
  - `payments.csv` (83 records): Multi-rail transactions (Cards, UPI, PayPal), retry attempts, and standard gateway error codes (`CARD_DECLINED`, `GATEWAY_TIMEOUT`, `INSUFFICIENT_FUNDS`).
  - `journey_events.csv` (583 records): Granular telemetry containing session IDs, event types, dwell times, and JSON metadata.
  - `support_tickets.csv` (5 records): SLA tracking, priority rankings, category classification, and agent notes.
  - `feedback.csv` (20 records): 1-to-5 star ratings, sentiment classification, and textual reviews.
- **Data Validation Guarantee:** Passed automated validation (`validate_data.py`) with zero foreign key mismatches, verified session monotonicity, and 100% scenario coverage.

#### Speaker Notes
> *"As Member 4, my primary responsibility was engineering the synthetic data foundation. Machine learning and AI systems are only as good as the data feeding them. We built 7 interconnected CSV datasets featuring 120 synthetic customer profiles and 583 journey telemetry events. Every order, payment, and support ticket strictly satisfies referential integrity, and our automated validation script confirms that event timestamps are strictly chronological within every user session."*

---

### Slide 6: AI Analysis & Multi-Signal Heuristics
**Title:** Multi-Signal Pattern Recognition, Severity Classification & Confidence Scoring

#### Key Presentation Points
- **Deterministic Multi-Signal Reasoning:**
  - Evaluates journey events, payment streaks, carrier tracking timestamps, and customer support ticket queues simultaneously.
- **Severity Classification Matrix:**
  - **CRITICAL:** Repeated payment failure (>=2 consecutive declines); High-priority customer support ticket with breached SLA (>24 hours).
  - **HIGH:** Single payment gateway timeout; Delivery delay with >=3 customer tracking checks; 1-star product defect review.
  - **MEDIUM:** Cart abandonment at checkout shipping step; High product spec/sizing toggling (confusion); High browsing (>=8 products) with zero cart additions.
  - **LOW / NONE:** Successful recovery after intervention; Clean journey with smooth progression and on-time fulfillment.
- **Confidence Scoring Algorithm:**
  - Confidence ($C \in [0.80, 0.98]$) is calculated based on signal density (e.g. 3 consecutive payment failure events yield 0.98 confidence; cart exit with dwell time yields 0.88 confidence).
- **Explainability First:** Generates an empirical evidence string citing exact error codes, order IDs, dwell times, and timestamps.

#### Speaker Notes
> *"Slide 6 explains our AI reasoning engine. We avoid black-box ambiguity by computing deterministic multi-signal heuristics. For instance, if a customer experiences two or more consecutive payment failures, the system immediately flags the journey as 'CRITICAL' severity with 98% confidence, cites the specific error codes in the empirical evidence trail, and suppresses generic promotions in favor of payment-assist recovery."*

---

### Slide 7: Showcase Customer Journey Case Study
**Title:** Deep-Dive: Scenario 4 – Repeated Payment Failure (`CUST-1004`)

#### Key Presentation Points
- **Customer Profile:** David Kim (`CUST-1004`), High-Value Segment, 5 Lifetime Orders.
- **Intended Purchase:** Ultra-Slim Wireless Mechanical Keyboard (PROD-001, $89.99).
- **Observed Journey Telemetry:**
  1. `11:00:00` – Product View: PROD-001 (Dwell: 60s)
  2. `11:01:05` – Add to Cart (Quantity: 1)
  3. `11:01:35` – Checkout Started (Order: ORD-2004)
  4. `11:02:10` – Payment Attempt #1: Credit Card ➔ **FAILED (`CARD_DECLINED`)**
  5. `11:03:30` – Payment Attempt #2: Credit Card ➔ **FAILED (`INSUFFICIENT_FUNDS`)**
  6. `11:05:10` – Payment Attempt #3: Debit Card ➔ **FAILED (`CARD_DECLINED` / 3DS Timeout)**
  7. `11:06:45` – Session Terminated / Drop-off.
- **AI Diagnosis:**
  - Category: `Repeated Payment Failure` | Severity: `CRITICAL` | Confidence: `98%`
  - Root Cause: Multiple bank authorization declines across credit/debit limits.
  - Evidence: "Observed 3 consecutive payment failure attempts. Error codes: CARD_DECLINED, INSUFFICIENT_FUNDS."

#### Speaker Notes
> *"Let us examine a concrete case study: Customer CUST-1004, David Kim. David is a high-value customer attempting to purchase an $89.99 mechanical keyboard. Within a span of 6 minutes, he attempted payment 3 separate times across credit and debit cards, receiving bank declines. Conventional analytics would only record that David didn't complete checkout. Our AI Assistant captures the exact error codes, recognizes a critical 3-failure streak, and triggers an immediate intervention."*

---

### Slide 8: Automated Recovery Intervention Strategy
**Title:** Closed-Loop Omnichannel Recovery Orchestration

#### Key Presentation Points
- **Dynamic Action Mapping:** Every friction category maps to an automated, contextual recovery action:
  - *Repeated Payment Failure:* Priority WhatsApp message with one-click UPI/NetBanking payment link + 5% courtesy retry discount.
  - *Cart Abandonment:* Automated email within 30 minutes offering free shipping promo code (`FREESHIP24`).
  - *Logistics Delivery Delay:* Proactive SMS apology with live carrier GPS tracking link + $15 store credit voucher.
  - *Unresolved Support SLA Breach:* Automatic escalation to Tier-2 senior supervisor + prepaid doorstep return/replacement pickup.
  - *Product Spec Confusion:* Interactive AI Shopping Assistant popup with sizing quiz and live agent chat assist.
- **Proven Recovery (Scenario 10 - `CUST-1010`):**
  - Customer Kevin Zhang abandoned cart at 15:03.
  - System dispatched recovery email with promo code `RECOVER15` at 15:38.
  - Customer clicked link at 16:53, completed checkout, and successfully placed order `ORD-2010`!

#### Speaker Notes
> *"Detection without action is useless. Slide 8 shows our closed-loop recovery mechanism. Instead of blasting generic marketing newsletters, the system dispatches context-specific interventions. For payment failures, it sends an alternate payment link with a courtesy discount. For shipping delays, it provides store credit and live GPS tracking before the customer even complains. Scenario 10 proves this works: a customer who abandoned cart was successfully recovered within 75 minutes via an automated discount link, completing order ORD-2010."*

---

### Slide 9: Testing, Validation & Results
**Title:** Comprehensive Automated Verification & Test Bench

#### Key Presentation Points
- **Testing Architecture (`tests/test_scenarios.py`):**
  - Built with Python's standard `unittest` framework for 100% portability without external dependencies.
  - Machine-readable benchmark specification (`tests/expected_results.json`).
- **Validated Test Suite (13 / 13 Tests Passing):**
  - `test_01`: Dataset minimum customer count (120 >= 100).
  - `test_02`: Complete referential integrity across orders, payments, tickets, and events.
  - `test_03`: Monotonic chronological timestamp sequence verification.
  - `test_04 - test_13`: Comprehensive scenario checks covering friction detection flag, category classification, severity tier, minimum confidence threshold, empirical evidence keywords, and recommended recovery strategy.
- **Execution Performance:** 13 tests execute in under 0.025 seconds with 0 failures and 0 errors.

#### Speaker Notes
> *"To ensure rigorous software engineering standards, we built a comprehensive test suite. In tests/test_scenarios.py, we evaluate 13 distinct assertions against our machine-readable expected results specification. We test dataset scale, referential integrity, event chronology, and each of the 10 friction scenarios. All 13 tests run in less than 25 milliseconds and pass with a 100% success rate, ensuring zero regressions."*

---

### Slide 10: Conclusion & Future Enhancements
**Title:** Project Summary & Next-Generation Roadmap

#### Key Presentation Points
- **Summary of Member 4 Contributions:**
  - 7 relational synthetic datasets (120 customers, 583 journey events, zero PII, 100% logically consistent).
  - 10 standardized benchmark journey scenario specifications in `scenarios/`.
  - Automated testing suite and machine-readable `expected_results.json`.
  - Explainable AI friction analyzer and interactive web dashboard.
  - Complete presentation deck and 5-minute timed live demo script.
- **Future Enhancements Roadmap:**
  1. *Machine Learning Predictive Modeling:* Train XGBoost / Random Forest classifiers on historical session trajectories to predict friction *before* checkout exit.
  2. *Reinforcement Learning for Recovery Optimization:* Use Multi-Armed Bandits to dynamically optimize discount percentages based on customer lifetime value.
  3. *Real-Time WebSocket Streaming:* Connect live Kafka/WebSocket telemetry streams for sub-second in-session intervention triggers.
  4. *Large Language Model (LLM) Support Integration:* Generate hyper-personalized empathetic support emails and conversational recovery scripts.

#### Speaker Notes
> *"In conclusion, Member 4 has delivered a production-ready synthetic data foundation, benchmark scenario suite, automated testing framework, and an explainable AI assistant dashboard. For future work, we plan to implement predictive machine learning to stop friction before it happens, and reinforcement learning to optimize intervention rewards. Thank you for your time, and we are now excited to demonstrate the live application!"*
