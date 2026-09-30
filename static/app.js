/**
 * AI Customer Journey Friction Detection & Recovery Assistant
 * Dashboard Frontend Controller
 * College Project - Team Member 4
 */

const QUICK_SCENARIOS = [
  { id: "CUST-1004", label: "Repeated Payment Fail", severity: "critical", badge: "badge-critical" },
  { id: "CUST-1001", label: "Smooth Purchase", severity: "none", badge: "badge-none" },
  { id: "CUST-1002", label: "Cart Abandonment", severity: "medium", badge: "badge-high" },
  { id: "CUST-1003", label: "Payment Timeout", severity: "high", badge: "badge-high" },
  { id: "CUST-1005", label: "Delivery Delay", severity: "high", badge: "badge-high" },
  { id: "CUST-1006", label: "Support Complaint", severity: "critical", badge: "badge-critical" },
  { id: "CUST-1007", label: "Negative Feedback", severity: "high", badge: "badge-high" },
  { id: "CUST-1008", label: "Product Confusion", severity: "medium", badge: "badge-high" },
  { id: "CUST-1009", label: "High Browsing", severity: "medium", badge: "badge-high" },
  { id: "CUST-1010", label: "Recovered Journey", severity: "low", badge: "badge-none" },
];

let currentCustomerData = null;
let activeTab = "ordersTab";

document.addEventListener("DOMContentLoaded", () => {
  initSummary();
  initScenarioChips();
  initCustomerDropdown();
  setupEventListeners();
  
  // Default select Scenario 4: CUST-1004 (Repeated Payment Failure)
  setTimeout(() => selectCustomer("CUST-1004"), 300);
});

async function initSummary() {
  try {
    const res = await fetch("/api/summary");
    const data = await res.json();
    document.getElementById("totalCustomers").innerText = data.total_customers;
    document.getElementById("totalEvents").innerText = data.total_journey_events;
    document.getElementById("totalOrders").innerText = data.total_orders;
  } catch (err) {
    console.error("Failed to load summary metrics:", err);
  }
}

function initScenarioChips() {
  const container = document.getElementById("scenarioChips");
  container.innerHTML = "";
  QUICK_SCENARIOS.forEach((sc) => {
    const chip = document.createElement("button");
    chip.className = `chip ${sc.badge}`;
    chip.id = `chip-${sc.id}`;
    chip.innerText = `${sc.id} (${sc.label})`;
    chip.addEventListener("click", () => selectCustomer(sc.id));
    container.appendChild(chip);
  });
}

async function initCustomerDropdown() {
  try {
    const res = await fetch("/api/customers");
    const customers = await res.json();
    const select = document.getElementById("customerSelect");
    select.innerHTML = "";
    
    customers.forEach((c) => {
      const opt = document.createElement("option");
      opt.value = c.customer_id;
      const statusIcon = c.friction_detected ? `⚠️ [${c.severity}]` : "✅ [CLEAN]";
      opt.innerText = `${c.customer_id} - ${c.name} (${c.segment}) ${statusIcon}`;
      select.appendChild(opt);
    });

    select.addEventListener("change", (e) => {
      if (e.target.value) {
        selectCustomer(e.target.value);
      }
    });
  } catch (err) {
    console.error("Failed to load customer list:", err);
  }
}

function setupEventListeners() {
  // Refresh button
  document.getElementById("refreshBtn").addEventListener("click", () => {
    const cur = document.getElementById("customerSelect").value;
    if (cur) selectCustomer(cur);
  });

  // Tab buttons
  document.querySelectorAll(".tab-btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
      document.querySelectorAll(".tab-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      activeTab = btn.getAttribute("data-tab");
      renderTabDetails();
    });
  });

  // Simulate intervention dispatch
  document.getElementById("dispatchInterventionBtn").addEventListener("click", () => {
    showToast("Automated Recovery Intervention Dispatched via Omnichannel Orchestrator!");
  });

  // Run test suite modal triggers
  const modal = document.getElementById("testModal");
  document.getElementById("runTestsBtn").addEventListener("click", runLiveTests);
  document.getElementById("closeModalBtn").addEventListener("click", () => modal.classList.remove("open"));
  document.getElementById("modalCloseBtn").addEventListener("click", () => modal.classList.remove("open"));
}

async function selectCustomer(customerId) {
  // Update chip active states
  document.querySelectorAll(".chip").forEach((c) => c.classList.remove("active"));
  const activeChip = document.getElementById(`chip-${customerId}`);
  if (activeChip) activeChip.classList.add("active");

  // Sync select dropdown
  const select = document.getElementById("customerSelect");
  if (select.value !== customerId) {
    select.value = customerId;
  }

  // Fetch full details and analysis concurrently
  try {
    const [detailRes, analysisRes] = await Promise.all([
      fetch(`/api/customer/${customerId}`),
      fetch(`/api/customer/${customerId}/analyze`),
    ]);

    const details = await detailRes.json();
    const analysis = await analysisRes.json();

    currentCustomerData = details;

    renderCustomerProfile(details.profile);
    renderAIAnalysis(analysis);
    renderJourneyTimeline(details.events);
    renderContextTabs(details);
  } catch (err) {
    console.error(`Error loading customer ${customerId}:`, err);
  }
}

function renderCustomerProfile(profile) {
  document.getElementById("profileId").innerText = profile.customer_id;
  document.getElementById("profileName").innerText = profile.name;
  document.getElementById("profileEmail").innerText = profile.email;
  document.getElementById("profilePay").innerText = profile.preferred_payment_method;
  document.getElementById("profileOrders").innerText = profile.total_lifetime_orders;
  document.getElementById("profileCreated").innerText = profile.created_at;
  document.getElementById("customerSegmentBadge").innerText = profile.segment;
}

function renderAIAnalysis(analysis) {
  const statusTag = document.getElementById("frictionStatusTag");
  if (analysis.friction_detected) {
    statusTag.innerText = `Friction: ${analysis.friction_category}`;
    statusTag.className = `status-tag status-${analysis.severity.toLowerCase()}`;
  } else {
    statusTag.innerText = "Journey Healthy (No Friction)";
    statusTag.className = "status-tag status-none";
  }

  document.getElementById("aiCategory").innerText = analysis.friction_category;
  document.getElementById("aiSeverity").innerText = analysis.severity;
  
  const pct = Math.round(analysis.confidence * 100);
  document.getElementById("aiConfidence").innerText = `${pct}%`;
  document.getElementById("confidencePct").innerText = `${pct}%`;
  document.getElementById("confidenceFill").style.width = `${pct}%`;

  document.getElementById("aiRootCause").innerText = analysis.root_cause;
  document.getElementById("aiEvidence").innerText = analysis.evidence;

  // Recovery card
  document.getElementById("recoveryText").innerText = analysis.recommended_recovery_action;
  document.getElementById("actionTypeBadge").innerText = analysis.action_type || "RECOVERY_ACTION";
}

function renderJourneyTimeline(events) {
  const container = document.getElementById("timelineContainer");
  document.getElementById("eventCountBadge").innerText = `${events.length} Events`;

  if (!events || events.length === 0) {
    container.innerHTML = '<div class="timeline-empty">No events recorded for this customer.</div>';
    return;
  }

  container.innerHTML = "";
  events.forEach((ev) => {
    const item = document.createElement("div");
    item.className = "timeline-item";

    let dotClass = "";
    if (ev.event_type.includes("failed") || ev.event_type.includes("exit")) dotClass = "danger";
    else if (ev.event_type.includes("success") || ev.event_type.includes("placed")) dotClass = "success";
    else if (ev.event_type.includes("recovery") || ev.event_type.includes("tracking")) dotClass = "warning";

    let metaDisplay = "";
    if (ev.metadata) {
      try {
        const m = JSON.parse(ev.metadata);
        metaDisplay = Object.entries(m).map(([k, v]) => `${k}: ${v}`).join(" | ");
      } catch (e) {
        metaDisplay = ev.metadata;
      }
    }

    item.innerHTML = `
      <div class="timeline-dot ${dotClass}"></div>
      <div class="timeline-content">
        <div class="timeline-header">
          <span class="event-type">${formatEventType(ev.event_type)}</span>
          <span class="event-time">${ev.timestamp}</span>
        </div>
        <div>
          <span class="muted">${ev.page_url}</span>
          ${ev.dwell_time_seconds > 0 ? `<span class="dwell-badge">⏱️ ${ev.dwell_time_seconds}s</span>` : ""}
        </div>
        ${metaDisplay ? `<div class="event-meta">ℹ️ ${metaDisplay}</div>` : ""}
      </div>
    `;
    container.appendChild(item);
  });
}

function formatEventType(type) {
  return type.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
}

function renderContextTabs(details) {
  document.getElementById("ordersCount").innerText = (details.orders || []).length;
  document.getElementById("paymentsCount").innerText = (details.payments || []).length;
  document.getElementById("ticketsCount").innerText = (details.tickets || []).length;
  document.getElementById("feedbackCount").innerText = (details.feedback || []).length;
  renderTabDetails();
}

function renderTabDetails() {
  const container = document.getElementById("tabDetails");
  if (!currentCustomerData) {
    container.innerHTML = "<p class='muted'>No customer data.</p>";
    return;
  }

  let html = "";
  if (activeTab === "ordersTab") {
    const orders = currentCustomerData.orders || [];
    if (orders.length === 0) html = "<p class='muted'>No orders recorded for this customer.</p>";
    else {
      html = orders.map((o) => `
        <div class="entity-row">
          <div><strong>${o.order_id}</strong> - Product: ${o.product_id} ($${o.total_amount})</div>
          <div><span class="badge ${o.order_status === 'delivered' ? 'status-none' : o.order_status === 'payment_failed' ? 'status-critical' : 'status-high'}">${o.order_status}</span></div>
        </div>
      `).join("");
    }
  } else if (activeTab === "paymentsTab") {
    const payments = currentCustomerData.payments || [];
    if (payments.length === 0) html = "<p class='muted'>No payment transactions recorded.</p>";
    else {
      html = payments.map((p) => `
        <div class="entity-row">
          <div><strong>${p.payment_id}</strong> - ${p.payment_method} ($${p.amount}) [Attempt #${p.attempt_number}]</div>
          <div><span class="badge ${p.payment_status === 'success' ? 'status-none' : 'status-critical'}">${p.payment_status}</span> ${p.error_code ? `(${p.error_code})` : ''}</div>
        </div>
      `).join("");
    }
  } else if (activeTab === "ticketsTab") {
    const tickets = currentCustomerData.tickets || [];
    if (tickets.length === 0) html = "<p class='muted'>No support tickets filed.</p>";
    else {
      html = tickets.map((t) => `
        <div class="entity-row">
          <div><strong>${t.ticket_id}</strong>: ${t.subject}</div>
          <div><span class="badge status-critical">${t.priority} / ${t.status}</span></div>
        </div>
      `).join("");
    }
  } else if (activeTab === "feedbackTab") {
    const feedbacks = currentCustomerData.feedback || [];
    if (feedbacks.length === 0) html = "<p class='muted'>No reviews or ratings submitted.</p>";
    else {
      html = feedbacks.map((f) => `
        <div class="entity-row">
          <div><strong>${'⭐'.repeat(f.rating)}</strong> - "${f.review_title}": ${f.review_text}</div>
          <div><span class="badge ${f.rating >= 4 ? 'status-none' : 'status-critical'}">${f.sentiment}</span></div>
        </div>
      `).join("");
    }
  }

  container.innerHTML = html;
}

async function runLiveTests() {
  const modal = document.getElementById("testModal");
  const summaryEl = document.getElementById("testModalSummary");
  const terminal = document.getElementById("testTerminalOutput");

  modal.classList.add("open");
  summaryEl.innerText = "Running 13 automated scenario & data consistency tests...";
  terminal.innerText = "Executing unittest runner...\n";

  try {
    const res = await fetch("/api/run-tests");
    const data = await res.json();

    if (data.was_successful) {
      summaryEl.innerHTML = `✅ <strong style="color: #10b981;">ALL ${data.tests_run} TESTS PASSED SUCCESSFULLY (0 Failures, 0 Errors)</strong>`;
    } else {
      summaryEl.innerHTML = `❌ <strong style="color: #ef4444;">${data.failures} Failures, ${data.errors} Errors detected</strong>`;
    }

    terminal.innerText = data.output_log;
  } catch (err) {
    terminal.innerText = "Error executing tests: " + err.message;
  }
}

function showToast(msg) {
  const toast = document.getElementById("toast");
  toast.innerText = msg;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 3500);
}
