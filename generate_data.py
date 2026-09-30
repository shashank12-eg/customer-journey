"""
Synthetic E-Commerce Dataset Generator for
AI-Powered Customer Journey Friction Detection and Recovery Assistant
College Project - Team Member 4
"""

import csv
import json
import os
import random
from datetime import datetime, timedelta

# Ensure reproducibility
random.seed(42)

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. PRODUCTS DATASET
# -------------------------------------------------------------
PRODUCTS = [
    {"product_id": "PROD-001", "product_name": "Ultra-Slim Wireless Mechanical Keyboard", "category": "Electronics", "price": 89.99, "stock_quantity": 150, "description": "Low profile mechanical keyboard with Bluetooth 5.0 and RGB backlight.", "avg_rating": 4.6},
    {"product_id": "PROD-002", "product_name": "Noise Cancelling Over-Ear Headphones", "category": "Electronics", "price": 199.99, "stock_quantity": 85, "description": "Active noise cancelling wireless headphones with 40h battery life.", "avg_rating": 4.4},
    {"product_id": "PROD-003", "product_name": "Ergonomic Mesh Office Chair", "category": "Furniture", "price": 249.50, "stock_quantity": 40, "description": "Breathable mesh executive desk chair with adjustable lumbar support.", "avg_rating": 4.7},
    {"product_id": "PROD-004", "product_name": "Smart Fitness Tracker Band 6", "category": "Wearables", "price": 49.99, "stock_quantity": 210, "description": "Waterproof fitness band with heart rate, SpO2, and sleep tracker.", "avg_rating": 3.8},
    {"product_id": "PROD-005", "product_name": "Water-Resistant Commuter Backpack 25L", "category": "Bags & Luggage", "price": 64.99, "stock_quantity": 120, "description": "Durable nylon laptop backpack with USB charging port and anti-theft pocket.", "avg_rating": 4.5},
    {"product_id": "PROD-006", "product_name": "Stainless Steel Thermal Travel Mug 500ml", "category": "Home & Kitchen", "price": 24.99, "stock_quantity": 300, "description": "Double-wall vacuum insulated coffee tumbler keeping drinks hot for 8 hours.", "avg_rating": 4.8},
    {"product_id": "PROD-007", "product_name": "Pro GPS Multisport Smartwatch", "category": "Wearables", "price": 299.99, "stock_quantity": 65, "description": "Rugged GPS watch with topographic maps, sapphire crystal, and offline music.", "avg_rating": 4.3},
    {"product_id": "PROD-008", "product_name": "Fast Wireless Charging Stand 15W", "category": "Electronics", "price": 34.99, "stock_quantity": 180, "description": "Qi-certified fast charging dock compatible with iPhone and Android.", "avg_rating": 4.2},
    {"product_id": "PROD-009", "product_name": "4K Ultra-HD Webcam with Dual Mic", "category": "Electronics", "price": 79.99, "stock_quantity": 90, "description": "Auto-focus streaming webcam with built-in noise cancelling microphones.", "avg_rating": 4.1},
    {"product_id": "PROD-010", "product_name": "Merino Wool Breathable Running Tee", "category": "Apparel", "price": 54.00, "stock_quantity": 110, "description": "Odor-resistant natural merino wool athletic shirt for training and marathon.", "avg_rating": 4.5},
    {"product_id": "PROD-011", "product_name": "Adjustable Aluminum Laptop Stand", "category": "Electronics", "price": 39.99, "stock_quantity": 140, "description": "Foldable ergonomic riser for MacBooks and laptops up to 17 inches.", "avg_rating": 4.6},
    {"product_id": "PROD-012", "product_name": "Ceramic Pour-Over Coffee Dripper Set", "category": "Home & Kitchen", "price": 32.50, "stock_quantity": 75, "description": "Artisan ceramic dripper with wooden collar and 100 unbleached filters.", "avg_rating": 4.9},
    {"product_id": "PROD-013", "product_name": "Men's Performance All-Weather Jacket", "category": "Apparel", "price": 145.00, "stock_quantity": 55, "description": "Windproof and waterproof hooded shell jacket with sealed seams.", "avg_rating": 4.3},
    {"product_id": "PROD-014", "product_name": "Organic Cotton Yoga Mat 6mm", "category": "Sports & Fitness", "price": 45.00, "stock_quantity": 95, "description": "Non-slip eco-friendly textured exercise mat with carrying strap.", "avg_rating": 4.7},
    {"product_id": "PROD-015", "product_name": "USB-C Multi-Port Hub 7-in-1", "category": "Electronics", "price": 42.99, "stock_quantity": 160, "description": "Adapter with 4K HDMI, 100W PD charging, SD card reader, and 3 USB 3.0 ports.", "avg_rating": 4.2},
    {"product_id": "PROD-016", "product_name": "Polarized UV400 Aviator Sunglasses", "category": "Accessories", "price": 29.99, "stock_quantity": 130, "description": "Classic metal frame shades with glare reduction and protective hard case.", "avg_rating": 4.4},
    {"product_id": "PROD-017", "product_name": "Electric Sonic Toothbrush with Travel Case", "category": "Health & Personal Care", "price": 59.99, "stock_quantity": 105, "description": "40,000 VPM motor with 5 brushing modes and 4 replacement brush heads.", "avg_rating": 4.6},
    {"product_id": "PROD-018", "product_name": "Compact Cordless Stick Vacuum Cleaner", "category": "Home Appliances", "price": 189.00, "stock_quantity": 45, "description": "Lightweight 250W brushless suction vacuum with HEPA filtration system.", "avg_rating": 4.0},
    {"product_id": "PROD-019", "product_name": "True Wireless Sport Earbuds with Earhooks", "category": "Electronics", "price": 69.99, "stock_quantity": 115, "description": "IPX7 waterproof in-ear sports headphones with bass boost mode.", "avg_rating": 4.3},
    {"product_id": "PROD-020", "product_name": "Hard Shell Polycarbonate Carry-On 20\"", "category": "Bags & Luggage", "price": 119.99, "stock_quantity": 50, "description": "TSA approved spinner luggage with 360 silent dual wheels.", "avg_rating": 4.5},
    {"product_id": "PROD-021", "product_name": "High-Precision Gaming Optical Mouse", "category": "Electronics", "price": 49.99, "stock_quantity": 125, "description": "16,000 DPI optical sensor, customizable RGB zones, and ultra-lightweight cable.", "avg_rating": 4.6},
    {"product_id": "PROD-022", "product_name": "Cast Iron Pre-Seasoned Skillet 10-Inch", "category": "Home & Kitchen", "price": 38.00, "stock_quantity": 80, "description": "Heavy-duty frying pan for stovetop, oven, and campfire cooking.", "avg_rating": 4.8},
    {"product_id": "PROD-023", "product_name": "Resistance Bands Workout Set (5-Pack)", "category": "Sports & Fitness", "price": 22.99, "stock_quantity": 250, "description": "Stackable loop exercise bands with door anchor, handles, and ankle straps.", "avg_rating": 4.5},
    {"product_id": "PROD-024", "product_name": "Aromatherapy Essential Oil Diffuser 400ml", "category": "Home & Living", "price": 27.50, "stock_quantity": 140, "description": "Ultrasonic cool mist humidifier with 7 color LED ambient lights.", "avg_rating": 4.4},
    {"product_id": "PROD-025", "product_name": "Memory Foam Ergonomic Neck Pillow", "category": "Travel", "price": 26.99, "stock_quantity": 170, "description": "360 head and neck support pillow with washable breathable velvet cover.", "avg_rating": 4.6}
]

# -------------------------------------------------------------
# 2. CUSTOMERS DATASET (120 Synthetic Customers)
# -------------------------------------------------------------
FIRST_NAMES = [
    "Sarah", "Marcus", "Elena", "David", "Amanda", "Robert", "Maya", "Daniel", "Sophia", "Kevin",
    "Aarav", "Zoe", "Liam", "Ananya", "Lucas", "Fatima", "Ethan", "Chloe", "Noah", "Olivia",
    "Rohan", "Grace", "Oliver", "Zara", "Leo", "Amara", "Jack", "Mia", "Alexander", "Hannah",
    "Benjamin", "Layla", "Samuel", "Ava", "Henry", "Emily", "Sebastian", "Isabella", "Gabriel", "Ella",
    "Matthew", "Charlotte", "Ryan", "Amelia", "Nathan", "Harper", "Julian", "Evelyn", "Caleb", "Abigail"
]

LAST_NAMES = [
    "Chen", "Vance", "Rostova", "Kim", "Garcia", "Jenkins", "Patel", "O'Connor", "Martinez", "Zhang",
    "Sharma", "Kowalski", "Smith", "Iyer", "Muller", "Al-Mansoor", "Brown", "Taylor", "Wilson", "Johnson",
    "Verma", "Davis", "Anderson", "Siddiqui", "Dubois", "Nakamura", "White", "Harris", "Martin", "Thompson",
    "Deshmukh", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez",
    "King", "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson"
]

SEGMENTS = ["Loyal VIP", "High Value", "Occasional Shopper", "New Visitor", "Window Shopper", "Lapsed Customer"]
PAYMENT_METHODS = ["Credit Card", "Debit Card", "UPI", "PayPal", "Digital Wallet", "NetBanking"]

CUSTOMERS = []
# Pre-define 10 key scenario customers
SCENARIO_CUSTOMERS_META = [
    {"id": "CUST-1001", "name": "Sarah Chen", "segment": "Loyal VIP", "payment_method": "Credit Card", "orders": 12},
    {"id": "CUST-1002", "name": "Marcus Vance", "segment": "Occasional Shopper", "payment_method": "Debit Card", "orders": 3},
    {"id": "CUST-1003", "name": "Elena Rostova", "segment": "New Visitor", "payment_method": "Credit Card", "orders": 1},
    {"id": "CUST-1004", "name": "David Kim", "segment": "High Value", "payment_method": "Credit Card", "orders": 5},
    {"id": "CUST-1005", "name": "Amanda Garcia", "segment": "Occasional Shopper", "payment_method": "PayPal", "orders": 4},
    {"id": "CUST-1006", "name": "Robert Jenkins", "segment": "Loyal VIP", "payment_method": "Credit Card", "orders": 18},
    {"id": "CUST-1007", "name": "Maya Patel", "segment": "Occasional Shopper", "payment_method": "Debit Card", "orders": 2},
    {"id": "CUST-1008", "name": "Daniel O'Connor", "segment": "New Visitor", "payment_method": "Digital Wallet", "orders": 0},
    {"id": "CUST-1009", "name": "Sophia Martinez", "segment": "Window Shopper", "payment_method": "Credit Card", "orders": 0},
    {"id": "CUST-1010", "name": "Kevin Zhang", "segment": "High Value", "payment_method": "UPI", "orders": 6}
]

for meta in SCENARIO_CUSTOMERS_META:
    first, last = meta["name"].split(" ", 1)
    clean_last = last.lower().replace("'", "")
    email = f"{first.lower()}.{clean_last}@example.com"
    phone = f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    created_at = (datetime(2026, 1, 15) + timedelta(days=random.randint(0, 180))).strftime("%Y-%m-%d %H:%M:%S")
    CUSTOMERS.append({
        "customer_id": meta["id"],
        "name": meta["name"],
        "email": email,
        "phone": phone,
        "segment": meta["segment"],
        "created_at": created_at,
        "total_lifetime_orders": meta["orders"],
        "preferred_payment_method": meta["payment_method"]
    })

# Add remaining 110 customers to reach 120 total
for i in range(11, 121):
    cust_id = f"CUST-{1000 + i}"
    fn = random.choice(FIRST_NAMES)
    ln = random.choice(LAST_NAMES)
    name = f"{fn} {ln}"
    clean_ln = ln.lower().replace("'", "")
    email = f"{fn.lower()}.{clean_ln}{i}@example.com"
    phone = f"+1-555-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
    segment = random.choice(SEGMENTS)
    created_at = (datetime(2026, 1, 10) + timedelta(days=random.randint(0, 200))).strftime("%Y-%m-%d %H:%M:%S")
    orders_cnt = random.randint(0, 8) if segment != "Loyal VIP" else random.randint(8, 25)
    pref_pay = random.choice(PAYMENT_METHODS)
    CUSTOMERS.append({
        "customer_id": cust_id,
        "name": name,
        "email": email,
        "phone": phone,
        "segment": segment,
        "created_at": created_at,
        "total_lifetime_orders": orders_cnt,
        "preferred_payment_method": pref_pay
    })

# -------------------------------------------------------------
# 3, 4, 5, 6, 7. BUILDING ORDERS, PAYMENTS, EVENTS, TICKETS, FEEDBACK
# -------------------------------------------------------------

ORDERS = []
PAYMENTS = []
JOURNEY_EVENTS = []
SUPPORT_TICKETS = []
FEEDBACK_LIST = []

event_counter = 1
order_counter = 2001
payment_counter = 5001
ticket_counter = 3001
feedback_counter = 4001

def next_event_id():
    global event_counter
    eid = f"EVT-{event_counter:06d}"
    event_counter += 1
    return eid

def next_order_id():
    global order_counter
    oid = f"ORD-{order_counter}"
    order_counter += 1
    return oid

def next_payment_id():
    global payment_counter
    pid = f"PAY-{payment_counter}"
    payment_counter += 1
    return pid

def next_ticket_id():
    global ticket_counter
    tid = f"TIK-{ticket_counter}"
    ticket_counter += 1
    return tid

def next_feedback_id():
    global feedback_counter
    fid = f"FDB-{feedback_counter}"
    feedback_counter += 1
    return fid

# -------------------------------------------------------------
# SCENARIO 1: Successful Purchase (CUST-1001)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 15, 10, 0, 0)
sess_1 = "SESS-1001-A"
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "page_view", "product_id": "", "page_url": "/home", "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 15, "metadata": json.dumps({"source": "organic_search"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "search", "product_id": "", "page_url": "/search?q=ergonomic+chair", "timestamp": (t0 + timedelta(seconds=20)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 25, "metadata": json.dumps({"query": "ergonomic chair"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "product_view", "product_id": "PROD-003", "page_url": "/product/PROD-003", "timestamp": (t0 + timedelta(seconds=50)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 90, "metadata": json.dumps({"tab": "overview"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "add_to_cart", "product_id": "PROD-003", "page_url": "/cart", "timestamp": (t0 + timedelta(seconds=145)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 30, "metadata": json.dumps({"quantity": 1, "price": 249.50})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "checkout_started", "product_id": "PROD-003", "page_url": "/checkout", "timestamp": (t0 + timedelta(seconds=180)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 45, "metadata": json.dumps({"step": "shipping_address"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "payment_attempt", "product_id": "PROD-003", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=230)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 20, "metadata": json.dumps({"method": "Credit Card", "attempt": 1})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "payment_success", "product_id": "PROD-003", "page_url": "/checkout/confirmation", "timestamp": (t0 + timedelta(seconds=255)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 40, "metadata": json.dumps({"transaction_id": "TXN-90111", "amount": 249.50})})

ord_1 = "ORD-2001"
order_counter = 2002
pay_1 = next_payment_id()
ORDERS.append({
    "order_id": ord_1, "customer_id": "CUST-1001", "product_id": "PROD-003",
    "order_date": (t0 + timedelta(seconds=260)).strftime("%Y-%m-%d %H:%M:%S"),
    "total_amount": 249.50, "order_status": "delivered",
    "shipping_address": "742 Evergreen Terrace, Springfield, OR",
    "estimated_delivery_date": "2026-09-18 18:00:00",
    "actual_delivery_date": "2026-09-18 14:15:00"
})
PAYMENTS.append({
    "payment_id": pay_1, "order_id": ord_1, "customer_id": "CUST-1001",
    "payment_method": "Credit Card", "amount": 249.50, "currency": "USD",
    "payment_status": "success", "error_code": "", "error_message": "",
    "attempt_number": 1, "timestamp": (t0 + timedelta(seconds=255)).strftime("%Y-%m-%d %H:%M:%S")
})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": sess_1, "event_type": "order_placed", "product_id": "PROD-003", "page_url": "/order/ORD-2001", "timestamp": (t0 + timedelta(seconds=260)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 60, "metadata": json.dumps({"order_id": ord_1, "amount": 249.50})})
# Delivered and gave 5-star feedback
fdb_1 = next_feedback_id()
FEEDBACK_LIST.append({
    "feedback_id": fdb_1, "customer_id": "CUST-1001", "product_id": "PROD-003", "order_id": ord_1,
    "rating": 5, "review_title": "Best office chair ever!", "review_text": "Arrived right on time, assembly was a breeze, super comfortable for 8+ hour workdays.",
    "sentiment": "positive", "feedback_date": "2026-09-19 11:30:00"
})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1001", "session_id": "SESS-1001-B", "event_type": "feedback_submitted", "product_id": "PROD-003", "page_url": "/order/ORD-2001/feedback", "timestamp": "2026-09-19 11:30:00", "dwell_time_seconds": 75, "metadata": json.dumps({"rating": 5, "feedback_id": fdb_1})})


# -------------------------------------------------------------
# SCENARIO 2: Cart Abandonment (CUST-1002)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 20, 14, 10, 0)
sess_2 = "SESS-1002-A"
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1002", "session_id": sess_2, "event_type": "page_view", "product_id": "", "page_url": "/category/bags", "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 35, "metadata": json.dumps({"referrer": "google_ads"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1002", "session_id": sess_2, "event_type": "product_view", "product_id": "PROD-005", "page_url": "/product/PROD-005", "timestamp": (t0 + timedelta(seconds=40)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 120, "metadata": json.dumps({"variant": "Charcoal Black"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1002", "session_id": sess_2, "event_type": "add_to_cart", "product_id": "PROD-005", "page_url": "/cart", "timestamp": (t0 + timedelta(seconds=165)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 45, "metadata": json.dumps({"cart_value": 64.99, "quantity": 1})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1002", "session_id": sess_2, "event_type": "checkout_started", "product_id": "PROD-005", "page_url": "/checkout/shipping", "timestamp": (t0 + timedelta(seconds=215)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 190, "metadata": json.dumps({"shipping_cost_displayed": 14.99, "total_with_tax": 84.98})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1002", "session_id": sess_2, "event_type": "page_exit_without_purchase", "product_id": "PROD-005", "page_url": "/checkout/shipping", "timestamp": (t0 + timedelta(seconds=410)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 0, "metadata": json.dumps({"abandoned_step": "shipping_fee_reveal", "cart_value": 64.99})})


# -------------------------------------------------------------
# SCENARIO 3: Single Payment Failure (CUST-1003)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 21, 16, 20, 0)
sess_3 = "SESS-1003-A"
ord_3 = next_order_id()
pay_3 = next_payment_id()
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1003", "session_id": sess_3, "event_type": "product_view", "product_id": "PROD-002", "page_url": "/product/PROD-002", "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 80, "metadata": json.dumps({"category": "Electronics"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1003", "session_id": sess_3, "event_type": "add_to_cart", "product_id": "PROD-002", "page_url": "/cart", "timestamp": (t0 + timedelta(seconds=85)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 30, "metadata": json.dumps({"price": 199.99})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1003", "session_id": sess_3, "event_type": "checkout_started", "product_id": "PROD-002", "page_url": "/checkout", "timestamp": (t0 + timedelta(seconds=120)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 45, "metadata": json.dumps({"order_id": ord_3})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1003", "session_id": sess_3, "event_type": "payment_attempt", "product_id": "PROD-002", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=170)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 35, "metadata": json.dumps({"payment_id": pay_3, "method": "Credit Card", "attempt": 1})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1003", "session_id": sess_3, "event_type": "payment_failed", "product_id": "PROD-002", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=210)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 60, "metadata": json.dumps({"error_code": "GATEWAY_TIMEOUT", "error_message": "Payment gateway timed out while authenticating with bank", "attempt": 1})})

ORDERS.append({
    "order_id": ord_3, "customer_id": "CUST-1003", "product_id": "PROD-002",
    "order_date": (t0 + timedelta(seconds=120)).strftime("%Y-%m-%d %H:%M:%S"),
    "total_amount": 199.99, "order_status": "payment_failed",
    "shipping_address": "456 Elm Street, Seattle, WA",
    "estimated_delivery_date": "2026-09-26 18:00:00",
    "actual_delivery_date": ""
})
PAYMENTS.append({
    "payment_id": pay_3, "order_id": ord_3, "customer_id": "CUST-1003",
    "payment_method": "Credit Card", "amount": 199.99, "currency": "USD",
    "payment_status": "failed", "error_code": "GATEWAY_TIMEOUT",
    "error_message": "Payment gateway timed out while authenticating with bank",
    "attempt_number": 1, "timestamp": (t0 + timedelta(seconds=210)).strftime("%Y-%m-%d %H:%M:%S")
})


# -------------------------------------------------------------
# SCENARIO 4: Repeated Payment Failure (CUST-1004)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 22, 11, 0, 0)
sess_4 = "SESS-1004-A"
ord_4 = next_order_id()
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "product_view", "product_id": "PROD-001", "page_url": "/product/PROD-001", "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 60, "metadata": json.dumps({"price": 89.99})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "add_to_cart", "product_id": "PROD-001", "page_url": "/cart", "timestamp": (t0 + timedelta(seconds=65)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 25, "metadata": json.dumps({"qty": 1})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "checkout_started", "product_id": "PROD-001", "page_url": "/checkout", "timestamp": (t0 + timedelta(seconds=95)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 30, "metadata": json.dumps({"order_id": ord_4})})

# Attempt 1
pay_4_1 = next_payment_id()
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "payment_attempt", "product_id": "PROD-001", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=130)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 20, "metadata": json.dumps({"attempt": 1, "method": "Credit Card"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "payment_failed", "product_id": "PROD-001", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=155)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 40, "metadata": json.dumps({"attempt": 1, "error_code": "CARD_DECLINED", "msg": "Issuer bank declined transaction"})})
PAYMENTS.append({
    "payment_id": pay_4_1, "order_id": ord_4, "customer_id": "CUST-1004",
    "payment_method": "Credit Card", "amount": 89.99, "currency": "USD",
    "payment_status": "failed", "error_code": "CARD_DECLINED",
    "error_message": "Issuer bank declined transaction",
    "attempt_number": 1, "timestamp": (t0 + timedelta(seconds=155)).strftime("%Y-%m-%d %H:%M:%S")
})

# Attempt 2
pay_4_2 = next_payment_id()
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "payment_attempt", "product_id": "PROD-001", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=210)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 25, "metadata": json.dumps({"attempt": 2, "method": "Credit Card"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "payment_failed", "product_id": "PROD-001", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=240)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 50, "metadata": json.dumps({"attempt": 2, "error_code": "INSUFFICIENT_FUNDS", "msg": "Account has insufficient available credit limit"})})
PAYMENTS.append({
    "payment_id": pay_4_2, "order_id": ord_4, "customer_id": "CUST-1004",
    "payment_method": "Credit Card", "amount": 89.99, "currency": "USD",
    "payment_status": "failed", "error_code": "INSUFFICIENT_FUNDS",
    "error_message": "Account has insufficient available credit limit",
    "attempt_number": 2, "timestamp": (t0 + timedelta(seconds=240)).strftime("%Y-%m-%d %H:%M:%S")
})

# Attempt 3
pay_4_3 = next_payment_id()
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "payment_attempt", "product_id": "PROD-001", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=310)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 20, "metadata": json.dumps({"attempt": 3, "method": "Debit Card"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1004", "session_id": sess_4, "event_type": "payment_failed", "product_id": "PROD-001", "page_url": "/checkout/payment", "timestamp": (t0 + timedelta(seconds=335)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 90, "metadata": json.dumps({"attempt": 3, "error_code": "CARD_DECLINED", "msg": "Card authentication failed (3D Secure timeout)"})})
PAYMENTS.append({
    "payment_id": pay_4_3, "order_id": ord_4, "customer_id": "CUST-1004",
    "payment_method": "Debit Card", "amount": 89.99, "currency": "USD",
    "payment_status": "failed", "error_code": "CARD_DECLINED",
    "error_message": "Card authentication failed (3D Secure timeout)",
    "attempt_number": 3, "timestamp": (t0 + timedelta(seconds=335)).strftime("%Y-%m-%d %H:%M:%S")
})

ORDERS.append({
    "order_id": ord_4, "customer_id": "CUST-1004", "product_id": "PROD-001",
    "order_date": (t0 + timedelta(seconds=95)).strftime("%Y-%m-%d %H:%M:%S"),
    "total_amount": 89.99, "order_status": "payment_failed",
    "shipping_address": "88 Pine Lane, Austin, TX",
    "estimated_delivery_date": "2026-09-27 18:00:00",
    "actual_delivery_date": ""
})


# -------------------------------------------------------------
# SCENARIO 5: Delivery Delay (CUST-1005)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 10, 9, 30, 0)
sess_5 = "SESS-1005-A"
ord_5 = next_order_id()
pay_5 = next_payment_id()
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1005", "session_id": sess_5, "event_type": "product_view", "product_id": "PROD-010", "page_url": "/product/PROD-010", "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 45, "metadata": json.dumps({"size": "M"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1005", "session_id": sess_5, "event_type": "add_to_cart", "product_id": "PROD-010", "page_url": "/cart", "timestamp": (t0 + timedelta(seconds=55)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 20, "metadata": json.dumps({"qty": 1})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1005", "session_id": sess_5, "event_type": "checkout_started", "product_id": "PROD-010", "page_url": "/checkout", "timestamp": (t0 + timedelta(seconds=80)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 40, "metadata": json.dumps({"method": "PayPal"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1005", "session_id": sess_5, "event_type": "payment_success", "product_id": "PROD-010", "page_url": "/checkout/confirmation", "timestamp": (t0 + timedelta(seconds=130)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 30, "metadata": json.dumps({"payment_id": pay_5})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1005", "session_id": sess_5, "event_type": "order_placed", "product_id": "PROD-010", "page_url": "/order/ORD-2005", "timestamp": (t0 + timedelta(seconds=140)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 40, "metadata": json.dumps({"order_id": ord_5, "amount": 54.00})})

ORDERS.append({
    "order_id": ord_5, "customer_id": "CUST-1005", "product_id": "PROD-010",
    "order_date": (t0 + timedelta(seconds=140)).strftime("%Y-%m-%d %H:%M:%S"),
    "total_amount": 54.00, "order_status": "delayed",
    "shipping_address": "1203 Maple Blvd, Denver, CO",
    "estimated_delivery_date": "2026-09-14 18:00:00",
    "actual_delivery_date": ""
})
PAYMENTS.append({
    "payment_id": pay_5, "order_id": ord_5, "customer_id": "CUST-1005",
    "payment_method": "PayPal", "amount": 54.00, "currency": "USD",
    "payment_status": "success", "error_code": "", "error_message": "",
    "attempt_number": 1, "timestamp": (t0 + timedelta(seconds=130)).strftime("%Y-%m-%d %H:%M:%S")
})

# Customer repeatedly checks tracking because it's delayed past Sep 14
track_times = [
    "2026-09-15 08:30:00", "2026-09-15 19:15:00",
    "2026-09-16 09:00:00", "2026-09-16 16:45:00",
    "2026-09-17 11:20:00", "2026-09-18 14:10:00"
]
for idx, tt in enumerate(track_times):
    JOURNEY_EVENTS.append({
        "event_id": next_event_id(), "customer_id": "CUST-1005", "session_id": f"SESS-1005-TRACK-{idx+1}",
        "event_type": "order_tracking_checked", "product_id": "PROD-010",
        "page_url": f"/account/orders/{ord_5}/tracking", "timestamp": tt,
        "dwell_time_seconds": 65, "metadata": json.dumps({"status": "Delayed in transit at hub", "days_overdue": 1 + idx // 2})
    })


# -------------------------------------------------------------
# SCENARIO 6: Customer Support Complaint (CUST-1006)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 12, 13, 0, 0)
sess_6 = "SESS-1006-A"
ord_6 = next_order_id()
pay_6 = next_payment_id()
ORDERS.append({
    "order_id": ord_6, "customer_id": "CUST-1006", "product_id": "PROD-013",
    "order_date": t0.strftime("%Y-%m-%d %H:%M:%S"),
    "total_amount": 145.00, "order_status": "delivered",
    "shipping_address": "301 Ocean View Way, San Diego, CA",
    "estimated_delivery_date": "2026-09-16 18:00:00",
    "actual_delivery_date": "2026-09-15 16:30:00"
})
PAYMENTS.append({
    "payment_id": pay_6, "order_id": ord_6, "customer_id": "CUST-1006",
    "payment_method": "Credit Card", "amount": 145.00, "currency": "USD",
    "payment_status": "success", "error_code": "", "error_message": "",
    "attempt_number": 1, "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S")
})

# Customer received wrong size jacket, files urgent ticket, ticket sits unanswered for 36 hours
tik_6 = next_ticket_id()
SUPPORT_TICKETS.append({
    "ticket_id": tik_6, "customer_id": "CUST-1006", "order_id": ord_6,
    "subject": "Received wrong size jacket - completely unwearable, urgent replacement needed",
    "category": "Product Sizing", "priority": "urgent", "status": "open",
    "created_at": "2026-09-16 10:15:00", "resolved_at": "",
    "resolution_notes": "SLA breached: First response SLA (4 hours) exceeded by 36+ hours. Customer waiting for exchange."
})
JOURNEY_EVENTS.append({
    "event_id": next_event_id(), "customer_id": "CUST-1006", "session_id": "SESS-1006-TIK",
    "event_type": "support_ticket_created", "product_id": "PROD-013",
    "page_url": "/support/tickets/new", "timestamp": "2026-09-16 10:15:00",
    "dwell_time_seconds": 180, "metadata": json.dumps({"ticket_id": tik_6, "priority": "urgent", "category": "Product Sizing"})
})
JOURNEY_EVENTS.append({
    "event_id": next_event_id(), "customer_id": "CUST-1006", "session_id": "SESS-1006-TIK-CHECK",
    "event_type": "support_ticket_viewed", "product_id": "PROD-013",
    "page_url": f"/support/tickets/{tik_6}", "timestamp": "2026-09-17 18:30:00",
    "dwell_time_seconds": 120, "metadata": json.dumps({"status": "open", "agent_assigned": False, "hours_elapsed": 32})
})


# -------------------------------------------------------------
# SCENARIO 7: Negative Product Feedback (CUST-1007)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 8, 15, 0, 0)
ord_7 = next_order_id()
pay_7 = next_payment_id()
ORDERS.append({
    "order_id": ord_7, "customer_id": "CUST-1007", "product_id": "PROD-004",
    "order_date": t0.strftime("%Y-%m-%d %H:%M:%S"),
    "total_amount": 49.99, "order_status": "delivered",
    "shipping_address": "550 Willow Creek Rd, Atlanta, GA",
    "estimated_delivery_date": "2026-09-12 18:00:00",
    "actual_delivery_date": "2026-09-11 15:00:00"
})
PAYMENTS.append({
    "payment_id": pay_7, "order_id": ord_7, "customer_id": "CUST-1007",
    "payment_method": "Debit Card", "amount": 49.99, "currency": "USD",
    "payment_status": "success", "error_code": "", "error_message": "",
    "attempt_number": 1, "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S")
})

fdb_7 = next_feedback_id()
FEEDBACK_LIST.append({
    "feedback_id": fdb_7, "customer_id": "CUST-1007", "product_id": "PROD-004", "order_id": ord_7,
    "rating": 1, "review_title": "Defective screen, stopped working after 3 days",
    "review_text": "Horrible quality. The screen flickered and died completely on day 3. Battery overheats when plugged in. Do not buy!",
    "sentiment": "negative", "feedback_date": "2026-09-16 14:20:00"
})
JOURNEY_EVENTS.append({
    "event_id": next_event_id(), "customer_id": "CUST-1007", "session_id": "SESS-1007-REV",
    "event_type": "feedback_submitted", "product_id": "PROD-004",
    "page_url": f"/product/PROD-004/review", "timestamp": "2026-09-16 14:20:00",
    "dwell_time_seconds": 150, "metadata": json.dumps({"rating": 1, "sentiment": "negative", "feedback_id": fdb_7})
})


# -------------------------------------------------------------
# SCENARIO 8: Product Information Confusion (CUST-1008)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 23, 19, 0, 0)
sess_8 = "SESS-1008-A"
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1008", "session_id": sess_8, "event_type": "product_view", "product_id": "PROD-007", "page_url": "/product/PROD-007", "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 45, "metadata": json.dumps({"section": "hero"})})
for step in range(4):
    ts_spec = (t0 + timedelta(seconds=50 + step * 70)).strftime("%Y-%m-%d %H:%M:%S")
    JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1008", "session_id": sess_8, "event_type": "specification_view", "product_id": "PROD-007", "page_url": "/product/PROD-007#specs", "timestamp": ts_spec, "dwell_time_seconds": 30, "metadata": json.dumps({"tab": "sensor_compatibility", "switch_count": step * 2 + 1})})
    ts_guide = (t0 + timedelta(seconds=85 + step * 70)).strftime("%Y-%m-%d %H:%M:%S")
    JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1008", "session_id": sess_8, "event_type": "size_guide_view", "product_id": "PROD-007", "page_url": "/product/PROD-007#strap_fit", "timestamp": ts_guide, "dwell_time_seconds": 35, "metadata": json.dumps({"modal": "strap_sizing_chart", "switch_count": step * 2 + 2})})

JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1008", "session_id": sess_8, "event_type": "page_exit_without_purchase", "product_id": "PROD-007", "page_url": "/product/PROD-007", "timestamp": (t0 + timedelta(seconds=420)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 0, "metadata": json.dumps({"reason": "high_hesitation_no_cart", "total_dwell_seconds": 420, "spec_switches": 8})})


# -------------------------------------------------------------
# SCENARIO 9: High Browsing But No Purchase (CUST-1009)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 24, 10, 0, 0)
sess_9 = "SESS-1009-A"
# 18 product views across multiple electronics products without a single add_to_cart
browse_products = ["PROD-001", "PROD-002", "PROD-008", "PROD-009", "PROD-011", "PROD-015", "PROD-019", "PROD-021"]
cur_time = t0
for idx in range(18):
    p_id = browse_products[idx % len(browse_products)]
    cur_time += timedelta(minutes=random.randint(1, 3), seconds=random.randint(10, 45))
    JOURNEY_EVENTS.append({
        "event_id": next_event_id(), "customer_id": "CUST-1009", "session_id": sess_9 if idx < 10 else "SESS-1009-B",
        "event_type": "product_view", "product_id": p_id,
        "page_url": f"/product/{p_id}", "timestamp": cur_time.strftime("%Y-%m-%d %H:%M:%S"),
        "dwell_time_seconds": random.randint(25, 65),
        "metadata": json.dumps({"filter_applied": "price_under_100", "browse_sequence": idx + 1})
    })
    if idx % 4 == 0:
        cur_time += timedelta(seconds=15)
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": "CUST-1009", "session_id": sess_9 if idx < 10 else "SESS-1009-B",
            "event_type": "search", "product_id": "",
            "page_url": "/search", "timestamp": cur_time.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": 20,
            "metadata": json.dumps({"query": f"affordable wireless accessories {idx}", "results_viewed": 12})
        })


# -------------------------------------------------------------
# SCENARIO 10: Successful Recovery After Intervention (CUST-1010)
# -------------------------------------------------------------
t0 = datetime(2026, 9, 25, 15, 0, 0)
sess_10_a = "SESS-1010-A"
ord_10 = next_order_id()
pay_10 = next_payment_id()

# Phase 1: Abandonment
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_a, "event_type": "product_view", "product_id": "PROD-008", "page_url": "/product/PROD-008", "timestamp": t0.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 60, "metadata": json.dumps({"price": 34.99})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_a, "event_type": "add_to_cart", "product_id": "PROD-008", "page_url": "/cart", "timestamp": (t0 + timedelta(seconds=70)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 30, "metadata": json.dumps({"quantity": 2, "cart_total": 69.98})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_a, "event_type": "checkout_started", "product_id": "PROD-008", "page_url": "/checkout", "timestamp": (t0 + timedelta(seconds=110)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 45, "metadata": json.dumps({"step": "payment_selection"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_a, "event_type": "page_exit_without_purchase", "product_id": "PROD-008", "page_url": "/checkout", "timestamp": (t0 + timedelta(seconds=180)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 0, "metadata": json.dumps({"friction_flag": "cart_abandoned", "cart_total": 69.98})})

# Phase 2: Automated Recovery Intervention dispatched 35 mins later
t_rec = t0 + timedelta(minutes=35)
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": "SYSTEM-INTERVENTION", "event_type": "recovery_email_sent", "product_id": "PROD-008", "page_url": "/system/notifications", "timestamp": t_rec.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 0, "metadata": json.dumps({"coupon_code": "RECOVER15", "discount_percent": 15, "channel": "email_and_sms"})})

# Phase 3: Customer clicks recovery link and finishes checkout
t_click = t_rec + timedelta(hours=1, minutes=15)
sess_10_b = "SESS-1010-B"
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_b, "event_type": "recovery_link_clicked", "product_id": "PROD-008", "page_url": "/cart?coupon=RECOVER15", "timestamp": t_click.strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 25, "metadata": json.dumps({"applied_coupon": "RECOVER15", "discounted_total": 59.48})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_b, "event_type": "checkout_started", "product_id": "PROD-008", "page_url": "/checkout", "timestamp": (t_click + timedelta(seconds=35)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 30, "metadata": json.dumps({"step": "payment"})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_b, "event_type": "payment_success", "product_id": "PROD-008", "page_url": "/checkout/confirmation", "timestamp": (t_click + timedelta(seconds=75)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 35, "metadata": json.dumps({"payment_id": pay_10, "method": "UPI", "amount": 59.48})})
JOURNEY_EVENTS.append({"event_id": next_event_id(), "customer_id": "CUST-1010", "session_id": sess_10_b, "event_type": "order_placed", "product_id": "PROD-008", "page_url": f"/order/{ord_10}", "timestamp": (t_click + timedelta(seconds=80)).strftime("%Y-%m-%d %H:%M:%S"), "dwell_time_seconds": 50, "metadata": json.dumps({"order_id": ord_10, "recovery_status": "converted", "coupon": "RECOVER15"})})

ORDERS.append({
    "order_id": ord_10, "customer_id": "CUST-1010", "product_id": "PROD-008",
    "order_date": (t_click + timedelta(seconds=80)).strftime("%Y-%m-%d %H:%M:%S"),
    "total_amount": 59.48, "order_status": "delivered",
    "shipping_address": "902 Broadway Ave, New York, NY",
    "estimated_delivery_date": "2026-09-28 18:00:00",
    "actual_delivery_date": "2026-09-28 13:40:00"
})
PAYMENTS.append({
    "payment_id": pay_10, "order_id": ord_10, "customer_id": "CUST-1010",
    "payment_method": "UPI", "amount": 59.48, "currency": "USD",
    "payment_status": "success", "error_code": "", "error_message": "",
    "attempt_number": 1, "timestamp": (t_click + timedelta(seconds=75)).strftime("%Y-%m-%d %H:%M:%S")
})


# -------------------------------------------------------------
# GENERATE REALISTIC JOURNEYS FOR REMAINING CUSTOMERS (CUST-1011 to CUST-1120)
# -------------------------------------------------------------
for c_idx in range(11, 121):
    cust = CUSTOMERS[c_idx - 1]
    cid = cust["customer_id"]
    base_date = datetime(2026, 8, 1) + timedelta(days=random.randint(0, 50), hours=random.randint(8, 20))
    sess_id = f"SESS-{cid[5:]}-1"
    
    # Randomly assign a behavior profile
    # 55% successful buyers, 20% cart abandoners, 10% browsers, 10% payment issues, 5% delivery/ticket
    profile = random.choices(
        ["success", "abandon", "browse_only", "payment_glitch", "ticket_inquiry"],
        weights=[55, 20, 10, 10, 5]
    )[0]
    
    prod = random.choice(PRODUCTS)
    pid = prod["product_id"]
    price = prod["price"]
    
    # Always view product
    JOURNEY_EVENTS.append({
        "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
        "event_type": "product_view", "product_id": pid, "page_url": f"/product/{pid}",
        "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
        "dwell_time_seconds": random.randint(30, 120),
        "metadata": json.dumps({"category": prod["category"]})
    })
    
    if profile == "browse_only":
        # Just browsed a couple more products
        for b in range(random.randint(2, 5)):
            p_extra = random.choice(PRODUCTS)["product_id"]
            base_date += timedelta(minutes=random.randint(1, 4))
            JOURNEY_EVENTS.append({
                "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
                "event_type": "product_view", "product_id": p_extra, "page_url": f"/product/{p_extra}",
                "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
                "dwell_time_seconds": random.randint(20, 60),
                "metadata": json.dumps({"category": prod["category"]})
            })
            
    elif profile == "abandon":
        base_date += timedelta(seconds=random.randint(40, 90))
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "add_to_cart", "product_id": pid, "page_url": "/cart",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(20, 50),
            "metadata": json.dumps({"price": price, "qty": 1})
        })
        base_date += timedelta(seconds=random.randint(30, 60))
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "checkout_started", "product_id": pid, "page_url": "/checkout",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(60, 150),
            "metadata": json.dumps({"step": "shipping"})
        })
        
    elif profile in ["success", "ticket_inquiry"]:
        base_date += timedelta(seconds=random.randint(30, 60))
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "add_to_cart", "product_id": pid, "page_url": "/cart",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(20, 45),
            "metadata": json.dumps({"price": price, "qty": 1})
        })
        base_date += timedelta(seconds=random.randint(25, 45))
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "checkout_started", "product_id": pid, "page_url": "/checkout",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(30, 60),
            "metadata": json.dumps({"step": "payment"})
        })
        base_date += timedelta(seconds=random.randint(20, 40))
        pay_id = next_payment_id()
        ord_id = next_order_id()
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "payment_success", "product_id": pid, "page_url": "/checkout/confirmation",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(20, 40),
            "metadata": json.dumps({"payment_id": pay_id, "amount": price})
        })
        base_date += timedelta(seconds=10)
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "order_placed", "product_id": pid, "page_url": f"/order/{ord_id}",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(30, 60),
            "metadata": json.dumps({"order_id": ord_id, "amount": price})
        })
        
        eta = base_date + timedelta(days=4)
        act = eta - timedelta(hours=random.randint(2, 12))
        ORDERS.append({
            "order_id": ord_id, "customer_id": cid, "product_id": pid,
            "order_date": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "total_amount": price, "order_status": "delivered",
            "shipping_address": f"{random.randint(100, 999)} Main Street, City {c_idx}, USA",
            "estimated_delivery_date": eta.strftime("%Y-%m-%d %H:%M:%S"),
            "actual_delivery_date": act.strftime("%Y-%m-%d %H:%M:%S")
        })
        PAYMENTS.append({
            "payment_id": pay_id, "order_id": ord_id, "customer_id": cid,
            "payment_method": cust["preferred_payment_method"], "amount": price, "currency": "USD",
            "payment_status": "success", "error_code": "", "error_message": "",
            "attempt_number": 1, "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # Some customers give feedback
        if random.random() < 0.35:
            r = random.choice([4, 5, 5, 4, 3])
            fid = next_feedback_id()
            f_date = act + timedelta(days=random.randint(1, 3))
            FEEDBACK_LIST.append({
                "feedback_id": fid, "customer_id": cid, "product_id": pid, "order_id": ord_id,
                "rating": r, "review_title": "Great quality and fast delivery" if r >= 4 else "Average product",
                "review_text": "Satisfied with purchase. Matches expectations." if r >= 4 else "Decent product, packaging could be better.",
                "sentiment": "positive" if r >= 4 else "neutral",
                "feedback_date": f_date.strftime("%Y-%m-%d %H:%M:%S")
            })
            JOURNEY_EVENTS.append({
                "event_id": next_event_id(), "customer_id": cid, "session_id": f"SESS-{cid[5:]}-REV",
                "event_type": "feedback_submitted", "product_id": pid, "page_url": f"/product/{pid}/review",
                "timestamp": f_date.strftime("%Y-%m-%d %H:%M:%S"),
                "dwell_time_seconds": random.randint(40, 80),
                "metadata": json.dumps({"rating": r, "feedback_id": fid})
            })
            
        if profile == "ticket_inquiry":
            tid = next_ticket_id()
            t_create = act + timedelta(days=1)
            t_resolve = t_create + timedelta(hours=3)
            SUPPORT_TICKETS.append({
                "ticket_id": tid, "customer_id": cid, "order_id": ord_id,
                "subject": "Inquiry regarding invoice copy and warranty registration",
                "category": "General Inquiry", "priority": "low", "status": "resolved",
                "created_at": t_create.strftime("%Y-%m-%d %H:%M:%S"),
                "resolved_at": t_resolve.strftime("%Y-%m-%d %H:%M:%S"),
                "resolution_notes": "Invoice copy emailed to customer. Warranty registered successfully."
            })
            
    elif profile == "payment_glitch":
        base_date += timedelta(seconds=random.randint(30, 60))
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "add_to_cart", "product_id": pid, "page_url": "/cart",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(20, 45),
            "metadata": json.dumps({"price": price, "qty": 1})
        })
        base_date += timedelta(seconds=random.randint(25, 45))
        ord_id = next_order_id()
        pay_id = next_payment_id()
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "checkout_started", "product_id": pid, "page_url": "/checkout",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(30, 60),
            "metadata": json.dumps({"order_id": ord_id})
        })
        base_date += timedelta(seconds=20)
        JOURNEY_EVENTS.append({
            "event_id": next_event_id(), "customer_id": cid, "session_id": sess_id,
            "event_type": "payment_failed", "product_id": pid, "page_url": "/checkout/payment",
            "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "dwell_time_seconds": random.randint(40, 90),
            "metadata": json.dumps({"error_code": "OTP_EXPIRED", "msg": "OTP verification timed out"})
        })
        ORDERS.append({
            "order_id": ord_id, "customer_id": cid, "product_id": pid,
            "order_date": base_date.strftime("%Y-%m-%d %H:%M:%S"),
            "total_amount": price, "order_status": "payment_failed",
            "shipping_address": f"{random.randint(100, 999)} Boulevard, City {c_idx}, USA",
            "estimated_delivery_date": (base_date + timedelta(days=4)).strftime("%Y-%m-%d %H:%M:%S"),
            "actual_delivery_date": ""
        })
        PAYMENTS.append({
            "payment_id": pay_id, "order_id": ord_id, "customer_id": cid,
            "payment_method": cust["preferred_payment_method"], "amount": price, "currency": "USD",
            "payment_status": "failed", "error_code": "OTP_EXPIRED",
            "error_message": "OTP verification timed out",
            "attempt_number": 1, "timestamp": base_date.strftime("%Y-%m-%d %H:%M:%S")
        })

# -------------------------------------------------------------
# WRITE CSV FILES
# -------------------------------------------------------------

def write_csv(filename, fieldnames, rows):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Generated {filename}: {len(rows)} records.")

# 1. products.csv
write_csv("products.csv", ["product_id", "product_name", "category", "price", "stock_quantity", "description", "avg_rating"], PRODUCTS)

# 2. customers.csv
write_csv("customers.csv", ["customer_id", "name", "email", "phone", "segment", "created_at", "total_lifetime_orders", "preferred_payment_method"], CUSTOMERS)

# 3. orders.csv
write_csv("orders.csv", ["order_id", "customer_id", "product_id", "order_date", "total_amount", "order_status", "shipping_address", "estimated_delivery_date", "actual_delivery_date"], ORDERS)

# 4. payments.csv
write_csv("payments.csv", ["payment_id", "order_id", "customer_id", "payment_method", "amount", "currency", "payment_status", "error_code", "error_message", "attempt_number", "timestamp"], PAYMENTS)

# 5. journey_events.csv
# Sort journey events chronologically per customer
JOURNEY_EVENTS.sort(key=lambda x: (x["customer_id"], x["timestamp"]))
write_csv("journey_events.csv", ["event_id", "customer_id", "session_id", "event_type", "product_id", "page_url", "timestamp", "dwell_time_seconds", "metadata"], JOURNEY_EVENTS)

# 6. support_tickets.csv
write_csv("support_tickets.csv", ["ticket_id", "customer_id", "order_id", "subject", "category", "priority", "status", "created_at", "resolved_at", "resolution_notes"], SUPPORT_TICKETS)

# 7. feedback.csv
write_csv("feedback.csv", ["feedback_id", "customer_id", "product_id", "order_id", "rating", "review_title", "review_text", "sentiment", "feedback_date"], FEEDBACK_LIST)

print("All 7 synthetic CSV datasets created successfully in 'data/'!")
