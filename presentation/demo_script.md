# 5-Minute Live Demo Script: AI Customer Journey Friction Assistant
**Course / Capstone Presentation**  
**Role:** Member 4 (Synthetic Datasets, Journey Scenarios, Testing Framework & Demo Lead)  
**Total Duration:** ~5 Minutes (300 Seconds)

---

## Quick Reference Summary

| Phase | Time | Action | Focus Customer / Feature | Key Message |
|---|---|---|---|---|
| **Phase 1** | 0:00 – 0:45 | Launch & Overview | Dashboard UI & Metrics Ribbon | Introduce system purpose & 120 synthetic customer dataset |
| **Phase 2** | 0:45 – 1:30 | Select Friction Customer | `CUST-1004` (David Kim) | Repeated payment failure journey & event timeline |
| **Phase 3** | 1:30 – 2:30 | AI Friction Analysis | `CUST-1004` Diagnosis | Detection badge, category, 98% confidence, root cause & evidence |
| **Phase 4** | 2:30 – 3:15 | Recovery Intervention | `CUST-1004` Recovery | Recommended action & "Simulate Intervention Dispatch" |
| **Phase 5** | 3:15 – 4:00 | Second Customer Comparison | `CUST-1001` (Sarah Chen) | Benchmark healthy, frictionless purchase journey |
| **Phase 6** | 4:00 – 4:45 | Live Test Suite Execution | Modal Test Runner | 13/13 automated scenario & data consistency tests passing |
| **Phase 7** | 4:45 – 5:00 | Closing & Q&A Transition | Team Summary | Wrap up deliverables and invite professor questions |

---

## Detailed Step-by-Step Demo Script

### Phase 1: Opening the Dashboard & Setting the Context (0:00 – 0:45)
**Screen Action:**
1. Open terminal and run:
   ```bash
   python app.py
   ```
2. Open web browser to `http://localhost:8000`.
3. Point your mouse to the top **Metrics Ribbon**.

**Spoken Script:**
> *"Good morning, esteemed professors and committee members. Today, I am proud to present Member 4's contributions to our team project: the AI-Powered Customer Journey Friction Detection and Recovery Assistant.*
>
> *As Member 4, my role encompasses generating the synthetic data foundation, formalizing real-world journey scenarios, building the automated testing system, and validating the AI recovery pipeline.*
>
> *Here on the live dashboard, you can see our telemetry summary: we have engineered 120 synthetic customer profiles, 25 catalog products, 81 orders, 83 payments, and 583 chronological journey events—all created with zero real personal data, complete referential integrity, and logical consistency across 10 distinct e-commerce friction scenarios."*

---

### Phase 2: Selecting an At-Risk Customer & Showing Their Journey (0:45 – 1:30)
**Screen Action:**
1. Click the quick scenario button: **`CUST-1004 (Repeated Payment Fail)`** (or select **David Kim** from the customer dropdown).
2. Point to the **Customer Profile Card** on the left.
3. Scroll down the **Customer Journey Event Timeline** on the right.

**Spoken Script:**
> *"Let us inspect an immediate high-friction case: Customer CUST-1004, David Kim. David is a high-value customer with 5 prior successful lifetime orders.*
>
> *Looking at his Journey Timeline on the right, we see him view an Ultra-Slim Wireless Keyboard, add it to his cart, and begin checkout for order ORD-2004.*
>
> *Notice what happens next in the timeline: at 11:02, his first credit card payment fails with error code CARD_DECLINED. He immediately retries with another card at 11:03, but encounters INSUFFICIENT_FUNDS. He tries a third time at 11:05 with a debit card, but the transaction times out. David then abandons the session in frustration.*
>
> *In a conventional e-commerce setup, David would simply become an abandoned cart statistic."*

---

### Phase 3: Demonstrating AI Friction Detection, Evidence & Confidence (1:30 – 2:30)
**Screen Action:**
1. Point to the **AI Friction Detection Card** on the left.
2. Highlight the **Red `CRITICAL` Severity Tag** and Category.
3. Highlight the **AI Confidence Meter** (98% progress bar).
4. Point to the **Root Cause** block and the dashed **Observed Empirical Evidence Box**.

**Spoken Script:**
> *"Now let's examine what our AI Friction Detection Engine does in real time:*
>
> *First, it flags the journey with a status tag of CRITICAL severity under the category 'Repeated Payment Failure'.*
>
> *Second, notice our AI Confidence Meter: the model reports a 98% confidence score. This high score is derived from our multi-signal heuristic engine, which recognizes a 3-failure streak across two payment rails within a short time window.*
>
> *Third, look at the explainability: our AI does not output a mysterious black-box number. Under 'Observed Empirical Evidence', it explicitly cites the exact error codes—CARD_DECLINED and INSUFFICIENT_FUNDS—and proves that the customer reached final payment before being blocked by banking authorization barriers."*

---

### Phase 4: Showing Recommended Recovery Action & Simulating Dispatch (2:30 – 3:15)
**Screen Action:**
1. Scroll to the **Recommended Recovery Action Card**.
2. Read the highlighted action strategy text.
3. Click the blue button: **`✉️ Simulate Intervention Dispatch`**.
4. Point to the green toast notification confirming dispatch.

**Spoken Script:**
> *"Detection is only half the battle; recovery is what saves revenue. Here in the Recommended Recovery Action card, the assistant dynamically prescribes a targeted omnichannel intervention:*
>
> *Instead of sending a generic marketing discount email hours later, it triggers a priority WhatsApp and SMS message offering alternate payment methods—such as one-click UPI or NetBanking—accompanied by a 5% courtesy retry discount.*
>
> *When we click 'Simulate Intervention Dispatch' [CLICK], the event is instantly orchestrated, sending the tailored payment link directly to David's phone before he switches to a competitor."*

---

### Phase 5: Showing a Second, Successful Customer for Contrast (3:15 – 4:00)
**Screen Action:**
1. Click the quick scenario chip: **`CUST-1001 (Smooth Purchase)`** (Sarah Chen).
2. Point to the green **`Journey Healthy (No Friction)`** badge.
3. Show the timeline progressing smoothly: Search ➔ Product View ➔ Cart ➔ Single Payment Success ➔ Order Delivered ➔ 5-Star Review.
4. Click the **Feedback Tab** on the bottom right to show the 5-star review.

**Spoken Script:**
> *"To verify that our AI system does not produce false alarms, let us inspect a second customer: CUST-1001, Sarah Chen [CLICK].*
>
> *Immediately, the dashboard updates:*
> *The AI status reflects 'Journey Healthy (No Friction)' with severity 'NONE'.*
>
> *Sarah's timeline shows an optimal funnel: search for ergonomic chair, product view, add to cart, single-attempt payment clearance, and on-time fulfillment.*
>
> *Checking the Feedback tab on the bottom right, we see Sarah submitted a verified 5-star review: 'Best office chair ever!'.*
>
> *Our AI correctly identifies that no corrective intervention is needed, recommending only standard VIP post-delivery loyalty reward points."*

---

### Phase 6: Demonstrating Automated Test Suite Execution (4:00 – 4:45)
**Screen Action:**
1. Move mouse to the header button: **`🧪 Run Test Suite (13 Tests)`** and click it.
2. The modal pops up and executes the test suite live.
3. Show the green banner: **`ALL 13 TESTS PASSED SUCCESSFULLY (0 Failures, 0 Errors)`**.
4. Scroll through the terminal output inside the modal.

**Spoken Script:**
> *"Software engineering quality requires automated verification. In tests/test_scenarios.py, we built an automated test harness using Python's standard unittest framework.*
>
> *Let's click 'Run Test Suite' to execute all tests live right from the dashboard [CLICK].*
>
> *In less than 30 milliseconds, the test suite executes 13 distinct tests:*
> - *It validates that our dataset has 120 customers (exceeding the 100-customer requirement).*
> - *It verifies referential integrity and timestamp chronology.*
> - *And it systematically tests all 10 customer scenarios against our machine-readable expected_results.json—checking friction detection, category, severity, confidence thresholds, evidence keywords, and recovery recommendations.*
>
> *As you can see on screen: 13 out of 13 tests pass with 0 failures and 0 errors."*

---

### Phase 7: Conclusion & Wrap-Up (4:45 – 5:00)
**Screen Action:**
1. Close the test modal.
2. Return to the main dashboard view.
3. Look up and address the panel.

**Spoken Script:**
> *"In summary, Member 4 has delivered:
> 1. A clean, 7-table synthetic e-commerce dataset with 120 customers and 583 events.
> 2. 10 standardized scenario specifications in scenarios/.
> 3. An explainable AI Friction Analyzer and working dashboard.
> 4. An automated 13-test regression suite with machine-readable expectations.
> 5. Complete presentation slides and documentation.
>
> Thank you, professors. I am now open to any questions!"*

---

## Presenter Preparation Checklist
- [ ] Terminal window ready in directory `member4`.
- [ ] Command `python app.py` tested and confirmed responsive on port `8000`.
- [ ] Browser window bookmarked to `http://localhost:8000`.
- [ ] Rehearse clicking `CUST-1004` (Friction) then `CUST-1001` (Success) then `Run Test Suite`.
- [ ] Keep `tests/expected_results.json` and `scenarios/README.md` open in VS Code if examiners ask to inspect the code.
