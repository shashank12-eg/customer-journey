"""
AI Customer Journey Friction Detection and Recovery Engine
Module: src.friction_analyzer
Author: Member 4 (Testing, Dataset & AI Validation Lead)

This module provides explainable, rule-and-heuristic-driven AI reasoning
to analyze e-commerce customer journeys, detect behavioral friction points,
measure severity and confidence, and recommend automated recovery actions.
"""

import csv
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional

class CustomerJourneyAnalyzer:
    """
    Intelligent analyzer that inspects customer telemetry events, orders,
    payments, support tickets, and reviews to diagnose friction in real-time.
    """

    def __init__(self, data_dir: Optional[str] = None):
        """
        Initialize analyzer and load reference datasets if directory is provided.
        """
        if data_dir is None:
            # Default to ../data or ./data
            base_dir = os.path.dirname(os.path.dirname(__file__))
            data_dir = os.path.join(base_dir, "data")
        
        self.data_dir = data_dir
        self.customers: Dict[str, Dict[str, Any]] = {}
        self.products: Dict[str, Dict[str, Any]] = {}
        self.orders_by_customer: Dict[str, List[Dict[str, Any]]] = {}
        self.payments_by_customer: Dict[str, List[Dict[str, Any]]] = {}
        self.tickets_by_customer: Dict[str, List[Dict[str, Any]]] = {}
        self.feedback_by_customer: Dict[str, List[Dict[str, Any]]] = {}
        self.events_by_customer: Dict[str, List[Dict[str, Any]]] = {}

        if os.path.exists(self.data_dir):
            self._load_datasets()

    def _load_datasets(self):
        """Load all CSV datasets into memory for fast relational querying."""
        # 1. Customers
        c_path = os.path.join(self.data_dir, "customers.csv")
        if os.path.exists(c_path):
            with open(c_path, mode="r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    self.customers[r["customer_id"]] = r

        # 2. Products
        p_path = os.path.join(self.data_dir, "products.csv")
        if os.path.exists(p_path):
            with open(p_path, mode="r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    self.products[r["product_id"]] = r

        # 3. Orders
        o_path = os.path.join(self.data_dir, "orders.csv")
        if os.path.exists(o_path):
            with open(o_path, mode="r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    self.orders_by_customer.setdefault(r["customer_id"], []).append(r)

        # 4. Payments
        pay_path = os.path.join(self.data_dir, "payments.csv")
        if os.path.exists(pay_path):
            with open(pay_path, mode="r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    self.payments_by_customer.setdefault(r["customer_id"], []).append(r)

        # 5. Support Tickets
        t_path = os.path.join(self.data_dir, "support_tickets.csv")
        if os.path.exists(t_path):
            with open(t_path, mode="r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    self.tickets_by_customer.setdefault(r["customer_id"], []).append(r)

        # 6. Feedback
        f_path = os.path.join(self.data_dir, "feedback.csv")
        if os.path.exists(f_path):
            with open(f_path, mode="r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    self.feedback_by_customer.setdefault(r["customer_id"], []).append(r)

        # 7. Journey Events
        e_path = os.path.join(self.data_dir, "journey_events.csv")
        if os.path.exists(e_path):
            with open(e_path, mode="r", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    self.events_by_customer.setdefault(r["customer_id"], []).append(r)

    def analyze_customer(self, customer_id: str, custom_events: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Perform comprehensive multi-signal friction analysis for a customer.
        Accepts optional custom_events to support scenario testing on isolated events.
        """
        customer = self.customers.get(customer_id, {"customer_id": customer_id, "name": "Unknown", "segment": "Standard"})
        events = custom_events if custom_events is not None else self.events_by_customer.get(customer_id, [])
        orders = self.orders_by_customer.get(customer_id, [])
        payments = self.payments_by_customer.get(customer_id, [])
        tickets = self.tickets_by_customer.get(customer_id, [])
        feedbacks = self.feedback_by_customer.get(customer_id, [])

        return self._evaluate_signals(
            customer=customer,
            events=events,
            orders=orders,
            payments=payments,
            tickets=tickets,
            feedbacks=feedbacks
        )

    def _evaluate_signals(
        self,
        customer: Dict[str, Any],
        events: List[Dict[str, Any]],
        orders: List[Dict[str, Any]],
        payments: List[Dict[str, Any]],
        tickets: List[Dict[str, Any]],
        feedbacks: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Core reasoning pipeline: applies behavioral heuristics, pattern recognition,
        and telemetry analysis to classify journey friction.
        """
        cid = customer.get("customer_id", "UNKNOWN")
        name = customer.get("name", "Valued Shopper")

        # -------------------------------------------------------------
        # 1. Check for Successful Recovery after Intervention
        # -------------------------------------------------------------
        recovery_sent = any(e.get("event_type") in ["recovery_email_sent", "recovery_sms_sent"] for e in events)
        recovery_clicked = any(e.get("event_type") == "recovery_link_clicked" for e in events)
        successful_order = any(o.get("order_status") in ["delivered", "completed", "shipped", "processing"] for o in orders)

        if recovery_sent and recovery_clicked and successful_order:
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Recovered Friction",
                "severity": "LOW",
                "confidence": 0.95,
                "root_cause": "Prior cart abandonment resolved by automated discount recovery incentive.",
                "evidence": f"Customer previously experienced checkout hesitation. Automated recovery campaign was dispatched and clicked, leading to completed order {orders[-1]['order_id']}.",
                "recommended_recovery_action": "Log recovery conversion metric, suppress further cart abandonment reminders, and send order delivery onboarding guide.",
                "action_type": "SUPPRESS_AND_REWARD"
            }

        # -------------------------------------------------------------
        # 2. Check for Repeated Payment Failure (CRITICAL)
        # -------------------------------------------------------------
        failed_payments = [p for p in payments if p.get("payment_status") == "failed"]
        failed_event_attempts = [e for e in events if e.get("event_type") == "payment_failed"]
        failure_count = max(len(failed_payments), len(failed_event_attempts))

        if failure_count >= 2:
            error_codes = list({p.get("error_code") for p in failed_payments if p.get("error_code")})
            codes_str = ", ".join(error_codes) if error_codes else "MULTIPLE_FAILURES"
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Repeated Payment Failure",
                "severity": "CRITICAL",
                "confidence": 0.98,
                "root_cause": f"Card limit or bank authorization decline across multiple attempts ({codes_str}).",
                "evidence": f"Observed {failure_count} consecutive payment failure attempts. Error codes: {codes_str}. Customer dropped off at final checkout stage.",
                "recommended_recovery_action": "Trigger priority WhatsApp notification offering alternate payment methods (UPI/NetBanking) with an automated 5% courtesy retry discount.",
                "action_type": "ALTERNATIVE_PAYMENT_PROMO"
            }

        # -------------------------------------------------------------
        # 3. Check for Single Payment Failure (HIGH)
        # -------------------------------------------------------------
        if failure_count == 1:
            err = failed_payments[0].get("error_code") if failed_payments else "GATEWAY_TIMEOUT"
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Payment Failure",
                "severity": "HIGH",
                "confidence": 0.92,
                "root_cause": f"Payment gateway interruption or bank processing error ({err}).",
                "evidence": f"Payment attempt failed with code {err}. Cart contents remain unpaid.",
                "recommended_recovery_action": "Send 1-click retry payment link via SMS and email with multiple payment options (Cards, UPI, PayPal).",
                "action_type": "RETRY_PAYMENT_LINK"
            }

        # -------------------------------------------------------------
        # 4. Check for Customer Support Complaint (CRITICAL)
        # -------------------------------------------------------------
        urgent_tickets = [t for t in tickets if t.get("priority") in ["urgent", "high"] and t.get("status") in ["open", "pending"]]
        if urgent_tickets:
            t = urgent_tickets[0]
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Customer Support Complaint",
                "severity": "CRITICAL",
                "confidence": 0.96,
                "root_cause": f"Unresolved customer issue ({t.get('category')}) exceeding support SLA: '{t.get('subject')}'.",
                "evidence": f"Urgent support ticket {t.get('ticket_id')} has been open without first agent response. Subject: {t.get('subject')}.",
                "recommended_recovery_action": "Escalate ticket immediately to Tier-2 senior supervisor, dispatch priority doorstep exchange/return pickup, and issue sincere apology.",
                "action_type": "SUPPORT_ESCALATION"
            }

        # -------------------------------------------------------------
        # 5. Check for Logistics Delivery Delay (HIGH)
        # -------------------------------------------------------------
        delayed_orders = [o for o in orders if o.get("order_status") == "delayed"]
        tracking_events = [e for e in events if e.get("event_type") == "order_tracking_checked"]
        if delayed_orders or len(tracking_events) >= 3:
            delayed_ord = delayed_orders[0] if delayed_orders else orders[0] if orders else {"order_id": "ORD-UNKNOWN"}
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Delivery Delay",
                "severity": "HIGH",
                "confidence": 0.91,
                "root_cause": "Carrier transit bottleneck causing order delivery SLA delay.",
                "evidence": f"Order {delayed_ord.get('order_id')} is delayed past estimated arrival. Customer repeatedly checked tracking {len(tracking_events)} times.",
                "recommended_recovery_action": "Proactive apology message with real-time GPS tracking update, prioritized carrier expedite request, and a $15 store credit voucher.",
                "action_type": "LOGISTICS_APOLOGY_CREDIT"
            }

        # -------------------------------------------------------------
        # 6. Check for Negative Product Feedback (HIGH)
        # -------------------------------------------------------------
        bad_feedback = [f for f in feedbacks if int(f.get("rating", 5)) <= 2 or f.get("sentiment") == "negative"]
        if bad_feedback:
            fb = bad_feedback[0]
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Negative Product Feedback",
                "severity": "HIGH",
                "confidence": 0.94,
                "root_cause": f"Product defect or dissatisfaction: '{fb.get('review_title')}'.",
                "evidence": f"Customer posted a {fb.get('rating')}-star negative review on product {fb.get('product_id')}: '{fb.get('review_text')}'",
                "recommended_recovery_action": "Trigger proactive warranty resolution outreach offering hassle-free product replacement or instant 100% refund.",
                "action_type": "WARRANTY_OUTREACH"
            }

        # -------------------------------------------------------------
        # 7. Check for Product Information Confusion (MEDIUM)
        # -------------------------------------------------------------
        spec_events = [e for e in events if e.get("event_type") in ["specification_view", "size_guide_view", "product_comparison"]]
        total_dwell = sum(int(e.get("dwell_time_seconds", 0)) for e in events)
        cart_events = [e for e in events if e.get("event_type") == "add_to_cart"]

        if len(spec_events) >= 4 and len(cart_events) == 0:
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Product Information Confusion",
                "severity": "MEDIUM",
                "confidence": 0.89,
                "root_cause": "Unclear technical specifications, sizing ambiguity, or compatibility uncertainty.",
                "evidence": f"Customer alternated {len(spec_events)} times between specifications and sizing guides with high dwell time ({total_dwell}s) without adding to cart.",
                "recommended_recovery_action": "Trigger contextual AI Shopping Assistant popup with interactive sizing quiz, spec summary comparison, and live chat assistance.",
                "action_type": "INTERACTIVE_AI_GUIDE"
            }

        # -------------------------------------------------------------
        # 8. Check for Cart Abandonment (MEDIUM)
        # -------------------------------------------------------------
        has_cart = len(cart_events) > 0
        has_purchase = any(e.get("event_type") in ["payment_success", "order_placed"] for e in events) or len(orders) > 0

        if has_cart and not has_purchase:
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "Cart Abandonment",
                "severity": "MEDIUM",
                "confidence": 0.88,
                "root_cause": "Unexpected shipping fees, checkout hesitation, or payment friction.",
                "evidence": "Customer added products to cart and initiated checkout but abandoned session prior to payment clearance.",
                "recommended_recovery_action": "Automated recovery email dispatched within 30 minutes offering free shipping coupon (FREESHIP24) or 10% cart completion discount.",
                "action_type": "ABANDONED_CART_DISCOUNT"
            }

        # -------------------------------------------------------------
        # 9. Check for High Browsing But No Purchase (MEDIUM)
        # -------------------------------------------------------------
        product_views = [e for e in events if e.get("event_type") == "product_view"]
        if len(product_views) >= 8 and not has_cart and not has_purchase:
            return {
                "customer_id": cid,
                "customer_name": name,
                "friction_detected": True,
                "friction_category": "High Browsing But No Purchase",
                "severity": "MEDIUM",
                "confidence": 0.86,
                "root_cause": "Choice overload, price comparison hesitation, or lack of tailored recommendations.",
                "evidence": f"Customer browsed {len(product_views)} different products across sessions without adding any items to cart.",
                "recommended_recovery_action": "Deliver personalized email with curated comparison table of top 3 reviewed products in browsed category + 10% welcome coupon.",
                "action_type": "CURATED_CATALOG_EMAIL"
            }

        # -------------------------------------------------------------
        # 10. Default: Smooth / Successful Journey (NONE)
        # -------------------------------------------------------------
        return {
            "customer_id": cid,
            "customer_name": name,
            "friction_detected": False,
            "friction_category": "None",
            "severity": "NONE",
            "confidence": 0.95,
            "root_cause": "Frictionless checkout experience with optimal progression and fulfillment.",
            "evidence": "Customer completed journey from browse to order confirmation without errors, delays, or excessive hesitation.",
            "recommended_recovery_action": "No corrective intervention required. Dispatch post-delivery VIP loyalty care points.",
            "action_type": "NO_ACTION_LOYALTY"
        }
