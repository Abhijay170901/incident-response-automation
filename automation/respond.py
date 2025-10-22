import json
from pathlib import Path

ACTIONS = {
    "High": [
        "Quarantine host (simulated)",
        "Revoke tokens/keys (simulated)",
        "Notify IR on-call (simulated)"
    ],
    "Medium": [
        "Open remediation ticket (simulated)",
        "Schedule patching within SLA (simulated)"
    ],
    "Low": [
        "Log and monitor (simulated)"
    ],
}

def load_alerts(path="reports/alerts.json"):
    p = Path(path)
    if not p.exists():
        print(f"[!] No alerts file found at {path}")
        return []
    return json.loads(p.read_text(encoding="utf-8"))

def respond_to_alerts(alerts):
    summary = {"High":0, "Medium":0, "Low":0, "Unknown":0}
    actions_taken = []

    for a in alerts:
        risk = a.get("risk", "Unknown")
        summary[risk] = summary.get(risk, 0) + 1

        for action in ACTIONS.get(risk, ["Log only (simulated)"]):
            actions_taken.append({
                "target": a["target"],
                "tool": a["tool"],
                "risk": risk,
                "action": action,
                "description": a["description"]
            })

    Path("reports").mkdir(parents=True, exist_ok=True)
    with open("reports/response_log.json", "w", encoding="utf-8") as f:
        json.dump({
            "summary": summary,
            "actions": actions_taken
        }, f, indent=2)
    print("[+] Response actions logged -> reports/response_log.json")
    print(f"[+] Summary: {summary}")
    return summary, actions_taken
