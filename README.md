


# 🛡️ Incident Response Automation (MXDR Simulation)

Automating Detection → Contextual Response → Notification for Cybersecurity Operations

👤 **Author:** Abhijay Nair
*Cybersecurity Lead | GRC & Incident Response | Security Automation Engineer*

## 🧩 Overview
This project simulates a real-world **Security Operations Center (SOC)** automation pipeline, heavily inspired by modern **MXDR (Managed Extended Detection and Response)** methodologies. It demonstrates how a security team can:
* **Detect** threats across endpoints and cloud environments.
* **Assess** severity using contextual and asset-criticality awareness to reduce false positives.
* **Respond** with automated containment (e.g., isolating hosts via EDR).
* **Notify** and log actions securely for analyst review.

It bridges technical execution (Python automation, DevSecOps) with leadership-level visibility (incident reporting, risk triage, audit trail creation).

## 🧱 Project Architecture
```text
incident-response-automation/
│
├── scanners/               → Simulated telemetry (Microsoft Sentinel, Defender for Endpoint APIs)
├── alerts/                 → Normalization & alert parsing engine
├── automation/             → Response playbooks & conditional logic
├── reports/                → Generated JSON artifacts and audit logs
├── .github/workflows/      → CI pipeline for GitHub Actions
│
├── config.py               → Secure environment variable loader
├── main.py                 → Orchestrator for detection → response → notify
├── requirements.txt        → Dependencies
├── .gitignore              → Excludes .env & secrets
└── README.md
```

Each folder mirrors how enterprise SOC teams organize automation pipelines, ensuring scalability and strict auditability.

## 🚨 Phase 1 – Telemetry Ingestion & Normalization
**Goal:** Simulate an enterprise SIEM/EDR ingestion workflow.

✅ **Key Features**
* **Simulated Microsoft Stack:** Parses mock logs simulating Microsoft Defender for Endpoint (MDE) and generic network scanners.
* **Secure Configuration:** All API keys and tokens handled securely via `.env` (never pushed to Git).
* **Target Discovery:** Dynamically loads asset targets from configuration.

**Output:** `🗂️ reports/alerts.json` – Normalized threat findings transformed into a unified schema for the response engine.

## ⚙️ Phase 2 – Context-Aware Response
**Goal:** Automate triage, containment, and communication while avoiding "alert fatigue."

🧠 **Logic Flow**
1. **Parse Findings:** Converts raw telemetry into structured actionable data.
2. **Respond Intelligently (Playbooks):**
   * **High Severity:** Trigger automated containment (e.g., Host Quarantine), revoke identity tokens, alert IR Lead. *(Note: Logic checks asset criticality to ensure 'Tier 0' servers are not auto-quarantined).*
   * **Medium Severity:** Open remediation ticket, schedule patch review.
   * **Low Severity:** Suppress immediate alerts; log to SIEM for behavioral tracking.
3. **Notify Channels:**
   * Console summary (Local execution).
   * Secure Webhook framework configured for future ChatOps deployment.

**Example Execution Output:**
```text
=== INCIDENT RESPONSE AUTOMATION: PHASE 2 ===
[+] Configuration loaded via secure environment.
[Microsoft Defender VM] Scanning internal network...

--- Alerts for WIN-SRV-FINANCE-01 ---
[High] Suspicious PowerShell execution detected
[Medium] Missing security patch

[+] Wrote normalized alerts -> reports/alerts.json
[+] Executing Playbooks -> Host Isolated (WIN-SRV-FINANCE-01)
[+] Summary: {'High': 1, 'Medium': 1, 'Low': 0}
[i] Webhook framework ready for Microsoft Teams integration (Phase 3).
```

## 🧰 Technologies Used
| Category | Tools & Frameworks |
| :--- | :--- |
| **Language** | Python 3.11 |
| **Automation** | PowerShell, GitHub Actions |
| **Simulated Stack** | Microsoft Sentinel, Defender for Endpoint (MDE), Qualys |
| **Reporting** | JSON, Markdown, Audit Logging |
| **Secrets Mgmt** | `.env` + `.gitignore` |

## 🧠 Key Skills Demonstrated
| Domain | Capability |
| :--- | :--- |
| **Incident Response** | Automated containment workflows & playbook execution |
| **Threat Triage** | Cross-platform alert normalization and context-aware severity mapping |
| **Security Engineering**| Modular architecture mimicking modern SOAR platforms |
| **DevSecOps** | CI/CD with GitHub Actions for automated testing |
| **Leadership** | Translating IR playbooks into code-driven governance |

## 🧩 Future Enhancements
| Phase | Description |
| :--- | :--- |
| **Phase 3 (ChatOps)** | Wire existing webhook logic into **Microsoft Teams** to push critical alert summaries directly to the SOC channel, enabling real-time analyst collaboration. |
| **Phase 4 (AI Triage)** | Integrate **LLM APIs (Agentic AI)** to automatically summarize alerts and generate "Conviction Scores" before human review to drastically reduce MTTI. |
| **Phase 5 (Cloud)** | Deepen Azure/Entra ID API integration for conditional access response. |

## 👨‍💼 Professional Summary
This repository demonstrates a foundational understanding of modern cybersecurity automation—merging policy, detection, and response under a unified framework. By modeling an environment that prioritizes **Microsoft integrations, context-aware logic, and an AI-ready architecture**, it showcases how manual SOC tasks can evolve into scalable, automated defense systems.
```

---
