import json
from pathlib import Path

class AlertParser:
    def parse(self, scan_result):
        alerts = []
        for issue in scan_result.get("issues", []):
            alerts.append({
                "target": scan_result["target"],
                "risk": issue.get("risk", "Unknown"),
                "description": issue.get("description", ""),
                "tool": scan_result.get("scanner", "Unknown"),
            })
        return alerts

def save_alerts(all_alerts, outfile="reports/alerts.json"):
    Path("reports").mkdir(parents=True, exist_ok=True)
    with open(outfile, "w", encoding="utf-8") as f:
        json.dump(all_alerts, f, indent=2)
    print(f"[+] Wrote normalized alerts -> {outfile}")
