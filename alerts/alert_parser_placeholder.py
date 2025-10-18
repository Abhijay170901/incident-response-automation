class AlertParser:
    def parse(self, scan_result):
        alerts = []
        for issue in scan_result.get("issues", []):
            alerts.append({
                "target": scan_result["target"],
                "risk": issue.get("risk", "Unknown"),
                "description": issue.get("description", ""),
                "tool": scan_result.get("scanner", "Unknown")
            })
        return alerts
