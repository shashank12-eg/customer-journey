"""
Scenario Builder Script
Generates 10 comprehensive scenario files in scenarios/ directory
Each containing:
- scenario_name
- customer_id
- journey_events
- observed_friction
- evidence
- expected_cause
- expected_severity
- expected_recovery_action
"""

import csv
import json
import os

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, "data")
SCENARIOS_DIR = os.path.join(BASE_DIR, "scenarios")
os.makedirs(SCENARIOS_DIR, exist_ok=True)

# Load events from CSV
events_by_customer = {}
with open(os.path.join(DATA_DIR, "journey_events.csv"), mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        events_by_customer.setdefault(row["customer_id"], []).append(row)

SCENARIOS_DEFINITIONS = [
    {
        "filename": "scenario_01_successful_purchase.json",
        "scenario_name": "Successful E-Commerce Purchase Journey",
        "customer_id": "CUST-1001",
        "observed_friction": "None",
        "evidence": "Customer completed smooth progression from search, product view, add to cart, single-attempt payment, to timely order fulfillment and 5-star positive review.",
        "expected_cause": "Frictionless UI/UX, transparent pricing, and instantaneous payment clearance.",
        "expected_severity": "NONE",
        "expected_recovery_action": "No corrective intervention required. Dispatch post-delivery VIP loyalty reward points and care guide."
    },
    {
        "filename": "scenario_02_cart_abandonment.json",
        "scenario_name": "High-Intent Checkout Cart Abandonment",
        "customer_id": "CUST-1002",
        "observed_friction": "Cart Abandonment",
        "evidence": "Customer added product PROD-005 ($64.99) to cart, progressed to shipping address step, dwelled for 190s upon shipping fee display, and exited without completing payment.",
        "expected_cause": "Unexpected shipping fee friction at checkout step ($14.99 additional fee).",
        "expected_severity": "MEDIUM",
        "expected_recovery_action": "Trigger automated recovery email within 30 minutes offering free shipping promo code (FREESHIP24)."
    },
    {
        "filename": "scenario_03_payment_failure.json",
        "scenario_name": "Single Gateway Timeout Payment Failure",
        "customer_id": "CUST-1003",
        "observed_friction": "Payment Failure",
        "evidence": "Customer attempted payment for ORD-2003 ($199.99), resulting in payment gateway error GATEWAY_TIMEOUT on attempt 1. Order left in pending/failed status.",
        "expected_cause": "External banking gateway timeout during 3D secure authentication handshake.",
        "expected_severity": "HIGH",
        "expected_recovery_action": "Dispatch instant SMS and email with 1-click retry payment link and alternative payment rail options (UPI/PayPal/Debit)."
    },
    {
        "filename": "scenario_04_repeated_payment_failure.json",
        "scenario_name": "Repeated Multiple Payment Failure",
        "customer_id": "CUST-1004",
        "observed_friction": "Repeated Payment Failure",
        "evidence": "Customer experienced 3 consecutive failed payment attempts within 6 minutes (CARD_DECLINED, INSUFFICIENT_FUNDS, CARD_DECLINED) on order ORD-2004 ($89.99).",
        "expected_cause": "Card credit limit restriction and issuer security decline across multiple cards.",
        "expected_severity": "CRITICAL",
        "expected_recovery_action": "Trigger priority proactive WhatsApp message with concierge payment assistance, split-payment option, and 5% courtesy retry discount."
    },
    {
        "filename": "scenario_05_delivery_delay.json",
        "scenario_name": "Logistics Delivery Delay with High Tracking Inquiries",
        "customer_id": "CUST-1005",
        "observed_friction": "Delivery Delay",
        "evidence": "Order ORD-2005 overdue past estimated delivery date (2026-09-14). Customer checked parcel tracking status 6 times across 4 days with order stuck in 'delayed' transit.",
        "expected_cause": "Carrier logistics hub congestion and delayed transit dispatch.",
        "expected_severity": "HIGH",
        "expected_recovery_action": "Proactive apology email/SMS with real-time carrier GPS tracking update, prioritized logistics expediting, and $15 store credit voucher."
    },
    {
        "filename": "scenario_06_support_complaint.json",
        "scenario_name": "Unresolved High-Priority Customer Support Complaint",
        "customer_id": "CUST-1006",
        "observed_friction": "Customer Support Complaint",
        "evidence": "Customer filed urgent support ticket TIK-3001 for wrong item received on order ORD-2006. Ticket SLA breached (unanswered for >32 hours).",
        "expected_cause": "Customer support routing queue backlog and delayed first-response SLA.",
        "expected_severity": "CRITICAL",
        "expected_recovery_action": "Automated escalation to Senior Concierge Support Supervisor, immediate doorstep prepaid exchange pickup, and instant apology call/email."
    },
    {
        "filename": "scenario_07_negative_feedback.json",
        "scenario_name": "Severe Negative Product Feedback and Defect Report",
        "customer_id": "CUST-1007",
        "observed_friction": "Negative Product Feedback",
        "evidence": "Customer submitted 1-star verified review stating product PROD-004 screen died after 3 days and battery overheats. Sentiment classified as strongly negative.",
        "expected_cause": "Hardware component defect and failure to meet user quality expectations.",
        "expected_severity": "HIGH",
        "expected_recovery_action": "Automated proactive warranty resolution email offering immediate no-return replacement or 100% refund plus a 20% discount code."
    },
    {
        "filename": "scenario_08_product_confusion.json",
        "scenario_name": "Product Information Confusion and High Hesitation",
        "customer_id": "CUST-1008",
        "observed_friction": "Product Information Confusion",
        "evidence": "Customer repeatedly switched between technical specifications and sizing guides 8 times with 420s total dwell time on PROD-007 before exiting without cart addition.",
        "expected_cause": "Complex technical specifications, unclear sizing chart, and compatibility ambiguity.",
        "expected_severity": "MEDIUM",
        "expected_recovery_action": "Trigger proactive contextual AI Shopping Assistant popup offering interactive sizing quiz, spec summary comparison, and live chat option."
    },
    {
        "filename": "scenario_09_high_browsing_no_purchase.json",
        "scenario_name": "High Browsing Volume Without Purchase (Choice Paralysis)",
        "customer_id": "CUST-1009",
        "observed_friction": "High Browsing But No Purchase",
        "evidence": "Customer viewed 18 different products across 2 sessions with 4 search/filter queries but added zero items to cart.",
        "expected_cause": "Choice overload, price-feature uncertainty, or lack of tailored recommendations.",
        "expected_severity": "MEDIUM",
        "expected_recovery_action": "Deliver personalized email curated comparison guide featuring top 3 best-rated products in viewed categories with a 10% welcome voucher."
    },
    {
        "filename": "scenario_10_successful_recovery.json",
        "scenario_name": "Successful Friction Recovery via Omnichannel Intervention",
        "customer_id": "CUST-1010",
        "observed_friction": "Recovered Friction (Prior Cart Abandonment)",
        "evidence": "Customer abandoned cart on PROD-008 ($69.98). System dispatched recovery email with RECOVER15 coupon. Customer clicked link 75 mins later, completed checkout, and successfully placed order ORD-2010.",
        "expected_cause": "Initial price hesitation successfully resolved by personalized incentive recovery intervention.",
        "expected_severity": "LOW",
        "expected_recovery_action": "Record recovery campaign conversion in analytics, suppress further abandonment messaging, and dispatch order delivery tracking guide."
    }
]

for sc in SCENARIOS_DEFINITIONS:
    cid = sc["customer_id"]
    ev_list = events_by_customer.get(cid, [])
    
    scenario_payload = {
        "scenario_name": sc["scenario_name"],
        "customer_id": sc["customer_id"],
        "observed_friction": sc["observed_friction"],
        "evidence": sc["evidence"],
        "expected_cause": sc["expected_cause"],
        "expected_severity": sc["expected_severity"],
        "expected_recovery_action": sc["expected_recovery_action"],
        "journey_events": ev_list
    }
    
    out_path = os.path.join(SCENARIOS_DIR, sc["filename"])
    with open(out_path, mode="w", encoding="utf-8") as f:
        json.dump(scenario_payload, f, indent=2)
    print(f"Created scenario file: {sc['filename']} ({len(ev_list)} events)")

# Create README.md in scenarios/
readme_content = """# Customer Journey Scenarios Directory

This directory contains standardized benchmark customer journey scenarios designed for validating the **AI-Powered Customer Journey Friction Detection and Recovery Assistant**.

## Scenario Catalog

| ID | File | Customer ID | Scenario Name | Observed Friction | Severity | Key Recovery Action |
|---|---|---|---|---|---|---|
| 01 | `scenario_01_successful_purchase.json` | `CUST-1001` | Successful Purchase | None | NONE | Post-purchase VIP loyalty care |
| 02 | `scenario_02_cart_abandonment.json` | `CUST-1002` | Cart Abandonment | Cart Abandonment | MEDIUM | Free shipping promo code (`FREESHIP24`) |
| 03 | `scenario_03_payment_failure.json` | `CUST-1003` | Single Payment Failure | Payment Failure | HIGH | Instant 1-click retry payment link |
| 04 | `scenario_04_repeated_payment_failure.json` | `CUST-1004` | Repeated Payment Failure | Repeated Payment Failure | CRITICAL | Alternate payment rail + 5% courtesy discount |
| 05 | `scenario_05_delivery_delay.json` | `CUST-1005` | Delivery Delay | Delivery Delay | HIGH | Carrier GPS tracking + $15 store credit |
| 06 | `scenario_06_support_complaint.json` | `CUST-1006` | Support SLA Complaint | Customer Support Complaint | CRITICAL | Tier-2 escalation + prepaid exchange pickup |
| 07 | `scenario_07_negative_feedback.json` | `CUST-1007` | Negative Product Review | Negative Product Feedback | HIGH | Concierge warranty replacement/refund |
| 08 | `scenario_08_product_confusion.json` | `CUST-1008` | Product Spec Confusion | Product Information Confusion | MEDIUM | Interactive sizing/compatibility assistant |
| 09 | `scenario_09_high_browsing_no_purchase.json` | `CUST-1009` | High Browsing No Cart | High Browsing But No Purchase | MEDIUM | Curated top-3 comparison + 10% welcome coupon |
| 10 | `scenario_10_successful_recovery.json` | `CUST-1010` | Successful Recovery | Recovered Friction | LOW | Recovery conversion logging + order onboarding |

## Schema Structure
Each scenario JSON file contains:
- `scenario_name`: Descriptive title of customer journey
- `customer_id`: Unique identifier referencing `data/customers.csv`
- `observed_friction`: Classification label of friction
- `evidence`: Empirical telemetry signals and event sequence proof
- `expected_cause`: Root cause diagnosis
- `expected_severity`: `NONE`, `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL`
- `expected_recovery_action`: Prescribed recovery intervention
- `journey_events`: Chronological list of user telemetry events from session start to exit
"""

with open(os.path.join(SCENARIOS_DIR, "README.md"), mode="w", encoding="utf-8") as f:
    f.write(readme_content)

print("Scenarios directory and README.md created successfully!")
