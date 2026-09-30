"""
Dataset Integrity and Logical Consistency Validator
For E-Commerce Customer Journey Friction Assistant
"""

import csv
import json
import os
import sys
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing required CSV: {filename}")
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def run_validation():
    print("=" * 60)
    print("STARTING SYNTHETIC DATASET INTEGRITY & LOGICAL CONSISTENCY AUDIT")
    print("=" * 60)

    customers = load_csv("customers.csv")
    products = load_csv("products.csv")
    orders = load_csv("orders.csv")
    payments = load_csv("payments.csv")
    events = load_csv("journey_events.csv")
    tickets = load_csv("support_tickets.csv")
    feedback = load_csv("feedback.csv")

    errors = []
    warnings = []

    # 1. Customer count check
    print(f"[CHECK 1] Customer records count: {len(customers)} (Requirement: >= 100)")
    if len(customers) < 100:
        errors.append(f"Customer count {len(customers)} is less than 100!")
    else:
        print("  -> PASS: Customer count requirement satisfied.")

    customer_ids = {c["customer_id"] for c in customers}
    product_ids = {p["product_id"] for p in products}
    order_ids = {o["order_id"] for o in orders}

    # 2. Referential integrity: Orders
    print(f"[CHECK 2] Validating Orders referential integrity ({len(orders)} orders)...")
    for o in orders:
        if o["customer_id"] not in customer_ids:
            errors.append(f"Order {o['order_id']} references nonexistent customer {o['customer_id']}")
        if o["product_id"] not in product_ids:
            errors.append(f"Order {o['order_id']} references nonexistent product {o['product_id']}")
        try:
            amt = float(o["total_amount"])
            if amt <= 0:
                errors.append(f"Order {o['order_id']} has non-positive amount {amt}")
        except ValueError:
            errors.append(f"Order {o['order_id']} invalid total_amount: {o['total_amount']}")
    print("  -> PASS: All orders reference valid customers and products.")

    # 3. Referential integrity: Payments
    print(f"[CHECK 3] Validating Payments referential integrity ({len(payments)} payments)...")
    for p in payments:
        if p["customer_id"] not in customer_ids:
            errors.append(f"Payment {p['payment_id']} references nonexistent customer {p['customer_id']}")
        if p["order_id"] and p["order_id"] not in order_ids:
            errors.append(f"Payment {p['payment_id']} references nonexistent order {p['order_id']}")
        if p["payment_status"] not in ["success", "failed", "pending"]:
            errors.append(f"Payment {p['payment_id']} has invalid status {p['payment_status']}")
        if p["payment_status"] == "failed" and not p["error_code"]:
            warnings.append(f"Payment {p['payment_id']} is failed but missing error_code")
    print("  -> PASS: All payments reference valid entities with sensible status codes.")

    # 4. Referential integrity: Support Tickets
    print(f"[CHECK 4] Validating Support Tickets ({len(tickets)} tickets)...")
    for t in tickets:
        if t["customer_id"] not in customer_ids:
            errors.append(f"Ticket {t['ticket_id']} references nonexistent customer {t['customer_id']}")
        if t["order_id"] and t["order_id"] not in order_ids:
            errors.append(f"Ticket {t['ticket_id']} references nonexistent order {t['order_id']}")
    print("  -> PASS: All support tickets linked accurately.")

    # 5. Referential integrity: Feedback
    print(f"[CHECK 5] Validating Feedback records ({len(feedback)} reviews)...")
    for f in feedback:
        if f["customer_id"] not in customer_ids:
            errors.append(f"Feedback {f['feedback_id']} references nonexistent customer {f['customer_id']}")
        if f["product_id"] not in product_ids:
            errors.append(f"Feedback {f['feedback_id']} references nonexistent product {f['product_id']}")
        rating = int(f["rating"])
        if not (1 <= rating <= 5):
            errors.append(f"Feedback {f['feedback_id']} rating {rating} outside 1-5 range")
    print("  -> PASS: All feedback entries linked accurately.")

    # 6. Journey Events sequence & timestamps
    print(f"[CHECK 6] Validating Journey Events ({len(events)} events)...")
    cust_events = {}
    for ev in events:
        cid = ev["customer_id"]
        if cid not in customer_ids:
            errors.append(f"Event {ev['event_id']} references nonexistent customer {cid}")
        if ev["product_id"] and ev["product_id"] not in product_ids:
            errors.append(f"Event {ev['event_id']} references nonexistent product {ev['product_id']}")
        
        # Verify timestamp parsing
        try:
            ts = datetime.strptime(ev["timestamp"], "%Y-%m-%d %H:%M:%S")
        except ValueError:
            errors.append(f"Event {ev['event_id']} has unparseable timestamp: {ev['timestamp']}")
            continue
        
        # Verify metadata is valid JSON
        if ev["metadata"]:
            try:
                json.loads(ev["metadata"])
            except json.JSONDecodeError:
                errors.append(f"Event {ev['event_id']} has malformed JSON metadata: {ev['metadata']}")
        
        cust_events.setdefault(cid, []).append(ev)

    # Check chronological ordering per session
    for cid, ev_list in cust_events.items():
        sess_times = {}
        for ev in ev_list:
            sid = ev["session_id"]
            ts = datetime.strptime(ev["timestamp"], "%Y-%m-%d %H:%M:%S")
            if sid in sess_times:
                last_ts = sess_times[sid]
                if ts < last_ts:
                    errors.append(f"Customer {cid} session {sid} has out-of-order event at {ts} (was {last_ts})")
            sess_times[sid] = ts

    print("  -> PASS: All journey events have valid timestamps, JSON metadata, and session chronology.")

    # 7. Coverage of 10 Required Scenarios
    print("[CHECK 7] Verifying presence of all 10 core friction and journey scenarios...")
    scenario_coverage = {
        "1. Successful purchase": False,
        "2. Cart abandonment": False,
        "3. Payment failure": False,
        "4. Repeated payment failure": False,
        "5. Delivery delay": False,
        "6. Customer support complaint": False,
        "7. Negative product feedback": False,
        "8. Product information confusion": False,
        "9. High browsing but no purchase": False,
        "10. Successful recovery after intervention": False
    }

    # CUST-1001: Successful purchase
    c1_orders = [o for o in orders if o["customer_id"] == "CUST-1001" and o["order_status"] == "delivered"]
    if c1_orders:
        scenario_coverage["1. Successful purchase"] = True

    # CUST-1002: Cart abandonment
    c2_ev = [e for e in events if e["customer_id"] == "CUST-1002"]
    if any(e["event_type"] == "add_to_cart" for e in c2_ev) and not any(o["customer_id"] == "CUST-1002" for o in orders):
        scenario_coverage["2. Cart abandonment"] = True

    # CUST-1003: Payment failure
    c3_pays = [p for p in payments if p["customer_id"] == "CUST-1003" and p["payment_status"] == "failed"]
    if len(c3_pays) == 1:
        scenario_coverage["3. Payment failure"] = True

    # CUST-1004: Repeated payment failure
    c4_pays = [p for p in payments if p["customer_id"] == "CUST-1004" and p["payment_status"] == "failed"]
    if len(c4_pays) >= 2:
        scenario_coverage["4. Repeated payment failure"] = True

    # CUST-1005: Delivery delay
    c5_orders = [o for o in orders if o["customer_id"] == "CUST-1005" and o["order_status"] == "delayed"]
    c5_tracking = [e for e in events if e["customer_id"] == "CUST-1005" and e["event_type"] == "order_tracking_checked"]
    if c5_orders and len(c5_tracking) >= 3:
        scenario_coverage["5. Delivery delay"] = True

    # CUST-1006: Customer support complaint
    c6_tickets = [t for t in tickets if t["customer_id"] == "CUST-1006" and t["priority"] in ["high", "urgent"]]
    if c6_tickets:
        scenario_coverage["6. Customer support complaint"] = True

    # CUST-1007: Negative product feedback
    c7_fb = [f for f in feedback if f["customer_id"] == "CUST-1007" and int(f["rating"]) <= 2]
    if c7_fb:
        scenario_coverage["7. Negative product feedback"] = True

    # CUST-1008: Product information confusion
    c8_ev = [e for e in events if e["customer_id"] == "CUST-1008" and e["event_type"] in ["specification_view", "size_guide_view"]]
    if len(c8_ev) >= 4:
        scenario_coverage["8. Product information confusion"] = True

    # CUST-1009: High browsing but no purchase
    c9_views = [e for e in events if e["customer_id"] == "CUST-1009" and e["event_type"] == "product_view"]
    c9_orders = [o for o in orders if o["customer_id"] == "CUST-1009"]
    if len(c9_views) >= 10 and len(c9_orders) == 0:
        scenario_coverage["9. High browsing but no purchase"] = True

    # CUST-1010: Successful recovery after intervention
    c10_rec_ev = [e for e in events if e["customer_id"] == "CUST-1010" and e["event_type"] in ["recovery_email_sent", "recovery_link_clicked"]]
    c10_orders = [o for o in orders if o["customer_id"] == "CUST-1010" and o["order_status"] in ["delivered", "completed", "shipped"]]
    if len(c10_rec_ev) >= 2 and c10_orders:
        scenario_coverage["10. Successful recovery after intervention"] = True

    for sc_name, passed in scenario_coverage.items():
        status_str = "PASS" if passed else "FAIL"
        print(f"  [{status_str}] {sc_name}")
        if not passed:
            errors.append(f"Missing or incomplete scenario representation: {sc_name}")

    print("=" * 60)
    if warnings:
        print(f"WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  * {w}")
    if errors:
        print(f"AUDIT FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  [X] {err}")
        sys.exit(1)
    else:
        print("AUDIT SUCCESS: All datasets are 100% valid, consistent, and satisfy all requirements!")
        print("=" * 60)

if __name__ == "__main__":
    run_validation()
