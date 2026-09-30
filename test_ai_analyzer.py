"""
Tests for ai_analyzer.py.   Run with:   python -m unittest -v      (or:  pytest -v)
No API key, server or extra package is needed.
"""
import os
import unittest

import ai_analyzer as a

os.environ.pop("ANTHROPIC_API_KEY", None)      # prove everything works WITHOUT an LLM


def ev(event_type, ts, **meta):
    """Tiny helper to build one event."""
    event = {"type": event_type, "ts": ts}
    if meta:
        event["meta"] = meta
    return event


def session(events, feedback="", sid="T1", cid="C1"):
    return {"session_id": sid, "customer_id": cid, "events": events, "feedback": feedback}


class TestScenarios(unittest.TestCase):
    """The 14 required scenarios."""

    def test_01_successful_purchase(self):
        r = a.analyze_session(session([ev("product_view", 0), ev("add_to_cart", 20), ev("checkout_start", 40),
                                       ev("payment_attempt", 60), ev("purchase", 70)]))
        self.assertEqual(r["status"], "CONVERTED")
        self.assertEqual(r["primary_cause"], "NONE")
        self.assertEqual(r["risk_level"], "LOW")
        self.assertEqual(r["features"]["purchase_completed"], 1)

    def test_02_single_payment_failure(self):
        r = a.analyze_session(session([ev("product_view", 0), ev("add_to_cart", 20), ev("checkout_start", 40),
                                       ev("payment_attempt", 60), ev("payment_failed", 65)]))
        self.assertEqual(r["primary_cause"], "PAYMENT_FAILURE")
        self.assertEqual(r["features"]["payment_failures"], 1)
        self.assertEqual(r["journey_stage"], "PAYMENT")
        self.assertIn("retry", r["recommendation"]["action"].lower())
        self.assertTrue(r["journey"]["ended_after_friction"])

    def test_03_repeated_payment_failures(self):
        r = a.analyze_session(session([ev("add_to_cart", 0), ev("checkout_start", 10),
                                       ev("payment_attempt", 20), ev("payment_failed", 25),
                                       ev("payment_attempt", 40), ev("payment_failed", 45),
                                       ev("payment_attempt", 60)]))
        self.assertEqual(r["features"]["payment_attempts"], 3)
        self.assertEqual(r["features"]["payment_failures"], 2)
        self.assertAlmostEqual(r["features"]["payment_failure_rate"], 0.667, places=3)
        self.assertEqual(r["primary_cause"], "PAYMENT_FAILURE")
        self.assertIn("alternate payment", r["recommendation"]["action"].lower())
        detail = [e for e in r["evidence_details"] if e["event_type"] == "payment_failed"][0]
        self.assertEqual(detail["count"], 2)
        self.assertEqual(detail["timestamps"], [25.0, 45.0])

    def test_04_delivery_uncertainty(self):
        r = a.analyze_session(session([ev("product_view", 0), ev("add_to_cart", 10),
                                       ev("delivery_check", 20, delivery_days=8), ev("delivery_check", 40, delivery_days=8),
                                       ev("delivery_check", 60, delivery_days=8)]))
        self.assertEqual(r["primary_cause"], "DELIVERY_UNCERTAINTY")
        self.assertEqual(r["features"]["delivery_checks"], 3)
        self.assertEqual(r["features"]["delivery_days"], 8)
        self.assertEqual(r["status"], "CART_ABANDONED")

    def test_05_price_shock(self):
        r = a.analyze_session(session([ev("product_view", 0), ev("add_to_cart", 10, price=999), ev("checkout_start", 30),
                                       ev("shipping_cost_shown", 40, shipping_cost=199), ev("coupon_failed", 60),
                                       ev("remove_from_cart", 80)]))
        self.assertEqual(r["primary_cause"], "PRICE_SHOCK")
        self.assertEqual(r["features"]["shipping_cost"], 199)
        self.assertEqual(r["features"]["coupon_failures"], 1)

    def test_06_product_information_problem(self):
        events = [ev("product_view", t) for t in (0, 20, 40, 60, 80)]
        events += [ev("size_chart_view", 30)] + [ev("review_read", t) for t in (50, 70, 90)]
        r = a.analyze_session(session(events, feedback="Not sure about the size, description unclear"))
        self.assertEqual(r["primary_cause"], "UNCLEAR_PRODUCT_INFO")
        self.assertEqual(r["features"]["product_views"], 5)
        self.assertEqual(r["features"]["review_reads"], 3)
        self.assertEqual(r["status"], "BROWSE_DROPOFF")

    def test_07_checkout_abandonment(self):
        r = a.analyze_session(session([ev("product_view", 0), ev("add_to_cart", 10), ev("checkout_start", 30),
                                       ev("form_error", 50), ev("form_error", 70)]))
        self.assertEqual(r["primary_cause"], "CHECKOUT_COMPLEXITY")
        self.assertEqual(r["journey_stage"], "CHECKOUT")
        self.assertEqual(r["features"]["form_errors"], 2)

    def test_08_post_purchase_support_issue(self):
        r = a.analyze_session(session([ev("purchase", 0), ev("order_delayed", 4000), ev("support_ticket", 4100)],
                                      feedback="Order not received, need refund"))
        self.assertEqual(r["primary_cause"], "POST_PURCHASE_ISSUE")
        self.assertEqual(r["status"], "PURCHASED_WITH_ISSUE")
        self.assertEqual(r["features"]["support_tickets"], 1)
        self.assertIn("priority support", r["recommendation"]["action"].lower())

    def test_09_empty_session(self):
        r = a.analyze_session(session([]))
        self.assertEqual(r["status"], "NO_ACTIVITY")
        self.assertEqual(r["primary_cause"], "NONE")
        self.assertEqual(r["risk_score"], 0)
        self.assertEqual(r["journey_stage"], "NO_ACTIVITY")
        self.assertEqual(a.analyze_session({"session_id": "X"})["status"], "NO_ACTIVITY")   # no 'events' key at all

    def test_10_missing_timestamps(self):
        r = a.analyze_session(session([ev("product_view", 0), {"type": "add_to_cart"}, ev("checkout_start", 30),
                                       {"type": "payment_attempt", "ts": None}, ev("payment_failed", 50)]))
        self.assertEqual(r["data_quality"]["missing_timestamps"], 2)
        self.assertEqual(r["data_quality"]["imputed_timestamps"], 2)
        self.assertEqual(r["primary_cause"], "PAYMENT_FAILURE")
        self.assertTrue(any("timestamps were missing" in f for f in r["confidence_factors"]))

    def test_11_missing_feedback(self):
        r = a.analyze_session({"session_id": "F", "customer_id": "C", "events": [ev("product_view", 0)]})
        self.assertEqual(r["data_quality"]["missing_feedback"], 1)
        self.assertEqual(r["cleaned_feedback"], "")
        self.assertEqual(r["feedback_analysis"]["sentiment"], "none")

    def test_12_duplicate_events(self):
        events = [ev("add_to_cart", 0), ev("checkout_start", 10),
                  ev("payment_failed", 30), ev("payment_failed", 30),                 # exact duplicate -> removed
                  ev("payment_attempt", 20), ev("payment_attempt", 50)]               # different times -> both kept
        clean = a.clean_session(session(events))
        types = [e["type"] for e in clean["events"]]
        self.assertEqual(clean["data_quality"]["duplicates_removed"], 1)
        self.assertEqual(types.count("payment_failed"), 1)
        self.assertEqual(types.count("payment_attempt"), 2)

    def test_13_multiple_simultaneous_causes(self):
        r = a.analyze_session(session([ev("product_view", 0), ev("add_to_cart", 10, price=500), ev("checkout_start", 20),
                                       ev("form_error", 30), ev("form_error", 40),
                                       ev("shipping_cost_shown", 50, shipping_cost=150), ev("coupon_failed", 60),
                                       ev("payment_attempt", 70), ev("payment_failed", 75)]))
        self.assertGreaterEqual(len(r["cause_scores"]), 3)
        self.assertTrue(r["secondary_causes"])
        self.assertEqual(len(r["secondary_cause_names"]), len(r["secondary_causes"]))
        self.assertNotIn(r["primary_cause"], r["secondary_cause_names"])
        self.assertIn("primary_cause_reason", r)

    def test_14_friction_but_still_purchases(self):
        r = a.analyze_session(session([ev("add_to_cart", 0), ev("checkout_start", 10), ev("payment_attempt", 20),
                                       ev("payment_failed", 25), ev("payment_attempt", 40), ev("purchase", 50)]))
        self.assertEqual(r["status"], "CONVERTED_AFTER_FRICTION")
        self.assertEqual(r["primary_cause"], "PAYMENT_FAILURE")
        self.assertEqual(r["risk_level"], "LOW")
        self.assertLessEqual(r["risk_score"], 30)
        self.assertEqual(r["recommendation"]["urgency"], "LOW")
        self.assertFalse(r["journey"]["ended_after_friction"])


class TestPreprocessing(unittest.TestCase):
    def test_timestamp_formats(self):
        self.assertEqual(a.parse_timestamp(5), 5.0)
        self.assertEqual(a.parse_timestamp("7.5"), 7.5)
        self.assertEqual(a.parse_timestamp(1_700_000_000_000), 1_700_000_000.0)      # milliseconds
        self.assertEqual(a.parse_timestamp("2026-09-30T10:00:10Z") - a.parse_timestamp("2026-09-30T10:00:00Z"), 10)
        self.assertIsNone(a.parse_timestamp("not a time"))
        self.assertIsNone(a.parse_timestamp(None))

    def test_timestamps_are_normalised_to_session_start(self):
        clean = a.clean_session(session([ev("product_view", 1000), ev("add_to_cart", 1040)]))
        self.assertEqual([e["ts"] for e in clean["events"]], [0.0, 40.0])

    def test_feedback_cleaning_keeps_original(self):
        clean = a.clean_session(session([], feedback="  DELIVERY is   TOO LATE!!!  \U0001F621 "))
        self.assertEqual(clean["cleaned_feedback"], "delivery is too late!")
        self.assertEqual(clean["raw_feedback"], "  DELIVERY is   TOO LATE!!!  \U0001F621 ")

    def test_missing_ids_and_invalid_events_are_reported(self):
        clean = a.clean_session({"events": [ev("product_view", 0), {"type": ""}, "junk", {"ts": 5}]})
        self.assertEqual(clean["customer_id"], "UNKNOWN_CUSTOMER")
        self.assertEqual(clean["session_id"], "UNKNOWN_SESSION")
        q = clean["data_quality"]
        self.assertEqual(q["invalid_events"], 3)
        self.assertEqual(q["total_events"], 4)
        self.assertEqual(q["clean_events"], 1)
        self.assertEqual(q["missing_customer_ids"], 1)

    def test_bad_input_raises_clear_error(self):
        with self.assertRaises(ValueError):
            a.analyze_session("not a dict")
        with self.assertRaises(ValueError):
            a.analyze_session({"events": "oops"})

    def test_dataset_quality_report_and_errors(self):
        clean, quality, errors = a.preprocess_dataset([session([ev("product_view", 0)]), 42, session([ev("search", 0)], sid="T2")])
        self.assertEqual(len(clean), 2)
        self.assertEqual(len(errors), 1)
        self.assertEqual(quality["unusable_sessions"], 1)
        self.assertEqual(quality["total_events"], 2)


class TestFeedbackAndFeatures(unittest.TestCase):
    def test_structured_feedback_analysis(self):
        fb = a.analyze_feedback(a.clean_feedback_text("My card payment failed twice, money deducted"))
        self.assertEqual(fb["sentiment"], "negative")
        self.assertEqual(fb["severity"], "high")
        self.assertIn("payment", fb["themes"])
        self.assertIn("money deducted", fb["keywords"])
        self.assertEqual(fb["method"], "rules")

    def test_whole_word_matching(self):
        self.assertEqual(a.classify_feedback("I love this chocolate"), {})          # 'late' inside 'chocolate'
        self.assertIn("DELIVERY_UNCERTAINTY", a.classify_feedback("delivery was late"))

    def test_positive_feedback_does_not_boost_a_cause(self):
        r = a.analyze_session(session([ev("product_view", 0)], feedback="Great delivery, very fast, thanks"))
        self.assertEqual(r["feedback_analysis"]["sentiment"], "positive")
        self.assertNotIn("DELIVERY_UNCERTAINTY", r["cause_scores"])

    def test_no_division_by_zero(self):
        f = a.engineer_features(a.clean_session(session([ev("product_view", 0)])))
        self.assertEqual(f["payment_failure_rate"], 0.0)
        self.assertEqual(f["cart_removal_rate"], 0.0)

    def test_time_features(self):
        events = [ev("product_view", 0), ev("add_to_cart", 40), ev("checkout_start", 90), ev("payment_attempt", 120),
                  ev("payment_failed", 125), ev("session_exit", 185)]
        f = a.engineer_features(a.clean_session(session(events)))
        self.assertEqual(f["time_view_to_cart"], 40)
        self.assertEqual(f["time_cart_to_checkout"], 50)
        self.assertEqual(f["time_checkout_to_payment"], 30)
        self.assertEqual(f["time_attempt_to_failure"], 5)
        self.assertEqual(f["time_friction_to_exit"], 60)
        self.assertEqual(f["session_duration"], 185)

    def test_features_are_numeric_or_none(self):
        f = a.engineer_features(a.clean_session(a.DEMO[0]))
        for name, value in f.items():
            self.assertTrue(value is None or isinstance(value, (int, float)), name)


class TestJourneyAndExplainability(unittest.TestCase):
    def test_journey_timeline_and_last_stage(self):
        r = a.analyze_session(a.DEMO[0])
        stages = [s["stage"] for s in r["journey"]["timeline"]]
        self.assertEqual(stages, ["PRODUCT_EVALUATION", "CART", "CHECKOUT", "PAYMENT"])
        self.assertEqual(r["journey"]["last_friction_event"]["type"], "payment_failed")
        self.assertEqual(r["journey_stage"], "PAYMENT")

    def test_support_is_not_the_meaningful_last_stage(self):
        r = a.analyze_session(session([ev("add_to_cart", 0), ev("support_chat", 20)]))
        self.assertEqual(r["journey"]["last_stage"], "SUPPORT")
        self.assertEqual(r["journey_stage"], "CART")

    def test_money_deducted_changes_recommendation(self):
        r = a.analyze_session(a.DEMO[0])
        self.assertIn("verification", r["recommendation"]["action"].lower())
        self.assertEqual(r["recommendation"]["urgency"], "HIGH")

    def test_confidence_and_risk_are_explained(self):
        r = a.analyze_session(a.DEMO[0])
        self.assertTrue(r["confidence_factors"])
        self.assertTrue(r["risk_factors"])
        self.assertIn(r["confidence_level"], ("LOW", "MEDIUM", "HIGH"))
        self.assertIn(r["risk_level"], ("LOW", "MEDIUM", "HIGH"))
        self.assertEqual(min(100, sum(p["points"] for p in r["risk_breakdown"])), r["risk_score"])
        self.assertIn("NOT a statistically validated probability", r["confidence_note"])
        self.assertIn("NOT a probability", r["risk_note"])

    def test_tie_break_uses_last_friction_event(self):
        journey = {"cause_of_last_friction": "CHECKOUT_COMPLEXITY", "ended_after_friction": True}
        primary, secondary, reason = a.select_causes({"PAYMENT_FAILURE": 0.60, "CHECKOUT_COMPLEXITY": 0.55}, journey, False)
        self.assertEqual(primary, "CHECKOUT_COMPLEXITY")
        self.assertEqual(secondary, ["PAYMENT_FAILURE"])
        self.assertIn("last friction event", reason)

    def test_recommendation_has_required_fields(self):
        for s in a.DEMO:
            rec = a.analyze_session(s)["recommendation"]
            for key in ("action", "reason", "channel", "owner", "urgency"):
                self.assertIn(key, rec)

    def test_playbook_is_not_mutated(self):
        before = a.PLAYBOOK["PAYMENT_FAILURE"]["action"]
        a.analyze_session(a.DEMO[0])
        self.assertEqual(a.PLAYBOOK["PAYMENT_FAILURE"]["action"], before)

    def test_works_without_api_key(self):
        self.assertIsNone(a.analyze_feedback_llm("payment failed"))
        r = a.analyze_session(a.DEMO[0], use_llm=True)            # falls back to rules
        self.assertEqual(r["feedback_analysis"]["method"], "rules")
        self.assertEqual(a.llm_explain(r), r["explanation"])


class TestBatchAndDemo(unittest.TestCase):
    def test_original_demo_still_gives_the_same_primary_causes(self):
        out = a.analyze_all(a.DEMO)
        got = {r["session_id"]: r["primary_cause"] for r in out["results"]}
        self.assertEqual(got["S1"], "PAYMENT_FAILURE")
        self.assertEqual(got["S2"], "PRICE_SHOCK")
        self.assertEqual(got["S3"], "UNCLEAR_PRODUCT_INFO")
        self.assertEqual(got["S4"], "DELIVERY_UNCERTAINTY")
        self.assertEqual(got["S5"], "POST_PURCHASE_ISSUE")
        self.assertEqual(got["S6"], "NONE")

    def test_v1_response_keys_still_present(self):
        r = a.analyze_session(a.DEMO[0])
        for key in ("session_id", "customer_id", "status", "risk_score", "risk_level", "primary_cause",
                    "cause_label", "confidence", "evidence", "secondary_causes", "recommendation", "explanation"):
            self.assertIn(key, r)
        self.assertIsInstance(r["evidence"][0], str)
        out = a.analyze_all(a.DEMO)
        for key in ("total_sessions", "abandoned", "high_risk", "cause_distribution", "avg_confidence"):
            self.assertIn(key, out["summary"])

    def test_dataset_summary_is_computed_from_data(self):
        out = a.analyze_all(a.DEMO)
        s = out["summary"]
        self.assertEqual(s["total_sessions"], len(a.DEMO))
        self.assertAlmostEqual(sum(s["cause_distribution_pct"].values()), 100.0, delta=0.5)
        self.assertEqual(sum(s["cause_distribution"].values()), sum(r["primary_cause"] != "NONE" for r in out["results"]))
        self.assertEqual(out["data_quality"]["duplicates_removed"], 1)                  # S7 has one duplicate
        self.assertEqual(out["data_quality"]["missing_customer_ids"], 1)                # S7 has no customer id

    def test_batch_reports_bad_sessions_instead_of_crashing(self):
        out = a.analyze_all([a.DEMO[0], "bad", None])
        self.assertEqual(len(out["results"]), 1)
        self.assertEqual(len(out["errors"]), 2)

    def test_empty_batch(self):
        out = a.analyze_all([])
        self.assertEqual(out["summary"]["total_sessions"], 0)
        self.assertIsNone(out["summary"]["most_common_cause"])


class TestOutcomeLoopAndApiHandlers(unittest.TestCase):
    def setUp(self):
        a.OUTCOME_LOG.clear()

    def test_outcome_loop(self):
        a.analyze_session(a.DEMO[0])
        a.record_outcome("S1", "recovered")
        a.record_outcome("S1", "not_recovered", primary_cause="PAYMENT_FAILURE")
        summary = a.outcome_summary()
        self.assertEqual(summary["by_cause"]["PAYMENT_FAILURE"]["total"], 2)
        self.assertEqual(summary["by_cause"]["PAYMENT_FAILURE"]["recovery_rate_pct"], 50.0)
        with self.assertRaises(ValueError):
            a.record_outcome("S1", "maybe")

    def test_api_handlers(self):
        self.assertIn("data_quality", a.handle_preprocess([a.DEMO[0]]))
        self.assertEqual(a.handle_outcome({"session_id": "S9", "outcome": "no_response"})["outcome"], "no_response")


if __name__ == "__main__":
    unittest.main(verbosity=2)
