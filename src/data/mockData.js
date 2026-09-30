// Telemetry dataset representing Real-Time Customer Sessions, Friction Detection, Diagnostic Inferences, and Recovery Yields
// Engine: PathPulse Enterprise Behavioral Analytics & Telemetry Layer


export const INITIAL_CUSTOMERS = [
  {
    id: "CUST-9481",
    name: "Alex Mercer",
    email: "alex.mercer@gmail.com",
    avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=120&auto=format&fit=crop&q=80",
    segment: "VIP / Returning",
    cartValue: 349.99,
    device: "iPhone 15 Pro (Safari Mobile)",
    location: "Austin, TX",
    journeyStage: "Payment",
    riskLevel: "Critical",
    riskScore: 94,
    frictionType: "Payment Gateway Failure",
    status: "Pending Action",
    timeElapsed: "3m ago",
    itemsInCart: [
      { name: "Sony WH-1000XM5 Wireless Headphones", price: 299.99, qty: 1, img: "🎧" },
      { name: "Hard Shell Headphone Carrying Case", price: 50.00, qty: 1, img: "💼" }
    ],
    journeySteps: [
      {
        id: "step-1",
        stepNumber: 1,
        title: "Search & Landing",
        page: "/search?q=noise+cancelling+headphones",
        dwellTime: "42s",
        timestamp: "11:42 AM",
        type: "navigation",
        sentiment: "neutral",
        details: "Entered from Google Shopping ad; filtered by Sony & 4+ stars.",
        friction: false
      },
      {
        id: "step-2",
        stepNumber: 2,
        title: "Product Detail Page",
        page: "/products/sony-wh-1000xm5-black",
        dwellTime: "2m 15s",
        timestamp: "11:43 AM",
        type: "interaction",
        sentiment: "positive",
        details: "Read 6 reviews; toggled 360-view; checked battery specs.",
        friction: false
      },
      {
        id: "step-3",
        stepNumber: 3,
        title: "Add to Cart & Upsell",
        page: "/cart",
        dwellTime: "55s",
        timestamp: "11:45 AM",
        type: "action",
        sentiment: "positive",
        details: "Accepted carrying case upsell; Total cart $349.99.",
        friction: false
      },
      {
        id: "step-4",
        stepNumber: 4,
        title: "Shipping Address Selection",
        page: "/checkout/shipping",
        dwellTime: "1m 10s",
        timestamp: "11:46 AM",
        type: "form",
        sentiment: "neutral",
        details: "Saved address pre-filled; selected Standard Free 2-Day Shipping.",
        friction: false
      },
      {
        id: "step-5",
        stepNumber: 5,
        title: "Payment Gateway Attempt #1",
        page: "/checkout/payment",
        dwellTime: "48s",
        timestamp: "11:48 AM",
        type: "transaction",
        sentiment: "frustrated",
        details: "Visa ending 4281 submitted; 3DS OTP verification modal froze.",
        friction: true,
        frictionAlert: "3DS Auth Timeout (Bank OTP iframe failed to render)"
      },
      {
        id: "step-6",
        stepNumber: 6,
        title: "Rage Clicks & Gateway Error #2",
        page: "/checkout/payment",
        dwellTime: "1m 20s",
        timestamp: "11:49 AM",
        type: "error",
        sentiment: "critical",
        details: "User clicked 'Complete Purchase' 5 times in 3.2 seconds. Gateway returned ERR_TIMEOUT_402.",
        friction: true,
        frictionAlert: "5 Rapid Rage Clicks detected + Gateway Timeout 402"
      },
      {
        id: "step-7",
        stepNumber: 7,
        title: "Session Abandonment",
        page: "/checkout/payment",
        dwellTime: "15s",
        timestamp: "11:51 AM",
        type: "dropoff",
        sentiment: "critical",
        details: "Tab lost focus; user switched to competitor tab (BestBuy.com).",
        friction: true,
        frictionAlert: "Cart Abandonment & Exit Intent Detected"
      }
    ],
    aiAnalysis: {
      primaryCause: "Payment Gateway Timeout & 3DS Authentication Failure",
      category: "Payment Failures",
      confidence: 96,
      rootCauseSummary: "The customer's issuing bank 3D-Secure 2.0 iframe failed to resolve within 30 seconds. The customer experienced UI freeze and triggered multiple rage clicks before exiting. Customer has high intent (VIP tier, 2 items in cart, 349.99 value).",
      evidenceSignals: [
        { label: "Payment Log Error", value: "ERR_3DS_CHALLENGE_TIMEOUT (Stripe Error 402)", severity: "high" },
        { label: "Behavioral Metric", value: "5 rage-clicks within 3.2s on Submit button", severity: "high" },
        { label: "Customer Lifetime Value", value: "$2,450 over 6 previous orders (High loyalty)", severity: "info" },
        { label: "Session Duration", value: "6m 10s active browsing before failure", severity: "info" }
      ],
      recommendations: [
        {
          id: "rec-1",
          type: "Instant Payment Fallback Link",
          description: "Generate 1-click Apple Pay / Google Pay / UPI recovery link sent via SMS and Email with cart reservation for 30 minutes.",
          expectedRecoveryRate: "88%",
          actionLabel: "Send Instant Alternate Payment Link",
          suggestedDiscount: null,
          channel: "SMS + Email"
        },
        {
          id: "rec-2",
          type: "Friction Apology + Priority Agent Call",
          description: "Alert VIP Support desk to initiate proactive WhatsApp / Phone concierge assistance with zero-friction checkout.",
          expectedRecoveryRate: "79%",
          actionLabel: "Dispatch VIP Concierge Assist",
          suggestedDiscount: "5% Courtesy Credit",
          channel: "WhatsApp"
        }
      ]
    }
  },
  {
    id: "CUST-9482",
    name: "Sarah Lin",
    email: "sarah.lin92@outlook.com",
    avatar: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=120&auto=format&fit=crop&q=80",
    segment: "First-Time Shopper",
    cartValue: 145.00,
    device: "MacBook Air (Chrome Desktop)",
    location: "Seattle, WA",
    journeyStage: "Cart Review",
    riskLevel: "High",
    riskScore: 82,
    frictionType: "Delivery Uncertainty & Shipping Shock",
    status: "Pending Action",
    timeElapsed: "8m ago",
    itemsInCart: [
      { name: "Organic Merino Wool Cardigan (Olive, M)", price: 115.00, qty: 1, img: "🧥" },
      { name: "Silk Scarf (Terracotta)", price: 30.00, qty: 1, img: "🧣" }
    ],
    journeySteps: [
      {
        id: "step-1",
        stepNumber: 1,
        title: "Instagram Ad Referral",
        page: "/collections/autumn-knitwear",
        dwellTime: "1m 05s",
        timestamp: "11:35 AM",
        type: "navigation",
        sentiment: "positive",
        details: "Referral from Instagram Story promo; high engagement.",
        friction: false
      },
      {
        id: "step-2",
        stepNumber: 2,
        title: "Product Page Exploration",
        page: "/products/merino-wool-cardigan",
        dwellTime: "3m 40s",
        timestamp: "11:36 AM",
        type: "interaction",
        sentiment: "positive",
        details: "Checked size chart; hovered fabric transparency info.",
        friction: false
      },
      {
        id: "step-3",
        stepNumber: 3,
        title: "Cart & Delivery Check",
        page: "/cart",
        dwellTime: "2m 10s",
        timestamp: "11:40 AM",
        type: "form",
        sentiment: "confused",
        details: "Entered zip 98101. Standard shipping showed '$18.50 - Estimated 7-12 business days (Unconfirmed)'.",
        friction: true,
        frictionAlert: "High Shipping Cost Shock ($18.50 on $145 order) & Vague ETA"
      },
      {
        id: "step-4",
        stepNumber: 4,
        title: "Shipping Policy FAQ Hovering",
        page: "/pages/shipping-faq",
        dwellTime: "1m 45s",
        timestamp: "11:42 AM",
        type: "navigation",
        sentiment: "frustrated",
        details: "Opened Delivery FAQ in modal; scrolled to 'Holiday Shipping Delays' section twice.",
        friction: true,
        frictionAlert: "Customer looking for delivery guarantees; none found."
      },
      {
        id: "step-5",
        stepNumber: 5,
        title: "Cart Left Idle",
        page: "/cart",
        dwellTime: "3m 00s",
        timestamp: "11:44 AM",
        type: "dropoff",
        sentiment: "critical",
        details: "Mouse left viewport toward browser close tab.",
        friction: true,
        frictionAlert: "Cart Idle & Exit Intent"
      }
    ],
    aiAnalysis: {
      primaryCause: "Unexpected Shipping Fee ($18.50) & Ambiguous Delivery Window",
      category: "Delivery Uncertainty",
      confidence: 93,
      rootCauseSummary: "User spent nearly 2 minutes reading shipping policies after seeing $18.50 shipping fee with vague 7-12 day ETA. Order is just $5 away from typical free shipping threshold ($150), causing hesitation.",
      evidenceSignals: [
        { label: "Cart Step Behavior", value: "User visited Shipping FAQ 2 times after cart calculation", severity: "high" },
        { label: "Threshold Proximity", value: "Cart total $145 is $5 below free shipping benchmark", severity: "medium" },
        { label: "Exit Trajectory", value: "Mouse cursor velocity toward back button after shipping display", severity: "medium" }
      ],
      recommendations: [
        {
          id: "rec-1",
          type: "Free Expedited Shipping Upgrade + Guaranteed Date",
          description: "Display an in-session banner: 'Free 3-Day Express Shipping unlocked! Guaranteed delivery by Friday, Oct 4.'",
          expectedRecoveryRate: "84%",
          actionLabel: "Grant Free Expedited Shipping",
          suggestedDiscount: "Free Shipping ($18.50 off)",
          channel: "In-App Toast & Dynamic Banner"
        },
        {
          id: "rec-2",
          type: "Add $5 Mystery Mini Add-on Offer",
          description: "Suggest a matching $8 wool care comb to cross the $150 free shipping threshold seamlessly.",
          expectedRecoveryRate: "72%",
          actionLabel: "Offer 1-Click Threshold Booster",
          suggestedDiscount: null,
          channel: "In-Cart Overlay"
        }
      ]
    }
  },
  {
    id: "CUST-9483",
    name: "David Miller",
    email: "dmiller.consulting@tech.org",
    avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=120&auto=format&fit=crop&q=80",
    segment: "High Intent / Evaluator",
    cartValue: 890.00,
    device: "Windows 11 (Edge Desktop)",
    location: "Chicago, IL",
    journeyStage: "Product Comparison",
    riskLevel: "High",
    riskScore: 78,
    frictionType: "Comparison Fatigue & Unclear Specs",
    status: "Pending Action",
    timeElapsed: "14m ago",
    itemsInCart: [
      { name: "UltraWide 38-inch Curved Monitor (Model Pro-X)", price: 890.00, qty: 1, img: "🖥️" }
    ],
    journeySteps: [
      {
        id: "step-1",
        stepNumber: 1,
        title: "Product Search & Filter",
        page: "/monitors/curved",
        dwellTime: "1m 30s",
        timestamp: "11:20 AM",
        type: "navigation",
        sentiment: "neutral",
        details: "Filtered by USB-C 90W Power Delivery and 144Hz refresh rate.",
        friction: false
      },
      {
        id: "step-2",
        stepNumber: 2,
        title: "Rapid Tab Switching (12 tabs)",
        page: "/products/compare?id1=PRO-X&id2=ULTRA-Z",
        dwellTime: "5m 10s",
        timestamp: "11:22 AM",
        type: "interaction",
        sentiment: "frustrated",
        details: "Toggled between Model Pro-X and Ultra-Z 14 times. Specification table missing Mac M3 compatibility confirmation.",
        friction: true,
        frictionAlert: "Comparison Fatigue: 14 toggles between two SKUs without decision"
      },
      {
        id: "step-3",
        stepNumber: 3,
        title: "Search in FAQ / Q&A",
        page: "/products/pro-x#qa-section",
        dwellTime: "2m 40s",
        timestamp: "11:27 AM",
        type: "search",
        sentiment: "confused",
        details: "Searched question: 'Does Thunderbolt 4 charge MacBook Pro 16 at full speed?' (0 results returned).",
        friction: true,
        frictionAlert: "Zero-Result Search Query on critical purchase blocker"
      },
      {
        id: "step-4",
        stepNumber: 4,
        title: "Return Policy Check",
        page: "/return-policy",
        dwellTime: "1m 15s",
        timestamp: "11:30 AM",
        type: "navigation",
        sentiment: "cautious",
        details: "Customer checking restocking fee clause for open-box electronics.",
        friction: true,
        frictionAlert: "High return-risk hesitation on $890 ticket item"
      }
    ],
    aiAnalysis: {
      primaryCause: "Compatibility Information Vacuum & Fear of Restocking Fee",
      category: "Unclear Product Information",
      confidence: 91,
      rootCauseSummary: "Buyer is hesitating on $890 purchase because product page fails to confirm Mac M3 Thunderbolt 4 90W charging compatibility. Search in Q&A returned 0 hits, driving customer to verify return policy.",
      evidenceSignals: [
        { label: "Search Telemetry", value: "Zero search results for 'Thunderbolt 4 MacBook Pro 16 charging'", severity: "high" },
        { label: "Comparison Loops", value: "14 side-by-side switches between 2 monitor variants", severity: "high" },
        { label: "Restocking Fee View", value: "Customer scrolled directly to 15% restocking fee fine print", severity: "medium" }
      ],
      recommendations: [
        {
          id: "rec-1",
          type: "Proactive AI Tech Spec Answer + Zero-Risk Trial",
          description: "Trigger in-app notification: 'Verified by Tech Support: Model Pro-X supports 90W fast charging on all MacBook Pro M1/M2/M3 chips. Plus, enjoy 30-Day Zero Restocking Fee trial.'",
          expectedRecoveryRate: "86%",
          actionLabel: "Send Instant Spec Clarification & Waiver",
          suggestedDiscount: "Waiver of Restocking Fee",
          channel: "Live In-Session Proactive Drawer"
        },
        {
          id: "rec-2",
          type: "Live Video Specialist Consultation",
          description: "Connect customer to hardware specialist via 1-click video or text chat.",
          expectedRecoveryRate: "74%",
          actionLabel: "Invite to Hardware Specialist Chat",
          suggestedDiscount: null,
          channel: "Live Chat"
        }
      ]
    }
  },
  {
    id: "CUST-9484",
    name: "Priya Sharma",
    email: "priya.s@gmail.com",
    avatar: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=120&auto=format&fit=crop&q=80",
    segment: "Promotional Target",
    cartValue: 78.50,
    device: "Android (Samsung Internet)",
    location: "San Jose, CA",
    journeyStage: "Promo Code Application",
    riskLevel: "Medium",
    riskScore: 68,
    frictionType: "Promo Code Failure & Rage Clicks",
    status: "Pending Action",
    timeElapsed: "21m ago",
    itemsInCart: [
      { name: "Hydrating Facial Cleanser & Serum Duo", price: 78.50, qty: 1, img: "🧴" }
    ],
    journeySteps: [
      {
        id: "step-1",
        stepNumber: 1,
        title: "Email Campaign Click",
        page: "/promos/festive20",
        dwellTime: "40s",
        timestamp: "11:10 AM",
        type: "navigation",
        sentiment: "positive",
        details: "Clicked promotional email offering 20% off with code FESTIVE20.",
        friction: false
      },
      {
        id: "step-2",
        stepNumber: 2,
        title: "Product Added to Cart",
        page: "/products/hydrating-duo",
        dwellTime: "1m 15s",
        timestamp: "11:11 AM",
        type: "action",
        sentiment: "positive",
        details: "Added to cart, proceed to checkout.",
        friction: false
      },
      {
        id: "step-3",
        stepNumber: 3,
        title: "Coupon Code 'FESTIVE20' Rejected",
        page: "/checkout",
        dwellTime: "1m 40s",
        timestamp: "11:13 AM",
        type: "error",
        sentiment: "frustrated",
        details: "System returned 'Code valid on orders over $80 only' (Current cart: $78.50).",
        friction: true,
        frictionAlert: "Promo code blocked by $1.50 minimum spend threshold"
      },
      {
        id: "step-4",
        stepNumber: 4,
        title: "Rage Clicks on Apply Button",
        page: "/checkout",
        dwellTime: "45s",
        timestamp: "11:14 AM",
        type: "error",
        sentiment: "critical",
        details: "Customer re-typed code in lowercase, clicked Apply 4 times in 2 seconds.",
        friction: true,
        frictionAlert: "Rage Clicks + Code rejection frustration"
      }
    ],
    aiAnalysis: {
      primaryCause: "Arbitrary $1.50 Threshold Gap on Promotional Campaign",
      category: "Promo Code Failure",
      confidence: 97,
      rootCauseSummary: "Email marketing team advertised 20% off without prominently disclosing $80 minimum spend. Cart value is $78.50. Rejecting code for a $1.50 deficit is causing high abandonment rate.",
      evidenceSignals: [
        { label: "Rule Rejection Log", value: "CouponRule: MIN_CART_VALUE = $80.00; CartActual = $78.50", severity: "high" },
        { label: "User Interaction", value: "4 rapid retries with capitalization variants", severity: "high" },
        { label: "Campaign Attributed", value: "Campaign ID: #EMAIL_FESTIVE_FALL", severity: "info" }
      ],
      recommendations: [
        {
          id: "rec-1",
          type: "Instant Threshold Waiver (Apply 20% Discount)",
          description: "Automatically bypass the $1.50 gap and apply 20% discount ($15.70 savings) right in the checkout form.",
          expectedRecoveryRate: "92%",
          actionLabel: "Auto-Apply FESTIVE20 ($15.70 off)",
          suggestedDiscount: "20% Discount Override",
          channel: "Checkout Banner"
        },
        {
          id: "rec-2",
          type: "1-Click Travel Size Cleanser ($4 Add-on)",
          description: "Offer a $4 mini travel cleanser to reach $82.50 total and activate promo legitimately.",
          expectedRecoveryRate: "76%",
          actionLabel: "Suggest $4 Mini Cleanser Add-on",
          suggestedDiscount: null,
          channel: "Checkout Modal"
        }
      ]
    }
  },
  {
    id: "CUST-9485",
    name: "Marcus Brody",
    email: "marcus.brody@nyu.edu",
    avatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=120&auto=format&fit=crop&q=80",
    segment: "Repeat Buyer",
    cartValue: 210.00,
    device: "iPad Pro (Safari)",
    location: "New York, NY",
    journeyStage: "Post-Purchase Support",
    riskLevel: "Medium",
    riskScore: 59,
    frictionType: "Tracking & Delivery Ambiguity",
    status: "Recovered",
    timeElapsed: "45m ago",
    itemsInCart: [
      { name: "Ergonomic Mesh Office Chair Cushion", price: 120.00, qty: 1, img: "💺" },
      { name: "Adjustable Footrest Platform", price: 90.00, qty: 1, img: "🪵" }
    ],
    journeySteps: [
      {
        id: "step-1",
        stepNumber: 1,
        title: "Order Placed 3 Days Ago",
        page: "/orders/ORD-88219",
        dwellTime: "25s",
        timestamp: "Yesterday",
        type: "action",
        sentiment: "positive",
        details: "Order placed for $210 with 3-day estimated delivery.",
        friction: false
      },
      {
        id: "step-2",
        stepNumber: 2,
        title: "Track Order Page Refreshes (5x)",
        page: "/track/ORD-88219",
        dwellTime: "2m 10s",
        timestamp: "10:30 AM",
        type: "interaction",
        sentiment: "frustrated",
        details: "Carrier tracking says 'Label Created - Awaiting Carrier Pickup' for 48 hours without update.",
        friction: true,
        frictionAlert: "Stagnant Carrier Status > 48h triggering anxiety"
      },
      {
        id: "step-3",
        stepNumber: 3,
        title: "Chat Bot Dead End",
        page: "/help/chat",
        dwellTime: "1m 30s",
        timestamp: "10:32 AM",
        type: "error",
        sentiment: "frustrated",
        details: "Bot gave generic automated answer: 'Your package is in transit'.",
        friction: true,
        frictionAlert: "Support loop deflection failure"
      }
    ],
    aiAnalysis: {
      primaryCause: "Carrier Scans Delayed at Regional Hub (USPS Jersey City)",
      category: "Delivery Uncertainty",
      confidence: 89,
      rootCauseSummary: "Tracking status stuck on 'Label Created' despite physical pickup. Customer refreshed tracking page 5 times and received unhelpful automated bot responses.",
      evidenceSignals: [
        { label: "Carrier Telemetry", value: "USPS scan backlog alert at Jersey City sorting hub", severity: "high" },
        { label: "Page Refreshes", value: "5 tracking refreshes in 15 minutes", severity: "medium" }
      ],
      recommendations: [
        {
          id: "rec-1",
          type: "Proactive Delivery Reassurance SMS + GPS ping",
          description: "Send direct SMS with verified hub arrival confirmation and $10 future credit for the delay anxiety.",
          expectedRecoveryRate: "95%",
          actionLabel: "Send Verified Tracking SMS + $10 Credit",
          suggestedDiscount: "$10 Store Credit",
          channel: "SMS"
        }
      ]
    }
  }
];

export const KPI_DATA = {
  sessionsMonitored: "42,850",
  sessionsGrowth: "+14.2% vs yesterday",
  frictionDetected: "1,842",
  frictionRate: "4.3% of traffic",
  revenueAtRisk: "$184,200",
  revenueAtRiskTrend: "-8.5% (Improving)",
  recoveredRevenue: "$129,500",
  recoveryRate: "70.3%",
  avgRecoveryTime: "1.8 mins",
  aiModelConfidence: "94.2%"
};

export const FUNNEL_DATA = [
  { stage: "Store Entry / Home", sessions: 42850, dropoff: 0, dropoffPct: "0%", frictionPoints: 120 },
  { stage: "Product View", sessions: 28400, dropoff: 14450, dropoffPct: "33.7%", frictionPoints: 340 },
  { stage: "Add to Cart", sessions: 11200, dropoff: 17200, dropoffPct: "60.5%", frictionPoints: 480 },
  { stage: "Initiate Checkout", sessions: 6900, dropoff: 4300, dropoffPct: "38.4%", frictionPoints: 390 },
  { stage: "Payment Step", sessions: 4100, dropoff: 2800, dropoffPct: "40.6%", frictionPoints: 450 },
  { stage: "Order Completed", sessions: 3350, dropoff: 750, dropoffPct: "18.3%", frictionPoints: 62 }
];

export const ROOT_CAUSES_BREAKDOWN = [
  { name: "Payment & 3DS Failures", count: 620, percentage: 34, color: "#ef4444" },
  { name: "Delivery & Shipping Uncertainty", count: 480, percentage: 26, color: "#f97316" },
  { name: "Promo / Coupon Invalidation", count: 330, percentage: 18, color: "#eab308" },
  { name: "Unclear Specs & Info Gaps", count: 260, percentage: 14, color: "#6366f1" },
  { name: "Return Policy & Hidden Fees", count: 152, percentage: 8, color: "#ec4899" }
];

export const RECOVERY_CHANNEL_STATS = [
  { channel: "1-Click Alternative Pay Link", attempts: 410, recovered: 352, rate: 85.8 },
  { channel: "In-App Friction Override Banner", attempts: 520, recovered: 426, rate: 81.9 },
  { channel: "Proactive WhatsApp VIP Assist", attempts: 290, recovered: 218, rate: 75.1 },
  { channel: "Dynamic Shipping Waiver Toast", attempts: 380, recovered: 285, rate: 75.0 },
  { channel: "Post-Drop Email Sequence", attempts: 242, recovered: 124, rate: 51.2 }
];

export const HOURLY_FRICTION_TREND = [
  { hour: "06:00", friction: 38, recovered: 25 },
  { hour: "08:00", friction: 65, recovered: 48 },
  { hour: "10:00", friction: 142, recovered: 104 },
  { hour: "12:00", friction: 198, recovered: 145 },
  { hour: "14:00", friction: 175, recovered: 130 },
  { hour: "16:00", friction: 210, recovered: 158 },
  { hour: "18:00", friction: 245, recovered: 182 },
  { hour: "20:00", friction: 190, recovered: 142 },
  { hour: "22:00", friction: 110, recovered: 85 }
];
