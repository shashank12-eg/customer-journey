# Customer Journey Scenarios Directory

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
