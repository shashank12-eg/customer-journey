"""
Automated Scenario Testing Suite for
AI-Powered Customer Journey Friction Detection and Recovery Assistant
College Project - Team Member 4

This test suite evaluates whether the AI friction analyzer produces reasonable,
accurate, and logically consistent outputs across all benchmark customer journeys.

Checked dimensions:
1. Friction Detection (boolean flag)
2. Friction Category (taxonomy alignment)
3. Empirical Evidence (telemetry audit trail)
4. Confidence Score (statistical certainty >= threshold)
5. Severity Classification (NONE, LOW, MEDIUM, HIGH, CRITICAL)
6. Recommended Recovery Action (actionable intervention strategy)
7. Dataset Referential Integrity & Chronological Consistency
"""

import json
import os
import sys
import unittest
import csv
from datetime import datetime

# Add project root to sys.path to enable direct running
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src.friction_analyzer import CustomerJourneyAnalyzer

class TestCustomerScenarios(unittest.TestCase):
    """
    Test suite verifying AI Friction Analyzer performance against benchmark scenarios.
    """

    @classmethod
    def setUpClass(cls):
        """Set up test environment and load expected results."""
        cls.data_dir = os.path.join(PROJECT_ROOT, "data")
        cls.scenarios_dir = os.path.join(PROJECT_ROOT, "scenarios")
        cls.expected_results_file = os.path.join(PROJECT_ROOT, "tests", "expected_results.json")

        # Instantiate analyzer pointing to synthetic dataset
        cls.analyzer = CustomerJourneyAnalyzer(data_dir=cls.data_dir)

        # Load expected results
        with open(cls.expected_results_file, mode="r", encoding="utf-8") as f:
            cls.expected_results = json.load(f)

    # -------------------------------------------------------------
    # 1. Dataset Integrity Tests
    # -------------------------------------------------------------
    def test_01_dataset_minimum_customer_count(self):
        """Verify that the dataset meets the college requirement of >= 100 customers."""
        customer_count = len(self.analyzer.customers)
        self.assertGreaterEqual(
            customer_count, 100,
            f"Dataset contains {customer_count} customers, but at least 100 are required."
        )

    def test_02_dataset_referential_integrity(self):
        """Verify that all referenced customer IDs and product IDs exist."""
        valid_cust_ids = set(self.analyzer.customers.keys())
        valid_prod_ids = set(self.analyzer.products.keys())

        # Check orders
        for cid, orders in self.analyzer.orders_by_customer.items():
            self.assertIn(cid, valid_cust_ids, f"Order references invalid customer: {cid}")
            for o in orders:
                self.assertIn(o["product_id"], valid_prod_ids, f"Order {o['order_id']} references invalid product {o['product_id']}")

        # Check payments
        for cid, payments in self.analyzer.payments_by_customer.items():
            self.assertIn(cid, valid_cust_ids, f"Payment references invalid customer: {cid}")

        # Check events
        for cid, events in self.analyzer.events_by_customer.items():
            self.assertIn(cid, valid_cust_ids, f"Event references invalid customer: {cid}")
            for ev in events:
                if ev.get("product_id"):
                    self.assertIn(ev["product_id"], valid_prod_ids, f"Event references invalid product: {ev['product_id']}")

    def test_03_journey_events_chronological_ordering(self):
        """Verify that journey events for each customer session have chronological timestamps."""
        for cid, events in self.analyzer.events_by_customer.items():
            session_times = {}
            for ev in events:
                sid = ev["session_id"]
                t = datetime.strptime(ev["timestamp"], "%Y-%m-%d %H:%M:%S")
                if sid in session_times:
                    prev_t = session_times[sid]
                    self.assertGreaterEqual(
                        t, prev_t,
                        f"Non-chronological event timestamp for customer {cid} in session {sid}: {t} < {prev_t}"
                    )
                session_times[sid] = t

    # -------------------------------------------------------------
    # 2. Individual Scenario Friction & Recovery Tests
    # -------------------------------------------------------------
    def _run_scenario_evaluation(self, scenario_key: str):
        """Helper method to validate analyzer output against expected results."""
        exp = self.expected_results[scenario_key]
        cust_id = exp["customer_id"]

        # Run AI analyzer
        analysis = self.analyzer.analyze_customer(cust_id)

        # 1. Check Friction Detection flag
        self.assertEqual(
            analysis["friction_detected"], exp["expected_friction_detected"],
            f"[{scenario_key}] Friction detection mismatch: got {analysis['friction_detected']}, expected {exp['expected_friction_detected']}"
        )

        # 2. Check Friction Category
        self.assertEqual(
            analysis["friction_category"], exp["expected_friction_category"],
            f"[{scenario_key}] Category mismatch: got '{analysis['friction_category']}', expected '{exp['expected_friction_category']}'"
        )

        # 3. Check Severity
        self.assertEqual(
            analysis["severity"], exp["expected_severity"],
            f"[{scenario_key}] Severity mismatch: got '{analysis['severity']}', expected '{exp['expected_severity']}'"
        )

        # 4. Check Confidence Threshold
        self.assertGreaterEqual(
            analysis["confidence"], exp["min_confidence"],
            f"[{scenario_key}] Confidence {analysis['confidence']} is below threshold {exp['min_confidence']}"
        )

        # 5. Check Evidence Keywords
        evidence_text = analysis.get("evidence", "").lower()
        self.assertTrue(len(evidence_text) > 0, f"[{scenario_key}] Evidence is empty")
        for kw in exp.get("evidence_keywords", []):
            self.assertIn(
                kw.lower(), evidence_text,
                f"[{scenario_key}] Expected keyword '{kw}' missing from evidence: '{analysis['evidence']}'"
            )

        # 6. Check Recommended Recovery Action Keywords
        rec_text = analysis.get("recommended_recovery_action", "").lower()
        self.assertTrue(len(rec_text) > 0, f"[{scenario_key}] Recommended action is empty")
        for kw in exp.get("recovery_keywords", []):
            self.assertIn(
                kw.lower(), rec_text,
                f"[{scenario_key}] Expected keyword '{kw}' missing from recovery action: '{analysis['recommended_recovery_action']}'"
            )

    def test_scenario_01_successful_purchase(self):
        """Test Scenario 1: Successful purchase with zero friction."""
        self._run_scenario_evaluation("scenario_01_successful_purchase")

    def test_scenario_02_cart_abandonment(self):
        """Test Scenario 2: Cart abandonment at shipping fee reveal."""
        self._run_scenario_evaluation("scenario_02_cart_abandonment")

    def test_scenario_03_payment_failure(self):
        """Test Scenario 3: Single payment gateway timeout failure."""
        self._run_scenario_evaluation("scenario_03_payment_failure")

    def test_scenario_04_repeated_payment_failure(self):
        """Test Scenario 4: Critical repeated payment failure streak."""
        self._run_scenario_evaluation("scenario_04_repeated_payment_failure")

    def test_scenario_05_delivery_delay(self):
        """Test Scenario 5: Carrier logistics delivery delay and tracking spikes."""
        self._run_scenario_evaluation("scenario_05_delivery_delay")

    def test_scenario_06_support_complaint(self):
        """Test Scenario 6: Customer support SLA breach and wrong product complaint."""
        self._run_scenario_evaluation("scenario_06_support_complaint")

    def test_scenario_07_negative_feedback(self):
        """Test Scenario 7: Negative 1-star product review and hardware defect."""
        self._run_scenario_evaluation("scenario_07_negative_feedback")

    def test_scenario_08_product_confusion(self):
        """Test Scenario 8: Product spec/sizing confusion with high hesitation."""
        self._run_scenario_evaluation("scenario_08_product_confusion")

    def test_scenario_09_high_browsing_no_purchase(self):
        """Test Scenario 9: High browsing volume without cart addition (choice overload)."""
        self._run_scenario_evaluation("scenario_09_high_browsing_no_purchase")

    def test_scenario_10_successful_recovery(self):
        """Test Scenario 10: Successful recovery conversion following omnichannel intervention."""
        self._run_scenario_evaluation("scenario_10_successful_recovery")

if __name__ == "__main__":
    unittest.main(verbosity=2)
