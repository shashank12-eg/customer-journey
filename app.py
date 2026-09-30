"""
Interactive Web Dashboard & REST API Server for
AI Customer Journey Friction Detection & Recovery Assistant
College Project - Team Member 4

Runs with standard Python library (no external packages required).
Usage: python app.py
Open: http://localhost:8000 in your browser
"""

import http.server
import socketserver
import json
import os
import sys
import urllib.parse
import io
import unittest

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from src.friction_analyzer import CustomerJourneyAnalyzer

PORT = 8000
DATA_DIR = os.path.join(BASE_DIR, "data")
STATIC_DIR = os.path.join(BASE_DIR, "static")
SCENARIOS_DIR = os.path.join(BASE_DIR, "scenarios")

analyzer = CustomerJourneyAnalyzer(data_dir=DATA_DIR)

class DashboardRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler serving REST APIs and static UI assets."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # REST API Endpoints
        if path == "/api/summary":
            self._handle_summary()
        elif path == "/api/customers":
            self._handle_customers()
        elif path.startswith("/api/customer/") and path.endswith("/analyze"):
            # e.g., /api/customer/CUST-1004/analyze
            parts = path.strip("/").split("/")
            if len(parts) == 4:
                cust_id = parts[2]
                self._handle_analyze_customer(cust_id)
            else:
                self._send_error_json(400, "Invalid endpoint path")
        elif path.startswith("/api/customer/"):
            parts = path.strip("/").split("/")
            if len(parts) == 3:
                cust_id = parts[2]
                self._handle_get_customer(cust_id)
            else:
                self._send_error_json(400, "Invalid customer endpoint")
        elif path == "/api/scenarios":
            self._handle_scenarios()
        elif path == "/api/run-tests":
            self._handle_run_tests()
        else:
            # Fallback to serving static files
            if path == "/":
                self.path = "/index.html"
            super().do_GET()

    def _send_json(self, data, status=200):
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _send_error_json(self, status, message):
        self._send_json({"error": message, "status": status}, status=status)

    def _handle_summary(self):
        total_customers = len(analyzer.customers)
        total_products = len(analyzer.products)
        total_orders = sum(len(o) for o in analyzer.orders_by_customer.values())
        total_payments = sum(len(p) for p in analyzer.payments_by_customer.values())
        total_events = sum(len(e) for e in analyzer.events_by_customer.values())
        total_tickets = sum(len(t) for t in analyzer.tickets_by_customer.values())
        total_feedback = sum(len(f) for f in analyzer.feedback_by_customer.values())

        summary = {
            "total_customers": total_customers,
            "total_products": total_products,
            "total_orders": total_orders,
            "total_payments": total_payments,
            "total_journey_events": total_events,
            "total_support_tickets": total_tickets,
            "total_reviews": total_feedback,
            "benchmark_scenarios": 10
        }
        self._send_json(summary)

    def _handle_customers(self):
        customer_list = []
        for cid, cust in analyzer.customers.items():
            # Get brief friction pre-check
            analysis = analyzer.analyze_customer(cid)
            customer_list.append({
                "customer_id": cid,
                "name": cust.get("name"),
                "email": cust.get("email"),
                "segment": cust.get("segment"),
                "total_orders": cust.get("total_lifetime_orders"),
                "friction_detected": analysis["friction_detected"],
                "friction_category": analysis["friction_category"],
                "severity": analysis["severity"]
            })
        self._send_json(customer_list)

    def _handle_get_customer(self, cust_id):
        if cust_id not in analyzer.customers:
            self._send_error_json(404, f"Customer {cust_id} not found")
            return
        
        cust = analyzer.customers[cust_id]
        events = analyzer.events_by_customer.get(cust_id, [])
        orders = analyzer.orders_by_customer.get(cust_id, [])
        payments = analyzer.payments_by_customer.get(cust_id, [])
        tickets = analyzer.tickets_by_customer.get(cust_id, [])
        feedback = analyzer.feedback_by_customer.get(cust_id, [])

        payload = {
            "profile": cust,
            "events": events,
            "orders": orders,
            "payments": payments,
            "tickets": tickets,
            "feedback": feedback
        }
        self._send_json(payload)

    def _handle_analyze_customer(self, cust_id):
        if cust_id not in analyzer.customers:
            self._send_error_json(404, f"Customer {cust_id} not found")
            return
        analysis = analyzer.analyze_customer(cust_id)
        self._send_json(analysis)

    def _handle_scenarios(self):
        scenarios = []
        if os.path.exists(SCENARIOS_DIR):
            for fname in sorted(os.listdir(SCENARIOS_DIR)):
                if fname.endswith(".json"):
                    fpath = os.path.join(SCENARIOS_DIR, fname)
                    with open(fpath, mode="r", encoding="utf-8") as f:
                        scenarios.append(json.load(f))
        self._send_json(scenarios)

    def _handle_run_tests(self):
        """Execute automated unittest suite and capture results into JSON response."""
        from tests import test_scenarios
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_scenarios)
        
        stream = io.StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)

        response_data = {
            "tests_run": result.testsRun,
            "failures": len(result.failures),
            "errors": len(result.errors),
            "was_successful": result.wasSuccessful(),
            "output_log": stream.getvalue()
        }
        self._send_json(response_data)

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), DashboardRequestHandler) as httpd:
        print("=" * 65)
        print(f"  AI Friction Detection & Recovery Assistant Dashboard")
        print(f"  Running locally at: http://localhost:{PORT}")
        print("  Press Ctrl+C to terminate the server.")
        print("=" * 65)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server cleanly.")

if __name__ == "__main__":
    start_server()
